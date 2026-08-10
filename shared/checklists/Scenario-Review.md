# Scenario Review Checklist

## Purpose

The `Scenario-Review` checklist defines the validation criteria for assessing the quality of structured test scenario artifacts.

Its purpose is to ensure that test scenarios provide complete, accurate, and reusable coverage of business requirements before detailed test cases are generated.

This checklist defines **what should be validated**. It does not define **how test scenarios are created**.

---

## Scope

This checklist applies to structured test scenario artifacts produced by QA engineers or AI capabilities.

Artifacts reviewed by this checklist include:

- Functional scenarios
- Business flow coverage
- Alternative flow coverage
- Exception flow coverage
- Edge case coverage
- Scenario priorities
- Traceability to requirements
- Traceability to business rules

---

## How To Use

Apply this checklist after the scenario set has been completed.

Review each validation category independently before determining the final review result.

- Verify all **MUST** criteria.
- Evaluate **SHOULD** criteria where applicable.
- Record review findings.
- Determine the final review result.

This checklist evaluates artifact quality only. It should not be used as a scenario generation guide or template.

---

## Validation Categories

### 1. Completeness

Review whether the scenario set sufficiently represents the analyzed requirements.

| Validation Criteria | Level |
|---------------------|:-----:|
| Every functional requirement is represented by one or more scenarios. | MUST |
| Primary business flows are covered. | MUST |
| Alternative flows are covered where applicable. | SHOULD |
| Exception flows are covered where applicable. | SHOULD |
| Preconditions are identified where applicable. | SHOULD |
| Postconditions are identified where applicable. | SHOULD |

---

### 2. Coverage

Review whether the scenario set provides sufficient testing coverage.

| Validation Criteria | Level |
|---------------------|:-----:|
| Business-critical functionality is covered. | MUST |
| Positive scenarios are included where applicable. | MUST |
| Negative scenarios are included where applicable. | SHOULD |
| Boundary conditions are represented where applicable. | SHOULD |
| Edge cases are identified where applicable. | SHOULD |
| High-risk functionality is covered. | MUST |

---

### 3. Accuracy

Review whether each scenario accurately represents the intended business behavior.

| Validation Criteria | Level |
|---------------------|:-----:|
| Scenarios do not contradict approved requirements. | MUST |
| Scenarios do not contradict business rules. | MUST |
| Expected business behavior is represented correctly. | MUST |
| Scenario objectives align with the intended business purpose. | MUST |

---

### 4. Consistency

Review whether the scenario set is internally consistent.

| Validation Criteria | Level |
|---------------------|:-----:|
| Terminology is used consistently. | MUST |
| Similar business behaviors follow a consistent scenario structure. | SHOULD |
| Duplicate scenarios do not exist. | MUST |
| Scenario priorities are applied consistently. | SHOULD |

---

### 5. Traceability

Review whether each scenario can be traced to upstream artifacts.

| Validation Criteria | Level |
|---------------------|:-----:|
| Each scenario is traceable to one or more requirements. | MUST |
| Supporting business rules are referenced where applicable. | SHOULD |
| Coverage gaps are explicitly identified. | MUST |
| Scenario relationships support downstream test case generation. | SHOULD |

---

### 6. Reusability

Review whether the scenario set can be reused across downstream QA activities.

| Validation Criteria | Level |
|---------------------|:-----:|
| Scenario descriptions remain implementation-independent. | MUST |
| Scenarios are suitable for detailed test case generation. | MUST |
| Scenario structure supports structured processing. | SHOULD |
| Scenarios are reusable across multiple testing activities. | SHOULD |

---

### 7. Testability

Review whether the scenario set can be translated into executable test cases.

| Validation Criteria | Level |
|---------------------|:-----:|
| Scenario objectives are testable. | MUST |
| Expected business outcomes are verifiable. | MUST |
| Scenario scope can be executed without additional interpretation. | SHOULD |
| Assumptions required for testing are documented where applicable. | SHOULD |

---

## Acceptance Criteria

| Review Result | Criteria |
|---------------|----------|
| **PASS** | All **MUST** criteria are satisfied. No critical review findings remain unresolved. The scenario set provides sufficient business coverage and is suitable for downstream test case generation. |
| **FAIL** | One or more **MUST** criteria are not satisfied, or critical review findings prevent reliable downstream QA activities. |

---

## Common Review Findings

| Category | Typical Findings |
|----------|------------------|
| Completeness | Missing primary, alternative, or exception flows |
| Coverage | Missing negative scenarios, boundary conditions, edge cases, or high-risk functionality |
| Accuracy | Scenario behavior does not align with requirements or business rules |
| Consistency | Duplicate scenarios or inconsistent prioritization |
| Traceability | Missing links between scenarios and upstream requirements |
| Reusability | Scenario descriptions contain implementation-specific details |
| Testability | Scenario objectives cannot be translated into executable test cases |

---

## Input Artifacts

- Requirement analysis
- Business rules
- Functional specifications

---

## Output Artifacts

- Reviewed scenario set
- Test case generation
- Coverage review
- Regression impact analysis

---

## References

- `shared/standards/`
- `shared/templates/Scenario.md`
- `shared/glossary/`