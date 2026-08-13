# Business Workflow

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **business workflow** describes the ordered or conditional flow of work among actors and systems to progress a business process.

## Purpose

Help QA reason about sequence, routing, responsibility, conditions, handoffs, and alternate paths.

## Core Concepts

### Step
A unit of work.
### Sequence
Required ordering between steps.
### Branch
A conditional route.
### Parallel Work
Activities that can proceed concurrently.
### Handoff
Transfer between roles or systems.
### Completion Condition
Evidence that workflow goals are satisfied.

## How It Works

Workflows connect triggers to steps, decisions, branches, waits, handoffs, and terminal outcomes. QA tests valid routes plus forbidden or incomplete transitions.

## When to Use

Use for approval flows, onboarding, fulfillment, claims, requests, and other stateful business operations.

## When Not to Use

Do not equate UI navigation with the business workflow; one workflow can span channels and systems.

## Advantages

Makes sequence and routing defects visible.

## Limitations

Workflow diagrams may omit timing, policy, concurrency, or manual exceptions.

## Examples

A request can move `Draft → Submitted → Approved → Completed`; rejection may return it to a rework state rather than simply end it.

## Best Practices

- Define allowed transitions and actors.
- Test branch conditions and skipped steps.
- Verify handoff data and ownership.
- Include concurrency and repeated actions where relevant.
- Separate process state from UI presentation.

## Related Knowledge

- `Process-States.md`
- `Process-Lifecycle.md`
- `Process-Exceptions.md`
- `Business-Events.md`

## References

- Workflow and BPM literature.