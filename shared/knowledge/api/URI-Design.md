# URI Design

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

A **Uniform Resource Identifier (URI)** identifies a resource or target in an API interaction. Good URI design makes identifiers stable, predictable, readable, and independent of backend implementation details.

## Purpose

URI-design knowledge helps QA review endpoint consistency, parameter placement, encoding, hierarchy, and compatibility. It also supports negative testing for malformed or ambiguous identifiers.

## Core Concepts

### Path

The path commonly identifies resource hierarchy or target location.

```text
/customers/42/orders/9
```

### Query

The query component commonly expresses optional selection, filtering, sorting, pagination, search, or projection criteria.

### Stability

A public URI should avoid exposing details likely to change, such as server file paths, internal class names, or database table names.

### Naming Consistency

Consistent pluralization, casing, separators, and terminology reduce consumer confusion.

### Encoding

Reserved and non-ASCII characters must be encoded according to URI rules. Incorrect encoding can change meaning or cause routing defects.

### Hierarchy

Nested paths can communicate relationships but excessive nesting may create brittle APIs.

## How It Works

```text
Scheme://Authority/Path?Query#Fragment
```

For HTTP APIs, the request target usually combines the path and optional query. Servers route the request based on the target and method.

## When to Use

Use URI-design knowledge when reviewing REST-style endpoints, testing path/query parameters, validating resource hierarchies, checking URL encoding, or assessing compatibility impact of endpoint changes.

## When Not to Use

Do not treat URI style preferences as functional defects unless they violate an agreed standard or contract. GraphQL and RPC-style APIs may intentionally use fewer resource-specific URIs.

## Advantages

Consistent URIs improve discoverability, maintainability, documentation quality, and consumer understanding.

## Limitations

A clear URI does not guarantee a good API. Business semantics, methods, schemas, errors, security, and compatibility remain equally important.

## Examples

### Stable Resource URI

```text
/orders/123
```

### Filtering

```text
/orders?status=Open&customerId=42
```

### Poor Implementation Leakage

```text
/database/order_table/getRow?id=123
```

This couples consumers to implementation details and makes evolution harder.

## Best Practices

- Use stable business terminology.
- Keep paths concise and predictable.
- Put resource identity in paths and optional selection criteria in query parameters when appropriate.
- Avoid sensitive information in query strings when it could leak through logs or browser history.
- Encode special characters correctly.
- Avoid unnecessary verbs in strongly resource-oriented APIs, while allowing explicit command semantics when justified.
- Define case-sensitivity and trailing-slash behavior consistently.

## Related Knowledge

- `Resource-Design.md`
- `REST-Architecture.md`
- `Request-Structure.md`
- `Filtering-Sorting-and-Searching.md`
- `Pagination.md`

## References

- RFC 3986, **Uniform Resource Identifier (URI): Generic Syntax**.
- RFC 9110, **HTTP Semantics**.

Project-specific URI naming conventions remain authoritative.
