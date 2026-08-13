# Business Capabilities

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **business capability** describes what an organization is able to do to achieve business outcomes, independent of a specific process, team, system, or implementation. Examples include order fulfillment, customer identity management, payment processing, eligibility assessment, or inventory control.

## Purpose

Help QA reason at a stable business level above individual features, identify affected capabilities, and assess cross-system regression impact.

## Core Concepts

### Capability
A durable business ability expressed as `what`, not `how`.

### Outcome
The business value or result supported by the capability.

### People / Process / Information / Technology
A capability can be delivered through several organizational and technical components.

### Capability Boundary
Defines responsibility and prevents one feature from being mistaken for the whole business ability.

### Dependency
Capabilities can depend on other capabilities, such as fulfillment depending on inventory visibility and customer/order management.

### Maturity
Organizations may assess capability strength or maturity, but no generic scoring model should be assumed.

### Ownership
Business ownership can differ from system ownership.

## How It Works

```text
Business objective
      ↓
Required capabilities
      ↓
Processes + data + rules + systems
      ↓
Features / integrations
```

QA can map a requirement to one or more capabilities, then inspect upstream/downstream dependencies and shared business invariants.

## When to Use

Use for roadmap analysis, large programs, cross-system regression, domain onboarding, impact analysis, and organizing knowledge across many features.

## When Not to Use

Do not replace detailed process or rule analysis with capability labels. Do not infer organization structure from capability ownership.

## Advantages

Capabilities provide stable business framing even when implementation or workflows change.

## Limitations

Capability boundaries can be subjective, and broad capability maps may be too abstract for executable testing without lower-level models.

## Examples

`Manage Inventory` can include receiving, stock visibility, reservation, adjustment, cycle count, and outbound consumption across multiple systems.

`Manage Customer Loyalty` can include enrollment, earn, redeem, expiry, adjustment, tiering, and partner integration.

## Best Practices

- Name capabilities using business outcomes or abilities.
- Keep capability distinct from process and system.
- Map affected capabilities during regression analysis.
- Identify shared data and rule dependencies.
- Use capabilities to organize domain knowledge and coverage, then drill into process/rules.
- Validate ownership with business stakeholders.

## Related Knowledge

- `Business-Domain.md`
- `Business-Context.md`
- `Business-Process-Fundamentals.md`
- `Domain-Model.md`
- `Bounded-Context.md`

## References

- Business architecture and capability-mapping literature.
- Approved enterprise/domain capability models.
