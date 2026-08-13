# Combinatorial Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Combinatorial Testing** systematically selects combinations of parameter values to cover interactions at a defined strength without executing the entire Cartesian product. Pairwise testing is the common two-way case; higher-strength covering arrays target three-way or greater interactions.

## Purpose

Control combinatorial explosion while making interaction coverage explicit and adjustable according to risk.

## Core Concepts

### Interaction Strength
`t-way` coverage requires every allowed combination of values across any `t` parameters to appear in at least one test.

### Covering Array
A compact test matrix designed to satisfy the requested interaction strength.

### Constraints
Rules describing impossible, invalid, or disallowed combinations.

### Seed / Required Tests
Known critical combinations can be forced into the generated suite.

### Model Quality
The technique covers only the parameters and values represented in the combinatorial model.

## How It Works

```text
Define factors + values
      ↓
Model constraints
      ↓
Choose interaction strength
      ↓
Generate covering array
      ↓
Inject critical combinations
      ↓
Review feasibility and coverage
```

## When to Use

Use for products with many configuration dimensions, compatibility matrices, integration options, roles/features, platform combinations, or parameterized APIs where interactions are a major risk.

## When Not to Use

Do not use combinatorial coverage to replace sequence, state, boundary, or precise business-rule testing. Avoid arbitrary high interaction strength without evidence because suite size grows quickly.

## Advantages

- Quantifies interaction coverage.
- Offers large reduction versus exhaustive combinations.
- Can incorporate constraints and mandatory cases.
- Scales from pairwise to higher strengths.

## Limitations

- Does not prove all defects are interaction defects of the chosen strength.
- Models can omit important factors.
- Constraints can make generation complex.
- Generated cases still need realistic data and expected results.

## Examples

A service supports authentication mode × payload format × region × role × feature flag. A 2-way or 3-way model can cover interactions systematically while manually seeding known regulatory or business-critical combinations.

A mobile app matrix may use device family × OS version × locale × account state while separate tests cover lifecycle and boundary behavior.

## Best Practices

- Choose interaction strength based on risk and evidence.
- Keep parameters semantically independent where possible.
- Encode constraints explicitly.
- Seed critical combinations.
- Review model changes whenever requirements or configuration options change.
- Combine with other test-design techniques.

## Related Knowledge

- `Pairwise-Testing.md`
- `Orthogonal-Array-Testing.md`
- `../Specification-Based/Decision-Table-Testing.md`
- `../../qa/Risk-Based-Testing.md`

## References

- NIST combinatorial interaction testing research.
- Covering-array testing literature.