# Testing Techniques Catalog

## Purpose

The **Testing Techniques** catalog defines the knowledge architecture and implementation roadmap for software testing techniques within the QA-AI framework.

Its primary objectives are to:

- Establish a structured knowledge base for software testing techniques.
- Organize testing techniques into logical categories based on industry-recognized classifications.
- Provide a consistent learning path for QA engineers and AI capabilities.
- Serve as the implementation backlog for testing technique knowledge articles.
- Enable reusable knowledge across multiple QA skills and workflows.
- Support long-term scalability and maintainability of the knowledge repository.

Rather than acting as a simple index of documents, this catalog serves as the authoritative roadmap for developing and maintaining the Testing Techniques knowledge domain.

---

## Scope

This catalog covers testing techniques that support:

- Test analysis
- Test design
- Test optimization
- Test coverage improvement
- Defect detection
- Quality risk reduction

The catalog focuses on **how test cases are designed and derived**.

The following topics are intentionally excluded because they belong to other knowledge domains.

| Topic | Knowledge Domain |
|---------|------------------|
| SDLC | QA |
| STLC | QA |
| Test Planning | QA |
| Test Strategy | QA |
| Test Estimation | QA |
| Test Management | QA |
| Risk-Based Testing Strategy | QA |
| Regression Testing | QA |
| Smoke Testing | QA |
| Sanity Testing | QA |
| API Testing | API |
| Database Testing | Database |
| Performance Testing | QA |
| Security Testing | QA |
| Accessibility Testing | QA |

---

## Objectives

The Testing Techniques knowledge base aims to:

- Build a comprehensive understanding of software testing techniques.
- Explain the principles behind each testing technique.
- Describe when each technique should be applied.
- Improve test design quality and efficiency.
- Reduce redundant and ineffective test cases.
- Increase functional and logical coverage.
- Support AI reasoning during test generation.
- Promote reusable testing knowledge across multiple domains.

---

## Knowledge Architecture

Testing techniques are organized according to internationally recognized software testing classifications and practical industry usage.

Each category represents a family of techniques sharing similar principles and objectives.

```text
Testing Techniques

├── Foundation
│
├── Specification-Based Techniques
│
├── Structure-Based Techniques
│
├── Experience-Based Techniques
│
├── Combinatorial Techniques
│
├── Model-Based Techniques
│
└── Advanced Techniques
```

This architecture separates techniques by **testing methodology**, not by testing phase, testing level, or software domain.

---

## Knowledge Map

### Foundation

Foundation articles introduce the core testing approaches that every QA engineer should understand before learning specific test design techniques.

```text
Foundation

├── Black Box Testing
├── White Box Testing
└── Gray Box Testing
```

These articles establish the conceptual foundation for all subsequent testing techniques.

---

### Specification-Based Techniques

Specification-Based Techniques derive test cases directly from requirements, business rules, functional specifications, or observable system behavior.

```text
Specification-Based Techniques

├── Equivalence Partitioning
├── Boundary Value Analysis
├── Decision Table Testing
├── State Transition Testing
├── Cause-Effect Graphing
└── Use Case Testing
```

These techniques are the primary methods used for functional test design and are widely adopted in manual testing.

---

### Structure-Based Techniques

Structure-Based Techniques analyze the internal implementation of software to evaluate code coverage and execution paths.

```text
Structure-Based Techniques

├── Statement Coverage
├── Branch Coverage
├── Decision Coverage
├── Condition Coverage
├── Path Coverage
└── Modified Condition Decision Coverage (MC/DC)
```

These techniques are commonly applied during white-box testing and are particularly valuable in high-reliability and safety-critical systems.

---

### Experience-Based Techniques

Experience-Based Techniques leverage tester expertise, domain knowledge, historical defects, and intuition.

```text
Experience-Based Techniques

├── Error Guessing
├── Exploratory Testing
├── Session-Based Testing
└── Checklist-Based Testing
```

These techniques complement structured test design methods by helping uncover unexpected defects and usability issues.

---

### Combinatorial Techniques

Combinatorial Techniques optimize test suites by selecting representative combinations of input parameters while maintaining effective coverage.

```text
Combinatorial Techniques

├── Pairwise Testing
├── Orthogonal Array Testing
└── Combinatorial Testing
```

These techniques are especially valuable for systems with numerous configurable inputs or complex parameter interactions.

---

### Model-Based Techniques

Model-Based Techniques generate test cases from abstract representations of system behavior, workflows, or state models.

```text
Model-Based Techniques

├── Model-Based Testing
└── Finite State Machine Testing
```

These techniques improve consistency, traceability, and coverage for systems with complex business logic.

---

### Advanced Techniques

Advanced Techniques address specialized testing scenarios and modern software engineering practices.

```text
Advanced Techniques

├── Mutation Testing
├── Fuzz Testing
├── Property-Based Testing
├── AI-Assisted Test Design
├── Prompt-Based Test Generation
└── Chaos Testing
```

These techniques extend traditional testing practices to support modern architectures, AI-assisted quality assurance, and advanced software validation.
## Article Catalog

The following catalog defines all planned knowledge articles for the **Testing Techniques** knowledge base.

Each article is classified by category, learning level, implementation priority, prerequisite knowledge, and current implementation status.

| Article | Category | Level | Prerequisites | Priority | Status |
|----------|----------|-------|---------------|----------|--------|
| Black Box Testing | Foundation | Foundation | None | High | Planned |
| White Box Testing | Foundation | Foundation | None | High | Planned |
| Gray Box Testing | Foundation | Foundation | Black Box Testing, White Box Testing | Medium | Planned |
| Equivalence Partitioning | Specification-Based | Foundation | Black Box Testing | High | Planned |
| Boundary Value Analysis | Specification-Based | Foundation | Black Box Testing, Equivalence Partitioning | High | Planned |
| Decision Table Testing | Specification-Based | Intermediate | Black Box Testing | High | Planned |
| State Transition Testing | Specification-Based | Intermediate | Black Box Testing | High | Planned |
| Cause-Effect Graphing | Specification-Based | Intermediate | Decision Table Testing | Medium | Planned |
| Use Case Testing | Specification-Based | Intermediate | Black Box Testing | Medium | Planned |
| Statement Coverage | Structure-Based | Intermediate | White Box Testing | Medium | Planned |
| Branch Coverage | Structure-Based | Intermediate | Statement Coverage | Medium | Planned |
| Decision Coverage | Structure-Based | Advanced | Branch Coverage | Low | Planned |
| Condition Coverage | Structure-Based | Advanced | Decision Coverage | Low | Planned |
| Path Coverage | Structure-Based | Advanced | Branch Coverage | Low | Planned |
| Modified Condition Decision Coverage (MC/DC) | Structure-Based | Advanced | Condition Coverage | Low | Planned |
| Error Guessing | Experience-Based | Foundation | Black Box Testing | Medium | Planned |
| Exploratory Testing | Experience-Based | Intermediate | Black Box Testing | Medium | Planned |
| Session-Based Testing | Experience-Based | Intermediate | Exploratory Testing | Medium | Planned |
| Checklist-Based Testing | Experience-Based | Intermediate | Black Box Testing | Medium | Planned |
| Pairwise Testing | Combinatorial | Advanced | Equivalence Partitioning | Medium | Planned |
| Orthogonal Array Testing | Combinatorial | Advanced | Pairwise Testing | Low | Planned |
| Combinatorial Testing | Combinatorial | Advanced | Pairwise Testing | Low | Planned |
| Model-Based Testing | Model-Based | Advanced | State Transition Testing | Medium | Planned |
| Finite State Machine Testing | Model-Based | Advanced | State Transition Testing | Medium | Planned |
| Mutation Testing | Advanced | Advanced | White Box Testing | Low | Planned |
| Fuzz Testing | Advanced | Advanced | Black Box Testing | Medium | Planned |
| Property-Based Testing | Advanced | Advanced | Black Box Testing | Low | Planned |
| AI-Assisted Test Design | Advanced | Advanced | Black Box Testing | High | Planned |
| Prompt-Based Test Generation | Advanced | Advanced | AI-Assisted Test Design | High | Planned |
| Chaos Testing | Advanced | Advanced | System Architecture Fundamentals | Medium | Planned |

---

## Category Summary

| Category | Articles | Purpose |
|----------|---------:|---------|
| Foundation | 3 | Introduce the primary software testing approaches. |
| Specification-Based Techniques | 6 | Design test cases from requirements and specifications. |
| Structure-Based Techniques | 6 | Evaluate implementation coverage and execution paths. |
| Experience-Based Techniques | 4 | Apply tester knowledge and practical experience. |
| Combinatorial Techniques | 3 | Optimize test suites with representative combinations. |
| Model-Based Techniques | 2 | Generate tests from behavioral or state models. |
| Advanced Techniques | 6 | Cover specialized and emerging testing approaches. |
| **Total** | **30** | |

---

## Knowledge Levels

Knowledge articles are grouped into progressive learning levels.

### Foundation

Foundation articles introduce the essential concepts every QA engineer should understand before learning more advanced testing techniques.

Characteristics:

- No or minimal prerequisites
- Frequently applied in software testing
- Essential for understanding subsequent techniques

---

### Intermediate

Intermediate articles expand upon foundational knowledge and introduce more specialized test design approaches.

Characteristics:

- Require one or more prerequisite concepts
- Improve testing effectiveness and coverage
- Commonly used by experienced QA engineers

---

### Advanced

Advanced articles focus on specialized, high-complexity, or emerging testing techniques.

Characteristics:

- Require multiple prerequisite concepts
- Often applied in complex or large-scale systems
- Support advanced QA practices and AI-assisted workflows

---

## Priority Definitions

Priority indicates the recommended implementation order of individual knowledge articles.

| Priority | Description |
|----------|-------------|
| High | Essential knowledge required by multiple skills and workflows. |
| Medium | Important supporting knowledge that extends core testing capabilities. |
| Low | Specialized or advanced knowledge intended for specific scenarios. |

---

## Status Definitions

Status indicates the current implementation state of each knowledge article.

| Status | Description |
|--------|-------------|
| Planned | The article has been identified but has not yet been implemented. |
| In Progress | The article is currently being written or updated. |
| Review | The article has been completed and is under quality review. |
| Approved | The article has been reviewed and approved for production use. |
| Deprecated | The article is retained for historical purposes and is no longer recommended. |
## Learning Path

The following learning path is recommended for QA engineers who are learning software testing techniques.

```text
Foundation
        │
        ▼
Specification-Based Techniques
        │
        ▼
Experience-Based Techniques
        │
        ▼
Structure-Based Techniques
        │
        ▼
Combinatorial Techniques
        │
        ▼
Model-Based Techniques
        │
        ▼
Advanced Techniques
```

This learning path gradually introduces testing techniques from fundamental concepts to advanced methodologies. Each category builds upon the knowledge established in the previous stage, helping learners develop strong analytical and test design skills.

---

## Implementation Phases

Knowledge articles should be implemented incrementally to establish a solid foundation before introducing more advanced concepts.

### Phase 1 — Foundation

**Objective**

Establish a common understanding of the fundamental software testing approaches.

**Articles**

- Black Box Testing
- White Box Testing
- Gray Box Testing

---

### Phase 2 — Core Test Design

**Objective**

Implement the most widely used specification-based testing techniques.

**Articles**

- Equivalence Partitioning
- Boundary Value Analysis
- Decision Table Testing
- State Transition Testing

---

### Phase 3 — Practical Techniques

**Objective**

Expand practical testing capability through experience-based and complementary specification-based techniques.

**Articles**

- Cause-Effect Graphing
- Use Case Testing
- Error Guessing
- Exploratory Testing
- Session-Based Testing
- Checklist-Based Testing

---

### Phase 4 — Structure-Based Techniques

**Objective**

Introduce implementation-aware testing techniques and code coverage concepts.

**Articles**

- Statement Coverage
- Branch Coverage
- Decision Coverage
- Condition Coverage
- Path Coverage
- Modified Condition Decision Coverage (MC/DC)

---

### Phase 5 — Optimization Techniques

**Objective**

Improve testing efficiency by reducing redundant test combinations while maintaining effective coverage.

**Articles**

- Pairwise Testing
- Orthogonal Array Testing
- Combinatorial Testing

---

### Phase 6 — Model-Based Techniques

**Objective**

Introduce techniques that derive test cases from behavioral and state models.

**Articles**

- Model-Based Testing
- Finite State Machine Testing

---

### Phase 7 — Advanced Techniques

**Objective**

Introduce specialized and emerging testing techniques used in modern software quality assurance.

**Articles**

- Mutation Testing
- Fuzz Testing
- Property-Based Testing
- AI-Assisted Test Design
- Prompt-Based Test Generation
- Chaos Testing

---

## Dependency Map

The following dependency map illustrates conceptual relationships between knowledge articles.

```text
Black Box Testing
        │
        ├── Equivalence Partitioning
        │       │
        │       └── Boundary Value Analysis
        │
        ├── Decision Table Testing
        │       │
        │       └── Cause-Effect Graphing
        │
        ├── State Transition Testing
        │       │
        │       ├── Finite State Machine Testing
        │       │       │
        │       │       └── Model-Based Testing
        │       │
        │       └── Use Case Testing
        │
        ├── Error Guessing
        ├── Exploratory Testing
        │       │
        │       └── Session-Based Testing
        │
        └── Checklist-Based Testing

White Box Testing
        │
        └── Statement Coverage
                │
                └── Branch Coverage
                        │
                        ├── Decision Coverage
                        ├── Condition Coverage
                        ├── Path Coverage
                        └── Modified Condition Decision Coverage (MC/DC)

Equivalence Partitioning
        │
        └── Pairwise Testing
                │
                ├── Orthogonal Array Testing
                └── Combinatorial Testing

AI-Assisted Test Design
        │
        └── Prompt-Based Test Generation
```

---

## Implementation Guidelines

When implementing knowledge articles, follow these principles:

- Complete articles according to the implementation phases.
- Satisfy prerequisite knowledge before implementing dependent articles.
- Follow the standard Knowledge Article template.
- Keep articles vendor-independent and reusable.
- Avoid overlapping with other knowledge domains.
- Update the article status after each review cycle.
- Maintain consistency with repository naming and documentation standards.

---

## Expansion Roadmap

Future knowledge articles may include:

### Emerging Techniques

- Differential Testing
- Metamorphic Testing
- Search-Based Software Testing
- Autonomous Testing

### AI-Driven Testing

- AI Test Oracles
- LLM-Based Test Generation
- AI-Based Test Prioritization
- Self-Healing Test Design

### Specialized Test Design

- Accessibility Test Design
- Security Test Design
- Performance Test Design
- Mobile Test Design
- Cloud-Native Test Design

Future additions should remain within the scope of **testing techniques** and avoid overlapping with QA processes, testing types, or technology-specific knowledge.

---

## References

Related repository resources include:

- `shared/knowledge/README.md`
- `shared/knowledge/qa/`
- `shared/glossary/QA-Terms.md`
- `shared/standards/`
- `shared/templates/`
- `shared/checklists/`
- `skills/`
- `workflows/`