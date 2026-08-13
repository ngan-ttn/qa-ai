# Database Catalog

## Purpose

This catalog is the authoritative inventory and knowledge architecture for `shared/knowledge/database/`. It organizes reusable database knowledge for QA and QA-AI while keeping project-specific schemas, products, credentials, thresholds, and business data outside the generic knowledge layer.

## Knowledge Architecture

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

## Article Catalog

| Article | File | Category | Level | Prerequisites | Priority | Status |
|---|---|---|---|---|---|---|
| Database Fundamentals | `Database-Fundamentals.md` | Foundations | Foundation | None | High | Approved |
| Relational Database Concepts | `Relational-Database-Concepts.md` | Foundations | Foundation | Database Fundamentals | High | Approved |
| Database Architecture | `Database-Architecture.md` | Foundations | Foundation | Database Fundamentals | Medium | Approved |
| Database Objects | `Database-Objects.md` | Foundations | Foundation | Relational Database Concepts | Medium | Approved |
| Database Lifecycle | `Database-Lifecycle.md` | Foundations | Intermediate | Database Fundamentals | Low | Approved |
| Tables | `Tables.md` | Data Modeling | Foundation | Relational Database Concepts | High | Approved |
| Columns | `Columns.md` | Data Modeling | Foundation | Tables | High | Approved |
| Rows | `Rows.md` | Data Modeling | Foundation | Tables | High | Approved |
| Primary Keys | `Primary-Keys.md` | Data Modeling | Foundation | Tables | High | Approved |
| Foreign Keys | `Foreign-Keys.md` | Data Modeling | Foundation | Primary Keys | High | Approved |
| Relationships | `Relationships.md` | Data Modeling | Foundation | Foreign Keys | High | Approved |
| Constraints | `Constraints.md` | Data Modeling | Intermediate | Relationships | High | Approved |
| Normalization | `Normalization.md` | Data Modeling | Intermediate | Relationships | Medium | Approved |
| SQL Overview | `SQL-Overview.md` | SQL Fundamentals | Foundation | Relational Database Concepts | High | Approved |
| Data Definition Language (DDL) | `Data-Definition-Language.md` | SQL Fundamentals | Foundation | SQL Overview | Medium | Approved |
| Data Manipulation Language (DML) | `Data-Manipulation-Language.md` | SQL Fundamentals | Foundation | SQL Overview | High | Approved |
| Data Query Language (DQL) | `Data-Query-Language.md` | SQL Fundamentals | Foundation | SQL Overview | High | Approved |
| Joins | `Joins.md` | SQL Fundamentals | Intermediate | DQL | High | Approved |
| Aggregation | `Aggregation.md` | SQL Fundamentals | Intermediate | DQL | Medium | Approved |
| Views | `Views.md` | SQL Fundamentals | Intermediate | DQL | Medium | Approved |
| Transactions | `Transactions.md` | Data Integrity | Foundation | DML | High | Approved |
| ACID Properties | `ACID-Properties.md` | Data Integrity | Intermediate | Transactions | High | Approved |
| Commit and Rollback | `Commit-and-Rollback.md` | Data Integrity | Foundation | Transactions | High | Approved |
| Isolation Levels | `Isolation-Levels.md` | Data Integrity | Advanced | ACID Properties | Medium | Approved |
| Locking | `Locking.md` | Data Integrity | Advanced | Transactions | Medium | Approved |
| Concurrency Control | `Concurrency-Control.md` | Data Integrity | Advanced | Isolation Levels | Medium | Approved |
| Indexes | `Indexes.md` | Performance | Intermediate | DQL | High | Approved |
| Query Optimization | `Query-Optimization.md` | Performance | Advanced | Indexes | Medium | Approved |
| Execution Plans | `Execution-Plans.md` | Performance | Advanced | Query Optimization | Low | Approved |
| Partitioning | `Partitioning.md` | Performance | Advanced | Database Architecture | Low | Approved |
| Performance Monitoring | `Performance-Monitoring.md` | Performance | Advanced | Query Optimization | Low | Approved |
| Database Test Strategy | `Database-Test-Strategy.md` | Database Testing | Foundation | SQL Overview | High | Approved |
| Data Validation | `Data-Validation.md` | Database Testing | Foundation | Database Test Strategy | High | Approved |
| CRUD Verification | `CRUD-Verification.md` | Database Testing | Foundation | Database Test Strategy | High | Approved |
| Stored Procedure Testing | `Stored-Procedure-Testing.md` | Database Testing | Intermediate | DML | Medium | Approved |
| Trigger Testing | `Trigger-Testing.md` | Database Testing | Intermediate | Stored Procedure Testing | Medium | Approved |
| Data Migration Testing | `Data-Migration-Testing.md` | Database Testing | Advanced | Data Validation | Medium | Approved |
| Backup and Recovery | `Backup-and-Recovery.md` | Advanced Topics | Advanced | Database Architecture | Low | Approved |
| Replication | `Replication.md` | Advanced Topics | Advanced | Database Architecture | Low | Approved |
| Sharding | `Sharding.md` | Advanced Topics | Advanced | Partitioning | Low | Approved |
| Data Warehousing | `Data-Warehousing.md` | Advanced Topics | Advanced | Database Fundamentals | Low | Approved |
| NoSQL Overview | `NoSQL-Overview.md` | Advanced Topics | Intermediate | Database Fundamentals | Low | Approved |

## Category Summary

| Category | Articles | Status |
|---|---:|---|
| Foundations | 5 | Approved |
| Data Modeling | 8 | Approved |
| SQL Fundamentals | 7 | Approved |
| Data Integrity | 6 | Approved |
| Performance | 5 | Approved |
| Database Testing | 6 | Approved |
| Advanced Topics | 5 | Approved |
| **Total** | **42** | **Approved** |

## Dependency Guidance

```text
Database Fundamentals
├── Relational Database Concepts → Data Modeling / SQL
├── Database Architecture → Partitioning / Replication / Recovery
└── Database Test Strategy → Validation / CRUD / Procedure / Trigger / Migration
```

Dependencies are learning guidance, not runtime dependencies.

## Scope Boundaries

Generic QA management belongs in `../qa/`; API behavior in `../api/`; test-design techniques in `../testing-techniques/`; industry-specific business meaning in `../domain/`.

No article may invent project-specific schemas, database products, credentials, isolation settings, replication guarantees, recovery objectives, retention rules, or performance thresholds.

## Quality Gate

Approval requires both the 12-section structure and sufficient semantic depth. Review covers database reasoning models, realistic QA examples, transaction/concurrency semantics, relational-vs-NoSQL boundaries, migration/recovery assumptions, cross-references, and project-specific assumption safety.

## Quality and Freeze Baseline

```text
Folder: shared/knowledge/database/
Physical Knowledge Articles: 42
Cataloged Knowledge Articles: 42
Catalog Status: Approved
Baseline State: Frozen
Freeze Date: 2026-08-13
Review Cycle: Structural + Content Depth + Cross-Article + Cross-Domain
```

## Status Definitions

- `Approved` — article passed review and is part of the active baseline.
- `Deprecated` — retained only for historical compatibility.

`Frozen` is a repository baseline state, not article lifecycle metadata.

## References

- `README.md`
- `../../standards/Knowledge-Article.md`
- `../../standards/Metadata.md`
- `../../standards/Naming.md`
- `../../glossary/Database-Terms.md`