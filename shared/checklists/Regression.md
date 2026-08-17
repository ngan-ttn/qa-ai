# Regression Review Checklist

## Purpose

The `Regression` checklist defines the validation criteria for assessing the quality of regression impact analysis artifacts.

Its purpose is to ensure that regression scope is complete, risk-based, traceable, internally consistent, and suitable for efficient regression testing.

This checklist defines **what should be validated**. It does not define **how regression analysis is performed**.

---

## Scope

This checklist applies to structured regression impact analysis artifacts produced by QA engineers or AI capabilities.

---

## How To Use

Apply this checklist after the regression analysis has been completed.

- Verify all **MUST** criteria.
- Evaluate **SHOULD** criteria where applicable.
- Record review findings.
- Determine the final review result.

---

## Validation Categories

### 1. Completeness

| Validation Criteria | Level |
|---|:---:|
| Changed functionality/change delta is identified. | MUST |
| Directly impacted behavior is identified. | MUST |
| Potential/indirect dependencies are considered where supported. | SHOULD |
| Out-of-scope or excluded behavior is explicit where applicable. | SHOULD |
| Unresolved dependencies are explicit. | MUST |

### 2. Impact Assessment

| Validation Criteria | Level |
|---|:---:|
| Direct impact is distinguished from indirect/potential impact. | MUST |
| Unsupported technical coupling is not invented. | MUST |
| Each material inclusion/exclusion has evidence/rationale. | MUST |
| Existing coverage is reused where valid rather than duplicated. | SHOULD |

### 3. Risk Assessment

| Validation Criteria | Level |
|---|:---:|
| Business-critical/high-risk confirmed behavior influences scope. | MUST |
| Regression priority reflects supported impact/risk. | MUST |
| Lower-risk/depth coverage is not promoted to Minimum without rationale. | SHOULD |

### 4. Canonical Scope Tiers

| Validation Criteria | Level |
|---|:---:|
| `Minimum / Release-Gate Regression` is identified when executable existing coverage is available. | MUST |
| Minimum represents the smallest defensible release-critical direct/high-risk/critical-state scope; it is not selected to hit a target percentage/count. | MUST |
| `Recommended Regression` is identified and contains justified additional coverage beyond Minimum. | MUST |
| Recommended is a superset of Minimum when both are produced. | MUST |
| `Full Changed-Feature Verification` is explicitly distinguished from default regression recommendations. | MUST |
| If Minimum approaches Full verification, the artifact explains why the change/risk evidence requires that breadth. | SHOULD |
| Clarification-dependent behavior without an oracle is not included as executable tier content. | MUST |

### 5. Traceability

| Validation Criteria | Level |
|---|:---:|
| Regression items trace to requirements/change/dependency evidence. | MUST |
| Impacted scenario/testcase references are valid where supplied. | MUST |
| No selected coverage ID is fabricated or absent from supplied artifacts. | MUST |

### 6. Count / Scope Integrity

| Validation Criteria | Level |
|---|:---:|
| Minimum count equals the number of unique listed selected IDs. | MUST |
| Recommended count equals the number of unique listed selected IDs. | MUST |
| Full Changed-Feature count reconciles with the stated confirmed feature coverage baseline. | MUST |
| Additional/overlap counts between tiers are arithmetically consistent. | MUST |
| Percentages use reconciled numerator/denominator values. | MUST |

### 7. Maintainability / Testability

| Validation Criteria | Level |
|---|:---:|
| Regression scope is clearly organized and behavior-oriented. | SHOULD |
| Duplicate regression items are avoided. | SHOULD |
| Scope can be translated into executable test activity. | MUST |
| Blocking assumptions/dependencies are documented. | SHOULD |

---

## Acceptance Criteria

| Review Result | Criteria |
|---|---|
| **PASS** | All **MUST** criteria are satisfied. Scope tiers, traceability, and counts are evidence-based and internally consistent. |
| **FAIL** | One or more **MUST** criteria are not satisfied, including fabricated dependencies/coverage IDs, invalid tier semantics, or count mismatches. |

---

## Common Review Findings

| Category | Typical Findings |
|---|---|
| Impact | Adjacent area included without supported dependency |
| Tiering | Minimum selected by percentage; Recommended nearly/full suite without rationale; Full verification mislabeled as regression |
| Traceability | Selected TC/SC IDs do not exist or do not support the stated impact |
| Uncertainty | Clarification-dependent behavior converted into executable regression expectation |
| Count Integrity | Tier counts, additional counts, overlaps, or percentages do not reconcile |

---

## References

- `shared/standards/Output.md`
- `shared/templates/Regression.md`
- `skills/regression-impact/README.md`
- `workflows/regression-analysis/README.md`
