"""Propagate confirmed revision changes through registered workspace dependencies."""
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def main()->int:
 p=argparse.ArgumentParser(); p.add_argument("feature_path"); p.add_argument("--change-set"); p.add_argument("--output"); a=p.parse_args(); f=Path(a.feature_path); f=f if f.is_absolute() else ROOT/f; meta=load(f/"metadata.json"); rev=meta["current_revision"]; cp=Path(a.change_set) if a.change_set else f/"revisions"/rev/"change-intelligence"/"change-set.json"; c=load(cp); changed={x["item_key"]:x for x in c["changes"] if x["classification"]!="Unchanged"}; impacts=[]; n=1
 for key,art in meta.get("artifacts",{}).items():
  refs=[]
  if f"artifact:{key}" in changed: refs.append((changed[f"artifact:{key}"],"Direct","self"))
  for d in art.get("dependencies",[]):
   target=d.get("target")
   if target in changed: refs.append((changed[target],"Dependency",d.get("relationship","registered")))
  for ch,typ,rel in refs:
   impacts.append({"impact_id":f"IMP-{n:03d}","change_id":ch["change_id"],"artifact_key":key,"impact_type":"Unknown" if ch["classification"]=="Unknown" else typ,"relationship":rel,"reason":f"{ch['classification']} change reaches artifact {key} through {rel} relationship.","evidence":[ch["item_key"],*(ch.get("evidence") or [])]}); n+=1
 summary={"total":len(impacts),"affected_artifacts":len(set(x["artifact_key"] for x in impacts))}
 data={"schema_version":"1.0","base_revision":c["base_revision"],"target_revision":c["target_revision"],"impacts":impacts,"summary":summary}; out=Path(a.output) if a.output else cp.parent/"impact-analysis.json"; out.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"); print(f"Impact analysis created: {out}"); print(f"Summary: {summary}"); return 0
if __name__=="__main__": raise SystemExit(main())
