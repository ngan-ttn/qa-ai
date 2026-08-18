"""Initialize a canonical QA-AI project/feature workspace."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORKSPACE = ROOT / "workspace"
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

ARTIFACT_FILENAMES = {
    "requirement-analysis": "Requirement-Analysis.md",
    "business-rules": "Business-Rules.md",
    "risk-analysis": "Risk-Analysis.md",
    "test-scenarios": "Test-Scenarios.md",
    "coverage-review": "Coverage-Review.md",
    "test-cases": "Test-Cases.md",
    "regression-analysis": "Regression-Analysis.md",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def git_revision() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return "unknown"


def validate_id(value: str, label: str) -> None:
    if not ID_PATTERN.fullmatch(value):
        raise SystemExit(f"ERROR {label} must use lowercase kebab-case: {value}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, help="stable lowercase kebab-case project ID")
    parser.add_argument("--feature", required=True, help="stable lowercase kebab-case feature ID")
    parser.add_argument("--name", help="feature display name; defaults to feature ID")
    args = parser.parse_args()
    validate_id(args.project, "project ID"); validate_id(args.feature, "feature ID")
    project_dir = WORKSPACE / "projects" / args.project
    feature_dir = project_dir / "features" / args.feature
    metadata_path = feature_dir / "metadata.json"
    if metadata_path.exists(): print(f"ERROR workspace already initialized: {metadata_path.relative_to(ROOT)}"); return 1
    for path in (
        feature_dir / "source" / "requirements", feature_dir / "source" / "supporting",
        feature_dir / "artifacts", feature_dir / "exports" / "generic", feature_dir / "executions",
        feature_dir / "revisions", feature_dir / "archive",
    ): path.mkdir(parents=True, exist_ok=True)
    project_readme = project_dir / "README.md"
    if not project_readme.exists(): project_readme.write_text(f"# Project: {args.project}\n\nCanonical feature workspaces are stored under `features/`.\n",encoding="utf-8")
    feature_readme = feature_dir / "README.md"
    feature_readme.write_text(
        f"# Feature: {args.name or args.feature}\n\n- Project ID: `{args.project}`\n- Feature ID: `{args.feature}`\n- Current Revision: `REV-001`\n\n"
        "Use `metadata.json` as the workspace lifecycle/provenance registry. Derived exports belong under `exports/`; execution evidence belongs under `executions/`.\n",
        encoding="utf-8",
    )
    timestamp=now_iso(); artifacts={key:{"artifact_type":key,"path":f"artifacts/{filename}","status":"Draft","freshness":"Unknown","revision":"ART-001","source_revision":"REV-001","generated_by":None,"framework_revision":git_revision(),"updated_at":timestamp,"dependencies":[]} for key,filename in ARTIFACT_FILENAMES.items()}
    metadata={"schema_version":"1.0","project_id":args.project,"feature_id":args.feature,"feature_name":args.name or args.feature,"status":"Active","current_revision":"REV-001","framework_revision":git_revision(),"created_at":timestamp,"updated_at":timestamp,"sources":[],"artifacts":artifacts}
    metadata_path.write_text(json.dumps(metadata,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"Initialized workspace: {feature_dir.relative_to(ROOT)}"); print("Current revision: REV-001"); print("Artifacts registered as Draft / Unknown freshness; export and execution directories initialized."); return 0
if __name__ == "__main__": raise SystemExit(main())
