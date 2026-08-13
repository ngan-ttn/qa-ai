"""Export structured JSON data to an XLSX workbook using openpyxl."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import read_json, resolve_repo_path


def normalize_rows(data: Any) -> tuple[list[str], list[list[Any]]]:
    if isinstance(data, list) and all(isinstance(item, dict) for item in data):
        headers = list(dict.fromkeys(key for item in data for key in item.keys()))
        return headers, [[item.get(key) for key in headers] for item in data]
    if isinstance(data, dict):
        return ["Key", "Value"], [[key, value] for key, value in data.items()]
    if isinstance(data, list):
        return ["Value"], [[item] for item in data]
    return ["Value"], [[data]]


def export_xlsx(data: Any, output: str | Path, *, sheet_name: str = "Output") -> Path:
    try:
        from openpyxl import Workbook
    except ImportError as exc:
        raise RuntimeError("openpyxl is required for Excel export") from exc

    headers, rows = normalize_rows(data)
    wb = Workbook()
    ws = wb.active
    ws.title = sheet_name[:31] or "Output"
    ws.append(headers)
    for row in rows:
        ws.append([str(value) if isinstance(value, (dict, list)) else value for value in row])
    for column in ws.columns:
        max_len = max((len(str(cell.value)) if cell.value is not None else 0 for cell in column), default=0)
        ws.column_dimensions[column[0].column_letter].width = min(max(max_len + 2, 10), 60)
    target = resolve_repo_path(output)
    target.parent.mkdir(parents=True, exist_ok=True)
    wb.save(target)
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Structured JSON input")
    parser.add_argument("--sheet", default="Output")
    parser.add_argument("--output", default="output/export.xlsx")
    args = parser.parse_args()
    target = export_xlsx(read_json(args.input), args.output, sheet_name=args.sheet)
    print(f"Excel exported -> {target.relative_to(ROOT) if target.is_relative_to(ROOT) else target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
