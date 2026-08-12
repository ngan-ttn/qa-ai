# GraphQL

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**GraphQL** is a query language and runtime for APIs in which clients request specific fields from a typed schema. Common operation types include queries for reading data, mutations for changing data, and subscriptions for streaming updates when supported.

## Purpose

GraphQL knowledge helps QA test schema-driven behavior, field selection, nested queries, resolver authorization, nullability, partial errors, query complexity, and compatibility.

## Core Concepts

### Schema

The schema defines object types, fields, arguments, enums, interfaces, unions, input types, and operation entry points.

### Query

A query requests selected fields. Clients can shape the response rather than receiving a fixed representation.

### Mutation

A mutation performs state-changing operations according to schema-defined semantics.

### Resolver

Resolvers obtain data for schema fields. Authorization and performance problems can arise at resolver boundaries.

### Nullability

GraphQL types explicitly distinguish nullable and non-null fields. A non-null failure can propagate null upward according to GraphQL execution rules.

### Errors

A GraphQL response can contain both `data` and `errors`, so HTTP success alone does not prove operation success.

### Introspection

GraphQL supports schema introspection unless restricted by deployment policy.

### Query Complexity

Deep or broad queries can create high server cost. Some providers enforce depth, complexity, timeout, or rate controls.

## How It Works

```text
Client query
     ↓
GraphQL schema validation
     ↓
Resolvers execute
     ↓
Data + possible field errors
     ↓
Response shaped like requested selection
```

Transport is often HTTP, but GraphQL semantics are defined above the transport layer.

## When to Use

Use GraphQL knowledge for schema-based APIs, client-defined response shapes, nested object access, mutation workflows, subscriptions, or GraphQL gateway testing.

## When Not to Use

Do not apply REST-specific expectations such as one resource per URI or status-code-only success interpretation to GraphQL without checking the actual transport contract.

## Advantages

GraphQL can reduce over-fetching, support strong typing and introspection, and let clients request exactly the fields they need.

## Limitations

It can create resolver-level authorization gaps, N+1 performance problems, complex caching, query-cost abuse, and more complicated error interpretation.

## Examples

### Field Selection

A query requests only `id` and `status`. QA verifies no unrequested sensitive fields are returned.

### Partial Error

One nested resolver fails while other fields succeed. The response may include partial `data` plus `errors`; QA validates both according to schema rules.

### Restricted Field

A caller can query the object but lacks permission for a sensitive field. Field-level authorization must still be enforced.

## Best Practices

- Validate operations against the schema.
- Test nullable and non-null behavior.
- Test field- and resolver-level authorization, not only operation-level access.
- Validate aliases, variables, fragments, nested selection, and invalid arguments where relevant.
- Check partial errors and response-path information.
- Include query-depth or complexity controls where documented.
- Test schema evolution for consumer compatibility.
- Avoid assuming HTTP `200` means the GraphQL operation is fully successful.

## Related Knowledge

- `API-Fundamentals.md`
- `Authorization.md`
- `Performance-Testing.md`
- `API-Versioning.md`
- `Contract-Testing.md`

## References

- GraphQL Specification.
- GraphQL over HTTP specification where applicable.

Schema details and transport behavior must come from the target GraphQL service.
