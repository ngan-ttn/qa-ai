"""Validate Markdown table shape and cell-count consistency in QA artifacts."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SEPARATOR_CELL = re.compile(r":?-{3,}:?")


def split_cells(line: str) -> list[str] | None:
    """Split a pipe-delimited row while ignoring escaped pipe characters."""
    text = line.strip()
    if not (text.startswith("|") and text.endswith("|")):
        return None
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in text[1:-1]:
        if char == "|" and not escaped:
            cells.append("".join(current).strip())
            current = []
            continue
        current.append(char)
        if char == "\\" and not escaped:
            escaped = True
        else:
            escaped = False
    cells.append("".join(current).strip())
    return cells


def is_separator(cells: list[str] | None) -> bool:
    return cells is not None and bool(cells) and all(
        SEPARATOR_CELL.fullmatch(cell.replace(" ", "")) for cell in cells
    )


def table_errors(text: str) -> list[str]:
    """Return line-specific errors for malformed Markdown tables.

    Fenced code blocks are skipped so that documented examples are not treated as
    rendered tables. Canonical table rows must have leading/trailing pipes.
    """
    lines = text.splitlines()
    errors: list[str] = []
    in_fence = False
    fence_char = ""
    fence_size = 0
    idx = 0

    while idx < len(lines):
        stripped = lines[idx].lstrip()
        fence = re.match(r"^(`{3,}|~{3,})", stripped)
        if fence:
            token = fence.group(1)
            if not in_fence:
                in_fence = True
                fence_char = token[0]
                fence_size = len(token)
            elif token[0] == fence_char and len(token) >= fence_size:
                in_fence = False
            idx += 1
            continue
        if in_fence:
            idx += 1
            continue

        header = split_cells(lines[idx])
        separator = split_cells(lines[idx + 1]) if idx + 1 < len(lines) else None
        if header is None or separator is None or not is_separator(separator):
            idx += 1
            continue

        start_line = idx + 1
        if len(header) != len(separator):
            errors.append(
                f"line {start_line}: header has {len(header)} cell(s), "
                f"separator has {len(separator)}"
            )
        blank_headers = [position + 1 for position, cell in enumerate(header) if not cell]
        if blank_headers:
            errors.append(
                f"line {start_line}: blank header cell(s) at column(s) "
                + ", ".join(map(str, blank_headers))
            )
        expected = len(header)
        idx += 2
        while idx < len(lines):
            row = split_cells(lines[idx])
            if row is None:
                break
            if len(row) != expected:
                errors.append(
                    f"line {idx + 1}: table row has {len(row)} cell(s); expected {expected}"
                )
            idx += 1
        continue

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="Markdown files to validate")
    args = parser.parse_args()
    checked = 0
    issues = 0
    for raw_path in args.paths:
        path = Path(raw_path)
        if not path.is_file():
            print(f"ERROR {path}: file not found")
            issues += 1
            continue
        checked += 1
        try:
            text = path.read_text(encoding="utf-8-sig")
        except UnicodeError as exc:
            print(f"ERROR {path}: cannot decode UTF-8: {exc}")
            issues += 1
            continue
        found = table_errors(text)
        for issue in found:
            print(f"ERROR {path}: {issue}")
        issues += len(found)
    print(f"Checked {checked} Markdown file(s); table issues={issues}")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
