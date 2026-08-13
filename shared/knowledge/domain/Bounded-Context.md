# Bounded Context

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **bounded context** is an explicit boundary within which a domain model and its language have a consistent meaning.

## Purpose

Help QA avoid assuming that identical terms, identifiers, states, or rules mean the same thing across systems or business areas.

## Core Concepts

### Model Boundary
Defines where a set of concepts and rules applies.
### Context-Specific Language
A term has precise meaning inside the boundary.
### Context Mapping
Relationships describe how concepts translate between boundaries.
### Integration Contract
Cross-context exchange requires explicit mapping.

## How It Works

Each context owns its model; integrations translate concepts rather than assuming shared internal representation.

## When to Use

Use for multi-service systems, organizational boundaries, overloaded terminology, and integration testing.

## When Not to Use

Do not invent bounded contexts from repository folders or services without domain evidence.

## Advantages

Clarifies ownership and reduces semantic coupling.

## Limitations

Real boundaries may be organizational, conceptual, and technical at different levels.

## Examples

`Product` in Catalog can describe sellable attributes while `Product` in Inventory focuses on stock identity and availability; mappings must preserve intended meaning.

## Best Practices

- Identify model ownership.
- Define context-specific terms.
- Test mappings at boundaries.
- Verify missing/unknown values and version changes.

## Related Knowledge

- `Domain-Driven-Thinking.md`
- `Ubiquitous-Language.md`
- `Domain-Model.md`

## References

- Eric Evans, *Domain-Driven Design*.