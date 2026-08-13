# Execution Plans

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

An **execution plan** describes the physical operations a DBMS intends to use, or actually used, to execute a query. Plans can include scans, seeks, joins, sorts, aggregates, filters, lookups, exchanges, and memory-consuming operators.

## Purpose

This article helps QA use execution plans as diagnostic evidence for performance regressions without treating product-specific plan output as a universal rule.

## Core Concepts

### Estimated Plan
Shows the optimizer's expected operations and cardinalities without necessarily executing the query.

### Actual Plan
Where supported, includes runtime information such as actual rows, loops, timing, or memory. Collecting it can execute the query and therefore requires care.

### Scan and Seek
A scan reads a broader structure; a seek navigates directly to selected ranges or keys. A scan is not automatically bad if much of the data is required.

### Join Operator
Nested-loop, hash, merge, and other algorithms suit different row counts and access paths.

### Sort / Aggregate
These can require significant memory or spill to temporary storage when estimates or capacity are insufficient.

### Estimated vs Actual Rows
Large differences can signal estimation problems, skew, stale statistics, or correlation the optimizer did not model accurately.

## How It Works

The optimizer produces a plan based on schema, statistics, predicates, indexes, parameters, and configuration. Runtime execution follows that plan while actual resource conditions can produce additional effects such as spills, waits, or parallelism.

## When to Use

Use execution plans when a query is reproducibly slow, after index/schema changes, during data-growth tests, or when latency differs strongly across parameters.

## When Not to Use

Do not collect actual plans for destructive or heavy statements in shared/production environments without authorization. Do not label every table scan or high-cost operator as a defect in isolation.

## Advantages

Plans expose the DBMS's physical reasoning and make performance investigation evidence-based.

## Limitations

Plan formats are vendor-specific, estimated costs are not directly comparable across engines, and a plan snapshot may not capture concurrency, cache, or storage effects.

## Examples

### Estimate Error
An operator estimates 10 rows but processes 1,000,000. Downstream join and memory choices may become inefficient.

### Sort Spill
A query sorts more data than estimated and spills to temporary storage, increasing latency.

### Full Scan by Design
A monthly export reads 90% of a table. A scan may be more efficient than repeated index lookups and is not automatically a problem.

## Best Practices

- Start with a reproducible slow query and representative parameters.
- Compare estimated and actual cardinality where safe.
- Interpret operators in the context of total workload and row counts.
- Pair plan analysis with wait, CPU, I/O, and memory evidence.
- Record schema/index/statistics context when comparing plans across releases.
- Avoid copying vendor-specific tuning rules into generic expectations.

## Related Knowledge

- `Query-Optimization.md`
- `Indexes.md`
- `Performance-Monitoring.md`
- `Joins.md`
- `Aggregation.md`

## References

- Target DBMS execution-plan documentation.
- Database query-optimization literature.