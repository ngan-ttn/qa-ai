# Regression Review Checklist

## Purpose

The `Regression` checklist defines the validation criteria for assessing the quality of regression impact analysis artifacts.

Its purpose is to ensure that regression scope is complete, risk-based, traceable, and suitable for efficient regression testing.

This checklist defines **what should be validated**. It does not define **how regression analysis is performed**.

---

## Scope

This checklist applies to structured regression impact analysis artifacts produced by QA engineers or AI capabilities.

Artifacts reviewed by this checklist include:

- Impact analysis
- Regression scope
- Impacted modules
- Impacted business flows
- Test priorities
- Risk assessment
- Regression recommendations

---

## How To Use

Apply this checklist after the regression analysis has been completed.

Review each validation category independently before determining the final review result.

- Verify all **MUST** criteria.
- Evaluate **SHOULD** criteria where applicable.
- Record review findings.
- Determine the final review result.

This checklist evaluates artifact quality only. It should not be used as a regression analysis guide or template.

---

## Validation Categories

### 1. Completeness

Review whether the regression analysis identifies all relevant impacts.

| Validation Criteria | Level |
|---------------------|:-----:|
| Changed functionality is identified. | MUST |
| Impacted modules are identified. | MUST |
| Impacted business flows are identified. | MUST |
| Dependencies are identified where applicable. | SHOULD |
| Out-of-scope items are explicitly documented where applicable. | SHOULD |

---

### 2. Impact Assessment

Review whether the identified impacts are accurate and sufficient.

| Validation Criteria | Level |
|---------------------|:-----:|
| Direct impacts are identified. | MUST |
| Indirect impacts are considered where applicable. | SHOULD |
| Shared components are evaluated where applicable. | SHOULD |
| Integration impacts are identified where applicable. | SHOULD |

---

### 3. Risk Assessment

Review whether regression priorities are aligned with business and technical risks.

| Validation Criteria | Level |
|---------------------|:-----:|
| Business-critical functionality is prioritized. | MUST |
| High-risk areas are identified. | MUST |
| Regression priority reflects impact severity. | MUST |
| Low-risk changes are appropriately categorized. | SHOULD |

---

### 4. Coverage

Review whether the regression scope provides sufficient verification coverage.

| Validation Criteria | Level |
|---------------------|:-----:|
| All impacted business flows are covered. | MUST |
| Critical integrations are included where applicable. | SHOULD |
| High-risk regression scenarios are included. | MUST |
| Historical defect areas are considered where applicable. | SHOULD |

---

### 5. Traceability

Review whether the regression analysis can be traced to upstream artifacts.

| Validation Criteria | Level |
|---------------------|:-----:|
| Regression items are traceable to requirements or change requests. | MUST |
| Impacted test scenarios are identified where applicable. | SHOULD |
| Impacted test cases are identified where applicable. | SHOULD |
| Impact rationale is documented. | MUST |

---

### 6. Maintainability

Review whether the regression analysis can be maintained efficiently.

| Validation Criteria | Level |
|---------------------|:-----:|
| Regression scope is clearly organized. | SHOULD |
| Duplicate regression items are avoided. | SHOULD |
| Regression recommendations remain understandable after future changes. | SHOULD |

---

### 7. Testability

Review whether the regression analysis supports effective regression execution.

| Validation Criteria | Level |
|---------------------|:-----:|
| Regression scope can be translated into executable test activities. | MUST |
| Regression priorities support execution planning. | MUST |
| Required environments or dependencies are identified where applicable. | SHOULD |
| Blocking assumptions are documented where applicable. | SHOULD |

---

## Acceptance Criteria

| Review Result | Criteria |
|---------------|----------|
| **PASS** | All **MUST** criteria are satisfied. No critical review findings remain unresolved. The regression analysis provides sufficient impact assessment and supports downstream regression testing. |
| **FAIL** | One or more **MUST** criteria are not satisfied, or critical review findings prevent reliable regression planning or execution. |

---

## Common Review Findings

| Category | Typical Findings |
|----------|------------------|
| Completeness | Missing impacted modules, business flows, or dependencies |
| Impact Assessment | Indirect impacts or integration impacts not considered |
| Risk Assessment | Incorrect regression priority or missing high-risk areas |
| Coverage | Missing impacted scenarios or historical defect areas |
| Traceability | Missing links to requirements, change requests, or test assets |
| Maintainability | Duplicate regression items or poorly organized scope |
| Testability | Regression scope cannot be translated into executable testing |

---

## Input Artifacts

- Requirement analysis
- Change requests
- Business rules
- Test scenarios
- Test cases

---

## Output Artifacts

- Reviewed regression analysis
- Regression scope
- Regression execution planning
- Regression test suite updates

---

## References

- `shared/standards/`
- `shared/templates/Regression.md`
- `shared/glossary/`