# Error Guessing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Error Guessing** is an experience-based technique in which testers use knowledge of common failure patterns, prior defects, architecture, domain behavior, and human mistakes to predict where defects are likely to exist.

## Purpose

Complement systematic techniques by targeting risks that formal specifications or models may not make obvious.

## Core Concepts

### Defect Heuristics
Reusable ideas such as null handling, duplicates, race conditions, stale data, partial failures, retries, timezone issues, rounding, and permission gaps.

### Historical Evidence
Past production incidents, escaped defects, recurring modules, and prior root causes can guide targeted tests.

### Domain Experience
Industry and product knowledge helps identify realistic misuse, unusual states, and business-specific failure patterns.

### Architecture Awareness
Understanding integrations, caches, queues, persistence, and external dependencies can reveal hidden error opportunities.

### Hypothesis
An error guess should be expressed as a testable defect hypothesis rather than an unbounded intuition.

## How It Works

```text
Known risks + prior defects + domain/technical experience
        ↓
Form defect hypotheses
        ↓
Prioritize by impact and plausibility
        ↓
Design targeted experiments
        ↓
Record evidence and reusable heuristics
```

## When to Use

Use during exploratory work, regression, defect investigation, risk-based testing, integration testing, and mature products with useful defect history.

## When Not to Use

Do not use error guessing as the sole basis for coverage where formal requirements, regulated evidence, or systematic test-design obligations exist.

## Advantages

- Fast and flexible.
- Uses real defect history and tester expertise.
- Finds issues missed by formal decomposition.
- Adapts well to incomplete specifications.

## Limitations

- Quality depends on tester experience.
- Coverage is difficult to measure objectively.
- Bias can over-focus on familiar defect types.
- New failure modes may be missed.

## Examples

For a payment flow, experienced testers may target duplicate submission, delayed callback, reversal after timeout, precision mismatch, or retries after partial completion.

For an upload feature, testers may try duplicate rows, inconsistent encodings, huge files, hidden sheets, repeated imports, and partial failures based on common defects.

## Best Practices

- Convert intuition into explicit hypotheses.
- Maintain reusable defect heuristics and incident learnings.
- Combine with structured techniques.
- Prioritize by risk rather than novelty.
- Record why a test was chosen.
- Refresh heuristics as architecture and products evolve.

## Related Knowledge

- `Exploratory-Testing.md`
- `Checklist-Based-Testing.md`
- `Session-Based-Testing.md`
- `../../qa/Defect-Analysis.md`
- `../../qa/Risk-Based-Testing.md`

## References

- ISTQB experience-based testing concepts.
- Project defect history and approved incident learnings.