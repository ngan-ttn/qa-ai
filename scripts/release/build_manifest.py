"""Build a deterministic QA-AI release manifest from canonical repository state."""
from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def git_revision() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def count_dirs(path: Path) -> int:
    return len([p for p in path.iterdir() if p.is_dir() and not p.name.startswith(".")]) if path.exists() else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-id", default="QA-AI-1.0.0")
    parser.add_argument(
        "--status",
        choices=["Draft", "Candidate", "Validated", "Released", "Superseded"],
        default="Candidate",
    )
    parser.add_argument(
        "--released-by",
        help="required for Released; records explicit human/operator release approval",
    )
    parser.add_argument("--output", type=Path, default=ROOT / "release" / "manifest.json")
    args = parser.parse_args()

    revision = git_revision()
    evidence: list[str] = []
    if args.status == "Released":
        if not args.released_by:
            print("ERROR: Released status requires --released-by <human/operator evidence>")
            return 1
        report_path = ROOT / "release" / "validation-report.json"
        if not report_path.is_file():
            print("ERROR: Released status requires release/validation-report.json")
            return 1
        report = json.loads(report_path.read_text(encoding="utf-8"))
        if report.get("overall") != "PASS":
            print("ERROR: Released status requires a PASS validation report")
            return 1
        if report.get("repository_revision") != revision:
            print(
                "ERROR: validation report revision does not match current HEAD: "
                f"report={report.get('repository_revision')} head={revision}"
            )
            return 1
        evidence = [
            f"Human release approval: {args.released_by}",
            "Validation evidence: release/validation-report.json",
        ]

    framework = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    data = {
        "schema_version": "1.0",
        "release_id": args.release_id,
        "version": framework.get("version", "1.0.0"),
        "status": args.status,
        "repository_revision": revision,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "capabilities": {
            "skills": count_dirs(ROOT / "skills"),
            "workflows": count_dirs(ROOT / "workflows"),
            "platforms": len([x for x in ("chatgpt", "claude", "cursor") if (ROOT / "adapters" / x).is_dir()]),
            "workspace_lifecycle": (ROOT / "scripts/workspace/validate_workspace.py").is_file(),
            "export_interoperability": (ROOT / "scripts/export/validate_export.py").is_file(),
            "execution_feedback": (ROOT / "scripts/execution/validate_execution.py").is_file(),
            "change_intelligence": (ROOT / "scripts/change_intelligence/validate_change_intelligence.py").is_file(),
        },
        "validation_requirements": [
            "structure",
            "links",
            "metadata",
            "outputs",
            "adapters",
            "roadmap",
            "workspace",
            "change-intelligence",
            "execution",
        ],
        "evidence": evidence,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"Built release manifest: {args.output}")
    print(f"repository_revision={data['repository_revision']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
