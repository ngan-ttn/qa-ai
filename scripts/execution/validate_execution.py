"""Validate a QA-AI execution run for scope, provenance, history, defects, and count integrity."""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; EXPORT=ROOT/"scripts"/"export"
if str(EXPORT) not in sys.path: sys.path.insert(0,str(EXPORT))
from parse_testcases import parse as parse_testcases
STATUSES={"Pass","Fail","Blocked","Not Run","Not Applicable"}
BLOCKERS={"Environment","Test Data","Access","Dependency","Requirement / Oracle","Other"}
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main()->int:
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("run_path"); args=ap.parse_args(); d=Path(args.run_path).resolve(); errors=[]
    rp,xp,dp=d/"execution.json",d/"results.json",d/"defects.json"
    if not all(p.is_file() for p in (rp,xp,dp)):
        print("ERROR required execution files missing"); return 1
    run,results,defects=load(rp),load(xp),load(dp)
    scope=run.get("scope_testcase_ids",[])
    if not scope or len(scope)!=len(set(scope)): errors.append("scope testcase IDs must be non-empty and unique")
    tc_source=Path(run.get("testcase_source",{}).get("path","") )
    if not tc_source.is_absolute(): tc_source=(ROOT/tc_source).resolve()
    if not tc_source.is_file(): errors.append("referenced testcase source does not exist")
    else:
        if sha(tc_source)!=run.get("testcase_source",{}).get("checksum"): errors.append("testcase source checksum mismatch")
        try:
            ids={r["test_case_id"] for r in parse_testcases(tc_source)["records"]}
            missing=[x for x in scope if x not in ids]
            if missing: errors.append(f"scoped testcase IDs missing from source: {missing}")
        except Exception as exc: errors.append(f"testcase source parse failed: {exc}")
    items=results.get("results",[]); result_ids=[]; by_id={}; latest={}
    for item in items:
        rid=item.get("execution_result_id"); tc=item.get("test_case_id"); st=item.get("status")
        if rid in by_id: errors.append(f"duplicate execution result ID: {rid}")
        if not isinstance(rid,str) or not rid.startswith("ER-"): errors.append(f"invalid execution result ID: {rid}")
        if tc not in scope: errors.append(f"result references testcase outside scope: {tc}")
        if st not in STATUSES: errors.append(f"invalid execution status for {rid}: {st}")
        if st=="Blocked":
            if item.get("blocker_type") not in BLOCKERS or not item.get("blocker_reason"): errors.append(f"Blocked result missing valid blocker evidence: {rid}")
        elif item.get("blocker_type") or item.get("blocker_reason"): errors.append(f"non-Blocked result has blocker fields: {rid}")
        by_id[rid]=item; result_ids.append(rid); latest[tc]=item
    for item in items:
        prior=item.get("retest_of")
        if prior:
            if prior not in by_id: errors.append(f"broken retest reference: {item.get('execution_result_id')} -> {prior}")
            elif by_id[prior].get("test_case_id")!=item.get("test_case_id"): errors.append(f"retest testcase mismatch: {item.get('execution_result_id')}")
    defect_ids=set()
    for defect in defects.get("defects",[]):
        did=defect.get("defect_id")
        if did in defect_ids: errors.append(f"duplicate defect ID: {did}")
        defect_ids.add(did)
        for rid in defect.get("source_execution_result_ids",[]):
            if rid not in by_id: errors.append(f"defect {did} references missing result {rid}")
            elif did not in by_id[rid].get("defect_ids",[]): errors.append(f"defect/result linkage not reciprocal: {did} / {rid}")
    for item in items:
        for did in item.get("defect_ids",[]):
            if did not in defect_ids: errors.append(f"result {item.get('execution_result_id')} references missing defect {did}")
    dispositions={tc:(latest[tc]["status"] if tc in latest else "Not Run") for tc in scope}
    counts={s:sum(1 for v in dispositions.values() if v==s) for s in STATUSES}
    if sum(counts.values())!=len(scope): errors.append("current disposition counts do not reconcile with unique scope")
    status=run.get("status")
    if status=="Completed" and counts["Not Run"]>0: errors.append("Completed run still has Not Run testcase(s)")
    if status=="Closed" and not run.get("closed_at"): errors.append("Closed run requires closed_at")
    if run.get("testcase_source",{}).get("freshness")=="Stale" and not run.get("allow_stale"): errors.append("Stale testcase execution lacks explicit allow_stale override")
    if run.get("allow_stale") and not run.get("override_reason"): errors.append("stale/unknown override lacks reason")
    if errors:
        for e in errors: print(f"ERROR {e}")
        print(f"Execution validation failed; issues={len(errors)}"); return 1
    print(f"PASS execution validation: {d}")
    print(f"Scope={len(scope)} attempts={len(items)} Pass={counts['Pass']} Fail={counts['Fail']} Blocked={counts['Blocked']} Not Run={counts['Not Run']} Not Applicable={counts['Not Applicable']}")
    return 0
if __name__=="__main__": raise SystemExit(main())
