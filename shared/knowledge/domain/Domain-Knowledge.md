# Domain Knowledge

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Domain knowledge** is the accumulated understanding of a business area: its purpose, terminology, actors, capabilities, entities, processes, rules, events, risks, constraints, and operating context. It is broader than one requirement and narrower than universal business knowledge.

## Purpose

Provide a model for acquiring, validating, applying, and maintaining domain knowledge so QA and QA-AI can reason accurately without inventing missing project facts.

## Core Concepts

### Explicit Knowledge
Documented information such as specifications, policies, process maps, contracts, and glossaries.

### Tacit Knowledge
Operational understanding held by SMEs or experienced users that may not yet be documented.

### Evidence Strength
Not all sources have equal authority. Approved policy may outweigh outdated wiki content; observed production behavior may reveal a defect rather than define the requirement.

### Assumption
An unverified belief used temporarily for analysis. Assumptions must be labeled and validated.

### Knowledge Gap
Missing information that prevents confident interpretation or testing.

### Knowledge Freshness
Domain knowledge can expire when products, regulations, processes, or business ownership change.

### Reusability Boundary
Generic patterns can guide questions, but organization-specific rules must remain project evidence.

## How It Works

```text
Collect sources
   ↓
Extract concepts / rules / processes
   ↓
Assess authority + freshness
   ↓
Resolve conflicts / gaps
   ↓
Apply to QA reasoning
   ↓
Capture learned corrections
```

Knowledge should be traceable enough that a reviewer can distinguish a confirmed fact from an inference or generic pattern.

## When to Use

Use for onboarding, complex requirement analysis, regression planning, test-data design, defect investigation, cross-system integration, and repeated features within the same domain.

## When Not to Use

Do not use historical knowledge as a substitute for current requirements. Do not treat stakeholder memory or common industry practice as automatically authoritative.

## Advantages

Strong domain knowledge improves risk detection, clarification quality, coverage, defect severity assessment, and communication with business stakeholders.

## Limitations

Knowledge can be incomplete, inconsistent, biased, outdated, or local to one team. Overconfidence in prior domain experience can cause false assumptions.

## Examples

A QA engineer familiar with loyalty systems knows that earn, redeem, refund, expiry, and adjustment often interact. That knowledge helps ask relevant questions, but the actual point-expiry rule must still come from the current product.

For import permits, prior knowledge may suggest allocation and remaining quantity are related, but the exact formula and edit restrictions must be verified from current requirements.

## Best Practices

- Tag source, owner, date, and confidence for important domain facts.
- Separate confirmed facts, assumptions, and open questions.
- Prefer current authoritative evidence over memory.
- Reuse patterns to improve questioning, not to fill gaps silently.
- Capture material learning from defects and UAT decisions.
- Review knowledge after major policy or product changes.
- Keep generic repository knowledge free of confidential project data.

## Related Knowledge

- `Business-Domain.md`
- `Domain-Terminology.md`
- `Business-Context.md`
- `Ubiquitous-Language.md`

## References

- Business-analysis knowledge-management literature.
- Approved project and organization documentation.
