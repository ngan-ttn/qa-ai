"""Validate repository structure against manifest.json and canonical QA-AI script inventory."""
from __future__ import annotations
import argparse,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from scripts.utils.file_utils import read_json
CORE_PATHS=["README.md","FRAMEWORK.md","manifest.json","docs","shared","skills","workflows","datasets","scripts","workspace"]
SCRIPT_FILES={
"validation":["validate_structure.py","validate_links.py","validate_metadata.py","validate_outputs.py"],
"knowledge":["build_index.py","chunk_knowledge.py","validate_catalog.py"],
"prompts":["assemble_context.py","build_prompt.py"],
"workflows":["load_workflow.py","resolve_skills.py","run_workflow.py"],
"evaluation":["benchmark.py","compare_output.py","score_coverage.py","score_format.py"],
"export":["export_excel.py","export_markdown.py","package_output.py","parse_testcases.py","parse_coverage.py","parse_regression.py","export_artifact.py","validate_export.py"],
"utils":["config_utils.py","file_utils.py","logging_utils.py"],
"roadmap":["collect_status.py","validate_progress.py","update_roadmap.py"],
"workspace":["init_workspace.py","register_source.py","register_artifact.py","validate_workspace.py","snapshot_revision.py","update_artifact_state.py"],
"execution":["init_execution.py","record_result.py","link_defect.py","record_retest.py","summarize_execution.py","validate_execution.py"],
"change_intelligence":["analyze_change.py","analyze_impact.py","plan_incremental_qa.py","render_change_report.py","validate_change_intelligence.py"],
}
def validate(root:Path)->list[str]:
 errors=[]
 for rel in CORE_PATHS:
  if not (root/rel).exists(): errors.append(f"missing required path: {rel}")
 manifest_path=root/"manifest.json"
 if manifest_path.exists():
  manifest=read_json(manifest_path)
  if not isinstance(manifest,dict): errors.append("manifest.json must contain an object")
  else:
   for key in ("entry_point","roadmap","roadmap_status"):
    rel=manifest.get(key)
    if not isinstance(rel,str) or not rel.strip(): errors.append(f"manifest missing required string field: {key}")
    elif not (root/rel).exists(): errors.append(f"manifest {key} points to missing path: {rel}")
   components=manifest.get("components",{})
   if not isinstance(components,dict): errors.append("manifest components must be an object")
   else:
    for name,rel in components.items():
     if not isinstance(rel,str) or not (root/rel).exists(): errors.append(f"manifest component {name} missing: {rel}")
 scripts=root/"scripts"
 for group,filenames in SCRIPT_FILES.items():
  group_path=scripts/group
  if not group_path.is_dir(): errors.append(f"missing script group: scripts/{group}"); continue
  for filename in filenames:
   path=group_path/filename
   if not path.is_file(): errors.append(f"missing canonical script: scripts/{group}/{filename}")
   elif path.stat().st_size==0: errors.append(f"canonical script is empty: scripts/{group}/{filename}")
 return errors
def main()->int:
 parser=argparse.ArgumentParser(description=__doc__); parser.add_argument("--root",type=Path,default=ROOT); args=parser.parse_args(); errors=validate(args.root.resolve())
 if errors:
  [print(f"ERROR: {x}") for x in errors]; print(f"FAIL: {len(errors)} structural issue(s)"); return 1
 print(f"PASS: repository structure is valid; canonical_scripts={sum(map(len,SCRIPT_FILES.values()))}"); return 0
if __name__=="__main__": raise SystemExit(main())
