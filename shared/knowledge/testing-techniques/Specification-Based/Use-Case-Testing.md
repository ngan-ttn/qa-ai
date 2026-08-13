# Use-Case Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Use-Case Testing** derives tests from actor goals and end-to-end interactions with a system. It validates main success flows, alternate flows, exceptions, preconditions, postconditions, and business outcomes across multiple steps.

## Purpose

Ensure that integrated system behavior supports meaningful user or external-actor goals rather than validating isolated functions only.

## Core Concepts

### Actor
A person, role, system, or external party interacting with the use case.

### Goal
The business outcome the actor intends to achieve.

### Preconditions
Conditions that must hold before the flow begins.

### Main Success Scenario
The normal path leading to the intended outcome.

### Alternate Flow
A valid variation that still supports a meaningful outcome.

### Exception Flow
A failure or interruption path requiring error handling, recovery, or termination.

### Postconditions
Expected business state after success or failure.

## How It Works

```text
Actor goal
   ↓
Define preconditions
   ↓
Map main interaction flow
   ↓
Identify alternate and exception branches
   ↓
Define postconditions / side effects
   ↓
Derive end-to-end scenarios
```

Use-case tests often combine techniques: BVA for values, Decision Tables for rules, and State Transition Testing for lifecycle steps.

## When to Use

Use for checkout, onboarding, booking, transfer, approval, import, fulfillment, returns, account management, and other multi-step business interactions.

## When Not to Use

Do not rely on use-case testing alone for exhaustive field validation, structural coverage, low-level protocol behavior, or high-dimensional combinations.

## Advantages

- Aligns tests with actor goals and business outcomes.
- Covers integration across multiple functions.
- Makes alternate and exception flows explicit.
- Helps reveal missing handoffs and incomplete postconditions.

## Limitations

- Use cases can be too high-level to cover detailed rules.
- Long flows may hide root causes when they fail.
- Complex branching can create many scenario variants.
- Quality depends on accurately defined actors and outcomes.

## Examples

### Checkout
Main flow: select item → cart → address → payment → order confirmation. Alternate flows include coupon use or saved address; exception flows include payment failure or inventory loss before confirmation.

### Permit Approval
Submit → review → approval → downstream availability. Rejection, withdrawal, resubmission, and timeout paths are tested separately.

## Best Practices

- Define one clear actor goal per use case.
- Verify preconditions and postconditions.
- Cover alternate and exception flows.
- Validate cross-system handoffs and side effects.
- Avoid duplicating detailed field tests already owned by other techniques.
- Trace use cases to business requirements.
- Separate user-visible success from asynchronous downstream completion when relevant.

## Related Knowledge

- `State-Transition-Testing.md`
- `Decision-Table-Testing.md`
- `../Foundation/Black-Box-Testing.md`
- `../../domain/Business-Workflow.md`
- `../../qa/Requirement-Analysis.md`

## References

- Use-case modeling literature.
- ISTQB scenario/use-case based testing guidance.