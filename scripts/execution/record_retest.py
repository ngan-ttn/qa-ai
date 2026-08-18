"""Append a retest attempt linked to an earlier result for the same testcase."""
from __future__ import annotations
import argparse, json
from datetime import datetime, timezone
from pathlib import Path
STATUSES={"Pass","Fail","Blocked","Not Applicable"}
BLOCKERS={"Environment","Test Data","Access","Dependency","Requirement / Oracle","Other"}
def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def save(p,d): p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("run_path"); ap.add_argument("prior_result_id"); ap.add_argument("status",choices=sorted(STATUSES))
    ap.add_argument("--actual-result"); ap.add_argument("--executed-by"); ap.add_argument("--notes")
    ap.add_argument("--blocker-type",choices=sorted(BLOCKERS)); ap.add_argument("--blocker-reason")
    args=ap.parse_args(); run_dir=Path(args.run_path).resolve(); run_p=run_dir/"execution.json"; res_p=run_dir/"results.json"
    if not run_p.is_file() or not res_p.is_file(): print("ERROR execution files missing"); return 1
    run=load(run_p)
    if run.get("status")=="Closed": print("ERROR Closed execution runs are immutable"); return 1
    results=load(res_p); items=results.get("results",[])
    prior=next((r for r in items if r.get("execution_result_id")==args.prior_result_id),None)
    if not prior: print("ERROR prior execution result not found"); return 1
    if args.status=="Blocked" and (not args.blocker_type or not args.blocker_reason): print("ERROR Blocked retest requires blocker type and reason"); return 1
    nums=[int(r["execution_result_id"][3:]) for r in items if r.get("execution_result_id","").startswith("ER-") and r["execution_result_id"][3:].isdigit()]
    rid=f"ER-{(max(nums,default=0)+1):04d}"; ts=now()
    items.append({"execution_result_id":rid,"test_case_id":prior["test_case_id"],"status":args.status,"actual_result":args.actual_result,"executed_by":args.executed_by or run.get("executor"),"executed_at":ts,"environment":run.get("environment"),"build":run.get("build"),"evidence":[],"defect_ids":list(prior.get("defect_ids",[])),"notes":args.notes,"retest_of":args.prior_result_id,"blocker_type":args.blocker_type,"blocker_reason":args.blocker_reason})
    results["results"]=items; save(res_p,results); run["updated_at"]=ts
    if run.get("status")=="Planned": run["status"]="In Progress"
    save(run_p,run); print(f"Recorded retest {rid}: {prior['test_case_id']} -> {args.status}; retest_of={args.prior_result_id}"); return 0
if __name__=="__main__": raise SystemExit(main())
