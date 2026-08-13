# Data Manipulation Language

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Data Manipulation Language (DML)** commonly refers to SQL statements that change stored relational data, especially `INSERT`, `UPDATE`, `DELETE`, and product-specific merge/upsert operations.

## Purpose

This article helps QA reason about mutation scope, affected rows, constraints, side effects, transactions, and safe database setup/verification.

## Core Concepts

### INSERT
Creates new rows using supplied, defaulted, or generated values.

### UPDATE
Changes columns on rows matching a predicate. An incomplete predicate can affect far more rows than intended.

### DELETE
Removes matching rows physically; application-level “delete” may instead use soft-delete updates.

### MERGE / UPSERT
Some dialects combine insert/update behavior. Concurrency and matching semantics differ across products.

### Affected Rows
A statement's reported affected-row count can help validate scope but product behavior should be confirmed.

### Transaction Scope
DML changes may remain uncommitted, become visible under isolation rules, or be rolled back.

## How It Works

The DBMS resolves the target rows, validates permissions, applies expressions, checks constraints, runs applicable triggers, maintains indexes, and records changes within a transaction.

```text
Predicate / values
      ↓
Target rows
      ↓
Constraint + trigger processing
      ↓
Index/storage changes
      ↓
Commit or rollback
```

## When to Use

Use DML knowledge for CRUD verification, controlled test-data setup, migration, defect reproduction, transaction testing, and side-effect analysis.

## When Not to Use

Do not mutate shared or production data without explicit authorization. Do not bypass application behavior when the test objective is to validate that application path.

## Advantages

DML gives precise control over persistent state and exposes mutation semantics directly.

## Limitations

Direct DML can bypass application validation, audit, authorization, events, or downstream integrations. A successful SQL statement does not prove the full business workflow succeeded.

## Examples

### Scoped Update
Before updating one test record, QA selects the target key, executes the controlled statement in a test environment, then confirms exactly one intended row changed.

### Missing Predicate
`DELETE FROM test_data` without a `WHERE` clause removes the entire table population. This illustrates why mutation safety is a quality requirement for test tooling.

### Trigger Side Effect
An `UPDATE` statement modifies one row but a trigger inserts an audit row. Both effects may need verification.

## Best Practices

- Prefer application/API setup when testing application behavior.
- Use transactions for reversible setup where supported and appropriate.
- Verify predicates with a `SELECT` before executing broad mutations.
- Check affected-row count and before/after state.
- Use dedicated test data and least privilege.
- Account for triggers, cascades, generated values, and asynchronous consumers.
- Never include real secrets or sensitive production values in shared scripts.

## Related Knowledge

- `SQL-Overview.md`
- `Transactions.md`
- `Commit-and-Rollback.md`
- `Constraints.md`
- `CRUD-Verification.md`
- `Trigger-Testing.md`

## References

- ISO/IEC 9075, SQL data manipulation.
- Target DBMS DML documentation.