# Execution Plans

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
An execution plan describes the operations a DBMS chooses to execute a query.

## Purpose
Provide QA a diagnostic view for performance regressions without turning plan shape into a brittle functional assertion.

## Core Concepts
### Operators
Plans contain scans, seeks, joins, sorts, aggregates, and other engine-specific operators.
### Estimated and Actual Metrics
Some tools show estimates; runtime analysis may show observed rows and timing.
### Cost
Optimizer cost is an internal comparative model, not necessarily elapsed time.

## How It Works
The optimizer produces a plan based on schema, statistics, parameters, and available access paths.

## When to Use
Use to investigate slow queries and explain changes after indexes, statistics, or schema updates.

## When Not to Use
Do not require an exact plan shape unless it is an intentional technical contract.

## Advantages
Plans expose where database work occurs and help identify estimation or access problems.

## Limitations
Terminology and metrics are vendor-specific and can change between versions.

## Examples
A large table scan with a highly selective predicate may suggest missing or unusable indexing, but evidence must be measured.

## Best Practices
- Compare plans under equivalent conditions.
- Distinguish estimates from actual execution.
- Pair plan analysis with latency/resource measurements.

## Related Knowledge
- `Query-Optimization.md`
- `Indexes.md`
- `Performance-Monitoring.md`

## References
- Target DBMS execution-plan documentation.