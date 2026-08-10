# Requirement Analysis

## Purpose

This template provides a structured approach for analyzing software requirements before test design.

Its goal is to ensure that requirements are fully understood, testable, complete, and ready for downstream QA activities such as business rule extraction, scenario design, and test case creation.

---

## When to Use

Use this template when:

- Reviewing new functional requirements.
- Reviewing change requests.
- Preparing test design activities.
- Performing impact analysis.
- Identifying missing or ambiguous requirements.

---

## Template Structure

```text
# Requirement Analysis

## Requirement Summary

## Functional Requirements

## Non-Functional Requirements

## Assumptions

## Dependencies

## Business Constraints

## Validation Rules

## Edge Cases

## Open Questions

## Risks

## Impact Analysis

## Testability Assessment

## Analysis Summary
```

---

## Section Descriptions

| Section | Description |
|----------|-------------|
| Requirement Summary | Summarize the requirement and its business objective. |
| Functional Requirements | Identify the expected system behaviors and user interactions. |
| Non-Functional Requirements | Capture performance, security, usability, compatibility, or other quality attributes. |
| Assumptions | Record assumptions made during analysis. |
| Dependencies | Identify related systems, modules, APIs, or external services. |
| Business Constraints | Document limitations, policies, or operational constraints. |
| Validation Rules | Capture validation logic described or implied by the requirement. |
| Edge Cases | Identify exceptional, boundary, and alternative conditions. |
| Open Questions | List unclear or missing information requiring clarification. |
| Risks | Identify potential implementation or testing risks. |
| Impact Analysis | Determine affected features, components, users, or integrations. |
| Testability Assessment | Evaluate whether the requirement can be effectively verified through testing. |
| Analysis Summary | Summarize the overall findings and readiness for test design. |

---

## Writing Guidelines

During analysis:

- Focus on understanding the requirement rather than proposing solutions.
- Distinguish explicitly between stated facts and assumptions.
- Capture implicit behaviors whenever they can be reasonably inferred.
- Record unresolved issues instead of making unsupported assumptions.
- Keep findings objective and evidence-based.

---

## Expected Output

A completed requirement analysis should:

- Clearly explain the requirement.
- Identify all significant business behaviors.
- Highlight missing or ambiguous information.
- Capture testing considerations.
- Provide sufficient input for business rule extraction and test design.

---

## Best Practices

- Read the entire requirement before starting the analysis.
- Separate facts from interpretations.
- Document uncertainties explicitly.
- Consider both normal and exceptional flows.
- Think from both business and user perspectives.
- Review the analysis before proceeding to the next QA activity.

---

## Related Templates

- `Business-Rule.md`
- `Scenario.md`
- `TestCase.md`
- `Risk-Analysis.md`