# Data Retention

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Data retention** defines how long business data, records, logs, backups, and derived copies are kept, archived, restricted, or deleted according to approved business, legal, operational, and compliance requirements.

## Purpose

Help QA validate retention lifecycle and deletion/archive behavior without inventing retention periods or legal obligations.

## Core Concepts

### Retention Period
The approved duration for keeping a data category, measured from a defined time anchor.

### Time Anchor
Retention may begin at creation, closure, contract termination, last activity, or another approved event.

### Data Category
Different records can have different retention rules.

### Active vs Archived
Archived data may remain retained but have different access, performance, or modification rules.

### Legal / Business Hold
Deletion can be suspended by an approved hold; applicability requires authoritative guidance.

### Deletion / Destruction
End-of-retention handling can involve logical deletion, physical deletion, anonymization, or another approved method.

### Backup / Replica
Copies may follow separate deletion timing because backup architecture differs from primary storage.

### Evidence
Retention jobs and exceptions may require logs or reports proving execution.

## How It Works

```text
Data created / event anchor
       ↓
Retention classification
       ↓
Active use
       ↓
Archive / restricted access (optional)
       ↓
Retention expiry
       ↓
Delete / anonymize / preserve on hold
```

QA must understand the category, time anchor, scope of copies, and approved execution mechanism.

## When to Use

Use for customer data, transaction history, audit logs, application records, documents, exports, backups, and compliance-driven lifecycle controls.

## When Not to Use

Do not invent retention durations, decide legal holds, or assume deleting a UI record means all copies must disappear immediately.

## Advantages

Retention testing reduces over-retention, premature deletion, inaccessible archives, and inconsistent lifecycle behavior.

## Limitations

Long periods are difficult to test in real time. Backups, analytics, search indexes, and third parties can follow different technical deletion mechanisms.

## Examples

### Time Anchor
A policy retains closed cases for a defined period after closure. QA verifies the timer starts from closure, not creation, based on approved interpretation.

### Legal Hold
A scheduled purge normally deletes expired records, but records under an approved hold are skipped and recorded in evidence.

### Backup Copy
Primary data is deleted while backup copies expire through backup rotation later. QA validates behavior only against the documented retention architecture.

## Best Practices

- Obtain data category, period, time anchor, and deletion method explicitly.
- Test boundary dates using controllable clocks/data where possible.
- Validate active, archived, expired, and held states.
- Check copies and downstream stores named in the requirement.
- Verify authorization to access archives.
- Validate purge-job evidence and failure handling.
- Avoid interpreting legal obligations independently.
- Recheck retention after schema/data-flow changes.

## Related Knowledge

- `Data-Privacy.md`
- `Compliance.md`
- `Audit-Trail.md`
- `Entity-Lifecycle.md`
- `../database/Backup-and-Recovery.md`

## References

- Approved retention schedule and data-governance policy.
- Applicable authoritative legal/compliance guidance.
