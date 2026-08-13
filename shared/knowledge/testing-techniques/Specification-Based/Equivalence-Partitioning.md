# Equivalence Partitioning

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Equivalence Partitioning (EP)** divides an input or condition domain into groups whose members are expected to be treated equivalently by the system. Instead of testing every possible value, QA selects representative values from meaningful valid and invalid partitions.

## Purpose

Reduce redundant tests while preserving systematic coverage of distinct behavioral classes.

## Core Concepts

### Equivalence Class
A set of values expected to produce the same type of behavior under the same rule.

### Valid Partition
Values that satisfy the rule or accepted domain.

### Invalid Partition
Values that violate the rule in materially different ways.

### Representative Value
A selected member used to exercise one partition. It should be typical of the partition and not accidentally overlap a boundary objective.

### Independent Dimensions
Multiple fields or conditions may each have their own partitions. Their combinations require additional reasoning and may need Decision Table or combinatorial techniques.

## How It Works

```text
Requirement / rule
      ↓
Identify input or condition domain
      ↓
Separate behaviorally distinct classes
      ↓
Label valid and invalid partitions
      ↓
Choose representative values
      ↓
Combine with boundary / rule / state coverage as needed
```

Partitions must be based on expected behavior, not arbitrary numeric ranges.

## When to Use

Use for input validation, categories, ranges, enums, role groups, formats, account states, file types, or any domain where many values are expected to behave alike.

## When Not to Use

Do not use EP alone when behavior changes at exact boundaries, depends on condition combinations, transitions between states, sequence, or pairwise interactions.

## Advantages

- Reduces unnecessary duplicate tests.
- Makes valid and invalid classes explicit.
- Scales well for large value domains.
- Provides a foundation for Boundary Value Analysis.

## Limitations

- Poor partition definitions can hide defects.
- Values inside a partition may not actually be equivalent if undocumented rules exist.
- EP does not automatically cover boundaries or cross-field interactions.

## Examples

### Age Rule
If age 18–65 is accepted, partitions may be `<18`, `18–65`, and `>65`. EP selects one representative from each; BVA separately tests 17, 18, 65, and 66.

### File Type
If only `.xlsx` is accepted, `.xlsx`, unsupported spreadsheet types, and non-spreadsheet files may form distinct partitions if the system handles them differently.

### Account State
`Active`, `Locked`, `Disabled`, and `Expired` should not be merged into one invalid partition if each state has different expected behavior.

## Best Practices

- Derive partitions from authoritative rules.
- Separate invalid classes when expected outcomes differ.
- Avoid mixing boundary objectives into representative selection.
- Document assumptions where the domain is ambiguous.
- Combine EP with BVA, Decision Tables, and state techniques when appropriate.
- Revisit partitions when requirements change.

## Related Knowledge

- `Boundary-Value-Analysis.md`
- `Decision-Table-Testing.md`
- `../Foundation/Black-Box-Testing.md`
- `../Combinatorial/Pairwise-Testing.md`
- `../../qa/Requirement-Analysis.md`

## References

- ISTQB specification-based test techniques.
- ISO/IEC/IEEE 29119 test-design concepts.