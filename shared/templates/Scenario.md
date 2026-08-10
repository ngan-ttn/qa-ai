# Scenario

## Purpose

This template provides a structured approach for defining high-level test scenarios based on analyzed requirements and documented business rules.

Its purpose is to identify **what should be tested** without specifying detailed execution steps, serving as the foundation for comprehensive test case design.

---

## When to Use

Use this template when:

- Designing test coverage from approved requirements.
- Translating business rules into testable scenarios.
- Planning functional or system testing.
- Reviewing test completeness before creating detailed test cases.
- Identifying missing or uncovered business behaviors.

---

## Template Structure

```text
# Test Scenarios

## Scenario Summary

## Scope

## Assumptions

## Test Scenarios

## Out of Scope

## Coverage Summary
```

---

## Section Descriptions

| Section | Description |
|---------|-------------|
| Scenario Summary | Provide an overview of the feature or business process being tested. |
| Scope | Define the functional areas and business behaviors covered by the scenarios. |
| Assumptions | Document assumptions that influence scenario design. |
| Test Scenarios | List all high-level test scenarios required to validate the feature. |
| Out of Scope | Identify features or behaviors intentionally excluded from testing. |
| Coverage Summary | Summarize overall test coverage and identify any remaining gaps. |

---

## Writing Guidelines

When creating test scenarios:

- Focus on business behavior rather than implementation details.
- Describe **what** should be validated, not **how** to execute the test.
- Keep each scenario independent whenever possible.
- Cover positive, negative, boundary, and alternative flows.
- Ensure every significant business rule is represented by at least one scenario.
- Avoid including detailed test steps or test data.

---

## Expected Output

A completed scenario document should:

- Provide comprehensive feature coverage.
- Reflect all identified business rules.
- Highlight major user and system behaviors.
- Support efficient test case creation.
- Make coverage gaps easy to identify.

---

## Best Practices

- Design scenarios from the user's perspective.
- Keep scenario titles concise and descriptive.
- Group related scenarios logically.
- Eliminate duplicate or overlapping scenarios.
- Review scenario coverage before proceeding to detailed test case design.

---

## Related Templates

- `Requirement-Analysis.md`
- `Business-Rule.md`
- `TestCase.md`
- `Regression.md`