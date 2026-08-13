# Domain-Driven Thinking

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Domain-driven thinking** prioritizes business meaning, language, boundaries, rules, and behavior when reasoning about software. It borrows useful ideas from domain-driven design without requiring QA to design the software architecture.

## Purpose

Help QA organize complex requirements around domain concepts rather than screens, endpoints, or tables alone.

## Core Concepts

### Business Meaning First
Implementation is interpreted through the business behavior it supports.

### Explicit Boundaries
A concept can mean different things in different contexts.

### Shared Language
Stakeholders and delivery teams benefit from consistent domain terms.

### Behavior and Invariants
Important rules are attached to the business concepts they govern.

## How It Works

QA identifies domain concepts, boundaries, language, events, invariants, and cross-context interactions, then uses them to challenge requirements and derive coverage.

## When to Use

Use for complex enterprise domains, multi-team systems, overloaded terminology, stateful workflows, and integration-heavy features.

## When Not to Use

Do not introduce DDD terminology merely to make simple requirements more complex.

## Advantages

Improves conceptual consistency and helps locate risks at business boundaries.

## Limitations

DDD concepts can be misapplied if architecture and business boundaries are assumed rather than discovered.

## Examples

`Customer` in sales and `Account Holder` in payments may be related but governed by different rules. Treating them as one universal entity can create incorrect tests.

## Best Practices

- Use domain language stakeholders recognize.
- Discover boundaries from evidence.
- Focus on rules and behavior, not jargon.
- Validate cross-context mappings explicitly.

## Related Knowledge

- `Bounded-Context.md`
- `Ubiquitous-Language.md`
- `Domain-Model.md`
- `Business-Events.md`

## References

- Eric Evans, *Domain-Driven Design*.
- Domain modeling literature.