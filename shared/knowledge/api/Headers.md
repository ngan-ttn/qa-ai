# Headers

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

HTTP header fields carry metadata about requests, responses, representations, authentication, caching, negotiation, routing, and client or server behavior. Headers are part of the API contract whenever consumers or providers rely on them.

## Purpose

Header knowledge helps QA test metadata that may not appear in the request or response body but can materially affect authorization, caching, media types, retries, tracing, and security.

## Core Concepts

### Representation Metadata

`Content-Type` describes the media type of content. `Content-Length` can describe content size when present and applicable.

### Negotiation

`Accept`, `Accept-Language`, `Accept-Encoding`, and related fields express client preferences.

### Authentication

`Authorization` carries credentials or tokens for many authentication schemes. `WWW-Authenticate` can communicate authentication challenges.

### Caching and Conditions

Headers such as `Cache-Control`, `ETag`, `If-None-Match`, and `Last-Modified` support caching and conditional requests.

### Location and Retry Metadata

`Location` can identify a created or redirected resource. `Retry-After` can communicate when a client may retry in applicable responses.

### Custom Headers

Organizations often define headers for correlation IDs, tenant context, versioning, tracing, or idempotency. Their semantics are project-specific.

## How It Works

Headers are parsed independently of the message body and influence how the request or response is interpreted.

```text
Headers + Body
    │
    ▼
Protocol / Gateway / Application Processing
```

Intermediaries may add, remove, or transform certain headers, making end-to-end validation important when architecture depends on them.

## When to Use

Use header testing for authentication, content negotiation, caching, tracing, rate limiting, idempotency, conditional requests, redirects, CORS-related behavior, or gateway integration.

## When Not to Use

Do not assume undocumented custom headers are stable API contracts. Do not expose or log sensitive header values unnecessarily.

## Advantages

Headers allow metadata to remain separate from domain payloads and support standardized protocol behavior across different representations.

## Limitations

Headers can be altered by intermediaries, have size limits, and may be omitted by clients. Custom headers can create coupling when not governed consistently.

## Examples

```http
Authorization: Bearer <token>
Content-Type: application/json
Accept: application/json
Idempotency-Key: 9e8...
X-Correlation-ID: abc-123
```

QA can validate required presence, invalid values, unsupported values, missing values, duplication behavior, and sensitive-data exposure.

## Best Practices

- Verify headers that are contractually required, not every incidental runtime header.
- Validate header-value syntax and case-insensitive field-name handling where applicable.
- Keep secrets out of screenshots and defect descriptions.
- Test intermediary behavior for security or routing-critical headers.
- Validate `Content-Type` against actual body format.
- Test conditional and caching headers only where the API supports those semantics.

## Related Knowledge

- `HTTP-Fundamentals.md`
- `Content-Negotiation.md`
- `Authentication.md`
- `Idempotency.md`
- `Rate-Limiting.md`
- `Retry-Strategy.md`

## References

- RFC 9110, **HTTP Semantics**.
- IANA HTTP Field Name Registry.

Custom header semantics must be obtained from the target API contract.
