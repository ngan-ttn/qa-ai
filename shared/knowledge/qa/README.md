# Quality Assurance

## Purpose

The `qa` knowledge module provides reusable knowledge about software quality assurance concepts, lifecycles, requirement engineering, test management, defect management, quality practices, measurement, and continuous improvement.

Its purpose is to establish a coherent QA knowledge base that supports both human practitioners and QA-AI capabilities throughout the software lifecycle.

This module explains **concepts and reasoning guidance**. It does not define project-specific requirements, standards, templates, checklists, workflows, role ownership, release gates, or business rules.

---

## Scope

The module covers:

- software quality foundations;
- SDLC and STLC concepts;
- testing principles;
- requirement engineering and requirement review;
- acceptance criteria;
- test planning, strategy, estimation, monitoring, and closure;
- defect lifecycle, reporting, classification, analysis, RCA, and retesting;
- regression and risk-based testing;
- functional/non-functional and static/dynamic testing perspectives;
- verification and validation;
- test and quality metrics;
- continuous improvement.

Detailed test-design techniques remain in `../testing-techniques/` rather than being duplicated here.

API, database, and domain-specific knowledge remain in their respective knowledge modules.

---

## Module Structure

```text
shared/
└── knowledge/
    └── qa/
        ├── README.md
        ├── Catalog.md
        │
        ├── Foundations
        │   ├── Software-Quality.md
        │   ├── Quality-Assurance-vs-Quality-Control.md
        │   ├── SDLC.md
        │   ├── STLC.md
        │   └── Testing-Principles.md
        │
        ├── Requirement Engineering
        │   ├── Requirement-Engineering.md
        │   ├── Requirement-Analysis.md
        │   ├── Requirement-Review.md
        │   └── Acceptance-Criteria.md
        │
        ├── Test Management
        │   ├── Test-Planning.md
        │   ├── Test-Strategy.md
        │   ├── Test-Estimation.md
        │   ├── Test-Monitoring-and-Control.md
        │   └── Test-Closure.md
        │
        ├── Defect Management
        │   ├── Defect-Lifecycle.md
        │   ├── Defect-Reporting.md
        │   ├── Defect-Severity-and-Priority.md
        │   ├── Defect-Analysis.md
        │   ├── Root-Cause-Analysis.md
        │   └── Retesting.md
        │
        ├── Quality Practices
        │   ├── Regression-Testing.md
        │   ├── Risk-Based-Testing.md
        │   ├── Functional-and-Non-Functional-Testing.md
        │   ├── Static-and-Dynamic-Testing.md
        │   └── Verification-and-Validation.md
        │
        └── Continuous Improvement
            ├── Test-Metrics.md
            ├── Quality-Metrics.md
            └── Continuous-Improvement.md
```

The category labels above are conceptual groupings. The physical files remain directly under `shared/knowledge/qa/`.

`Catalog.md` is the authoritative source for article classification, prerequisites, priority, and implementation status.

---

## Knowledge Areas

### Foundations

Establish the meaning of software quality, QA/QC, software lifecycles, and testing principles.

### Requirement Engineering

Explain how requirement information is defined, analyzed, reviewed, and translated into acceptance-significant behavior.

### Test Management

Explain how testing is planned, guided, estimated, monitored, controlled, and closed.

### Defect Management

Explain how defects are reported, classified, tracked, verified, analyzed, and used for learning.

### Quality Practices

Explain reusable testing and evaluation perspectives that support risk-aware coverage and quality reasoning.

### Continuous Improvement

Explain how testing and product-quality evidence can be measured and converted into focused improvement.

---

## Knowledge Article Standard

All QA knowledge articles follow `../../standards/Knowledge-Article.md`.

The 12 mandatory sections are:

```text
1. Overview
2. Purpose
3. Core Concepts
4. How It Works
5. When to Use
6. When Not to Use
7. Advantages
8. Limitations
9. Examples
10. Best Practices
11. Related Knowledge
12. References
```

Optional sections such as `Common Mistakes`, `Comparison`, `FAQ`, or `AI Considerations` may be added when they improve the article.

Article headings should use a consistent hierarchy:

```text
# Article Title
## Mandatory / major section
### Concept or subsection
#### Deeper subsection — only when needed
```

---

## Design Principles

QA knowledge articles should:

- focus on reusable concepts rather than project implementation;
- remain methodology-independent where practical;
- use established QA terminology consistently;
- explain boundaries with related articles instead of duplicating them;
- include practical examples that improve reasoning;
- distinguish generic guidance from project-specific facts;
- preserve uncertainty when authoritative information is missing;
- support independent AI retrieval without requiring hidden conversation context;
- avoid inventing business rules, thresholds, roles, or governance.

---

## Cross-Domain Relationships

The QA module commonly references:

- `../testing-techniques/` for systematic test-design techniques;
- `../api/` for API-specific knowledge;
- `../database/` for database-specific knowledge;
- `../domain/` for business-domain knowledge;
- `../../glossary/` for shared terminology;
- `../../templates/` for output structures;
- `../../checklists/` for review controls;
- `../../../skills/` for QA-AI capabilities;
- `../../../workflows/` for multi-skill execution flows.

Cross-domain knowledge should be referenced rather than copied into the QA module without a clear ownership reason.

---

## QA-AI Usage

Knowledge in this module supports capabilities such as:

- requirement analysis;
- business-rule extraction;
- risk analysis;
- scenario generation;
- testcase generation;
- coverage review;
- regression analysis;
- defect-report review;
- test-data planning;
- quality-status reasoning.

Knowledge articles provide reasoning context. Authoritative project inputs remain the source of truth for actual expected behavior.

---

## Freeze Baseline

The current QA knowledge baseline contains **28 knowledge articles** and is frozen on **2026-08-12** after cross-artifact review.

The approved article list and status are maintained in `Catalog.md`.

Freeze means:

- the current architecture is considered stable;
- existing articles should not be changed casually;
- material changes require targeted self-review and cross-reference review;
- additions, removals, renames, or category changes require `Catalog.md` and `README.md` updates;
- affected articles must continue to comply with `../../standards/Knowledge-Article.md` before the baseline is frozen again.

`Frozen` describes the repository maintenance state. It is not a document metadata status.

---

## References

Primary repository references include:

- `Catalog.md`
- `../../standards/Knowledge-Article.md`
- `../../standards/Metadata.md`
- `../testing-techniques/`
- `../../glossary/`
- `../../../skills/`
- `../../../workflows/`
