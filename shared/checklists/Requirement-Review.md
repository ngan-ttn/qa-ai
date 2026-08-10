# Requirement Review Checklist

## Purpose

The `Requirement-Review` checklist defines the validation criteria for assessing the quality of structured requirement analysis artifacts.

Its purpose is to ensure that requirement analysis outputs are complete, accurate, consistent, and suitable for downstream QA activities.

This checklist defines **what should be validated**. It does not define **how requirement analysis is performed**.

---

## Scope

This checklist applies to structured requirement analysis artifacts produced by QA engineers or AI capabilities.

Artifacts reviewed by this checklist include:

- Requirement summary
- Business objective
- Functional scope
- Actors
- Inputs and outputs
- Dependencies
- Constraints
- Assumptions
- Open questions

---

## How To Use

Apply this checklist after the requirement analysis has been completed.

Review each validation category independently before determining the final review result.

- Verify all **MUST** criteria.
- Evaluate **SHOULD** criteria where applicable.
- Record review findings.
- Determine the final review result.

This checklist evaluates artifact quality only. It should not be used as a requirement analysis guide or template.

---

## Validation Categories

### 1. Completeness

Review whether all essential requirement information has been identified.

| Validation Criteria | Level |
|---------------------|:-----:|
| The business objective is identified. | MUST |
| The functional scope is defined. | MUST |
| All identified actors are documented. | MUST |
| Inputs and outputs are identified where applicable. | SHOULD |
| Dependencies are identified where applicable. | SHOULD |
| Constraints are documented where applicable. | SHOULD |
| Assumptions are explicitly documented. | MUST |
| Missing information is explicitly identified. | MUST |

---

### 2. Accuracy

Review whether the analysis accurately represents the source requirement.

| Validation Criteria | Level |
|---------------------|:-----:|
| The analysis does not contradict the source requirement. | MUST |
| Business intent is preserved. | MUST |
| Functional behavior is represented correctly. | MUST |
| Unsupported assumptions are not introduced. | MUST |

---

### 3. Consistency

Review whether the analysis is internally consistent.

| Validation Criteria | Level |
|---------------------|:-----:|
| Terminology is used consistently. | MUST |
| Similar concepts are represented consistently. | SHOULD |
| Conflicting statements do not exist. | MUST |
| Related information follows a consistent structure. | SHOULD |

---

### 4. Clarity

Review whether the analysis is easy to understand.

| Validation Criteria | Level |
|---------------------|:-----:|
| Statements are clear and unambiguous. | MUST |
| Information is logically organized. | SHOULD |
| Business and technical terminology is used appropriately. | SHOULD |
| Open questions are distinguishable from confirmed information. | MUST |

---

### 5. Traceability

Review whether downstream QA activities can trace information back to the requirement analysis.

| Validation Criteria | Level |
|---------------------|:-----:|
| Each identified feature is traceable to the source requirement. | MUST |
| Assumptions are distinguishable from confirmed requirements. | MUST |
| Missing information remains traceable. | MUST |
| The analysis supports downstream business rule extraction. | SHOULD |

---

### 6. Reusability

Review whether the analysis can be reused by downstream skills and workflows.

| Validation Criteria | Level |
|---------------------|:-----:|
| Information is structured for reuse. | MUST |
| Implementation-specific details are not included. | MUST |
| The analysis can be consumed without manual interpretation. | SHOULD |
| Information supports structured processing. | SHOULD |

---

### 7. Testability

Review whether the requirement analysis provides sufficient information for downstream testing activities.

| Validation Criteria | Level |
|---------------------|:-----:|
| Functional behavior can be translated into test scenarios. | MUST |
| Business rules can be identified for validation. | MUST |
| Missing information that blocks testing is explicitly documented. | MUST |
| Test assumptions are clearly distinguishable from confirmed requirements. | SHOULD |

---

## Acceptance Criteria

| Review Result | Criteria |
|---------------|----------|
| **PASS** | All **MUST** criteria are satisfied. No critical review findings remain unresolved. The requirement analysis is suitable for downstream QA activities. |
| **FAIL** | One or more **MUST** criteria are not satisfied, or critical review findings prevent reliable downstream QA activities. |

---

## Common Review Findings

| Category | Typical Findings |
|----------|------------------|
| Completeness | Missing business objectives, actors, assumptions, or dependencies |
| Accuracy | Incorrect interpretation of business intent or functional behavior |
| Consistency | Inconsistent terminology or conflicting statements |
| Clarity | Ambiguous wording or poorly organized information |
| Traceability | Missing links between analysis and source requirements |
| Reusability | Unstructured content or implementation-specific details |
| Testability | Insufficient information to derive test scenarios or business rules |

---

## Input Artifacts

- Requirement documents
- User stories
- Feature specifications
- Acceptance criteria

---

## Output Artifacts

- Reviewed requirement analysis
- Business rule extraction
- Test scenario generation
- Test case generation
- Coverage review
- Regression impact analysis

---

## References

- `shared/standards/`
- `shared/templates/Requirement-Analysis.md`
- `shared/glossary/`