# Process States

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **process state** represents the business condition of a process instance at a point in its lifecycle.

## Purpose

Support precise testing of state-dependent permissions, actions, transitions, visibility, and side effects.

## Core Concepts

### State
A meaningful business condition.
### Transition
Movement from one state to another.
### Guard
A condition required for a transition.
### Terminal State
A state with no normal onward transition.
### Invalid Transition
A prohibited movement.

## How It Works

Events or actions evaluate guards and rules; if valid, state changes and associated effects occur. QA verifies both transition and invariants around it.

## When to Use

Use for status-driven workflows, approvals, orders, payments, tickets, permits, and lifecycle-based permissions.

## When Not to Use

Do not infer business states solely from labels displayed in UI.

## Advantages

State modeling exposes invalid transitions and missing coverage efficiently.

## Limitations

Composite or parallel processes may have multiple state dimensions rather than one status field.

## Examples

An `Approved` record may allow execution but prohibit editing. A transition from `Canceled` back to `Active` should not be assumed unless explicitly supported.

## Best Practices

- Define each state's business meaning.
- Test valid and invalid transitions.
- Verify role and action availability per state.
- Check side effects and audit evidence.
- Consider concurrent transition attempts.

## Related Knowledge

- `Business-Workflow.md`
- `Process-Lifecycle.md`
- `../testing-techniques/Specification-Based/State-Transition-Testing.md`

## References

- State-machine and business-process literature.