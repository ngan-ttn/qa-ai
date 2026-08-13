# Process Lifecycle

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **process lifecycle** is the progression of a business process from initiation through active states to completion, cancellation, expiration, archival, or another terminal condition.

## Purpose

Help QA cover behavior across time and lifecycle phases instead of testing only creation and current-state actions.

## Core Concepts

### Initiation
Entry conditions and initial state.
### Active Phase
Normal work and transitions.
### Suspension or Waiting
Temporary non-terminal states.
### Completion
Successful business outcome.
### Termination
Cancellation, rejection, expiration, or failure.
### Post-Lifecycle
Retention, audit, reopening, or archival behavior.

## How It Works

Lifecycle rules determine which events are accepted in each phase and what data or actions remain available afterward.

## When to Use

Use for long-running records, approvals, subscriptions, orders, cases, permits, and contracts.

## When Not to Use

Do not assume every lifecycle is linear or reversible.

## Advantages

Reveals time-dependent and post-completion defects.

## Limitations

Lifecycle boundaries may differ by role, subsystem, or legal status.

## Examples

A permit can be drafted, submitted, approved, active, expired, and retained for audit. Editing rules can change at every phase.

## Best Practices

- Define entry/exit conditions.
- Test expiry and timeout boundaries.
- Verify terminal-state restrictions.
- Cover reopen/reactivation only when supported.
- Validate retention and audit behavior after closure.

## Related Knowledge

- `Process-States.md`
- `Process-Exceptions.md`
- `Entity-Lifecycle.md`
- `Data-Retention.md`

## References

- Business lifecycle and process-management literature.