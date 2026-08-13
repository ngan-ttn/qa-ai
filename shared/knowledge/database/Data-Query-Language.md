# Data Query Language

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Data Query Language (DQL)** is a common teaching term for SQL used to retrieve data, primarily through `SELECT` statements. Querying combines projection, filtering, joins, grouping, ordering, subqueries, and expressions to produce a result set.

## Purpose

This article helps QA create reliable verification queries and understand why a syntactically correct query can still produce misleading evidence.

## Core Concepts

### Projection
The `SELECT` list controls which expressions and columns appear in the result.

### Filtering
`WHERE` restricts rows using predicates and SQL three-valued logic.

### Join
Joins combine rows from multiple data sources according to matching conditions.

### Grouping
`GROUP BY` partitions rows for aggregate calculations.

### Ordering
`ORDER BY` defines deterministic output order. Without it, order is not guaranteed.

### Limiting / Pagination
Dialects expose different mechanisms such as `LIMIT`, `OFFSET`, `FETCH`, or window functions.

### Subquery and CTE
Nested queries and common table expressions make complex logic composable and can improve readability.

## How It Works

SQL has a logical processing model in which data sources and joins are resolved, rows are filtered, groups and aggregates are formed, projections are calculated, and final ordering/limiting is applied. The optimizer can execute an equivalent physical plan in a different order.

## When to Use

Use DQL for data validation, relationship checks, duplicate detection, reconciliation, reporting validation, migration comparisons, defect investigation, and test-data discovery.

## When Not to Use

Do not treat one query as authoritative until its joins, filters, null handling, and source freshness are understood. Do not run heavy unbounded queries on sensitive shared systems without approval.

## Advantages

DQL is expressive, non-destructive when used read-only, and supports precise inspection of large relational datasets.

## Limitations

Incorrect joins, missing filters, stale replicas, isolation, timezone conversion, and hidden soft-delete conditions can create false conclusions.

## Examples

### Targeted Record
A query filters by a stable business/test key to verify one persisted record rather than visually scanning a broad result.

### Null Predicate
`column = NULL` does not test for null under standard SQL semantics; `IS NULL` is required.

### Deterministic Latest Record
Selecting a “latest” row requires an explicit ordering criterion. Relying on physical insertion order is unsafe.

## Best Practices

- Select only the columns needed for evidence.
- Use stable, selective predicates.
- Explicitly handle nulls.
- Validate join cardinality before aggregating.
- Add deterministic `ORDER BY` when sequence matters.
- Confirm whether the queried node is primary, replica, warehouse, or cache-backed.
- Use execution plans for expensive queries rather than guessing performance causes.

## Related Knowledge

- `Joins.md`
- `Aggregation.md`
- `Views.md`
- `Indexes.md`
- `Data-Validation.md`

## References

- ISO/IEC 9075, SQL query specification.
- Target DBMS query documentation.