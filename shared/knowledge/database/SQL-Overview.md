# SQL Overview

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**SQL (Structured Query Language)** is the standard language family used to define, query, modify, and control relational database data and objects. SQL is declarative: callers describe the desired result or state change while the DBMS determines an execution strategy.

## Purpose

This article gives QA a safe, vendor-independent foundation for reading SQL, validating persisted data, constructing targeted verification queries, and recognizing where dialect-specific behavior must be confirmed.

## Core Concepts

### Declarative Processing
SQL describes what data should be returned or changed rather than prescribing low-level iteration.

### Statement Categories
SQL is often discussed as DDL for schema definition, DML for data modification, DQL for querying, and transaction/control statements. These labels are useful teaching categories but exact classification varies by source and product.

### Set and Multiset Semantics
Queries operate over collections of rows. Duplicates can exist unless constrained or removed explicitly. Ordering is not guaranteed without `ORDER BY`.

### Three-Valued Logic
Predicates involving `NULL` can evaluate to true, false, or unknown. This affects filters, joins, checks, and test expectations.

### SQL Dialects
DBMSs differ in syntax, types, functions, pagination, upsert behavior, transaction semantics, and identifier rules.

### Query Safety
A read-only verification query and a mutating statement have very different risk. QA should use the least-privilege, least-destructive operation needed for the test.

## How It Works

A simplified query lifecycle is:

```text
SQL text
   ↓
Parse and validate
   ↓
Resolve objects and permissions
   ↓
Optimize
   ↓
Execute against visible data
   ↓
Return rows / affected-row result
```

For mutations, transaction handling and constraint checks determine whether changes become committed state.

## When to Use

Use SQL for direct data validation, reconciliation, migration checks, defect analysis, relationship verification, duplicate detection, aggregates, and targeted setup in authorized test environments.

## When Not to Use

Do not use raw SQL to bypass the application when the test objective is to validate application behavior. Do not run destructive or broad statements in shared/production environments without explicit authorization and safeguards.

## Advantages

SQL provides precise access to persisted state, expressive filtering and aggregation, and a common language for relational verification.

## Limitations

SQL results can mislead when joins multiply rows, replicas lag, isolation hides changes, null semantics are misunderstood, or business logic exists outside the database. Dialect differences also limit portability.

## Examples

### Targeted Verification
`SELECT status FROM orders WHERE order_id = ?` validates one persisted status using a stable key.

### Duplicate Detection
`GROUP BY` with `HAVING COUNT(*) > 1` can detect duplicate key candidates, provided the grouping columns reflect the real uniqueness rule.

### Unsafe Assumption
A query returns rows in insertion order during several runs. Without `ORDER BY`, QA should not encode that incidental order as a requirement.

## Best Practices

- Prefer explicit column lists over `SELECT *` in reusable validation queries.
- Filter by stable keys and limit result populations when possible.
- Use deterministic ordering when evidence depends on sequence.
- Understand `NULL` semantics before writing predicates.
- Check join cardinality before trusting aggregates.
- Parameterize inputs in tooling rather than building unsafe SQL strings.
- Separate read-only validation credentials from mutation privileges.
- Confirm dialect-specific syntax against target DBMS documentation.

## Related Knowledge

- `Data-Definition-Language.md`
- `Data-Manipulation-Language.md`
- `Data-Query-Language.md`
- `Joins.md`
- `Aggregation.md`
- `Transactions.md`
- `Data-Validation.md`

## References

- ISO/IEC 9075, Database Languages — SQL.
- Target DBMS SQL reference.