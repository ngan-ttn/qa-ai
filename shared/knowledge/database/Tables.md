# Tables

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
A table is a relational structure that organizes data into rows and columns under a defined schema.

## Purpose
Explain the primary persistence structure used in relational database validation.

## Core Concepts
### Schema
Defines columns, types, defaults, nullability, keys, and constraints.
### Row Set
A table represents a set or multiset of records depending on query semantics.
### Identity
Keys distinguish records and support relationships.

## How It Works
Insert, update, delete, and query operations act on table data while constraints and transactions control validity.

## When to Use
Use when validating persistence, schema changes, CRUD behavior, relationships, and migrations.

## When Not to Use
Do not equate every application object with one physical table.

## Advantages
Tables provide explicit structure and strong integration with SQL and integrity rules.

## Limitations
Physical table design may differ from business models and can change without changing external behavior.

## Examples
An `orders` table may store order identity, customer reference, status, totals, and timestamps.

## Best Practices
- Validate schema and data separately.
- Avoid relying on row order without `ORDER BY`.
- Use keys rather than display values to identify records.

## Related Knowledge
- `Columns.md`
- `Rows.md`
- `Primary-Keys.md`
- `Constraints.md`

## References
- ISO/IEC 9075, SQL.