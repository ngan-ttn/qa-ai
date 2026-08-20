"""Build a deterministic QA-AI release manifest from canonical repository state."""
from __future__ import annotations
import argparse,json,subprocess
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def git_revision()->str:
 return subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip()

def count_dirs(path:Path)->int:
 return len([p for p in path.iterdir() if p.is_dir() and not p.name.startswith(".")]) if path.exists() else 0

def main()->int:
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument("--release-id",default="QA-AI-1.0.0"); p.add_argument("--status",choices=["Draft","Candidate","Validated","Released","Superseded"],default="Candidate")
 p.add_argument("--output",type=Path,default=ROOT/"release"/"manifest.json"); a=p.parse_args()
 framework=json.loads((ROOT/"manifest.json").read_text(encoding="utf-8"))
 data={"schema_version":"1.0","release_id":a.release_id,"version":framework.get("version","1.0.0"),"status":a.status,"repository_revision":git_revision(),"generated_at":datetime.now(timezone.utc).isoformat(),"capabilities":{"skills":count_dirs(ROOT/"skills"),"workflows":count_dirs(ROOT/"workflows"),"platforms":len([x for x in ("chatgpt","claude","cursor") if (ROOT/"adapters"/x).is_dir()]),"workspace_lifecycle":(ROOT/"scripts/workspace/validate_workspace.py").is_file(),"export_interoperability":(ROOT/"scripts/export/validate_export.py").is_file(),"execution_feedback":(ROOT/"scripts/execution/validate_execution.py").is_file(),"change_intelligence":(ROOT/"scripts/change_intelligence/validate_change_intelligence.py").is_file()},"validation_requirements":["structure","links","metadata","outputs","adapters","roadmap","workspace","change-intelligence","execution"],"evidence":[]}
 a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
 print(f"Built release manifest: {a.output}"); print(f"repository_revision={data['repository_revision']}"); return 0
if __name__=="__main__": raise SystemExit(main())
