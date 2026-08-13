# Indexes

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
An index is a database structure that provides alternative access paths to table data and may also enforce uniqueness.

## Purpose
Help QA understand performance and integrity effects of indexing without assuming a particular engine implementation.

## Core Concepts
### Search Key
Indexed columns or expressions determine lookup organization.
### Composite Index
Multiple fields may participate and order can matter.
### Unique Index
May enforce uniqueness subject to DBMS null semantics.

## How It Works
The DBMS maintains index entries as data changes and the optimizer may choose an index for eligible queries.

## When to Use
Use for query-performance analysis, uniqueness checks, and migration regression.

## When Not to Use
Do not assume an index will always be used or always improve performance.

## Advantages
Indexes can reduce data access work and support constraints.

## Limitations
They consume storage and add maintenance cost to writes.

## Examples
An index on `(customer_id, created_at)` may support customer-history queries depending on predicates and engine planning.

## Best Practices
- Measure with representative data.
- Review write impact.
- Avoid duplicate/redundant indexes.
- Use execution plans to confirm access paths.

## Related Knowledge
- `Query-Optimization.md`
- `Execution-Plans.md`
- `Performance-Monitoring.md`

## References
- Target DBMS indexing documentation.