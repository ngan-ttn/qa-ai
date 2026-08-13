# Relationships

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
Relationships describe associations among data entities, commonly one-to-one, one-to-many, or many-to-many.

## Purpose
Help QA translate business associations into relational validation coverage.

## Core Concepts
### Cardinality
Defines how many records may participate on each side.
### Optionality
Defines whether participation is required.
### Junction Table
Many-to-many relationships are commonly represented through an associative table.

## How It Works
Keys, foreign keys, unique constraints, and application logic implement relationship rules.

## When to Use
Use for entity modeling, joins, referential integrity, and relationship-specific business rules.

## When Not to Use
Do not infer cardinality only from sample data.

## Advantages
Explicit relationships improve data consistency and queryability.

## Limitations
Database constraints may represent only part of the domain relationship semantics.

## Examples
One customer may have many orders; an order belongs to one customer according to the approved model.

## Best Practices
- Verify cardinality and optionality against requirements.
- Test creation, reassignment, and deletion effects.
- Validate both constraints and application behavior.

## Related Knowledge
- `Foreign-Keys.md`
- `Joins.md`
- `Normalization.md`

## References
- Relational modeling literature.
- ISO/IEC 9075, SQL.