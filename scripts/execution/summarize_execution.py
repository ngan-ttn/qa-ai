"""Derive current testcase dispositions, summary, and optionally close a completed run."""
from __future__ import annotations
import argparse, json
from datetime import datetime, timezone
from pathlib import Path
STATUSES=["Pass","Fail","Blocked","Not Run","Not Applicable"]
def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def save(p,d): p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
def main()->int:
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("run_path"); ap.add_argument("--close",action="store_true"); args=ap.parse_args(); d=Path(args.run_path).resolve()
    rp=d/"execution.json"; xp=d/"results.json"
    if not rp.is_file() or not xp.is_file(): print("ERROR execution files missing"); return 1
    run=load(rp); results=load(xp).get("results",[]); latest={}
    for item in results: latest[item["test_case_id"]]=item
    dispositions={tc:(latest[tc]["status"] if tc in latest else "Not Run") for tc in run.get("scope_testcase_ids",[])}
    counts={s:sum(1 for v in dispositions.values() if v==s) for s in STATUSES}; total=len(dispositions)
    if sum(counts.values())!=total: print("ERROR disposition counts do not reconcile"); return 1
    ts=now()
    if run.get("status")!="Closed":
        if counts["Not Run"]==0:
            run["status"]="Completed"; run["completed_at"]=run.get("completed_at") or ts
        elif results: run["status"]="In Progress"
        else: run["status"]="Planned"
        if args.close:
            if run["status"]!="Completed": print("ERROR only a Completed run can be closed"); return 1
            run["status"]="Closed"; run["closed_at"]=ts
        run["updated_at"]=ts; save(rp,run)
    elif args.close:
        print("Run is already Closed.")
    lines=[f"# Execution Summary — {run['execution_id']}","",f"- Status: `{run['status']}`",f"- Scope Type: `{run['scope_type']}`",f"- Feature Revision: `{run['feature_revision']}`",f"- Environment: `{run.get('environment') or '—'}`",f"- Build: `{run.get('build') or '—'}`","","## Current Disposition Summary","","| Status | Count |","|---|---:|"]
    for s in STATUSES: lines.append(f"| {s} | {counts[s]} |")
    lines += [f"| **Total** | **{total}** |","","## Current Testcase Dispositions","","| Test Case ID | Status | Latest Result ID | Defect IDs |","|---|---|---|---|"]
    for tc in run.get("scope_testcase_ids",[]):
        item=latest.get(tc); lines.append(f"| {tc} | {dispositions[tc]} | {item.get('execution_result_id','—') if item else '—'} | {', '.join(item.get('defect_ids',[])) if item and item.get('defect_ids') else '—'} |")
    lines += ["","## Reconciliation","",f"`Pass + Fail + Blocked + Not Run + Not Applicable = {sum(counts.values())} = {total} unique scoped testcase IDs.`",""]
    (d/"Execution-Summary.md").write_text("\n".join(lines),encoding="utf-8")
    print(f"Execution summary: total={total} Pass={counts['Pass']} Fail={counts['Fail']} Blocked={counts['Blocked']} Not Run={counts['Not Run']} Not Applicable={counts['Not Applicable']}")
    print(f"Run status: {run['status']}"); return 0
if __name__=="__main__": raise SystemExit(main())
