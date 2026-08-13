# Primary Keys

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
A primary key is the selected key used to uniquely identify each row in a table and is not nullable under relational SQL semantics.

## Purpose
Support uniqueness, identity, relationship, and duplicate-data validation.

## Core Concepts
### Uniqueness
No two rows may share the same primary-key value combination.
### Composite Key
A key may contain multiple columns.
### Surrogate and Natural Keys
Identity may use generated technical values or meaningful business attributes.

## How It Works
The DBMS enforces the primary-key constraint during inserts and updates; foreign keys may reference it.

## When to Use
Use for record identification, duplicate testing, relationship validation, and migration reconciliation.

## When Not to Use
Do not assume the primary key is the same as the business identifier exposed to users.

## Advantages
Primary keys provide stable row identity and support referential integrity.

## Limitations
A technically unique key does not guarantee business-level uniqueness unless the business rule is also constrained.

## Examples
`order_id` may be the primary key while `external_order_number` has a separate unique constraint.

## Best Practices
- Test duplicate insertion and key updates where permitted.
- Verify generated-key behavior without assuming sequence continuity.
- Distinguish technical and business uniqueness.

## Related Knowledge
- `Foreign-Keys.md`
- `Constraints.md`
- `Relationships.md`

## References
- ISO/IEC 9075, SQL.