# Modified Condition Decision Coverage (MC/DC)

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Modified Condition Decision Coverage (MC/DC)** is a strong structural coverage criterion requiring evidence that each atomic condition in a decision can independently affect the overall decision outcome. It is commonly associated with high-assurance and safety-critical software contexts.

## Purpose

Provide a disciplined method for demonstrating condition independence without requiring exhaustive testing of every boolean combination.

## Core Concepts

### Atomic Condition
An individual boolean predicate within a decision.

### Decision Outcome
The overall true/false result controlling execution.

### Independent Effect
For each condition, there must be paired test situations where changing that condition changes the decision outcome while other relevant conditions are held appropriately controlled according to the selected MC/DC interpretation.

### Masking and Short-Circuiting
Language semantics can affect whether a condition influences or is evaluated within a decision.

### Coverage Evidence
MC/DC claims require traceable tests and tool/analysis evidence, especially when external standards mandate it.

## How It Works

```text
Identify compound decision
      ↓
Decompose atomic conditions
      ↓
Construct truth relationships
      ↓
Find independence pairs for each condition
      ↓
Execute and measure
      ↓
Review masking, short-circuit, unreachable combinations
```

## When to Use

Use when required by applicable safety/assurance standards, project policy, or risk analysis for critical decision logic.

## When Not to Use

Do not impose MC/DC generically on ordinary application code without a justified requirement. The analysis and maintenance cost can be substantial.

## Advantages

- Stronger than simple decision or condition coverage.
- Demonstrates independent influence of conditions.
- Achieves strong boolean-logic evidence with fewer cases than full truth-table enumeration in many situations.

## Limitations

- More complex to design and review.
- Language and tool semantics matter.
- Some combinations may be infeasible.
- Coverage does not prove requirements or algorithms are correct.
- Regulatory/standard applicability must not be assumed.

## Examples

For `A && B`, tests can show A independently changes the decision while B is held true, and B independently changes it while A is held true.

For larger expressions, QA constructs independence pairs carefully rather than assuming all true/false permutations are necessary or sufficient.

## Best Practices

- Confirm whether MC/DC is actually required.
- Use qualified or approved tooling when mandated by project governance.
- Document atomic-condition decomposition and independence pairs.
- Account for short-circuit and masking semantics.
- Review infeasible combinations with engineering stakeholders.
- Pair structural evidence with requirement and hazard/risk coverage.

## Related Knowledge

- `Condition-Coverage.md`
- `Decision-Coverage.md`
- `Branch-Coverage.md`
- `../Foundation/White-Box-Testing.md`

## References

- ISTQB structure-based coverage concepts.
- Applicable project/safety standard when MC/DC is required.
- Target language and coverage-tool documentation.