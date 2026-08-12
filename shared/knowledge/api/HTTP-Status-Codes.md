# HTTP Status Codes

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

HTTP status codes communicate the protocol-level outcome of an HTTP request. They are grouped into informational `1xx`, successful `2xx`, redirection `3xx`, client-error `4xx`, and server-error `5xx` classes.

A status code should be interpreted together with method semantics, response headers, response content, and the API contract.

## Purpose

Status-code knowledge helps QA validate whether APIs communicate outcomes consistently and distinguish malformed requests, authentication failures, authorization failures, missing resources, conflicts, rate limits, and server failures.

## Core Concepts

### 2xx Success

Common examples include `200 OK`, `201 Created`, `202 Accepted`, and `204 No Content`.

### 3xx Redirection

Redirect responses indicate another location or conditional outcome. Browser behavior may automatically follow redirects, so raw API traffic should be examined when redirect semantics matter.

### 4xx Client Error

These indicate that the request cannot be fulfilled under current client-supplied conditions. Examples include `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `409 Conflict`, `415 Unsupported Media Type`, `422 Unprocessable Content`, and `429 Too Many Requests`.

### 5xx Server Error

These indicate server-side inability to fulfill an otherwise valid request, such as `500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable`, or `504 Gateway Timeout`.

### Status vs Business Error

A successful HTTP response can still contain a business-level result such as a completed operation with warnings. Conversely, an application should not hide protocol errors behind a universal `200` unless that is an intentional and documented contract.

## How It Works

```text
Request Processing Outcome
        ↓
Select HTTP status semantics
        ↓
Attach headers and body
        ↓
Client decides next action
```

The same business problem can map differently across APIs, but mappings should be internally consistent and documented.

## When to Use

Use status-code knowledge for functional API testing, negative testing, retry analysis, gateway behavior, authentication/authorization checks, asynchronous APIs, and error-contract review.

## When Not to Use

Do not assert a specific status code solely because it is common industry practice when the target API contract explicitly defines another valid behavior. Also do not rely on status code alone to validate business outcome.

## Advantages

Standardized status semantics improve interoperability, client behavior, observability, and error handling.

## Limitations

Status codes are intentionally broad and do not carry full business-error detail. Different APIs may choose different valid mappings for similar domain conditions.

## Examples

### Created

`201 Created` may be accompanied by a `Location` header identifying the new resource.

### Accepted

`202 Accepted` indicates that processing has been accepted but may not be complete. QA must validate eventual completion separately.

### Conflict

`409 Conflict` can represent a state conflict such as trying to create a duplicate unique resource or update a stale version, depending on the contract.

### Rate Limit

`429 Too Many Requests` commonly signals that the caller exceeded an enforced rate policy.

## Best Practices

- Validate status code, headers, body, and side effects together.
- Distinguish `401` authentication problems from `403` authorization denial according to the contract.
- Check success variants such as `201`, `202`, and `204`, not only `200`.
- Verify gateway-generated `5xx` errors are handled consistently.
- Test unsupported media type and invalid content separately.
- Use error codes in the response body for domain-specific precision when the API defines them.

## Related Knowledge

- `Response-Structure.md`
- `Error-Response-Design.md`
- `Retry-Strategy.md`
- `Timeout-Handling.md`
- `Rate-Limiting.md`

## References

- RFC 9110, **HTTP Semantics**.
- RFC 6585, **Additional HTTP Status Codes**.

The target API specification remains authoritative for domain-to-status mappings.
