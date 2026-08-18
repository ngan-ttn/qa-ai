"""Parse canonical QA-AI Test-Cases.md into a normalized export model."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HEADERS = [
    "Test Case ID", "Module / Function", "Scenario ID", "Test Case Title",
    "Preconditions / Setup", "Test Steps", "Test Data", "Expected Result",
    "Priority", "Traceability",
]
FIELD_MAP = {
    "Test Case ID": "test_case_id",
    "Module / Function": "module_function",
    "Scenario ID": "scenario_id",
    "Test Case Title": "title",
    "Preconditions / Setup": "preconditions_setup",
    "Test Steps": "steps",
    "Test Data": "test_data",
    "Expected Result": "expected_result",
    "Priority": "priority",
    "Traceability": "traceability",
}


def source_checksum(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _split_row(line: str) -> list[str]:
    text = line.strip()
    if not text.startswith("|") or not text.endswith("|"):
        raise ValueError(f"not a Markdown table row: {line}")
    text = text[1:-1]
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in text:
        if escaped:
            current.append(char)
            escaped = False
        elif char == "\\":
            escaped = True
            current.append(char)
        elif char == "|":
            cells.append("".join(current).strip().replace("\\|", "|"))
            current = []
        else:
            current.append(char)
    cells.append("".join(current).strip().replace("\\|", "|"))
    return cells


def parse_table(lines: list[str], start: int) -> tuple[list[str], list[dict[str, str]], int]:
    headers = _split_row(lines[start])
    if start + 1 >= len(lines):
        raise ValueError("table separator is missing")
    separator = _split_row(lines[start + 1])
    if len(separator) != len(headers) or not all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in separator):
        raise ValueError("invalid Markdown table separator")
    rows: list[dict[str, str]] = []
    idx = start + 2
    while idx < len(lines) and lines[idx].strip().startswith("|"):
        cells = _split_row(lines[idx])
        if len(cells) != len(headers):
            raise ValueError(f"table row has {len(cells)} cells; expected {len(headers)} at line {idx + 1}")
        rows.append(dict(zip(headers, cells)))
        idx += 1
    return headers, rows, idx


def find_table_after_heading(text: str, heading: str) -> tuple[list[str], list[dict[str, str]]]:
    lines = text.splitlines()
    heading_index = next((i for i, line in enumerate(lines) if line.strip() == heading), None)
    if heading_index is None:
        raise ValueError(f"missing canonical heading: {heading}")
    for idx in range(heading_index + 1, len(lines)):
        if lines[idx].startswith("## ") and idx > heading_index + 1:
            break
        if lines[idx].strip().startswith("|"):
            headers, rows, _ = parse_table(lines, idx)
            return headers, rows
    raise ValueError(f"missing canonical table under {heading}")


def _normalize_steps(value: str) -> list[str]:
    parts = re.split(r"\s*<br\s*/?>\s*|\r?\n", value, flags=re.I)
    return [part.strip() for part in parts if part.strip()]


def parse(path: str | Path) -> dict[str, object]:
    source = Path(path)
    text = source.read_text(encoding="utf-8-sig")
    if re.search(r"^###\s+TC-", text, flags=re.M):
        raise ValueError("section-per-testcase representation is non-canonical")
    headers, raw_rows = find_table_after_heading(text, "## Test Cases")
    if headers != HEADERS:
        raise ValueError(f"noncanonical Test Case headers/order: {headers}")
    records: list[dict[str, object]] = []
    seen: set[str] = set()
    for row in raw_rows:
        tc_id = row["Test Case ID"].strip()
        if not re.fullmatch(r"TC-[A-Za-z0-9-]+", tc_id):
            raise ValueError(f"invalid Test Case ID: {tc_id}")
        if tc_id in seen:
            raise ValueError(f"duplicate Test Case ID: {tc_id}")
        seen.add(tc_id)
        record: dict[str, object] = {}
        for header in HEADERS:
            key = FIELD_MAP[header]
            record[key] = _normalize_steps(row[header]) if header == "Test Steps" else row[header].strip()
        records.append(record)
    return {
        "schema_version": "1.0",
        "artifact_type": "test-cases",
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
        print(f"Parsed {len(model['records'])} testcase(s) -> {args.output}")
    else:
        print(body, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
