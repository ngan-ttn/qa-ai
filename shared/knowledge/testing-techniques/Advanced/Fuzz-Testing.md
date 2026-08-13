# Fuzz Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Fuzz Testing** automatically or semi-automatically supplies large volumes of malformed, unexpected, random, mutated, or coverage-guided inputs to discover crashes, hangs, parser faults, validation gaps, memory errors, and robustness/security issues.

## Purpose

Explore input spaces beyond manually designed examples and expose failures caused by unexpected data shapes or sequences.

## Core Concepts

### Fuzz Input
Generated or mutated data presented to a target interface.

### Seed Corpus
Initial valid or interesting inputs used as starting material for mutation-based fuzzing.

### Generator / Mutator
Mechanism that creates candidate inputs.

### Oracle
Crashes, hangs, sanitizer findings, invariant violations, unexpected status, or other measurable abnormal outcomes.

### Coverage-Guided Fuzzing
Uses execution feedback to favor inputs that reach new code regions.

### Reproducibility
Discovered failures need minimized, stable inputs for debugging and regression.

## How It Works

```text
Define target + safety boundary
      ↓
Provide seeds / grammar / generator
      ↓
Generate many inputs
      ↓
Observe crash, hang, invariant, sanitizer, coverage signals
      ↓
Minimize interesting failures
      ↓
Reproduce and convert to regression tests
```

## When to Use

Use for parsers, protocol handlers, file imports, APIs, serialization, compilers, security-sensitive input processing, or components exposed to untrusted data.

## When Not to Use

Do not fuzz production or shared environments without explicit authorization and isolation. Avoid using uncontrolled fuzzing where generated traffic can trigger irreversible business actions or unsafe side effects.

## Advantages

- Explores many unexpected inputs efficiently.
- Finds robustness issues humans may not anticipate.
- Works well with sanitizers and coverage feedback.
- Produces reusable crashing inputs.

## Limitations

- Functional business correctness may be under-tested.
- Reaching deep states can require good seeds or stateful models.
- Findings can be noisy without strong oracles.
- Safety and environment isolation are essential.

## Examples

A file parser is fuzzed with corrupted lengths, encodings, nested structures, and truncated content; crashes are minimized into deterministic regression files.

An API parser receives malformed JSON structures and boundary payload sizes in a controlled environment while ensuring no real downstream transaction is created.

## Best Practices

- Define authorized targets and rate limits.
- Use isolated data and environments.
- Preserve seeds and minimized repro cases.
- Add sanitizers/invariant checks when appropriate.
- Separate robustness fuzzing from business-rule tests.
- Convert confirmed findings into regression tests.

## Related Knowledge

- `Property-Based-Testing.md`
- `Mutation-Testing.md`
- `../Experience-Based/Error-Guessing.md`
- `../../api/Security-Testing.md`

## References

- Fuzzing and coverage-guided fuzzing literature.
- Target fuzzer and sanitizer documentation.