# Entity Lifecycle

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

An **entity lifecycle** describes how a business entity is created, activated, modified, suspended, expired, closed, merged, archived, or otherwise changes over time.

## Purpose

Help QA derive lifecycle-aware coverage for state, mutability, identity, permissions, historical behavior, and downstream references.

## Core Concepts

### Creation
Defines when the entity becomes business-valid and what mandatory data or approvals are required.

### Active State
The entity can participate in normal business operations.

### Modification
Allowed fields and relationships can change while immutable identity or historical facts remain protected.

### Suspension / Inactivation
The entity exists but normal use is restricted.

### Expiry
Validity ends based on time or condition.

### Closure / Termination
The business relationship ends, potentially with outstanding obligations or history preserved.

### Merge
Duplicate or related entities can be consolidated while preserving traceability.

### Archival / Retention
Inactive entities may remain available for history, audit, reporting, or legal requirements.

## How It Works

```text
Create → Validate/Approve → Active
   ↘                    ↙
   Reject            Suspend
                         ↓
                    Reactivate
                         ↓
              Close / Expire / Archive
```

Actual lifecycle can branch and include correction, merge, or reopen paths. Each transition can change permissions, visibility, relationships, and downstream behavior.

## When to Use

Use for customer, product, account, permit, subscription, employee, order, and other long-lived business objects.

## When Not to Use

Do not assume lifecycle is equivalent to one `status` field. Do not infer deletion or retention behavior from UI visibility.

## Advantages

Lifecycle thinking reveals stale-reference, invalid-action, reactivation, expiry, and historical consistency defects.

## Limitations

Different contexts can maintain independent lifecycle states for the same real-world object. External systems can lag behind authoritative state.

## Examples

A product is inactive for new orders but must remain visible on historical orders. QA verifies new-use restriction without breaking history.

A customer record is merged into another identity. Historical transactions must remain traceable and future actions must use the surviving identity according to approved rules.

## Best Practices

- Define lifecycle states, entry/exit conditions, and actors.
- Identify field mutability by lifecycle stage.
- Test inactive/expired entities in new and historical flows.
- Verify relationship behavior after closure or merge.
- Include time boundaries and stale sessions.
- Preserve audit/history expectations.
- Distinguish soft deletion, archival, and business closure.

## Related Knowledge

- `Business-Entity.md`
- `Process-Lifecycle.md`
- `Entity-Relationships.md`
- `Data-Retention.md`
- `Audit-Trail.md`

## References

- Domain lifecycle and data-governance literature.
- Approved entity lifecycle specifications.
