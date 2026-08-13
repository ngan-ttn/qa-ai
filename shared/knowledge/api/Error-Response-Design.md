# Error Response Design

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**Error response design** defines how an API communicates unsuccessful outcomes in a structured, predictable, and safe way. A useful error response complements the HTTP status code with machine-readable and human-readable details needed by consumers.

## Purpose

This knowledge helps QA evaluate error consistency, field-level validation errors, business error codes, traceability, localization concerns, and sensitive-information exposure.

## Core Concepts

### HTTP Status

The status code communicates the protocol outcome category.

### Error Code

A stable application-level error code helps clients distinguish domain-specific conditions without parsing free-form messages.

### Message

A human-readable message explains the problem. Clients should not depend on mutable message wording when a stable error code exists.

### Field Errors

Validation failures may identify affected fields, reasons, and rejected constraints.

### Correlation Identifier

A trace or correlation ID can help support teams locate server-side evidence without exposing internal stack traces.

### Problem Details

Standards such as Problem Details for HTTP APIs define reusable fields for machine-readable errors.

### Security

Errors should avoid exposing secrets, credentials, stack traces, internal paths, SQL fragments, or unnecessary personal data.

## How It Works

```text
Failure detected
      ↓
Map to HTTP status
      ↓
Map to stable application error
      ↓
Build safe response
      ↓
Client handles condition
```

The error contract should remain consistent across endpoints where practical.

## When to Use

Use error-response knowledge when testing validation, business rules, authorization, conflicts, dependencies, unsupported operations, or consumer-facing failure handling.

## When Not to Use

Do not require verbose error detail for security-sensitive conditions where additional information would help attackers. The correct level of detail depends on the threat model and consumer needs.

## Advantages

Consistent errors improve client reliability, automation, support diagnostics, and testability.

## Limitations

Overly detailed errors can leak sensitive implementation information. Highly generic errors, however, make troubleshooting and consumer handling difficult.

## Examples

```json
{
  "code": "ORDER_NOT_EDITABLE",
  "message": "The order cannot be edited in its current state.",
  "correlationId": "abc-123"
}
```

For validation, an API may include structured field errors rather than returning only one free-form message.

## Best Practices

- Keep application error codes stable and documented.
- Make status code and error body semantically consistent.
- Avoid exposing stack traces or secrets.
- Include correlation identifiers where observability supports them.
- Test multiple simultaneous validation errors if the contract supports them.
- Verify unknown internal failures degrade to safe generic errors.
- Distinguish client-correctable errors from transient server failures.
- Consider localization only if the contract promises localized messages.

## Related Knowledge

- `HTTP-Status-Codes.md`
- `Response-Structure.md`
- `API-Security-Best-Practices.md`
- `Retry-Strategy.md`
- `Contract-Testing.md`

## References

- RFC 9457, **Problem Details for HTTP APIs**.
- OWASP guidance on error handling and information exposure.

Error codes and message requirements are project-specific.
