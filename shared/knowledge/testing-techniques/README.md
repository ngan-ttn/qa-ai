# Testing Techniques

## Purpose

The `testing-techniques` knowledge module provides reusable knowledge about software testing approaches and test-design techniques used throughout the QA-AI framework.

Its purpose is to explain how testing techniques work, when they should be applied, how they relate to one another, and how they support effective test analysis, test design, coverage improvement, and defect detection.

This module acts as the entry point for the Testing Techniques knowledge domain.

---

## Scope

The module covers testing techniques organized by testing methodology rather than by testing phase, testing level, or software domain.

It includes:

- Foundation approaches.
- Specification-Based techniques.
- Structure-Based techniques.
- Experience-Based techniques.
- Combinatorial techniques.
- Model-Based techniques.
- Advanced techniques.

It does not define QA processes such as test planning, test management, regression strategy, or release management. Those belong to other QA knowledge areas.

---

## Module Structure

```text
shared/
└── knowledge/
    └── testing-techniques/
        ├── README.md
        ├── Catalog.md
        │
        ├── Foundation/
        │   ├── README.md
        │   ├── Black-Box-Testing.md
        │   ├── White-Box-Testing.md
        │   └── Gray-Box-Testing.md
        │
        ├── Specification-Based/
        │   ├── README.md
        │   ├── Equivalence-Partitioning.md
        │   ├── Boundary-Value-Analysis.md
        │   ├── Decision-Table-Testing.md
        │   ├── State-Transition-Testing.md
        │   ├── Cause-Effect-Graphing.md
        │   └── Use-Case-Testing.md
        │
        ├── Structure-Based/
        │   ├── README.md
        │   ├── Statement-Coverage.md
        │   ├── Branch-Coverage.md
        │   ├── Decision-Coverage.md
        │   ├── Condition-Coverage.md
        │   ├── Path-Coverage.md
        │   └── Modified-Condition-Decision-Coverage-(MC-DC).md
        │
        ├── Experience-Based/
        │   ├── README.md
        │   ├── Error-Guessing.md
        │   ├── Checklist-Based-Testing.md
        │   ├── Exploratory-Testing.md
        │   └── Session-Based-Testing.md
        │
        ├── Combinatorial/
        │   ├── README.md
        │   ├── Combinatorial-Testing.md
        │   ├── Pairwise-Testing.md
        │   └── Orthogonal-Array-Testing.md
        │
        ├── Model-Based/
        │   ├── README.md
        │   ├── Model-Based-Testing.md
        │   └── Finite-State-Machine-Testing.md
        │
        └── Advanced/
            ├── README.md
            ├── Mutation-Testing.md
            ├── Fuzz-Testing.md
            ├── Property-Based-Testing.md
            ├── AI-Assisted-Test-Design.md
            ├── Prompt-Based-Test-Generation.md
            └── Chaos-Testing.md
```

---

## Knowledge Architecture

```text
Testing Techniques
        │
        ├── Foundation
        ├── Specification-Based
        ├── Structure-Based
        ├── Experience-Based
        ├── Combinatorial
        ├── Model-Based
        └── Advanced
```

Each category has its own README that introduces the category scope, learning path, relationships, and article navigation.

`Catalog.md` is the authoritative catalog for article classification, prerequisites, priority, status, implementation phases, and dependency relationships.

---

## Knowledge Areas

### Foundation

Introduces the primary testing perspectives:

- Black Box Testing
- White Box Testing
- Gray Box Testing

### Specification-Based

Derives tests from requirements, business rules, specifications, and observable behavior.

### Structure-Based

Evaluates internal implementation structure and execution coverage.

### Experience-Based

Uses tester experience, historical defects, intuition, observation, and adaptive investigation.

### Combinatorial

Reduces large input-combination spaces while preserving meaningful interaction coverage.

### Model-Based

Derives tests from abstract behavioral, workflow, or state models.

### Advanced

Covers specialized and emerging techniques used in modern software quality engineering.

---

## Recommended Learning Path

A recommended progression is:

```text
Foundation
        │
        ▼
Specification-Based
        │
        ▼
Experience-Based
        │
        ▼
Structure-Based
        │
        ▼
Combinatorial
        │
        ▼
Model-Based
        │
        ▼
Advanced
```

This sequence is intended as a learning guide rather than a mandatory execution order.

Testing techniques should be selected according to the characteristics and risks of the system under test.

---

## Article Structure

Individual knowledge articles follow the standard defined in:

`shared/standards/Knowledge-Article.md`

Articles typically cover:

- Overview
- Purpose
- Core Concepts
- How It Works
- When to Use
- When Not to Use
- Advantages
- Limitations
- Examples
- Best Practices
- Related Knowledge
- References

Category README files provide navigation and context, while individual articles provide detailed technique guidance.

---

## Design Principles

Testing-technique knowledge should:

- Explain concepts before implementation details.
- Remain vendor-independent and tool-independent.
- Be reusable across software domains.
- Preserve clear boundaries between techniques.
- Avoid redefining QA processes that belong to other knowledge domains.
- Support QA reasoning without inventing project-specific business rules.
- Make prerequisites and relationships explicit.
- Remain traceable through the catalog and category indexes.

---

## Relationships with QA-AI

Testing-technique knowledge may support capabilities such as:

- Requirement Analysis
- Business Rule Analysis
- Risk Analysis
- Test Scenario Generation
- Test Case Generation
- Coverage Review
- Regression Analysis
- Test Data Design

Skills and workflows may reference this knowledge when a technique is relevant to their objective.

Knowledge articles provide reasoning guidance; they do not replace authoritative project requirements or workflow contracts.

---

## Navigation

Use the following entry points:

- `Catalog.md` — article catalog, prerequisites, priorities, status, implementation phases, and dependency map.
- `Foundation/README.md` — foundational testing approaches.
- `Specification-Based/README.md` — specification-driven test design.
- `Structure-Based/README.md` — implementation and coverage techniques.
- `Experience-Based/README.md` — experience-driven testing.
- `Combinatorial/README.md` — combination-reduction techniques.
- `Model-Based/README.md` — model-driven testing.
- `Advanced/README.md` — advanced and emerging techniques.

---

## References

Related repository resources include:

- `shared/knowledge/README.md`
- `shared/knowledge/qa/`
- `shared/glossary/QA-Terms.md`
- `shared/standards/Knowledge-Article.md`
- `shared/templates/`
- `shared/checklists/`
- `skills/`
- `workflows/`

---

## Summary

The Testing Techniques module provides a structured knowledge base for selecting and applying software testing techniques within QA-AI.

Its category architecture separates foundational approaches, specification-driven techniques, implementation coverage, experience-driven investigation, combination optimization, model-driven testing, and advanced techniques while keeping each article reusable and independently maintainable.