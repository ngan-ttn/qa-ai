# Domain Knowledge

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Domain knowledge** is structured understanding of a business area: its terminology, actors, entities, processes, rules, events, exceptions, risks, and constraints.

## Purpose

Explain how reusable domain knowledge supports QA reasoning without replacing current project evidence or subject-matter expertise.

## Core Concepts

### Explicit Knowledge
Documented rules, policies, models, specifications, and definitions.

### Tacit Knowledge
Operational understanding held by experienced stakeholders but not fully documented.

### Authoritative Knowledge
Information accepted as the source of truth for a decision or rule.

### Contextual Knowledge
Meaning that depends on product, market, jurisdiction, role, or lifecycle state.

## How It Works

QA gathers evidence, identifies concepts and relationships, validates understanding with authoritative sources, and applies that knowledge to requirement analysis, risk assessment, scenarios, and defect impact.

## When to Use

Use throughout analysis, test design, regression planning, defect triage, and onboarding.

## When Not to Use

Do not treat historical knowledge or generic industry patterns as proof of current product behavior.

## Advantages

Domain knowledge increases relevance of testing and helps reveal omissions that syntax-focused review misses.

## Limitations

Knowledge can become stale, incomplete, contradictory, or jurisdiction-specific.

## Examples

Knowing that refunds may have eligibility, settlement, reversal, and notification stages helps QA ask better questions than testing only a `Refund` button.

## Best Practices

- Track source and context.
- Prefer current authoritative evidence.
- Separate fact, assumption, and inference.
- Refresh knowledge when business policy changes.
- Capture unresolved questions rather than invent answers.

## Related Knowledge

- `Business-Domain.md`
- `Business-Context.md`
- `Domain-Terminology.md`
- `Domain-Model.md`

## References

- Business-analysis and knowledge-management literature.
- Approved project/domain sources.