# Decision Rules

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

A **decision rule** maps a set of business conditions to one or more outcomes. Decision logic can be simple, hierarchical, mutually exclusive, overlapping, or dependent on precedence.

## Purpose

Help QA structure decision logic so missing combinations, conflicting outcomes, defaults, and precedence defects become visible.

## Core Concepts

### Input Fact
A business fact used by the decision, such as status, role, amount, type, or date.

### Condition
A predicate evaluated against input facts.

### Outcome
The action, classification, permission, rate, route, or decision produced.

### Decision Table
A structured representation of combinations and outcomes.

### Mutual Exclusivity
Rules may be intended so exactly one outcome matches.

### Overlap
More than one rule may match, requiring explicit priority or aggregation behavior.

### Default
Fallback behavior when no specific rule matches.

### Precedence
An ordering or priority used to resolve competing rules.

## How It Works

QA identifies independent conditions, enumerates meaningful combinations, maps expected outcomes, then checks for gaps, impossible combinations, and overlapping rules.

```text
Facts
 ↓
Conditions evaluated
 ↓
0 / 1 / many rules match
 ↓
apply default or precedence
 ↓
outcome
```

## When to Use

Use for approvals, pricing, eligibility, routing, permissions, risk classification, fees, and rule-driven status behavior.

## When Not to Use

Do not build exhaustive combinations blindly when conditions are dependent or impossible. Do not assume first-match or highest-priority behavior unless defined.

## Advantages

Decision modeling exposes missing cases and contradictory logic more effectively than prose review alone.

## Limitations

Large condition sets can create combinatorial explosion. Hidden dependencies or effective-dated rules can make a decision table incomplete.

## Examples

A transaction route depends on amount band, customer type, account status, and risk flag. Some combinations may be invalid; others may require escalation rather than approval/rejection.

A discount decision can have a default rate plus campaign override. QA tests overlap and confirms which rule wins.

## Best Practices

- Normalize conditions into unambiguous facts.
- Identify impossible combinations before generating cases.
- Define no-match and multi-match behavior.
- Capture precedence explicitly.
- Use decision tables for complex combinations.
- Include effective-date and scope conditions.
- Trace every outcome to source rules.
- Review decision logic with business owners before treating it as baseline.

## Related Knowledge

- `Business-Rule-Fundamentals.md`
- `Eligibility-Rules.md`
- `Rule-Exceptions.md`
- `../testing-techniques/Specification-Based/Decision-Table-Testing.md`

## References

- Decision-modeling and business-rules literature.
- Approved decision policy.
