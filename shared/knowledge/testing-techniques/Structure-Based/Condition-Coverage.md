# Condition Coverage

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Condition Coverage** evaluates whether each atomic boolean condition within a compound decision has evaluated both true and false during testing.

## Purpose

Expose gaps hidden by decision-only coverage when multiple conditions combine to produce one overall outcome.

## Core Concepts

### Atomic Condition
A boolean sub-expression that can independently evaluate true or false.

### Compound Decision
A logical expression containing multiple atomic conditions.

### Short-Circuit Evaluation
Some languages skip later conditions once the overall decision is determined, affecting whether conditions are actually evaluated.

### Condition vs Decision Outcome
All conditions can take both values without guaranteeing that the whole decision takes both outcomes, and vice versa.

## How It Works

```text
Identify compound decisions
      ↓
Decompose into atomic conditions
      ↓
Design tests so each condition evaluates T and F
      ↓
Account for short-circuit evaluation
      ↓
Confirm overall behavior and coverage
```

## When to Use

Use for complex boolean logic, authorization, validation, safety checks, eligibility, and any decision where individual condition behavior matters.

## When Not to Use

Do not assume condition coverage proves each condition independently affects the decision. That is the stronger objective of MC/DC.

## Advantages

- Reveals atomic-condition gaps.
- Improves visibility into compound boolean expressions.
- Helps expose short-circuit-related blind spots.

## Limitations

- Can require more tests than decision coverage.
- Does not prove condition independence.
- Does not guarantee all combinations or paths.
- Tool instrumentation may treat complex expressions differently.

## Examples

For `A && B`, tests should cause `A` and `B` each to evaluate true and false. Because of short-circuiting, a test with `A=false` may prevent `B` from being evaluated at all.

For `roleAllowed || ownsObject`, both conditions should be observed as true and false across tests, not merely the combined decision.

## Best Practices

- Decompose expressions accurately.
- Consider short-circuit rules of the language.
- Pair condition coverage with decision coverage.
- Use truth tables for complex expressions.
- Escalate to MC/DC only when required by risk or standard.

## Related Knowledge

- `Decision-Coverage.md`
- `Branch-Coverage.md`
- `Modified-Condition-Decision-Coverage-(MC-DC).md`
- `../Specification-Based/Decision-Table-Testing.md`

## References

- ISTQB condition coverage concepts.
- Target language evaluation semantics.