# Bounded Context

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **bounded context** is an explicit boundary within which a domain model and its language have a consistent meaning. The same term or real-world object can have different attributes, rules, identity, and lifecycle in another context.

## Purpose

Help QA and QA-AI identify semantic boundaries, ownership, translation, and integration risk without assuming all systems share one universal model.

## Core Concepts

### Context Boundary
Defines where a model's rules and terminology are valid.

### Local Model
Each context can represent concepts according to its own business responsibility.

### Ubiquitous Language
Terms are consistent within the context but can differ outside it.

### Context Ownership
A team or business area may own decisions and source-of-truth data within its boundary.

### Translation
Cross-context communication may require mapping between identifiers, statuses, codes, and meaning.

### Upstream / Downstream
One context may supply data or decisions another consumes.

### Anti-Corruption / Adaptation Layer
Some architectures isolate one model from another through mapping or translation; QA should verify it only when documented.

### Consistency Expectation
Cross-context state can be immediate, delayed, or eventually consistent depending on architecture and business requirement.

## How It Works

```text
Context A model
   │
   │ contract / mapping
   ▼
Translation boundary
   │
   ▼
Context B model
```

QA asks which context owns each fact, how concepts map, what timing is expected, and what happens when one context changes independently.

## When to Use

Use for microservices, enterprise integrations, partner systems, multiple business units, duplicated terminology, and complex domain models.

## When Not to Use

Do not introduce bounded-context terminology simply because applications are separate. A deployment boundary is not automatically a business semantic boundary.

## Advantages

Context thinking prevents false equivalence, clarifies ownership, and improves integration and regression analysis.

## Limitations

Boundaries can be difficult to discover, may not align with organization charts, and can change during architecture evolution.

## Examples

`Product` in Catalog may own descriptive and merchandising data, while `Product` in Inventory owns stock-tracking attributes. QA verifies mappings without expecting identical schemas.

`Customer` in Loyalty may be a member with tier and points, while CRM owns broader contact and marketing data. Deactivating one relationship does not necessarily delete the other.

## Best Practices

- Define business responsibility of each context.
- Identify source-of-truth ownership per fact.
- Document identifier, status, and code mappings.
- Test translation at semantic boundaries.
- Cover stale, missing, duplicated, and out-of-order updates where applicable.
- Do not assume immediate consistency across contexts.
- Use context-specific terminology in QA artifacts.

## Related Knowledge

- `Domain-Driven-Thinking.md`
- `Domain-Model.md`
- `Ubiquitous-Language.md`
- `Business-Events.md`
- `Entity-Relationships.md`

## References

- Domain-driven design context-mapping literature.
- Approved integration and ownership documentation.
