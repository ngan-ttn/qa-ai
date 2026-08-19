"""Create one deterministic incremental QA recommendation per registered artifact."""
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def choose(rows,art):
 if not rows: return "Reuse"
 if any(r["impact_type"]=="Unknown" for r in rows): return "Blocked"
 typ=str(art.get("artifact_type","")).lower()
 if "regression" in typ: return "Revalidate"
 if "test" in typ and "case" in typ: return "Regenerate"
 return "Regenerate" if any(r["impact_type"] in {"Direct","Dependency"} for r in rows) else "Review"
def main()->int:
 p=argparse.ArgumentParser(); p.add_argument("feature_path"); p.add_argument("--impact-analysis"); p.add_argument("--output"); a=p.parse_args(); f=Path(a.feature_path); f=f if f.is_absolute() else ROOT/f; meta=load(f/"metadata.json"); rev=meta["current_revision"]; ip=Path(a.impact_analysis) if a.impact_analysis else f/"revisions"/rev/"change-intelligence"/"impact-analysis.json"; d=load(ip); by={}
 for r in d["impacts"]: by.setdefault(r["artifact_key"],[]).append(r)
 actions=[]
 for i,(key,art) in enumerate(sorted(meta.get("artifacts",{}).items()),1):
  rows=by.get(key,[]); action=choose(rows,art); ids=[r["impact_id"] for r in rows]; evidence=sorted({e for r in rows for e in r.get("evidence",[])})
  reason="No supported change impact reaches this artifact; reuse is justified." if action=="Reuse" else f"Supported impact requires {action} before this artifact can be treated as current for the target revision."
  actions.append({"action_id":f"ACT-{i:03d}","artifact_key":key,"action":action,"impact_ids":ids,"reason":reason,"evidence":evidence})
 counts={x:sum(r["action"]==x for r in actions) for x in ["Reuse","Review","Regenerate","Revalidate","Re-execute","Blocked"]}; data={"schema_version":"1.0","base_revision":d["base_revision"],"target_revision":d["target_revision"],"actions":actions,"summary":{"total":len(actions),**counts}}; out=Path(a.output) if a.output else ip.parent/"incremental-plan.json"; out.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"); print(f"Incremental QA plan created: {out}"); print(f"Summary: {data['summary']}"); return 0
if __name__=="__main__": raise SystemExit(main())
