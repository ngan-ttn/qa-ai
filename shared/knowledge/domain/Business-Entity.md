# Business Entity

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **business entity** is a business-significant concept whose identity, attributes, relationships, lifecycle, ownership, and invariants matter to a domain. A business entity is defined by meaning and behavior, not by one database table, API resource, or UI form.

## Purpose

Help QA and QA-AI reason about identity, source of truth, lifecycle, duplication, mutability, relationships, and cross-system representation without overfitting tests to implementation.

## Core Concepts

### Business Identity
The criteria that make one entity distinct from another. Business identity may differ from a technical surrogate ID.

### Attributes
Properties describing the entity. Some are mutable, immutable, derived, historical, sensitive, or context-specific.

### Ownership
A role or system may be authoritative for creation or change of particular attributes.

### Source of Truth
The authoritative representation for a fact can differ by field or context rather than one system owning everything.

### Relationships
Entities can reference, contain, depend on, or be associated with other entities.

### Lifecycle
Creation, activation, modification, suspension, merge, closure, archival, and other state changes affect what actions are valid.

### Invariants
Conditions that must remain true for valid business state.

### Duplicate / Merge
Real-world entities can be represented more than once and later matched or merged according to business rules.

### Cross-Context Identity
The same real-world object can have different identifiers and meaning in different systems or bounded contexts.

## How It Works

```text
Business identity
      ↓
Authoritative attributes + relationships
      ↓
Lifecycle actions
      ↓
Rules / invariants
      ↓
Representations across UI / API / DB / integrations
```

QA validates business meaning across representations rather than assuming technical equality implies business equality.

## When to Use

Use for data-centric requirements, CRUD behavior, lifecycle testing, integration mapping, migration, duplicate handling, master data, permissions, and domain modeling.

## When Not to Use

Do not equate a business entity automatically with one table, one JSON object, or one screen. Do not assume technical IDs are stable business identifiers without evidence.

## Advantages

Entity thinking improves identity, ownership, relationship, lifecycle, duplicate, and invariant coverage.

## Limitations

Entity boundaries can differ across contexts. Legacy systems may contain multiple identifiers, stale duplicates, or denormalized copies with different freshness.

## Examples

### Order
An `Order` has identity, customer relationship, lines, totals, status, ownership, and lifecycle even when stored across many tables and exposed by several APIs.

### Customer
A customer can exist in CRM, loyalty, payment, and support systems with different IDs. QA must verify mapping rules rather than assume one universal customer key.

### Product
Product master data can contain an immutable code but mutable name or classification. Downstream systems may cache older descriptions while the authoritative identity remains unchanged.

## Best Practices

- Identify business key and technical identifiers separately.
- Clarify attribute ownership and source of truth.
- Define mutable, immutable, derived, and historical fields.
- Test duplicate creation, merge, and identity collision risks where relevant.
- Validate relationships and invariants across lifecycle changes.
- Cover deactivation, archival, reopening, and stale references.
- Map cross-system identifiers explicitly.
- Avoid coupling high-level business tests to internal schema unnecessarily.

## Related Knowledge

- `Entity-Relationships.md`
- `Entity-Lifecycle.md`
- `Master-Data.md`
- `Transaction-Data.md`
- `Reference-Data.md`
- `Domain-Model.md`

## References

- Domain modeling and master-data literature.
- Approved business data definitions.
