# Domain Terminology

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Domain terminology** is the vocabulary used by stakeholders to describe business concepts, roles, states, events, rules, and outcomes. Consistent terminology is essential because the same word can have different meanings across domains or bounded contexts.

## Purpose

Help QA and QA-AI interpret requirements consistently, expose ambiguous terms, and avoid silently translating business language into incorrect technical assumptions.

## Core Concepts

### Term
A named business concept with an agreed meaning.

### Definition
The meaning of a term within a specific context.

### Synonym and Alias
Different labels may refer to the same concept; equivalence must be confirmed.

### Homonym
The same label may represent different concepts in different contexts.

### Controlled Vocabulary
An approved set of terms reduces ambiguity in requirements and artifacts.

## How It Works

Terminology is collected from requirements, SMEs, policies, UI labels, process documents, and existing models; definitions are reconciled within context and then reused consistently across analysis and testing.

## When to Use

Use during requirement review, domain onboarding, integration work, glossary creation, and whenever terms are overloaded or inconsistent.

## When Not to Use

Do not force one universal definition across contexts when the business intentionally uses different meanings.

## Advantages

Clear terminology reduces misunderstanding, duplicate concepts, incorrect scenarios, and communication defects.

## Limitations

Language evolves and local teams may use legacy or informal terms. A glossary is useful only when ownership and context are clear.

## Examples

`Customer`, `member`, and `account holder` may overlap but are not automatically equivalent. `Posted` can mean finalized in one financial process and merely recorded in another.

## Best Practices

- Define terms in business language.
- Record context and ownership.
- Flag conflicting definitions explicitly.
- Reuse approved terms in test artifacts.
- Avoid replacing business terms with implementation names unless mapping is documented.

## Related Knowledge

- `Business-Domain.md`
- `Ubiquitous-Language.md`
- `Bounded-Context.md`
- `Business-Context.md`

## References

- `../../glossary/Business-Terms.md`
- Project glossaries and authoritative business documentation.