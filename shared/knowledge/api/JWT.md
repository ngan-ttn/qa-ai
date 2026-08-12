# JWT

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

A **JSON Web Token (JWT)** is a compact, URL-safe representation of claims that can be digitally signed and, in related JOSE standards, encrypted. JWT is a token format, not an authentication or authorization protocol by itself.

## Purpose

JWT knowledge helps QA validate token claims, signature enforcement, expiry, issuer and audience checks, algorithm handling, and the distinction between readable token content and trusted token content.

## Core Concepts

### Header

The JOSE header identifies metadata such as the signing algorithm and key identifier.

### Payload / Claims

Claims can include `iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti`, and application-specific values.

### Signature

A signature protects integrity and authenticity according to the selected algorithm and key. Base64url encoding alone provides no security.

### Expiration

The `exp` claim indicates when the token must no longer be accepted.

### Audience and Issuer

`aud` and `iss` help ensure a token is used by the intended resource server and issued by a trusted authority.

### Opaque vs Self-Contained Tokens

Not all tokens are JWTs. Opaque tokens may require introspection or server-side lookup.

## How It Works

```text
Header.Payload.Signature
       ↓
Resource server parses token
       ↓
Validates signature + required claims
       ↓
Builds identity/authorization context
```

Trust comes from successful validation, not from decoding the token.

## When to Use

Use JWT knowledge when APIs accept signed JWT access tokens, identity tokens, service assertions, or other JWT-based credentials.

## When Not to Use

Do not assume every bearer token is a JWT. Do not use decoded unverified claims as trusted test evidence.

## Advantages

JWTs can carry verifiable claims without requiring a database lookup for every request, support distributed validation, and integrate with standardized identity and authorization systems.

## Limitations

JWTs can be difficult to revoke immediately, can expose readable claim data if only signed, and are vulnerable to implementation mistakes involving algorithms, keys, expiry, and claim validation.

## Examples

### Expired Token

Modify or obtain a token whose `exp` is in the past. The API should reject it even if the signature is otherwise valid.

### Wrong Audience

A token valid for Service A is sent to Service B. B should reject it if audience validation is required.

### Tampered Claim

Changing a role claim without re-signing invalidates the signature. The server must not trust the modified token.

## Best Practices

- Validate signature before trusting claims.
- Enforce allowed algorithms rather than trusting arbitrary token headers.
- Validate expiry, issuer, audience, and not-before requirements.
- Avoid storing sensitive plaintext data in signed-only JWT payloads.
- Test key rotation when architecture supports it.
- Avoid leaking tokens in logs or bug reports.
- Confirm clock-skew tolerance from policy instead of inventing one.

## Related Knowledge

- `Authentication.md`
- `Authorization.md`
- `OAuth-2.0.md`
- `API-Security-Best-Practices.md`

## References

- RFC 7519, **JSON Web Token (JWT)**.
- RFC 7515, **JSON Web Signature (JWS)**.
- RFC 8725, **JSON Web Token Best Current Practices**.

Claim requirements and trusted issuers are system-specific.
