# Business Domain

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **business domain** is an area of business activity, knowledge, rules, terminology, actors, outcomes, and constraints that a software system supports. Domain understanding gives QA the context needed to judge whether behavior is merely technically valid or actually correct for the business.

## Purpose

Provide a reusable foundation for identifying domain boundaries, concepts, stakeholders, rules, risks, and evidence before deriving QA artifacts.

## Core Concepts

### Domain Scope
Defines which business problems and capabilities are inside the area being analyzed.

### Actors and Stakeholders
People, organizations, systems, or roles that initiate, perform, approve, receive, or govern domain activities.

### Business Outcomes
Observable results the domain is expected to produce, such as fulfilling an order or settling a payment.

### Domain Rules
Policies and constraints that determine valid states, decisions, calculations, and transitions.

### Domain Language
Terms must be interpreted according to business meaning, not assumed from everyday or technical usage.

## How It Works

```text
Business objective
      ↓
Domain scope + actors
      ↓
Entities + processes + rules
      ↓
States + events + exceptions
      ↓
Observable business outcomes
```

QA uses this model to connect requirements to business intent and to detect missing assumptions or contradictory behavior.

## When to Use

Use when entering a new product area, reviewing requirements, defining scenarios, assessing regression impact, or investigating defects with unclear business consequences.

## When Not to Use

Do not use generic domain knowledge to override project requirements, legal advice, approved policy, or authoritative subject-matter expertise.

## Advantages

Domain framing improves requirement interpretation, risk identification, terminology consistency, and business-focused test coverage.

## Limitations

Domains vary by organization, jurisdiction, product, and operating model. Generic knowledge cannot supply project-specific thresholds, permissions, calculations, or compliance obligations.

## Examples

In e-commerce, checkout may involve customer, cart, inventory, pricing, payment, order, fulfillment, and refund concepts. A technically successful API call is insufficient if the resulting order violates inventory or payment rules.

In banking, a transfer involves more than moving numbers: account eligibility, authorization, limits, posting state, reversals, auditability, and regulatory obligations may matter.

## Best Practices

- Establish scope before analyzing details.
- Identify authoritative terminology and stakeholders.
- Separate generic domain patterns from project-specific rules.
- Trace business outcomes to entities, processes, rules, and exceptions.
- Record ambiguity instead of inventing missing business behavior.
- Revalidate assumptions when context or jurisdiction changes.

## Related Knowledge

- `Domain-Terminology.md`
- `Domain-Knowledge.md`
- `Business-Context.md`
- `Domain-Driven-Thinking.md`
- `Business-Process-Fundamentals.md`
- `Business-Entity.md`

## References

- Domain-driven design and business-analysis literature.
- Project requirements and approved business documentation.