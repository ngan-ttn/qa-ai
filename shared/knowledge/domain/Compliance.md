# Compliance

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Compliance** is the state and practice of meeting applicable external obligations and internal policies through defined controls, evidence, governance, and remediation.

## Purpose

Provide QA a control-oriented model for verifying implemented requirements without substituting for legal, security, or audit judgment.

## Core Concepts

### Requirement
The obligation to satisfy.
### Control
A measure intended to satisfy or reduce risk related to the requirement.
### Evidence
Records showing the control operated.
### Exception
Known deviation requiring governance.
### Remediation
Action to correct control failure.

## How It Works

Requirements map to controls; controls operate in processes/systems; evidence supports assessment; failures lead to remediation or approved exceptions.

## When to Use

Use for auditability, privacy, security controls, retention, access, reporting, and regulated workflows.

## When Not to Use

Do not claim certification or legal compliance solely from functional test results.

## Advantages

Control mapping improves traceability and risk-based testing.

## Limitations

Compliance scope includes people/process controls beyond software.

## Examples

An access-control requirement may map to authentication, authorization, review, logging, and revocation controls; testing one login path is insufficient evidence for the whole control environment.

## Best Practices

- Trace requirement → control → evidence.
- Verify negative and bypass paths.
- Test configuration/effective scope where authorized.
- Preserve audit-quality evidence.
- Escalate interpretation gaps.

## Related Knowledge

- `Regulatory-Requirements.md`
- `Security-Compliance.md`
- `Audit-Trail.md`

## References

- Applicable compliance frameworks and approved organizational controls.