# Testing Techniques

## Purpose

The `testing-techniques` knowledge module provides reusable knowledge about software testing perspectives and test-design techniques used by human QA engineers and QA-AI capabilities.

It explains **how tests are selected or derived**. It does not own generic QA lifecycle/process management, API/database technology knowledge, or project-specific business rules.

## Scope

The approved architecture contains seven categories and 30 knowledge articles:

```text
Testing Techniques
├── Foundation                 3
├── Specification-Based       6
├── Structure-Based           6
├── Experience-Based          4
├── Combinatorial             3
├── Model-Based               2
└── Advanced                  6
                              ──
Total                         30
```

## Module Structure

```text
shared/knowledge/testing-techniques/
├── README.md
├── Catalog.md
├── Foundation/
├── Specification-Based/
├── Structure-Based/
├── Experience-Based/
├── Combinatorial/
├── Model-Based/
└── Advanced/
```

Each category contains its own `README.md` plus knowledge articles. `Catalog.md` is the authoritative article inventory, classification, prerequisite, priority, and lifecycle-status source.

## Knowledge Article Standard

Every knowledge article follows `../../standards/Knowledge-Article.md` and uses:

```text
# Article Title

> Version: 1.0.0
> Status: Approved
> Last Updated: YYYY-MM-DD

## Overview
## Purpose
## Core Concepts
## How It Works
## When to Use
## When Not to Use
## Advantages
## Limitations
## Examples
## Best Practices
## Related Knowledge
## References
```

Optional sections are allowed only when they add meaningful value and must not replace mandatory sections.

## Ownership Boundary

| Topic | Owner |
|---|---|
| Test derivation and test-design techniques | `testing-techniques/` |
| QA lifecycle, planning, defect and generic quality practices | `../qa/` |
| API protocols and API-specific testing | `../api/` |
| SQL, persistence and database-specific testing | `../database/` |
| Business concepts, entities, workflows and industry knowledge | `../domain/` |

Testing-technique articles should reference neighboring domains instead of duplicating their primary responsibility.

## Recommended Learning Path

```text
Foundation
   ↓
Specification-Based
   ↓
Experience-Based
   ↓
Structure-Based
   ↓
Combinatorial
   ↓
Model-Based
   ↓
Advanced
```

This is guidance, not a mandatory execution order. Technique selection depends on the test objective and risk.

## QA-AI Usage

Testing-technique knowledge supports requirement analysis, scenario generation, testcase generation, coverage review, test-data design, regression analysis, and exploratory/risk reasoning.

QA-AI must use authoritative project requirements as the test oracle. Generic knowledge may suggest techniques or missing dimensions, but it must not invent expected behavior.

## Quality Gate

An article is Approved only when it:

- contains all 12 mandatory sections with correct `#`/`##` hierarchy;
- has sufficient semantic depth for standalone retrieval;
- uses a clear reasoning model rather than terminology lists only;
- includes practical QA examples and limitations;
- states assumptions and technique boundaries;
- preserves cross-domain ownership;
- avoids project-specific thresholds and rules;
- has accurate repository-relative cross-references;
- is useful for both human readers and AI reasoning.

A structurally complete but shallow article does not pass.

## Freeze Baseline

```text
Folder: shared/knowledge/testing-techniques/
Physical Knowledge Articles: 30
Cataloged Knowledge Articles: 30
Catalog Status: Approved
Baseline State: Frozen
Freeze Date: 2026-08-13
Review Level: Structural + Content Depth + Cross-Article + Cross-Domain
```

Future material changes require targeted review of affected articles and cross-reference impact before the baseline is frozen again.

## References

- `Catalog.md`
- `../../standards/Knowledge-Article.md`
- `../../glossary/QA-Terms.md`
- `../qa/`
- `../api/`
- `../database/`
- `../domain/`
- `../../../skills/`
- `../../../workflows/`