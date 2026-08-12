# Quality Assurance Catalog

## Purpose

The **Quality Assurance** catalog defines the approved knowledge architecture for quality assurance concepts, methodologies, and engineering practices within the QA-AI framework.

Its primary objectives are to:

- organize QA knowledge into clear and maintainable domains;
- provide a consistent learning and reasoning path for QA engineers and AI capabilities;
- define the authoritative set of QA knowledge articles in `shared/knowledge/qa/`;
- make prerequisite and cross-article relationships explicit;
- support reusable QA reasoning across skills and workflows;
- prevent knowledge duplication across QA, testing-techniques, API, database, and domain knowledge areas.

This catalog is the source of truth for the current QA knowledge baseline.

---

## Scope

This catalog covers reusable knowledge related to:

- software quality foundations;
- software development and testing lifecycles;
- requirement engineering;
- test management;
- defect management;
- quality practices;
- quality measurement and continuous improvement.

The catalog focuses on **quality assurance concepts, processes, and engineering practices**.

The following topics are intentionally owned by other knowledge domains.

| Topic | Knowledge Domain |
|---|---|
| Equivalence Partitioning | `../testing-techniques/` |
| Boundary Value Analysis | `../testing-techniques/` |
| Decision Table Testing | `../testing-techniques/` |
| State Transition Testing | `../testing-techniques/` |
| Exploratory Testing | `../testing-techniques/` |
| API Architecture and HTTP | `../api/` |
| SQL and database validation concepts | `../database/` |
| Industry-specific business knowledge | `../domain/` |

---

## Knowledge Architecture

The QA knowledge domain is organized into six categories.

```text
Quality Assurance
│
├── Foundations
├── Requirement Engineering
├── Test Management
├── Defect Management
├── Quality Practices
└── Continuous Improvement
```

Each category owns a distinct responsibility while remaining connected to the broader QA knowledge graph.

---

## Knowledge Map

### Foundations

Foundation articles establish the common quality and lifecycle concepts used throughout the QA knowledge base.

```text
Foundations
├── Software Quality
├── Quality Assurance vs Quality Control
├── Software Development Life Cycle
├── Software Testing Life Cycle
└── Testing Principles
```

### Requirement Engineering

Requirement Engineering articles explain how requirement information is created, analyzed, reviewed, and translated into acceptance-significant behavior.

```text
Requirement Engineering
├── Requirement Engineering
├── Requirement Analysis
├── Requirement Review
└── Acceptance Criteria
```

### Test Management

Test Management articles explain how testing direction, scope, effort, progress, and completion are organized.

```text
Test Management
├── Test Planning
├── Test Strategy
├── Test Estimation
├── Test Monitoring and Control
└── Test Closure
```

### Defect Management

Defect Management articles explain how defects are reported, classified, verified, analyzed, and used for quality learning.

```text
Defect Management
├── Defect Lifecycle
├── Defect Reporting
├── Defect Severity and Priority
├── Defect Analysis
├── Root Cause Analysis
└── Retesting
```

### Quality Practices

Quality Practices articles provide reusable approaches for selecting, evaluating, and maintaining meaningful quality coverage.

```text
Quality Practices
├── Regression Testing
├── Risk-Based Testing
├── Functional and Non-Functional Testing
├── Static and Dynamic Testing
└── Verification and Validation
```

### Continuous Improvement

Continuous Improvement articles explain how testing and product-quality evidence can be measured, interpreted, and converted into learning.

```text
Continuous Improvement
├── Test Metrics
├── Quality Metrics
└── Continuous Improvement
```

---

## Article Catalog

The table below defines the current approved QA knowledge baseline.

| Article | File | Category | Level | Prerequisites | Priority | Status |
|---|---|---|---|---|---|---|
| Software Quality | `Software-Quality.md` | Foundations | Foundation | None | High | Approved |
| Quality Assurance vs Quality Control | `Quality-Assurance-vs-Quality-Control.md` | Foundations | Foundation | Software Quality | High | Approved |
| Software Development Life Cycle | `SDLC.md` | Foundations | Foundation | None | High | Approved |
| Software Testing Life Cycle | `STLC.md` | Foundations | Foundation | SDLC | High | Approved |
| Testing Principles | `Testing-Principles.md` | Foundations | Foundation | Software Quality | High | Approved |
| Requirement Engineering | `Requirement-Engineering.md` | Requirement Engineering | Foundation | SDLC | High | Approved |
| Requirement Analysis | `Requirement-Analysis.md` | Requirement Engineering | Foundation | Requirement Engineering | High | Approved |
| Requirement Review | `Requirement-Review.md` | Requirement Engineering | Intermediate | Requirement Analysis | High | Approved |
| Acceptance Criteria | `Acceptance-Criteria.md` | Requirement Engineering | Foundation | Requirement Analysis | High | Approved |
| Test Planning | `Test-Planning.md` | Test Management | Intermediate | STLC | High | Approved |
| Test Strategy | `Test-Strategy.md` | Test Management | Intermediate | Test Planning | High | Approved |
| Test Estimation | `Test-Estimation.md` | Test Management | Advanced | Test Planning | Medium | Approved |
| Test Monitoring and Control | `Test-Monitoring-and-Control.md` | Test Management | Intermediate | Test Planning | High | Approved |
| Test Closure | `Test-Closure.md` | Test Management | Intermediate | Test Monitoring and Control | High | Approved |
| Defect Lifecycle | `Defect-Lifecycle.md` | Defect Management | Foundation | STLC | High | Approved |
| Defect Reporting | `Defect-Reporting.md` | Defect Management | Foundation | Defect Lifecycle | High | Approved |
| Defect Severity and Priority | `Defect-Severity-and-Priority.md` | Defect Management | Foundation | Defect Lifecycle | High | Approved |
| Defect Analysis | `Defect-Analysis.md` | Defect Management | Intermediate | Defect Reporting | Medium | Approved |
| Root Cause Analysis | `Root-Cause-Analysis.md` | Defect Management | Advanced | Defect Analysis | Medium | Approved |
| Retesting | `Retesting.md` | Defect Management | Foundation | Defect Lifecycle | High | Approved |
| Regression Testing | `Regression-Testing.md` | Quality Practices | Foundation | STLC | High | Approved |
| Risk-Based Testing | `Risk-Based-Testing.md` | Quality Practices | Advanced | Test Strategy | High | Approved |
| Functional and Non-Functional Testing | `Functional-and-Non-Functional-Testing.md` | Quality Practices | Foundation | Software Quality | High | Approved |
| Static and Dynamic Testing | `Static-and-Dynamic-Testing.md` | Quality Practices | Foundation | Testing Principles | High | Approved |
| Verification and Validation | `Verification-and-Validation.md` | Quality Practices | Intermediate | Requirement Engineering | Medium | Approved |
| Test Metrics | `Test-Metrics.md` | Continuous Improvement | Intermediate | Test Monitoring and Control | Medium | Approved |
| Quality Metrics | `Quality-Metrics.md` | Continuous Improvement | Intermediate | Software Quality | Medium | Approved |
| Continuous Improvement | `Continuous-Improvement.md` | Continuous Improvement | Advanced | Test Metrics, Defect Analysis | Medium | Approved |

---

## Category Summary

| Category | Articles | Status | Purpose |
|---|---:|---|---|
| Foundations | 5 | Approved | Establish core quality and lifecycle concepts. |
| Requirement Engineering | 4 | Approved | Understand, analyze, and review software requirements. |
| Test Management | 5 | Approved | Plan, guide, monitor, and close testing activities. |
| Defect Management | 6 | Approved | Report, classify, verify, and analyze defects. |
| Quality Practices | 5 | Approved | Apply risk-aware and lifecycle-aware quality practices. |
| Continuous Improvement | 3 | Approved | Measure quality evidence and drive improvement. |
| **Total** | **28** | **Approved** | Current QA knowledge baseline. |

The catalog count must match the physical knowledge articles in `shared/knowledge/qa/`, excluding `README.md` and `Catalog.md`.

---

## Knowledge Levels

### Foundation

Foundation articles establish concepts required for routine QA reasoning and have minimal prerequisites.

### Intermediate

Intermediate articles combine foundational concepts into practical QA management, review, analysis, or evaluation practices.

### Advanced

Advanced articles require broader context, judgment, or multiple prerequisite concepts and support more complex quality decisions.

Knowledge level describes conceptual dependency and expected reasoning depth. It does not represent job seniority.

---

## Priority Definitions

Priority indicates the importance of an article to the QA-AI knowledge graph and downstream capabilities.

| Priority | Description |
|---|---|
| High | Core knowledge required by multiple QA skills or workflows. |
| Medium | Supporting knowledge that extends or deepens QA reasoning. |
| Low | Specialized knowledge with narrower reusable scope. |

Priority is not a document-quality rating.

---

## Status Definitions

Catalog status describes implementation readiness of each knowledge article.

| Status | Description |
|---|---|
| Planned | Identified but not yet implemented. |
| In Progress | Currently being developed. |
| Review | Draft completed and undergoing review. |
| Approved | Passed review and accepted for active QA-AI use. |
| Deprecated | Retained for historical compatibility but no longer recommended. |

The current QA baseline contains **28 Approved articles** and no Planned, In Progress, or Review articles.

---

## Learning Path

A recommended conceptual progression is:

```text
Foundations
    │
    ▼
Requirement Engineering
    │
    ▼
Test Management
    │
    ├──────────────┐
    ▼              ▼
Defect Management Quality Practices
    │              │
    └──────┬───────┘
           ▼
Continuous Improvement
```

This learning path is guidance rather than a mandatory reading sequence.

---

## Dependency Map

The principal knowledge relationships are:

```text
Software Quality
├── Quality Assurance vs Quality Control
├── Testing Principles
├── Functional and Non-Functional Testing
└── Quality Metrics

SDLC
├── STLC
└── Requirement Engineering

Requirement Engineering
├── Requirement Analysis
│   ├── Requirement Review
│   └── Acceptance Criteria
└── Verification and Validation

STLC
├── Test Planning
│   ├── Test Strategy
│   │   └── Risk-Based Testing
│   ├── Test Estimation
│   ├── Test Monitoring and Control
│   │   ├── Test Closure
│   │   └── Test Metrics
│   └── Regression Testing
└── Defect Lifecycle
    ├── Defect Reporting
    │   └── Defect Analysis
    │       ├── Root Cause Analysis
    │       └── Continuous Improvement
    ├── Defect Severity and Priority
    └── Retesting

Testing Principles
└── Static and Dynamic Testing

Regression Testing
├── Retesting
├── Defect Analysis
└── Risk-Based Testing

Test Metrics
└── Continuous Improvement

Quality Metrics
└── Continuous Improvement
```

The map represents primary conceptual dependencies, not every cross-reference between articles.

---

## Usage in QA-AI

The QA knowledge domain supports reusable reasoning across capabilities such as:

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

Knowledge articles provide conceptual context. They do not replace project requirements, standards, workflows, templates, or authoritative domain rules.

---

## Freeze Baseline

The QA knowledge folder is frozen as the approved baseline on **2026-08-12**.

```text
Folder: shared/knowledge/qa/
Physical Knowledge Articles: 28
Cataloged Knowledge Articles: 28
Catalog Status: Approved
Baseline State: Frozen
```

`Frozen` is a repository maintenance state, not a document metadata lifecycle value.

After freeze:

1. Existing articles should not be changed casually.
2. Corrections or conceptual changes require targeted review of the affected article.
3. Cross-reference impact must be reviewed when an article is renamed, moved, added, deprecated, or materially re-scoped.
4. `Catalog.md` and `README.md` must be updated whenever the physical QA knowledge architecture changes.
5. New articles must follow `shared/standards/Knowledge-Article.md` before being added to the approved baseline.
6. Cross-domain concepts should remain in their owning knowledge domain and be referenced rather than duplicated.

---

## Review Gate

The frozen baseline has been reviewed for:

- physical file and catalog consistency;
- mandatory Knowledge Article structure;
- terminology consistency;
- scope boundaries;
- cross-article duplication;
- cross-reference accuracy;
- human readability;
- AI readability and independent retrieval;
- project-specific assumption safety.

Any future baseline change should pass the same review dimensions before the folder is considered frozen again.
