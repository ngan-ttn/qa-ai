# Statement Coverage

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Statement Coverage** measures whether executable statements in the target code were executed by the test suite. It is one of the simplest structure-based coverage measures and provides a baseline view of exercised implementation.

## Purpose

Identify executable code that has not been run by tests and establish a basic structural-coverage signal without treating execution alone as proof of correctness.

## Core Concepts

### Executable Statement
A code instruction that can be executed at runtime under the target language and tooling model.

### Coverage Ratio
A common form is `executed statements / total executable statements`, subject to tool-specific counting rules.

### Instrumentation
Coverage tools observe execution through instrumentation, tracing, or runtime hooks.

### Assertion Quality
A statement can be covered while its result is not meaningfully verified.

## How It Works

```text
Instrument target code
      ↓
Run selected tests
      ↓
Record executed statements
      ↓
Compare with executable statement set
      ↓
Investigate uncovered code and weak assertions
```

Statement coverage does not distinguish whether alternative decision outcomes were exercised.

## When to Use

Use as a basic structural signal during unit/component testing, regression analysis, coverage review, and investigation of apparently untested implementation areas.

## When Not to Use

Do not use statement coverage alone as a release-quality target or as proof that decisions, conditions, requirements, or error paths are adequately tested.

## Advantages

- Simple to understand and measure.
- Highlights completely unexecuted code.
- Useful as a first structural-coverage baseline.

## Limitations

- Can reach high percentages without exercising both sides of decisions.
- Does not prove assertions are meaningful.
- Tool counting semantics can differ.
- Generated, unreachable, defensive, or environment-specific code can distort interpretation.

## Examples

If an `if/else` contains one statement in each branch, tests that execute only the `if` branch may cover most surrounding statements but still miss the `else` behavior.

A logging statement can be covered without verifying the business result that caused it.

## Best Practices

- Pair statement coverage with branch/decision coverage where risk warrants it.
- Review uncovered lines qualitatively.
- Exclude generated code only through documented policy.
- Use meaningful assertions, not execution-only tests.
- Interpret percentages in context rather than using generic thresholds.

## Related Knowledge

- `Branch-Coverage.md`
- `Decision-Coverage.md`
- `../Foundation/White-Box-Testing.md`
- `../../qa/Test-Metrics.md`

## References

- ISTQB structure-based testing terminology.
- Target coverage-tool documentation.