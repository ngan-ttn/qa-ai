# Authorization

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**Authorization** determines whether an authenticated or otherwise identified principal is allowed to perform an action on a resource. Authorization can depend on roles, permissions, ownership, attributes, scopes, relationships, tenant boundaries, resource state, or policy rules.

## Purpose

Authorization knowledge helps QA validate access-control decisions systematically and detect horizontal privilege escalation, vertical privilege escalation, tenant leakage, and missing action-level restrictions.

## Core Concepts

### Subject, Action, Resource

A common authorization model evaluates whether a **subject** may perform an **action** on a **resource**.

### Role-Based Access Control

RBAC assigns permissions through roles.

### Attribute-Based Access Control

ABAC evaluates attributes of the user, resource, environment, and action.

### Ownership and Relationship

Access may depend on whether the caller owns or is related to the target resource.

### Scope

OAuth and similar systems can express delegated permissions through scopes, but scopes are only one input to authorization.

### Least Privilege

Principals should receive only the permissions needed for intended responsibilities.

### Deny by Default

When no rule grants access, secure systems commonly deny the action.

## How It Works

```text
Authenticated identity
      +
Requested action/resource
      +
Roles/scopes/attributes/policy
      ↓
Authorization decision
      ↓
Allow or Deny
```

Authorization may be enforced in gateways, services, domain logic, databases, or multiple layers.

## When to Use

Use authorization testing for role-based systems, multi-tenant APIs, admin functions, ownership rules, approval workflows, restricted fields, resource-level access, and delegated-access APIs.

## When Not to Use

Do not assume a valid token proves authorization. Do not rely solely on UI-hidden controls; manipulated direct API calls must also be evaluated.

## Advantages

Correct authorization protects data and operations, enforces separation of duties, and limits damage from compromised identities.

## Limitations

Complex policies can be difficult to reason about and may become inconsistent across services. Distributed authorization also requires reliable identity and policy context propagation.

## Examples

### Horizontal Access

User A requests `/users/B/orders`. QA verifies whether A is permitted to access B's data rather than checking only that A is logged in.

### Vertical Access

A standard user directly calls an admin-only endpoint. The server must enforce the restriction even if the UI never exposes the control.

### Field-Level Restriction

A role may read a record but be forbidden from changing approval status. QA validates action- and field-level policy.

## Best Practices

- Build positive and negative coverage for each role or policy dimension.
- Test direct-object-reference manipulation.
- Verify tenant isolation.
- Test state-dependent permissions where lifecycle matters.
- Distinguish unauthenticated from unauthorized outcomes.
- Validate both collection and item endpoints.
- Include export, bulk, search, and nested-resource paths, not only primary CRUD endpoints.
- Treat UI visibility as convenience, not enforcement.

## Related Knowledge

- `Authentication.md`
- `OAuth-2.0.md`
- `JWT.md`
- `API-Security-Best-Practices.md`
- `Security-Testing.md`
- `../domain/Eligibility-Rules.md`

## References

- OWASP Authorization Cheat Sheet.
- OWASP API Security Top 10 guidance on object-level and function-level authorization.

Project-specific roles, scopes, and policy rules must come from authoritative access-control requirements.
