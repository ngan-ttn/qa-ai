# Domain-Driven Thinking

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Domain-driven thinking** is an approach to understanding software through business meaning, behavior, boundaries, and language rather than starting from screens, endpoints, or database structures. It borrows useful reasoning principles from domain-driven design without requiring a project to implement DDD.

## Purpose

Help QA and QA-AI structure complex business understanding, recognize context boundaries, and avoid coupling test reasoning too tightly to implementation details.

## Core Concepts

### Business Meaning First
Start from why a capability exists and what business outcome must remain correct.

### Model as a Reasoning Tool
A domain model organizes important concepts, rules, states, and interactions; it is not automatically an implementation blueprint.

### Bounded Context
The meaning and rules of a concept can differ across contexts. Boundaries make those differences explicit.

### Ubiquitous Language
Shared terminology reduces translation errors between stakeholders and technical teams.

### Invariants
Important business conditions must remain true despite implementation changes.

### Events and State Change
Business events explain what happened and why state moved.

### Context Mapping
Cross-context integrations require explicit translation, ownership, and consistency expectations.

## How It Works

```text
Business problem
    ↓
Language + concepts
    ↓
Context boundaries
    ↓
Rules + invariants
    ↓
Events + state changes
    ↓
Interfaces / implementations
```

For QA, this enables scenarios to be derived from business behavior first, then mapped to UI, API, database, or integration evidence.

## When to Use

Use for complex domains, cross-system flows, ambiguous terminology, multiple ownership boundaries, event-driven processes, and regression analysis that spans technical layers.

## When Not to Use

Do not impose DDD terminology on simple projects where it adds no value. Do not assume architecture patterns such as aggregates, event sourcing, or microservices unless the design confirms them.

## Advantages

Improves business-focused coverage, boundary awareness, terminology consistency, and resilience of QA artifacts to implementation change.

## Limitations

Models and boundaries can be subjective. Poorly understood domains may produce misleading abstractions, and multiple teams may disagree on language or ownership.

## Examples

A `Customer` in CRM may represent a marketing relationship while a `Customer` in billing represents a legal payer. Domain-driven thinking prevents QA from assuming fields, permissions, or lifecycle are identical.

An `Order` may have a business invariant that total payable equals approved line totals minus valid discounts plus charges. QA can test that invariant through different interfaces without treating one table as the domain model.

## Best Practices

- Start from business outcomes and invariants.
- Define context when terms change meaning.
- Use stakeholder language consistently.
- Map cross-context ownership and translation explicitly.
- Separate conceptual model from storage/API representation.
- Treat models as hypotheses to validate with stakeholders.
- Avoid importing DDD implementation patterns without evidence.

## Related Knowledge

- `Business-Domain.md`
- `Domain-Model.md`
- `Bounded-Context.md`
- `Ubiquitous-Language.md`
- `Event-Storming.md`

## References

- Domain-driven design literature.
- Business-analysis and systems-modeling literature.
