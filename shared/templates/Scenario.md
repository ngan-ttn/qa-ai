# Scenario

## Purpose

This template provides a structured approach for defining high-level test scenarios based on analyzed requirements and documented business rules.

Its purpose is to identify **what should be tested** without specifying detailed execution steps, serving as the foundation for comprehensive test case design.

---

## When to Use

Use this template when:

- Designing test coverage from approved requirements.
- Translating business rules into testable scenarios.
- Planning functional or system testing.
- Reviewing test completeness before creating detailed test cases.
- Identifying missing or uncovered business behaviors.

---

## Canonical Output Format

Scenario documents use a **hybrid format**:

- document-level context remains section-based;
- the core scenario inventory is a Markdown table;
- assumptions, out-of-scope items, open questions, and coverage summary remain sections/lists unless a table improves readability.

This format is designed for Manual QC review, traceability, comparison, and future spreadsheet/test-management export.

---

## Template Structure

```text
# Test Scenarios

## Scenario Summary

## Scope

## Assumptions

## Test Scenarios
    → canonical scenario table

## Out of Scope

## Open Questions

## Coverage Summary
```

---

## Canonical Test Scenario Table

| Scenario ID | Module / Feature | Scenario | Type | Preconditions / Conditions | Expected Behavior | Requirement / Rule Traceability | Risk Traceability | Priority |
|---|---|---|---|---|---|---|---|---|
| SC-001 | <module> | <what should be validated> | Positive / Negative / Boundary / State / Permission / Exception / Dependency | <scenario-level condition> | <observable behavior at scenario level> | <REQ/AC/BR IDs> | <risk ID or N/A> | High / Medium / Low |

### Column Rules

| Column | Requirement |
|---|---|
| Scenario ID | Stable unique identifier, e.g. `SC-001`. |
| Module / Feature | Functional area used for grouping and scanability. |
| Scenario | Concise scenario objective describing **what** is validated. |
| Type | Primary scenario category; use multiple values only when materially useful. |
| Preconditions / Conditions | Scenario-level state, actor, data condition, boundary, or dependency. Do not include detailed execution steps. |
| Expected Behavior | High-level observable behavior supported by authoritative input. Do not invent unresolved behavior. |
| Requirement / Rule Traceability | Upstream requirement, acceptance criterion, and/or business-rule identifiers. |
| Risk Traceability | Applicable risk identifiers when risk analysis exists; otherwise `N/A`. |
| Priority | QA execution/design priority derived from requirement/risk context. |

---

## Section Descriptions

| Section | Description |
|---|---|
| Scenario Summary | Provide an overview of the feature or business process being tested. |
| Scope | Define the functional areas and business behaviors covered by the scenarios. |
| Assumptions | Document assumptions that influence scenario design. |
| Test Scenarios | Maintain the canonical scenario inventory in table form. |
| Out of Scope | Identify features or behaviors intentionally excluded from testing. |
| Open Questions | Record unresolved behavior that must not be silently converted into expected results. |
| Coverage Summary | Summarize overall test coverage and identify remaining gaps. |

---

## Writing Guidelines

When creating test scenarios:

- Focus on business behavior rather than implementation details.
- Describe **what** should be validated, not **how** to execute the test.
- Keep each scenario independent whenever possible.
- Cover positive, negative, boundary, state, permission, exception, and dependency behavior where supported.
- Ensure every significant business rule is represented by scenario coverage.
- Avoid detailed test steps or concrete test data in the scenario table.
- Preserve uncertainty: clarification-dependent behavior belongs in Open Questions or is clearly marked, not invented.
- Use `<br>` inside a table cell only when multiple short conditions or references are required.

---

## Expected Output

A completed scenario document should:

- Provide comprehensive feature coverage.
- Reflect identified business rules and relevant risks.
- Make scenario-to-requirement traceability visible in one scanable table.
- Highlight major user and system behaviors.
- Support efficient test case creation and export.
- Make coverage gaps and unresolved behavior easy to identify.

---

## Best Practices

- Design scenarios from the user's perspective.
- Keep scenario titles concise and descriptive.
- Group related scenarios using `Module / Feature` rather than creating excessive subsections.
- Eliminate duplicate or overlapping scenarios.
- Keep one primary coverage objective per row.
- Review scenario coverage before proceeding to detailed test case design.

---

## Related Templates

- `Requirement-Analysis.md`
- `Business-Rule.md`
- `Risk-Analysis.md`
- `TestCase.md`
- `Regression.md`
