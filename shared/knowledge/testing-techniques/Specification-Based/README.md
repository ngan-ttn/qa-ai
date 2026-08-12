# Specification-Based Testing

## Purpose

The **Specification-Based Testing** knowledge base covers test-design techniques that derive tests from requirements, business rules, functional specifications, use cases, and externally observable system behavior.

These techniques provide systematic ways to transform specification information into meaningful test conditions and test scenarios without depending on source-code structure.

---

## Scope

This knowledge base contains:

- Equivalence Partitioning
- Boundary Value Analysis
- Decision Table Testing
- State Transition Testing
- Cause-Effect Graphing
- Use Case Testing

| Technique | Primary Focus |
|---|---|
| Equivalence Partitioning | Divide input or output domains into representative classes. |
| Boundary Value Analysis | Verify behavior at and around important boundaries. |
| Decision Table Testing | Validate combinations of conditions and resulting actions. |
| State Transition Testing | Validate behavior across states, events, and transitions. |
| Cause-Effect Graphing | Model logical relationships between causes and effects. |
| Use Case Testing | Derive tests from user interactions and end-to-end flows. |

---

## Learning Objectives

After completing this category, readers should be able to:

- Select an appropriate specification-based technique for a requirement.
- Reduce redundant test cases using representative partitions.
- Identify important boundary conditions.
- Model complex business-rule combinations.
- Validate state-dependent behavior.
- Translate logical cause-effect relationships into test conditions.
- Derive tests from user and system interaction flows.

---

## Knowledge Structure

```text
Specification-Based/
│
├── README.md
├── Equivalence-Partitioning.md
├── Boundary-Value-Analysis.md
├── Decision-Table-Testing.md
├── State-Transition-Testing.md
├── Cause-Effect-Graphing.md
└── Use-Case-Testing.md
```

---

## Learning Roadmap

A recommended learning sequence is:

```text
Equivalence Partitioning
        │
        ▼
Boundary Value Analysis
        │
        ▼
Decision Table Testing
        │
        ▼
State Transition Testing
        │
        ├── Cause-Effect Graphing
        └── Use Case Testing
```

The roadmap is a learning guide rather than a mandatory execution sequence.

Different requirements may justify different techniques independently or in combination.

---

## Technique Selection

Use the requirement structure to guide technique selection.

```text
Input domains or value classes
        → Equivalence Partitioning

Numeric or ordered boundaries
        → Boundary Value Analysis

Condition/action combinations
        → Decision Table Testing

States and events
        → State Transition Testing

Complex logical dependencies
        → Cause-Effect Graphing

User journeys and interaction flows
        → Use Case Testing
```

---

## Relationship with Other Testing Techniques

Specification-Based Testing primarily uses the Black Box Testing perspective.

It complements:

- Experience-Based Testing for risk-driven and adaptive investigation.
- Structure-Based Testing for implementation coverage.
- Combinatorial Testing for efficient parameter-interaction coverage.
- Model-Based Testing for tests derived from formal or abstract behavioral models.

---

## Practical Applications

Specification-Based Testing is commonly applied to:

- form validation;
- business rules;
- calculations;
- workflow states;
- permissions and eligibility rules;
- user journeys;
- API request and response behavior;
- import and upload validation;
- transaction processing.

---

## Best Practices

- Start from authoritative requirements and business rules.
- Use the simplest technique that represents the behavior correctly.
- Combine techniques when a requirement contains multiple logical dimensions.
- Preserve traceability between requirement conditions and derived tests.
- Avoid generating duplicate tests when techniques overlap.
- Validate assumptions instead of inventing missing rules.

---

## Related Knowledge

Prerequisites:

- Black Box Testing

Related categories:

- Experience-Based Testing
- Structure-Based Testing
- Combinatorial Testing
- Model-Based Testing

Articles in this category:

- `Equivalence-Partitioning.md`
- `Boundary-Value-Analysis.md`
- `Decision-Table-Testing.md`
- `State-Transition-Testing.md`
- `Cause-Effect-Graphing.md`
- `Use-Case-Testing.md`

---

## References

Related repository resources include:

- `shared/knowledge/testing-techniques/Catalog.md`
- `shared/knowledge/testing-techniques/Foundation/`
- `shared/standards/Knowledge-Article.md`
- `shared/templates/`
- `skills/`
- `workflows/`

---

## Summary

Specification-Based Testing converts requirements and observable behavior into systematic test designs.

Its techniques help QA engineers identify representative inputs, boundaries, rule combinations, state behavior, logical dependencies, and end-to-end interactions while remaining independent of source-code structure.