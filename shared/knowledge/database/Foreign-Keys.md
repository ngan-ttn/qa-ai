# Foreign Keys

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **foreign key** is a relational constraint that requires values in one set of columns to correspond to a referenced key in another or the same table, subject to nullability and referential-action rules.

## Purpose

This article helps QA validate referential integrity, parent-child behavior, cascades, orphan prevention, migration ordering, and deletion/update impacts.

## Core Concepts

### Referencing and Referenced Tables
The child/referencing table contains the foreign-key columns; the parent/referenced table exposes the target key.

### Referential Integrity
A non-null referencing value must match an allowed referenced key when the foreign key is enforced.

### Nullable Foreign Key
A relationship can be optional if the foreign-key columns permit null under the schema.

### Referential Actions
On parent update or delete, a DBMS may restrict the operation, cascade it, set child values to null/default, or apply another supported action.

### Self-Reference
A foreign key can reference the same table, such as an employee-manager hierarchy.

## How It Works

On insert or update of a child row, the DBMS checks the referenced key. On update/delete of a parent key, the configured referential action determines the result.

## When to Use

Use foreign-key knowledge for parent-child CRUD, delete rules, import order, migration, orphan detection, and integrity validation.

## When Not to Use

Do not assume every logical relationship has a physical foreign key. Some architectures enforce references in application code or across services where a DB constraint cannot exist.

## Advantages

Foreign keys prevent many orphan and invalid-reference states and make relational intent explicit in the schema.

## Limitations

They do not validate all cross-row business rules and can add write coordination cost. Cross-database or distributed relationships may not be enforceable by one DBMS.

## Examples

### Invalid Child
An order references a nonexistent customer. If a foreign key exists, the invalid row should not persist.

### Restricted Delete
Deleting a customer with active orders may fail because the schema uses `RESTRICT`/equivalent behavior.

### Cascade
Deleting a parent automatically deletes children under a cascading rule. QA must verify this only when the schema explicitly defines it.

## Best Practices

- Confirm the actual referenced columns and actions.
- Test valid, invalid, null, and delete/update paths.
- Detect orphan rows during migration reconciliation.
- Do not infer cascade behavior from application UI wording.
- Consider transaction boundaries when parent and child rows are created together.

## Related Knowledge

- `Primary-Keys.md`
- `Relationships.md`
- `Constraints.md`
- `Transactions.md`
- `Data-Migration-Testing.md`

## References

- ISO/IEC 9075, referential constraints.
- Target DBMS foreign-key documentation.