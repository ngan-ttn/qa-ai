"""Assemble deterministic prompt context from explicit QA-AI source files."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import read_text, relative_to_repo, resolve_repo_path, write_json


def assemble(paths: list[str], *, max_chars: int = 30000) -> dict[str, object]:
    sources: list[dict[str, str]] = []
    used = 0
    for raw in paths:
        path = resolve_repo_path(raw)
        text = read_text(path).strip()
        remaining = max_chars - used
        if remaining <= 0:
            break
        clipped = text[:remaining]
        sources.append({"path": relative_to_repo(path), "content": clipped})
        used += len(clipped)
    return {
        "sources": sources,
        "characters": used,
        "truncated": any(len(read_text(item)) > len(next(s["content"] for s in sources if s["path"] == relative_to_repo(item))) for item in [resolve_repo_path(p) for p in paths[:len(sources)]]) if sources else False,
    }


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
