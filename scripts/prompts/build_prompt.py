"""Build a prompt package from instruction text and assembled source context."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import read_json, read_text, write_text


def build_prompt(instruction: str, context: dict[str, object]) -> str:
    sections = ["# Task", instruction.strip(), "# Source Context"]
    sources = context.get("sources", [])
    if not isinstance(sources, list):
        raise ValueError("context.sources must be a list")
    for item in sources:
        if not isinstance(item, dict) or "path" not in item or "content" not in item:
            raise ValueError("each context source requires path and content")
        sections.extend([
            f"## Source: {item['path']}",
            str(item["content"]).strip(),
        ])
    sections.extend([
        "# Grounding Rules",
        "- Use authoritative project sources before generic framework knowledge.",
        "- Do not invent missing project rules, values, schemas, policies, or evidence.",
        "- Surface unresolved ambiguity explicitly.",
    ])
    return "\n\n".join(sections).strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--instruction")
    group.add_argument("--instruction-file")
    parser.add_argument("--context", required=True, help="JSON created by assemble_context.py")
    parser.add_argument("--output", default="output/prompt.md")
    args = parser.parse_args()
    instruction = args.instruction if args.instruction is not None else read_text(args.instruction_file)
    prompt = build_prompt(instruction, read_json(args.context))
    write_text(args.output, prompt)
    print(f"Prompt written -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
