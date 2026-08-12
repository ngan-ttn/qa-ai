# Security Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-12

## Overview

**API security testing** evaluates whether security controls behave as intended and whether common API attack paths are prevented within an authorized test scope. It includes security-focused functional testing and may extend to specialized penetration testing performed by qualified teams.

## Purpose

This article provides QA with a safe, reusable framework for validating authentication, authorization, data exposure, input handling, abuse controls, and security-sensitive error behavior.

## Core Concepts

### Authentication Testing

Verify invalid, expired, revoked, malformed, or missing credentials are handled safely.

### Authorization Testing

Verify object-level, function-level, role-level, tenant-level, and field-level restrictions.

### Data Exposure

Responses, errors, logs, and metadata should not expose data beyond policy or contract.

### Input Robustness

Unexpected input should be rejected or handled safely without revealing internals or bypassing validation.

### Abuse Resistance

Rate limits, resource limits, pagination limits, upload limits, and workflow controls can reduce automated abuse.

### Security Misconfiguration

Incorrect CORS, insecure transport, debug endpoints, overly permissive gateways, or exposed management surfaces can weaken an otherwise correct application.

### Business Logic Security

Sequence manipulation, replay, duplicate actions, state bypass, and ownership manipulation can create vulnerabilities even when input syntax is valid.

## How It Works

Security testing derives scenarios from:

```text
Assets + Trust Boundaries + Roles + API Contract + Threats
                           ↓
                  Security Test Objectives
                           ↓
              Controlled authorized execution
                           ↓
                    Evidence and findings
```

The depth of testing depends on risk and authorization.

## When to Use

Use security testing for protected APIs, sensitive data, financial operations, partner integrations, admin functions, multi-tenant systems, and pre-release security assurance.

## When Not to Use

Do not perform destructive payloads, credential attacks, denial-of-service activity, or broad scanning outside explicit authorization and agreed scope.

## Advantages

Security testing reveals defects that normal functional tests may miss and validates that security requirements hold under manipulated requests.

## Limitations

QA-focused security tests do not replace professional penetration testing, code review, threat modeling, dependency scanning, or infrastructure security assessment.

## Examples

### Object Access

Change a resource identifier to another tenant's object and verify access is denied without leaking protected data.

### Over-Posting

Send a restricted field such as `role=admin` even if the UI never sends it; verify the server rejects or ignores unauthorized modification according to the contract.

### Error Exposure

Send malformed input and confirm the error does not reveal stack traces, secrets, SQL, or internal file paths.

## Best Practices

- Obtain explicit scope before intrusive testing.
- Prioritize authorization and business-logic security.
- Test direct API requests independent of UI restrictions.
- Protect all credentials and captured traffic.
- Use safe test data and non-production environments for destructive cases.
- Map findings to concrete security requirements or recognized risk categories.
- Retest fixes and assess regression impact.
- Use OWASP API Security guidance as a checklist, not as a substitute for a threat model.

## Related Knowledge

- `API-Security-Best-Practices.md`
- `Authentication.md`
- `Authorization.md`
- `OAuth-2.0.md`
- `JWT.md`
- `Rate-Limiting.md`

## References

- OWASP API Security Top 10.
- OWASP Web Security Testing Guide.
- OWASP Authentication and Authorization Cheat Sheets.

Security acceptance criteria and permitted test techniques are organization-specific.
