# QA-AI Implementation Roadmap

> Version: 1.3.0  
> Status: Approved  
> Last Updated: 2026-08-14

---

## 1. Purpose

This document is the canonical human-readable implementation roadmap for QA-AI. It defines phase scope, deliverables, dependencies, exit criteria, current status, and progress-tracking rules.

Detailed component behavior remains in the corresponding standards, skills, workflows, knowledge, datasets, examples, scripts, adapters, and component READMEs.

---

## 2. Roadmap Principles

### 2.1 Foundation Before Automation

Framework concepts, standards, structures, and contracts must be stable before deterministic automation is introduced.

### 2.2 Reusable Components Before Platform Integration

Core QA capabilities remain platform-independent. Adapters translate packaging/execution mechanics without redefining QA behavior.

### 2.3 Definition Before Execution

Canonical definitions precede runtime artifacts.

```text
Fixture Model → Fixture Instance
Benchmark Definition → Benchmark Execution → Benchmark Record
```

### 2.4 Validation Before Expansion

A framework layer should pass its quality gate before downstream layers significantly expand their dependency on it.

### 2.5 Explicit Phase Boundaries

Work intentionally planned for a later phase is not incomplete work in the current phase.

### 2.6 Freeze Stable Foundations

A phase may be frozen after scope completion, artifact completion, cross-component review, issue resolution, and downstream-readiness validation.

### 2.7 Progress From Verified State

```text
File exists              ≠ Completed
Content written          ≠ Completed
Quality gate passed      = Completed
Cross-component baseline = Frozen
```

Machine-readable status: `roadmap-status.json`  
Tracking contract: `shared/standards/Roadmap-Progress.md`

---

## 3. Status Definitions

| Status | Meaning |
|---|---|
| `Planned` | Defined; implementation not started. |
| `In Progress` | Implementation underway. |
| `Review` | Primary implementation complete; quality/consistency review underway. |
| `Completed` | Defined scope and exit criteria satisfied. |
| `Frozen` | Completed and accepted as a stable downstream dependency. |

```text
Planned → In Progress → Review → Completed → Frozen
```

---

## 4. Implementation Overview

<!-- ROADMAP_STATUS:START -->

| Phase | Name | Status | Progress |
|---|---|---|---|
| Phase 1 | Framework Foundation | Completed | — |
| Phase 2 | Shared Standards and Foundations | Completed | — |
| Phase 3 | Workflow Library | Completed | — |
| Phase 4 | Skill Library Foundation | Completed | 6/6 foundation_skills |
| Phase 5 | Knowledge Foundation | Completed | — |
| Phase 6 | Examples and End-to-End Validation | Completed | — |
| Phase 7 | Framework Integration and Validation | Completed | — |
| Phase 8 | Datasets and Evaluation | Frozen | — |
| Phase 9 | Repository Completion and Alignment | Completed | — |
| Phase 10 | Knowledge Library Completion | Frozen | 181/181 knowledge_articles |
| Phase 11 | Skill Library Expansion | Frozen | 5/5 expansion_skills |
| Phase 12 | Scripts Implementation | Frozen | 8/8 script_groups |
| Phase 13 | Platform Integration | Frozen | 3/3 platform_adapters |

<!-- ROADMAP_STATUS:END -->

Current baseline after Phase 13 freeze:

```text
Latest Frozen Phase: Phase 13 — Platform Integration
Canonical Skill Library: 11/11
Knowledge Baseline: 181/181
Canonical Scripts: 25 / 8 groups
Platform Adapters: ChatGPT + Claude + Cursor (3/3 Frozen)
```

---

## 5. Phase 1 — Framework Foundation

### Objective

Establish QA-AI purpose, architecture, concepts, component boundaries, repository structure, and governance model.

### Primary Scope

`docs/`

### Exit Criteria

- framework purpose and architecture are defined;
- major components and boundaries are documented;
- downstream implementation can follow a stable conceptual model.

### Status

`Completed`

---

## 6. Phase 2 — Shared Standards and Foundations

### Objective

Create reusable standards and shared assets for consistent framework behavior.

### Primary Scope

```text
shared/
├── standards/
├── templates/
├── checklists/
├── prompt-patterns/
└── glossary/
```

### Exit Criteria

Reusable standards, templates, checklists, prompt patterns, and terminology are available to downstream components.

### Status

`Completed`

---

## 7. Phase 3 — Workflow Library

### Objective

Define reusable multi-step QA workflows without embedding platform-specific behavior.

### Baseline

```text
workflows/
├── testcase-generation/
├── testcase-quality-review/
└── regression-analysis/
```

### Exit Criteria

Workflow/skill responsibilities are separated and stages have clear input/output contracts.

### Status

`Completed`

---

## 8. Phase 4 — Skill Library Foundation

### Objective

Establish the initial reusable QA skill architecture.

### Frozen Foundation Inventory

```text
requirement-analyzer
business-rule-extractor
scenario-generator
testcase-generator
coverage-reviewer
regression-impact
```

These six skills form the foundation baseline and are not counted as Phase 11 expansion progress.

### Status

`Completed — 6/6 foundation skills`

---

## 9. Phase 5 — Knowledge Foundation

### Objective

Establish the knowledge architecture, taxonomy, catalogs, and article conventions used by skills/workflows.

### Scope

```text
shared/knowledge/
├── testing-techniques/
├── qa/
├── api/
├── database/
└── domain/
```

### Status

`Completed`

Full population was completed and frozen in Phase 10.

---

## 10. Phase 6 — Examples and End-to-End Validation

### Objective

Demonstrate representative requirement-to-QA-artifact transformations and traceability.

### Status

`Completed`

---

## 11. Phase 7 — Framework Integration and Validation

### Objective

Validate cross-component terminology, contracts, traceability, examples, and ownership boundaries.

### Status

`Completed`

---

## 12. Phase 8 — Datasets and Evaluation

### Objective

Establish controlled requirement datasets, golden references, evaluation criteria/rubrics/scoring, benchmark definitions, and fixture models.

### Scope

```text
datasets/
├── requirements/
├── golden-output/
├── evaluation/
├── benchmark/
└── fixtures/
```

### Status

`Frozen`

---

## 13. Phase 9 — Repository Completion and Alignment

### Objective

Align repository-level documentation, governance, navigation, placeholders, and framework status representation.

### Status

`Completed`

---

## 14. Phase 10 — Knowledge Library Completion

### Objective

Complete and quality-gate the knowledge library as a stable downstream dependency.

### Frozen Baseline

| Knowledge Domain | Articles | Status |
|---|---:|---|
| Testing Techniques | 30 | Frozen |
| QA | 28 | Frozen |
| API | 40 | Frozen |
| Database | 42 | Frozen |
| Domain | 41 | Frozen |
| **Total** | **181** | **Frozen** |

### Freeze Gate Result

- physical content and catalogs aligned;
- approved knowledge-article standard applied;
- folder-level and cross-domain review passed;
- ownership boundaries and authoritative-input rules aligned;
- no blocking cross-domain issue remained.

### Status

`Frozen — 181/181 knowledge articles`

---

## 15. Phase 11 — Skill Library Expansion

### Objective

Expand the reusable skill library with capabilities not already owned by the six Phase 4 foundation skills.

### Canonical Expansion Scope

| Skill | Primary Responsibility | Final Status |
|---|---|---|
| `risk-analyzer` | QA risk identification, assessment, prioritization, and QA-focus guidance | Frozen |
| `bug-report-reviewer` | Bug-report completeness, reproducibility, evidence, consistency, and actionability review | Frozen |
| `api-test-generator` | API-specific test design and technical assertions | Frozen |
| `sql-validation` | QA-oriented database/SQL verification logic | Frozen |
| `test-data-generator` | Test-data requirements, partitions, constraints, and reusable datasets | Frozen |

```text
Expansion progress: 5 / 5
Total canonical skill library: 11 skills
```

### Inventory Decision

`regression-analyzer` was reviewed and intentionally not introduced. `regression-impact` already owns authoritative change-delta analysis, affected-area identification, regression-scope definition, and prioritization; a second broad regression analyzer would materially overlap it.

### Cross-Skill Review Findings and Fixes

Final review covered all 11 skills and found/fixed the following architectural issues:

1. **Regression input contract** — `regression-impact` requires an authoritative change delta plus sufficient baseline context; coverage is supporting evidence.
2. **Risk integration** — scenario, testcase, coverage, and regression contracts consume Structured Risk Analysis where relevant without redefining risk ownership.
3. **Coverage baseline** — `coverage-reviewer` requires both test artifacts and sufficient authoritative source material.
4. **Generic vs technical design** — `testcase-generator` remains technology-neutral; API-specific and SQL-specific details are owned by specialized skills.
5. **Business-rule authority** — rule extraction cannot invent project policy, thresholds, defaults, or precedence from generic knowledge.
6. **Dependency-cycle safety** — test-data/testcase and API/SQL enrichment relationships remain optional rather than circular hard dependencies.
7. **Feedback paths** — coverage/regression remediation may re-invoke generators through workflow orchestration, not hard skill dependencies.
8. **Shared knowledge usage** — authoritative project inputs override generic knowledge across the library.

### Frozen Capability Groups

```text
Requirement Understanding
├── requirement-analyzer
├── business-rule-extractor
└── risk-analyzer

Test Design
├── scenario-generator
├── testcase-generator
└── test-data-generator

Quality Assessment
├── coverage-reviewer
├── regression-impact
└── bug-report-reviewer

Technical Validation
├── api-test-generator
└── sql-validation
```

### Phase Freeze Gate

The full 11-skill library passed ownership, input/output compatibility, hard dependency-cycle, workflow-remediation boundary, shared-knowledge dependency, and generic-vs-specialized capability review. No blocking cross-skill issue remains.

### Status

`Frozen — 5/5 expansion skills; 11-skill canonical baseline`

---

## 16. Phase 12 — Scripts Implementation

### Objective

Introduce deterministic tooling that validates, manages, evaluates, exports, and synchronizes QA-AI framework artifacts.

### Frozen Scope

```text
scripts/
├── validation/   4
├── knowledge/    3
├── prompts/      2
├── workflows/    3
├── evaluation/   4
├── export/       3
├── utils/        3
└── roadmap/      3
                  ──
                  25 scripts / 8 groups
```

### Freeze Gate Result

Phase 12 passed:

- full 25-script implementation across 8 canonical groups;
- cross-script ownership/contract/dependency review;
- deterministic compile and smoke validation;
- validation, metadata, links, output, catalog, workflow, and roadmap checks;
- evaluation semantics review against Phase 8 definitions;
- export/prompt safety review;
- metadata/output false-positive fixes and legacy metadata migration;
- workflow contract alignment for coverage and regression analysis;
- deterministic roadmap status collection, validation, and synchronization.

No blocking Phase 12 issue remains.

### Status

`Frozen — 8/8 script groups; 25 canonical scripts`

---

## 17. Phase 13 — Platform Integration

### Objective

Make the platform-independent QA-AI framework consumable through supported AI runtimes without duplicating or redefining canonical QA semantics.

### Frozen Platform Baseline

```text
ChatGPT
Claude
Cursor
```

| Platform | Native Integration Mechanism | Final Status |
|---|---|---|
| ChatGPT | Custom GPT Instructions + bounded generated Knowledge bundles | Frozen |
| Claude | Claude Code repository-root `CLAUDE.md` + canonical repository references | Frozen |
| Cursor | Repository-root `.cursor/rules/*.mdc` + `.cursor/commands/*.md` | Frozen |

### Adapter Principle

```text
Authoritative Project Input
        ↓
QA-AI Core
        ↓
Platform Adapter
        ↓
Platform Runtime
```

Adapters own platform-native loading, packaging, routing, and installation mechanics. Canonical skill behavior, workflow orchestration, shared standards, knowledge, and evaluation semantics remain owned by the platform-independent core.

### Frozen Integration Contract

All three adapters preserve:

1. authoritative project input as highest-priority source;
2. canonical workflow ownership for coordinated multi-artifact work;
3. canonical skill ownership for individual QA capabilities;
4. shared standards/templates/checklists/knowledge as supporting references;
5. explicit separation of confirmed, derived, assumed, potential, and unknown information;
6. no invention of project-specific behavior, API contracts, schemas, dependencies, roles, status values, or expected results;
7. clarification-dependent treatment when required behavior is unresolved;
8. specialized routing for API and SQL/database design;
9. canonical `regression-impact` ownership without a duplicate `regression-analyzer` capability.

### Runtime Validation

**ChatGPT** passed Custom GPT Preview smoke tests for requirement routing, testcase-generation workflow orchestration, API missing-contract handling, and canonical knowledge retrieval.

**Claude** passed repository instruction loading, requirement source-grounding, testcase-generation workflow orchestration, assumption-propagation enforcement, API missing-contract blocking, and regression ownership retrieval. Runtime findings discovered during review were fixed in `adapters/claude/CLAUDE.md` and successfully rerun.

**Cursor** passed workspace Project Rule loading, requirement source-grounding, testcase-generation workflow orchestration, clarification-dependent coverage behavior, API missing-contract blocking, and canonical regression ownership retrieval.

### Phase Freeze Gate

Final cross-platform review covered:

- source-priority consistency;
- capability routing and ownership;
- workflow orchestration;
- assumption propagation and executable expected-result safety;
- specialized API behavior;
- regression capability ownership;
- installation/runtime topology;
- platform-specific smoke evidence;
- adapter/core boundary consistency.

All 3 adapters passed. No blocking Phase 13 issue remains.

### Status

`Frozen — 3/3 platform adapters (ChatGPT + Claude + Cursor)`

---

## 18. Phase Dependencies

```text
Phase 1  Framework Foundation
   ↓
Phase 2  Shared Standards and Foundations
   ↓
Phase 3  Workflow Library
   ↓
Phase 4  Skill Library Foundation
   ↓
Phase 5  Knowledge Foundation
   ↓
Phase 6  Examples and End-to-End Validation
   ↓
Phase 7  Framework Integration and Validation
   ↓
Phase 8  Datasets and Evaluation
   ↓
Phase 9  Repository Completion and Alignment
   ↓
Phase 10 Knowledge Library Completion
   ↓
Phase 11 Skill Library Expansion
   ↓
Phase 12 Scripts Implementation
   ↓
Phase 13 Platform Integration
```

---

## 19. Roadmap Progress Tracking

### 19.1 Source of Truth

`roadmap-status.json` is the machine-readable source of truth. This roadmap is its synchronized human-readable representation.

### 19.2 Tracking Unit

Progress is measured at roadmap deliverable/component level, not arbitrary file count.

### 19.3 Synchronization Trigger

When a tracked component passes or loses its quality gate, both registry and roadmap must be recalculated/synchronized.

### 19.4 Freeze Rule

A phase cannot be marked `Frozen` merely because all physical files exist. Its phase-level cross-component review must pass.

### 19.5 Deterministic Automation

Phase 12 provides deterministic status collection, validation, and roadmap synchronization under `scripts/roadmap/`. Registry state remains authoritative; generated roadmap status must remain synchronized with it.

---

## 20. Current Implementation Focus

```text
Latest Frozen Phase: Phase 13 — Platform Integration
Canonical Skill Library: 11/11
Knowledge Baseline: 181/181
Canonical Scripts: 25 / 8 groups
Platform Adapters: 3/3 Frozen
Current State: Phase 1–13 baseline implemented and quality-gated
```

Any subsequent roadmap expansion must be explicitly defined and reviewed before a new phase is added.

---

## 21. Change Governance

Roadmap changes must preserve phase boundaries, component ownership, lifecycle semantics, registry synchronization, and traceability between implemented artifacts and reported progress. Changes to canonical phase scope or tracked inventory require explicit review before registry updates.
