"""Validate local Markdown links without performing network requests."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import iter_files, relative_to_repo

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#", "data:")


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for raw in LINK_RE.findall(text):
        target = raw.strip().split()[0].strip("<>")
        if not target or target.startswith(SKIP_PREFIXES):
            continue
        target = unquote(target.split("#", 1)[0])
        if not target:
            continue
        candidate = (path.parent / target).resolve()
        if not candidate.exists():
            errors.append(f"broken local link: {raw}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", default=["."])
    args = parser.parse_args()
    issues = 0
    checked = 0
    ignored_dirs = {".git", ".venv", "venv", "node_modules"}
    for base in args.paths:
        for path in iter_files(base, ("*.md",)):
            if any(part in ignored_dirs for part in path.parts):
                continue
            checked += 1
            for error in validate_file(path):
                issues += 1
                print(f"ERROR {relative_to_repo(path)}: {error}")
    print(f"Checked {checked} Markdown file(s); broken_links={issues}")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
