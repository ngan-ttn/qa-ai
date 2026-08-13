# Database Test Strategy

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
Database test strategy defines how data correctness, integrity, transactions, database logic, migrations, and relevant non-functional risks are validated.

## Purpose
Provide reusable QA guidance for selecting database coverage based on risk and architecture.

## Core Concepts
### Test Layers
Validation may occur through application/API behavior, direct database queries, migrations, and database-side objects.
### Risk Areas
Integrity, concurrency, security, migration, recovery, and performance require different evidence.
### Test Data
Known preconditions and cleanup are essential for reliable results.

## How It Works
QA maps requirements and risks to observable database outcomes, chooses safe validation methods, prepares data, executes tests, and reconciles expected state.

## When to Use
Use when a feature persists data, changes schema, migrates data, or depends on database-side behavior.

## When Not to Use
Do not require direct database access when external behavior provides sufficient evidence or policy forbids it.

## Advantages
A strategy prevents ad hoc SQL checks and improves risk coverage.

## Limitations
Direct database testing can couple tests to implementation details and requires controlled access.

## Examples
A migration strategy may include schema checks, row counts, key reconciliation, transformation validation, rollback/recovery, and performance sampling.

## Best Practices
- Start from business risk and data contract.
- Separate setup SQL from verification SQL.
- Use least privilege and masked/non-sensitive data.
- Include negative and concurrency cases where relevant.
- Keep evidence reproducible.

## Related Knowledge
- `Data-Validation.md`
- `CRUD-Verification.md`
- `Data-Migration-Testing.md`
- `../qa/Test-Strategy.md`

## References
- `../../standards/Knowledge-Article.md`.
- Target DBMS testing and operational documentation.