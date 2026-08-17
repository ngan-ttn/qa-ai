# Regression

## Purpose

This template provides a structured approach for documenting regression impact and planned revalidation after software changes.

Its purpose is to identify **what existing behavior needs to be retested, why it is in scope, and what can remain out of scope** without inventing implementation coupling.

---

## Canonical Output Format

Regression artifacts use a **hybrid format**. Change context, assumptions, entry/exit criteria, and execution notes remain section-based. The canonical regression-impact inventory is maintained as a table for scope review, prioritization, and traceability.

Regression recommendations MUST distinguish the three canonical execution-scope tiers defined below. These tiers are semantic decision levels, not fixed testcase percentages.

---

## Canonical Regression Scope Tiers

| Tier | Purpose | Selection Principle |
|---|---|---|
| `Minimum / Release-Gate Regression` | Smallest defensible set needed to detect release-critical regression in directly changed and highest-risk confirmed behavior. | Include direct change paths, critical state/eligibility/boundary behavior, and strongly supported dependencies whose failure could invalidate release confidence. Exclude depth-only/representative presentation coverage unless release-critical. |
| `Recommended Regression` | Practical risk-based regression set recommended for normal release confidence. | Includes the Minimum tier plus supported adjacent/dependent behavior, important alternate states/partitions, and material Medium/High-risk coverage justified by change relationship. |
| `Full Changed-Feature Verification` | Complete confirmed functional verification of the changed feature scope. | Includes all valid confirmed test coverage for the changed feature, including lower-risk/depth/display partitions that are not necessary in the smaller regression tiers. This is not automatically the default regression recommendation. |

Rules:

- Do not select a tier by targeting a predetermined percentage or testcase count.
- `Minimum` must remain meaningfully smaller than Full verification when evidence permits; if it cannot, explain why.
- `Recommended` must add justified value beyond Minimum; do not include cases merely because they exist.
- `Full Changed-Feature Verification` is a comparison/reference scope and may equal the full confirmed testcase suite for the changed feature.
- Clarification-dependent behavior without an authoritative oracle is not executable tier content; keep it `Clarify`/open.
- If no complete prior baseline exists, state the limitation and identify the evidence used to establish change relationship.

---

## Template Structure

```text
# Regression Analysis

## Regression Summary

## Change Overview

## Regression Impact / Coverage
    → canonical regression table

## Regression Scope Tiers
    → Minimum / Release-Gate Regression
    → Recommended Regression
    → Full Changed-Feature Verification

## Excluded Scope

## Entry Criteria

## Exit Criteria

## Assumptions / Open Questions

## Execution Notes
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
- Use the three canonical scope tiers consistently and explain material inclusions, especially in Minimum and Recommended scope.
- Do not call the full testcase suite "regression" merely because the feature changed; identify it explicitly as Full Changed-Feature Verification when appropriate.

---

## Expected Output

A completed regression artifact should:

- make impacted and excluded behavior easy to review;
- explain why each area is included, excluded, or clarification-dependent;
- preserve traceability to the actual change and existing QA coverage;
- provide Minimum, Recommended, and Full Changed-Feature scope views where existing test coverage is available;
- support risk-based regression execution without unnecessary unrelated retesting;
- be easy to filter or export for release/regression tracking.

---

## Validation

Before delivery, verify that:

- every included impact has supported change/dependency evidence;
- unsupported technical coupling was not invented;
- all selected testcase/scenario IDs actually exist in the supplied coverage artifacts;
- Minimum / Release-Gate scope follows release-critical/direct/high-risk selection logic rather than a target count;
- Recommended scope is a justified superset of Minimum when both are produced;
- Full Changed-Feature Verification is clearly distinguished from the recommended regression scope;
- clarification-dependent items are not converted into executable expectations;
- counts reported for each scope tier reconcile exactly with the unique listed testcase IDs;
- overlap/additional-count arithmetic between tiers is internally consistent.

A scope-count mismatch or inclusion of nonexistent coverage IDs is a validation failure and must be corrected before delivery.

---

## Related Templates

- `Requirement-Analysis.md`
- `Business-Rule.md`
- `Risk-Analysis.md`
- `Scenario.md`
- `TestCase.md`
- `Bug-Report.md`
