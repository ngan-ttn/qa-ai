"""Compute canonical QA-AI artifact quality score from rubric levels."""
from __future__ import annotations

import argparse
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import read_json, write_json

FACTORS = {"L4": 1.00, "L3": 0.80, "L2": 0.50, "L1": 0.25, "L0": 0.00}
WEIGHTS = {"C01": 15, "C02": 15, "C03": 12, "C04": 8, "C05": 8, "C06": 10,
           "C07": 5, "C08": 7, "C09": 5, "C10": 5, "C11": 5, "C12": 5}
CAPS = {"CF-01": 49, "CF-02": 49, "CF-03": 69, "CF-04": 49, "CF-05": 69, "CF-06": 59, "CF-07": 49}


def half_up(value: float) -> int:
    return int(Decimal(str(value)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def quality_band(score: int) -> str:
    if score >= 95: return "Excellent"
    if score >= 85: return "Good"
    if score >= 70: return "Acceptable"
    if score >= 50: return "Weak"
    return "Failed"


def score(levels: dict[str, str], critical_failures: list[str] | None = None) -> dict[str, object]:
    unknown = sorted(set(levels) - set(WEIGHTS))
    if unknown:
        raise ValueError(f"Unknown criteria: {', '.join(unknown)}")
    details: dict[str, object] = {}
    active_weight = 0
    raw = 0.0
    for criterion, weight in WEIGHTS.items():
        level = levels.get(criterion)
        if level is None:
            raise ValueError(f"Missing criterion: {criterion}; use N/A only when canonically justified")
        if level == "N/A":
            details[criterion] = {"weight": weight, "level": level, "weighted_score": None}
            continue
        if level not in FACTORS:
            raise ValueError(f"Invalid level for {criterion}: {level}")
        active_weight += weight
        weighted = weight * FACTORS[level]
        raw += weighted
        details[criterion] = {"weight": weight, "level": level, "factor": FACTORS[level], "weighted_score": round(weighted, 2)}
    if active_weight == 0:
        raise ValueError("Active weight cannot be zero")
    normalized = raw / active_weight * 100
    failures = list(critical_failures or [])
    invalid_cf = sorted(set(failures) - set(CAPS))
    if invalid_cf:
        raise ValueError(f"Unknown critical failures: {', '.join(invalid_cf)}")
    cap = min((CAPS[item] for item in failures), default=None)
    final_unrounded = min(normalized, cap) if cap is not None else normalized
    final = half_up(final_unrounded)
    return {
        "criteria": details,
        "raw_weighted_score": round(raw, 2),
        "active_weight": active_weight,
        "normalized_score": round(normalized, 2),
        "critical_failures": failures,
        "applied_cap": cap,
        "final_unrounded_score": round(final_unrounded, 2),
        "final_score": final,
        "quality_band": quality_band(final),
        "result": "PASS" if final >= 85 and not failures else "FAIL",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="JSON: {levels:{C01:L4,...}, critical_failures:[CF-..]}")
    parser.add_argument("--output", default="output/evaluation-score.json")
    args = parser.parse_args()
    data = read_json(args.input)
    result = score(data.get("levels", {}), data.get("critical_failures", []))
    write_json(args.output, result)
    print(f"{result['result']} score={result['final_score']} band={result['quality_band']} -> {args.output}")
    return 0 if result["result"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
