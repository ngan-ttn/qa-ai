# Relational Database Concepts

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **relational database** represents data as relations, commonly implemented as tables composed of rows and columns. Relationships between data sets are expressed through shared values and keys, while constraints and transactions help preserve consistency.

The relational model separates logical data structure from physical storage. Applications reason about rows, columns, keys, and relationships without needing to know exactly where pages or files are stored.

## Purpose

This article gives QA a foundation for understanding relational schemas, interpreting SQL results, validating relationships, and distinguishing relational concepts from application-layer objects or document-oriented storage.

## Core Concepts

### Relation / Table

A relation is a set of tuples under a defined heading. Practical DBMSs expose relations mainly as tables. Physical tables may include implementation details that go beyond the pure relational model.

### Tuple / Row

A row represents one occurrence of the facts modeled by a table. Row identity should be established through keys or documented uniqueness rather than visual row position.

### Attribute / Column

A column defines one named property with a domain or data type. Nullability, defaults, constraints, and collation may affect allowed values and comparisons.

### Key

Keys identify rows or relate tables. Candidate keys are minimal unique identifiers; a primary key is the chosen principal key; foreign keys reference candidate or primary keys in another or the same table.

### Relationship

One-to-one, one-to-many, and many-to-many relationships describe how records associate. Many-to-many relationships are commonly represented through an associative table.

### Integrity Constraints

Relational integrity includes entity integrity, referential integrity, uniqueness, nullability, and additional checks. Not every business rule is necessarily represented as a database constraint.

### Set-Oriented Processing

SQL generally operates on sets or multisets of rows rather than one record at a time. Query results have no guaranteed order unless ordering is explicitly requested.

## How It Works

A simplified relational model might be:

```text
Customer
- customer_id (PK)
- name

Order
- order_id (PK)
- customer_id (FK)
- status

Customer 1 ───── * Order
```

The foreign key links each order to a customer. A query can join tables through these key values, while constraints may prevent invalid references.

Relational systems use declarative queries: the caller describes the desired result, and the optimizer chooses a physical execution plan. Therefore, logically equivalent queries can have different execution strategies.

## When to Use

Use relational concepts when validating SQL-backed systems, interpreting schemas, designing joins, checking duplicates, testing referential integrity, reviewing normalization, or tracing business entities across multiple tables.

## When Not to Use

Do not assume every database is relational. Document stores, key-value databases, graph databases, search engines, and event stores may model identity and relationships differently.

Do not assume table structure maps one-to-one to domain entities; a single business concept may span many tables, and one table may support several use cases.

## Advantages

Relational systems provide a mature, standardized model for structured data, expressive querying, constraints, transactional operations, and relationships. SQL enables flexible ad hoc verification, which is especially valuable for QA investigations and reconciliation.

## Limitations

Relational modeling can require joins and schema evolution, and highly distributed or schema-flexible workloads may prefer other models. Product-specific behavior also differs in null handling, locking, isolation, types, indexing, and DDL semantics.

## Examples

### One-to-Many

One customer can own many orders, but each order references one customer. QA verifies that all expected orders use the correct `customer_id` and that invalid references are rejected if referential integrity is enforced.

### Many-to-Many

Users may belong to many roles and each role to many users. A junction table such as `user_role(user_id, role_id)` represents the relationship. Duplicate pairs may need a unique constraint depending on the model.

### Set Semantics

A query without `ORDER BY` returns the correct rows but in a different sequence between runs. This is not automatically a database defect because row order is not guaranteed without explicit ordering.

## Best Practices

- Identify keys before validating row counts or relationships.
- Verify relationship cardinality from authoritative schema or requirements.
- Use joins carefully to avoid accidental row multiplication.
- Treat null as a distinct SQL concept rather than an empty string or zero.
- Avoid inferring business semantics solely from table or column names.
- Check both positive relationships and orphan/duplicate conditions where relevant.
- Use `ORDER BY` when test expectations depend on deterministic ordering.

## Related Knowledge

- `Tables.md`
- `Columns.md`
- `Rows.md`
- `Primary-Keys.md`
- `Foreign-Keys.md`
- `Relationships.md`
- `Normalization.md`
- `SQL-Overview.md`

## References

- E. F. Codd, relational model literature.
- ISO/IEC 9075, SQL.
- Target DBMS documentation for implementation-specific relational behavior.