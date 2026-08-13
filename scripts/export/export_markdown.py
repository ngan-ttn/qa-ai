"""Export structured JSON data to readable deterministic Markdown."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import read_json, write_text


def scalar(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def render(value: Any, *, level: int = 2) -> str:
    if isinstance(value, dict):
        parts: list[str] = []
        for key, item in value.items():
            parts.append(f"{'#' * level} {key}")
            if isinstance(item, (dict, list)):
                parts.append(render(item, level=min(level + 1, 6)))
            else:
                parts.append(scalar(item))
        return "\n\n".join(parts)
    if isinstance(value, list):
        if value and all(isinstance(item, dict) for item in value):
            keys = list(dict.fromkeys(k for item in value for k in item.keys()))
            header = "| " + " | ".join(keys) + " |"
            sep = "|" + "|".join("---" for _ in keys) + "|"
            rows = ["| " + " | ".join(scalar(item.get(k)) for k in keys) + " |" for item in value]
            return "\n".join([header, sep, *rows])
        return "\n".join(f"- {scalar(item)}" for item in value)
    return scalar(value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Structured JSON input")
    parser.add_argument("--title", default="QA-AI Output")
    parser.add_argument("--output", default="output/export.md")
    args = parser.parse_args()
    body = f"# {args.title}\n\n{render(read_json(args.input))}\n"
    write_text(args.output, body)
    print(f"Markdown exported -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
