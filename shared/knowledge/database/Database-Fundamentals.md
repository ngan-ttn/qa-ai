# Database Fundamentals

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
A database is an organized data store managed so applications can create, retrieve, update, protect, and preserve information reliably.

## Purpose
Provide QA-AI with the baseline vocabulary for reasoning about persistent data, database behavior, and validation boundaries.

## Core Concepts
### Database Management System
A DBMS manages storage, access, integrity, concurrency, recovery, and administration.
### Schema and Data
A schema defines structure; data is the stored state that conforms to that structure.
### Persistence
Persistent data survives beyond an individual process or request.

## How It Works
Applications issue operations through a database interface. The DBMS validates them, executes reads or writes, coordinates concurrent work, and persists committed changes.

## When to Use
Use this knowledge when requirements involve stored state, backend verification, SQL, migration, transactions, or data defects.

## When Not to Use
Do not infer a project's schema, engine, retention policy, or consistency guarantees from this generic model.

## Advantages
Databases provide structured persistence, controlled access, integrity mechanisms, query capability, and recovery support.

## Limitations
Database correctness does not by itself prove business correctness; application logic, integrations, caches, and asynchronous processing may affect observable state.

## Examples
A QA engineer verifies that creating an order produces the expected persistent record and that rejected creation leaves no unintended data.

## Best Practices
- Treat project schema and data contracts as authoritative.
- Verify both stored values and business-visible outcomes.
- Use controlled test data and least-privilege access.
- Avoid destructive validation in shared environments.

## Related Knowledge
- `Relational-Database-Concepts.md`
- `Database-Architecture.md`
- `Database-Test-Strategy.md`
- `Data-Validation.md`

## References
- ISO/IEC 9075, SQL.
- Vendor documentation for the database under test.