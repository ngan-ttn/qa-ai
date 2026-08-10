# Test Case Review Checklist

## Purpose

The `TestCase-Review` checklist defines the validation criteria for assessing the quality of structured test case artifacts.

Its purpose is to ensure that test cases are complete, correct, executable, maintainable, and suitable for efficient manual or automated testing.

This checklist defines **what should be validated**. It does not define **how test cases are created**.

---

## Scope

This checklist applies to structured test case artifacts produced by QA engineers or AI capabilities.

Artifacts reviewed by this checklist include:

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

Apply this checklist after the test case has been completed.

Review each validation category independently before determining the final review result.

- Verify all **MUST** criteria.
- Evaluate **SHOULD** criteria where applicable.
- Record review findings.
- Determine the final review result.

This checklist evaluates artifact quality only. It should not be used as a test case generation guide or template.

---

## Validation Categories

### 1. Completeness

Review whether the test case contains all required information.

| Validation Criteria | Level |
|---------------------|:-----:|
| The test objective is clearly defined. | MUST |
| Preconditions are documented where required. | MUST |
| Test steps are complete. | MUST |
| Expected results are provided for every verification point. | MUST |
| Required test data is identified where applicable. | SHOULD |
| Test priority is assigned where applicable. | SHOULD |
| A unique test case identifier exists where applicable. | SHOULD |

---

### 2. Correctness

Review whether the test case accurately verifies the intended business behavior.

| Validation Criteria | Level |
|---------------------|:-----:|
| The test case aligns with the approved requirement. | MUST |
| The verification objective matches the intended business behavior. | MUST |
| Expected results represent the correct system behavior. | MUST |
| Unsupported assumptions are not introduced. | MUST |

---

### 3. Executability

Review whether the test case can be executed without additional interpretation.

| Validation Criteria | Level |
|---------------------|:-----:|
| Test steps are sequential and executable. | MUST |
| Each step describes a single executable action or verification. | MUST |
| Test steps avoid ambiguous wording. | SHOULD |
| Expected results are objectively verifiable. | MUST |
| Required environment or setup is identified where applicable. | SHOULD |

---

### 4. Coverage

Review whether the test case contributes sufficient verification coverage.

| Validation Criteria | Level |
|---------------------|:-----:|
| Business-critical functionality is covered. | MUST |
| Positive validation is included where applicable. | MUST |
| Negative validation is included where applicable. | SHOULD |
| Boundary conditions are verified where applicable. | SHOULD |
| Error handling is verified where applicable. | SHOULD |

---

### 5. Traceability

Review whether the test case can be traced to upstream artifacts.

| Validation Criteria | Level |
|---------------------|:-----:|
| The test case is traceable to one or more requirements. | MUST |
| Supporting business rules are referenced where applicable. | SHOULD |
| One or more test scenarios are referenced where applicable. | SHOULD |
| The verification objective remains traceable throughout the QA workflow. | MUST |

---

### 6. Maintainability

Review whether the test case can be maintained efficiently over time.

| Validation Criteria | Level |
|---------------------|:-----:|
| Test steps avoid unnecessary implementation details. | SHOULD |
| Test data is reusable where applicable. | SHOULD |
| Duplicate validation logic is avoided. | SHOULD |
| The test case remains understandable after requirement updates. | SHOULD |

---

### 7. Testability

Review whether the test case supports reliable execution and objective evaluation.

| Validation Criteria | Level |
|---------------------|:-----:|
| The expected outcome is measurable. | MUST |
| Pass or fail can be determined objectively. | MUST |
| Manual execution is possible without additional interpretation. | SHOULD |
| The test case supports automation where applicable. | SHOULD |

---

## Acceptance Criteria

| Review Result | Criteria |
|---------------|----------|
| **PASS** | All **MUST** criteria are satisfied. No critical review findings remain unresolved. The test case is executable and suitable for downstream testing activities. |
| **FAIL** | One or more **MUST** criteria are not satisfied, or critical review findings prevent reliable execution or downstream testing activities. |

---

## Common Review Findings

| Category | Typical Findings |
|----------|------------------|
| Completeness | Missing preconditions, test data, or expected results |
| Correctness | Expected results do not align with business requirements |
| Executability | Ambiguous steps or missing execution details |
| Coverage | Missing negative, boundary, or error validation |
| Traceability | Missing links to requirements or test scenarios |
| Maintainability | Duplicate steps or implementation-dependent wording |
| Testability | Expected results are subjective or cannot determine pass/fail objectively |

---

## Input Artifacts

- Requirement analysis
- Business rules
- Test scenarios

---

## Output Artifacts

- Reviewed test cases
- Manual test execution
- Automated test implementation
- Coverage assessment
- Regression testing

---

## References

- `shared/standards/`
- `shared/templates/TestCase.md`
- `shared/glossary/`