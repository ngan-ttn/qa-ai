# Mutation Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Mutation Testing** evaluates test-suite effectiveness by making small controlled changes (mutants) to implementation logic and checking whether existing tests detect the change. A killed mutant means at least one test fails; a surviving mutant may indicate weak assertions, missing coverage, an equivalent mutation, or irrelevant code.

## Purpose

Assess whether tests are sensitive to plausible implementation faults rather than merely executing code.

## Core Concepts

### Mutant
A modified program version created by a mutation operator.

### Mutation Operator
A rule that changes code in a fault-like way, such as altering a comparison, boolean operator, arithmetic operator, or constant.

### Killed Mutant
A mutant detected because the test suite produces a failing result.

### Surviving Mutant
A mutant not detected by the tests.

### Equivalent Mutant
A change that does not alter observable behavior for any relevant input and therefore cannot be killed by tests.

### Mutation Score
A ratio based on killed versus non-equivalent mutants, subject to tool and project definitions.

## How It Works

```text
Baseline tests pass
      ↓
Generate controlled mutants
      ↓
Run relevant tests against each mutant
      ↓
Classify killed / survived / equivalent / invalid
      ↓
Inspect survivors for coverage or assertion gaps
```

## When to Use

Use for critical business logic, libraries, calculation code, validation, security-sensitive decisions, or mature automated test suites where statement/branch coverage is already high but assertion strength is uncertain.

## When Not to Use

Do not use mutation testing blindly across very large systems without cost controls. It is also unsuitable as a replacement for requirement-based testing or as a universal release gate without project-defined policy.

## Advantages

- Tests assertion quality, not just execution.
- Finds weak tests hidden behind high coverage metrics.
- Provides actionable evidence about fault-detection sensitivity.

## Limitations

- Computationally expensive.
- Equivalent mutants require review.
- Results depend on mutation-operator quality.
- Surviving mutants do not automatically mean a defect exists.

## Examples

Changing `amount >= limit` to `amount > limit` should be detected by boundary tests if inclusive behavior matters.

Replacing `AND` with `OR` in an authorization condition should be detected by condition-combination tests.

## Best Practices

- Start with risk-critical modules.
- Use incremental or diff-based mutation where available.
- Review surviving mutants qualitatively.
- Combine with branch/condition and requirement coverage.
- Exclude generated or trivial code only through explicit policy.
- Do not optimize solely for mutation score.

## Related Knowledge

- `../Structure-Based/Branch-Coverage.md`
- `../Structure-Based/Condition-Coverage.md`
- `Property-Based-Testing.md`
- `../../qa/Test-Metrics.md`

## References

- Mutation testing research literature.
- Target mutation-tool documentation.