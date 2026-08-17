# Regression

## Purpose

This template provides a structured approach for documenting regression impact and planned revalidation after software changes.

Its purpose is to identify **what existing behavior needs to be retested, why it is in scope, and what can remain out of scope** without inventing implementation coupling.

---

## Canonical Output Format

Regression artifacts use a **hybrid format**. Change context, assumptions, entry/exit criteria, and execution notes remain section-based. The canonical regression-impact inventory is maintained as a table for scope review, prioritization, and traceability.

---

## Template Structure

```text
# Regression Analysis

## Regression Summary

## Change Overview

## Regression Impact / Coverage
    → canonical regression table

## Excluded Scope

## Entry Criteria

## Exit Criteria

## Assumptions / Open Questions

## Execution Notes

## Regression Summary
```

---

## Canonical Regression Table

| Impact ID | Area / Module | Change Relationship | Regression Scope / Behavior to Revalidate | Impact Type | Evidence / Traceability | Priority | Existing Coverage Reference | Decision |
|---|---|---|---|---|---|---|---|---|
| RI-001 | <area> | Direct / Indirect / Dependency / Potential | <existing behavior requiring revalidation> | Confirmed / Potential | <change/REQ/BR/SC/TC reference> | High / Medium / Low | <scenario/testcase IDs or N/A> | Include / Exclude / Clarify |

### Column Rules

| Column | Requirement |
|---|---|
| Impact ID | Stable unique identifier, e.g. `RI-001`. |
| Area / Module | Feature, workflow, integration, or business area under impact review. |
| Change Relationship | Why the area is related to the authoritative change delta. |
| Regression Scope / Behavior to Revalidate | Existing behavior that should be retested; describe behavior, not vague module names alone. |
| Impact Type | `Confirmed` only with supporting evidence; use `Potential` when coupling is plausible but not proven. |
| Evidence / Traceability | Change, requirement, rule, scenario, test case, dependency, or other authoritative reference. |
| Priority | Risk/business-based regression priority. |
| Existing Coverage Reference | Existing scenario/testcase IDs that can be reused where available. |
| Decision | `Include`, `Exclude`, or `Clarify`; exclusion must be supportable. |

---

## Writing Guidelines

- Base regression scope on an authoritative change delta plus known baseline behavior.
- Separate direct/confirmed impact from potential impact.
- Do not infer API, database, service, or module coupling without evidence.
- Keep one primary impacted behavior per row where practical.
- Prefer behavior-level scope over broad statements such as "regression entire module".
- Preserve existing coverage references so execution can reuse scenarios/test cases.
- Keep unresolved impact in `Clarify`/Potential rather than silently promoting it to confirmed scope.

---

## Expected Output

A completed regression artifact should:

- make impacted and excluded behavior easy to review;
- explain why each area is included, excluded, or clarification-dependent;
- preserve traceability to the actual change and existing QA coverage;
- support risk-based regression execution without unnecessary unrelated retesting;
- be easy to filter or export for release/regression tracking.

---

## Related Templates

- `Requirement-Analysis.md`
- `Business-Rule.md`
- `Risk-Analysis.md`
- `Scenario.md`
- `TestCase.md`
- `Bug-Report.md`
