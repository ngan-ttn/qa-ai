# Business Rule

## Purpose

This template provides a structured approach for identifying, documenting, and organizing business rules extracted from software requirements.

Its purpose is to separate business logic from implementation details, ensuring that business behaviors are explicit, testable, and reusable throughout the QA process.

---

## When to Use

Use this template when:

- Analyzing functional requirements.
- Reviewing business specifications.
- Preparing test scenarios.
- Identifying validation logic.
- Clarifying implicit business behaviors.

---

## Template Structure

```text
# Business Rules

## Rule Summary

## Business Rules

## Validation Rules

## Decision Rules

## Exception Rules

## Preconditions

## Postconditions

## Business Constraints

## Rule Dependencies

## Open Questions

## Rule Summary
```

---

## Section Descriptions

| Section | Description |
|----------|-------------|
| Rule Summary | Provide a brief overview of the business logic covered by the requirement. |
| Business Rules | Define the core business rules governing the feature or process. |
| Validation Rules | Describe validation conditions for user input, system behavior, or data integrity. |
| Decision Rules | Define conditional logic that determines system behavior. |
| Exception Rules | Describe how exceptional or invalid conditions should be handled. |
| Preconditions | Identify conditions that must be satisfied before a rule can be applied. |
| Postconditions | Describe the expected system state after a rule is successfully executed. |
| Business Constraints | Document limitations imposed by business policies or regulations. |
| Rule Dependencies | Identify relationships with other rules, modules, or external systems. |
| Open Questions | Record unclear or unresolved business logic requiring clarification. |
| Rule Summary | Summarize the extracted business logic and overall completeness. |

---

## Writing Guidelines

When documenting business rules:

- Focus on business behavior rather than implementation details.
- Keep each rule independent whenever possible.
- Write one rule per statement.
- Use clear and measurable language.
- Separate mandatory rules from optional behaviors.
- Record assumptions explicitly instead of embedding them into rules.

---

## Expected Output

A completed business rule document should:

- Clearly define all business logic.
- Separate business rules from technical implementation.
- Capture explicit and implicit behaviors.
- Support downstream scenario and test case design.
- Reduce ambiguity during development and testing.

---

## Best Practices

- Assign one logical idea to each business rule.
- Keep wording concise and unambiguous.
- Avoid mixing multiple conditions in a single rule.
- Identify missing business rules early.
- Validate rule completeness before creating test scenarios.

---

## Related Templates

- `Requirement-Analysis.md`
- `Scenario.md`
- `TestCase.md`
- `Risk-Analysis.md`