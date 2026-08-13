# Database Catalog

## Purpose

This catalog is the authoritative inventory and knowledge architecture for `shared/knowledge/database/`. It organizes reusable database knowledge for QA and QA-AI while keeping project-specific schemas, products, credentials, thresholds, and business data outside the generic knowledge layer.

---

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

---

## Article Catalog

| Article | Category | Level | Prerequisites | Priority | Status |
|---|---|---|---|---|---|
| Database Fundamentals | Foundations | Foundation | None | High | Approved |
| Relational Database Concepts | Foundations | Foundation | Database Fundamentals | High | Approved |
| Database Architecture | Foundations | Foundation | Database Fundamentals | Medium | Approved |
| Database Objects | Foundations | Foundation | Relational Database Concepts | Medium | Approved |
| Database Lifecycle | Foundations | Intermediate | Database Fundamentals | Low | Approved |
| Tables | Data Modeling | Foundation | Relational Database Concepts | High | Approved |
| Columns | Data Modeling | Foundation | Tables | High | Approved |
| Rows | Data Modeling | Foundation | Tables | High | Approved |
| Primary Keys | Data Modeling | Foundation | Tables | High | Approved |
| Foreign Keys | Data Modeling | Foundation | Primary Keys | High | Approved |
| Relationships | Data Modeling | Foundation | Foreign Keys | High | Approved |
| Constraints | Data Modeling | Intermediate | Relationships | High | Approved |
| Normalization | Data Modeling | Intermediate | Relationships | Medium | Approved |
| SQL Overview | SQL Fundamentals | Foundation | Relational Database Concepts | High | Approved |
| Data Definition Language (DDL) | SQL Fundamentals | Foundation | SQL Overview | Medium | Approved |
| Data Manipulation Language (DML) | SQL Fundamentals | Foundation | SQL Overview | High | Approved |
| Data Query Language (DQL) | SQL Fundamentals | Foundation | SQL Overview | High | Approved |
| Joins | SQL Fundamentals | Intermediate | DQL | High | Approved |
| Aggregation | SQL Fundamentals | Intermediate | DQL | Medium | Approved |
| Views | SQL Fundamentals | Intermediate | DQL | Medium | Approved |
| Transactions | Data Integrity | Foundation | DML | High | Approved |
| ACID Properties | Data Integrity | Intermediate | Transactions | High | Approved |
| Commit and Rollback | Data Integrity | Foundation | Transactions | High | Approved |
| Isolation Levels | Data Integrity | Advanced | ACID Properties | Medium | Approved |
| Locking | Data Integrity | Advanced | Transactions | Medium | Approved |
| Concurrency Control | Data Integrity | Advanced | Isolation Levels | Medium | Approved |
| Indexes | Performance | Intermediate | DQL | High | Approved |
| Query Optimization | Performance | Advanced | Indexes | Medium | Approved |
| Execution Plans | Performance | Advanced | Query Optimization | Low | Approved |
| Partitioning | Performance | Advanced | Database Architecture | Low | Approved |
| Performance Monitoring | Performance | Advanced | Query Optimization | Low | Approved |
| Database Test Strategy | Database Testing | Foundation | SQL Overview | High | Approved |
| Data Validation | Database Testing | Foundation | Database Test Strategy | High | Approved |
| CRUD Verification | Database Testing | Foundation | Database Test Strategy | High | Approved |
| Stored Procedure Testing | Database Testing | Intermediate | DML | Medium | Approved |
| Trigger Testing | Database Testing | Intermediate | Stored Procedure Testing | Medium | Approved |
| Data Migration Testing | Database Testing | Advanced | Data Validation | Medium | Approved |
| Backup and Recovery | Advanced Topics | Advanced | Database Architecture | Low | Approved |
| Replication | Advanced Topics | Advanced | Database Architecture | Low | Approved |
| Sharding | Advanced Topics | Advanced | Partitioning | Low | Approved |
| Data Warehousing | Advanced Topics | Advanced | Database Fundamentals | Low | Approved |
| NoSQL Overview | Advanced Topics | Intermediate | Database Fundamentals | Low | Approved |

---

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

---

## Dependency Guidance

```text
Database Fundamentals
├── Relational Database Concepts
│   ├── Data Modeling
│   └── SQL Overview
│       ├── DDL / DML / DQL
│       ├── Transactions → ACID / Isolation / Locking / Concurrency
│       └── Querying → Joins / Aggregation / Views / Indexes
├── Database Architecture
│   ├── Partitioning → Sharding
│   ├── Replication
│   └── Backup and Recovery
└── Database Test Strategy
    ├── Data Validation
    ├── CRUD Verification
    ├── Stored Procedure / Trigger Testing
    └── Data Migration Testing
```

Dependencies are learning guidance, not mandatory runtime dependencies.

---

## Scope Boundaries

The catalog owns generic database concepts. Generic QA management belongs in `../qa/`; API behavior belongs in `../api/`; test-design techniques belong in `../testing-techniques/`; industry-specific schemas and business entities belong in `../domain/`.

No article may invent project-specific schemas, database products, credentials, isolation settings, replication guarantees, recovery objectives, retention rules, or performance thresholds.

---

## Quality and Freeze Baseline

```text
Folder: shared/knowledge/database/
Physical Knowledge Articles: 42
Cataloged Knowledge Articles: 42
Catalog Status: Approved
Baseline State: Frozen
Freeze Date: 2026-08-13
```

All 42 articles were reviewed for mandatory section structure, terminology, scope boundaries, relational/NoSQL distinction, SQL safety, transaction semantics, concurrency assumptions, cross-references, and QA-AI usability before this baseline was marked frozen.

---

## Status Definitions

- `Approved` — article passed review and is part of the current baseline.
- `Deprecated` — retained only when historical compatibility requires it.

`Frozen` is a repository baseline state, not an article lifecycle metadata status.

---

## References

- `README.md`
- `../../standards/Knowledge-Article.md`
- `../../standards/Metadata.md`
- `../../standards/Naming.md`
- `../../glossary/Database-Terms.md`