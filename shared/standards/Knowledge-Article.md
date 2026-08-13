# Knowledge Article Standard

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Purpose

The **Knowledge Article Standard** defines the mandatory structure, writing rules, quality gates, metadata expectations, and review requirements for reusable knowledge articles in QA-AI.

The standard exists to keep knowledge independently readable by humans, retrievable by AI, maintainable across domains, and safe from accidental project-specific assumptions.

## Scope

This standard applies to knowledge articles under:

```text
shared/knowledge/
├── testing-techniques/
├── qa/
├── api/
├── database/
└── domain/
```

`README.md`, `Catalog.md`, category indexes, standards, templates, checklists, datasets, skills, and workflows are not themselves Knowledge Articles and may use structures appropriate to their document type.

## Objectives

Knowledge articles must:

- explain one primary reusable concept;
- be understandable without hidden conversation context;
- support AI retrieval and reasoning;
- preserve authoritative-source and assumption boundaries;
- minimize duplication across knowledge domains;
- include enough depth to be useful beyond terminology lookup;
- remain maintainable as the repository evolves.

## Metadata Requirements

Every Knowledge Article must begin with:

```md
# Article Title

> Version: 1.0.0
> Status: Approved
> Last Updated: YYYY-MM-DD
```

Allowed lifecycle values are governed by `Metadata.md`. `Frozen` is a repository baseline state and must not be used as article lifecycle metadata.

Metadata must contain real values when an article is approved. Placeholder dates such as `YYYY-MM-DD` are not permitted in an Approved article.

## Heading Hierarchy

Knowledge Articles use:

```text
#  Article title — exactly one top-level heading
## Mandatory or optional major section
### Concept/subsection
#### Deeper subdivision only when genuinely needed
```

Mandatory sections must be `##` headings. Articles must not promote every major section to a second `#` heading.

## Mandatory Sections

Every Knowledge Article must contain all 12 sections below, in this order unless an approved exception improves clarity without harming retrieval:

1. `## Overview`
2. `## Purpose`
3. `## Core Concepts`
4. `## How It Works`
5. `## When to Use`
6. `## When Not to Use`
7. `## Advantages`
8. `## Limitations`
9. `## Examples`
10. `## Best Practices`
11. `## Related Knowledge`
12. `## References`

Optional sections may be inserted only when they add material value. Examples include Comparison, Common Mistakes, FAQ, Industry Applications, AI Considerations, or Implementation Notes.

Optional content must not replace or hollow out mandatory sections.

## Section Quality Requirements

### Overview

Define the concept, its scope, and the distinction that makes it worth its own article.

### Purpose

Explain why the concept matters to QA or QA-AI reasoning.

### Core Concepts

Present the reasoning model and important dimensions needed to understand the topic. A glossary-style list without relationships is insufficient for non-trivial topics.

### How It Works

Explain behavior, lifecycle, interaction, derivation, or decision flow. This section must add explanatory value rather than restating the definition.

### When to Use / When Not to Use

State applicability and boundaries. These sections prevent techniques or concepts from being applied universally without justification.

### Advantages / Limitations

Describe realistic strengths and failure boundaries. Limitations should include architectural, contextual, evidence, tool, or assumption constraints when relevant.

### Examples

Include practical QA-relevant examples sufficient to demonstrate reasoning. Examples may be illustrative but must not invent project-specific expected behavior.

### Best Practices

Provide actionable guidance that remains generic enough for reuse. Do not encode organization-specific governance as universal practice.

### Related Knowledge

Use repository-relative links or paths to conceptually related articles. Cross-domain references are encouraged when they preserve ownership instead of duplicating content.

### References

List stable standards, literature, vendor documentation, or authoritative project sources appropriate to the topic. Do not fabricate citations.

## Content-Depth Gate

An article does **not** pass merely because all 12 headings exist.

Approval additionally requires:

- enough semantic depth for standalone reading and AI retrieval;
- a clear reasoning model for the concept;
- realistic examples and meaningful limitations;
- explicit boundary with neighboring concepts;
- actionable QA applicability where relevant;
- assumption safety for project-specific, vendor-specific, legal, clinical, financial, security, or regulatory details;
- no unresolved contradiction with another approved article.

A structurally complete but semantically shallow skeleton must remain in Review or be rewritten before approval.

## Single-Responsibility Rule

Each article owns one primary concept.

Related concepts should be cross-referenced rather than merged when they have distinct reasoning responsibilities. Conversely, artificial fragmentation should be avoided when two tiny pages cannot stand independently.

## Knowledge Ownership and Cross-Domain Rules

The top-level knowledge domains own different responsibilities:

| Knowledge Domain | Primary Ownership |
|---|---|
| `testing-techniques/` | test derivation and test-design techniques |
| `qa/` | QA lifecycle, management, defect, quality and generic testing practices |
| `api/` | API architecture, protocols, security and API-specific testing |
| `database/` | database concepts, SQL, persistence and database-specific testing |
| `domain/` | business concepts, processes, entities, rules and industry orientation |

When a concept crosses domains, the article should explain only the part owned by its domain and reference the authoritative neighboring article for the rest.

## Authoritative-Source Rule

Generic knowledge is guidance, not a substitute for project truth.

Knowledge Articles must not invent:

- business thresholds or formulas;
- permissions or role ownership;
- project statuses or workflows;
- endpoint contracts or database schemas;
- service-level objectives;
- legal or regulatory applicability;
- clinical or financial policy;
- vendor-specific guarantees unless clearly attributed.

When project documentation conflicts with generic knowledge, reviewers should determine whether the project behavior is a legitimate context-specific rule, a technical incompatibility, or a requirement defect. The knowledge article itself must not silently override authoritative project inputs.

## AI Optimization Guidelines

Articles should:

- use descriptive headings and direct definitions;
- keep sections semantically coherent;
- define concepts before referring to them;
- avoid hidden pronouns or context-dependent wording;
- preserve consistent terminology;
- distinguish facts, examples, assumptions, and constraints;
- use lists/tables/diagrams where they improve retrieval and reasoning;
- avoid unnecessary narrative repetition.

## Cross-Reference Requirements

Cross-references should:

- point to real repository paths;
- use relative paths appropriate to the current file;
- identify prerequisite, complementary, specialization, or boundary relationships;
- avoid circular duplication;
- be re-reviewed when files are renamed, moved, deprecated, or materially re-scoped.

## Review Requirements

Before an article becomes Approved, review must cover:

- metadata validity;
- one `#` title and correct `##` mandatory hierarchy;
- presence of all 12 mandatory sections;
- semantic/content depth;
- technical or conceptual accuracy;
- terminology consistency;
- practical QA usefulness;
- assumption and safety boundaries;
- cross-reference accuracy;
- duplicate-responsibility risk;
- independent human readability;
- AI retrieval/reasoning usefulness.

## Self-Review Requirement

Authors or AI generation workflows should perform self-review before presenting an article as complete.

Self-review must identify and fix issues rather than merely score the draft. A score is evidence of review, not a replacement for issue correction.

## Catalog and Freeze Requirements

A knowledge-domain baseline may be marked Frozen only when:

- physical article count matches the Catalog;
- all baseline articles are Approved;
- required cross-article review has passed;
- cross-domain ownership conflicts are resolved;
- README and Catalog reflect the physical architecture;
- no known blocking quality issue remains.

`Frozen` means the baseline is stable, not immutable. Corrective or intentional changes require targeted review and re-freeze.

## Maintenance Rules

When an article is materially changed:

1. review the changed article against this standard;
2. review affected cross-references and prerequisites;
3. update Catalog/README if architecture or status changes;
4. run cross-domain review when ownership or shared terminology changes;
5. update `Last Updated` when required by metadata policy.

## Compliance

Compliance with this standard is mandatory for approved Knowledge Articles unless a documented and reviewed exception exists.

## Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-08-13 | Finalized article structure, content-depth gate, cross-domain ownership, review, and freeze requirements. |