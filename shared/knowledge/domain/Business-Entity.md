# Business Entity

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **business entity** is a business-significant concept whose identity, attributes, relationships, lifecycle, and rules matter to the domain.

## Purpose

Help QA distinguish business objects from implementation records and reason about identity, ownership, lifecycle, relationships, and invariants.

## Core Concepts

### Identity
Stable business identity distinguishes one entity from another.
### Attributes
Properties describing the entity.
### Relationships
Connections to other business concepts.
### Lifecycle
States and transitions over time.
### Invariants
Rules that must remain true for valid entity state.

## How It Works

Requirements create, change, relate, query, or retire entities through business processes. One entity may span multiple technical representations.

## When to Use

Use for data-centric requirements, CRUD behavior, lifecycle testing, integration mapping, and domain modeling.

## When Not to Use

Do not equate a business entity automatically with one database table or API resource.

## Advantages

Entity thinking improves identity, relationship, and lifecycle coverage.

## Limitations

Entity boundaries can differ across contexts and systems.

## Examples

An `Order` can have business identity, customer relationship, items, totals, status, and fulfillment lifecycle even if stored across many tables.

## Best Practices

- Identify business keys and ownership.
- Define mutable vs immutable attributes.
- Validate relationships and invariants.
- Cover lifecycle and duplicate identity risks.
- Separate business identity from storage identifiers.

## Related Knowledge

- `Entity-Relationships.md`
- `Entity-Lifecycle.md`
- `Master-Data.md`
- `Domain-Model.md`

## References

- Domain modeling and data-management literature.