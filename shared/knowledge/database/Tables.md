# Tables

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **table** is a relational database object that organizes data into rows and columns under a defined schema. Tables commonly represent persistent entities, associations, events, reference values, or technical state.

## Purpose

This article helps QA interpret table structure, identify row populations, trace persistence effects, and avoid assuming that a table maps one-to-one to a business entity.

## Core Concepts

### Table Definition
A table defines named columns, data types, nullability, defaults, and constraints.

### Base Table
A base table stores data directly, unlike a logical view whose rows are derived from a query.

### Keys
Primary, candidate, and foreign keys identify rows and relationships.

### Constraints
Constraints restrict allowed states and may enforce uniqueness, references, ranges, or required values.

### Row Population
The set of rows in a table changes over time through inserts, updates, deletes, migrations, and database-side logic.

### Logical vs Physical Structure
The logical table does not expose all physical details such as pages, partitions, compression, or indexes.

## How It Works

Applications or database routines execute operations against a table. The DBMS validates types and constraints, manages transactions, updates indexes, and records persistent changes according to engine semantics.

```text
Input operation
   ↓
Column/type validation
   ↓
Constraint checks
   ↓
Row change
   ↓
Index/trigger side effects
   ↓
Commit or rollback
```

## When to Use

Use table knowledge when validating CRUD behavior, migrations, data reconciliation, joins, constraints, reports, archival, and defect investigation.

## When Not to Use

Do not infer a business entity's complete state from one table without confirming mappings. Do not assume row order is meaningful unless an explicit ordering rule exists.

## Advantages

Tables provide structured, queryable persistence and make state validation straightforward when keys and relationships are understood.

## Limitations

A table can contain implementation-specific columns, denormalized data, audit fields, soft-delete flags, or technical state that is not directly visible in requirements. Some systems use views or non-relational stores instead.

## Examples

### Entity Table
An `orders` table may store order identifiers, customer references, status, and timestamps.

### Junction Table
A `user_role` table can model a many-to-many relationship between users and roles.

### History Table
An audit/history table may contain multiple versions for one business entity, so row count is not equal to entity count.

## Best Practices

- Identify the table's purpose before writing validation queries.
- Use stable keys rather than row position.
- Check constraints and relationships alongside field values.
- Compare expected and actual row populations carefully.
- Consider soft delete, history, partitioning, and asynchronous updates.
- Avoid destructive changes in shared environments without authorization.

## Related Knowledge

- `Columns.md`
- `Rows.md`
- `Primary-Keys.md`
- `Foreign-Keys.md`
- `Constraints.md`
- `Views.md`

## References

- ISO/IEC 9075, SQL table concepts.
- Target DBMS table documentation.