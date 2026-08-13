# Domain Terminology

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Domain terminology** is the vocabulary used by business stakeholders to describe concepts, states, roles, actions, rules, and outcomes. Correct terminology is a prerequisite for correct requirement interpretation because the same word can carry different meanings across products or contexts.

## Purpose

Help QA and QA-AI identify, normalize, validate, and safely use domain terms without replacing authoritative definitions with generic assumptions.

## Core Concepts

### Term
A word or phrase with defined business meaning.

### Definition
The agreed meaning and boundary of a term in a specific context.

### Synonym
Different terms that stakeholders use for the same concept. Synonyms can be useful but can also hide inconsistent language.

### Homonym / Ambiguous Term
One term may refer to different concepts in different contexts, such as `account`, `status`, or `customer`.

### State Vocabulary
State names often encode lifecycle meaning. Similar labels such as `Approved`, `Active`, and `Completed` should not be assumed equivalent.

### Context Ownership
A term may have one meaning in one bounded context and a different meaning elsewhere.

### Canonical Vocabulary
A glossary or ubiquitous language can establish preferred terms for shared communication.

## How It Works

```text
Requirement wording
      ↓
Identify domain terms
      ↓
Locate authoritative definitions
      ↓
Resolve synonyms / ambiguity
      ↓
Apply meaning within context
      ↓
Trace into rules and scenarios
```

When definitions conflict, QA should capture the conflict and its source rather than choosing one silently.

## When to Use

Use during requirement analysis, business-rule extraction, domain onboarding, defect triage, API/data mapping, and any activity where inconsistent wording can change expected behavior.

## When Not to Use

Do not force terminology uniformity when different contexts intentionally use different meanings. Do not create definitions solely from UI labels or code names when business meaning is unknown.

## Advantages

Clear terminology reduces misunderstanding, duplicate concepts, invalid assumptions, and inconsistent test expectations.

## Limitations

Terminology evolves. Legacy systems, regulatory language, partner integrations, and internal teams may use competing vocabularies.

## Examples

### Account
In banking, `account` may mean a financial account. In identity management, it may mean a login identity. A requirement saying “account status” is ambiguous until context is established.

### Remaining Quantity
A warehouse or permit domain may distinguish approved quantity, allocated quantity, consumed quantity, and remaining quantity. QA should confirm formula and timing rather than infer them from labels.

### Approved
An object can be business-approved while still not executable because another prerequisite is pending. State semantics must be explicit.

## Best Practices

- Maintain a source-linked glossary for important terms.
- Capture synonyms and deprecated terms explicitly.
- Record context when one term has multiple meanings.
- Treat state names, role names, and calculation labels as high-risk terminology.
- Use authoritative definitions in QA artifacts.
- Raise terminology conflicts as clarification questions.
- Avoid renaming business concepts in tests unless mapping is explicit.

## Related Knowledge

- `Business-Domain.md`
- `Domain-Knowledge.md`
- `Ubiquitous-Language.md`
- `Bounded-Context.md`
- `../../glossary/Business-Terms.md`

## References

- Project glossary and approved business documentation.
- Business-analysis and domain-modeling literature.
