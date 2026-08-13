# Testing Techniques Catalog

## Purpose

This catalog is the authoritative inventory and architecture for `shared/knowledge/testing-techniques/`. It defines the approved baseline of reusable test-design knowledge while keeping QA process, technology-specific behavior, and project-specific rules in their owning knowledge domains.

## Knowledge Architecture

```text
Testing Techniques
├── Foundation
├── Specification-Based
├── Structure-Based
├── Experience-Based
├── Combinatorial
├── Model-Based
└── Advanced
```

## Article Catalog

| Article | File | Category | Level | Prerequisites | Priority | Status |
|---|---|---|---|---|---|---|
| Black Box Testing | `Foundation/Black-Box-Testing.md` | Foundation | Foundation | None | High | Approved |
| White Box Testing | `Foundation/White-Box-Testing.md` | Foundation | Foundation | None | High | Approved |
| Gray Box Testing | `Foundation/Gray-Box-Testing.md` | Foundation | Foundation | Black Box Testing, White Box Testing | Medium | Approved |
| Equivalence Partitioning | `Specification-Based/Equivalence-Partitioning.md` | Specification-Based | Foundation | Black Box Testing | High | Approved |
| Boundary Value Analysis | `Specification-Based/Boundary-Value-Analysis.md` | Specification-Based | Foundation | Equivalence Partitioning | High | Approved |
| Decision Table Testing | `Specification-Based/Decision-Table-Testing.md` | Specification-Based | Intermediate | Black Box Testing | High | Approved |
| State Transition Testing | `Specification-Based/State-Transition-Testing.md` | Specification-Based | Intermediate | Black Box Testing | High | Approved |
| Cause-Effect Graphing | `Specification-Based/Cause-Effect-Graphing.md` | Specification-Based | Intermediate | Decision Table Testing | Medium | Approved |
| Use Case Testing | `Specification-Based/Use-Case-Testing.md` | Specification-Based | Intermediate | Black Box Testing | Medium | Approved |
| Statement Coverage | `Structure-Based/Statement-Coverage.md` | Structure-Based | Intermediate | White Box Testing | Medium | Approved |
| Branch Coverage | `Structure-Based/Branch-Coverage.md` | Structure-Based | Intermediate | Statement Coverage | Medium | Approved |
| Decision Coverage | `Structure-Based/Decision-Coverage.md` | Structure-Based | Advanced | Branch Coverage | Low | Approved |
| Condition Coverage | `Structure-Based/Condition-Coverage.md` | Structure-Based | Advanced | Decision Coverage | Low | Approved |
| Path Coverage | `Structure-Based/Path-Coverage.md` | Structure-Based | Advanced | Branch Coverage | Low | Approved |
| Modified Condition Decision Coverage (MC/DC) | `Structure-Based/Modified-Condition-Decision-Coverage-(MC-DC).md` | Structure-Based | Advanced | Condition Coverage | Low | Approved |
| Error Guessing | `Experience-Based/Error-Guessing.md` | Experience-Based | Foundation | Black Box Testing | Medium | Approved |
| Exploratory Testing | `Experience-Based/Exploratory-Testing.md` | Experience-Based | Intermediate | Black Box Testing | Medium | Approved |
| Session-Based Testing | `Experience-Based/Session-Based-Testing.md` | Experience-Based | Intermediate | Exploratory Testing | Medium | Approved |
| Checklist-Based Testing | `Experience-Based/Checklist-Based-Testing.md` | Experience-Based | Intermediate | Black Box Testing | Medium | Approved |
| Pairwise Testing | `Combinatorial/Pairwise-Testing.md` | Combinatorial | Advanced | Equivalence Partitioning | Medium | Approved |
| Orthogonal Array Testing | `Combinatorial/Orthogonal-Array-Testing.md` | Combinatorial | Advanced | Pairwise Testing | Low | Approved |
| Combinatorial Testing | `Combinatorial/Combinatorial-Testing.md` | Combinatorial | Advanced | Pairwise Testing | Low | Approved |
| Model-Based Testing | `Model-Based/Model-Based-Testing.md` | Model-Based | Advanced | State Transition Testing | Medium | Approved |
| Finite State Machine Testing | `Model-Based/Finite-State-Machine-Testing.md` | Model-Based | Advanced | State Transition Testing | Medium | Approved |
| Mutation Testing | `Advanced/Mutation-Testing.md` | Advanced | Advanced | White Box Testing | Low | Approved |
| Fuzz Testing | `Advanced/Fuzz-Testing.md` | Advanced | Advanced | Black Box Testing | Medium | Approved |
| Property-Based Testing | `Advanced/Property-Based-Testing.md` | Advanced | Advanced | Black Box Testing | Low | Approved |
| AI-Assisted Test Design | `Advanced/AI-Assisted-Test-Design.md` | Advanced | Advanced | Black Box Testing | High | Approved |
| Prompt-Based Test Generation | `Advanced/Prompt-Based-Test-Generation.md` | Advanced | Advanced | AI-Assisted Test Design | High | Approved |
| Chaos Testing | `Advanced/Chaos-Testing.md` | Advanced | Advanced | QA Risk-Based Testing, confirmed system architecture context | Medium | Approved |

## Category Summary

| Category | Articles | Status |
|---|---:|---|
| Foundation | 3 | Approved |
| Specification-Based | 6 | Approved |
| Structure-Based | 6 | Approved |
| Experience-Based | 4 | Approved |
| Combinatorial | 3 | Approved |
| Model-Based | 2 | Approved |
| Advanced | 6 | Approved |
| **Total** | **30** | **Approved** |

## Dependency Guidance

```text
Black Box Testing
├── Specification-Based techniques
├── Experience-Based techniques
├── Pairwise / Combinatorial
├── Fuzz / Property-Based
└── AI-Assisted Test Design → Prompt-Based Test Generation

White Box Testing
└── Statement → Branch/Decision → Condition → selected Path / MC/DC

State Transition Testing
└── Finite State Machine Testing → Model-Based Testing
```

Dependencies are learning guidance, not runtime dependencies. Cross-domain prerequisites name their owning domain explicitly; contextual prerequisites such as current system architecture must come from authoritative project sources.

## Cross-Domain Boundaries

- QA lifecycle, strategy, risk and defect processes → `../qa/`
- API-specific behavior/testing → `../api/`
- database-specific behavior/testing → `../database/`
- business entities, workflows and industry rules → `../domain/`

A technique may be applied inside another domain without transferring ownership of the underlying technology or business concept.

## Quality and Freeze Baseline

```text
Folder: shared/knowledge/testing-techniques/
Physical Knowledge Articles: 30
Cataloged Knowledge Articles: 30
Catalog Status: Approved
Baseline State: Frozen
Freeze Date: 2026-08-13
Review Level: Structural + Content Depth + Cross-Article + Cross-Domain
```

The 30-article baseline was normalized from the legacy draft generation to the current Knowledge Article standard. Review covered heading hierarchy, metadata, semantic depth, technique boundaries, practical examples, cross-references, assumption safety, and QA-AI retrieval usefulness.

## Status Definitions

- `Approved` — passed structural and content review and belongs to the active baseline.
- `Deprecated` — retained only for historical compatibility.

`Frozen` is a repository baseline state, not article lifecycle metadata.

## References

- `README.md`
- `../../standards/Knowledge-Article.md`
- `../../standards/Metadata.md`
- `../../standards/Naming.md`
- `../../glossary/QA-Terms.md`