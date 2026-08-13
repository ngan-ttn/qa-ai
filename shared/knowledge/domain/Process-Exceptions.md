# Process Exceptions

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **process exception** is a condition that prevents, diverts, delays, reverses, or otherwise changes the normal business process path. Exceptions are business behavior, not merely technical errors.

## Purpose

Help QA systematically identify and test alternate handling, recovery, escalation, compensation, and incomplete outcomes.

## Core Concepts

### Business Rejection
Input or context fails a business rule and is intentionally rejected.

### Operational Failure
A required resource, role, document, inventory item, or external party is unavailable.

### Technical Failure
A service, network, database, or integration fails; business handling still needs definition.

### Timeout
Expected action or response does not occur within an approved period.

### Retry
The same or equivalent work is attempted again. Safe retry depends on business and technical idempotency.

### Compensation
A later action offsets an earlier successful action when full rollback is impossible.

### Escalation
An exception is transferred to another role or control path.

### Manual Intervention
Human correction may resolve a condition that automated workflow cannot.

## How It Works

```text
Normal step
   ↓
Exception detected
   ↓
classify + record
   ↓
reject / retry / wait / compensate / escalate
   ↓
recover, terminate, or continue
```

QA must validate the resulting business state, not only the error message. Partial side effects and duplicate recovery actions are major risks.

## When to Use

Use for external integrations, payment, inventory, approval, batch jobs, migrations, asynchronous processing, and any high-risk workflow.

## When Not to Use

Do not invent recovery policy from technical capabilities. A retry may be unsafe when the original outcome is uncertain.

## Advantages

Exception analysis improves resilience coverage and exposes stranded, duplicated, or inconsistent business state.

## Limitations

Some exceptions are operationally rare or hard to reproduce. Observability may be insufficient to know whether an external action succeeded.

## Examples

A payment request times out after the provider accepted it. Blind retry can create a duplicate charge unless the integration has a safe duplicate-control strategy.

Inventory reservation succeeds but order confirmation fails. Recovery may release inventory or retain reservation depending on policy.

An approval task is assigned to an unavailable approver. The process may escalate or reassign rather than remain stuck indefinitely.

## Best Practices

- Classify business, operational, and technical exceptions separately.
- Define expected state after each failure point.
- Test partial success and unknown outcome.
- Verify retry safety and duplicate controls.
- Cover timeout, cancellation, compensation, and escalation.
- Validate user-visible status and operational observability.
- Preserve audit evidence for manual intervention.

## Related Knowledge

- `Business-Workflow.md`
- `Process-States.md`
- `Business-Events.md`
- `Rule-Exceptions.md`
- `../api/Retry-Strategy.md`
- `../api/Idempotency.md`

## References

- Workflow resilience and business process literature.
- Approved exception-handling procedures.
