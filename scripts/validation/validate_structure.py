"""Validate repository structure against manifest.json and core QA-AI conventions."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import read_json

CORE_PATHS = [
    "README.md", "FRAMEWORK.md", "manifest.json", "docs", "shared", "skills",
    "workflows", "datasets", "scripts",
]
SCRIPT_GROUPS = ["validation", "knowledge", "prompts", "workflows", "evaluation", "export", "utils"]


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    for rel in CORE_PATHS:
        if not (root / rel).exists():
            errors.append(f"missing required path: {rel}")

    manifest_path = root / "manifest.json"
    if manifest_path.exists():
        manifest = read_json(manifest_path)
        if not isinstance(manifest, dict):
            errors.append("manifest.json must contain an object")
        else:
            for key in ("entry_point", "roadmap", "roadmap_status"):
                rel = manifest.get(key)
                if rel and not (root / rel).exists():
                    errors.append(f"manifest {key} points to missing path: {rel}")
            components = manifest.get("components", {})
            if isinstance(components, dict):
                for name, rel in components.items():
                    if not (root / str(rel)).exists():
                        errors.append(f"manifest component {name} missing: {rel}")

    scripts = root / "scripts"
    for group in SCRIPT_GROUPS:
        if not (scripts / group).is_dir():
            errors.append(f"missing script group: scripts/{group}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    if errors:
        for item in errors:
            print(f"ERROR: {item}")
        print(f"FAIL: {len(errors)} structural issue(s)")
        return 1
    print("PASS: repository structure is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
