# Finite State Machine Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Finite State Machine (FSM) Testing** uses a finite set of states, events, transitions, and guards as an executable or analyzable model for deriving tests. It is a model-based specialization of state-oriented testing.

## Purpose

Provide rigorous lifecycle and sequence coverage when system behavior can be represented as a finite state machine.

## Core Concepts

### State Set
A finite collection of relevant states.

### Event / Input
An occurrence that may trigger a transition.

### Transition Function
Defines the next state for a state-event combination when conditions are satisfied.

### Guard
A predicate controlling whether a transition is permitted.

### Output / Side Effect
Observable behavior associated with a transition or state.

### Coverage Criteria
Examples include all states, all transitions, transition pairs, or selected longer sequences.

## How It Works

Create the state machine from authoritative behavior, validate state/event completeness, select coverage criteria, derive event sequences, execute them, and compare observed states/outputs with the model.

## When to Use

Use for protocols, device controllers, approval lifecycles, sessions, transaction states, workflow engines, subscription status, or other finite-state behavior.

## When Not to Use

Do not force FSM modeling onto behavior dominated by continuous data, large unbounded context, or parallel state dimensions that are better represented with richer models.

## Advantages

- Precise representation of allowed and forbidden transitions.
- Supports automated path generation.
- Makes sequence dependencies explicit.
- Provides measurable state/transition coverage.

## Limitations

- State explosion can occur with many dimensions.
- Parallel or hierarchical states may exceed a simple FSM model.
- Timing and concurrency need additional modeling.
- Incorrect state abstraction leads to misleading tests.

## Examples

A login session FSM may contain `LoggedOut`, `Authenticated`, `Expired`, and `Revoked` states with events such as login, logout, timeout, and token refresh.

An approval item FSM can model submit, approve, reject, cancel, and rework transitions while explicitly rejecting forbidden events from terminal states.

## Best Practices

- Use business-significant states.
- Include invalid state-event combinations.
- Define terminal and recovery behavior.
- Add guards and side effects explicitly.
- Control state explosion through meaningful abstraction.
- Supplement the model for timing, concurrency, and data boundaries.

## Related Knowledge

- `Model-Based-Testing.md`
- `../Specification-Based/State-Transition-Testing.md`
- `../../domain/Process-States.md`
- `../../domain/Process-Lifecycle.md`

## References

- Finite-state machine testing literature.
- State-modeling and protocol-testing references.