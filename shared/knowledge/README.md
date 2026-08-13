# Knowledge

## Purpose

The `shared/knowledge/` module is the reusable conceptual knowledge layer for QA-AI. It provides the methods, quality concepts, technology knowledge, and business-domain context consumed by skills and workflows without duplicating project-specific requirements or repository execution rules.

## Scope

The approved knowledge architecture contains five domains:

```text
shared/knowledge/
├── testing-techniques/   30 articles
├── qa/                   28 articles
├── api/                  40 articles
├── database/             42 articles
└── domain/               41 articles
                         ───────────
Total                    181 articles
```

`README.md` and `Catalog.md` files are navigation/governance artifacts and are excluded from article counts.

## Cross-Domain Ownership

| Domain | Owns | Does Not Own |
|---|---|---|
| `testing-techniques/` | test derivation and test-design techniques | generic QA management, API/DB/domain behavior |
| `qa/` | QA lifecycle, requirement engineering, test management, defects, generic quality practices | detailed design techniques or technology/domain-specific behavior |
| `api/` | API architecture, communication, security, error handling and API-specific testing | generic QA management, SQL, business policy |
| `database/` | relational/SQL/data-integrity/performance/database-testing concepts | API contracts, generic QA process, industry policy |
| `domain/` | business concepts, entities, processes, rules, industry and compliance orientation | technical implementation and generic QA process |

When a subject crosses boundaries, the owning domain explains the primary concept and neighboring domains reference it rather than copy it.

## Source of Truth

Each domain contains a `Catalog.md` that is authoritative for:

- article inventory and physical mapping;
- category classification;
- conceptual prerequisites;
- priority;
- lifecycle status;
- current freeze baseline.

The physical repository, Catalog, and README must remain consistent.

## Knowledge Article Standard

Every approved Knowledge Article follows `../standards/Knowledge-Article.md`.

Mandatory hierarchy:

```text
# Article Title
## Overview
## Purpose
## Core Concepts
## How It Works
## When to Use
## When Not to Use
## Advantages
## Limitations
## Examples
## Best Practices
## Related Knowledge
## References
```

The 12-section structure is only the structural gate. Approval also requires semantic depth, accurate boundaries, practical examples, assumption safety, and cross-reference quality.

## Domain Baselines

| Domain | Articles | Catalog Status | Baseline |
|---|---:|---|---|
| Testing Techniques | 30 | Approved | Frozen |
| QA | 28 | Approved | Frozen |
| API | 40 | Approved | Frozen |
| Database | 42 | Approved | Frozen |
| Domain | 41 | Approved | Frozen |
| **Total** | **181** | **Approved** | **Frozen** |

## Knowledge Relationships

```text
Requirements / Project Context
            ↓
        Domain Knowledge
            ↓
QA concepts ─┼─ Testing Techniques
            │
            ├─ API Knowledge
            └─ Database Knowledge
            ↓
      Skills and Workflows
            ↓
       QA Artifacts
```

This diagram is conceptual, not a fixed runtime loading order. Skills should retrieve only the knowledge relevant to their objective.

## Authoritative Input Rule

Generic repository knowledge provides reusable reasoning. It does not override authoritative project inputs.

Project-specific requirements, approved business rules, contracts, policies, schemas, roles, thresholds, formulas, and jurisdiction-specific obligations remain authoritative for the actual feature being tested.

When information is missing, QA-AI should surface a clarification or explicit assumption rather than silently manufacture expected behavior.

## Relationships with Other Shared Modules

- `../standards/` defines repository and article rules.
- `../templates/` defines artifact structures.
- `../checklists/` defines review controls.
- `../prompt-patterns/` defines reusable reasoning/prompt patterns.
- `../glossary/` provides concise canonical terminology.
- `../../skills/` consume knowledge for single capabilities.
- `../../workflows/` orchestrate capabilities and knowledge across steps.

Knowledge explains concepts; it should not duplicate the responsibilities of those modules.

## Cross-Domain Quality Gate

The root knowledge baseline is Frozen only when:

- all five domain Catalog counts match physical articles;
- all baseline articles are Approved;
- every domain follows the current Knowledge Article Standard;
- root/domain README and Catalog information is consistent;
- no unresolved ownership conflict or duplicate primary responsibility remains;
- cross-domain references use real paths;
- project-specific and high-stakes assumptions are bounded;
- testing/technology/domain specialization is separated from generic QA concepts.

## Maintenance Policy

A frozen baseline can change when corrections or intentional extensions are needed.

Material changes require:

1. targeted self-review of changed articles;
2. cross-reference impact review;
3. Catalog/README reconciliation when architecture changes;
4. cross-domain review when ownership, shared terminology, or prerequisites change;
5. re-freeze only after blockers are resolved.

## Root Freeze Baseline

```text
Folder: shared/knowledge/
Knowledge Domains: 5
Approved Knowledge Articles: 181
Domain Catalogs: 5
Cross-Domain Review: PASS
Baseline State: Frozen
Freeze Date: 2026-08-13
```

## References

- `../standards/Knowledge-Article.md`
- `testing-techniques/Catalog.md`
- `qa/Catalog.md`
- `api/Catalog.md`
- `database/Catalog.md`
- `domain/Catalog.md`
- `../glossary/`
- `../../skills/`
- `../../workflows/`