# Structure-Based Testing

## Purpose

The **Structure-Based Testing** knowledge base covers testing techniques that evaluate software using information about internal implementation structure and execution behavior.

These techniques are commonly used to measure how thoroughly code structures, decisions, conditions, branches, and execution paths have been exercised.

---

## Scope

This knowledge base contains:

- Statement Coverage
- Branch Coverage
- Decision Coverage
- Condition Coverage
- Path Coverage
- Modified Condition Decision Coverage (MC/DC)

| Technique | Primary Focus |
|---|---|
| Statement Coverage | Measure whether executable statements have been exercised. |
| Branch Coverage | Measure whether control-flow branches have been exercised. |
| Decision Coverage | Measure whether decision outcomes have been exercised. |
| Condition Coverage | Measure whether individual Boolean conditions have evaluated to relevant outcomes. |
| Path Coverage | Evaluate execution paths through the implementation. |
| Modified Condition Decision Coverage (MC/DC) | Verify that each condition can independently affect a decision outcome. |

---

## Learning Objectives

After completing this category, readers should be able to:

- Explain the purpose of structure-based testing.
- Distinguish statement, branch, decision, condition, path, and MC/DC coverage.
- Understand the relationship between code structure and test coverage.
- Interpret coverage metrics without treating them as proof of software correctness.
- Select suitable coverage techniques according to risk and context.

---

## Knowledge Structure

```text
Structure-Based/
│
├── README.md
├── Statement-Coverage.md
├── Branch-Coverage.md
├── Decision-Coverage.md
├── Condition-Coverage.md
├── Path-Coverage.md
└── Modified-Condition-Decision-Coverage-(MC-DC).md
```

---

## Learning Roadmap

A recommended learning sequence is:

```text
Statement Coverage
        │
        ▼
Branch Coverage
        │
        ├── Decision Coverage
        ├── Condition Coverage
        ├── Path Coverage
        └── MC/DC
```

The sequence introduces basic execution coverage before more detailed decision and condition analysis.

---

## Relationship with White Box Testing

Structure-Based Testing primarily operates from the White Box Testing perspective.

```text
White Box Testing
        │
        ▼
Structure-Based Testing
        │
        ├── Statement Coverage
        ├── Branch Coverage
        ├── Decision Coverage
        ├── Condition Coverage
        ├── Path Coverage
        └── MC/DC
```

White Box Testing is the broader approach.

Structure-Based Testing provides specific techniques for evaluating implementation coverage.

---

## Coverage Interpretation

Coverage metrics indicate which implementation structures have been exercised.

They do not prove that:

- all requirements are correct;
- all expected behaviors are verified;
- all defects have been found;
- all important data combinations have been tested.

Structure-Based Testing should therefore complement specification-based and experience-based testing rather than replace them.

---

## Practical Applications

Structure-Based Testing is useful for:

- unit and component testing;
- code coverage analysis;
- safety-critical or high-reliability systems;
- evaluating complex conditional logic;
- identifying untested branches or paths;
- improving confidence in implementation-level verification.

---

## Best Practices

- Choose coverage targets according to risk and context.
- Interpret coverage as evidence of execution, not evidence of correctness.
- Combine structural coverage with requirement-based verification.
- Investigate uncovered code intentionally rather than maximizing metrics mechanically.
- Use higher-strength coverage such as MC/DC only when justified by system criticality or applicable standards.

---

## Related Knowledge

Prerequisites:

- White Box Testing

Related categories:

- Foundation Testing Techniques
- Specification-Based Testing
- Experience-Based Testing

Articles in this category:

- `Statement-Coverage.md`
- `Branch-Coverage.md`
- `Decision-Coverage.md`
- `Condition-Coverage.md`
- `Path-Coverage.md`
- `Modified-Condition-Decision-Coverage-(MC-DC).md`

---

## References

Related repository resources include:

- `shared/knowledge/testing-techniques/Catalog.md`
- `shared/knowledge/testing-techniques/Foundation/White-Box-Testing.md`
- `shared/standards/Knowledge-Article.md`
- `skills/`
- `workflows/`

---

## Summary

Structure-Based Testing evaluates the degree to which internal software structures have been exercised by tests.

The techniques in this category provide progressively stronger ways to reason about statements, branches, decisions, conditions, paths, and independent condition effects while remaining complementary to functional and experience-based testing.