# Bug Report Checklist

## Purpose

The `Bug-Report` checklist defines the validation criteria for assessing the quality of bug report artifacts.

Its purpose is to ensure that bug reports are complete, accurate, reproducible, and actionable for developers, testers, and stakeholders.

This checklist defines **what should be validated**. It does not define **how bug reports are created**.

---

## Scope

This checklist applies to bug reports produced by QA engineers or AI capabilities.

Artifacts reviewed by this checklist include:

- Bug summary
- Environment information
- Preconditions
- Reproduction steps
- Expected result
- Actual result
- Supporting evidence
- Severity
- Priority
- Additional references

---

## How To Use

Apply this checklist after the bug report has been completed.

Review each validation category independently before determining the final review result.

- Verify all **MUST** criteria.
- Evaluate **SHOULD** criteria where applicable.
- Record review findings.
- Determine the final review result.

This checklist evaluates artifact quality only. It should not be used as a bug reporting guide or template.

---

## Validation Categories

### 1. Completeness

Review whether the bug report contains all required information.

| Validation Criteria | Level |
|---------------------|:-----:|
| A clear bug summary is provided. | MUST |
| Preconditions are documented where applicable. | SHOULD |
| Reproduction steps are complete. | MUST |
| Expected result is documented. | MUST |
| Actual result is documented. | MUST |
| Environment information is provided where applicable. | SHOULD |
| Severity is assigned. | MUST |
| Priority is assigned where applicable. | SHOULD |

---

### 2. Accuracy

Review whether the reported issue accurately represents the observed behavior.

| Validation Criteria | Level |
|---------------------|:-----:|
| Expected and actual results accurately reflect the observed issue. | MUST |
| The reported behavior is factual and objective. | MUST |
| Unsupported assumptions are not introduced. | MUST |

---

### 3. Reproducibility

Review whether another reviewer can reproduce the issue.

| Validation Criteria | Level |
|---------------------|:-----:|
| Reproduction steps are executable. | MUST |
| Reproduction steps are unambiguous. | MUST |
| Required test data is identified where applicable. | SHOULD |
| Required environment or configuration is documented where applicable. | SHOULD |

---

### 4. Evidence

Review whether sufficient evidence supports the reported issue.

| Validation Criteria | Level |
|---------------------|:-----:|
| Supporting evidence is attached where applicable. | SHOULD |
| Screenshots or recordings clearly demonstrate the issue where applicable. | SHOULD |
| Relevant logs, API responses, or database evidence are included where applicable. | SHOULD |

---

### 5. Traceability

Review whether the bug report can be traced to related QA artifacts.

| Validation Criteria | Level |
|---------------------|:-----:|
| The affected requirement is identified where applicable. | SHOULD |
| Related test case is referenced where applicable. | SHOULD |
| Related test scenario is referenced where applicable. | SHOULD |
| Related defects are referenced where applicable. | SHOULD |

---

### 6. Maintainability

Review whether the bug report remains understandable throughout its lifecycle.

| Validation Criteria | Level |
|---------------------|:-----:|
| The bug description is concise and well organized. | SHOULD |
| Duplicate information is avoided. | SHOULD |
| Terminology is used consistently. | MUST |

---

### 7. Actionability

Review whether the bug report provides sufficient information for investigation and resolution.

| Validation Criteria | Level |
|---------------------|:-----:|
| Developers can identify the reported issue without additional clarification. | MUST |
| Root cause investigation is supported by the provided information. | SHOULD |
| The report supports efficient verification after the fix. | SHOULD |

---

## Acceptance Criteria

| Review Result | Criteria |
|---------------|----------|
| **PASS** | All **MUST** criteria are satisfied. No critical review findings remain unresolved. The bug report is reproducible and actionable. |
| **FAIL** | One or more **MUST** criteria are not satisfied, or critical review findings prevent reliable investigation or verification. |

---

## Common Review Findings

| Category | Typical Findings |
|----------|------------------|
| Completeness | Missing expected result, actual result, or reproduction steps |
| Accuracy | Incorrect issue description or unsupported assumptions |
| Reproducibility | Missing test data or unclear reproduction steps |
| Evidence | Missing screenshots, logs, or API/DB evidence |
| Traceability | Missing references to related QA artifacts |
| Maintainability | Poor organization or inconsistent terminology |
| Actionability | Insufficient information for developers to investigate |

---

## Input Artifacts

- Executed test cases
- Test execution results
- Requirements
- Test scenarios

---

## Output Artifacts

- Reviewed bug report
- Defect tracking record
- Verification activities

---

## References

- `shared/standards/`
- `shared/templates/Bug-Report.md`
- `shared/glossary/`