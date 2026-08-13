# Relationships

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Relationships** describe how records or business entities associate with one another. In relational databases, relationships are typically represented by keys, foreign keys, junction tables, or agreed logical references.

## Purpose

This article helps QA translate relationship requirements into validation of cardinality, ownership, optionality, referential integrity, and join behavior.

## Core Concepts

### One-to-One
One record is associated with at most one corresponding record on the other side.

### One-to-Many
One parent can relate to many children while each child relates to one parent under the model.

### Many-to-Many
Both sides can relate to multiple records, commonly implemented through an associative table.

### Optionality
A relationship can be mandatory or optional. Nullability and constraints may reflect this but should be confirmed against requirements.

### Ownership and Lifecycle
Deleting or changing one record may or may not affect related records. Ownership semantics are business/design decisions, not implied by cardinality alone.

## How It Works

Keys connect records, and queries use joins to retrieve related data. Constraints can enforce existence, but cardinality such as one-to-one may also require uniqueness constraints.

## When to Use

Use relationship knowledge for schema review, joins, CRUD, cascade behavior, permissions tied to ownership, migration, and domain-model reconciliation.

## When Not to Use

Do not infer relationship rules solely from foreign-key presence. A database can permit technically valid relationships that violate application-specific business rules.

## Advantages

Explicit relationship models make data dependencies testable and improve consistency across CRUD and reporting flows.

## Limitations

Complex temporal, hierarchical, polymorphic, or cross-service relationships may not be fully represented by simple foreign keys.

## Examples

### One-to-One
A user has at most one profile row. A foreign key plus uniqueness constraint may enforce this.

### One-to-Many
One order contains many items. Deleting an item should not delete the order unless a specific rule says otherwise.

### Many-to-Many
Products belong to many categories through `product_category`. QA checks duplicate pairs and missing associations.

## Best Practices

- Confirm cardinality and optionality from authoritative models.
- Validate positive and invalid relationships.
- Test relationship lifecycle behavior on update/delete.
- Check uniqueness needed to enforce one-to-one or junction semantics.
- Reconcile application/domain relationships with physical implementation without assuming one-to-one mapping.

## Related Knowledge

- `Foreign-Keys.md`
- `Primary-Keys.md`
- `Constraints.md`
- `Joins.md`
- `Normalization.md`

## References

- Relational modeling literature.
- Target schema and DBMS constraint documentation.