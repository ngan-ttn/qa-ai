"""Initialize a QA-AI execution run from canonical Test Cases."""
from __future__ import annotations
import argparse, hashlib, json, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
EXPORT = ROOT / "scripts" / "export"
if str(EXPORT) not in sys.path: sys.path.insert(0, str(EXPORT))
from parse_testcases import parse as parse_testcases
from parse_regression import parse as parse_regression

TIERS = {
    "Minimum / Release-Gate Regression": "minimum_release_gate",
    "Recommended Regression": "recommended",
    "Full Changed-Feature Verification": "full_changed_feature",
}

def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def git_rev():
    try: return subprocess.check_output(["git","rev-parse","HEAD"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception: return "unknown"
def resolve(path: str, base: Path | None = None) -> Path:
    p = Path(path)
    if p.is_absolute(): return p
    if base and (base / p).exists(): return (base / p).resolve()
    return (ROOT / p).resolve()

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("feature_path")
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--scope-type", required=True, choices=["Full Test Suite", *TIERS.keys(), "Custom"])
    ap.add_argument("--testcases", default="artifacts/Test-Cases.md")
    ap.add_argument("--testcase-id", action="append", default=[])
    ap.add_argument("--regression-source")
    ap.add_argument("--environment")
    ap.add_argument("--build")
    ap.add_argument("--executor")
    ap.add_argument("--allow-stale", action="store_true")
    ap.add_argument("--reason")
    args = ap.parse_args()
    if not args.run_id.startswith("RUN-"):
        print("ERROR run ID must start with RUN-"); return 1
    feature = resolve(args.feature_path)
    meta_path = feature / "metadata.json"
    if not meta_path.is_file(): print(f"ERROR feature metadata not found: {meta_path}"); return 1
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    tc_path = resolve(args.testcases, feature)
    if not tc_path.is_file(): print(f"ERROR testcase artifact not found: {tc_path}"); return 1
    model = parse_testcases(tc_path)
    all_ids = [r["test_case_id"] for r in model["records"]]
    freshness = meta.get("artifacts",{}).get("test-cases",{}).get("freshness","Unknown")
    if freshness == "Stale" and not args.allow_stale:
        print("ERROR testcase artifact is Stale; use --allow-stale --reason <reason> only for an explicit audited override"); return 1
    if freshness in {"Stale","Unknown"} and args.allow_stale and not args.reason:
        print("ERROR --allow-stale requires --reason"); return 1
    regression_meta = None
    if args.scope_type == "Full Test Suite": scope = all_ids
    elif args.scope_type == "Custom": scope = args.testcase_id
    else:
        if not args.regression_source:
            print("ERROR regression scope type requires --regression-source"); return 1
        reg_path = resolve(args.regression_source, feature)
        reg = parse_regression(reg_path)
        scope = [x for x in reg["tiers"][TIERS[args.scope_type]] if x.startswith("TC-")]
        regression_meta = {"path": reg_path.as_posix(), "checksum": sha(reg_path), "tier": args.scope_type}
    scope = list(dict.fromkeys(scope))
    if not scope: print("ERROR execution scope is empty"); return 1
    unknown = [x for x in scope if x not in set(all_ids)]
    if unknown: print(f"ERROR scoped testcase IDs not found in source: {unknown}"); return 1
    run_dir = feature / "executions" / args.run_id
    if run_dir.exists(): print(f"ERROR execution run already exists: {run_dir}"); return 1
    (run_dir / "evidence").mkdir(parents=True)
    ts = now()
    run = {
        "schema_version":"1.0", "execution_id":args.run_id,
        "feature_revision":meta.get("current_revision"), "status":"Planned",
        "scope_type":args.scope_type, "scope_testcase_ids":scope,
        "testcase_source":{"path":tc_path.as_posix(),"checksum":sha(tc_path),"artifact_revision":meta.get("artifacts",{}).get("test-cases",{}).get("revision"),"freshness":freshness},
        "regression_source":regression_meta, "build":args.build, "environment":args.environment,
        "executor":args.executor, "allow_stale":bool(args.allow_stale), "override_reason":args.reason,
        "created_at":ts, "updated_at":ts, "completed_at":None, "closed_at":None,
        "framework_revision":git_rev(),
    }
    (run_dir/"execution.json").write_text(json.dumps(run,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    (run_dir/"results.json").write_text(json.dumps({"schema_version":"1.0","execution_id":args.run_id,"results":[]},indent=2)+"\n",encoding="utf-8")
    (run_dir/"defects.json").write_text(json.dumps({"schema_version":"1.0","execution_id":args.run_id,"defects":[]},indent=2)+"\n",encoding="utf-8")
    print(f"Initialized execution: {run_dir.relative_to(ROOT)}")
    print(f"Scope: {len(scope)} unique testcase(s); status=Planned; testcase freshness={freshness}")
    return 0
if __name__ == "__main__": raise SystemExit(main())
