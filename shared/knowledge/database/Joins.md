# Joins

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
A join combines rows from two or more relational inputs according to a join condition.

## Purpose
Enable correct validation of data distributed across related tables.

## Core Concepts
### INNER JOIN
Returns matching combinations.
### OUTER JOIN
Preserves unmatched rows from one or both sides according to join type.
### Join Cardinality
One-to-many joins can multiply result rows.

## How It Works
The DBMS evaluates join predicates and combines eligible row pairs; the optimizer selects a physical algorithm.

## When to Use
Use for relationship validation, reconciliation, reports, and multi-table assertions.

## When Not to Use
Do not use joins without understanding cardinality and duplicate effects.

## Advantages
Joins reconstruct related business information from normalized data.

## Limitations
Incorrect predicates can create missing, duplicated, or Cartesian results.

## Examples
Joining orders to order items yields one row per matching item, not necessarily one row per order.

## Best Practices
- Join on intended keys.
- Check expected cardinality.
- Use outer joins to detect missing relationships when appropriate.
- Validate counts before trusting aggregates over joined data.

## Related Knowledge
- `Relationships.md`
- `Foreign-Keys.md`
- `Aggregation.md`

## References
- ISO/IEC 9075, SQL.