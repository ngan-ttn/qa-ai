# Views

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **view** is a named database object defined by a query. It presents data through a logical interface without necessarily storing the result. Some DBMSs also support materialized views that persist query results and refresh them according to configured rules.

## Purpose

This article helps QA understand derived database interfaces, validate report/filter logic, analyze security boundaries, and distinguish base-table state from view-visible state.

## Core Concepts

### Logical View
Stores the query definition and computes results when accessed.

### Materialized View
Stores derived results physically and requires refresh or maintenance. Freshness guarantees are implementation-specific.

### Abstraction
A view can hide joins, transformations, soft-delete filters, or implementation complexity from consumers.

### Security
Views can expose selected columns/rows while restricting direct access to base tables, depending on DBMS permissions.

### Updatability
Some views can accept inserts/updates; others are read-only. Rules differ by product and definition.

## How It Works

When a logical view is queried, the DBMS expands or optimizes its defining query against underlying objects. A materialized view instead serves stored derived state that may be refreshed synchronously or asynchronously.

## When to Use

Use view knowledge for reporting, abstraction-layer validation, data-access security, backward-compatible schema interfaces, soft-delete behavior, and data-warehouse checks.

## When Not to Use

Do not assume a view is current or writable. Do not treat a view's filtered result as proof that base rows do not exist.

## Advantages

Views encapsulate complex queries, centralize reusable logic, and can provide stable or restricted interfaces over changing base schemas.

## Limitations

Nested/complex views can obscure performance and business logic. Materialized views can be stale. Changes to underlying objects may break dependent views.

## Examples

### Soft-Delete View
A view exposes only rows where `deleted_at IS NULL`. QA sees fewer rows than the base table by design.

### Security View
A reporting role can query a view that excludes sensitive columns while direct base-table access is denied.

### Materialized Summary
A dashboard reads a materialized daily summary refreshed every hour. A newly committed transaction may not appear immediately if that refresh policy is expected.

## Best Practices

- Inspect the view definition before interpreting results.
- Identify underlying tables and filters.
- Confirm whether the view is logical or materialized.
- Validate refresh/freshness requirements separately.
- Include dependent views in schema-change regression analysis.
- Do not assume updatability across DBMS products.

## Related Knowledge

- `Database-Objects.md`
- `Data-Query-Language.md`
- `Joins.md`
- `Aggregation.md`
- `Data-Warehousing.md`

## References

- ISO/IEC 9075, SQL views.
- Target DBMS view/materialized-view documentation.