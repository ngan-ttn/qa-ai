# API Keys

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

An **API key** is a credential value used to identify or authenticate an API consumer, application, project, or integration. API keys are simple and widely used, but they generally provide weaker identity and delegation semantics than modern token-based mechanisms.

## Purpose

This article helps QA validate key issuance, usage, revocation, scope, rotation, leakage resistance, and failure behavior.

## Core Concepts

### Key Identity

A key may identify an application rather than an individual user.

### Secret Value

Possession of the key may be sufficient to call an API, so the key must be treated as a secret when it grants access.

### Scope and Restriction

Keys can be limited by endpoint, environment, origin, IP range, tenant, quota, or other policy.

### Rotation

Keys should support replacement without unnecessary downtime where operational policy requires it.

### Revocation

A compromised or obsolete key should be invalidatable.

## How It Works

```text
Client sends API key
       ↓
Gateway/service validates key
       ↓
Resolve consumer + policy
       ↓
Allow, throttle, or reject request
```

Keys may be sent in headers, but exact placement is contract-specific.

## When to Use

Use API-key knowledge for service integrations, partner APIs, low-complexity machine clients, metering, quotas, or systems where keys are an approved credential type.

## When Not to Use

Do not assume API keys are sufficient for high-risk user authorization or delegated access. Do not place secrets in query strings unless a documented system requirement explicitly accepts the associated exposure risk.

## Advantages

API keys are simple to issue, integrate, rotate, and meter. They work well for identifying applications or projects.

## Limitations

They can be copied, leaked, replayed, or shared. They often lack user identity, fine-grained delegation, short-lived expiry, and strong proof-of-possession.

## Examples

### Missing Key

A protected endpoint is called without a key. QA validates the documented rejection.

### Revoked Key

A revoked key must no longer grant access after the revocation propagation window defined by the system.

### Wrong Environment

A test-environment key is used against production and should be rejected if environments are isolated.

## Best Practices

- Never expose real keys in logs, screenshots, repositories, or shared test cases.
- Test invalid, missing, expired, revoked, and restricted keys.
- Validate rate-limit and quota association where keys drive metering.
- Test rotation if dual-key or overlap behavior is supported.
- Prefer secure headers over URLs for secret transmission.
- Distinguish application identity from end-user authorization.

## Related Knowledge

- `Authentication.md`
- `Authorization.md`
- `Rate-Limiting.md`
- `API-Security-Best-Practices.md`
- `Headers.md`

## References

- OWASP API Security guidance.
- Provider-specific API-key security recommendations.

Key format, placement, scope, and rotation policy are project-specific.
