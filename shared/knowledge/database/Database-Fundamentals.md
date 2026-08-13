# Database Fundamentals

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **database** is an organized system for storing, retrieving, updating, and protecting data. A database management system (DBMS) provides the mechanisms that applications and users use to define data structures, query data, enforce integrity, coordinate concurrent access, recover from failures, and control permissions.

For QA, the database is often the persistence layer behind application behavior. Understanding this layer helps distinguish UI/API defects from data defects, verify state changes directly, analyze integration failures, and design tests for consistency, concurrency, migration, recovery, and performance.

## Purpose

This article establishes the conceptual foundation used by every other article in `shared/knowledge/database/`. It gives QA and QA-AI a vendor-independent model for reasoning about stored data without assuming a specific schema, product, deployment topology, or business rule.

## Core Concepts

### Data and Persistence

Data represents facts, states, events, or relationships. Persistence means that information survives beyond the lifetime of a single process or request according to the storage system's guarantees.

### Database Management System

A DBMS manages storage, query processing, transactions, permissions, metadata, concurrency, and recovery. Relational systems commonly use SQL, while other database families expose different models and query mechanisms.

### Schema

A schema describes how data is organized. In relational systems it commonly includes tables, columns, keys, constraints, views, indexes, and programmable objects. Schema design is an implementation of business information needs; it is not itself the business specification.

### Query and Mutation

A query reads data. A mutation changes stored state through inserts, updates, deletes, procedures, or equivalent operations. Application actions can generate multiple database operations within one business flow.

### Integrity

Integrity is the preservation of valid relationships and allowed values. Some integrity is enforced by the database through types, keys, constraints, and transactions; other rules exist only in application or domain logic.

### Transaction

A transaction groups operations under defined commit, rollback, isolation, and durability semantics. A business process may span multiple transactions or external services, so database transaction scope must not be assumed to equal business workflow scope.

### Logical and Physical Views

The logical model describes entities, attributes, relationships, and constraints. The physical implementation includes storage layout, indexes, partitions, replicas, files, caches, and engine-specific structures.

## How It Works

A simplified interaction is:

```text
Application / Tool
       ↓
Connection + Authentication
       ↓
SQL / Database Operation
       ↓
Parser / Planner / Transaction Manager
       ↓
Storage + Indexes + Logs + Constraints
       ↓
Result / Persisted State
```

The DBMS interprets an operation, checks permissions and constraints, chooses an execution approach, reads or modifies data, coordinates concurrent work, records transactional information, and returns a result. Exact behavior depends on product, configuration, transaction boundaries, and deployment architecture.

For QA, a useful reasoning sequence is:

```text
Expected business behavior
        ↓
Expected persistent state
        ↓
Database objects involved
        ↓
Operation / transaction behavior
        ↓
Observed rows, relationships, side effects
        ↓
Compare against authoritative requirement
```

## When to Use

Use database fundamentals when requirements involve persistence, data validation, CRUD operations, reports, imports, migrations, audit records, reconciliation, concurrency, transactions, recovery, or database-backed integration behavior.

This knowledge is especially useful when UI or API results alone cannot prove whether underlying state was stored correctly.

## When Not to Use

Do not use generic database knowledge to invent table names, production access methods, retention periods, recovery objectives, isolation levels, replication guarantees, performance thresholds, or business rules. Those must come from project documentation, architecture, DBMS configuration, or authorized operational sources.

Do not query production data or execute destructive statements merely because direct database validation would be convenient.

## Advantages

Database-level understanding enables:

- direct validation of persisted state;
- better defect isolation between presentation, service, and storage layers;
- validation of relationships and data integrity;
- stronger migration and reconciliation testing;
- transaction and concurrency analysis;
- performance investigation using query and execution evidence;
- reusable QA reasoning independent of a specific UI.

## Limitations

Database observation alone cannot prove complete business correctness. Data may be eventually updated, denormalized, cached, replicated, encrypted, archived, or generated by asynchronous processes. A row that looks correct can still violate an external business rule, and a temporarily missing row may be expected in an eventually consistent architecture.

Direct queries can also change behavior if they use locks, heavy scans, or unsafe statements. Environment permissions and operational constraints must remain authoritative.

## Examples

### Persistence Verification

A user creates an order through an API. QA verifies the API response and then checks that the order row, child rows, expected identifiers, and required relationships were persisted without unintended duplicates.

### Defect Isolation

A UI displays an outdated status. The database contains the new status, so QA investigates caching, API mapping, or frontend state rather than assuming persistence failed.

### Data Integrity

An application attempts to create a child record referencing a nonexistent parent. QA verifies behavior according to the system contract and, where a foreign key exists, confirms that invalid referential state is not persisted.

## Best Practices

- Start from authoritative business and technical requirements before inspecting implementation.
- Prefer read-only validation unless a test explicitly requires controlled mutation.
- Use stable keys to identify records and compare before/after state.
- Distinguish business validation from database-enforced integrity.
- Confirm transaction and consistency assumptions rather than inferring them.
- Avoid exposing credentials, production data, or sensitive fields in evidence.
- Account for asynchronous processing, replicas, caches, and eventual consistency when applicable.
- Keep queries targeted and safe, especially in shared environments.
- Record timestamps, correlation identifiers, and transaction context when they help defect analysis.

## Related Knowledge

- `Relational-Database-Concepts.md`
- `Database-Architecture.md`
- `Database-Objects.md`
- `SQL-Overview.md`
- `Transactions.md`
- `Database-Test-Strategy.md`
- `../domain/Business-Entity.md`

## References

- ISO/IEC 9075, Database Languages — SQL.
- Database-system architecture and transaction-processing literature.
- Target DBMS documentation for product-specific behavior.

Project-specific schema, access, consistency, and operational rules remain authoritative over generic knowledge.