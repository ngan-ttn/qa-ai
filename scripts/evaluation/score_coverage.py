"""Score traceability coverage from explicit expected and covered identifiers."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import read_json, write_json


def score_coverage(expected: list[str], covered: list[str]) -> dict[str, object]:
    expected_set = {str(x).strip() for x in expected if str(x).strip()}
    covered_set = {str(x).strip() for x in covered if str(x).strip()}
    if not expected_set:
        raise ValueError("expected identifiers cannot be empty")
    matched = expected_set & covered_set
    missing = expected_set - covered_set
    extra = covered_set - expected_set
    percent = len(matched) / len(expected_set) * 100
    return {
        "expected": len(expected_set),
        "covered": len(matched),
        "coverage_percent": round(percent, 2),
        "missing": sorted(missing),
        "extra": sorted(extra),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="JSON object with expected[] and covered[]")
    parser.add_argument("--output", default="output/coverage-score.json")
    args = parser.parse_args()
    data = read_json(args.input)
    result = score_coverage(data.get("expected", []), data.get("covered", []))
    write_json(args.output, result)
    print(f"Coverage {result['covered']}/{result['expected']} = {result['coverage_percent']}% -> {args.output}")
    return 0 if not result["missing"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
