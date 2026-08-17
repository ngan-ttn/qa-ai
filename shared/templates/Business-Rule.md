# Business Rule

## Purpose

This template provides a structured approach for identifying, documenting, and organizing business rules extracted from software requirements.

Its purpose is to separate business logic from implementation details, ensuring that business behaviors are explicit, testable, traceable, and reusable throughout the QA process.

---

## Canonical Output Format

Business-rule documents use a **hybrid format**. Narrative context and unresolved questions remain section-based, while the canonical rule inventory is maintained as a table for easier review and downstream traceability.

---

## Template Structure

```text
# Business Rules

## Rule Summary

## Business Rules
    → canonical rule table

## Rule Dependencies

## Assumptions

## Open Questions

## Rule Coverage Summary
```

---

## Canonical Business Rule Table

| Rule ID | Rule Type | Business Rule | Conditions / Inputs | Expected Outcome / Constraint | Source Traceability | Dependencies | Status |
|---|---|---|---|---|---|---|---|
| BR-001 | Core / Validation / Decision / Exception / Precondition / Postcondition / Constraint | <single business rule> | <when/if/applicable conditions> | <required behavior or constraint> | <REQ/AC/source reference> | <related BR/module or N/A> | Confirmed / Clarification-Dependent |

### Column Rules

| Column | Requirement |
|---|---|
| Rule ID | Stable unique identifier, e.g. `BR-001`. |
| Rule Type | Primary rule classification used for grouping/filtering. |
| Business Rule | One logical rule per row, written in business terms. |
| Conditions / Inputs | Preconditions, decision inputs, validation context, or triggering state. |
| Expected Outcome / Constraint | Required business behavior, permitted/forbidden outcome, or invariant. |
| Source Traceability | Authoritative requirement, acceptance criterion, specification, or source location. |
| Dependencies | Other rules, modules, roles, or externally defined dependencies when explicitly supported. |
| Status | `Confirmed` only when grounded; otherwise `Clarification-Dependent`. |

---

## Writing Guidelines

- Focus on business behavior rather than technical implementation.
- Keep one logical rule per row.
- Preserve thresholds, durations, roles, states, defaults, and precedence exactly as supported by the source.
- Do not convert generic QA knowledge into project-specific policy.
- Separate unresolved behavior from confirmed rules.
- Use rule types for organization instead of splitting the document into many repetitive rule sections.
- Keep source traceability explicit enough for downstream scenario/testcase generation.

---

## Expected Output

A completed business-rule document should:

- make the complete rule inventory easy to scan and compare;
- separate confirmed and clarification-dependent behavior;
- maintain source authority and traceability;
- support scenario, risk, testcase, coverage, and regression artifacts without reinterpreting the original requirement;
- be straightforward to export or filter in tabular tools.

---

## Related Templates

- `Requirement-Analysis.md`
- `Risk-Analysis.md`
- `Scenario.md`
- `TestCase.md`
- `Regression.md`
