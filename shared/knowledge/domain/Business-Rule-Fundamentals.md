# Business Rule Fundamentals

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **business rule** is an explicit constraint, decision, derivation, obligation, policy, or exception that governs business behavior. Rules explain what must, may, or must not happen under defined conditions.

## Purpose

Give QA and QA-AI a rigorous framework for identifying, structuring, validating, and testing business rules without confusing them with implementation details or inventing missing policy.

## Core Concepts

### Condition
A fact or context that determines whether a rule applies.

### Outcome
The required result when conditions are satisfied.

### Scope
The actor, product, state, market, time period, or population to which the rule applies.

### Constraint Rule
Restricts what is allowed.

### Decision Rule
Selects an outcome among alternatives.

### Calculation Rule
Derives a value from inputs and formula semantics.

### Eligibility Rule
Determines whether an actor, entity, or transaction qualifies.

### Exception Rule
Overrides or alters normal behavior under defined circumstances.

### Rule Precedence
When rules overlap, precedence determines which rule wins. Precedence must come from authoritative business evidence.

### Effective Period
Rules may become active, expire, or change at specific dates/times.

### Default / No-Match Behavior
The expected result when no explicit condition matches must be defined rather than assumed.

### Rule Version and Source
The authority, version, and approval state of a rule matter when documents conflict.

## How It Works

```text
Business facts + context
        ↓
Determine applicable rules
        ↓
Resolve scope / precedence / effective date
        ↓
Decision / validation / calculation
        ↓
Observable outcome + evidence
```

QA converts each rule into explicit conditions and outcomes, then tests individual conditions, combinations, boundaries, exceptions, and conflicts. If source documents disagree, the discrepancy is a requirement issue, not something QA should silently resolve.

## When to Use

Use in requirement analysis, acceptance-criteria review, scenario generation, decision tables, calculation testing, policy-heavy workflows, and defect analysis.

## When Not to Use

Do not infer missing rules from common industry practice. Do not assume implementation behavior is the intended business rule merely because the system currently behaves that way.

## Advantages

Explicit rule modeling improves traceability, systematic coverage, conflict detection, and change-impact analysis.

## Limitations

Rules can be distributed across documents, embedded in manual processes, effective-dated, market-specific, or dependent on other rules. Complex rule combinations can produce combinatorial test growth.

## Examples

### Eligibility
`A refund is allowed only when the transaction is completed, the request is within the approved period, and the transaction has not already been fully refunded.`

### Precedence
A general discount applies to all members, but a campaign-specific rule may override the rate for an eligible segment during a defined period. The precedence must be explicit.

### No Match
A scoring matrix defines outcomes for several bands. QA must clarify what happens when an input falls outside every band instead of assuming rejection or zero.

## Best Practices

- Express each rule as conditions, scope, and outcome.
- Identify source, owner, version, and effective period.
- Separate normal rules, defaults, and exceptions.
- Clarify precedence when rules overlap.
- Test each condition independently and in meaningful combinations.
- Cover boundary values and no-match behavior.
- Trace derived scenarios back to the rule source.
- Record ambiguity instead of inventing policy.

## Related Knowledge

- `Validation-Rules.md`
- `Decision-Rules.md`
- `Calculation-Rules.md`
- `Eligibility-Rules.md`
- `Rule-Exceptions.md`
- `Business-Context.md`
- `../testing-techniques/Specification-Based/Decision-Table-Testing.md`

## References

- Business Rules Group and business-analysis literature.
- Approved policy and requirement sources.
