# Aggregation

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
Aggregation summarizes multiple rows using functions such as `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX`, often with grouping.

## Purpose
Support validation of totals, summaries, dashboards, and reconciliations.

## Core Concepts
### Aggregate Function
Produces a summary from a set of input values.
### GROUP BY
Partitions rows into groups.
### HAVING
Filters groups after aggregation.
### NULL Behavior
Aggregate handling of nulls differs by function.

## How It Works
Rows are filtered, grouped, and reduced to aggregate results according to query semantics.

## When to Use
Use for totals, balances, counts, metrics, and duplicate detection.

## When Not to Use
Do not aggregate joined data until row multiplication has been understood.

## Advantages
Aggregation efficiently verifies large datasets and derived business summaries.

## Limitations
Grouping mistakes and null semantics can hide data-quality issues.

## Examples
`COUNT(*)` counts rows while `COUNT(column)` excludes null values in that column.

## Best Practices
- Define the population and grouping keys explicitly.
- Reconcile aggregates to detail samples.
- Check duplicate effects from joins.
- Distinguish zero from no matching rows.

## Related Knowledge
- `Data-Query-Language.md`
- `Joins.md`
- `Data-Validation.md`

## References
- ISO/IEC 9075, SQL.