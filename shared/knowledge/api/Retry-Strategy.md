# Retry Strategy

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

A **retry strategy** defines when and how a client repeats an API operation after a failure or uncertain outcome. Safe retry design must consider whether the operation is idempotent, whether the failure is transient, how long to wait, and whether retrying could amplify an outage.

## Purpose

Retry knowledge helps QA test resilience without creating duplicate business actions or unrealistic expectations about transient failures.

## Core Concepts

### Transient Failure

A failure is transient when a later attempt may succeed without changing the request, such as temporary unavailability or some network interruptions.

### Permanent Failure

Validation errors, authorization failures, and many business-rule failures generally should not be retried unchanged.

### Backoff

Clients often wait increasingly longer between retries. Exponential backoff reduces repeated pressure on an unhealthy dependency.

### Jitter

Random variation reduces synchronized retry storms across many clients.

### Retry-After

A server may provide explicit retry guidance through `Retry-After` or provider-specific metadata.

### Retry Budget

A retry policy should cap attempts or total elapsed time.

### Idempotency

Retrying a non-idempotent action can create duplicate side effects unless the API provides a deduplication mechanism.

## How It Works

```text
Request fails
    ↓
Classify failure
    ↓
Is retry safe and allowed?
  ↙                ↘
 no                 yes
stop           wait/backoff
                    ↓
                 retry
```

Client and server policies may both influence the final behavior.

## When to Use

Use retry testing for service-to-service calls, asynchronous workers, payment/order submission with idempotency controls, rate limiting, temporary unavailability, and network resilience.

## When Not to Use

Do not automatically retry validation errors, permission failures, or non-idempotent operations unless the contract defines a safe mechanism. Do not generate high-volume retries against unstable production systems during testing.

## Advantages

Controlled retries improve resilience to brief network or dependency failures and can reduce user-visible errors.

## Limitations

Poor retry design can cause duplicate operations, retry storms, increased latency, cascading failures, and hidden reliability problems.

## Examples

### 503 with Retry Guidance

The API returns temporary unavailability and a retry hint. QA validates that the client waits as specified rather than retrying immediately in a tight loop.

### Timeout After POST

The client does not know whether the server created the order. A safe retry requires idempotency or another reconciliation mechanism.

### 400 Validation Error

The same invalid request should not be retried unchanged.

## Best Practices

- Classify retryable conditions explicitly.
- Combine retries with timeouts and idempotency controls.
- Cap retry count or elapsed time.
- Use backoff and jitter for distributed clients.
- Respect server retry guidance where defined.
- Test duplicate-side-effect risk.
- Verify retry behavior under concurrent failures.
- Preserve original correlation context when observability requires it.

## Related Knowledge

- `Idempotency.md`
- `Timeout-Handling.md`
- `HTTP-Status-Codes.md`
- `Rate-Limiting.md`
- `Integration-Testing.md`

## References

- RFC 9110 for `Retry-After` semantics.
- Distributed-systems resilience practices for bounded exponential backoff and jitter.

Exact retryable statuses and timing values must come from project policy.
