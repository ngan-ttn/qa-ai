# State Transition Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**State Transition Testing** validates behavior that depends on the current state of an entity or system and on events that cause state changes. It tests not only destination states but also allowed, forbidden, repeated, and history-dependent transitions.

## Purpose

Provide systematic coverage for lifecycle behavior where the same event can produce different results depending on prior state.

## Core Concepts

### State
A business-significant condition that affects allowed behavior.

### Event
An action, trigger, message, time condition, or external occurrence that may cause a transition.

### Transition
A change from one state to another under defined conditions.

### Guard
A condition that must be satisfied for a transition to be allowed.

### Invalid Transition
An attempted event that must not produce the requested state change.

### Transition History
Some systems depend on previous states, counters, or event sequences rather than current state alone.

## How It Works

```text
Identify states
    ↓
Identify events and guards
    ↓
Map valid transitions
    ↓
Identify forbidden/repeated transitions
    ↓
Define expected side effects
    ↓
Derive state and transition coverage tests
```

Coverage may target states, valid transitions, invalid transitions, transition pairs, or longer sequences depending on risk.

## When to Use

Use for approvals, orders, payments, sessions, subscriptions, permits, claims, tickets, device states, workflow items, retries, or any lifecycle-driven feature.

## When Not to Use

Do not use it as the only technique for value ranges, independent field validation, or complex condition combinations that do not materially depend on state history.

## Advantages

- Exposes invalid lifecycle movement.
- Makes repeated and out-of-order actions testable.
- Supports sequence-sensitive coverage.
- Reveals missing terminal, recovery, or exception states.

## Limitations

- State models can become large.
- Hidden substates or parallel states may complicate modeling.
- Timing and concurrency can create behavior not captured by a simple diagram.
- The state model must be validated against authoritative business rules.

## Examples

### Approval
`Draft → Submitted → Approved → Completed`; attempts to edit after completion may be forbidden while rejection may return to rework.

### Payment
`Initiated → Authorized → Posted → Settled`, with separate rejected, reversed, or returned paths. Acceptance is not assumed to equal settlement.

### Session
Repeated login, timeout, logout, and token refresh behavior can depend on whether the session is active, expired, or revoked.

## Best Practices

- Define business states, not UI screen labels alone.
- Cover valid and invalid transitions.
- Include repeated events and idempotent behavior where relevant.
- Test terminal and recovery paths.
- Consider timing, concurrency, and asynchronous completion.
- Verify transition side effects, not only status values.
- Keep state models aligned with domain lifecycle knowledge.

## Related Knowledge

- `Use-Case-Testing.md`
- `Decision-Table-Testing.md`
- `../Model-Based/Finite-State-Machine-Testing.md`
- `../../domain/Process-States.md`
- `../../domain/Process-Lifecycle.md`

## References

- ISTQB State Transition Testing guidance.
- State-machine and workflow modeling literature.