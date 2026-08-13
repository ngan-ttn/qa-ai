# Session-Based Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Session-Based Testing** structures exploratory testing into focused, time-bounded sessions with a charter, notes, coverage information, findings, and debriefing.

## Purpose

Preserve the adaptability of exploratory testing while improving accountability, repeatability, reviewability, and coverage communication.

## Core Concepts

### Charter
Defines the mission, scope, risks, data, or questions for a session.

### Time Box
Limits exploration to a planned duration so effort remains focused.

### Session Notes
Capture actions, observations, test ideas, data, environment, questions, and evidence.

### Findings
Defects, risks, questions, and coverage discoveries produced during the session.

### Debrief
A review of what was tested, what was learned, blockers, and what should happen next.

## How It Works

```text
Risk / objective
     ↓
Create charter
     ↓
Run time-boxed exploration
     ↓
Record notes + evidence
     ↓
Classify findings and coverage
     ↓
Debrief and plan follow-up
```

## When to Use

Use when exploratory work needs stronger structure, when teams need visibility into exploratory coverage, or when multiple testers divide a complex feature by risk-oriented charters.

## When Not to Use

Do not turn session-based testing into rigid scripting that removes exploration. It is also not a substitute for required formal execution records when those have stricter evidence rules.

## Advantages

- Makes exploratory effort visible.
- Improves focus and debrief quality.
- Supports collaboration and follow-up.
- Produces reusable learning artifacts.

## Limitations

- Requires disciplined note-taking.
- Poor charters can constrain learning or miss risk.
- Session metrics can be misused as productivity measures.
- Documentation overhead can become excessive if not proportionate.

## Examples

A 60-minute charter may focus on `Explore refund behavior around partial payment, timeout, and repeated submission using transaction-state and concurrency heuristics`.

A session for an import module may focus on `Explore recovery and duplicate behavior after partial row failures and repeated uploads`.

## Best Practices

- Write risk-focused charters, not generic feature names.
- Capture enough evidence to reproduce findings.
- Distinguish test execution time from setup/blocker time if measured.
- Debrief on learning, not only defect count.
- Convert important discoveries into backlog, scripted regression, or new charters.
- Avoid ranking testers by session defect counts.

## Related Knowledge

- `Exploratory-Testing.md`
- `Error-Guessing.md`
- `Checklist-Based-Testing.md`
- `../../qa/Test-Monitoring-and-Control.md`

## References

- Session-Based Test Management literature.
- Exploratory testing practices.