"""Build deterministic benchmark evidence from artifacts and canonical evaluation results.

Text comparison is supporting evidence only. QA-AI benchmark quality conclusions come from
canonical evaluation results; wording or formatting differences must not be treated as
quality regression by themselves.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.evaluation.compare_output import compare
from scripts.utils.file_utils import read_json, read_text, write_json


def _validate_score(score: object) -> dict[str, object]:
    if not isinstance(score, dict):
        raise ValueError("score file must contain a JSON object")
    result = score.get("result")
    final_score = score.get("final_score")
    failures = score.get("critical_failures", [])
    if result not in {"PASS", "FAIL"}:
        raise ValueError("score file result must be PASS or FAIL")
    if not isinstance(final_score, (int, float)) or isinstance(final_score, bool):
        raise ValueError("score file requires numeric final_score")
    if not isinstance(failures, list):
        raise ValueError("score file critical_failures must be a list")
    if result == "PASS" and failures:
        raise ValueError("PASS score file cannot contain unresolved critical failures")
    return score


def run(golden: str, actual: str, score_file: str | None = None) -> dict[str, object]:
    comparison = compare(read_text(golden), read_text(actual))
    score = _validate_score(read_json(score_file)) if score_file else None
    return {
        "golden": golden,
        "actual": actual,
        "comparison": comparison,
        "comparison_role": "supporting-evidence-only",
        "quality_score": score,
        "benchmark_result": score["result"] if score is not None else "UNSCORED",
        "note": (
            "Textual similarity is not a canonical quality gate. Provide --score-file from "
            "canonical evaluation scoring to produce PASS/FAIL benchmark evidence."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("golden")
    parser.add_argument("actual")
    parser.add_argument("--score-file", help="Canonical evaluation score JSON from score_format.py")
    parser.add_argument("--output", default="output/benchmark-result.json")
    args = parser.parse_args()
    result = run(args.golden, args.actual, args.score_file)
    write_json(args.output, result)
    print(
        f"Benchmark result={result['benchmark_result']} "
        f"similarity={result['comparison']['similarity']}% -> {args.output}"
    )
    if result["benchmark_result"] == "PASS":
        return 0
    if result["benchmark_result"] == "FAIL":
        return 2
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
