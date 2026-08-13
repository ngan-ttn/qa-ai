# Process Exceptions

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Process exceptions** are expected or unexpected conditions that prevent a business process from following its normal path.

## Purpose

Provide a model for testing alternate handling, recovery, escalation, compensation, and safe failure.

## Core Concepts

### Business Exception
A valid condition such as ineligibility or insufficient stock.
### Technical Exception
Infrastructure or integration failure affecting execution.
### Recovery
Retry, correction, resumption, or alternate processing.
### Compensation
Business action that counteracts a completed effect when rollback is impossible.
### Escalation
Transfer to another role or process.

## How It Works

The system detects a condition, classifies it, preserves required state, applies an approved exception path, and communicates an actionable outcome.

## When to Use

Use for failures, rejections, timeouts, duplicate requests, unavailable dependencies, and manual review paths.

## When Not to Use

Do not expect technical rollback to undo business effects in external systems automatically.

## Advantages

Exception testing exposes data inconsistency and stranded-process risks.

## Limitations

Some recovery behavior is operational rather than application-controlled.

## Examples

Payment succeeds externally but order creation fails. Recovery may require reconciliation or compensation rather than simply retrying the whole request.

## Best Practices

- Separate business and technical exceptions.
- Verify preserved state and user visibility.
- Test retry/idempotency where applicable.
- Validate escalation and compensation paths.
- Check audit evidence and final consistency.

## Related Knowledge

- `Business-Workflow.md`
- `Rule-Exceptions.md`
- `Business-Events.md`
- `../api/Retry-Strategy.md`

## References

- BPM and distributed-workflow literature.