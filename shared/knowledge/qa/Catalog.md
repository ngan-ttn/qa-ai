# Quality Assurance Catalog

## Purpose

The **Quality Assurance** catalog defines the knowledge architecture and implementation roadmap for quality assurance concepts, methodologies, and engineering practices within the QA-AI framework.

Its primary objectives are to:

- Establish a structured knowledge base for software quality assurance.
- Organize QA concepts into logical knowledge domains.
- Provide a consistent learning path for QA engineers and AI capabilities.
- Serve as the implementation backlog for QA knowledge articles.
- Enable reusable QA knowledge across multiple skills and workflows.
- Support long-term scalability and maintainability of the knowledge repository.

Rather than acting as a simple document index, this catalog serves as the authoritative roadmap for developing and maintaining the Quality Assurance knowledge domain.

---

## Scope

This catalog covers knowledge related to software quality assurance, including:

- Quality engineering principles
- Software development and testing lifecycles
- Requirement engineering
- Test management
- Defect management
- Quality assurance practices
- Continuous quality improvement

The catalog focuses on **quality assurance methodologies, processes, and engineering practices**.

The following topics are intentionally excluded because they belong to other knowledge domains.

| Topic | Knowledge Domain |
|---------|------------------|
| Equivalence Partitioning | Testing Techniques |
| Boundary Value Analysis | Testing Techniques |
| Decision Table Testing | Testing Techniques |
| State Transition Testing | Testing Techniques |
| API Architecture | API |
| HTTP | API |
| SQL | Database |
| Database Design | Database |
| Banking | Domain |
| Healthcare | Domain |
| Warehouse Management | Domain |

---

## Objectives

The Quality Assurance knowledge base aims to:

- Build a comprehensive understanding of software quality assurance.
- Explain QA processes throughout the software development lifecycle.
- Promote consistent quality engineering practices.
- Improve requirement analysis and defect prevention.
- Strengthen planning, execution, and quality governance.
- Support AI reasoning throughout QA workflows.
- Establish reusable QA knowledge across projects and industries.

---

## Knowledge Architecture

Quality Assurance knowledge is organized according to major QA disciplines commonly adopted in professional software engineering.

```text
Quality Assurance

├── Foundations
│
├── Requirement Engineering
│
├── Test Management
│
├── Defect Management
│
├── Quality Practices
│
└── Continuous Improvement
```

Each category groups related concepts that support a specific aspect of software quality assurance.

---

## Knowledge Map

### Foundations

Foundation articles introduce the core concepts that define software quality assurance and establish the common language used throughout the repository.

```text
Foundations

├── Software Quality
├── Quality Assurance vs Quality Control
├── SDLC
├── STLC
└── Testing Principles
```

These articles provide the conceptual foundation for all subsequent QA knowledge.

---

### Requirement Engineering

Requirement Engineering focuses on understanding, analyzing, validating, and tracing software requirements throughout the development lifecycle.

```text
Requirement Engineering

├── Requirement Analysis
├── Requirement Traceability
├── Business Rule Analysis
└── Acceptance Criteria
```

These articles support accurate requirement understanding and improve downstream testing quality.

---

### Test Management

Test Management covers planning, organizing, monitoring, and controlling software testing activities.

```text
Test Management

├── Test Planning
├── Test Strategy
├── Test Estimation
├── Test Environment Management
└── Test Data Management
```

These articles provide guidance for managing testing activities efficiently and consistently.

---

### Defect Management

Defect Management focuses on identifying, classifying, tracking, analyzing, and resolving software defects.

```text
Defect Management

├── Defect Lifecycle
├── Defect Severity and Priority
├── Root Cause Analysis
└── Defect Triage
```

These articles help improve defect handling and quality communication across development teams.

---

### Quality Practices

Quality Practices describe engineering approaches that improve software quality throughout the testing lifecycle.

```text
Quality Practices

├── Risk-Based Testing
├── Regression Testing
├── Smoke Testing
├── Sanity Testing
├── Test Coverage
└── Release Readiness
```

These practices support effective test execution, risk reduction, and release confidence.

---

### Continuous Improvement

Continuous Improvement focuses on measuring, evaluating, and improving QA effectiveness over time.

```text
Continuous Improvement

├── Test Metrics
├── Test Reporting
├── Lessons Learned
└── QA Best Practices
```

These articles promote continuous learning and long-term quality improvement.
## Article Catalog

The following catalog defines all planned knowledge articles for the **Quality Assurance** knowledge base.

Each article is classified by category, learning level, prerequisite knowledge, implementation priority, and current implementation status.

| Article | Category | Level | Prerequisites | Priority | Status |
|----------|----------|-------|---------------|----------|--------|
| Software Quality | Foundations | Foundation | None | High | Planned |
| Quality Assurance vs Quality Control | Foundations | Foundation | Software Quality | High | Planned |
| SDLC | Foundations | Foundation | None | High | Planned |
| STLC | Foundations | Foundation | SDLC | High | Planned |
| Testing Principles | Foundations | Foundation | Software Quality | High | Planned |
| Requirement Analysis | Requirement Engineering | Foundation | STLC | High | Planned |
| Requirement Traceability | Requirement Engineering | Intermediate | Requirement Analysis | High | Planned |
| Business Rule Analysis | Requirement Engineering | Intermediate | Requirement Analysis | High | Planned |
| Acceptance Criteria | Requirement Engineering | Foundation | Requirement Analysis | High | Planned |
| Test Planning | Test Management | Intermediate | STLC | High | Planned |
| Test Strategy | Test Management | Intermediate | Test Planning | High | Planned |
| Test Estimation | Test Management | Advanced | Test Planning | Medium | Planned |
| Test Environment Management | Test Management | Intermediate | Test Planning | Medium | Planned |
| Test Data Management | Test Management | Intermediate | Test Planning | High | Planned |
| Defect Lifecycle | Defect Management | Foundation | STLC | High | Planned |
| Defect Severity and Priority | Defect Management | Foundation | Defect Lifecycle | High | Planned |
| Root Cause Analysis | Defect Management | Advanced | Defect Lifecycle | Medium | Planned |
| Defect Triage | Defect Management | Intermediate | Defect Lifecycle | Medium | Planned |
| Risk-Based Testing | Quality Practices | Advanced | Test Strategy | High | Planned |
| Regression Testing | Quality Practices | Foundation | STLC | High | Planned |
| Smoke Testing | Quality Practices | Foundation | STLC | High | Planned |
| Sanity Testing | Quality Practices | Foundation | Regression Testing | Medium | Planned |
| Test Coverage | Quality Practices | Intermediate | Test Planning | High | Planned |
| Release Readiness | Quality Practices | Intermediate | Test Strategy | Medium | Planned |
| Test Metrics | Continuous Improvement | Intermediate | Test Planning | Medium | Planned |
| Test Reporting | Continuous Improvement | Intermediate | Test Metrics | Medium | Planned |
| Lessons Learned | Continuous Improvement | Intermediate | Test Reporting | Low | Planned |
| QA Best Practices | Continuous Improvement | Advanced | Test Strategy | Medium | Planned |

---

## Category Summary

| Category | Articles | Purpose |
|----------|---------:|---------|
| Foundations | 5 | Introduce the core concepts of software quality assurance. |
| Requirement Engineering | 4 | Understand, analyze, and manage software requirements. |
| Test Management | 5 | Plan, organize, and control testing activities. |
| Defect Management | 4 | Manage defects throughout their lifecycle. |
| Quality Practices | 6 | Improve software quality through proven QA practices. |
| Continuous Improvement | 4 | Measure, evaluate, and continuously improve QA effectiveness. |
| **Total** | **28** | |

---

## Knowledge Levels

Knowledge articles are organized into progressive learning levels.

### Foundation

Foundation articles introduce the essential concepts every QA engineer should understand.

Characteristics:

- Minimal prerequisites
- Frequently used in software projects
- Establish the basis for all subsequent QA knowledge

---

### Intermediate

Intermediate articles expand foundational knowledge by introducing practical QA methodologies and engineering practices.

Characteristics:

- Require prior understanding of QA fundamentals
- Frequently applied in day-to-day QA activities
- Improve planning, execution, and quality control

---

### Advanced

Advanced articles focus on organizational practices, strategic thinking, and continuous quality improvement.

Characteristics:

- Require multiple prerequisite concepts
- Applicable to complex projects and mature QA organizations
- Support QA leadership and AI-assisted quality engineering

---

## Priority Definitions

Priority indicates the recommended implementation order of individual knowledge articles.

| Priority | Description |
|----------|-------------|
| High | Core QA knowledge required by multiple skills, workflows, and repositories. |
| Medium | Supporting knowledge that extends QA capability. |
| Low | Specialized knowledge intended for mature QA practices. |

---

## Status Definitions

Status indicates the implementation state of each knowledge article.

| Status | Description |
|--------|-------------|
| Planned | The article has been identified but has not yet been implemented. |
| In Progress | The article is currently being developed. |
| Review | The article has completed drafting and is under review. |
| Approved | The article has passed review and is ready for production use. |
| Deprecated | The article is retained for historical purposes and is no longer recommended. |

## Learning Path

The following learning path is recommended for QA engineers who are developing professional software quality assurance knowledge.

```text
Foundations
        │
        ▼
Requirement Engineering
        │
        ▼
Test Management
        │
        ▼
Defect Management
        │
        ▼
Quality Practices
        │
        ▼
Continuous Improvement
```

The learning path gradually introduces software quality assurance concepts from fundamental principles to advanced engineering practices. Each category builds upon the knowledge established in the previous stage, enabling learners to develop comprehensive QA capabilities.

---

## Implementation Phases

Knowledge articles should be implemented incrementally to establish a solid quality assurance foundation before introducing advanced QA practices.

### Phase 1 — Foundations

**Objective**

Establish a common understanding of software quality assurance and software development lifecycles.

**Articles**

- Software Quality
- Quality Assurance vs Quality Control
- SDLC
- STLC
- Testing Principles

---

### Phase 2 — Requirement Engineering

**Objective**

Develop the ability to analyze, validate, and manage software requirements effectively.

**Articles**

- Requirement Analysis
- Requirement Traceability
- Business Rule Analysis
- Acceptance Criteria

---

### Phase 3 — Test Management

**Objective**

Introduce planning, organization, estimation, and management techniques for software testing.

**Articles**

- Test Planning
- Test Strategy
- Test Estimation
- Test Environment Management
- Test Data Management

---

### Phase 4 — Defect Management

**Objective**

Build knowledge for effective defect handling, communication, and continuous quality improvement.

**Articles**

- Defect Lifecycle
- Defect Severity and Priority
- Defect Triage
- Root Cause Analysis

---

### Phase 5 — Quality Practices

**Objective**

Introduce practical QA methodologies that improve testing effectiveness and release quality.

**Articles**

- Risk-Based Testing
- Regression Testing
- Smoke Testing
- Sanity Testing
- Test Coverage
- Release Readiness

---

### Phase 6 — Continuous Improvement

**Objective**

Develop continuous improvement practices through measurement, reporting, and organizational learning.

**Articles**

- Test Metrics
- Test Reporting
- Lessons Learned
- QA Best Practices

---

## Dependency Map

The following dependency map illustrates conceptual relationships between knowledge articles.

```text
Software Quality
        │
        ├── Quality Assurance vs Quality Control
        │
        ├── SDLC
        │       │
        │       └── STLC
        │               │
        │               ├── Requirement Analysis
        │               │       ├── Requirement Traceability
        │               │       ├── Business Rule Analysis
        │               │       └── Acceptance Criteria
        │               │
        │               ├── Test Planning
        │               │       ├── Test Strategy
        │               │       ├── Test Estimation
        │               │       ├── Test Environment Management
        │               │       └── Test Data Management
        │               │
        │               └── Defect Lifecycle
        │                       ├── Defect Severity and Priority
        │                       ├── Defect Triage
        │                       └── Root Cause Analysis
        │
        ├── Regression Testing
        │       └── Sanity Testing
        │
        ├── Test Strategy
        │       ├── Risk-Based Testing
        │       └── Release Readiness
        │
        └── Test Planning
                ├── Test Coverage
                └── Test Metrics
                        │
                        └── Test Reporting
                                │
                                ├── Lessons Learned
                                └── QA Best Practices
```

---

## Implementation Guidelines

When implementing knowledge articles, follow these principles:

- Implement articles according to the defined implementation phases.
- Complete prerequisite articles before dependent articles.
- Follow the standard Knowledge Article template.
- Keep articles technology-independent whenever possible.
- Avoid overlapping with Testing Techniques, API, Database, and Domain knowledge.
- Maintain consistency with repository documentation standards.
- Update article status after every review cycle.
- Periodically review dependencies as the knowledge base evolves.

---

## Expansion Roadmap

Future knowledge articles may include:

### Modern QA Practices

- Shift-Left Testing
- Shift-Right Testing
- Continuous Testing
- DevTestOps
- Quality Engineering

### Quality Frameworks

- Test Maturity Model Integration (TMMi)
- Test Process Improvement (TPI)
- ISO 25010 Software Quality Model
- IEEE Software Testing Standards

### AI-Driven Quality Assurance

- AI-Assisted Requirement Analysis
- AI-Assisted Test Planning
- AI-Assisted Defect Analysis
- AI Quality Governance

Future additions should remain within the scope of **quality assurance methodologies, engineering practices, and quality management**, while avoiding overlap with other knowledge domains.

---

## References

Related repository resources include:

- `shared/knowledge/README.md`
- `shared/knowledge/testing-techniques/`
- `shared/glossary/QA-Terms.md`
- `shared/standards/`
- `shared/templates/`
- `shared/checklists/`
- `skills/`
- `workflows/`