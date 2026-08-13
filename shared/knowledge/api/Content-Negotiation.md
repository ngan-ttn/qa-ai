# Content Negotiation

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**Content negotiation** is the process by which an HTTP client and server select an appropriate representation based on metadata such as media type, language, or content encoding. API testing most commonly focuses on media-type negotiation through `Accept` and `Content-Type`.

## Purpose

This article helps QA distinguish the media type a client sends from the representation it is willing to receive and validate behavior for supported, unsupported, and ambiguous combinations.

## Core Concepts

### Content-Type

`Content-Type` describes the media type of the message content being sent.

### Accept

`Accept` describes media types the client is willing to receive, optionally with preferences.

### Representation

The same conceptual resource can have multiple representations, such as JSON or XML.

### Server-Driven Negotiation

The server selects a representation based on request preferences and available representations.

### Unsupported Media Type

A server may reject a request body whose media type it does not support.

### Not Acceptable

A server may reject a request when it cannot produce a representation acceptable to the client.

## How It Works

```text
Client
Accept: application/json
        │
        ▼
Server available representations
        │
        ▼
Select representation
        │
        ▼
Content-Type: application/json
```

Request-body media type is evaluated separately from response preference.

## When to Use

Use content-negotiation testing when an API supports multiple media types, languages, encodings, file formats, or strict request content types.

## When Not to Use

Do not create unnecessary negotiation scenarios when the API contract explicitly supports only one fixed representation and ignores optional preference headers by design.

## Advantages

Negotiation enables flexible representation formats without requiring separate resource identifiers for every format.

## Limitations

Multiple representations increase implementation, caching, documentation, and test complexity. Intermediaries may also affect caching when representation choice varies by headers.

## Examples

### Supported Request and Response

```http
Content-Type: application/json
Accept: application/json
```

### Unsupported Request Media Type

```http
Content-Type: application/xml
```

If XML is unsupported, QA validates the documented error outcome.

### Unsupported Response Preference

```http
Accept: application/pdf
```

If the endpoint cannot produce PDF, the server should follow its documented HTTP behavior rather than silently returning an unrelated representation when strict negotiation is required.

## Best Practices

- Test `Content-Type` and `Accept` independently.
- Verify actual body format matches the returned `Content-Type`.
- Test missing headers only according to documented defaults.
- Include charset behavior where text encoding matters.
- Validate fallback rules and quality preferences if supported.
- Consider cache variation when multiple representations exist.

## Related Knowledge

- `Headers.md`
- `Request-Structure.md`
- `Response-Structure.md`
- `HTTP-Status-Codes.md`

## References

- RFC 9110, **HTTP Semantics**.
- IANA Media Types registry.

Supported representations and defaults are contract-specific and must be verified from the target API documentation.
