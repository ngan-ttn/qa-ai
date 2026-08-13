# Ubiquitous Language

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Ubiquitous language** is a shared, context-specific vocabulary used consistently by domain experts and delivery teams to describe the domain model and behavior.

## Purpose

Help QA maintain semantic consistency across requirements, scenarios, defects, and discussions.

## Core Concepts

### Shared Meaning
Terms have agreed definitions within context.
### Model Alignment
Language reflects actual domain concepts and behavior.
### Context Boundary
The same word may differ outside the bounded context.
### Evolution
Language changes as understanding improves.

## How It Works

Teams use the same domain terms in conversation, models, requirements, tests, and code where appropriate, resolving ambiguity as it appears.

## When to Use

Use in domain modeling, requirement review, glossary work, and cross-team communication.

## When Not to Use

Do not force one term across contexts when meanings legitimately differ.

## Advantages

Reduces translation errors and exposes conceptual disagreement early.

## Limitations

Language can become jargon if definitions are not maintained.

## Examples

If `allocation` means reserving stock, tests should not use it interchangeably with physical shipment or financial allocation.

## Best Practices

- Prefer stakeholder-recognized business terms.
- Define ambiguous words.
- Keep context explicit.
- Update artifacts when terminology changes.

## Related Knowledge

- `Domain-Terminology.md`
- `Bounded-Context.md`
- `Domain-Model.md`

## References

- Domain-driven design literature.