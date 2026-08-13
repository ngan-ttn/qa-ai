# Business Workflow

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **business workflow** describes how work moves among steps, actors, systems, decisions, waits, and terminal outcomes within a business process. It makes routing and sequencing explicit, including alternate and exception paths.

## Purpose

Help QA reason about valid sequence, responsibility, branch conditions, handoffs, concurrency, re-entry, failure handling, and completion evidence.

## Core Concepts

### Step
A unit of work with defined preconditions, action, ownership, and expected postconditions.

### Sequence
Required ordering between steps. Some sequences are strict; others allow independent or parallel progress.

### Branch
A conditional route selected from business facts or decisions.

### Parallel Work
Activities that may proceed concurrently and later require synchronization.

### Wait State
A workflow can pause for time, an external event, approval, payment, or another dependency.

### Handoff
Transfer of work or data between roles or systems. Handoffs are common failure points.

### Re-entry / Retry
A failed or paused step may be attempted again; rules must define whether repetition is safe.

### Cancellation / Compensation
A workflow may end early or compensate for already completed work rather than reverse everything.

### Completion Condition
Evidence that the workflow's business goal is satisfied, not merely that the last screen was reached.

## How It Works

```text
Trigger
  ↓
[Precondition]
  ↓
Step A ──decision──► Step B / Step C
  │                    │
  └──── parallel ──────┘
           ↓
        Wait / event
           ↓
   complete / reject / cancel
```

For each transition, QA asks who can act, what must already be true, what data is carried forward, whether the action is repeatable, what happens on partial failure, and what outcome proves success.

## When to Use

Use for approval flows, onboarding, fulfillment, claims, requests, imports, returns, asynchronous processes, and other stateful business operations.

## When Not to Use

Do not equate UI navigation with the business workflow. Do not assume the workflow is synchronous, single-channel, or owned by one system.

## Advantages

Workflow modeling makes sequence, routing, state, ownership, duplicate-action, and incomplete-transition defects visible.

## Limitations

Workflow diagrams may omit timing, concurrency, retries, manual work, access rules, or exception escalation. Real processes can also deviate operationally from documented flow.

## Examples

### Approval with Rework
`Draft → Submitted → Under Review → Approved → Completed`. A rejection may return the item to `Draft` or `Rework`; whether previous approvals remain valid must be defined.

### Parallel Checks
Fraud screening and eligibility validation run independently. Completion requires both. QA tests different completion orders and one-side failure.

### Duplicate Action
A user double-clicks `Submit` or retries after a timeout. QA verifies whether duplicate workflow instances, duplicate charges, or inconsistent states can occur.

### Timeout and Re-entry
A pending external response expires. The workflow may retry, escalate, cancel, or wait indefinitely depending on approved rules.

## Best Practices

- Define preconditions and postconditions for material steps.
- Map allowed and forbidden transitions by actor.
- Test every branch condition near its boundaries.
- Verify handoff data, ownership, and authorization.
- Cover waits, timeout, retry, re-entry, cancellation, and compensation.
- Test parallel completion in different orders.
- Verify repeated actions and idempotency expectations.
- Separate business state from UI page or button visibility.
- Validate terminal outcome and audit evidence.

## Related Knowledge

- `Business-Process-Fundamentals.md`
- `Process-States.md`
- `Process-Lifecycle.md`
- `Process-Exceptions.md`
- `Business-Events.md`
- `../api/Idempotency.md`

## References

- Workflow and BPM literature.
- Approved business process and state-transition documentation.
