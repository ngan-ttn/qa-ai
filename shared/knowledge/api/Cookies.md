# Cookies

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

HTTP cookies are small name-value data items that a server can ask a user agent to store and return in subsequent requests under defined scope rules. Cookies are commonly used for web sessions, preferences, anti-CSRF patterns, and state correlation.

## Purpose

Cookie knowledge helps QA validate browser-oriented authentication and session behavior, logout behavior, expiration, domain/path scope, and security attributes.

## Core Concepts

### Set-Cookie

A server sends `Set-Cookie` to create or update a cookie.

### Cookie

A user agent sends applicable cookies back using the `Cookie` request header.

### Scope

Domain and Path attributes influence where a cookie is sent.

### Expiration

Cookies may be session cookies or persistent cookies with `Expires` or `Max-Age`.

### Secure

The `Secure` attribute restricts transmission to secure contexts.

### HttpOnly

`HttpOnly` limits script access and helps reduce some token-theft risks from client-side script execution.

### SameSite

`SameSite` influences cross-site cookie sending and is important for CSRF risk management and federated flows.

## How It Works

```text
Server response
  Set-Cookie: session=...
        │
        ▼
Browser stores cookie
        │
        ▼
Later matching request
  Cookie: session=...
```

The browser applies cookie scope and security rules automatically. Application logout commonly invalidates the server-side session and may also expire the browser cookie.

## When to Use

Use cookie testing for browser sessions, SSO-backed web applications, logout, remember-me behavior, CSRF protection, multi-domain applications, and session expiration.

## When Not to Use

Do not assume all API authentication uses cookies. Mobile and service-to-service APIs often use authorization headers or other mechanisms.

## Advantages

Cookies integrate naturally with browsers and provide standardized scope, persistence, and security attributes.

## Limitations

Cookie-based state can introduce CSRF risk, browser-policy differences, cross-domain complexity, and debugging confusion. A cookie remaining in storage after logout may or may not represent a security problem depending on whether its server-side credential is still valid.

## Examples

### Session Cookie

```http
Set-Cookie: session=<opaque>; Secure; HttpOnly; SameSite=Lax; Path=/
```

QA validates login creation, authenticated use, expiry, logout invalidation, and behavior after token/session revocation.

### Logout

A robust logout test verifies both client-visible cookie handling and whether replaying the old session credential still grants access.

## Best Practices

- Validate session invalidation, not only cookie deletion.
- Check `Secure`, `HttpOnly`, `SameSite`, Domain, and Path against intended security policy.
- Test expiration and idle/session timeout requirements.
- Verify cross-site or SSO flows in supported browsers.
- Never include real session values in shared defect reports.
- Test whether stale cookies are safely rejected after logout or revocation.

## Related Knowledge

- `Authentication.md`
- `Authorization.md`
- `Headers.md`
- `API-Security-Best-Practices.md`
- `OAuth-2.0.md`

## References

- RFC 6265 and subsequent cookie updates.
- OWASP guidance on session management and CSRF prevention.

Cookie policy and session invalidation requirements must come from the target application security design.
