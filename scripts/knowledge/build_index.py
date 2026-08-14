"""Build a deterministic JSON index for QA-AI knowledge Markdown files."""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import iter_files, relative_to_repo, write_json

TITLE_RE = re.compile(r"^#\s+(.+)$", re.M)
STATUS_RE = re.compile(r"^>\s*Status:\s*(.+)$", re.M)


def make_entry(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    rel = relative_to_repo(path)
    title = TITLE_RE.search(text)
    status = STATUS_RE.search(text)
    return {
        "path": rel,
        "domain": rel.split("/")[2] if rel.startswith("shared/knowledge/") else None,
        "title": title.group(1).strip() if title else path.stem,
        "status": status.group(1).strip() if status else None,
        "bytes": len(text.encode("utf-8")),
        "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    }


def build(base: str = "shared/knowledge") -> list[dict[str, object]]:
    return [
        make_entry(path)
        for path in iter_files(base, ("*.md",))
        if path.name not in {"README.md", "Catalog.md"}
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="shared/knowledge")
    parser.add_argument("--output", default="output/knowledge-index.json")
    args = parser.parse_args()
    entries = build(args.base)
    write_json(args.output, {"count": len(entries), "entries": entries})
    print(f"Indexed {len(entries)} knowledge article(s) -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
