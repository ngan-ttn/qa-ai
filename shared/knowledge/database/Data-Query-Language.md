# Data Query Language

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
DQL refers to SQL querying, primarily `SELECT`, used to retrieve and derive relational data.

## Purpose
Provide the foundation for evidence-based database verification.

## Core Concepts
### Projection
Chooses output expressions or columns.
### Selection
Filters rows with predicates.
### Ordering
`ORDER BY` defines result order when order matters.
### Grouping
Aggregation summarizes groups of rows.

## How It Works
A query describes a result; the optimizer chooses an execution strategy consistent with SQL semantics.

## When to Use
Use for backend checks, reconciliation, defect analysis, and migration validation.

## When Not to Use
Do not treat unspecified row order as deterministic.

## Advantages
Queries can validate exact stored state without modifying it.

## Limitations
Incorrect joins, null handling, or predicates can produce convincing but wrong evidence.

## Examples
A query may count active records before and after an operation to validate the expected delta.

## Best Practices
- Filter by stable identifiers.
- Handle `NULL` explicitly.
- Use deterministic ordering when comparing ordered outputs.
- Validate joins against relationship cardinality.

## Related Knowledge
- `Joins.md`
- `Aggregation.md`
- `Views.md`

## References
- ISO/IEC 9075, SQL.