"""Run fail-closed QA-AI release readiness validation and write revision-bound evidence."""
from __future__ import annotations
import argparse,json,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def run(name:str,args:list[str])->dict:
 p=subprocess.run([sys.executable,*args],cwd=ROOT,text=True,capture_output=True); out=(p.stdout+p.stderr).strip()
 print(out); print(f"{name}: {'PASS' if p.returncode==0 else 'FAIL'}")
 return {"name":name,"status":"PASS" if p.returncode==0 else "FAIL","command":"python "+" ".join(args),"exit_code":p.returncode,"output":out[-4000:]}

def main()->int:
 ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--workspace",required=True); ap.add_argument("--revision",required=True); ap.add_argument("--execution",required=True); ap.add_argument("--output",type=Path,default=ROOT/"release/validation-report.json"); a=ap.parse_args()
 manifest=json.loads((ROOT/"release/manifest.json").read_text(encoding="utf-8")); rev=subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip()
 gates=[("manifest",["scripts/release/validate_manifest.py"]),("structure",["scripts/validation/validate_structure.py"]),("links",["scripts/validation/validate_links.py"]),("metadata",["scripts/validation/validate_metadata.py"]),("outputs",["scripts/validation/validate_outputs.py"]),("adapters",["adapters/validate_adapters.py"]),("roadmap",["scripts/roadmap/validate_progress.py"]),("workspace",["scripts/workspace/validate_workspace.py",a.workspace]),("change-intelligence",["scripts/change_intelligence/validate_change_intelligence.py",a.workspace,"--revision",a.revision]),("execution",["scripts/execution/validate_execution.py",a.execution])]
 results=[run(n,c) for n,c in gates]; overall="PASS" if all(x["status"]=="PASS" for x in results) else "FAIL"
 report={"schema_version":"1.0","release_id":manifest["release_id"],"repository_revision":rev,"validated_at":datetime.now(timezone.utc).isoformat(),"validators":results,"overall":overall}
 a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
 print(f"Release Readiness: {overall}"); return 0 if overall=="PASS" else 1
if __name__=="__main__": raise SystemExit(main())
