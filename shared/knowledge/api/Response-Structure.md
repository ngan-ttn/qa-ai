# Response Structure

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

An HTTP response communicates the result of a request through a status code, header fields, and optional content. Correct testing evaluates these elements together rather than checking only response data or only the status code.

## Purpose

This article provides a systematic model for validating API responses, including success outcomes, errors, metadata, representations, and protocol behavior.

## Core Concepts

### Status Code

The status code communicates the HTTP outcome class and more specific protocol semantics.

### Headers

Response headers may describe content type, caching, location, authentication challenges, rate limits, pagination links, correlation identifiers, or retry information.

### Response Content

A response body may contain a resource representation, operation result, error object, binary payload, or no content.

### Schema

Structured responses often follow a defined schema. QA can validate required fields, types, nullability, enumeration values, nesting, and backward compatibility.

### Business Outcome

A protocol-level success does not necessarily prove the business result is correct. The returned data and side effects must be validated against requirements.

## How It Works

```text
Request processed
      │
      ├── determine HTTP outcome
      ├── create headers
      ├── serialize representation/error
      ▼
HTTP Response
      │
      ▼
Consumer interprets result
```

Clients may use status code, headers, and body together to decide the next action.

## When to Use

Use this knowledge when validating API contracts, frontend-backend integration, error handling, content negotiation, pagination, caching, rate limiting, redirects, or schema compatibility.

## When Not to Use

Do not infer database correctness or downstream completion solely from a syntactically valid response. For asynchronous operations, an accepted response may indicate only that work was queued.

## Advantages

Response-structure validation detects interface defects early and provides clear evidence for consumer compatibility problems.

## Limitations

A response may be correct while hidden side effects are wrong. Conversely, business data may be correct while protocol metadata is defective. Both require separate verification.

## Examples

### Created Resource

```http
HTTP/1.1 201 Created
Location: /orders/123
Content-Type: application/json

{"id":"123","status":"Created"}
```

QA validates status, `Location`, media type, body schema, returned values, and resource persistence.

### No Content

```http
HTTP/1.1 204 No Content
```

A 204 response must not depend on a response body for required information.

## Best Practices

- Validate status, headers, schema, field values, and side effects.
- Check consistency between status code and error or success body.
- Verify no sensitive internal information leaks in errors.
- Validate content type against actual content.
- Test optional and newly added response fields for compatibility.
- Verify asynchronous acknowledgements separately from eventual completion.
- Use contract validation where machine-readable schemas are available.

## Related Knowledge

- `HTTP-Status-Codes.md`
- `Headers.md`
- `Error-Response-Design.md`
- `Content-Negotiation.md`
- `Contract-Testing.md`

## References

- RFC 9110, **HTTP Semantics**.
- OpenAPI Specification for response descriptions and schemas.

Project-specific response fields and business outcomes must come from the authoritative API specification.
