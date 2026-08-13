# Rows

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **row** represents one tuple of values under a table's column definition. Rows are the unit most often inspected during database validation, but their identity and meaning depend on keys, relationships, history strategy, and schema design.

## Purpose

This article helps QA reason correctly about record identity, duplicate detection, before/after state, soft deletion, versioning, and row-count expectations.

## Core Concepts

### Row Identity
A row should be identified by a key or documented uniqueness rule, not by physical position.

### Current vs Historical Row
Some schemas update one row in place; others append versions or events. Multiple rows can represent one business entity over time.

### Soft Delete
A logical delete may change a flag or status while retaining the physical row.

### Duplicate
Two rows are not necessarily duplicates just because visible fields match. The business uniqueness definition determines whether duplication exists.

### Row Visibility
Transactions and isolation levels can affect which rows a session can observe at a given moment.

## How It Works

Rows are inserted, updated, read, or deleted within database operations and transactions. Constraints validate each resulting row and its relationships. Queries then select rows based on predicates, joins, grouping, and visibility rules.

## When to Use

Use row-level reasoning for CRUD validation, duplicate analysis, reconciliation, migrations, concurrency checks, pagination verification, and audit/history testing.

## When Not to Use

Do not rely on natural display order. Do not equate total physical rows with active entities when history, soft delete, or partitioned/archive data exists.

## Advantages

Row-level comparison makes persistence defects tangible and supports precise before/after validation.

## Limitations

A business result may depend on aggregates, related tables, views, or derived state rather than one row. Direct row inspection can also miss asynchronous changes.

## Examples

### Update Verification
Capture the target row before an edit, execute the application action, then compare only fields expected to change and verify immutable fields remain stable.

### Soft Delete
Deleting a user may set `is_deleted = true` instead of removing the row. The correct expectation comes from project behavior, not the generic word “delete.”

### Duplicate Analysis
Two transactions create rows with the same email. Whether this is invalid depends on the authoritative uniqueness rule and any database constraint.

## Best Practices

- Identify rows through stable keys.
- Compare before/after values rather than visual assumptions.
- Account for history and soft-delete strategies.
- Use deterministic filters and ordering in evidence queries.
- Avoid exposing sensitive row data unnecessarily.
- Check affected-row count when validating scoped updates or deletes.

## Related Knowledge

- `Tables.md`
- `Primary-Keys.md`
- `Constraints.md`
- `Transactions.md`
- `CRUD-Verification.md`

## References

- Relational model literature.
- ISO/IEC 9075, SQL row and query concepts.