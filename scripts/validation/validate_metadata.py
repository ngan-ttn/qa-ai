"""Validate QA-AI Markdown metadata blocks and safely migrate date placeholders."""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import iter_files, relative_to_repo

META_PATTERNS = {
    "Version": re.compile(r"^>\s*Version:\s*(\S+)\s*$", re.M),
    "Status": re.compile(r"^>\s*Status:\s*(.+?)\s*$", re.M),
    "Last Updated": re.compile(r"^>\s*Last Updated:\s*(.+?)\s*$", re.M),
}
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ALLOWED_STATUS = {"Draft", "Review", "Approved", "Completed", "Frozen", "Planned", "In Progress"}
METADATA_SCAN_LINES = 20


def metadata_window(text: str) -> str:
    """Return only the document preamble where canonical metadata may live."""
    return "\n".join(text.splitlines()[:METADATA_SCAN_LINES])


def requires_metadata(path: Path, text: str) -> bool:
    rel = relative_to_repo(path)
    if rel.startswith("shared/knowledge/") and path.name not in {"README.md", "Catalog.md"}:
        return True
    preamble = metadata_window(text)
    return any(label in preamble for label in ("> Version:", "> Status:", "> Last Updated:"))


def validate_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    if not requires_metadata(path, text):
        return []

    preamble = metadata_window(text)
    errors: list[str] = []
    matches = {key: pattern.search(preamble) for key, pattern in META_PATTERNS.items()}
    for key, match in matches.items():
        if not match:
            errors.append(f"missing metadata field: {key}")

    version = matches.get("Version")
    if version and not VERSION_RE.fullmatch(version.group(1).strip()):
        errors.append(f"invalid Version: {version.group(1).strip()}")

    status = matches.get("Status")
    if status and status.group(1).strip() not in ALLOWED_STATUS:
        errors.append(f"unsupported Status: {status.group(1).strip()}")

    updated = matches.get("Last Updated")
    if updated:
        value = updated.group(1).strip()
        if value == "YYYY-MM-DD":
            errors.append("placeholder Last Updated value remains")
        elif not DATE_RE.fullmatch(value):
            errors.append(f"invalid Last Updated: {value}")
        else:
            try:
                date.fromisoformat(value)
            except ValueError:
                errors.append(f"invalid Last Updated calendar date: {value}")
    return errors


def fix_date_placeholder(path: Path, replacement: str) -> bool:
    """Replace only a canonical top-of-document Last Updated placeholder."""
    text = path.read_text(encoding="utf-8")
    if not requires_metadata(path, text):
        return False

    lines = text.splitlines(keepends=True)
    changed = False
    for index in range(min(METADATA_SCAN_LINES, len(lines))):
        line = lines[index]
        newline = "\n" if line.endswith("\n") else ""
        body = line.rstrip("\r\n")
        if re.fullmatch(r">\s*Last Updated:\s*YYYY-MM-DD\s*", body):
            lines[index] = f"> Last Updated: {replacement}{newline}"
            changed = True
            break
    if changed:
        path.write_text("".join(lines), encoding="utf-8", newline="\n")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", default=["shared/knowledge", "shared/standards", "docs"])
    parser.add_argument(
        "--fix-placeholders",
        action="store_true",
        help="Replace top-level Last Updated YYYY-MM-DD placeholders before validation",
    )
    parser.add_argument(
        "--date",
        help="Replacement ISO date required with --fix-placeholders (YYYY-MM-DD)",
    )
    args = parser.parse_args()

    if args.fix_placeholders:
        if not args.date or not DATE_RE.fullmatch(args.date):
            parser.error("--fix-placeholders requires --date YYYY-MM-DD")
        try:
            date.fromisoformat(args.date)
        except ValueError:
            parser.error("--date must be a valid calendar date")

    files: list[Path] = []
    for base in args.paths:
        files.extend(iter_files(base, ("*.md",)))
    files = sorted(set(files))

    if args.fix_placeholders:
        fixed = 0
        for path in files:
            if fix_date_placeholder(path, args.date):
                fixed += 1
                print(f"FIXED {relative_to_repo(path)}: Last Updated -> {args.date}")
        print(f"Fixed {fixed} metadata placeholder(s)")

    failures = 0
    checked = 0
    for path in files:
        checked += 1
        for error in validate_file(path):
            failures += 1
            print(f"ERROR {relative_to_repo(path)}: {error}")
    print(f"Checked {checked} Markdown file(s); issues={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
