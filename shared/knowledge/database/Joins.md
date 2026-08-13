# Joins

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **join** combines rows from two or more relational inputs based on matching conditions. Joins are essential for validating relationships but are also a common source of incorrect QA evidence when cardinality is misunderstood.

## Purpose

This article helps QA choose the correct join type, detect missing/orphan relationships, avoid accidental row multiplication, and interpret null-extended results accurately.

## Core Concepts

### INNER JOIN
Returns combinations that satisfy the join condition on both sides.

### LEFT OUTER JOIN
Preserves all left-side rows and supplies nulls for missing right-side matches.

### RIGHT / FULL OUTER JOIN
Preserve the right side or both sides where supported.

### CROSS JOIN
Produces the Cartesian product of both inputs and can explode row counts.

### Join Cardinality
One-to-one, one-to-many, and many-to-many relationships determine how many output rows each input row can produce.

### Join Predicate
The join condition should reflect actual keys/relationships. Missing part of a composite key can create false matches.

## How It Works

Logically, the DBMS matches rows according to the predicate. Physically, it may use nested-loop, hash, merge, index-assisted, or other strategies. The physical algorithm affects performance but not intended logical result semantics.

## When to Use

Use joins for parent-child validation, reconciliation, orphan detection, report checks, migration comparisons, permissions derived from relationships, and cross-table defect analysis.

## When Not to Use

Do not join tables simply because similarly named columns exist. Do not aggregate joined results until multiplicity is understood.

## Advantages

Joins reconstruct related business information from normalized structures and make missing or inconsistent relationships visible.

## Limitations

Many-to-many joins can multiply rows dramatically. Outer joins introduce nulls. Filtering in the wrong clause can unintentionally turn an outer join into inner-join-like behavior.

## Examples

### Orphan Detection
A left join from child to parent followed by `WHERE parent.key IS NULL` can identify child rows without a matching parent when physical constraints are absent.

### Row Multiplication
Joining orders to items turns one order into multiple result rows. Counting orders after the join requires careful distinct/grouping logic.

### Composite Key Error
Joining only on `order_id` when the real relationship is `(tenant_id, order_id)` can mix tenants and create false validation failures.

## Best Practices

- Join on authoritative keys, including all composite-key components.
- Predict expected cardinality before running the query.
- Compare pre- and post-join row counts when diagnosing duplication.
- Use outer joins deliberately for missing-match analysis.
- Keep filters on the correct side/clause to preserve intended semantics.
- Inspect a small sample before trusting aggregate results.

## Related Knowledge

- `Relationships.md`
- `Primary-Keys.md`
- `Foreign-Keys.md`
- `Aggregation.md`
- `Data-Validation.md`

## References

- ISO/IEC 9075, SQL joined tables.
- Target DBMS query-planning documentation.