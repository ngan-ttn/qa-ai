# Domain Knowledge Catalog

## Purpose

This catalog is the authoritative inventory and knowledge architecture for `shared/knowledge/domain/`. It organizes reusable business-domain knowledge for QA and QA-AI while keeping project-specific policy, legal interpretation, clinical decisions, organization data, thresholds, calculations, permissions, and implementation details outside the generic knowledge layer.

---

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

---

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
| Rule Exceptions | Business Rules | Intermediate | Business Rule Fundamentals | Medium | Approved |
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

---

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

---

## Dependency Guidance

```text
Business Domain
├── Domain Terminology / Domain Knowledge
├── Business Context
│   ├── Business Processes
│   └── Business Rules
├── Business Entity
│   ├── Entity Relationships / Lifecycle / data types
│   └── Domain Model
├── Industry Domains
└── Regulatory Requirements → Compliance

Domain-Driven Thinking
├── Ubiquitous Language
├── Bounded Context
└── Domain Model → Business Capabilities / Event Storming
```

Dependencies are learning guidance, not mandatory runtime dependencies.

---

## Scope Boundaries

The catalog owns generic business-domain concepts and industry orientation. It does not own project-specific business rules, legal conclusions, clinical decisions, security certification, accounting policy, organization-specific operating policy, or technology implementation.

Cross-domain boundaries:

- generic QA management → `../qa/`
- testing techniques → `../testing-techniques/`
- API behavior → `../api/`
- database behavior → `../database/`
- canonical business terms → `../../glossary/Business-Terms.md`

Industry articles provide **orientation and risk vocabulary**, not authoritative project requirements. Regulatory/compliance articles explain QA reasoning boundaries and require authorized interpretation for legal applicability.

---

## Content-Depth Quality Gate

Every approved article must satisfy both the 12 mandatory structural sections and semantic quality criteria:

1. concept definition and business scope are clear;
2. `Core Concepts` covers the dimensions needed for QA reasoning;
3. `How It Works` explains behavior, lifecycle, or decision flow rather than repeating the definition;
4. examples demonstrate realistic reasoning and important edge/failure conditions;
5. limitations expose ambiguity, stale data, external dependency, or model-boundary risks where relevant;
6. best practices are actionable for QA but do not duplicate detailed test-case templates;
7. project-specific thresholds, rules, legal interpretations, and specialized professional judgments are not invented;
8. neighboring articles have distinct responsibilities and use cross-references instead of unnecessary duplication;
9. industry/compliance knowledge is phrased safely enough for reuse across organizations and jurisdictions;
10. the article is useful to human QA readers and AI retrieval/reasoning.

An article with all required headings but shallow one-line content does **not** pass this gate.

---

## Review Coverage

The final cross-review specifically checked:

- business domain vs technical implementation boundary;
- terminology and bounded-context consistency;
- workflow state, lifecycle, retry, exception, and concurrency reasoning;
- entity identity, ownership, source-of-truth, relationship, and lifecycle reasoning;
- business-rule scope, precedence, effective dates, defaults, and exceptions;
- calculation precision and no invented formulas;
- industry articles for unsupported product/market assumptions;
- regulatory/compliance articles for legal-advice boundary and evidence-based testing;
- privacy for data-flow, masking, copies, deletion propagation, and test-data risks;
- domain modeling for behavior/invariants rather than noun-only models;
- repository-relative cross-references and QA-AI retrieval usefulness.

---

## Quality and Freeze Baseline

```text
Folder: shared/knowledge/domain/
Physical Knowledge Articles: 41
Cataloged Knowledge Articles: 41
Catalog Status: Approved
Baseline State: Frozen
Freeze Date: 2026-08-13
Review Level: Structural + Content Depth + Cross-Article + Assumption Safety
```

All 41 articles passed the final deep review after the baseline was reopened to fix shallow-content issues found during pre-merge validation.

---

## Status Definitions

- `Approved` — article passed structural and content-depth review and belongs to the current baseline.
- `Deprecated` — retained only when historical compatibility requires it.

`Frozen` is a repository baseline state, not an article metadata status.

---

## References

- `README.md`
- `../../standards/Knowledge-Article.md`
- `../../standards/Metadata.md`
- `../../standards/Naming.md`
- `../../glossary/Business-Terms.md`
