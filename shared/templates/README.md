# Templates

## Overview

The `shared/templates/` directory contains reusable templates for common QA artifacts and AI-assisted documentation.

Each template provides a standardized document structure that can be adapted to different projects while remaining consistent with repository standards.

---

## Template Catalog

| Template | Purpose | Canonical Core Format |
|---|---|---|
| `Requirement-Analysis.md` | Analyze requirements and identify testable information before test design. | Section-based with tables where useful |
| `Business-Rule.md` | Extract, organize, and document business rules from requirements. | Hybrid + rule inventory table |
| `Risk-Analysis.md` | Identify testing risks, impacts, assumptions, and mitigation focus. | Hybrid + risk register table |
| `Scenario.md` | Define high-level test scenarios covering functional and business behaviors. | Hybrid + scenario inventory table |
| `TestCase.md` | Create detailed and executable test cases for validation. | Hybrid + executable testcase table |
| `Regression.md` | Define regression impact and revalidation scope after change. | Hybrid + regression-impact table |
| `Bug-Report.md` | Record software defects using a consistent reporting structure. | Section-based |
| `Knowledge-Article.md` | Structure reusable knowledge articles. | Section-based |

---

## Table-Oriented QA Artifacts

Business Rules, Risk Analysis, Test Scenarios, Test Cases, and Regression Analysis represent collections of comparable QA records. Their core inventories therefore use canonical Markdown tables.

Document-level context remains in surrounding sections when useful. The table is the canonical record representation and should not be replaced by repeated per-item subsections in normal generated output.

This improves:

- Manual QC scanability and review;
- stable ID and traceability visibility;
- comparison across related artifacts;
- spreadsheet/test-management export;
- deterministic downstream processing.

Platform adapters may transform presentation, but they must preserve the semantic fields defined by the canonical template.

---

## Recommended Artifact Flow

```text
Requirement Analysis
          ↓
Business Rules
          ↓
Risk Analysis (when applicable)
          ↓
Test Scenarios
          ↓
Test Cases
```

Regression Analysis is change-driven and consumes an authoritative change delta plus relevant baseline context/coverage. Bug Reports are execution/defect artifacts rather than a mandatory next stage of testcase generation.

Individual templates may also be used independently when their required inputs are available.

---

## Usage

When creating an artifact:

1. Select the template that matches the intended artifact.
2. Preserve the canonical core fields and format.
3. Replace placeholder content with source-grounded project information.
4. Keep unsupported behavior in assumptions/open questions rather than inventing expected results.
5. Remove only optional surrounding sections that are genuinely not applicable; do not remove required canonical table columns casually.
6. Keep the output aligned with `shared/standards/Output.md`.

---

## Related Standards

All templates should comply with:

- `shared/standards/Metadata.md`
- `shared/standards/Naming.md`
- `shared/standards/Documentation.md`
- `shared/standards/Output.md`
- `shared/standards/Prompt.md`
