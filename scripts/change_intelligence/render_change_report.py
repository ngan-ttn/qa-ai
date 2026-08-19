"""Render human-readable Change-Impact.md from canonical Phase 19 JSON evidence."""
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def main()->int:
 p=argparse.ArgumentParser(); p.add_argument("feature_path"); p.add_argument("--revision"); a=p.parse_args(); f=Path(a.feature_path); f=f if f.is_absolute() else ROOT/f; meta=load(f/"metadata.json"); rev=a.revision or meta["current_revision"]; d=f/"revisions"/rev/"change-intelligence"; c,i,q=load(d/"change-set.json"),load(d/"impact-analysis.json"),load(d/"incremental-plan.json")
 lines=["# Change Impact", "",f"> Base Revision: {c['base_revision']}",f"> Target Revision: {c['target_revision']}","> Status: Analysis Evidence","","## Change Summary","",f"Total compared items: **{c['summary']['total']}**.","","| Change ID | Item | Classification | Reason |","|---|---|---|---|"]
 for r in c["changes"]: lines.append(f"| {r['change_id']} | {r['item_key']} | {r['classification']} | {r['reason']} |")
 lines += ["","## Impact Analysis","","| Impact ID | Change ID | Artifact | Type | Relationship | Reason |","|---|---|---|---|---|---|"]
 for r in i["impacts"]: lines.append(f"| {r['impact_id']} | {r['change_id']} | {r['artifact_key']} | {r['impact_type']} | {r['relationship']} | {r['reason']} |")
 lines += ["","## Incremental QA Plan","","| Action ID | Artifact | Action | Impact IDs | Reason |","|---|---|---|---|---|"]
 for r in q["actions"]: lines.append(f"| {r['action_id']} | {r['artifact_key']} | {r['action']} | {', '.join(r['impact_ids']) or '-'} | {r['reason']} |")
 lines += ["","## Boundary","","This report recommends incremental QA work only. It does not regenerate, approve, mark Current, select regression tiers, or execute tests.",""]
 out=d/"Change-Impact.md"; out.write_text("\n".join(lines),encoding="utf-8"); print(f"Rendered change report: {out}"); return 0
if __name__=="__main__": raise SystemExit(main())
