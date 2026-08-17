# Test Case Review Checklist

## Purpose

The `TestCase-Review` checklist defines the validation criteria for assessing the quality of structured test case artifacts.

Its purpose is to ensure that test cases are complete, correct, executable, maintainable, traceable, and compliant with the canonical testcase representation.

This checklist defines **what should be validated**. It does not define **how test cases are created**.

---

## Scope

This checklist applies to structured test case artifacts produced by QA engineers or AI capabilities.

Artifacts reviewed by this checklist include:

- Canonical testcase inventory format
- Test case metadata
- Test objective
- Preconditions
- Test steps
- Test data
- Expected results
- Priority
- Traceability
- Test coverage

---

## How To Use

Apply this checklist after the test case artifact has been completed.

- Verify all **MUST** criteria.
- Evaluate **SHOULD** criteria where applicable.
- Record review findings.
- Determine the final review result.

---

## Validation Categories

### 1. Canonical Format Compliance

| Validation Criteria | Level |
|---|:---:|
| `## Test Cases` contains one canonical Markdown testcase inventory table. | MUST |
| Every executable `TC-*` appears exactly once as a row in the canonical inventory. | MUST |
| Section-per-testcase rendering such as `### TC-*` is not used as the canonical representation. | MUST |
| Separate per-testcase/nested steps tables are not used. | MUST |
| Ordered steps are represented in the `Test Steps` cell using numbered `<br>` content. | MUST |
| Supporting sections do not duplicate or fragment the canonical testcase inventory. | MUST |

### 2. Completeness

| Validation Criteria | Level |
|---|:---:|
| The test objective is clearly defined. | MUST |
| Preconditions are documented where required. | MUST |
| Test steps are complete. | MUST |
| Expected results are provided for every verification point. | MUST |
| Required test data is identified where applicable. | SHOULD |
| Test priority is assigned where applicable. | SHOULD |
| A unique test case identifier exists. | MUST |

### 3. Correctness

| Validation Criteria | Level |
|---|:---:|
| The test case aligns with approved authoritative behavior. | MUST |
| The verification objective matches the intended business behavior. | MUST |
| Expected results represent source-supported system behavior. | MUST |
| Unsupported assumptions are not introduced. | MUST |
| Clarification-dependent behavior without an authoritative oracle is excluded from executable rows. | MUST |

### 4. Executability

| Validation Criteria | Level |
|---|:---:|
| Test steps are sequential and executable. | MUST |
| Each step describes a clear executable action or verification. | MUST |
| Test steps avoid ambiguous wording. | SHOULD |
| Expected results are objectively verifiable. | MUST |
| Required environment or setup is identified where applicable. | SHOULD |

### 5. Coverage

| Validation Criteria | Level |
|---|:---:|
| Business-critical functionality is covered. | MUST |
| Positive validation is included where applicable. | MUST |
| Negative validation is included where applicable. | SHOULD |
| Boundary conditions are verified where applicable. | SHOULD |
| Error handling is verified where applicable. | SHOULD |
| Supplied Coverage Review findings are handled according to `Covered / Weakly Covered / Gap / Blocked` semantics. | SHOULD |

### 6. Traceability

| Validation Criteria | Level |
|---|:---:|
| Every executable testcase traces to at least one approved scenario. | MUST |
| Requirements/business rules/risks are referenced where the canonical workflow supplies them. | SHOULD |
| The verification objective remains traceable throughout the QA workflow. | MUST |

### 7. Maintainability

| Validation Criteria | Level |
|---|:---:|
| Test steps avoid unnecessary implementation details. | SHOULD |
| Test data is reusable where applicable. | SHOULD |
| Duplicate validation logic is avoided. | SHOULD |
| Shared setup is factored out without hiding case-specific setup. | SHOULD |
| The test case remains understandable after requirement updates. | SHOULD |

### 8. Count / Inventory Integrity

| Validation Criteria | Level |
|---|:---:|
| Reported testcase totals equal the number of unique `TC-*` rows. | MUST |
| Functional-area subtotals reconcile with the stated total when categories are exhaustive. | MUST |
| Scenario coverage counts reconcile with actual unique scenario IDs represented by executable rows. | MUST |
| ID ranges are not reported as continuous unless the IDs actually exist. | MUST |

---

## Acceptance Criteria

| Review Result | Criteria |
|---|---|
| **PASS** | All **MUST** criteria are satisfied. No critical review findings remain unresolved. The artifact is canonical-format compliant, executable, source-grounded, traceable, and internally consistent. |
| **FAIL** | One or more **MUST** criteria are not satisfied, including canonical representation or count-integrity failures. |

---

## Common Review Findings

| Category | Typical Findings |
|---|---|
| Canonical Format | Section-per-testcase output; separate per-case steps tables; duplicated testcase inventory |
| Completeness | Missing preconditions, test data, or expected results |
| Correctness | Expected results do not align with authoritative behavior |
| Executability | Ambiguous steps or missing execution details |
| Coverage | Missing confirmed negative/boundary/state coverage; blocked behavior converted to executable oracle |
| Traceability | Missing scenario or upstream references |
| Maintainability | Duplicate steps or unnecessary implementation-dependent wording |
| Count Integrity | Summary count/subtotals do not reconcile with actual TC/SC IDs |

---

## References

- `shared/standards/Output.md`
- `shared/templates/TestCase.md`
- `skills/testcase-generator/README.md`
- `skills/coverage-reviewer/README.md`
