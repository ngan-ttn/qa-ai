# HTTP Methods

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

HTTP methods express the intended semantics of a request. Common methods include GET, POST, PUT, PATCH, DELETE, HEAD, and OPTIONS. Correct method selection affects safety, idempotency, caching, retry behavior, and client expectations.

## Purpose

This article helps QA validate whether an HTTP API uses method semantics consistently and whether implementation behavior matches the contract. It also provides a basis for negative testing, duplicate-request testing, and retry analysis.

## Core Concepts

### GET

GET retrieves a representation or information about a resource. It is defined as safe and idempotent and should not intentionally create business-side effects.

### POST

POST submits data for processing under the semantics defined by the target resource. It is commonly used for creation or commands and is not inherently idempotent.

### PUT

PUT creates or replaces the state of a target resource using the supplied representation. Equivalent repeated PUT requests are expected to have idempotent effect.

### PATCH

PATCH applies partial modification semantics defined by the API and patch document format. PATCH is not inherently idempotent, although an API can design a particular PATCH operation to be idempotent.

### DELETE

DELETE requests removal of the association represented by the target resource. DELETE is idempotent at the HTTP semantic level: repeating the same request should not create additional deletion effects.

### HEAD

HEAD is similar to GET but returns response metadata without response content.

### OPTIONS

OPTIONS asks for communication options associated with a resource or server. Browsers may use OPTIONS for CORS preflight requests.

### Safe and Idempotent

A safe method is intended for retrieval rather than state change. An idempotent method can be repeated with the same intended effect as one execution, although response status or metadata may differ between attempts.

## How It Works

The method combines with a target URI and request metadata to express intent:

```text
METHOD + Target URI + Headers + Optional Body
                 │
                 ▼
           Server Semantics
```

Method semantics guide intermediaries and clients. They also influence whether automatic retries can be safe. Business logic must still define exact outcome rules.

## When to Use

Use this knowledge when testing CRUD-style APIs, retry behavior, duplicate submissions, browser integration, caching, partial updates, or REST-oriented interfaces.

## When Not to Use

Do not infer complete business semantics from the method alone. A POST can represent many different domain actions. Do not assume every API is REST-oriented or that an unconventional method choice is automatically defective without a documented contract or standard.

## Advantages

Consistent method usage improves interoperability, predictability, cache behavior, retry safety, documentation quality, and tool compatibility.

## Limitations

HTTP methods do not define field validation, authorization, transaction boundaries, domain-specific idempotency keys, or exact response schemas. A technically idempotent operation can still have complex observable behavior through logs, notifications, or timestamps.

## Examples

### Retrieval

```http
GET /orders/123
```

QA validates retrieval without unintended order mutation.

### Full Replacement

```http
PUT /profiles/123
```

Repeating the same request should not create duplicate profiles.

### Duplicate POST

```http
POST /payments
```

Because POST is not inherently idempotent, QA should verify whether the API requires an idempotency key or another duplicate-prevention mechanism.

## Best Practices

- Validate method semantics together with URI and business behavior.
- Test repeated requests for operations documented as idempotent.
- Verify unsupported methods return an appropriate outcome.
- Check whether GET and HEAD cause unexpected persistent side effects.
- Test PATCH behavior for omitted fields, explicit nulls, and repeated patches where applicable.
- Confirm retry rules rather than assuming all methods can be retried safely.

## Related Knowledge

- `HTTP-Fundamentals.md`
- `Idempotency.md`
- `REST-Architecture.md`
- `Request-Structure.md`
- `HTTP-Status-Codes.md`

## References

- RFC 9110, **HTTP Semantics**.
- RFC 5789, **PATCH Method for HTTP**.

Project-specific method behavior must be confirmed from the API contract.
