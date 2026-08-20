"""Generate human-readable release notes from release manifest and validation evidence."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main()->int:
 m=json.loads((ROOT/"release/manifest.json").read_text(encoding="utf-8")); vpath=ROOT/"release/validation-report.json"; v=json.loads(vpath.read_text(encoding="utf-8")) if vpath.exists() else None
 lines=[f"# QA-AI Release {m['version']}","",f"> Release ID: {m['release_id']}",f"> Status: {m['status']}",f"> Repository Revision: `{m['repository_revision']}`","","## Capability Baseline",""]
 for k,val in m["capabilities"].items(): lines.append(f"- **{k}**: {val}")
 lines += ["","## Validation",""]
 if v:
  lines.append(f"Overall: **{v['overall']}**")
  for x in v["validators"]: lines.append(f"- {x['name']}: **{x['status']}**")
 else: lines.append("No release validation evidence has been generated yet.")
 lines += ["","## Release Boundary","","This release evidence verifies the recorded repository revision only. It does not approve project artifacts, select regression scope, execute tests, or mutate workspace lifecycle state.",""]
 (ROOT/"release/RELEASE-NOTES.md").write_text("\n".join(lines),encoding="utf-8"); print("Generated release/RELEASE-NOTES.md"); return 0
if __name__=="__main__": raise SystemExit(main())
