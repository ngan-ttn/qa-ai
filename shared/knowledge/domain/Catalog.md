# Domain Knowledge Catalog

## Purpose

This catalog is the authoritative inventory and architecture for `shared/knowledge/domain/`. It organizes reusable business-domain knowledge for QA and QA-AI while keeping project-specific policy, legal interpretation, clinical decisions, organization data, thresholds, formulas, permissions, and implementation details outside the generic knowledge layer.

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

| Article | File | Category | Level | Prerequisites | Priority | Status |
|---|---|---|---|---|---|---|
| Business Domain | `Business-Domain.md` | Domain Fundamentals | Foundation | None | High | Approved |
| Domain Terminology | `Domain-Terminology.md` | Domain Fundamentals | Foundation | Business Domain | High | Approved |
| Domain Knowledge | `Domain-Knowledge.md` | Domain Fundamentals | Foundation | Business Domain | High | Approved |
| Business Context | `Business-Context.md` | Domain Fundamentals | Foundation | Business Domain | High | Approved |
| Domain-Driven Thinking | `Domain-Driven-Thinking.md` | Domain Fundamentals | Intermediate | Business Context | Medium | Approved |
| Business Process Fundamentals | `Business-Process-Fundamentals.md` | Business Processes | Foundation | Business Context | High | Approved |
| Business Workflow | `Business-Workflow.md` | Business Processes | Foundation | Business Process Fundamentals | High | Approved |
| Process States | `Process-States.md` | Business Processes | Intermediate | Business Workflow | Medium | Approved |
| Process Lifecycle | `Process-Lifecycle.md` | Business Processes | Intermediate | Business Workflow | Medium | Approved |
| Process Exceptions | `Process-Exceptions.md` | Business Processes | Intermediate | Business Workflow | Medium | Approved |
| Business Events | `Business-Events.md` | Business Processes | Intermediate | Business Workflow | Medium | Approved |
| Business Entity | `Business-Entity.md` | Business Entities | Foundation | Business Domain | High | Approved |
| Entity Relationships | `Entity-Relationships.md` | Business Entities | Foundation | Business Entity | High | Approved |
| Entity Lifecycle | `Entity-Lifecycle.md` | Business Entities | Intermediate | Business Entity | Medium | Approved |
| Master Data | `Master-Data.md` | Business Entities | Foundation | Business Entity | High | Approved |
| Transaction Data | `Transaction-Data.md` | Business Entities | Foundation | Business Entity | High | Approved |
| Reference Data | `Reference-Data.md` | Business Entities | Foundation | Business Entity | Medium | Approved |
| Business Rule Fundamentals | `Business-Rule-Fundamentals.md` | Business Rules | Foundation | Business Context | High | Approved |
| Validation Rules | `Validation-Rules.md` | Business Rules | Foundation | Business Rule Fundamentals | High | Approved |
| Decision Rules | `Decision-Rules.md` | Business Rules | Intermediate | Business Rule Fundamentals | High | Approved |
| Calculation Rules | `Calculation-Rules.md` | Business Rules | Intermediate | Business Rule Fundamentals | Medium | Approved |
| Eligibility Rules | `Eligibility-Rules.md` | Business Rules | Intermediate | Decision Rules | Medium | Approved |
| Rule Exceptions | `Rule-Exceptions.md` | Business Rules | Intermediate | Business Rule Fundamentals | Medium | Approved |
| Banking | `Banking.md` | Industry Domains | Intermediate | Business Domain | Medium | Approved |
| Healthcare | `Healthcare.md` | Industry Domains | Intermediate | Business Domain | Medium | Approved |
| Retail | `Retail.md` | Industry Domains | Intermediate | Business Domain | Medium | Approved |
| E-Commerce | `E-Commerce.md` | Industry Domains | Intermediate | Business Domain | High | Approved |
| Logistics | `Logistics.md` | Industry Domains | Intermediate | Business Domain | High | Approved |
| Manufacturing | `Manufacturing.md` | Industry Domains | Intermediate | Business Domain | Medium | Approved |
| Government | `Government.md` | Industry Domains | Intermediate | Business Domain | Low | Approved |
| Regulatory Requirements | `Regulatory-Requirements.md` | Regulatory & Compliance | Intermediate | Business Rule Fundamentals | Medium | Approved |
| Compliance | `Compliance.md` | Regulatory & Compliance | Intermediate | Regulatory Requirements | Medium | Approved |
| Audit Trail | `Audit-Trail.md` | Regulatory & Compliance | Intermediate | Compliance | High | Approved |
| Data Privacy | `Data-Privacy.md` | Regulatory & Compliance | Intermediate | Compliance | High | Approved |
| Security Compliance | `Security-Compliance.md` | Regulatory & Compliance | Advanced | Compliance | Medium | Approved |
| Data Retention | `Data-Retention.md` | Regulatory & Compliance | Advanced | Compliance | Medium | Approved |
| Domain Model | `Domain-Model.md` | Domain Modeling | Intermediate | Business Entity, Business Workflow | High | Approved |
| Business Capabilities | `Business-Capabilities.md` | Domain Modeling | Advanced | Domain Model | Medium | Approved |
| Bounded Context | `Bounded-Context.md` | Domain Modeling | Advanced | Domain-Driven Thinking, Domain Model | Medium | Approved |
| Ubiquitous Language | `Ubiquitous-Language.md` | Domain Modeling | Intermediate | Domain-Driven Thinking | Medium | Approved |
| Event Storming | `Event-Storming.md` | Domain Modeling | Advanced | Business Workflow, Domain Model | Low | Approved |

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
├── Domain Fundamentals / Business Context
├── Business Processes
├── Business Entities → Domain Model
├── Business Rules
├── Industry Domains
└── Regulatory Requirements → Compliance

Domain-Driven Thinking
├── Ubiquitous Language
└── Bounded Context / Domain Model
```

Dependencies are learning guidance, not runtime dependencies.

## Scope Boundaries

Generic QA management → `../qa/`; test-design techniques → `../testing-techniques/`; API behavior → `../api/`; database behavior → `../database/`; canonical concise business terminology → `../../glossary/Business-Terms.md`.

Industry articles provide orientation and risk vocabulary, not authoritative project rules. Regulatory/compliance articles do not determine legal applicability.

## Content-Depth Quality Gate

Approved articles must combine the 12 mandatory sections with semantic depth, realistic QA examples, failure/exception reasoning, explicit assumptions, neighboring-article boundaries, and human/AI retrieval usefulness. Structurally complete one-line skeletons do not pass.

## Quality and Freeze Baseline

```text
Folder: shared/knowledge/domain/
Physical Knowledge Articles: 41
Cataloged Knowledge Articles: 41
Catalog Status: Approved
Baseline State: Frozen
Freeze Date: 2026-08-13
Review Level: Structural + Content Depth + Cross-Article + Cross-Domain + Assumption Safety
```

## Status Definitions

- `Approved` — passed structural and content-depth review and belongs to the active baseline.
- `Deprecated` — retained only for historical compatibility.

`Frozen` is a repository baseline state, not article lifecycle metadata.

## References

- `README.md`
- `../../standards/Knowledge-Article.md`
- `../../standards/Metadata.md`
- `../../standards/Naming.md`
- `../../glossary/Business-Terms.md`