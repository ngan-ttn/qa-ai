"""Validate Phase 19 change-set, impact analysis, and incremental plan reconciliation."""
from __future__ import annotations
import argparse,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; ACTIONS={"Reuse","Review","Regenerate","Revalidate","Re-execute","Blocked"}; CLASSES={"Added","Modified","Removed","Unchanged","Unknown"}; IMPACTS={"Direct","Dependency","Potential","Unknown"}
def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def unique(rows,key,errors,label):
 vals=[r.get(key) for r in rows]
 if len(vals)!=len(set(vals)): errors.append(f"duplicate {label} IDs")
 return set(vals)
def main()->int:
 p=argparse.ArgumentParser(); p.add_argument("feature_path"); p.add_argument("--revision"); a=p.parse_args(); f=Path(a.feature_path); f=f if f.is_absolute() else ROOT/f; meta=load(f/"metadata.json"); rev=a.revision or meta["current_revision"]; d=f/"revisions"/rev/"change-intelligence"; errors=[]
 try: c,i,q=load(d/"change-set.json"),load(d/"impact-analysis.json"),load(d/"incremental-plan.json")
 except Exception as e: print(f"ERROR {e}"); return 1
 if not (c.get("base_revision")==i.get("base_revision")==q.get("base_revision")) or not (c.get("target_revision")==i.get("target_revision")==q.get("target_revision")==rev): errors.append("revision reconciliation mismatch")
 changes,impacts,actions=c.get("changes",[]),i.get("impacts",[]),q.get("actions",[]); ch=unique(changes,"change_id",errors,"change"); im=unique(impacts,"impact_id",errors,"impact"); unique(actions,"action_id",errors,"action")
 for r in changes:
  if r.get("classification") not in CLASSES: errors.append(f"invalid change classification: {r.get('change_id')}")
 for r in impacts:
  if r.get("change_id") not in ch: errors.append(f"impact references unknown change: {r.get('impact_id')}")
  if r.get("artifact_key") not in meta.get("artifacts",{}): errors.append(f"impact references unknown artifact: {r.get('artifact_key')}")
  if r.get("impact_type") not in IMPACTS: errors.append(f"invalid impact type: {r.get('impact_id')}")
 by_art={}
 for r in actions:
  k=r.get("artifact_key"); by_art[k]=by_art.get(k,0)+1
  if k not in meta.get("artifacts",{}): errors.append(f"action references unknown artifact: {k}")
  if r.get("action") not in ACTIONS: errors.append(f"invalid action: {r.get('action')}")
  if any(x not in im for x in r.get("impact_ids",[])): errors.append(f"action references unknown impact: {r.get('action_id')}")
  if r.get("action")!="Reuse" and (not r.get("reason") or not r.get("evidence")): errors.append(f"non-Reuse action lacks reason/evidence: {r.get('action_id')}")
 if any(v!=1 for v in by_art.values()) or set(by_art)!=set(meta.get("artifacts",{})): errors.append("incremental plan must contain exactly one action per registered artifact")
 for data,rows,field in [(c,changes,"classification"),(q,actions,"action")]:
  if data.get("summary",{}).get("total")!=len(rows): errors.append("summary total mismatch")
  for name in (CLASSES if field=="classification" else ACTIONS):
   if data.get("summary",{}).get(name,0)!=sum(r.get(field)==name for r in rows): errors.append(f"summary count mismatch: {name}")
 if i.get("summary",{}).get("total")!=len(impacts): errors.append("impact summary total mismatch")
 if errors:
  [print(f"ERROR {e}") for e in errors]; print(f"Change intelligence validation failed; issues={len(errors)}"); return 1
 print(f"PASS change intelligence validation: {d}"); print(f"Changes={len(changes)} Impacts={len(impacts)} Actions={len(actions)}"); return 0
if __name__=="__main__": raise SystemExit(main())
