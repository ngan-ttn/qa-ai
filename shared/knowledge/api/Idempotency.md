# Idempotency

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**Idempotency** means that repeating an operation produces the same intended effect on server state as performing it once. Idempotency is especially important when clients cannot know whether a timed-out request reached the server and may retry.

## Purpose

Idempotency knowledge helps QA test duplicate prevention, retry safety, payment or order submission behavior, and method semantics in distributed systems.

## Core Concepts

### HTTP Idempotent Methods

HTTP defines PUT, DELETE, and safe methods as idempotent in intended semantics. POST and PATCH are not inherently idempotent.

### Business Idempotency

An API can make a POST operation effectively idempotent using a business key, idempotency key, request fingerprint, or equivalent mechanism.

### Idempotency Key

A client-supplied key can let the server recognize equivalent retries and return the original outcome instead of repeating side effects.

### Same Effect vs Same Response

Idempotency concerns intended server effect, not necessarily byte-for-byte identical responses. Timestamps, headers, or current-state status may differ between attempts.

### Retry Window

If keys expire, the supported deduplication window must be defined. Retrying after that window may behave differently.

## How It Works

```text
Request + Idempotency Key
        │
        ▼
Server checks prior result
   │              │
 none           exists
   │              │
execute        reuse result
   │              │
store result ◄────┘
```

The exact algorithm is implementation-specific.

## When to Use

Use idempotency testing for payments, orders, bookings, provisioning, message submission, retryable API calls, and any action where duplicate side effects are costly.

## When Not to Use

Do not require idempotency for operations intentionally designed to create a new independent result on every call, unless the contract says otherwise.

## Advantages

Idempotency reduces duplicate side effects, improves retry safety, and makes distributed interactions more resilient to uncertain network outcomes.

## Limitations

Idempotency mechanisms require storage, key scoping, expiry rules, concurrency handling, and clear definition of what counts as the same request.

## Examples

### Duplicate Payment Submission

Two identical POST requests with the same idempotency key should not create two payments if the contract promises idempotency.

### Same Key, Different Payload

A robust design should define how the server reacts when the same key is reused with a different request payload.

### Concurrent Duplicates

Two requests with the same key arrive nearly simultaneously. QA verifies that race conditions do not create duplicate resources.

## Best Practices

- Test sequential and concurrent duplicate requests.
- Verify same-key/different-payload behavior.
- Test retries after client timeout.
- Confirm key scope, format, and expiry rules.
- Validate response consistency with the documented mechanism.
- Check persistence and downstream side effects, not only status codes.
- Distinguish protocol idempotency from business-level deduplication.

## Related Knowledge

- `HTTP-Methods.md`
- `Retry-Strategy.md`
- `Timeout-Handling.md`
- `Headers.md`
- `Integration-Testing.md`

## References

- RFC 9110, **HTTP Semantics**, for method idempotency.
- Industry API practices commonly use idempotency keys for non-idempotent business operations.

Key format, storage window, and duplicate-result behavior are contract-specific.
