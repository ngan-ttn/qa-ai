# OAuth 2.0

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**OAuth 2.0** is an authorization framework that allows a client to obtain limited access to protected resources, typically using access tokens issued by an authorization server. OAuth 2.0 is primarily about delegated authorization; it is not by itself an end-user authentication protocol.

## Purpose

OAuth knowledge helps QA validate token issuance, scopes, redirect behavior, client identity, token expiry, refresh behavior, and protected-resource access without confusing OAuth with identity proof.

## Core Concepts

### Resource Owner

The entity capable of granting access to a protected resource.

### Client

The application requesting access.

### Authorization Server

The server that authenticates relevant parties and issues tokens according to policy.

### Resource Server

The API that accepts and validates access tokens.

### Access Token

A credential used to access protected resources.

### Refresh Token

A credential that may be exchanged for a new access token without repeating the full authorization interaction.

### Scope

Scopes describe requested or granted delegated access dimensions.

### Authorization Code Flow

A common browser-based flow redirects the user to an authorization server, returns an authorization code to the client, and exchanges the code for tokens. Public clients commonly use PKCE.

## How It Works

```text
Client → Authorization Server: authorization request
User / policy grants access
Client ← authorization code
Client → token endpoint: code exchange
Client ← access token
Client → Resource Server: access token
```

Exact security requirements vary by client type and profile.

## When to Use

Use OAuth knowledge for SSO-adjacent integrations, partner APIs, delegated access, mobile/web authorization flows, token scopes, refresh tokens, and third-party resource access.

## When Not to Use

Do not treat OAuth access tokens as proof of an authenticated end-user identity unless the system uses an identity layer such as OpenID Connect and the contract says so.

## Advantages

OAuth supports delegated access, limited scopes, token lifetimes, separation between client credentials and user credentials, and standardized authorization flows.

## Limitations

OAuth deployments are configuration-sensitive. Redirect URI mistakes, token leakage, weak client handling, over-broad scopes, and poor refresh-token protection can create serious risks.

## Examples

### Scope Restriction

A token with `orders:read` is used on an order-update endpoint. QA verifies that read scope does not grant write access.

### Expired Access Token

The resource server rejects an expired token and the client follows the intended refresh or reauthorization path.

### Redirect URI Manipulation

QA validates that unauthorized redirect URIs are rejected according to the registered client configuration.

## Best Practices

- Test scope boundaries and least privilege.
- Validate token expiry and refresh behavior.
- Verify redirect URI restrictions.
- Test authorization-code replay prevention.
- Validate PKCE for applicable public clients.
- Protect tokens in logs, screenshots, browser storage, and test artifacts.
- Verify audience and issuer checks when access tokens include those claims.
- Test revocation or session termination only according to supported provider behavior.

## Related Knowledge

- `Authentication.md`
- `Authorization.md`
- `JWT.md`
- `API-Security-Best-Practices.md`
- `Cookies.md`

## References

- RFC 6749, **The OAuth 2.0 Authorization Framework**.
- RFC 7636, **Proof Key for Code Exchange (PKCE)**.
- RFC 9700, **Best Current Practice for OAuth 2.0 Security**.

Provider-specific flows and scopes must be taken from the target authorization-server configuration.
