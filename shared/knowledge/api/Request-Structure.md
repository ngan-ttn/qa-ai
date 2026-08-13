# Request Structure

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

An HTTP API request combines a method, target URI, header fields, and optionally content. Query parameters, path parameters, cookies, and authentication metadata may also contribute to request meaning.

## Purpose

Understanding request structure enables QA to systematically validate how an API interprets inputs, rejects malformed requests, handles optional fields, and distinguishes transport metadata from business data.

## Core Concepts

### Method

The HTTP method communicates operation intent.

### Target URI

The URI identifies the target resource or operation. It may contain path segments and query parameters.

### Path Parameters

Path parameters commonly identify a resource or hierarchy, for example `/orders/{orderId}`.

### Query Parameters

Query parameters commonly express filtering, pagination, sorting, search, projection, or optional behavior.

### Headers

Headers carry metadata such as authorization, content type, accepted response types, correlation IDs, caching directives, and conditional-request values.

### Request Content

A request body may contain JSON, XML, form data, multipart content, binary data, or another representation. Content rules are defined by media type and API contract.

### Cookies

Cookies can carry session or preference information where the architecture uses them.

## How It Works

```text
Method      POST
Target      /orders?source=mobile
Headers     Content-Type, Authorization, ...
Body        { ... }
                 │
                 ▼
        Request Parsing
                 │
        Validation / Auth
                 │
                 ▼
          Business Logic
```

A server can reject a request before domain processing if the request is malformed, uses an unsupported media type, lacks required credentials, or violates interface constraints.

## When to Use

Use this knowledge for API functional testing, negative testing, security-focused input validation, schema validation, pagination/filter testing, multipart upload testing, or defect analysis involving malformed requests.

## When Not to Use

Do not assume every API puts the same data in the same location. A value placed in a path in one API may be a query parameter or body field in another. Follow the published contract.

## Advantages

Structured request analysis improves test completeness by separating method, URI, headers, and content into independently testable dimensions.

## Limitations

Request structure alone does not reveal business meaning, authorization policy, persistence behavior, or downstream side effects.

## Examples

```http
POST /orders?notify=true
Content-Type: application/json
Authorization: Bearer <token>

{"productId":"P100","quantity":2}
```

Relevant tests include missing authorization, unsupported content type, invalid JSON, missing required fields, invalid quantity, unknown product, duplicate submission, and `notify` parameter behavior.

## Best Practices

- Test required, optional, omitted, null, empty, malformed, and boundary inputs according to the contract.
- Validate path and query parameter encoding.
- Check duplicate parameter handling when relevant.
- Verify media-type and charset expectations.
- Keep authentication tests distinct from business validation tests when possible.
- Test manipulated requests independently of client-side validation.
- Avoid sending secrets in query strings unless the API explicitly requires a safe mechanism.

## Related Knowledge

- `HTTP-Methods.md`
- `Headers.md`
- `Content-Negotiation.md`
- `Authentication.md`
- `Pagination.md`
- `Filtering-Sorting-and-Searching.md`

## References

- RFC 9110, **HTTP Semantics**.
- RFC 3986, **Uniform Resource Identifier (URI): Generic Syntax**.
- Media-type specifications applicable to the request format.

The API contract remains authoritative for field location and validation rules.
