"""Compare two text artifacts deterministically and emit a structured diff summary."""
from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import read_text, write_json


def normalize(text: str) -> list[str]:
    lines: list[str] = []
    for raw in text.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        line = re.sub(r"[ \t]+", " ", raw.strip())
        if line:
            lines.append(line)
    return lines


def compare(expected_text: str, actual_text: str) -> dict[str, object]:
    expected = normalize(expected_text)
    actual = normalize(actual_text)
    matcher = difflib.SequenceMatcher(a=expected, b=actual, autojunk=False)
    opcodes = matcher.get_opcodes()
    changes = []
    for tag, i1, i2, j1, j2 in opcodes:
        if tag == "equal":
            continue
        changes.append({
            "type": tag,
            "expected_lines": expected[i1:i2],
            "actual_lines": actual[j1:j2],
        })
    return {
        "similarity": round(matcher.ratio() * 100, 2),
        "expected_nonempty_lines": len(expected),
        "actual_nonempty_lines": len(actual),
        "change_blocks": len(changes),
        "exact_after_normalization": expected == actual,
        "changes": changes,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("expected")
    parser.add_argument("actual")
    parser.add_argument("--output", default="output/output-comparison.json")
    args = parser.parse_args()
    result = compare(read_text(args.expected), read_text(args.actual))
    write_json(args.output, result)
    print(f"Similarity={result['similarity']}% changes={result['change_blocks']} -> {args.output}")
    return 0 if result["exact_after_normalization"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
