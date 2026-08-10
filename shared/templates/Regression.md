# Regression

## Purpose

This template provides a structured approach for planning and documenting regression testing activities.

Its purpose is to identify the scope of revalidation after software changes, ensuring that existing functionality continues to operate as expected without unintended side effects.

---

## When to Use

Use this template when:

- Preparing regression testing after new feature implementation.
- Validating bug fixes.
- Assessing changes before a release.
- Planning regression testing for maintenance or hotfix deployments.
- Evaluating the impact of system modifications.

---

## Template Structure

```text
# Regression Plan

## Regression Summary

## Change Overview

## Regression Scope

## Excluded Scope

## Impact Assessment

## Regression Coverage

## Test Prioritization

## Entry Criteria

## Exit Criteria

## Risks

## Execution Notes

## Regression Summary
```

---

## Section Descriptions

| Section | Description |
|----------|-------------|
| Regression Summary | Provide an overview of the regression testing objective. |
| Change Overview | Summarize the software changes that trigger regression testing. |
| Regression Scope | Define the features, modules, or workflows that require revalidation. |
| Excluded Scope | Identify areas intentionally excluded from regression testing. |
| Impact Assessment | Describe the expected impact of the implemented changes. |
| Regression Coverage | Summarize the planned regression coverage across affected functionality. |
| Test Prioritization | Identify high, medium, and low priority regression areas based on risk and business impact. |
| Entry Criteria | Define the conditions required before regression testing can begin. |
| Exit Criteria | Define the conditions that determine regression completion. |
| Risks | Identify risks that may affect regression quality or completeness. |
| Execution Notes | Record additional considerations, limitations, or observations for regression testing. |
| Regression Summary | Summarize the overall regression strategy and readiness. |

---

## Writing Guidelines

When planning regression testing:

- Focus on affected business functionality rather than individual defects.
- Prioritize testing based on business impact and technical risk.
- Clearly distinguish included and excluded scope.
- Document assumptions and limitations explicitly.
- Maintain traceability to the related software changes.

---

## Expected Output

A completed regression plan should:

- Clearly explain why regression testing is required.
- Define the regression scope.
- Identify affected business areas.
- Prioritize regression activities.
- Support efficient and risk-based regression execution.

---

## Best Practices

- Base regression scope on change impact rather than system size.
- Prioritize critical business workflows.
- Include both direct and indirect impacts.
- Avoid unnecessary regression of unrelated functionality.
- Review and update the regression plan whenever the implementation scope changes.

---

## Related Templates

- `Requirement-Analysis.md`
- `Scenario.md`
- `TestCase.md`
- `Bug-Report.md`
- `Risk-Analysis.md`