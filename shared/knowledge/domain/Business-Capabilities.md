# Business Capabilities

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **business capability** describes what an organization must be able to do to achieve outcomes, independent of a particular process or technology implementation.

## Purpose

Help QA understand feature scope and impact at a stable business-function level.

## Core Concepts

### Capability
An ability such as `Manage Orders` or `Settle Payments`.
### Outcome
Business value the capability enables.
### Supporting Process
How the capability is operationalized.
### Dependency
Other capabilities required to deliver the outcome.

## How It Works

Capabilities provide a map from strategic/business needs to processes, systems, and changes; QA can use it to identify impacted areas beyond the immediate feature.

## When to Use

Use for large change impact, portfolio context, integration scope, and regression analysis.

## When Not to Use

Do not treat a capability map as a detailed workflow or requirement specification.

## Advantages

Provides stable high-level scope across changing implementations.

## Limitations

Capability definitions can be too broad for executable testing.

## Examples

`Manage Returns` may depend on order lookup, eligibility, inventory, refund, and customer notification capabilities.

## Best Practices

- Name capabilities as business abilities.
- Map dependencies and outcomes.
- Use capabilities to find impact, then descend into detailed rules/processes.

## Related Knowledge

- `Domain-Model.md`
- `Business-Process-Fundamentals.md`
- `Business-Context.md`

## References

- Business architecture literature.