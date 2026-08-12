# Rate Limiting

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**Rate limiting** controls how frequently a client, user, key, tenant, IP, or other identity may perform API operations within a defined period or algorithm. It protects availability, fairness, cost, and downstream capacity.

## Purpose

Rate-limit knowledge helps QA validate thresholds, identity scope, reset behavior, retry guidance, concurrency effects, and distinctions between rate limiting, quotas, and general capacity failures.

## Core Concepts

### Limit Subject

Limits may apply per user, client, key, IP, endpoint, tenant, or combination.

### Window or Algorithm

Common approaches include fixed windows, sliding windows, token buckets, and leaky buckets.

### Throttling Response

HTTP APIs commonly use `429 Too Many Requests` when a client exceeds an enforced rate policy.

### Retry Information

A response may provide `Retry-After` or provider-specific limit metadata.

### Quota

A quota usually constrains total usage over a longer period; rate limiting controls request frequency. Some systems use the terms interchangeably.

## How It Works

```text
Incoming request
      ↓
Identify limit bucket
      ↓
Check available capacity
   ↙          ↘
allow        reject/throttle
```

Distributed enforcement may involve gateways or shared counters.

## When to Use

Use rate-limit testing for public APIs, partner integrations, authentication endpoints, expensive operations, abuse-sensitive APIs, or systems with documented traffic controls.

## When Not to Use

Do not load-test production systems or intentionally trigger broad denial-of-service effects without explicit authorization and safe test controls.

## Advantages

Rate limiting protects stability, controls abuse, supports fairness, and prevents individual consumers from exhausting shared capacity.

## Limitations

Incorrect limits can reject legitimate traffic, distributed counters may be approximate, and clients can behave poorly if retry guidance is unclear.

## Examples

### Threshold Boundary

If a documented limit is N requests per window, QA validates behavior at N and N+1 using an approved test environment.

### Identity Isolation

One client's exhaustion should not incorrectly block another client when limits are defined per client.

### Reset

After the defined window or token replenishment, requests become available again according to policy.

## Best Practices

- Test exact documented boundaries in safe environments.
- Confirm which identity dimensions share a bucket.
- Validate `429` and retry metadata where specified.
- Test burst versus sustained patterns when relevant.
- Verify sensitive endpoints may have different limits.
- Avoid making assumptions about exact algorithms from externally observed timing alone.
- Coordinate performance-style testing to prevent environment disruption.

## Related Knowledge

- `HTTP-Status-Codes.md`
- `Retry-Strategy.md`
- `API-Keys.md`
- `Performance-Testing.md`
- `API-Security-Best-Practices.md`

## References

- RFC 6585 defines `429 Too Many Requests`.
- RFC 9110 defines `Retry-After` semantics.

Rate thresholds and enforcement identity are contract-specific.
