# Database Knowledge

## Purpose

The `shared/knowledge/database/` module provides reusable, vendor-independent knowledge about relational databases, data modeling, SQL, transactional integrity, database performance, database testing, and selected modern data architectures.

It supports human QA work and QA-AI reasoning during requirement analysis, test generation, SQL validation, regression analysis, migration review, concurrency analysis, and defect investigation.

This module does not define project-specific schemas, credentials, production data, retention policies, recovery objectives, performance thresholds, or database products.

---

## Scope

The Database knowledge domain contains seven areas:

```text
Database
├── Foundations
├── Data Modeling
├── SQL Fundamentals
├── Data Integrity
├── Performance
├── Database Testing
└── Advanced Topics
```

Knowledge owned by other domains remains outside this folder:

- generic QA lifecycle and management → `../qa/`
- API behavior → `../api/`
- test-design techniques → `../testing-techniques/`
- industry-specific data models → `../domain/`

---

## Module Structure

The folder contains **42 approved knowledge articles**, excluding `README.md` and `Catalog.md`.

### Foundations — 5
`Database-Fundamentals.md`, `Relational-Database-Concepts.md`, `Database-Architecture.md`, `Database-Objects.md`, `Database-Lifecycle.md`

### Data Modeling — 8
`Tables.md`, `Columns.md`, `Rows.md`, `Primary-Keys.md`, `Foreign-Keys.md`, `Relationships.md`, `Constraints.md`, `Normalization.md`

### SQL Fundamentals — 7
`SQL-Overview.md`, `Data-Definition-Language.md`, `Data-Manipulation-Language.md`, `Data-Query-Language.md`, `Joins.md`, `Aggregation.md`, `Views.md`

### Data Integrity — 6
`Transactions.md`, `ACID-Properties.md`, `Commit-and-Rollback.md`, `Isolation-Levels.md`, `Locking.md`, `Concurrency-Control.md`

### Performance — 5
`Indexes.md`, `Query-Optimization.md`, `Execution-Plans.md`, `Partitioning.md`, `Performance-Monitoring.md`

### Database Testing — 6
`Database-Test-Strategy.md`, `Data-Validation.md`, `CRUD-Verification.md`, `Stored-Procedure-Testing.md`, `Trigger-Testing.md`, `Data-Migration-Testing.md`

### Advanced Topics — 5
`Backup-and-Recovery.md`, `Replication.md`, `Sharding.md`, `Data-Warehousing.md`, `NoSQL-Overview.md`

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

---

## Design Principles

Database articles must:

- keep one primary responsibility per article;
- remain vendor-independent unless a vendor distinction is necessary for accuracy;
- separate database guarantees from application/business guarantees;
- distinguish logical models from physical implementation;
- avoid inventing schema, transaction, consistency, retention, recovery, or performance requirements;
- treat project documentation and actual DBMS configuration as authoritative;
- protect sensitive data and encourage least-privilege validation;
- cross-reference related articles instead of duplicating them;
- support both human readability and AI retrieval.

---

## QA-AI Usage

This domain supports database-aware requirement analysis, SQL validation, CRUD verification, integrity and relationship checks, transaction/concurrency reasoning, migration reconciliation, performance investigation, and database-focused regression analysis.

QA-AI must not infer production access, destructive-test permission, schema details, or database guarantees from generic knowledge.

---

## Relationships

- `../qa/` — QA strategy, risk, regression, defect and quality concepts.
- `../api/` — API contracts and integration behavior.
- `../testing-techniques/` — systematic test design.
- `../domain/` — business-specific data meaning.
- `../../glossary/Database-Terms.md` — concise terminology.
- `../../../skills/` and `../../../workflows/` — consumers of reusable database knowledge.

---

## Maintenance and Freeze Policy

`Catalog.md` is the source of truth for the approved Database knowledge baseline. The current baseline is frozen after full cross-article review. `Frozen` is a repository baseline state; article lifecycle metadata uses `Approved`.

A frozen article may be changed when a technical error, material standard change, cross-domain correction, or approved architecture expansion requires it. Any change must preserve physical-file ↔ Catalog consistency and trigger appropriate cross-review.

---

## References

- `Catalog.md`
- `../../standards/Knowledge-Article.md`
- `../../standards/Metadata.md`
- `../../standards/Naming.md`