# Domain Knowledge

## Purpose

The `shared/knowledge/domain/` module provides reusable, implementation-independent knowledge about business domains, processes, entities, rules, industry context, regulatory/compliance concepts, and domain modeling for human QA work and QA-AI reasoning.

The module helps requirement analysis, business-rule extraction, risk analysis, scenario generation, test-case generation, regression analysis, test-data reasoning, and defect investigation without embedding project-specific policy or confidential business data.

---

## Scope

The domain knowledge baseline contains seven areas:

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

This folder owns generic business/domain reasoning. It does **not** define project-specific thresholds, formulas, permissions, legal conclusions, clinical decisions, organization policy, implementation architecture, or current regulatory interpretation.

Cross-domain ownership:

- generic QA management → `../qa/`
- testing techniques → `../testing-techniques/`
- API behavior → `../api/`
- database behavior → `../database/`
- concise canonical terminology → `../../glossary/Business-Terms.md`

---

## Module Structure

The folder contains **41 approved knowledge articles**, excluding `README.md` and `Catalog.md`.

### Domain Fundamentals — 5
`Business-Domain.md`, `Domain-Terminology.md`, `Domain-Knowledge.md`, `Business-Context.md`, `Domain-Driven-Thinking.md`

### Business Processes — 6
`Business-Process-Fundamentals.md`, `Business-Workflow.md`, `Process-States.md`, `Process-Lifecycle.md`, `Process-Exceptions.md`, `Business-Events.md`

### Business Entities — 6
`Business-Entity.md`, `Entity-Relationships.md`, `Entity-Lifecycle.md`, `Master-Data.md`, `Transaction-Data.md`, `Reference-Data.md`

### Business Rules — 6
`Business-Rule-Fundamentals.md`, `Validation-Rules.md`, `Decision-Rules.md`, `Calculation-Rules.md`, `Eligibility-Rules.md`, `Rule-Exceptions.md`

### Industry Domains — 7
`Banking.md`, `Healthcare.md`, `Retail.md`, `E-Commerce.md`, `Logistics.md`, `Manufacturing.md`, `Government.md`

### Regulatory & Compliance — 6
`Regulatory-Requirements.md`, `Compliance.md`, `Audit-Trail.md`, `Data-Privacy.md`, `Security-Compliance.md`, `Data-Retention.md`

### Domain Modeling — 5
`Domain-Model.md`, `Business-Capabilities.md`, `Bounded-Context.md`, `Ubiquitous-Language.md`, `Event-Storming.md`

---

## Standard Article Structure

Every article follows `../../standards/Knowledge-Article.md` and contains the 12 mandatory sections:

1. `Overview`
2. `Purpose`
3. `Core Concepts`
4. `How It Works`
5. `When to Use`
6. `When Not to Use`
7. `Advantages`
8. `Limitations`
9. `Examples`
10. `Best Practices`
11. `Related Knowledge`
12. `References`

Structural completeness alone is not sufficient for approval.

---

## Content-Depth Gate

A Domain article can be `Approved` only when it also satisfies all of the following:

- explains the concept deeply enough to support QA reasoning, not only definition recall;
- identifies scope, ownership, state/lifecycle, timing, or authority when materially relevant;
- includes realistic examples that demonstrate reasoning rather than merely repeat the definition;
- covers meaningful failure, exception, ambiguity, or stale-data modes for the topic;
- states important limitations and unsupported-assumption boundaries;
- separates generic domain patterns from project-specific rules;
- avoids turning industry orientation into legal, clinical, financial-policy, or organization-specific conclusions;
- contains actionable QA implications without becoming a duplicate test-case template;
- uses cross-references instead of duplicating neighboring articles;
- remains useful to both human QA readers and AI retrieval/reasoning.

An article that has all 12 headings but remains skeleton-like fails this gate.

---

## Design Principles

Domain articles must:

- keep one primary responsibility per article;
- start from business meaning rather than technical implementation;
- distinguish confirmed facts, generic patterns, assumptions, and authoritative project policy;
- preserve context when the same term or entity has different meanings;
- identify source-of-truth and ownership questions when relevant;
- treat state, lifecycle, timing, and exception behavior as first-class concerns;
- avoid inventing thresholds, calculations, permissions, retention periods, regulatory obligations, or market rules;
- avoid making legal, medical, accounting, security-certification, or other professional determinations;
- encourage escalation to qualified owners where specialized interpretation is required;
- cross-reference QA/API/database/testing-technique knowledge rather than duplicating it.

---

## QA-AI Usage

This domain supports QA-AI when it needs to:

- identify business concepts, actors, outcomes, states, events, and relationships;
- extract and structure business rules;
- detect ambiguity or missing domain context;
- derive high-risk process, lifecycle, entity, rule, industry, and compliance scenarios;
- reason about cross-system ownership and semantic boundaries;
- assess regression impact beyond one technical component;
- distinguish generic domain expectations from project-specific evidence.

QA-AI must never silently convert generic industry knowledge into a project requirement. When evidence is missing, it should surface an assumption or clarification question.

---

## Relationships

- `../qa/` — QA lifecycle, risk, regression, defect, and quality concepts.
- `../testing-techniques/` — systematic scenario/test design methods.
- `../api/` — API contracts, security, retries, idempotency, and event delivery.
- `../database/` — persistence, data integrity, SQL, transactions, and database validation.
- `../../glossary/Business-Terms.md` — concise terminology.
- `../../../skills/` and `../../../workflows/` — consumers of reusable domain knowledge.

---

## Maintenance and Freeze Policy

`Catalog.md` is the source of truth for the approved Domain knowledge baseline. The current baseline is frozen only after physical-file mapping, structural validation, content-depth review, cross-article review, and assumption-safety review all pass.

A frozen article may be changed when a material error, domain-model correction, standard change, cross-domain correction, or approved knowledge expansion requires it. Any change must preserve Catalog ↔ physical-file consistency and trigger appropriate cross-review.

---

## References

- `Catalog.md`
- `../../standards/Knowledge-Article.md`
- `../../standards/Metadata.md`
- `../../standards/Naming.md`
- `../../glossary/Business-Terms.md`
