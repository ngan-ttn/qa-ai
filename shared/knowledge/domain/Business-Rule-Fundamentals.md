# Business Rule Fundamentals

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **business rule** is an explicit constraint, decision, derivation, obligation, or policy that governs business behavior.

## Purpose

Give QA a foundation for identifying rules, separating them from implementation, and deriving positive, negative, boundary, and exception coverage.

## Core Concepts

### Constraint Rule
Restricts what is allowed.
### Decision Rule
Selects an outcome from conditions.
### Calculation Rule
Derives a value.
### Eligibility Rule
Determines qualification.
### Exception Rule
Overrides or alters normal behavior under defined conditions.

## How It Works

```text
Business facts + context
        ↓
Applicable rule
        ↓
Decision / validation / calculation
        ↓
Observable outcome
```

## When to Use

Use in requirement analysis, acceptance criteria review, scenario generation, and defect analysis.

## When Not to Use

Do not infer missing rules from common industry practice without confirmation.

## Advantages

Explicit rules improve traceability and systematic coverage.

## Limitations

Rules may conflict, depend on effective dates, or be distributed across sources.

## Examples

`A refund is allowed only within the approved period and only for eligible transaction states` contains both temporal and state conditions.

## Best Practices

- Express conditions and outcomes unambiguously.
- Identify precedence and exceptions.
- Test each condition independently and in combinations.
- Capture effective dates and scope.
- Trace rules to authoritative sources.

## Related Knowledge

- `Validation-Rules.md`
- `Decision-Rules.md`
- `Calculation-Rules.md`
- `Eligibility-Rules.md`
- `Rule-Exceptions.md`

## References

- Business Rules Group and business-analysis literature.