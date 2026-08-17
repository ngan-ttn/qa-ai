"""Validate generated/example QA output artifacts for deterministic structural defects."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.utils.file_utils import iter_files, relative_to_repo

# Generic words such as "placeholder" are valid in test-data guidance (for example,
# credential placeholders) and must not be treated as unresolved work. Detect only
# explicit authoring markers and unresolved template dates.
UNRESOLVED_MARKERS = re.compile(r"\b(TODO|TBD|FIXME)\b|YYYY-MM-DD", re.I)
HEADING = re.compile(r"^#{1,6}\s+\S", re.M)
TESTCASE_SECTION_PER_ITEM = re.compile(r"^#{2,6}\s+TC(?:-[A-Z0-9]+)+\b", re.M | re.I)

# Table-oriented output contracts apply to current curated examples/golden references.
# Historical runtime evidence under output/ or benchmark run records is intentionally
# excluded from this representation check because it must remain immutable evidence.
CANONICAL_TABLE_HEADERS = {
    "Business-Rules.md": "| Rule ID | Rule Type | Business Rule | Conditions / Inputs | Expected Outcome / Constraint | Source Traceability | Dependencies | Status |",
    "Risk-Analysis.md": "| Risk ID | Area / Feature | Risk Description | Trigger / Cause | Impact | Likelihood | Severity / Exposure | Mitigation / QA Focus | Traceability | Status |",
    "Test-Scenarios.md": "| Scenario ID | Module / Feature | Scenario | Type | Preconditions / Conditions | Expected Behavior | Requirement / Rule Traceability | Risk Traceability | Priority |",
    "Test-Cases.md": "| Test Case ID | Module / Function | Scenario ID | Test Case Title | Preconditions / Setup | Test Steps | Test Data | Expected Result | Priority | Traceability |",
    "Regression-Analysis.md": "| Impact ID | Area / Module | Change Relationship | Regression Scope / Behavior to Revalidate | Impact Type | Evidence / Traceability | Priority | Existing Coverage Reference | Decision |",
}

GOLDEN_SUFFIX_HEADERS = {
    "-Business-Rules.md": CANONICAL_TABLE_HEADERS["Business-Rules.md"],
    "-Risk-Analysis.md": CANONICAL_TABLE_HEADERS["Risk-Analysis.md"],
    "-Test-Scenarios.md": CANONICAL_TABLE_HEADERS["Test-Scenarios.md"],
    "-Test-Cases.md": CANONICAL_TABLE_HEADERS["Test-Cases.md"],
    "-Regression-Analysis.md": CANONICAL_TABLE_HEADERS["Regression-Analysis.md"],
}

REGRESSION_TIER_MARKERS = (
    "Minimum / Release-Gate Regression",
    "Recommended Regression",
    "Full Changed-Feature Verification",
)

COVERAGE_STATUS_MARKERS = (
    "Covered",
    "Weakly Covered",
    "Gap",
    "Blocked",
)


def canonical_header_for(path: Path) -> str | None:
    """Return required canonical table header for curated list-oriented QA outputs."""
    rel = relative_to_repo(path)
    if "/expected-output/" in f"/{rel}":
        return CANONICAL_TABLE_HEADERS.get(path.name)
    if rel.startswith("datasets/golden-output/"):
        for suffix, header in GOLDEN_SUFFIX_HEADERS.items():
            if path.name.endswith(suffix):
                return header
    return None


def is_curated_testcase(path: Path) -> bool:
    rel = relative_to_repo(path)
    return (
        ("/expected-output/" in f"/{rel}" and path.name == "Test-Cases.md")
        or (rel.startswith("datasets/golden-output/") and path.name.endswith("-Test-Cases.md"))
    )


def is_curated_regression(path: Path) -> bool:
    rel = relative_to_repo(path)
    return (
        ("/expected-output/" in f"/{rel}" and path.name == "Regression-Analysis.md")
        or (rel.startswith("datasets/golden-output/") and path.name.endswith("-Regression-Analysis.md"))
    )


def is_curated_coverage_review(path: Path) -> bool:
    rel = relative_to_repo(path)
    return "/expected-output/" in f"/{rel}" and path.name == "Coverage-Review.md"


def should_check_authoring_markers(path: Path) -> bool:
    """Return whether unresolved authoring markers are defects for this artifact.

    Generated ChatGPT Knowledge bundles are deterministic concatenations of canonical
    framework sources. They intentionally preserve template authoring tokens such as
    ``YYYY-MM-DD`` and ``TBD`` when those tokens are part of the source documentation,
    so treating them as unresolved generated-output work produces false positives.
    Curated expected outputs, golden outputs, and other generated deliverables remain
    subject to the unresolved-marker check.
    """
    rel = relative_to_repo(path)
    return not rel.startswith("output/chatgpt-knowledge/")


def validate_testcase_contract(text: str) -> list[str]:
    errors: list[str] = []
    header = CANONICAL_TABLE_HEADERS["Test-Cases.md"]
    if text.count(header) != 1:
        errors.append("testcase artifact must contain exactly one canonical testcase inventory header")
    if TESTCASE_SECTION_PER_ITEM.search(text):
        errors.append("section-per-testcase rendering is not canonical; TC-* must be rows in the single testcase table")
    return errors


def validate_regression_contract(text: str) -> list[str]:
    errors: list[str] = []
    for marker in REGRESSION_TIER_MARKERS:
        if marker not in text:
            errors.append(f"missing canonical regression scope tier: {marker}")
    return errors


def validate_coverage_contract(text: str) -> list[str]:
    errors: list[str] = []
    for marker in COVERAGE_STATUS_MARKERS:
        if marker not in text:
            errors.append(f"missing canonical coverage status semantic: {marker}")
    if re.search(r"\|\s*Partial\s*\|", text, re.I):
        errors.append("legacy coverage status 'Partial' found; use 'Weakly Covered'")
    if re.search(r"\|\s*Clarification-Dependent\s*\|", text, re.I):
        errors.append("legacy coverage sufficiency status 'Clarification-Dependent' found; use 'Blocked' for unresolved oracle/dependency")
    return errors


def validate_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return ["empty artifact"]
    errors: list[str] = []
    if path.suffix.lower() == ".md":
        if not HEADING.search(text):
            errors.append("Markdown artifact has no heading")
        if should_check_authoring_markers(path):
            hit = UNRESOLVED_MARKERS.search(text)
            if hit:
                errors.append(f"unresolved authoring marker: {hit.group(0)}")

        required_header = canonical_header_for(path)
        if required_header and required_header not in text:
            errors.append("missing canonical table-oriented core header")

        if is_curated_testcase(path):
            errors.extend(validate_testcase_contract(text))
        if is_curated_regression(path):
            errors.extend(validate_regression_contract(text))
        if is_curated_coverage_review(path):
            errors.extend(validate_coverage_contract(text))
    return errors


def is_output_artifact(path: Path) -> bool:
    rel = relative_to_repo(path)
    return "/expected-output/" in f"/{rel}" or rel.startswith("datasets/golden-output/") or rel.startswith("output/")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", default=["examples", "datasets/golden-output", "output"])
    args = parser.parse_args()
    checked = 0
    issues = 0
    for base in args.paths:
        for path in iter_files(base, ("*.md", "*.json", "*.txt")):
            if not is_output_artifact(path):
                continue
            checked += 1
            for issue in validate_file(path):
                issues += 1
                print(f"ERROR {relative_to_repo(path)}: {issue}")
    print(f"Checked {checked} output artifact(s); issues={issues}")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
