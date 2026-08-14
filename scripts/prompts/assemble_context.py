"""Assemble deterministic prompt context from explicit QA-AI source files."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import read_text, resolve_repo_path, write_json


def _repo_source(raw: str) -> Path:
    path = resolve_repo_path(raw).resolve()
    try:
        path.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise ValueError(f"Context source must be inside the QA-AI repository: {raw}") from exc
    if not path.is_file():
        raise FileNotFoundError(path)
    return path


def assemble(paths: list[str], *, max_chars: int = 30000) -> dict[str, object]:
    if max_chars <= 0:
        raise ValueError("max_chars must be positive")
    sources: list[dict[str, object]] = []
    used = 0
    truncated = False
    seen: set[str] = set()
    for raw in paths:
        path = _repo_source(raw)
        rel = path.relative_to(ROOT.resolve()).as_posix()
        if rel in seen:
            raise ValueError(f"Duplicate context source: {rel}")
        seen.add(rel)
        text = read_text(path).strip()
        remaining = max_chars - used
        if remaining <= 0:
            truncated = True
            break
        clipped = text[:remaining]
        was_truncated = len(clipped) < len(text)
        sources.append({
            "path": rel,
            "content": clipped,
            "truncated": was_truncated,
        })
        used += len(clipped)
        truncated = truncated or was_truncated
        if was_truncated:
            break
    return {"sources": sources, "characters": used, "truncated": truncated}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="Explicit repository files to include in order")
    parser.add_argument("--max-chars", type=int, default=30000)
    parser.add_argument("--output", default="output/prompt-context.json")
    args = parser.parse_args()
    if args.max_chars <= 0:
        parser.error("--max-chars must be positive")
    data = assemble(args.paths, max_chars=args.max_chars)
    write_json(args.output, data)
    print(f"Assembled {len(data['sources'])} source(s), {data['characters']} chars -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
