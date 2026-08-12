# Authentication

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**Authentication** is the process of establishing or verifying the identity of a user, service, device, or other principal. In API systems, authentication commonly relies on credentials such as passwords, session identifiers, API keys, signed tokens, client certificates, or delegated authorization flows.

Authentication answers **who is the caller?** It is distinct from authorization, which determines what that caller may do.

## Purpose

Authentication knowledge helps QA validate login or token issuance, credential handling, session lifecycle, failure behavior, expiration, revocation, and identity propagation across service boundaries.

## Core Concepts

### Principal

The entity whose identity is being established.

### Credential

Evidence used to authenticate a principal, such as a password, token, certificate, secret, or signed assertion.

### Authentication Factor

Factors are commonly categorized as knowledge, possession, or inherence. Multi-factor authentication combines independent factors.

### Session

A session can preserve authenticated state across requests, often through a cookie or token.

### Token

A token represents authentication or authorization state. Tokens may be opaque or self-contained and may have expiration, scope, audience, issuer, and revocation semantics.

### Expiration and Revocation

Expiration limits credential lifetime. Revocation invalidates a credential before its natural expiry when supported.

### Authentication vs Authorization

Successful authentication does not imply permission to access every resource.

## How It Works

A simplified token-based flow is:

```text
Caller presents credential
        ↓
Authentication service validates identity
        ↓
Session/token issued
        ↓
Caller sends credential/token on later requests
        ↓
API validates authentication state
```

The exact flow depends on the authentication mechanism.

## When to Use

Use this knowledge for login APIs, SSO, session handling, access-token use, service-to-service authentication, credential rotation, logout, token expiry, and unauthorized-request testing.

## When Not to Use

Do not use authentication testing as a substitute for authorization testing. A caller can be correctly authenticated yet incorrectly granted access.

## Advantages

Strong authentication establishes trustworthy identity context, supports accountability, and enables downstream access-control decisions.

## Limitations

Authentication can be undermined by credential theft, replay, insecure storage, weak recovery flows, poor revocation, or excessive credential lifetime. Authentication alone does not enforce least privilege.

## Examples

### Missing Credential

A protected endpoint is called without credentials. QA verifies the documented unauthenticated outcome.

### Expired Token

A previously valid token expires. The API should reject it according to policy and avoid treating it as a valid identity.

### Logout

QA verifies that logout invalidates or otherwise terminates the credential/session as required, not merely that the UI redirects.

## Best Practices

- Test valid, missing, malformed, expired, revoked, and wrong-audience credentials where applicable.
- Separate authentication failure from authorization failure.
- Verify credentials are protected in transit and not leaked in logs or error messages.
- Test session termination and credential rotation according to requirements.
- Validate clock-sensitive behavior around expiry boundaries.
- Avoid using production credentials in test evidence.
- Confirm identity propagation across service boundaries when downstream authorization depends on it.

## Related Knowledge

- `Authorization.md`
- `OAuth-2.0.md`
- `JWT.md`
- `API-Keys.md`
- `Cookies.md`
- `API-Security-Best-Practices.md`

## References

- OWASP Authentication Cheat Sheet.
- OAuth 2.0 and OpenID Connect specifications where applicable.
- RFC 9110 for HTTP authentication framework semantics.

The target system's identity architecture and credential policy remain authoritative.
