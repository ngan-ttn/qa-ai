"""Validate release manifest structure and reconcile capability inventory."""
from __future__ import annotations
import json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def count_dirs(path:Path)->int: return len([p for p in path.iterdir() if p.is_dir() and not p.name.startswith(".")]) if path.exists() else 0

def main()->int:
 path=ROOT/"release/manifest.json"
 if not path.is_file(): print("ERROR: missing release/manifest.json"); return 1
 d=json.loads(path.read_text(encoding="utf-8")); errors=[]
 for k in ("schema_version","release_id","version","status","repository_revision","generated_at","capabilities","validation_requirements"):
  if k not in d: errors.append(f"missing field: {k}")
 if d.get("status") not in {"Draft","Candidate","Validated","Released","Superseded"}: errors.append("invalid release status")
 caps=d.get("capabilities",{})
 expected={"skills":count_dirs(ROOT/"skills"),"workflows":count_dirs(ROOT/"workflows"),"platforms":len([x for x in ("chatgpt","claude","cursor") if (ROOT/"adapters"/x).is_dir())}
 for k,v in expected.items():
  if caps.get(k)!=v: errors.append(f"capability count mismatch {k}: manifest={caps.get(k)} actual={v}")
 for k,p in {"workspace_lifecycle":"scripts/workspace/validate_workspace.py","export_interoperability":"scripts/export/validate_export.py","execution_feedback":"scripts/execution/validate_execution.py","change_intelligence":"scripts/change_intelligence/validate_change_intelligence.py"}.items():
  actual=(ROOT/p).is_file()
  if caps.get(k)!=actual: errors.append(f"capability flag mismatch {k}")
 if errors:
  [print("ERROR:",x) for x in errors]; print(f"FAIL release manifest validation: issues={len(errors)}"); return 1
 print(f"PASS release manifest validation: skills={expected['skills']} workflows={expected['workflows']} platforms={expected['platforms']}"); return 0
if __name__=="__main__": raise SystemExit(main())
