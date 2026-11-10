"""Export canonical QA-AI Markdown artifacts to generic XLSX or CSV with provenance metadata."""
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

EXPORT_DIR = Path(__file__).resolve().parent
ROOT = EXPORT_DIR.parents[1]
if str(EXPORT_DIR) not in sys.path:
    sys.path.insert(0, str(EXPORT_DIR))
from parse_testcases import parse as parse_testcases
from parse_coverage import parse as parse_coverage
from parse_regression import parse as parse_regression

PARSERS = {"test-cases": parse_testcases, "coverage-review": parse_coverage, "regression-analysis": parse_regression}

TC_HEADERS = ["Test Case ID", "Module / Function", "Scenario ID", "Test Case Title", "Preconditions / Setup", "Test Steps", "Test Data", "Expected Result", "Priority", "Traceability"]
TC_KEYS = ["test_case_id", "module_function", "scenario_id", "title", "preconditions_setup", "steps", "test_data", "expected_result", "priority", "traceability"]
TC_OPERATIONAL_HEADERS = ["Status", "BUG ID", "Bug Priority", "Bug Status", "Note"]
TC_STATUSES = ["PASS", "FAIL", "NOT RUN", "PENDING"]
TC_STATUS_COLORS = {"PASS": "70AD47", "FAIL": "FF5050", "NOT RUN": "BFBFBF", "PENDING": "FFD966"}
BUG_PRIORITIES = ["High", "Medium", "Low"]
BUG_PRIORITY_COLORS = {"High": "FF5050", "Medium": "FFD966", "Low": "70AD47"}
BUG_STATUSES = ["Open", "In Progress", "Resolved", "Closed"]
BUG_STATUS_COLORS = {"Open": "FF5050", "In Progress": "FFD966", "Resolved": "5B9BD5", "Closed": "70AD47"}
REPORT_SHEET = "Report Test Case"

COVERAGE_HEADERS = ["Coverage Finding ID", "Coverage Status", "Related Source", "Current Evidence", "Finding", "Priority", "Recommended Owning Action"]
COVERAGE_KEYS = ["coverage_finding_id", "coverage_status", "related_source", "current_evidence", "finding", "priority", "recommended_owning_action"]

REGRESSION_HEADERS = ["Impact ID", "Area / Module", "Change Relationship", "Regression Scope / Behavior to Revalidate", "Impact Type", "Evidence / Traceability", "Priority", "Existing Coverage Reference", "Decision"]
REGRESSION_KEYS = ["impact_id", "area_module", "change_relationship", "behavior_to_revalidate", "impact_type", "evidence_traceability", "priority", "existing_coverage_reference", "decision"]

COLUMN_WIDTHS = {
    "Test Case ID": 16, "Module / Function": 24, "Scenario ID": 18, "Test Case Title": 36,
    "Preconditions / Setup": 40, "Test Steps": 55, "Test Data": 36, "Expected Result": 55,
    "Priority": 14, "Traceability": 34, "Status": 16, "BUG ID": 16,
    "Bug Priority": 16, "Bug Status": 18, "Note": 36,
    "Coverage Finding ID": 20, "Coverage Status": 20, "Related Source": 38, "Current Evidence": 38,
    "Finding": 55, "Recommended Owning Action": 55,
    "Impact ID": 14, "Area / Module": 28, "Change Relationship": 24,
    "Regression Scope / Behavior to Revalidate": 60, "Impact Type": 18, "Evidence / Traceability": 40,
    "Existing Coverage Reference": 42, "Decision": 22,
    "Tier": 38, "Reference ID": 22,
}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def git_revision() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return "unknown"


def _string(value: object) -> str:
    if isinstance(value, list):
        return "\n".join(str(x) for x in value)
    return "" if value is None else str(value)


def _record_rows(records: list[dict[str, object]], keys: list[str]) -> list[list[str]]:
    return [[_string(record.get(key)) for key in keys] for record in records]


def _rows(model: dict[str, object]) -> tuple[list[str], list[list[str]], str]:
    kind = model["artifact_type"]
    if kind == "test-cases":
        return TC_HEADERS, _record_rows(model["records"], TC_KEYS), "Test Cases"
    if kind == "coverage-review":
        return COVERAGE_HEADERS, _record_rows(model["records"], COVERAGE_KEYS), "Coverage Review"
    return REGRESSION_HEADERS, _record_rows(model["impact_records"], REGRESSION_KEYS), "Regression Impact"


def _write_csv(model: dict[str, object], output: Path) -> None:
    headers, rows, _ = _rows(model)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(headers)
        writer.writerows(rows)


def _font(bold: bool = False, color: str | None = None):
    from openpyxl.styles import Font

    return Font(name="Times New Roman", size=12, bold=bold, color=color)


def _apply_font(ws, min_row: int, max_row: int, min_col: int, max_col: int) -> None:
    for row in ws.iter_rows(min_row=min_row, max_row=max_row, min_col=min_col, max_col=max_col):
        for cell in row:
            cell.font = _font(bool(cell.font and cell.font.bold))


def _style_count(cell) -> None:
    from openpyxl.styles import Alignment

    cell.font = _font(True)
    cell.alignment = Alignment(horizontal="center", vertical="center")


def _center_title(cell) -> None:
    from openpyxl.styles import Alignment, PatternFill

    cell.font = _font(True, "FFFFFF")
    cell.fill = PatternFill("solid", fgColor="002060")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)


def _apply_borders(ws, min_row: int, max_row: int, min_col: int, max_col: int) -> None:
    from openpyxl.styles import Border, Side

    side = Side(style="thin", color="000000")
    border = Border(left=side, right=side, top=side, bottom=side)
    for row in ws.iter_rows(min_row=min_row, max_row=max_row, min_col=min_col, max_col=max_col):
        for cell in row:
            cell.border = border


def _format_sheet(ws, headers: list[str]) -> None:
    from openpyxl.styles import Alignment, Font

    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    ws.row_dimensions[1].height = 30
    for cell in ws[1]:
        cell.font = _font(True)
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    for row in ws.iter_rows(min_row=2, max_col=len(headers)):
        for cell in row:
            cell.alignment = Alignment(vertical="center", wrap_text=True)
    for index, header in enumerate(headers, start=1):
        letter = ws.cell(row=1, column=index).column_letter
        if header in COLUMN_WIDTHS:
            ws.column_dimensions[letter].width = COLUMN_WIDTHS[header]
            continue
        values = [ws.cell(row=row, column=index).value for row in range(1, ws.max_row + 1)]
        width = max((len(str(value or "").split("\n")[0]) for value in values), default=10)
        ws.column_dimensions[letter].width = min(max(width + 2, 12), 50)
    if headers and ws.max_row:
        _apply_font(ws, 1, ws.max_row, 1, len(headers))
        for cell in ws[1]:
            cell.font = _font(True)
            _center_title(cell)
        _apply_borders(ws, 1, ws.max_row, 1, len(headers))


def _count_block(ws, start_row: int, label: str, values: list[str], colors: dict[str, str], formula_range: str) -> tuple[int, int, int]:
    from openpyxl.styles import PatternFill

    ws.cell(start_row, 1, label).font = _font(True)
    ws.cell(start_row, 2, "Count").font = _font(True)
    first = start_row + 1
    for offset, value in enumerate(values):
        row = first + offset
        ws.cell(row, 1, value).font = _font(False)
        count = ws.cell(row, 2, f"=COUNTIF({formula_range},A{row})")
        _style_count(count)
        color = colors.get(value)
        if color:
            fill = PatternFill("solid", fgColor=color)
            ws.cell(row, 1).fill = fill
            ws.cell(row, 2).fill = fill
    total_row = first + len(values)
    ws.cell(total_row, 1, "Total").font = _font(True)
    total = ws.cell(total_row, 2, f"=SUM(B{first}:B{total_row - 1})" if values else 0)
    _style_count(total)
    return first, total_row - 1, total_row


def _chart_txpr():
    from openpyxl.chart.text import RichText
    from openpyxl.drawing.text import CharacterProperties, Font, Paragraph, ParagraphProperties, RichTextProperties

    props = CharacterProperties(
        sz=1000,
        latin=Font(typeface="Times New Roman"),
        ea=Font(typeface="Times New Roman"),
        cs=Font(typeface="Times New Roman"),
    )
    return RichText(bodyPr=RichTextProperties(), p=[Paragraph(pPr=ParagraphProperties(defRPr=props), endParaRPr=props)])


def _apply_chart_font(chart) -> None:
    from openpyxl.drawing.text import CharacterProperties, Font, ParagraphProperties

    props = CharacterProperties(
        sz=1000,
        latin=Font(typeface="Times New Roman"),
        ea=Font(typeface="Times New Roman"),
        cs=Font(typeface="Times New Roman"),
    )
    chart.txPr = _chart_txpr()
    if chart.title is not None:
        chart.title.txPr = _chart_txpr()
        rich = getattr(getattr(chart.title, "tx", None), "rich", None)
        if rich is not None:
            for paragraph in rich.p:
                paragraph.pPr = ParagraphProperties(defRPr=props)
                paragraph.endParaRPr = props
                for run in paragraph.r or []:
                    run.rPr = props
    if chart.legend is not None:
        chart.legend.txPr = _chart_txpr()
    if chart.dataLabels is not None:
        chart.dataLabels.txPr = _chart_txpr()


def _pie(ws, title: str, first: int, last: int, colors: list[str], anchor: str) -> None:
    from openpyxl.chart import PieChart, Reference
    from openpyxl.chart.label import DataLabelList
    from openpyxl.chart.legend import Legend
    from openpyxl.chart.series import DataPoint
    from openpyxl.chart.shapes import GraphicalProperties

    chart = PieChart()
    chart.title = title
    if chart.title is not None:
        chart.title.overlay = False
    from openpyxl.chart.data_source import AxDataSource, StrRef

    data = Reference(ws, min_col=2, min_row=first, max_row=last)
    labels = Reference(ws, min_col=1, min_row=first, max_row=last)
    chart.add_data(data, titles_from_data=False)
    chart.set_categories(labels)
    for series in chart.series:
        if series.cat is not None and series.cat.numRef is not None:
            series.cat = AxDataSource(strRef=StrRef(f=series.cat.numRef.f))
    chart.legend = Legend()
    chart.legend.position = "b"
    chart.legend.overlay = False
    chart.dataLabels = DataLabelList()
    chart.dataLabels.showPercent = True
    chart.dataLabels.showVal = False
    chart.dataLabels.showCatName = True
    chart.dataLabels.showSerName = False
    chart.dataLabels.showLeaderLines = True
    chart.width = 15
    chart.height = 8
    points = []
    for index, color in enumerate(colors):
        point = DataPoint(idx=index)
        point.graphicalProperties = GraphicalProperties(solidFill=color)
        points.append(point)
    chart.series[0].data_points = points
    _apply_chart_font(chart)
    ws.add_chart(chart, anchor)


def _write_testcase_report(wb, record_count: int) -> None:
    from openpyxl.styles import Alignment, Font

    ws = wb.create_sheet(REPORT_SHEET, 0)
    last = max(record_count + 1, 2)
    status_range = f"'Test Cases'!$K$2:$K${last}"
    bug_range = f"'Test Cases'!$L$2:$L${last}"
    bug_priority_range = f"'Test Cases'!$M$2:$M${last}"
    bug_status_range = f"'Test Cases'!$N$2:$N${last}"
    ws["A1"] = "Test Case Report"
    ws["A1"].font = _font(True)
    ws["A3"] = "Total test cases"
    ws["A3"].font = _font(True)
    total_cases = ws.cell(3, 2, f"=COUNTA('Test Cases'!A2:A{last})" if record_count else 0)
    _style_count(total_cases)
    status_first, status_last, status_total = _count_block(ws, 5, "Test case status", TC_STATUSES, TC_STATUS_COLORS, status_range)
    ws.cell(status_total + 1, 1, "Reconciliation")
    recon = ws.cell(status_total + 1, 2, f'=IF(B{status_total}=B3,"PASS + FAIL + NOT RUN + PENDING = "&B{status_total}&" unique test cases","Count mismatch")')
    recon.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[status_total + 1].height = 32
    _pie(ws, "Test case status", status_first, status_last, [TC_STATUS_COLORS[item] for item in TC_STATUSES], "D3")
    ws["A13"] = "Total bugs"
    ws["A13"].font = _font(True)
    total_bugs = ws.cell(13, 2, f"=COUNTA({bug_range})" if record_count else 0)
    _style_count(total_bugs)
    priority_first, priority_last, priority_total = _count_block(ws, 15, "Bug priority", BUG_PRIORITIES, BUG_PRIORITY_COLORS, bug_priority_range)
    _pie(ws, "Bug priority", priority_first, priority_last, [BUG_PRIORITY_COLORS[item] for item in BUG_PRIORITIES], "D20")
    bug_status_header = priority_total + 2
    status_bug_first, status_bug_last, bug_status_total = _count_block(ws, bug_status_header, "Bug status", BUG_STATUSES, BUG_STATUS_COLORS, bug_status_range)
    _pie(ws, "Bug status", status_bug_first, status_bug_last, [BUG_STATUS_COLORS[item] for item in BUG_STATUSES], "D36")
    ws.column_dimensions["A"].width = 28
    ws.column_dimensions["B"].width = 62
    for row in ws.iter_rows(min_col=1, max_col=2):
        for cell in row:
            if cell.alignment is None or cell.alignment.wrap_text is not True:
                cell.alignment = Alignment(vertical="center", wrap_text=False)
    _apply_borders(ws, 3, 3, 1, 2)
    _apply_borders(ws, 5, status_total + 1, 1, 2)
    _apply_borders(ws, 13, 13, 1, 2)
    _apply_borders(ws, 15, priority_total, 1, 2)
    _apply_borders(ws, bug_status_header, bug_status_total, 1, 2)
    _apply_font(ws, 1, bug_status_total, 1, 2)
    for row in (3, 13, *range(status_first, status_total + 1), *range(priority_first, priority_total + 1), *range(status_bug_first, bug_status_total + 1)):
        _style_count(ws.cell(row, 2))
    for row in (1, 3, 5, 13, 15, bug_status_header):
        _center_title(ws.cell(row, 1))
    for row in (5, 15, bug_status_header):
        _center_title(ws.cell(row, 2))


def _add_status_validation(ws, record_count: int) -> None:
    if record_count == 0:
        return
    from openpyxl.worksheet.datavalidation import DataValidation

    from openpyxl.formatting.rule import FormulaRule
    from openpyxl.styles import Alignment, PatternFill

    status_range = f"K2:K{record_count + 1}"
    status_list = DataValidation(type="list", formula1='"PASS,FAIL,NOT RUN,PENDING"', allow_blank=True)
    status_list.error = "Status must be PASS, FAIL, NOT RUN, or PENDING"
    status_list.errorTitle = "Invalid status"
    status_list.add(status_range)
    ws.add_data_validation(status_list)
    for row in range(2, record_count + 2):
        cell = ws.cell(row, 11)
        color = TC_STATUS_COLORS.get(str(cell.value or ""))
        cell.alignment = Alignment(vertical="center", horizontal="center", wrap_text=True)
        if color:
            cell.fill = PatternFill("solid", fgColor=color)
    for status, color in TC_STATUS_COLORS.items():
        ws.conditional_formatting.add(
            status_range,
            FormulaRule(
                formula=[f'K2="{status}"'],
                fill=PatternFill(fill_type="solid", start_color=color, end_color=color, fgColor=color),
            ),
        )
    priority_list = DataValidation(type="list", formula1='"High,Medium,Low"', allow_blank=True)
    priority_list.add(f"M2:M{record_count + 1}")
    ws.add_data_validation(priority_list)
    bug_status_list = DataValidation(type="list", formula1='"Open,In Progress,Resolved,Closed"', allow_blank=True)
    bug_status_list.add(f"N2:N{record_count + 1}")
    ws.add_data_validation(bug_status_list)


def _write_xlsx(model: dict[str, object], output: Path) -> None:
    try:
        from openpyxl import Workbook
    except ImportError as exc:
        raise RuntimeError("openpyxl is required for XLSX export") from exc

    headers, rows, sheet = _rows(model)
    if model["artifact_type"] == "test-cases":
        headers = [*headers, *TC_OPERATIONAL_HEADERS]
        rows = [row + ["NOT RUN", "", "", "", ""] for row in rows]
    wb = Workbook()
    ws = wb.active
    ws.title = sheet[:31]
    ws.append(headers)
    for row in rows:
        ws.append(row)
    _format_sheet(ws, headers)
    if model["artifact_type"] == "test-cases":
        _add_status_validation(ws, len(rows))
        _write_testcase_report(wb, len(rows))

    if model["artifact_type"] == "regression-analysis":
        tier_headers = ["Tier", "Reference ID"]
        tier_ws = wb.create_sheet("Regression Scope")
        tier_ws.append(tier_headers)
        titles = {
            "minimum_release_gate": "Minimum / Release-Gate Regression",
            "recommended": "Recommended Regression",
            "full_changed_feature": "Full Changed-Feature Verification",
        }
        for key, title in titles.items():
            for reference in model["tiers"][key]:
                tier_ws.append([title, reference])
        _format_sheet(tier_ws, tier_headers)

    output.parent.mkdir(parents=True, exist_ok=True)
    wb.save(output)


def export(source: Path, artifact_type: str, fmt: str, output: Path, profile: str) -> Path:
    if artifact_type == "regression-analysis" and fmt == "csv":
        raise ValueError("regression-analysis requires XLSX in the Phase 17 baseline because tier membership is multi-table data")
    model = PARSERS[artifact_type](source)
    _write_csv(model, output) if fmt == "csv" else _write_xlsx(model, output)
    count = len(model.get("records", model.get("impact_records", [])))
    metadata = {
        "schema_version": "1.0", "artifact_type": artifact_type,
        "source_path": source.as_posix(), "source_checksum": model["source_checksum"],
        "export_path": output.as_posix(), "export_format": fmt, "export_profile": profile,
        "record_count": count, "exported_at": now_iso(), "framework_revision": git_revision(),
    }
    sidecar = output.with_suffix(output.suffix + ".export.json")
    sidecar.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Exported {count} {artifact_type} record(s) -> {output}")
    print(f"Metadata -> {sidecar}")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input")
    parser.add_argument("--type", required=True, choices=tuple(PARSERS))
    parser.add_argument("--format", required=True, choices=("xlsx", "csv"))
    parser.add_argument("--profile", default="generic")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if args.profile != "generic":
        print("ERROR only the verified generic profile is supported in the Phase 17 baseline")
        return 1
    try:
        export(Path(args.input), args.type, args.format, Path(args.output), args.profile)
    except Exception as exc:
        print(f"ERROR {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
