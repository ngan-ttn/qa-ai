# Normalization

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Normalization** is a relational modeling approach that organizes data to reduce undesirable redundancy and update anomalies by decomposing relations according to dependencies. Common discussions include first, second, third normal form and Boyce-Codd normal form.

## Purpose

This article helps QA understand why one business concept may span several tables and how schema design influences update, insert, delete, join, and migration risks.

## Core Concepts

### Functional Dependency
A set of attributes determines another set under the modeled rules.

### First Normal Form
Values are represented in a relationally appropriate atomic structure rather than repeating groups within one attribute.

### Second and Third Normal Forms
These progressively address dependencies on only part of a composite key and transitive dependencies on non-key attributes.

### Denormalization
A schema can intentionally duplicate or precompute data for performance or operational reasons. Denormalization is not automatically a defect.

### Anomalies
Poor structure can create update, insert, or delete anomalies where one fact must be changed in many places or cannot be represented cleanly.

## How It Works

Normalization analyzes keys and dependencies, then separates facts into relations so that each fact is represented consistently. Queries later reassemble related data through joins.

## When to Use

Use normalization knowledge during schema review, duplicate-data analysis, join design, migration mapping, and investigations where the same fact appears in multiple places.

## When Not to Use

Do not demand a particular normal form as a universal QA requirement. Warehouses, read models, caches, and performance-sensitive systems may intentionally denormalize.

## Advantages

Normalization can reduce inconsistency, clarify ownership of facts, and simplify integrity enforcement.

## Limitations

Highly normalized designs can increase join complexity and may not fit analytical or distributed access patterns. Formal normal forms also depend on accurately known functional dependencies.

## Examples

### Repeated Customer Data
Storing customer name on every order can cause inconsistent updates. A normalized design may store customer data once and reference it from orders.

### Deliberate Denormalization
A reporting table stores daily totals so dashboards avoid expensive aggregation. QA verifies refresh and reconciliation behavior rather than flagging the duplication itself.

## Best Practices

- Understand business dependencies before judging schema shape.
- Treat denormalization as a design choice requiring consistency strategy.
- Test update paths where duplicated data exists.
- Verify joins do not lose or multiply records unexpectedly.
- Include migration/backfill logic when structure is normalized or denormalized.

## Related Knowledge

- `Relationships.md`
- `Primary-Keys.md`
- `Foreign-Keys.md`
- `Joins.md`
- `Data-Warehousing.md`

## References

- Relational normalization literature.
- Target data-model documentation.