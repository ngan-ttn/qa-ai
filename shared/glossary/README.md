# Glossary

## Purpose

The `glossary` module defines a shared vocabulary for the QA-AI framework.

Its purpose is to establish consistent terminology across documentation, skills, workflows, templates, and other shared resources.

This module serves as the single source of truth for domain-specific terms used throughout the repository.

---

## Scope

This module contains standardized definitions for commonly used terms across different domains.

It does not provide implementation guidance, tutorials, or best practices.

Instead, each glossary entry defines the meaning and intended usage of a specific term.

---

## Module Structure

```text
shared/
└── glossary/
    ├── README.md
    ├── QA-Terms.md
    ├── API-Terms.md
    ├── Database-Terms.md
    └── Business-Terms.md
```

---

## Glossary Categories

### QA Terms

Defines terminology related to software quality assurance and testing activities.

Typical topics include:

- Testing types
- Testing levels
- Testing techniques
- Defect management
- Test management

---

### API Terms

Defines terminology related to API design, integration, and testing.

Typical topics include:

- HTTP
- REST
- Authentication
- Authorization
- Request and response
- API contracts

---

### Database Terms

Defines terminology related to database concepts and data management.

Typical topics include:

- Tables
- Relationships
- Transactions
- Constraints
- Indexes
- Data consistency

---

### Business Terms

Defines terminology related to business analysis and software requirements.

Typical topics include:

- Requirements
- Business rules
- User stories
- Acceptance criteria
- Actors
- Business processes

---

## Design Principles

Glossary entries should:

- Use clear and concise definitions.
- Remain domain-independent where possible.
- Use consistent terminology throughout the repository.
- Avoid implementation-specific details.
- Reference related terms where applicable.

---

## Relationships

The glossary is a shared reference used throughout the QA-AI framework.

Typical consumers include:

- Shared standards
- Shared templates
- Shared checklists
- Prompt patterns
- Skills
- Workflows

Glossary definitions should be referenced rather than duplicated in other modules.

---

## References

Related modules include:

- `shared/standards/`
- `shared/templates/`
- `shared/checklists/`
- `shared/prompt-patterns/`
- `skills/`
- `workflows/`