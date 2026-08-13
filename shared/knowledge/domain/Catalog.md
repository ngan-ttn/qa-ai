# Domain Knowledge Catalog

## Purpose

This catalog is the authoritative inventory and knowledge architecture for `shared/knowledge/domain/`. It organizes reusable business-domain knowledge for QA and QA-AI while keeping project-specific policy, legal interpretation, organization data, thresholds, calculations, and implementation details outside the generic knowledge layer.

## Knowledge Architecture

```text
Domain Knowledge
├── Domain Fundamentals
├── Business Processes
├── Business Entities
├── Business Rules
├── Industry Domains
├── Regulatory & Compliance
└── Domain Modeling
```

## Article Catalog

| Article | Category | Level | Prerequisites | Priority | Status |
|---|---|---|---|---|---|
| Business Domain | Domain Fundamentals | Foundation | None | High | Approved |
| Domain Terminology | Domain Fundamentals | Foundation | Business Domain | High | Approved |
| Domain Knowledge | Domain Fundamentals | Foundation | Business Domain | High | Approved |
| Business Context | Domain Fundamentals | Foundation | Business Domain | High | Approved |
| Domain-Driven Thinking | Domain Fundamentals | Intermediate | Business Context | Medium | Approved |
| Business Process Fundamentals | Business Processes | Foundation | Business Context | High | Approved |
| Business Workflow | Business Processes | Foundation | Business Process Fundamentals | High | Approved |
| Process States | Business Processes | Intermediate | Business Workflow | Medium | Approved |
| Process Lifecycle | Business Processes | Intermediate | Business Workflow | Medium | Approved |
| Process Exceptions | Business Processes | Intermediate | Business Workflow | Medium | Approved |
| Business Events | Business Processes | Intermediate | Business Workflow | Medium | Approved |
| Business Entity | Business Entities | Foundation | Business Domain | High | Approved |
| Entity Relationships | Business Entities | Foundation | Business Entity | High | Approved |
| Entity Lifecycle | Business Entities | Intermediate | Business Entity | Medium | Approved |
| Master Data | Business Entities | Foundation | Business Entity | High | Approved |
| Transaction Data | Business Entities | Foundation | Business Entity | High | Approved |
| Reference Data | Business Entities | Foundation | Business Entity | Medium | Approved |
| Business Rule Fundamentals | Business Rules | Foundation | Business Context | High | Approved |
| Validation Rules | Business Rules | Foundation | Business Rule Fundamentals | High | Approved |
| Decision Rules | Business Rules | Intermediate | Business Rule Fundamentals | High | Approved |
| Calculation Rules | Business Rules | Intermediate | Business Rule Fundamentals | Medium | Approved |
| Eligibility Rules | Business Rules | Intermediate | Decision Rules | Medium | Approved |
| Rule Exceptions | Business Rules | Intermediate | Validation Rules | Medium | Approved |
| Banking | Industry Domains | Intermediate | Business Domain | Medium | Approved |
| Healthcare | Industry Domains | Intermediate | Business Domain | Medium | Approved |
| Retail | Industry Domains | Intermediate | Business Domain | Medium | Approved |
| E-Commerce | Industry Domains | Intermediate | Business Domain | High | Approved |
| Logistics | Industry Domains | Intermediate | Business Domain | High | Approved |
| Manufacturing | Industry Domains | Intermediate | Business Domain | Medium | Approved |
| Government | Industry Domains | Intermediate | Business Domain | Low | Approved |
| Regulatory Requirements | Regulatory & Compliance | Intermediate | Business Rule Fundamentals | Medium | Approved |
| Compliance | Regulatory & Compliance | Intermediate | Regulatory Requirements | Medium | Approved |
| Audit Trail | Regulatory & Compliance | Intermediate | Compliance | High | Approved |
| Data Privacy | Regulatory & Compliance | Intermediate | Compliance | High | Approved |
| Security Compliance | Regulatory & Compliance | Advanced | Compliance | Medium | Approved |
| Data Retention | Regulatory & Compliance | Advanced | Compliance | Medium | Approved |
| Domain Model | Domain Modeling | Intermediate | Business Entity, Business Workflow | High | Approved |
| Business Capabilities | Domain Modeling | Advanced | Domain Model | Medium | Approved |
| Bounded Context | Domain Modeling | Advanced | Domain-Driven Thinking, Domain Model | Medium | Approved |
| Ubiquitous Language | Domain Modeling | Intermediate | Domain-Driven Thinking | Medium | Approved |
| Event Storming | Domain Modeling | Advanced | Business Workflow, Domain Model | Low | Approved |

## Category Summary

| Category | Articles | Status |
|---|---:|---|
| Domain Fundamentals | 5 | Approved |
| Business Processes | 6 | Approved |
| Business Entities | 6 | Approved |
| Business Rules | 6 | Approved |
| Industry Domains | 7 | Approved |
| Regulatory & Compliance | 6 | Approved |
| Domain Modeling | 5 | Approved |
| **Total** | **41** | **Approved** |

## Dependency Guidance

```text
Business Domain
├── Domain Fundamentals
├── Business Context
│   ├── Business Processes
│   └── Business Rules
├── Business Entity
│   ├── Entity knowledge
│   └── Domain Model
├── Industry Domains
└── Regulatory Requirements → Compliance

Domain-Driven Thinking
├── Ubiquitous Language
└── Bounded Context
```

Dependencies are learning guidance, not mandatory runtime dependencies.

## Scope Boundaries

The catalog owns generic domain concepts and industry orientation. It does not own project-specific business rules, legal conclusions, clinical decisions, security assessment, accounting policy, or technology implementation.

Cross-domain boundaries:

- generic QA management → `../qa/`
- testing techniques → `../testing-techniques/`
- API behavior → `../api/`
- database behavior → `../database/`
- canonical business terms → `../../glossary/Business-Terms.md`

## Quality and Freeze Baseline

```text
Folder: shared/knowledge/domain/
Physical Knowledge Articles: 41
Cataloged Knowledge Articles: 41
Catalog Status: Approved
Baseline State: Frozen
Freeze Date: 2026-08-13
```

All 41 articles were reviewed for the mandatory 12-section structure, semantic depth, QA applicability, business/technical boundary, unsupported-assumption safety, terminology consistency, cross-references, and QA-AI retrieval usefulness.

## Status Definitions

- `Approved` — article passed structural and content-depth review and belongs to the current baseline.
- `Deprecated` — retained only when historical compatibility requires it.

`Frozen` is a repository baseline state, not an article metadata status.

## References

- `README.md`
- `../../standards/Knowledge-Article.md`
- `../../standards/Metadata.md`
- `../../standards/Naming.md`
- `../../glossary/Business-Terms.md`