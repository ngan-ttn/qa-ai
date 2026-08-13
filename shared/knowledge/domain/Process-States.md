# Process States

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **process state** is a business-significant condition of a process instance at a point in time. States represent what is currently true, what actions are allowed, and what transitions may occur next.

## Purpose

Help QA model stateful behavior precisely and detect invalid transitions, missing permissions, inconsistent derived status, and race conditions.

## Core Concepts

### State
A named business condition such as `Draft`, `Submitted`, `Approved`, `Canceled`, or `Completed`.

### Transition
A change from one state to another caused by an action, event, decision, or timeout.

### Guard
A condition that must be true before a transition is allowed.

### Terminal State
A state with no normal forward transition, although reopening or correction may still be possible if defined.

### Composite / Derived State
Displayed status may be derived from several underlying facts or sub-processes.

### Actor Permission
Different roles may be allowed to trigger different transitions from the same state.

### Historical State
Audit/history can be needed to understand how current state was reached.

## How It Works

```text
Current state
 + actor
 + event/action
 + guard conditions
      ↓
Allowed transition?
      ↓
new state + side effects + history
```

QA should verify both transition permission and resulting side effects. Invalid transitions should not leave partial state changes.

## When to Use

Use for workflow-heavy features, approvals, requests, orders, subscriptions, inventory operations, lifecycle management, and asynchronous processes.

## When Not to Use

Do not create artificial states from temporary UI presentation unless they have business meaning. Do not assume status labels alone fully represent all process facts.

## Advantages

State modeling supports systematic positive, negative, role-based, and transition-path testing.

## Limitations

State explosion can occur when one displayed status summarizes multiple independent dimensions. Legacy systems may also allow historical state combinations that new rules would forbid.

## Examples

A request in `Submitted` may allow `Approve` for an approver and `Cancel` for the requester, while `Edit` is blocked. After `Approved`, cancellation may require a different rule or compensation path.

A shipment may display `In Progress` while packing is complete but carrier pickup is pending. The displayed state is derived from sub-process facts.

## Best Practices

- Define state meaning, owner, entry condition, and allowed exits.
- Build a transition matrix by actor and condition.
- Test forbidden transitions directly.
- Verify side effects and audit history for every critical transition.
- Include concurrent and stale-state actions.
- Distinguish stored state from derived/display state.
- Clarify reopening, correction, and terminal-state rules.

## Related Knowledge

- `Business-Workflow.md`
- `Process-Lifecycle.md`
- `Process-Exceptions.md`
- `Business-Events.md`
- `../testing-techniques/Specification-Based/State-Transition-Testing.md`

## References

- State-machine and workflow literature.
- Approved process-state definitions.
