"""Validate release manifest structure and reconcile capability inventory."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def count_dirs(path: Path) -> int:
    if not path.exists():
        return 0
    return len([p for p in path.iterdir() if p.is_dir() and not p.name.startswith(".")])


def main() -> int:
    path = ROOT / "release/manifest.json"
    if not path.is_file():
        print("ERROR: missing release/manifest.json")
        return 1

    d = json.loads(path.read_text(encoding="utf-8"))
    errors = []

    for key in (
        "schema_version",
        "release_id",
        "version",
        "status",
        "repository_revision",
        "generated_at",
        "capabilities",
        "validation_requirements",
    ):
        if key not in d:
            errors.append(f"missing field: {key}")

    if d.get("status") not in {"Draft", "Candidate", "Validated", "Released", "Superseded"}:
        errors.append("invalid release status")

    caps = d.get("capabilities", {})
    expected = {
        "skills": count_dirs(ROOT / "skills"),
        "workflows": count_dirs(ROOT / "workflows"),
        "platforms": len(
            [
                platform
                for platform in ("chatgpt", "claude", "cursor")
                if (ROOT / "adapters" / platform).is_dir()
            ]
        ),
    }

    for key, value in expected.items():
        if caps.get(key) != value:
            errors.append(
                f"capability count mismatch {key}: manifest={caps.get(key)} actual={value}"
            )

    capability_scripts = {
        "workspace_lifecycle": "scripts/workspace/validate_workspace.py",
        "export_interoperability": "scripts/export/validate_export.py",
        "execution_feedback": "scripts/execution/validate_execution.py",
        "change_intelligence": "scripts/change_intelligence/validate_change_intelligence.py",
    }
    for key, script_path in capability_scripts.items():
        actual = (ROOT / script_path).is_file()
        if caps.get(key) != actual:
            errors.append(f"capability flag mismatch {key}")

    if errors:
        for error in errors:
            print("ERROR:", error)
        print(f"FAIL release manifest validation: issues={len(errors)}")
        return 1

    print(
        "PASS release manifest validation: "
        f"skills={expected['skills']} "
        f"workflows={expected['workflows']} "
        f"platforms={expected['platforms']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
