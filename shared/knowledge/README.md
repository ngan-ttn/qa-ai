# Knowledge

## Purpose

The `knowledge` module provides reusable domain knowledge that supports AI reasoning across the QA-AI framework.

Its purpose is to centralize concepts, methodologies, technical references, and domain-specific knowledge that can be shared by multiple skills and workflows.

This module serves as the knowledge base for the repository, reducing duplication and promoting consistent understanding across AI capabilities.

---

## Scope

This module contains reference materials that explain concepts, practices, technologies, and business domains relevant to software quality assurance.

It does not define repository standards, output templates, reasoning patterns, or workflow execution.

Instead, it provides the knowledge required to support those activities.

---

## Module Structure

```text
shared/
└── knowledge/
    ├── README.md
    ├── testing-techniques/
    ├── qa/
    ├── api/
    ├── database/
    └── domain/
```

---

## Knowledge Categories

### Testing Techniques

Provides knowledge about testing methodologies and test design techniques.

Typical topics include:

- Black Box Testing
- White Box Testing
- Boundary Value Analysis
- Equivalence Partitioning
- Decision Table Testing
- State Transition Testing
- Pairwise Testing
- Error Guessing

---

### QA

Provides knowledge about software quality assurance processes and practices.

Typical topics include:

- SDLC
- STLC
- Test Planning
- Defect Management
- Risk-Based Testing
- Regression Testing
- Test Strategy

---

### API

Provides knowledge about API architecture, communication, and testing.

Typical topics include:

- HTTP
- REST
- Authentication
- Authorization
- Status Codes
- API Versioning
- API Security

---

### Database

Provides knowledge about database concepts and data validation.

Typical topics include:

- SQL
- Transactions
- Indexes
- Relationships
- Constraints
- Normalization
- Data Integrity

---

### Domain

Provides business-domain knowledge that supports domain-specific testing activities.

Typical topics include:

- Healthcare
- Banking
- E-Commerce
- Loyalty
- Warehouse Management
- Inventory Management

---

## Design Principles

Knowledge articles should:

- Explain concepts rather than define terminology.
- Remain reusable across multiple skills and workflows.
- Be organized by subject area.
- Avoid duplicating standards, templates, or glossary entries.
- Support AI reasoning through accurate and structured knowledge.

---

## Relationships

The knowledge module is a shared resource used throughout the QA-AI framework.

Typical consumers include:

- Skills
- Workflows
- Prompt Patterns

Knowledge complements other shared modules:

- Standards define rules.
- Templates define output structures.
- Checklists define quality criteria.
- Prompt Patterns define reasoning approaches.
- Glossary defines terminology.
- Knowledge explains concepts.

---

## References

Related modules include:

- `shared/standards/`
- `shared/templates/`
- `shared/checklists/`
- `shared/prompt-patterns/`
- `shared/glossary/`
- `skills/`
- `workflows/`