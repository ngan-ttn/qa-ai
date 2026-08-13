# Entity Relationships

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Entity relationships** describe meaningful business associations among entities, including ownership, membership, dependency, composition, reference, and temporal relationships.

## Purpose

Help QA validate relationship correctness, cardinality, lifecycle coupling, authorization, and cross-system mapping.

## Core Concepts

### Cardinality
One-to-one, one-to-many, many-to-many, or constrained counts depending on the business model.

### Ownership
One entity may own or control another's lifecycle or permissions.

### Composition
A child concept may exist only as part of a parent business object.

### Association
Entities may be linked without shared lifecycle.

### Referential Business Rule
A relationship can require valid, active, eligible, or context-compatible related entities.

### Temporal Relationship
A relationship can have effective start/end dates or historical versions.

### Directionality
The meaning of `A relates to B` may differ from the reverse direction.

## How It Works

Relationships are created, changed, expired, or removed through business actions. QA validates both the relationship record and the business consequences: visibility, permission, calculation, eligibility, and lifecycle behavior.

## When to Use

Use for parent-child structures, account ownership, customer-product relationships, order lines, memberships, allocations, permissions, and integration mappings.

## When Not to Use

Do not infer business cardinality directly from database foreign keys. Technical schemas can allow more states than business rules permit.

## Advantages

Relationship analysis exposes orphan, duplicate-link, wrong-owner, stale-reference, and cross-entity consistency defects.

## Limitations

Relationships may be implicit, derived, effective-dated, or represented differently across systems.

## Examples

A permit may cover multiple UPNs while each UPN can appear on multiple historical permits. The valid relationship at a specific date depends on approval period and business rules.

A corporate account may have multiple authorized users with roles and effective dates. Removing one user should not remove the account or unrelated users.

## Best Practices

- Define relationship meaning and cardinality from business evidence.
- Test creation, update, removal, and expiry.
- Verify ownership and authorization implications.
- Check duplicate and orphan relationships.
- Include effective-date boundaries.
- Validate behavior when related entities are inactive or deleted.
- Compare cross-system relationship mappings when integrations exist.

## Related Knowledge

- `Business-Entity.md`
- `Entity-Lifecycle.md`
- `Master-Data.md`
- `Domain-Model.md`
- `../database/Relationships.md`

## References

- Domain modeling and data-modeling literature.
- Approved entity relationship definitions.
