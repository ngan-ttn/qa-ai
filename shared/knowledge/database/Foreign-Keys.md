# Foreign Keys

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview
A foreign key constrains values in one table to reference an eligible key in another table, or sometimes the same table.

## Purpose
Explain referential integrity for relationship and deletion/update testing.

## Core Concepts
### Referencing and Referenced Rows
The child stores the reference; the parent exposes the referenced key.
### Referential Actions
Delete or update behavior may restrict, cascade, set null, or follow engine-supported actions.

## How It Works
The DBMS checks that non-null foreign-key values satisfy the declared relationship and applies configured referential actions.

## When to Use
Use for parent-child data, orphan prevention, cascade behavior, and migration checks.

## When Not to Use
Do not assume every logical relationship is enforced by a physical foreign key.

## Advantages
Foreign keys prevent many classes of orphaned or inconsistent references.

## Limitations
They do not validate all business relationship rules and can add write/deployment considerations.

## Examples
An order item referencing a nonexistent order should be rejected when a foreign key enforces the relationship.

## Best Practices
- Test valid, invalid, null, update, and delete paths.
- Confirm configured referential action rather than assuming cascade.
- Validate migration order for related tables.

## Related Knowledge
- `Primary-Keys.md`
- `Relationships.md`
- `Constraints.md`

## References
- ISO/IEC 9075, SQL.