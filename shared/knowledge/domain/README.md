# Domain Knowledge

## Purpose

`shared/knowledge/domain/` provides reusable business-domain knowledge for QA and QA-AI. It helps interpret requirements, business rules, processes, entities, industry context, compliance concerns, and domain models without inventing project-specific behavior.

## Scope

The module owns generic business/domain knowledge. QA process belongs in `../qa/`, test-design techniques in `../testing-techniques/`, API behavior in `../api/`, and database behavior in `../database/`.

Industry articles provide orientation and QA reasoning patterns only. They do not replace current project requirements, SME decisions, legal advice, regulatory interpretation, clinical guidance, accounting policy, or organization-specific rules.

## Knowledge Architecture

```text
Domain Knowledge
├── Domain Fundamentals        5
├── Business Processes         6
├── Business Entities          6
├── Business Rules             6
├── Industry Domains           7
├── Regulatory & Compliance    6
└── Domain Modeling            5
                              ──
                              41
```

## Article Standard

Every knowledge article follows `../../standards/Knowledge-Article.md` and contains:

```text
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

Metadata uses:

```text
Version: 1.0.0
Status: Approved
Last Updated: 2026-08-13
```

## Content-Depth Gate

Presence of headings alone is not sufficient. An approved article must also:

- explain the concept deeply enough for independent QA reasoning;
- distinguish generic knowledge from project-specific assumptions;
- include realistic QA-relevant examples;
- identify limitations, exceptions, or failure risks;
- avoid unsupported legal, regulatory, clinical, financial, or industry-specific claims;
- define boundaries with adjacent articles;
- provide useful cross-references;
- remain suitable for retrieval by QA-AI skills and workflows.

## Domain Safety and Evidence Rules

- Never infer project rules from generic industry patterns.
- Never invent thresholds, eligibility criteria, retention periods, calculations, permissions, SLAs, or regulatory obligations.
- Treat jurisdiction and effective date as material when regulation is involved.
- Prefer authoritative project/business sources when generic knowledge conflicts with current requirements.
- Record ambiguity as a clarification need rather than silently filling the gap.
- Keep business concepts separate from implementation representations unless an explicit mapping exists.

## Usage in QA-AI

Domain knowledge supports requirement analysis, business-rule extraction, risk analysis, scenario generation, test-case generation, regression analysis, and test-data reasoning. Skills should retrieve only relevant articles and combine them with the actual requirement context.

## Baseline

```text
Physical Knowledge Articles: 41
Cataloged Knowledge Articles: 41
Article Status: Approved
Baseline State: Frozen
Freeze Date: 2026-08-13
```

## References

- `Catalog.md`
- `../../standards/Knowledge-Article.md`
- `../../glossary/Business-Terms.md`
- `../qa/`
- `../api/`
- `../database/`
- `../testing-techniques/`