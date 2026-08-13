"""Resolve and validate skill references required by a QA-AI workflow."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.workflows.load_workflow import load_workflow
from scripts.utils.file_utils import write_json


def resolve(workflow: str) -> dict[str, object]:
    definition = load_workflow(workflow)
    resolved: list[dict[str, object]] = []
    missing: list[str] = []
    for name in definition.get("required_skills", []):
        readme = ROOT / "skills" / str(name) / "README.md"
        exists = readme.is_file() and readme.stat().st_size > 0
        item = {
            "skill": name,
            "path": readme.relative_to(ROOT).as_posix(),
            "available": exists,
        }
        resolved.append(item)
        if not exists:
            missing.append(str(name))
    return {"workflow": definition["name"], "skills": resolved, "missing": missing}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workflow")
    parser.add_argument("--output")
    args = parser.parse_args()
    result = resolve(args.workflow)
    if args.output:
        write_json(args.output, result)
    for item in result["skills"]:
        print(f"{'PASS' if item['available'] else 'ERROR'} {item['skill']} -> {item['path']}")
    if result["missing"]:
        print("Missing skills: " + ", ".join(result["missing"]))
        return 1
    print(f"PASS: all skills resolved for {result['workflow']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
