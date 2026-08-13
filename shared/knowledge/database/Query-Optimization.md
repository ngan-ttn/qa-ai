# Query Optimization

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Query optimization** is the process by which a DBMS chooses an efficient execution strategy for a declarative query. It considers available access paths, join orders, statistics, estimated cardinalities, memory, indexes, and implementation-specific cost models.

## Purpose

This article helps QA investigate database performance using evidence rather than guessing from SQL text alone, and distinguish logical query correctness from physical execution efficiency.

## Core Concepts

### Cost-Based Optimization
Most modern relational engines estimate the relative cost of candidate plans and choose one considered efficient under current statistics and configuration.

### Cardinality Estimation
The optimizer predicts how many rows each operation will produce. Poor estimates can lead to inefficient join strategies or access paths.

### Statistics
Distribution and row-count statistics help estimate selectivity. Stale or insufficient statistics can degrade plan quality.

### Sargability
Predicates structured so indexes can be used effectively are often called sargable. Functions, casts, or expressions can prevent efficient access in some products.

### Join Order and Algorithm
The optimizer can reorder joins and choose nested-loop, hash, merge, or other methods.

### Parameter Sensitivity
A plan that works well for one parameter distribution may perform poorly for another. Product behavior varies.

## How It Works

```text
SQL
 ↓
Parse / normalize
 ↓
Estimate row counts and costs
 ↓
Explore access paths / joins
 ↓
Choose execution plan
 ↓
Execute and collect runtime evidence
```

A query can be logically identical while obtaining different plans after data growth, statistics changes, index changes, or software upgrades.

## When to Use

Use query-optimization knowledge for slow endpoints, report regressions, timeout analysis, bulk operations, data-growth testing, index review, and release performance comparison.

## When Not to Use

Do not rewrite queries or add hints before establishing a reproducible performance problem and reviewing the actual execution plan. Do not assume the lowest estimated cost always predicts production behavior perfectly.

## Advantages

Optimization allows declarative SQL to adapt to data shape and available structures without hardcoding physical algorithms in application code.

## Limitations

Cost models are estimates. Skewed data, stale statistics, runtime memory pressure, concurrency, caching, and parameter distributions can invalidate estimates.

## Examples

### Stale Statistics
A table grows from thousands to millions of rows, but statistics remain outdated. The optimizer chooses a plan based on an old cardinality estimate, causing a regression.

### Non-Sargable Predicate
A filter transforms an indexed column inside a function. The engine may scan instead of seeking, depending on available expression indexes and optimizer capabilities.

### Parameter Sensitivity
A query is fast for a selective customer but slow for one owning most records because the reused plan is not suitable for both populations.

## Best Practices

- Reproduce performance with representative data and parameters.
- Capture estimated and, where safe, actual execution evidence.
- Compare estimated versus actual row counts.
- Review indexes, statistics, join order, and predicates together.
- Measure before and after any optimization.
- Test concurrency and cache state where they materially affect latency.
- Prefer portable query improvements before product-specific hints unless architecture requires otherwise.

## Related Knowledge

- `Indexes.md`
- `Execution-Plans.md`
- `Performance-Monitoring.md`
- `Joins.md`
- `Partitioning.md`

## References

- Database query-optimization literature.
- Target DBMS optimizer and statistics documentation.