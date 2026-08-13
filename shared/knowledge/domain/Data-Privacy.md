# Data Privacy

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Data privacy** concerns appropriate collection, use, access, disclosure, retention, deletion, and other handling of information about people under applicable policy and law. Privacy testing focuses on implemented requirements and data flows; it does not determine legal obligations.

## Purpose

Give QA and QA-AI a privacy-aware reasoning model covering data lifecycle, exposure surfaces, copies, downstream propagation, and test-data handling without asserting jurisdiction-specific legal conclusions.

## Core Concepts

### Personal / Sensitive Data
Whether data is legally or organizationally classified as personal or sensitive depends on approved definitions.

### Purpose and Scope
Data collection and use should align with the approved purpose, product behavior, and permissions.

### Data Flow
Information moves through UI, API, databases, logs, caches, exports, notifications, analytics, backups, and third parties.

### Access
Authorization should control who can see or change data at object, field, and action level as required.

### Minimization
Approved design may restrict unnecessary collection, display, logging, or transfer.

### Masking / Redaction
Sensitive values may need to be partially or fully hidden in specific contexts.

### Retention / Deletion
Operational deletion may need propagation to copies, derived data, or downstream systems according to approved requirements.

### Consent / Preference
Some products track permissions or preferences; exact legal meaning and behavior must come from policy.

### Third-Party Sharing
Integrations can expose data beyond the primary system and require explicit scope and contract.

### Test Data
Non-production environments can create privacy risk if real sensitive data is copied or weakly protected.

## How It Works

```text
Collect
  ↓
Store / process
  ↓
Display / share / export
  ↓
Copy / derive / back up
  ↓
Retain / delete / archive
```

QA maps approved privacy requirements across each stage and verifies both obvious and indirect exposure surfaces.

## When to Use

Use whenever features process customer, employee, applicant, patient, user, or other person-related data.

## When Not to Use

Do not independently classify data, determine lawful basis, define consent requirements, or interpret privacy law without authorized legal/privacy guidance.

## Advantages

Privacy-aware testing reduces unauthorized exposure, excessive logging, incomplete deletion, and inconsistent access across channels.

## Limitations

Data can be copied into caches, analytics, backups, exports, and third parties that are difficult to observe. Legal requirements vary by jurisdiction and context.

## Examples

### Export Exposure
A role sees only masked fields in UI, but CSV export includes full values. QA verifies export independently against approved permissions.

### Log Leakage
A failed API request records credentials or personal data in logs. Functional behavior may pass while privacy control fails.

### Deletion Propagation
A record is removed from the primary UI but remains in search index, cache, or downstream reporting. QA validates deletion scope against the approved requirement.

### Test Environment
Production data is copied to staging. QA verifies the organization's approved masking/protection approach rather than assuming non-production is low risk.

## Best Practices

- Map sensitive data across full lifecycle and integration flow.
- Test field-level and object-level access.
- Check logs, errors, exports, caches, notifications, analytics, and downloads.
- Verify masking/redaction rules by role and channel.
- Validate retention/deletion propagation where required.
- Use synthetic or appropriately protected test data.
- Avoid capturing unnecessary sensitive values in test evidence.
- Escalate legal interpretation to authorized stakeholders.

## Related Knowledge

- `Compliance.md`
- `Security-Compliance.md`
- `Data-Retention.md`
- `Audit-Trail.md`
- `../api/Authorization.md`

## References

- Applicable privacy law and approved organizational privacy policy.
- Approved data classification and handling standards.
