"""Parse canonical QA-AI Coverage-Review.md into a normalized export model."""
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

CANONICAL_STATUSES = {"Covered", "Weakly Covered", "Gap", "Blocked"}
STATUS_HEADERS = {"Coverage Status", "Status", "Classification"}
ID_HEADERS = {"Coverage Finding ID", "Finding ID", "Coverage ID"}


def _key(header: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", header.lower()).strip("_")


def parse(path: str | Path) -> dict[str, object]:
    source = Path(path)
    text = source.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    candidate: tuple[list[str], list[dict[str, str]]] | None = None
    idx = 0
    while idx < len(lines):
        if lines[idx].strip().startswith("|"):
            try:
                headers, rows, end = parse_table(lines, idx)
            except ValueError:
                idx += 1
                continue
            status_header = next((h for h in headers if h in STATUS_HEADERS), None)
            id_header = next((h for h in headers if h in ID_HEADERS), None)
            if status_header and id_header and rows:
                statuses = {row.get(status_header, "").strip(" `") for row in rows}
                if statuses & CANONICAL_STATUSES:
                    candidate = (headers, rows)
                    break
            idx = end
        else:
            idx += 1
    if candidate is None:
        raise ValueError("missing canonical Coverage Review findings table with finding ID and canonical coverage classification")
    headers, rows = candidate
    status_header = next(h for h in headers if h in STATUS_HEADERS)
    id_header = next(h for h in headers if h in ID_HEADERS)
    seen: set[str] = set()
    records: list[dict[str, str]] = []
    for row in rows:
        finding_id = row[id_header].strip(" `")
        if not finding_id:
            raise ValueError("empty coverage finding ID")
        if finding_id in seen:
            raise ValueError(f"duplicate coverage finding ID: {finding_id}")
        seen.add(finding_id)
        status = row[status_header].strip(" `")
        if status not in CANONICAL_STATUSES:
            raise ValueError(f"noncanonical coverage status {status!r} for {finding_id}")
        record: dict[str, str] = {
            "coverage_finding_id": finding_id,
            "coverage_status": status,
        }
        for header, value in row.items():
            if header not in {id_header, status_header}:
                record[_key(header)] = value.strip()
        records.append(record)
    return {
        "schema_version": "1.0",
        "artifact_type": "coverage-review",
        "source_path": source.as_posix(),
        "source_checksum": source_checksum(source),
        "records": records,
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
        print(f"Parsed {len(model['records'])} coverage finding(s) -> {args.output}")
    else:
        print(body, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
