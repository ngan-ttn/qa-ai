# Business Context

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Business context** is the environment in which a requirement or behavior has meaning: objectives, actors, products, channels, policies, lifecycle states, dependencies, jurisdiction, and operational constraints.

## Purpose

Prevent isolated requirement interpretation by giving QA a model for understanding why behavior exists and what surrounding conditions can change its expected result.

## Core Concepts

### Objective
The business outcome being pursued.

### Stakeholder Context
Different roles can have different permissions, incentives, and views of the same process.

### Operational Context
Timing, channel, geography, dependencies, and process state influence behavior.

### Policy Context
Rules can depend on product, customer segment, jurisdiction, or effective date.

## How It Works

```text
Requirement
 + actor
 + objective
 + process state
 + governing rules
 + dependencies
 = interpretable business behavior
```

## When to Use

Use when requirements are terse, cross-functional, role-dependent, stateful, regulated, or integrated with external systems.

## When Not to Use

Do not add contextual assumptions that are not supported by evidence.

## Advantages

Context exposes hidden dependencies, role differences, lifecycle conditions, and missing acceptance criteria.

## Limitations

Context can be broad and change over time; not every surrounding fact is relevant to a specific decision.

## Examples

A cancellation rule can differ before fulfillment, after shipment, or after settlement. The word `cancel` alone does not define expected behavior.

## Best Practices

- Identify actor, objective, state, channel, and governing rule.
- Ask which context dimensions change the outcome.
- Keep assumptions explicit.
- Trace context-sensitive rules into scenarios.

## Related Knowledge

- `Business-Domain.md`
- `Business-Process-Fundamentals.md`
- `Business-Rule-Fundamentals.md`
- `Bounded-Context.md`

## References

- Business-analysis literature.
- Current product and policy documentation.