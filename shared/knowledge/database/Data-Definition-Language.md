# Data Definition Language

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
DDL is the SQL area used to create, alter, and remove schema objects.

## Purpose
Support QA review of schema migrations and structural changes.

## Core Concepts
### CREATE
Defines new objects.
### ALTER
Changes existing definitions.
### DROP
Removes objects.

## How It Works
DDL changes database metadata and may affect stored data, dependencies, locks, and transaction behavior depending on the DBMS.

## When to Use
Use for migration review, schema setup, and structural verification.

## When Not to Use
Do not assume DDL transactional behavior is identical across database engines.

## Advantages
DDL provides explicit, automatable schema evolution.

## Limitations
Unsafe changes can cause data loss, blocking, or compatibility failures.

## Examples
Adding a non-null column to a populated table requires a valid migration strategy for existing rows.

## Best Practices
- Review backward compatibility and existing data.
- Test migration on representative volume.
- Verify rollback/recovery strategy.
- Check dependent objects.

## Related Knowledge
- `Database-Objects.md`
- `Data-Migration-Testing.md`
- `Constraints.md`

## References
- ISO/IEC 9075, SQL.
- Target DBMS DDL documentation.