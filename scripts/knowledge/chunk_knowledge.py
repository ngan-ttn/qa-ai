"""Chunk QA-AI knowledge articles deterministically by Markdown sections."""
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

SECTION_RE = re.compile(r"(?m)^(#{1,3})\s+(.+)$")


def split_sections(text: str) -> list[tuple[str, str]]:
    matches = list(SECTION_RE.finditer(text))
    if not matches:
        return [("Document", text.strip())]
    result: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result.append((match.group(2).strip(), text[start:end].strip()))
    return result


def chunk_text(text: str, max_chars: int) -> list[tuple[str, str]]:
    chunks: list[tuple[str, str]] = []
    for heading, section in split_sections(text):
        if len(section) <= max_chars:
            chunks.append((heading, section))
            continue
        paragraphs = [p.strip() for p in section.split("\n\n") if p.strip()]
        current = ""
        part = 1
        for paragraph in paragraphs:
            candidate = f"{current}\n\n{paragraph}".strip()
            if current and len(candidate) > max_chars:
                chunks.append((f"{heading} (part {part})", current))
                part += 1
                current = paragraph
            else:
                current = candidate
        if current:
            chunks.append((f"{heading} (part {part})" if part > 1 else heading, current))
    return chunks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="shared/knowledge")
    parser.add_argument("--output", default="output/knowledge-chunks.json")
    parser.add_argument("--max-chars", type=int, default=4000)
    args = parser.parse_args()
    if args.max_chars < 500:
        parser.error("--max-chars must be >= 500")
    records: list[dict[str, object]] = []
    for path in iter_files(args.base, ("*.md",)):
        if path.name in {"README.md", "Catalog.md"}:
            continue
        rel = relative_to_repo(path)
        for number, (heading, content) in enumerate(chunk_text(path.read_text(encoding="utf-8"), args.max_chars), 1):
            records.append({
                "id": hashlib.sha1(f"{rel}:{number}:{content}".encode()).hexdigest()[:16],
                "source": rel,
                "chunk": number,
                "heading": heading,
                "content": content,
            })
    write_json(args.output, {"count": len(records), "chunks": records})
    print(f"Created {len(records)} chunk(s) -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
