# Data Manipulation Language

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
DML changes relational data, commonly through `INSERT`, `UPDATE`, `DELETE`, and related DBMS-supported statements.

## Purpose
Explain write operations used in application persistence and QA data preparation.

## Core Concepts
### Insert
Creates rows.
### Update
Changes selected rows.
### Delete
Removes selected rows.
### Affected Scope
Predicates determine which rows are changed.

## How It Works
DML is validated against schema and constraints and normally participates in transaction semantics.

## When to Use
Use for CRUD validation, controlled test-data setup, and transaction testing.

## When Not to Use
Do not execute broad writes in shared environments without safeguards.

## Advantages
DML gives direct control over relational test data.

## Limitations
Direct writes may bypass application rules, audit paths, or integrations.

## Examples
An `UPDATE` without the intended `WHERE` predicate can modify many rows, illustrating why scope validation matters.

## Best Practices
- Prefer application/API setup when side effects matter.
- Preview target rows before destructive changes.
- Use transactions for reversible setup when appropriate.
- Verify affected-row count.

## Related Knowledge
- `Transactions.md`
- `CRUD-Verification.md`
- `Data-Validation.md`

## References
- ISO/IEC 9075, SQL.