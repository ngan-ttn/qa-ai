# Bug Report

## Purpose

This template provides a standardized structure for documenting software defects.

Its purpose is to communicate issues clearly, consistently, and objectively, enabling efficient reproduction, investigation, prioritization, and resolution.

---

## When to Use

Use this template when:

- Reporting a newly discovered defect.
- Verifying unexpected system behavior.
- Recording regression issues.
- Documenting production defects.
- Tracking issues identified during testing or review.

---

## Template Structure

```text
# Bug Report

## Defect Summary

## Environment

## Preconditions

## Steps to Reproduce

## Actual Result

## Expected Result

## Supporting Evidence

## Impact Assessment

## Notes

## Related Artifacts
```

---

## Section Descriptions

| Section | Description |
|----------|-------------|
| Defect Summary | Provide a concise description of the observed issue. |
| Environment | Specify the environment where the issue occurred (application version, platform, browser, device, etc.). |
| Preconditions | Describe any required setup before reproducing the issue. |
| Steps to Reproduce | List the minimum steps required to consistently reproduce the defect. |
| Actual Result | Describe the observed system behavior. |
| Expected Result | Describe the expected system behavior based on requirements or business rules. |
| Supporting Evidence | Include screenshots, videos, logs, API responses, or other supporting materials. |
| Impact Assessment | Describe the business, functional, or user impact of the defect. |
| Notes | Record additional observations or investigation details. |
| Related Artifacts | Reference related requirements, business rules, scenarios, test cases, or existing defects. |

---

## Writing Guidelines

When documenting defects:

- Describe observable behavior rather than assumptions.
- Keep reproduction steps clear, concise, and repeatable.
- Separate facts from investigation notes.
- Use objective and professional language.
- Include only information relevant to understanding and reproducing the issue.
- Reference related artifacts whenever possible.

---

## Expected Output

A completed bug report should:

- Clearly describe the observed issue.
- Enable others to reproduce the defect consistently.
- Explain the expected system behavior.
- Provide sufficient evidence for investigation.
- Support efficient defect triage and resolution.

---

## Best Practices

- Report one defect per bug report.
- Use descriptive and searchable titles.
- Reproduce the issue before submitting whenever possible.
- Attach evidence that supports the reported behavior.
- Update the report when new findings become available.
- Avoid including implementation assumptions unless they are verified.

---

## Related Templates

- `Requirement-Analysis.md`
- `Business-Rule.md`
- `Scenario.md`
- `TestCase.md`
- `Regression.md`