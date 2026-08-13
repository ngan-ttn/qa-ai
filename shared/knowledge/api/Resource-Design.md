# Resource Design

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**Resource design** is the practice of modeling API interfaces around stable business or technical concepts that consumers can identify and interact with. In resource-oriented APIs, resources such as customers, orders, files, permits, or reports are exposed through consistent operations and representations.

## Purpose

Resource design knowledge helps QA evaluate whether an API contract reflects meaningful domain concepts, uses consistent interaction patterns, and avoids leaking unstable implementation details such as internal table layouts or service names.

## Core Concepts

### Resource

A resource is an identifiable concept that has state or behavior relevant to API consumers. A resource is not necessarily a database row.

### Resource Identity

Resources normally have stable identifiers or URI locations. Identity should remain meaningful even if backend storage changes.

### Collection and Item

A collection represents multiple resources; an item represents one resource.

```text
/orders
/orders/123
```

### Representation

Clients interact with representations of resource state. Representation fields should reflect contract meaning rather than accidental internal structure.

### Relationship

Resources can relate to each other, for example customer-to-orders or project-to-members. Relationships may be modeled through nested resources, links, identifiers, or dedicated relationship endpoints.

### Action Modeling

Not every domain operation maps cleanly to CRUD. Domain actions may be modeled as state transitions, sub-resources, command endpoints, or other explicit operations. Consistency and clarity are more important than forcing artificial CRUD semantics.

## How It Works

Resource design typically starts from consumer use cases and domain concepts:

```text
Consumer Need
    ↓
Business Concept
    ↓
Resource Boundary
    ↓
Identity + Representation
    ↓
Supported Operations
    ↓
Error / State Rules
```

The resulting contract should let consumers reason about the resource without knowing implementation internals.

## When to Use

Use resource-design knowledge when reviewing REST-oriented API contracts, testing URI structures, evaluating consistency across endpoints, or analyzing whether field and operation boundaries match business concepts.

## When Not to Use

Do not force resource-oriented modeling onto APIs intentionally designed as RPC, GraphQL, gRPC, or event-driven interfaces. Do not reject a command-style endpoint solely because it is not CRUD if it accurately represents a domain action.

## Advantages

Good resource design can improve discoverability, consistency, client independence, versioning stability, and contract readability. It can also make test scenarios easier to organize around business entities and lifecycle states.

## Limitations

Resource modeling can become awkward for long-running commands, calculations, searches, batch operations, or cross-resource workflows. Poorly chosen resource boundaries can create excessive coupling or fragmented APIs.

## Examples

### Collection and Item

```text
GET /orders
GET /orders/123
POST /orders
```

### Relationship

```text
GET /customers/42/orders
```

### Domain Action

Instead of hiding an approval rule inside an ambiguous update, an API might expose an explicit operation representing the state transition if that matches the domain contract.

## Best Practices

- Model resources around stable domain concepts, not database tables.
- Keep identifiers stable and opaque where possible.
- Use consistent naming across related resources.
- Define resource lifecycle states and allowed transitions when stateful behavior matters.
- Avoid deeply nested resource hierarchies that make relationships hard to manage.
- Make command-style operations explicit when CRUD semantics would be misleading.
- Validate authorization at the resource and action boundary.

## Related Knowledge

- `REST-Architecture.md`
- `URI-Design.md`
- `HTTP-Methods.md`
- `Idempotency.md`
- `API-Versioning.md`
- `../domain/Business-Entity.md`

## References

- Roy Fielding's REST architectural work provides the foundation for resource-oriented interfaces.
- RFC 9110 defines HTTP method and representation semantics.

Project-specific resource boundaries must come from the API contract and domain requirements.
