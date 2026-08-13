# Data Privacy

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Data privacy** concerns appropriate collection, use, access, disclosure, retention, and deletion of information about people under applicable policy and law.

## Purpose

Give QA a privacy-aware testing model without asserting jurisdiction-specific legal requirements.

## Core Concepts

### Personal Data
Information treated as relating to an identifiable person under applicable definitions.
### Purpose and Scope
Data use should align with approved purpose and rules.
### Access
Only authorized actors should access data according to policy.
### Minimization
Systems should handle only data required by approved design.
### Lifecycle
Collection, storage, sharing, retention, and deletion all matter.

## How It Works

Privacy requirements are translated into controls across data flows, access, UI/API exposure, logs, exports, retention, and integrations.

## When to Use

Use whenever features process user/customer/person data.

## When Not to Use

Do not classify data or determine legal obligations without authoritative policy/legal guidance.

## Advantages

Privacy testing reduces unauthorized exposure and lifecycle defects.

## Limitations

Applicability and definitions vary by jurisdiction and organization.

## Examples

An export intended for one role may expose fields not visible in the UI; QA verifies export scope independently against approved permissions.

## Best Practices

- Map sensitive data flows.
- Test role and object-level access.
- Check logs, exports, errors, caches, and notifications.
- Verify retention/deletion requirements.
- Use synthetic or protected test data.

## Related Knowledge

- `Compliance.md`
- `Security-Compliance.md`
- `Data-Retention.md`
- `Audit-Trail.md`

## References

- Applicable privacy law/policy and approved data classification.