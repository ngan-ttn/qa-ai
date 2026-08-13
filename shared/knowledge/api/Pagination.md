# Pagination

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**Pagination** divides large result sets into smaller pages or windows that clients can retrieve incrementally. Common approaches include offset/limit, page-number, cursor, keyset, and continuation-token pagination.

## Purpose

Pagination knowledge helps QA validate completeness, ordering, boundaries, navigation metadata, performance-sensitive behavior, and consistency when underlying data changes between requests.

## Core Concepts

### Page Size

The maximum or requested number of records returned in one response.

### Offset / Limit

The client requests a starting offset and count. This is simple but can become inefficient or inconsistent under frequent data changes.

### Page Number

The client requests a logical page index, usually with a page size.

### Cursor / Continuation Token

The server returns an opaque token indicating where the next page should continue. This can be more stable and efficient for changing datasets.

### Ordering

Reliable pagination requires deterministic ordering. Without it, items can move unpredictably between pages.

### Total Count

Some APIs return total records or total pages. This metadata may be expensive or may become stale during concurrent changes.

## How It Works

```text
Request page/window
      ↓
Server selects ordered subset
      ↓
Response items + navigation metadata
      ↓
Client requests next window
```

The exact parameters and response fields are contract-specific.

## When to Use

Use pagination testing for list, search, history, transaction, reporting, or catalog endpoints where result sets may exceed a single response.

## When Not to Use

Do not impose pagination on endpoints guaranteed to return a very small bounded set unless the contract requires it.

## Advantages

Pagination limits response size, reduces memory and bandwidth use, and improves client control over large datasets.

## Limitations

Concurrent inserts, deletes, or updates can cause duplicate or missing records across pages, especially with offset-based approaches. Total counts can also become inconsistent between requests.

## Examples

### Offset Pagination

```text
GET /orders?limit=50&offset=100
```

### Cursor Pagination

```text
GET /orders?cursor=eyJpZCI6...
```

### Boundary Cases

QA validates empty results, one record, exact page-size results, last partial page, page beyond range, minimum/maximum page size, invalid token, and expired token behavior.

## Best Practices

- Verify no duplicates or gaps in a stable dataset.
- Confirm deterministic ordering.
- Test first, middle, last, empty, and out-of-range pages.
- Test invalid or reused continuation tokens.
- Validate maximum page-size enforcement.
- Check filtering and sorting remain consistent across pages.
- Consider concurrent dataset changes when business requirements demand stable iteration.

## Related Knowledge

- `Filtering-Sorting-and-Searching.md`
- `Request-Structure.md`
- `Response-Structure.md`
- `URI-Design.md`
- `Performance-Testing.md`

## References

- API pagination patterns are implementation conventions rather than one universal HTTP standard.
- RFC 8288 defines Web Linking, which may be used for pagination links.

The target API contract defines the supported pagination model.
