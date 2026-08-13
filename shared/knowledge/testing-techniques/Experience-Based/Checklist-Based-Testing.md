# Checklist-Based Testing

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Checklist-Based Testing** uses a curated set of conditions, risks, or quality reminders to guide testing without prescribing complete step-by-step cases.

## Purpose

Reuse organizational and tester knowledge consistently while retaining enough flexibility to adapt checks to the feature under test.

## Core Concepts

### Checklist Item
A concise reminder of a behavior, risk, or question to verify.

### Reusability
Items should be generic enough to apply across features but specific enough to trigger meaningful testing.

### Context Adaptation
Not every checklist item applies to every feature; applicability must be evaluated.

### Maintenance
Checklists evolve from defect history, incidents, standards, product changes, and review findings.

### Guidance vs Script
A checklist guides coverage but does not fully define data, steps, or exact expected results like a detailed test case.

## How It Works

QA selects an appropriate checklist, filters relevant items, interprets them in feature context, executes suitable checks, records results or findings, and feeds new lessons back into checklist maintenance.

## When to Use

Use for recurring feature reviews, smoke/sanity support, UI/API/upload/security hygiene, regression hotspots, review activities, and onboarding less experienced testers.

## When Not to Use

Do not treat a generic checklist as proof of requirement coverage. Avoid blindly running irrelevant items or replacing precise high-risk scenarios with vague reminders.

## Advantages

- Reuses defect-prevention knowledge.
- Fast to apply.
- Improves consistency across testers.
- Flexible across similar features.

## Limitations

- Can become stale or bloated.
- Encourages superficial checking if items are vague.
- Coverage is not automatically traceable to requirements.
- Generic lists can miss feature-specific risks.

## Examples

An upload checklist may prompt checks for file type, size, duplicate import, partial failure, malformed content, permission, result reporting, and retry behavior.

An API checklist may prompt authentication, authorization, schema, error, idempotency, pagination, and rate behavior while detailed API strategy remains elsewhere.

## Best Practices

- Keep items concise and actionable.
- Maintain ownership and review cadence.
- Remove obsolete or duplicate items.
- Tag items by context or risk where useful.
- Combine checklists with requirement-driven techniques.
- Add new items from escaped defects and incidents.
- Avoid converting the checklist into an unmaintainable mega-script.

## Related Knowledge

- `Exploratory-Testing.md`
- `Error-Guessing.md`
- `Session-Based-Testing.md`
- `../../checklists/`
- `../../qa/Regression-Testing.md`

## References

- ISTQB checklist-based testing concepts.
- Repository checklists and approved defect learnings.