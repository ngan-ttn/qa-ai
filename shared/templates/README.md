# Templates

## Overview

The `shared/templates/` directory contains reusable templates for common QA artifacts and AI-assisted documentation.

Each template provides a standardized document structure that can be adapted to different projects while remaining consistent with the repository standards.

---

## Template Catalog

| Template | Purpose |
|----------|---------|
| `Requirement-Analysis.md` | Analyze requirements and identify testable information before test design. |
| `Business-Rule.md` | Extract, organize, and document business rules from requirements. |
| `Scenario.md` | Define high-level test scenarios covering functional and business behaviors. |
| `TestCase.md` | Create detailed and executable test cases for validation. |
| `Bug-Report.md` | Record software defects using a consistent reporting structure. |
| `Regression.md` | Define regression testing scope and execution strategy. |
| `Risk-Analysis.md` | Identify testing risks, impacts, assumptions, and mitigation strategies. |

---

## Recommended Workflow

Most QA activities follow a progressive workflow where the output of one template becomes the input for the next.

```text
Requirement Analysis
          │
          ▼
Business Rules
          │
          ▼
Test Scenarios
          │
          ▼
Test Cases
          │
          ▼
Bug Reports
          │
          ▼
Regression Planning
          │
          ▼
Risk Analysis
```

Depending on the project, individual templates may also be used independently.

---

## Usage

When creating a new document:

1. Select the template that matches the intended artifact.
2. Copy the template into the project documentation.
3. Replace placeholder content with project-specific information.
4. Remove sections that are not applicable.
5. Keep the overall structure consistent unless customization is required.

---

## Related Standards

All templates should comply with the standards defined in:

- `shared/standards/Metadata.md`
- `shared/standards/Naming.md`
- `shared/standards/Documentation.md`
- `shared/standards/Output.md`
- `shared/standards/Prompt.md`