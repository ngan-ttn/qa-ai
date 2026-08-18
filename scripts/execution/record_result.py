"""Append one immutable execution result attempt to a QA-AI run."""
from __future__ import annotations
import argparse, json
from datetime import datetime, timezone
from pathlib import Path
STATUSES={"Pass","Fail","Blocked","Not Run","Not Applicable"}
BLOCKERS={"Environment","Test Data","Access","Dependency","Requirement / Oracle","Other"}
def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
def load(path): return json.loads(path.read_text(encoding="utf-8"))
def save(path,data): path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("run_path"); ap.add_argument("test_case_id"); ap.add_argument("status",choices=sorted(STATUSES))
    ap.add_argument("--actual-result"); ap.add_argument("--executed-by"); ap.add_argument("--notes")
    ap.add_argument("--blocker-type",choices=sorted(BLOCKERS)); ap.add_argument("--blocker-reason")
    ap.add_argument("--evidence-type",choices=["screenshot","video","log","request-response","database","other"])
    ap.add_argument("--evidence-path"); ap.add_argument("--evidence-description")
    args=ap.parse_args(); run_dir=Path(args.run_path).resolve(); run_p=run_dir/"execution.json"; res_p=run_dir/"results.json"
    if not run_p.is_file() or not res_p.is_file(): print("ERROR execution.json/results.json not found"); return 1
    run=load(run_p); results=load(res_p)
    if run.get("status")=="Closed": print("ERROR Closed execution runs are immutable"); return 1
    if args.test_case_id not in run.get("scope_testcase_ids",[]): print("ERROR testcase is not in execution scope"); return 1
    if args.status=="Blocked" and (not args.blocker_type or not args.blocker_reason): print("ERROR Blocked requires --blocker-type and --blocker-reason"); return 1
    if args.status!="Blocked" and (args.blocker_type or args.blocker_reason): print("ERROR blocker fields are valid only for Blocked results"); return 1
    existing=results.get("results",[]); nums=[]
    for item in existing:
        rid=item.get("execution_result_id","")
        if rid.startswith("ER-") and rid[3:].isdigit(): nums.append(int(rid[3:]))
    rid=f"ER-{(max(nums,default=0)+1):04d}"; ts=now(); evidence=[]
    if args.evidence_type or args.evidence_path:
        if not args.evidence_type or not args.evidence_path: print("ERROR evidence requires both --evidence-type and --evidence-path"); return 1
        evidence=[{"evidence_id":f"EV-{rid[3:]}","type":args.evidence_type,"path":args.evidence_path,"description":args.evidence_description}]
    record={"execution_result_id":rid,"test_case_id":args.test_case_id,"status":args.status,"actual_result":args.actual_result,"executed_by":args.executed_by or run.get("executor"),"executed_at":ts,"environment":run.get("environment"),"build":run.get("build"),"evidence":evidence,"defect_ids":[],"notes":args.notes,"retest_of":None,"blocker_type":args.blocker_type,"blocker_reason":args.blocker_reason}
    existing.append(record); results["results"]=existing; save(res_p,results)
    if run.get("status")=="Planned": run["status"]="In Progress"
    run["updated_at"]=ts; save(run_p,run)
    print(f"Recorded {rid}: {args.test_case_id} -> {args.status}"); return 0
if __name__=="__main__": raise SystemExit(main())
