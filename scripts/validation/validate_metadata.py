"""Validate QA-AI Markdown metadata blocks."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import iter_files, relative_to_repo

META_PATTERNS = {
    "Version": re.compile(r"^>\s*Version:\s*(\S+)\s*$", re.M),
    "Status": re.compile(r"^>\s*Status:\s*(.+?)\s*$", re.M),
    "Last Updated": re.compile(r"^>\s*Last Updated:\s*(\d{4}-\d{2}-\d{2})\s*$", re.M),
}
ALLOWED_STATUS = {"Draft", "Review", "Approved", "Completed", "Frozen", "Planned", "In Progress"}


def requires_metadata(path: Path, text: str) -> bool:
    rel = relative_to_repo(path)
    if rel.startswith("shared/knowledge/") and path.name not in {"README.md", "Catalog.md"}:
        return True
    return any(label in text for label in ("> Version:", "> Status:", "> Last Updated:"))


def validate_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    if not requires_metadata(path, text):
        return []
    errors: list[str] = []
    matches = {key: pattern.search(text) for key, pattern in META_PATTERNS.items()}
    for key, match in matches.items():
        if not match:
            errors.append(f"missing or invalid metadata field: {key}")
    status = matches.get("Status")
    if status and status.group(1).strip() not in ALLOWED_STATUS:
        errors.append(f"unsupported Status: {status.group(1).strip()}")
    if "YYYY-MM-DD" in text[:500]:
        errors.append("placeholder Last Updated value remains")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", default=["shared/knowledge", "shared/standards", "docs"])
    args = parser.parse_args()
    failures = 0
    checked = 0
    for base in args.paths:
        for path in iter_files(base, ("*.md",)):
            checked += 1
            for error in validate_file(path):
                failures += 1
                print(f"ERROR {relative_to_repo(path)}: {error}")
    print(f"Checked {checked} Markdown file(s); issues={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
