# Foundation Testing Techniques

## Purpose

The **Foundation Testing Techniques** knowledge base introduces the primary testing approaches that establish the conceptual basis for the rest of the QA-AI testing-techniques library.

These articles explain how testing can be performed from external behavior, internal implementation, or a combination of both perspectives.

---

## Scope

This knowledge base contains:

- Black Box Testing
- White Box Testing
- Gray Box Testing

| Technique | Primary Focus |
|---|---|
| Black Box Testing | Validate observable system behavior without relying on internal implementation details. |
| White Box Testing | Validate internal logic, implementation structure, and code-level execution behavior. |
| Gray Box Testing | Combine external behavior validation with partial implementation knowledge. |

---

## Learning Objectives

After completing this category, readers should be able to:

- Distinguish Black Box, White Box, and Gray Box Testing.
- Understand what information each approach uses.
- Recognize the strengths and limitations of each approach.
- Select an appropriate testing perspective for a given context.
- Understand how these approaches support more specialized testing techniques.

---

## Knowledge Structure

```text
Foundation/
│
├── README.md
├── Black-Box-Testing.md
├── White-Box-Testing.md
└── Gray-Box-Testing.md
```

---

## Learning Roadmap

A recommended learning sequence is:

```text
Black Box Testing
        │
        ▼
White Box Testing
        │
        ▼
Gray Box Testing
```

Black Box Testing establishes the external-behavior perspective.

White Box Testing introduces implementation-aware validation.

Gray Box Testing combines both perspectives when partial internal knowledge is available.

---

## Relationship with Other Testing Techniques

Foundation techniques provide prerequisite concepts for later testing-technique categories.

```text
Foundation
    │
    ├── Specification-Based Techniques
    ├── Structure-Based Techniques
    ├── Experience-Based Techniques
    ├── Combinatorial Techniques
    ├── Model-Based Techniques
    └── Advanced Techniques
```

They define the testing perspective rather than a complete test-design process by themselves.

---

## Practical Applications

Foundation approaches are commonly used when:

- validating functional behavior from requirements;
- reviewing implementation logic and code coverage;
- combining API, database, UI, or architectural knowledge with functional testing;
- selecting downstream test-design techniques;
- determining the level of internal system knowledge available to the tester.

---

## Best Practices

- Select the testing approach according to the objective and available information.
- Do not assume Black Box Testing means testing without technical knowledge.
- Do not use White Box Testing only as a synonym for unit testing.
- Use Gray Box Testing deliberately when partial implementation knowledge improves coverage.
- Combine approaches when system risk requires multiple perspectives.

---

## Related Knowledge

Related categories:

- Specification-Based Testing
- Structure-Based Testing
- Experience-Based Testing
- Model-Based Testing

Articles in this category:

- `Black-Box-Testing.md`
- `White-Box-Testing.md`
- `Gray-Box-Testing.md`

---

## References

Related repository resources include:

- `shared/knowledge/testing-techniques/Catalog.md`
- `shared/knowledge/testing-techniques/README.md`
- `shared/standards/Knowledge-Article.md`
- `shared/glossary/QA-Terms.md`

---

## Summary

Foundation Testing Techniques establish the primary perspectives used to evaluate software.

Black Box Testing focuses on observable behavior, White Box Testing focuses on internal implementation, and Gray Box Testing combines both perspectives.

These concepts provide the foundation for selecting and understanding more specialized testing techniques throughout QA-AI.