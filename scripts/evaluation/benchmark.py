"""Run deterministic QA-AI benchmark checks over existing artifacts.

The runner compares an actual artifact to a golden artifact and can optionally attach
an already-recorded canonical rubric score. It does not invoke an AI model.
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.evaluation.compare_output import compare
from scripts.utils.file_utils import read_json, read_text, write_json


def run(golden: str, actual: str, score_file: str | None = None) -> dict[str, object]:
    comparison = compare(read_text(golden), read_text(actual))
    score = read_json(score_file) if score_file else None
    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "golden": golden,
        "actual": actual,
        "comparison": comparison,
        "quality_score": score,
    }
    if score is not None:
        result["benchmark_result"] = score.get("result", "UNKNOWN")
    else:
        result["benchmark_result"] = "MATCH" if comparison["exact_after_normalization"] else "DIFF"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("golden")
    parser.add_argument("actual")
    parser.add_argument("--score-file")
    parser.add_argument("--output", default="output/benchmark-result.json")
    args = parser.parse_args()
    result = run(args.golden, args.actual, args.score_file)
    write_json(args.output, result)
    print(f"Benchmark result={result['benchmark_result']} similarity={result['comparison']['similarity']}% -> {args.output}")
    return 0 if result["benchmark_result"] in {"PASS", "MATCH"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
