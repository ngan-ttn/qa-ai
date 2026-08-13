# Compliance

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Compliance** is the state and practice of meeting applicable obligations from law, regulation, policy, contract, standard, or internal governance through defined controls and evidence.

## Purpose

Help QA validate control behavior and evidence while respecting the boundary between testing and legal/compliance judgment.

## Core Concepts

### Requirement
The authoritative obligation or approved policy statement.

### Control
A preventive, detective, corrective, or compensating mechanism intended to satisfy a requirement.

### Control Owner
The role accountable for operation or governance of the control.

### Evidence
Records showing that a control operated as designed.

### Frequency / Trigger
Controls can run per transaction, periodically, at approval, or on change.

### Exception
A control failure or approved exception requires defined handling and evidence.

### Monitoring
Ongoing review can identify control drift, failure, or noncompliant state.

### Traceability
Tests should link to the approved control requirement rather than generic regulation summaries.

## How It Works

```text
Obligation / policy
      ↓
Approved control design
      ↓
Software + operational implementation
      ↓
Control execution
      ↓
Evidence / monitoring / exception handling
```

QA verifies implementation against the approved control design. Compliance certification or legal conclusion remains outside generic QA authority.

## When to Use

Use for access controls, approvals, audit trails, retention, privacy, security governance, regulated calculations, recordkeeping, and other controlled business behavior.

## When Not to Use

Do not declare a product legally compliant based solely on functional tests. Do not assume all controls are implemented in software; some are operational or organizational.

## Advantages

Compliance-oriented testing strengthens traceability, bypass resistance, evidence verification, and change-impact analysis.

## Limitations

Controls can depend on manual procedures, external systems, policy interpretation, and environment-specific configuration.

## Examples

A four-eyes approval control requires that the initiator cannot approve the same transaction. QA tests role combinations, reassignment, stale sessions, API bypass, and audit evidence according to the approved control design.

A retention control may run as a scheduled purge process; functional UI behavior alone cannot prove it executes correctly over time.

## Best Practices

- Map each test to an approved control requirement.
- Identify control owner and evidence source.
- Test bypass paths and alternate channels.
- Verify failures are observable and handled.
- Include role, timing, configuration, and lifecycle conditions.
- Avoid over-collecting sensitive evidence.
- Revalidate controls after material system or policy changes.
- Distinguish test PASS from formal compliance attestation.

## Related Knowledge

- `Regulatory-Requirements.md`
- `Audit-Trail.md`
- `Data-Privacy.md`
- `Security-Compliance.md`
- `Data-Retention.md`

## References

- Approved compliance framework, policy, and control documentation.
- Applicable authoritative standards and regulations.
