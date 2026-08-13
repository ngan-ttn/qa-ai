"""Validate generated/example QA output artifacts for deterministic structural defects."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import iter_files, relative_to_repo

PLACEHOLDERS = re.compile(r"\b(TODO|TBD|FIXME|PLACEHOLDER)\b|YYYY-MM-DD", re.I)
HEADING = re.compile(r"^#{1,6}\s+\S", re.M)


def validate_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return ["empty artifact"]
    errors: list[str] = []
    if path.suffix.lower() == ".md":
        if not HEADING.search(text):
            errors.append("Markdown artifact has no heading")
        hit = PLACEHOLDERS.search(text)
        if hit:
            errors.append(f"unresolved placeholder: {hit.group(0)}")
    return errors


def is_output_artifact(path: Path) -> bool:
    rel = relative_to_repo(path)
    return "/expected-output/" in f"/{rel}" or rel.startswith("datasets/golden-output/") or rel.startswith("output/")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", default=["examples", "datasets/golden-output", "output"])
    args = parser.parse_args()
    checked = 0
    issues = 0
    for base in args.paths:
        for path in iter_files(base, ("*.md", "*.json", "*.txt")):
            if not is_output_artifact(path):
                continue
            checked += 1
            for issue in validate_file(path):
                issues += 1
                print(f"ERROR {relative_to_repo(path)}: {issue}")
    print(f"Checked {checked} output artifact(s); issues={issues}")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
