# Test Case

## Purpose

This template provides a structured approach for creating detailed and executable test cases based on approved test scenarios.

Its purpose is to define **how a feature should be verified**, ensuring that testing is consistent, repeatable, reviewable, and traceable to the original requirements, rules, and scenarios.

---

## When to Use

Use this template when:

- Translating approved test scenarios into executable tests.
- Preparing functional, integration, system, or acceptance testing.
- Building manual or automated test suites.
- Documenting verification procedures for software validation.
- Preparing test cases for spreadsheet or test-management export.

---

## Canonical Output Format

Test case documents use a **hybrid + table-oriented format**:

- suite-level context remains section-based;
- the complete executable test case inventory **MUST be represented by one canonical Markdown table** under `## Test Cases`;
- each executable test case **MUST occupy one row** in that canonical table;
- shared data/dependency notes, execution notes, open questions, and coverage summary remain sections when appropriate.

The canonical test case inventory **MUST NOT** be rendered as section-per-testcase content such as `### TC-001`, `### TC-002`, or repeated per-testcase metadata/step sections. A document is not compliant merely because each testcase section contains its own table.

The table is the canonical representation of individual test cases because it supports Manual QC review, execution tracking, filtering, traceability, comparison, and downstream export.

Supporting sections may explain shared context, but they **MUST NOT replace, duplicate, or fragment** the canonical testcase table.

---

## Template Structure

```text
# Test Cases

## Test Suite Summary

## Shared Preconditions / Environment

## Test Cases
    → one canonical testcase table containing all executable TC-* rows

## Shared Test Data / Dependencies

## Execution Notes

## Open Questions

## Coverage Summary
```

---

## Canonical Test Case Table

| Test Case ID | Module / Function | Scenario ID | Test Case Title | Preconditions / Setup | Test Steps | Test Data | Expected Result | Priority | Traceability |
|---|---|---|---|---|---|---|---|---|---|
| TC-001 | <module> | SC-001 | <single test objective> | <role/state/setup> | 1. <step><br>2. <step><br>3. <step> | <logical data or reference> | <observable expected result> | High / Medium / Low | <REQ/AC/BR/Risk IDs> |
| TC-002 | <module> | SC-002 | <single test objective> | <case-specific setup or shared setup reference> | 1. <step><br>2. <step><br>3. <step> | <logical data or reference> | <observable expected result> | High / Medium / Low | <REQ/AC/BR/Risk IDs> |

### Mandatory Representation Rules

1. `## Test Cases` **MUST contain one canonical Markdown table for the executable testcase inventory**.
2. Every executable `TC-*` **MUST appear as a row in that table**.
3. Do **not** create `### TC-*` or equivalent section-per-testcase representations in canonical output.
4. Do **not** create a separate steps table for each testcase.
5. Ordered steps **MUST be written inside the `Test Steps` cell** using numbered text separated by `<br>`.
6. The `Expected Result` cell **MUST contain the authoritative observable outcome for that testcase**. Where multiple step-level observations are necessary, keep them concise and aligned to the numbered steps using `<br>`.
7. Shared preconditions or data may be defined once in supporting sections and referenced from rows, but case-specific setup/data **MUST remain visible in the applicable row**.
8. Clarification-dependent items without an authoritative oracle **MUST NOT be promoted into executable `TC-*` rows**.
9. Additional summary or traceability tables may supplement the artifact, but **MUST NOT duplicate the testcase inventory in another representation**.

### Column Rules

| Column | Requirement |
|---|---|
| Test Case ID | Stable unique identifier, e.g. `TC-001`. |
| Module / Function | Functional area for grouping, filtering, and execution tracking. |
| Scenario ID | Upstream scenario identifier; multiple IDs only when the case legitimately covers a shared objective. |
| Test Case Title | Concise title with one primary verification objective. |
| Preconditions / Setup | Actor/role, required state, setup, dependencies, and required pre-existing data. |
| Test Steps | Ordered executable steps. Use `<br>` between numbered steps inside the Markdown table cell. |
| Test Data | Concrete supplied data or logical data requirement/reference. Do not fabricate business-valid values when unknown. |
| Expected Result | Observable and measurable expected behavior grounded in authoritative requirements/rules. |
| Priority | Execution/design priority preserved from scenario/risk context. |
| Traceability | Requirement, acceptance criterion, business rule, and risk references needed to justify the case. |

---

## Section Descriptions

| Section | Description |
|---|---|
| Test Suite Summary | Provide an overview of the feature, module, or business process covered by the test cases. |
| Shared Preconditions / Environment | Record setup that applies to many cases without repeating unnecessary text in every row. Case-specific setup still belongs in the table. |
| Test Cases | Maintain the **single canonical executable testcase inventory** in table form. |
| Shared Test Data / Dependencies | Describe reusable accounts, datasets, configurations, environments, systems, APIs, or services needed by multiple cases. |
| Execution Notes | Record important execution considerations or limitations. |
| Open Questions | Record unresolved behavior that prevents an authoritative expected result. |
| Coverage Summary | Summarize scenario/rule coverage and known gaps. |

---

## Writing Guidelines

When creating test cases:

- Verify one logical behavior per test case whenever practical.
- Keep each test case independent and repeatable.
- Define expected results that are clear, measurable, and source-grounded.
- Use realistic and maintainable test data when supplied or authorized.
- Avoid combining multiple unrelated objectives into one row.
- Ensure every test case traces back to an originating scenario and authoritative behavior.
- Keep unresolved expected behavior out of executable cases or mark the item clarification-dependent outside the authoritative table.
- Use `<br>` for multiple ordered steps in a table cell; do not create nested Markdown tables inside a testcase row.
- Do not use section-per-testcase formatting as an alternate canonical representation.

---

## Expected Output

A completed test case document should:

- Provide executable verification procedures.
- Cover all approved test scenarios that have sufficiently defined expected behavior.
- Clearly define observable outcomes.
- Support repeatable manual or automated execution.
- Make scenario-to-testcase and requirement/rule traceability easy to scan.
- Be straightforward to export into spreadsheet or test-management formats.
- Contain exactly one canonical testcase inventory representation rather than duplicating the same `TC-*` content across sections and tables.

---

## Validation

Before delivery, verify that:

- `## Test Cases` contains the canonical Markdown table;
- every executable `TC-*` appears exactly once in the canonical testcase inventory;
- no `### TC-*` or equivalent section-per-testcase representation exists;
- no testcase has a separate nested/per-item steps table;
- numbered steps use `<br>` inside the `Test Steps` cell;
- each expected result is observable and source-grounded;
- each executable testcase traces to at least one approved scenario;
- clarification-dependent behavior without an authoritative oracle is excluded from executable rows;
- shared sections do not hide required case-specific setup or data;
- supporting tables do not duplicate the canonical testcase inventory.

If any mandatory representation rule fails, the artifact is **not canonical-format compliant** and must be corrected before delivery.

---

## Best Practices

- Write concise and descriptive test case titles.
- Design test cases to be independent whenever possible.
- Separate positive, negative, boundary, state, permission, and exception objectives.
- Minimize redundant cases.
- Keep shared setup in shared sections when that improves readability, but never hide case-specific preconditions.
- Review coverage before execution.
- Update test cases whenever related requirements change.

---

## Related Templates

- `Requirement-Analysis.md`
- `Business-Rule.md`
- `Risk-Analysis.md`
- `Scenario.md`
- `Bug-Report.md`
- `Regression.md`
