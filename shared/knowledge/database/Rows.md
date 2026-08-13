# Rows

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
A row is one tuple or record in a relational table, containing values for the table's columns.

## Purpose
Clarify record-level reasoning for CRUD and data validation.

## Core Concepts
### Record State
A row represents stored state at a point in time.
### Identity
Primary or candidate keys distinguish logical records.
### Visibility
Transactions and isolation determine when changes become visible.

## How It Works
DML creates, changes, and removes rows; queries select rows according to predicates and transaction visibility.

## When to Use
Use for persistence verification, duplicate analysis, migration reconciliation, and state-transition checks.

## When Not to Use
Do not assume physical row order or storage location has business meaning.

## Advantages
Rows provide a natural unit for record-level verification.

## Limitations
A business entity may span multiple rows or tables, and one row may contain denormalized data.

## Examples
Updating an order status should change the intended order row without altering unrelated orders.

## Best Practices
- Identify rows by stable keys.
- Verify affected-row scope.
- Consider transaction visibility during concurrent tests.

## Related Knowledge
- `Tables.md`
- `Primary-Keys.md`
- `Transactions.md`
- `CRUD-Verification.md`

## References
- ISO/IEC 9075, SQL.