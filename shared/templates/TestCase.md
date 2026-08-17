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

Test case documents use a **hybrid format**:

- suite-level context remains section-based;
- the executable test case inventory is a Markdown table;
- shared data/dependency notes, execution notes, open questions, and coverage summary remain sections when appropriate.

The table is the canonical representation of individual test cases because it supports Manual QC review, execution tracking, filtering, traceability, and downstream export.

---

## Template Structure

```text
# Test Cases

## Test Suite Summary

## Shared Preconditions / Environment

## Test Cases
    → canonical testcase table

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
| Test Cases | Maintain the canonical executable testcase inventory in table form. |
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

---

## Expected Output

A completed test case document should:

- Provide executable verification procedures.
- Cover all approved test scenarios that have sufficiently defined expected behavior.
- Clearly define observable outcomes.
- Support repeatable manual or automated execution.
- Make scenario-to-testcase and requirement/rule traceability easy to scan.
- Be straightforward to export into spreadsheet or test-management formats.

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
