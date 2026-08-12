# HTTP Fundamentals

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**HTTP (Hypertext Transfer Protocol)** is an application-layer protocol widely used for communication between clients and servers. HTTP defines request and response message semantics, methods, status codes, header fields, representation metadata, caching behavior, and related interaction rules.

HTTPS is HTTP carried over a secure transport using TLS. The HTTP semantics remain HTTP semantics; TLS adds confidentiality, integrity, and server authentication at the transport-security layer.

## Purpose

HTTP fundamentals help QA interpret API traffic correctly and design tests that validate protocol behavior as well as business behavior. This knowledge is especially important for REST-style APIs, web applications, browser integrations, gateways, and service-to-service HTTP communication.

## Core Concepts

### Request

An HTTP request contains a method, target URI, header fields, and optionally content.

### Response

An HTTP response contains a status code, header fields, and optionally content.

### Method Semantics

Methods such as GET, POST, PUT, PATCH, DELETE, HEAD, and OPTIONS communicate request intent. Their semantics influence safety, idempotency, caching, and expected server behavior.

### Status Codes

Status codes communicate the protocol-level outcome class. They do not replace application-specific error details.

### Headers

Headers carry metadata such as content type, authorization credentials, caching directives, conditional-request fields, correlation identifiers, and client preferences.

### Representation

A resource can be represented in formats such as JSON, XML, text, or binary content. The resource and its representation are related but not identical concepts.

### Connection and Version

HTTP/1.1, HTTP/2, and HTTP/3 differ in transport and framing behavior while preserving core HTTP semantics. Tests should focus on protocol-version-specific details only when required by the system under test.

## How It Works

A simplified HTTP exchange is:

```text
Client
  │
  │ METHOD /target HTTP
  │ headers
  │ optional body
  ▼
Server
  │
  │ status code
  │ headers
  │ optional body
  ▼
Client
```

For HTTPS, a secure TLS channel is established before HTTP messages are exchanged. Intermediaries such as proxies, load balancers, gateways, and caches may participate between client and origin server.

## When to Use

Use HTTP fundamentals when:

- testing HTTP-based APIs;
- debugging browser-network traffic;
- validating methods, headers, status codes, or content types;
- testing caching or conditional requests;
- analyzing redirects;
- checking gateway or proxy behavior;
- validating secure transport expectations.

## When Not to Use

Do not apply HTTP-specific rules directly to non-HTTP protocols such as raw messaging systems or native gRPC transport behavior without verifying the applicable protocol. Do not infer project business rules solely from HTTP conventions.

## Advantages

HTTP provides:

- standardized semantics;
- broad client and server support;
- interoperability across platforms;
- extensibility through headers and representations;
- mature tooling and observability;
- support for intermediaries, caching, and content negotiation.

## Limitations

HTTP does not by itself define:

- application business rules;
- domain-specific error schemas;
- authentication policy;
- transaction boundaries;
- retry policy;
- service-level objectives.

Distributed HTTP communication also remains subject to latency, network loss, timeouts, proxy behavior, and partial failure.

## Examples

### GET Request

```http
GET /products/123 HTTP/1.1
Accept: application/json
```

A server may return a JSON representation with `200`, a `404` when no matching resource exists, or an authorization-related status when access is restricted.

### POST Request

```http
POST /orders HTTP/1.1
Content-Type: application/json

{"productId":"P-100","quantity":2}
```

The server may validate media type, payload syntax, field constraints, permissions, and business rules before returning an outcome.

### Redirect

A `3xx` response may instruct a client to use another URI. QA should validate both the redirect response and client follow behavior when relevant.

## Best Practices

- Validate method semantics instead of checking only endpoint availability.
- Verify status code, headers, and body together.
- Distinguish malformed HTTP content from valid HTTP carrying invalid business data.
- Test relevant media types and charset handling.
- Validate authorization and sensitive-data exposure in both headers and body.
- Consider cache behavior for data that must remain current or private.
- Avoid assuming all `2xx` responses mean the same thing.
- Include timeout and intermediary behavior where architecture makes them relevant.

## Related Knowledge

- `HTTP-Methods.md` covers method-specific behavior.
- `HTTP-Status-Codes.md` explains response status semantics.
- `Headers.md` covers request and response metadata.
- `Request-Structure.md` and `Response-Structure.md` detail message composition.
- `Content-Negotiation.md` explains representation selection.
- `REST-Architecture.md` explains an architectural style commonly implemented over HTTP.

## References

- RFC 9110, **HTTP Semantics**.
- RFC 9111, **HTTP Caching**.
- RFC 9112, **HTTP/1.1**.
- RFC 9113, **HTTP/2**.
- RFC 9114, **HTTP/3**.

Project-specific behavior overrides generic expectations only when it remains valid under the applicable protocol and is documented by an authoritative source.
