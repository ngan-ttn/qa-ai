# Specification-Based Testing Techniques

## Purpose

This category contains test-design techniques that derive tests from requirements, rules, models, and observable behavior rather than source-code structure.

## Scope

```text
Specification-Based/
├── Equivalence-Partitioning.md
├── Boundary-Value-Analysis.md
├── Decision-Table-Testing.md
├── State-Transition-Testing.md
├── Cause-Effect-Graphing.md
└── Use-Case-Testing.md
```

## Selection Guidance

- Use **Equivalence Partitioning** for behaviorally equivalent value classes.
- Use **Boundary Value Analysis** around ordered transition points.
- Use **Decision Tables** for combinations of conditions and outcomes.
- Use **State Transition Testing** for lifecycle and history-dependent behavior.
- Use **Cause-Effect Graphing** to clarify complex logical relationships.
- Use **Use-Case Testing** for actor goals and end-to-end flows.

Techniques may be combined within one feature.

## Quality Boundary

The technique does not invent missing requirements. When expected behavior is unclear, the output should identify assumptions or clarification needs rather than manufacture a test oracle.

## References

- `../Catalog.md`
- `../Foundation/Black-Box-Testing.md`
- `../../../standards/Knowledge-Article.md`