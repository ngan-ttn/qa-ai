"""Link a defect reference to an existing execution result."""
from __future__ import annotations
import argparse, json
from pathlib import Path

def load(p): return json.loads(p.read_text(encoding="utf-8"))
def save(p,d): p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("run_path"); ap.add_argument("execution_result_id"); ap.add_argument("defect_id")
    ap.add_argument("--title",required=True); ap.add_argument("--external-id"); ap.add_argument("--status"); ap.add_argument("--url")
    args=ap.parse_args(); run_dir=Path(args.run_path).resolve(); run_p=run_dir/"execution.json"; res_p=run_dir/"results.json"; def_p=run_dir/"defects.json"
    if not all(p.is_file() for p in (run_p,res_p,def_p)): print("ERROR execution files missing"); return 1
    run=load(run_p)
    if run.get("status")=="Closed": print("ERROR Closed execution runs are immutable"); return 1
    results=load(res_p); defects=load(def_p)
    match=next((r for r in results.get("results",[]) if r.get("execution_result_id")==args.execution_result_id),None)
    if not match: print("ERROR execution result not found"); return 1
    if not args.defect_id.startswith("BUG-"): print("ERROR defect ID must start with BUG-"); return 1
    existing=next((d for d in defects.get("defects",[]) if d.get("defect_id")==args.defect_id),None)
    if existing:
        ids=existing.setdefault("source_execution_result_ids",[])
        if args.execution_result_id not in ids: ids.append(args.execution_result_id)
        if args.external_id is not None: existing["external_id"]=args.external_id
        if args.status is not None: existing["status"]=args.status
        if args.url is not None: existing["url"]=args.url
    else:
        defects.setdefault("defects",[]).append({"defect_id":args.defect_id,"external_id":args.external_id,"title":args.title,"source_execution_result_ids":[args.execution_result_id],"status":args.status,"url":args.url})
    linked=match.setdefault("defect_ids",[])
    if args.defect_id not in linked: linked.append(args.defect_id)
    save(res_p,results); save(def_p,defects)
    print(f"Linked {args.defect_id} to {args.execution_result_id}"); return 0
if __name__=="__main__": raise SystemExit(main())
