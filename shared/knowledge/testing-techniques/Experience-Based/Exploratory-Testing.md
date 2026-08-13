# Exploratory Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Exploratory Testing** integrates learning, test design, and execution as mutually reinforcing activities. The tester continuously adapts based on observations rather than following only pre-scripted cases.

## Purpose

Discover risks, ambiguities, unexpected behavior, and interaction defects efficiently while learning how the product actually behaves.

## Core Concepts

### Simultaneous Learning and Testing
New observations immediately influence subsequent test ideas.

### Charter
A focused mission or risk area guides exploration without prescribing every step.

### Heuristics
Mental models, checklists, boundaries, histories, and domain patterns generate new experiments.

### Observation and Oracles
The tester compares behavior with requirements, consistency expectations, domain knowledge, standards, comparable features, and other defensible oracles.

### Adaptation
Testing direction changes when new evidence suggests higher-value paths.

## How It Works

```text
Define mission / risk
      ↓
Explore feature and context
      ↓
Observe behavior
      ↓
Form new hypotheses
      ↓
Run focused experiments
      ↓
Capture findings and coverage notes
      ↺
```

## When to Use

Use for new or changing features, ambiguous requirements, defect investigation, usability risks, integration-heavy behavior, regression hotspots, and time-constrained risk discovery.

## When Not to Use

Do not rely on unstructured exploration alone when repeatable evidence, formal traceability, regulated scripts, or deterministic regression execution is required.

## Advantages

- Responds quickly to new information.
- Effective for unknown unknowns.
- Encourages critical thinking and product learning.
- Can uncover defects outside scripted expectations.

## Limitations

- Coverage can be hard to communicate without notes or charters.
- Results depend strongly on tester skill.
- Reproduction suffers if evidence is weak.
- Unbounded exploration can waste time.

## Examples

A tester exploring an approval screen notices that editing in one tab changes state while another tab remains stale, leading to concurrency and stale-data experiments not present in scripted cases.

While exploring a file import, a partial-failure pattern suggests testing retry, duplicate import, result-file consistency, and idempotency.

## Best Practices

- Use clear charters and time boxes.
- Capture data, environment, sequence, and evidence for findings.
- Maintain coverage notes and open questions.
- Use heuristics deliberately rather than randomly clicking.
- Convert valuable discoveries into repeatable regression tests when appropriate.
- Pair exploration with requirements and risk analysis.

## Related Knowledge

- `Session-Based-Testing.md`
- `Error-Guessing.md`
- `Checklist-Based-Testing.md`
- `../../qa/Risk-Based-Testing.md`
- `../../qa/Defect-Reporting.md`

## References

- Exploratory testing literature.
- ISTQB experience-based testing concepts.