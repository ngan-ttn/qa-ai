# Aggregation

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Aggregation** summarizes a set of rows into metrics such as counts, totals, averages, minima, maxima, or grouped measures. SQL commonly uses aggregate functions together with `GROUP BY` and `HAVING`.

## Purpose

Aggregation knowledge helps QA validate dashboards, balances, inventory totals, reconciliation, duplicates, reporting logic, and data-quality metrics without masking population or join errors.

## Core Concepts

### COUNT
`COUNT(*)` counts result rows, while `COUNT(expression)` generally excludes null expression values.

### SUM and AVG
Calculate totals and averages over applicable numeric values, with null handling defined by SQL semantics.

### MIN and MAX
Return extrema according to data type and collation/order semantics.

### GROUP BY
Partitions the input into groups defined by grouping expressions.

### HAVING
Filters groups after aggregation, unlike `WHERE`, which filters input rows before grouping.

### Distinct Aggregation
`COUNT(DISTINCT x)` or equivalent can remove duplicate values, but using it to hide an incorrect join is unsafe.

## How It Works

A typical logical flow is:

```text
FROM / JOIN
    ↓
WHERE filter
    ↓
GROUP BY
    ↓
Aggregate functions
    ↓
HAVING
    ↓
SELECT / ORDER BY
```

If joins multiply rows before aggregation, the resulting totals can be wrong even though the aggregate syntax is correct.

## When to Use

Use aggregation for totals, balances, summary cards, reconciliation, duplicate detection, coverage metrics, warehouse checks, and report validation.

## When Not to Use

Do not trust aggregates until the source population and join cardinality are validated. Do not compare rounded display totals directly to higher-precision database values without understanding rounding rules.

## Advantages

Aggregation efficiently validates large datasets and exposes population-level defects that row-by-row sampling may miss.

## Limitations

Nulls, duplicates, joins, rounding, timezone/date bucketing, and filtering rules can materially alter results. Analytical systems may also contain delayed or transformed data.

## Examples

### Count Semantics
A column contains three rows: `A`, `B`, and `NULL`. `COUNT(*)` returns 3 while `COUNT(column)` returns 2.

### Duplicate Check
Group by the authoritative uniqueness columns and use `HAVING COUNT(*) > 1` to identify duplicate groups.

### Reconciliation
Sum transaction amounts by business date and compare with an independently generated expected total, accounting for reversals and status filters defined by the requirement.

## Best Practices

- Define source population and filters explicitly.
- Validate join multiplicity first.
- Understand null and distinct semantics.
- Reconcile aggregate results to detail samples.
- Confirm precision, rounding, currency, and timezone rules.
- Treat warehouse/reporting freshness separately from source-of-truth correctness.

## Related Knowledge

- `Data-Query-Language.md`
- `Joins.md`
- `Data-Validation.md`
- `Data-Warehousing.md`
- `Performance-Monitoring.md`

## References

- ISO/IEC 9075, SQL aggregate functions.
- Target DBMS aggregate and numeric documentation.