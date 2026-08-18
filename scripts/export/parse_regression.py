"""Parse canonical QA-AI Regression-Analysis.md into a normalized export model."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

EXPORT_DIR = Path(__file__).resolve().parent
if str(EXPORT_DIR) not in sys.path:
    sys.path.insert(0, str(EXPORT_DIR))
from parse_testcases import parse_table, source_checksum

IMPACT_HEADERS = [
    "Impact ID", "Area / Module", "Change Relationship",
    "Regression Scope / Behavior to Revalidate", "Impact Type",
    "Evidence / Traceability", "Priority", "Existing Coverage Reference", "Decision",
]
TIERS = {
    "minimum_release_gate": "Minimum / Release-Gate Regression",
    "recommended": "Recommended Regression",
    "full_changed_feature": "Full Changed-Feature Verification",
}
REF_RE = re.compile(r"\b(?:TC|RI)-[A-Za-z0-9-]+\b")
RANGE_RE = re.compile(r"\b((?:TC|RI)-[A-Za-z-]*?)(\d+)\s*[–—-]\s*((?:TC|RI)-[A-Za-z-]*?)(\d+)\b")


def _find_impact_table(lines: list[str]) -> list[dict[str, str]]:
    for idx, line in enumerate(lines):
        if line.strip().startswith("|"):
            try:
                headers, rows, _ = parse_table(lines, idx)
            except ValueError:
                continue
            if headers == IMPACT_HEADERS:
                return rows
    raise ValueError("missing canonical regression impact table")


def _section_text(text: str, title: str) -> str:
    pattern = re.compile(
        rf"^###?\s+{re.escape(title)}\s*$\n(?P<body>.*?)(?=^###?\s+|\Z)",
        flags=re.M | re.S,
    )
    match = pattern.search(text)
    return match.group("body") if match else ""


def _references(body: str) -> list[str]:
    expanded: list[str] = []
    for match in RANGE_RE.finditer(body):
        prefix1, start, prefix2, end = match.groups()
        if prefix1 == prefix2:
            width = max(len(start), len(end))
            expanded.extend(f"{prefix1}{value:0{width}d}" for value in range(int(start), int(end) + 1))
    refs = REF_RE.findall(body)
    return list(dict.fromkeys([*refs, *expanded]))


def _extract_tier_ids(text: str) -> dict[str, list[str]]:
    explicit: dict[str, list[str]] = {}
    for key, title in TIERS.items():
        body = _section_text(text, title)
        if not body:
            match = re.search(
                rf"(?:\*\*)?{re.escape(title)}(?:\*\*)?\s*[:\-]?\s*(.*?)(?=(?:\*\*)?(?:Recommended Regression|Full Changed-Feature Verification)(?:\*\*)?|\Z)",
                text,
                flags=re.S,
            )
            body = match.group(1) if match else ""
        explicit[key] = _references(body)
    if not any(explicit.values()):
        raise ValueError("canonical regression scope tiers found no executable/impact references")
    minimum = explicit["minimum_release_gate"]
    recommended = list(dict.fromkeys([*minimum, *explicit["recommended"]]))
    full = list(dict.fromkeys([*recommended, *explicit["full_changed_feature"]]))
    return {
        "minimum_release_gate": minimum,
        "recommended": recommended,
        "full_changed_feature": full,
    }


def parse(path: str | Path) -> dict[str, object]:
    source = Path(path)
    text = source.read_text(encoding="utf-8-sig")
    impact_rows = _find_impact_table(text.splitlines())
    seen: set[str] = set()
    impact_records: list[dict[str, str]] = []
    for row in impact_rows:
        impact_id = row["Impact ID"].strip(" `")
        if not impact_id:
            raise ValueError("empty regression Impact ID")
        if impact_id in seen:
            raise ValueError(f"duplicate regression Impact ID: {impact_id}")
        seen.add(impact_id)
        impact_records.append({
            "impact_id": impact_id,
            "area_module": row["Area / Module"].strip(),
            "change_relationship": row["Change Relationship"].strip(),
            "behavior_to_revalidate": row["Regression Scope / Behavior to Revalidate"].strip(),
            "impact_type": row["Impact Type"].strip(" `"),
            "evidence_traceability": row["Evidence / Traceability"].strip(),
            "priority": row["Priority"].strip(),
            "existing_coverage_reference": row["Existing Coverage Reference"].strip(),
            "decision": row["Decision"].strip(" `"),
        })
    tiers = _extract_tier_ids(text)
    return {
        "schema_version": "1.0",
        "artifact_type": "regression-analysis",
        "source_path": source.as_posix(),
        "source_checksum": source_checksum(source),
        "impact_records": impact_records,
        "tiers": tiers,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        model = parse(args.input)
    except Exception as exc:
        print(f"ERROR {exc}")
        return 1
    body = json.dumps(model, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        Path(args.output).write_text(body, encoding="utf-8")
        print(f"Parsed {len(model['impact_records'])} regression impact(s) -> {args.output}")
    else:
        print(body, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
