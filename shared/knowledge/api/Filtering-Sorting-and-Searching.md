# Filtering, Sorting and Searching

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

Filtering, sorting, and searching allow API consumers to control which records are returned and in what order. These capabilities are common on collection endpoints but have distinct semantics.

## Purpose

This article helps QA design coverage for selection criteria, combined parameters, ordering, search syntax, invalid inputs, and interaction with pagination.

## Core Concepts

### Filtering

Filtering restricts results using exact or rule-based criteria such as status, date range, category, owner, or numeric threshold.

### Sorting

Sorting defines result order using one or more fields and directions.

### Searching

Searching usually performs text or relevance-based matching across one or more fields. Exact semantics can range from simple substring matching to tokenized or ranked search.

### Combination

APIs often allow filters, search terms, sorting, and pagination together. The composition rules should be explicit.

### Deterministic Ordering

Stable pagination requires deterministic ordering, often including a unique tie-breaker when primary sort values are equal.

### Encoding and Syntax

Special characters, repeated parameters, arrays, ranges, and operators require clear syntax and correct URI encoding.

## How It Works

```text
Base Collection
    ↓ apply filters
Candidate Set
    ↓ apply search/relevance
Matched Set
    ↓ apply sorting
Ordered Set
    ↓ paginate
Response Window
```

Actual operation order can differ by API design, but the contract should produce predictable observable behavior.

## When to Use

Use this knowledge for list endpoints, administrative searches, transaction histories, product catalogs, report filters, or any API returning selectable collections.

## When Not to Use

Do not assume database query capabilities are exposed directly through an API. A secure API should constrain supported fields and operators rather than accepting arbitrary backend query expressions.

## Advantages

These capabilities reduce transferred data, improve client usability, and allow reusable collection endpoints to serve multiple consumer needs.

## Limitations

Complex combinations can increase implementation cost, performance risk, ambiguity, and security exposure. Search relevance may also be non-deterministic unless clearly specified.

## Examples

```text
GET /orders?status=Open&sort=-createdAt&pageSize=25
```

Relevant tests include valid combinations, unsupported sort fields, invalid directions, empty search, special characters, multiple filters, date boundaries, and sorting ties.

## Best Practices

- Verify each criterion independently before combination testing.
- Test supported and unsupported fields/operators.
- Validate case sensitivity and locale behavior where specified.
- Include special characters and encoding cases.
- Verify deterministic sorting for pagination.
- Test null or missing field behavior.
- Avoid assuming fuzzy-search semantics without documentation.
- Validate authorization so filtering cannot expose otherwise inaccessible records.

## Related Knowledge

- `Pagination.md`
- `URI-Design.md`
- `Request-Structure.md`
- `Performance-Testing.md`
- `Authorization.md`

## References

- RFC 3986 for URI query syntax.
- Search and filtering semantics are API-specific and should be documented in the contract.

No universal standard defines exact filter, sort, or search parameter names across APIs.
