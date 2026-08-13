# Security Compliance

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Security compliance** concerns satisfying applicable security requirements and control frameworks through implemented controls and evidence.

## Purpose

Help QA connect functional behavior to approved security controls without replacing security assessment or penetration testing.

## Core Concepts

### Control Objective
Security outcome a requirement intends to achieve.
### Preventive Control
Attempts to stop undesired action.
### Detective Control
Identifies relevant events or failures.
### Corrective Control
Supports recovery or remediation.
### Evidence
Demonstrates control operation.

## How It Works

Approved security requirements map to controls across identity, access, data handling, logging, configuration, and operations; QA verifies in-scope observable behavior.

## When to Use

Use for authentication/authorization requirements, audit, secure configuration, sensitive data, and regulated products.

## When Not to Use

Do not claim security certification or perform intrusive testing without authorization.

## Advantages

Improves traceability between security requirements and functional evidence.

## Limitations

Many controls are infrastructure/process-level and outside normal functional QA scope.

## Examples

A privileged action may require role authorization and auditable evidence; QA validates permitted/denied behavior and logging according to approved requirements.

## Best Practices

- Test least-privilege behavior.
- Verify denial paths and no unintended state change.
- Check audit evidence.
- Protect secrets and test data.
- Escalate specialist security testing appropriately.

## Related Knowledge

- `Compliance.md`
- `Audit-Trail.md`
- `Data-Privacy.md`
- `../api/API-Security-Best-Practices.md`

## References

- Applicable security frameworks and approved organizational controls.