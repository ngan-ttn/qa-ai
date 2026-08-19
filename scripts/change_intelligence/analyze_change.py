"""Create deterministic revision change-set evidence from workspace snapshot metadata/artifact checksums."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; REV=re.compile(r"^REV-[0-9]{3,}$")
def digest(p:Path)->str: return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p:Path): return json.loads(p.read_text(encoding="utf-8"))
def inventory(feature:Path, rev:str)->dict:
    snap=feature/"revisions"/rev; meta=snap/"metadata.json"
    if not meta.is_file(): raise ValueError(f"revision snapshot metadata not found: {meta}")
    d=load(meta); out={}
    for k,a in d.get("artifacts",{}).items():
        if not isinstance(a,dict): continue
        name=Path(a.get("path","")).name; p=snap/"artifacts"/name
        out[f"artifact:{k}"]={"checksum":digest(p) if p.is_file() else None,"path":str(p.relative_to(feature)).replace('\\','/'),"revision":a.get("revision")}
    for s in d.get("sources",[]):
        if isinstance(s,dict) and s.get("source_id"): out[f"source:{s['source_id']}"]={"checksum":s.get("checksum"),"path":s.get("path"),"revision":rev}
    return out
def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("feature_path"); p.add_argument("base_revision"); p.add_argument("target_revision"); p.add_argument("--output"); a=p.parse_args(); feature=Path(a.feature_path); feature=feature if feature.is_absolute() else ROOT/feature
    if not REV.fullmatch(a.base_revision) or not REV.fullmatch(a.target_revision) or a.base_revision==a.target_revision: print("ERROR revisions must be distinct canonical REV-* IDs"); return 1
    try: b,t=inventory(feature,a.base_revision),inventory(feature,a.target_revision)
    except Exception as e: print(f"ERROR {e}"); return 1
    rows=[]
    for i,key in enumerate(sorted(set(b)|set(t)),1):
        if key not in b: c="Added"
        elif key not in t: c="Removed"
        elif b[key].get("checksum") and t[key].get("checksum"): c="Unchanged" if b[key]["checksum"]==t[key]["checksum"] else "Modified"
        else: c="Unknown" if b[key].get("checksum")!=t[key].get("checksum") else "Unchanged"
        rows.append({"change_id":f"CHG-{i:03d}","item_key":key,"classification":c,"reason":f"Deterministic revision inventory comparison classified {key} as {c}.","evidence":[b.get(key,{}).get("path","base:absent"),t.get(key,{}).get("path","target:absent")]})
    counts={x:sum(r["classification"]==x for r in rows) for x in ["Added","Modified","Removed","Unchanged","Unknown"]}
    data={"schema_version":"1.0","base_revision":a.base_revision,"target_revision":a.target_revision,"changes":rows,"summary":{"total":len(rows),**counts}}
    out=Path(a.output) if a.output else feature/"revisions"/a.target_revision/"change-intelligence"/"change-set.json"; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"); print(f"Change set created: {out}"); print(f"Summary: {data['summary']}"); return 0
if __name__=="__main__": raise SystemExit(main())
