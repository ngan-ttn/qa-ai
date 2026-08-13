# Indexes

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

An **index** is an auxiliary database structure that helps the DBMS locate rows more efficiently for selected access patterns. Indexes are commonly built over one or more columns and may also support uniqueness, ordering, or specialized lookup behavior.

## Purpose

This article helps QA understand why logically correct queries can perform differently, how indexes affect read/write behavior, and how schema changes can introduce performance or uniqueness regressions.

## Core Concepts

### Index Key
The indexed columns or expressions used to organize lookup entries.

### Composite Index
An index can contain multiple columns. Column order often matters for which predicates or sort patterns can use it effectively.

### Unique Index
A unique index can enforce uniqueness, though exact null semantics and relationship to constraints are DBMS-specific.

### Covering Access
A query may be satisfied from index data without reading full table rows when required columns are available through the index.

### Selectivity
Highly selective predicates often benefit more from index access than predicates matching a large portion of the table.

### Maintenance Cost
Every insert, update, or delete may require index maintenance, so excessive or poorly chosen indexes can increase write cost and storage use.

## How It Works

A simplified lookup is:

```text
Query predicate
      ↓
Optimizer considers indexes
      ↓
Index seek/scan or table scan
      ↓
Fetch qualifying rows
```

The optimizer may ignore an available index if statistics, selectivity, function use, type conversion, or cost estimates favor another plan.

## When to Use

Use index knowledge during query-performance investigation, uniqueness validation, schema review, regression analysis, batch/migration planning, and workload changes.

## When Not to Use

Do not assume “add an index” is the correct fix for every slow query. Do not infer index usage solely from index existence; inspect the execution plan or platform evidence.

## Advantages

Indexes can reduce data scanned, accelerate joins and lookups, support ordered access, and enforce selected uniqueness rules.

## Limitations

Indexes consume storage and write resources, can become fragmented or stale depending on the engine, and may not help low-selectivity or transformed predicates. Index behavior is product-specific.

## Examples

### Lookup Index
A query frequently retrieves an order by `order_id`. An appropriate index can avoid scanning the entire table.

### Composite Index
An index on `(tenant_id, created_at)` may support tenant-scoped date queries better than one on `created_at` alone, depending on workload and optimizer behavior.

### Write Regression
Adding several indexes improves reporting reads but increases bulk-import time because each inserted row updates more structures.

## Best Practices

- Start from measured query patterns and execution plans.
- Consider read benefit together with write/storage cost.
- Validate uniqueness behavior when an index enforces business-critical uniqueness.
- Review composite-key order against real predicates and sorting.
- Re-test representative workloads after index changes.
- Avoid production index experiments without operational approval.

## Related Knowledge

- `Query-Optimization.md`
- `Execution-Plans.md`
- `Performance-Monitoring.md`
- `Constraints.md`
- `Data-Query-Language.md`

## References

- Database indexing literature.
- Target DBMS index and optimizer documentation.