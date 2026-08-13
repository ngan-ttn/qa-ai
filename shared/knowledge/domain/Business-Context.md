# Business Context

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Business context** is the surrounding set of objectives, stakeholders, constraints, policies, channels, dependencies, timing, and operating conditions that gives a requirement its meaning. The same feature can require different behavior under different contexts.

## Purpose

Help QA identify contextual factors that change expected behavior and prevent isolated interpretation of requirements.

## Core Concepts

### Business Objective
Why the capability exists and what outcome it supports.

### Stakeholder Context
Who owns, performs, approves, receives, or is affected by the behavior.

### Operational Context
Channels, timing, manual steps, external partners, batch windows, and environment conditions surrounding the feature.

### Policy Context
Rules, approvals, commercial terms, or governance that constrain behavior.

### Data Context
Source-of-truth systems, data freshness, ownership, and lifecycle affect interpretation.

### Temporal Context
Effective dates, cutoffs, periods, sequence, and historical state can alter outcomes.

### Jurisdiction / Market Context
Legal, currency, localization, or market rules can differ; they must be sourced explicitly.

## How It Works

```text
Requirement
   + objective
   + actor
   + process position
   + data ownership
   + timing
   + policy / market
   = contextual expected behavior
```

QA should make context explicit before deriving scenarios, especially when a rule appears universal but may only apply to one product, role, state, or market.

## When to Use

Use for ambiguous requirements, cross-role flows, integrations, market-specific behavior, effective-dated rules, migrations, and regression analysis.

## When Not to Use

Do not expand scope indefinitely. Context should be limited to factors that materially affect the feature or its risks.

## Advantages

Context exposes hidden dependencies, missing preconditions, conflicting assumptions, and cross-feature impacts.

## Limitations

Business context can be distributed across many sources and may change independently of the software implementation.

## Examples

### Role Context
An Edit action may be valid for RA users but forbidden for Requestors even on the same record state.

### Timing Context
A refund rule may depend on transaction date, settlement date, or request date. The relevant date must be defined.

### Integration Context
A WebView can behave differently depending on whether authentication, account status, or entitlement is owned by the host app or partner system.

## Best Practices

- State objective, actor, state, timing, and source-of-truth explicitly.
- Identify upstream and downstream dependencies.
- Capture market or policy scope when applicable.
- Distinguish business prerequisite from technical prerequisite.
- Trace contextual assumptions into test preconditions.
- Recheck context during regression-impact analysis.

## Related Knowledge

- `Business-Domain.md`
- `Business-Process-Fundamentals.md`
- `Business-Rule-Fundamentals.md`
- `Business-Capabilities.md`

## References

- Business-analysis and requirements-engineering literature.
- Approved project business documentation.
