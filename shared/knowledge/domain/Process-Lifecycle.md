# Process Lifecycle

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **process lifecycle** describes how a business process instance is created, progresses, pauses, changes, completes, expires, is canceled, or is reopened over time.

## Purpose

Give QA a time-aware model for validating process evolution beyond individual transitions.

## Core Concepts

### Creation
The point at which a process instance becomes business-significant and receives identity or initial state.

### Active Progress
Normal work advances the instance through states and activities.

### Pending / Suspended
Progress can pause while waiting for time, information, approval, or an external dependency.

### Completion
The intended business outcome has been reached and required side effects are finalized.

### Cancellation / Abandonment
The process stops before normal completion under defined rules.

### Expiry
Time-based rules can make a process or authorization invalid.

### Reopen / Correction
Completed or closed items may re-enter controlled handling if policy allows.

### Retention / Archival
Historical process data can remain after active processing ends according to approved requirements.

## How It Works

Lifecycle reasoning combines state, time, actors, events, and policy. A transition valid today may be invalid after expiry; a completed process may still permit a correction workflow without returning to its original lifecycle.

## When to Use

Use for long-running requests, approvals, orders, permits, subscriptions, claims, returns, or any feature where time and historical state matter.

## When Not to Use

Do not assume every entity or process shares a simple create-update-delete lifecycle. Do not infer retention or reopening behavior without evidence.

## Advantages

Lifecycle analysis exposes expiry, stale-action, reopen, cleanup, and historical consistency defects that single-step testing misses.

## Limitations

Long lifecycles can depend on external systems, policy effective dates, and operational interventions that are difficult to simulate fully.

## Examples

### Expiry
An approved permit can be valid only for a defined period. After expiry, new allocation may be blocked while historical records remain visible.

### Cancellation
An order canceled before shipment may release inventory; cancellation after shipment may require return/refund instead.

### Reopen
A completed support request may be reopened within an approved window, creating new history without erasing the original completion.

## Best Practices

- Identify lifecycle start, active, pending, terminal, and exceptional stages.
- Define time anchors and effective dates precisely.
- Test actions near expiry and cutoff boundaries.
- Verify side effects on cancel, expire, and reopen.
- Preserve historical/audit consistency.
- Test stale sessions acting on changed lifecycle state.
- Separate archival/retention from active business status.

## Related Knowledge

- `Process-States.md`
- `Business-Workflow.md`
- `Process-Exceptions.md`
- `Entity-Lifecycle.md`
- `Data-Retention.md`

## References

- Business lifecycle and workflow literature.
- Approved lifecycle requirements and policies.
