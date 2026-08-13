# QA-AI Implementation Roadmap

> Version: 1.2.0  
> Status: Approved  
> Last Updated: 2026-08-13

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

| Phase | Name | Status |
|---|---|---|
| Phase 1 | Framework Foundation | Completed |
| Phase 2 | Shared Standards and Foundations | Completed |
| Phase 3 | Workflow Library | Completed |
| Phase 4 | Skill Library Foundation | Completed |
| Phase 5 | Knowledge Foundation | Completed |
| Phase 6 | Examples and End-to-End Validation | Completed |
| Phase 7 | Framework Integration and Validation | Completed |
| Phase 8 | Datasets and Evaluation | Frozen |
| Phase 9 | Repository Completion and Alignment | Completed |
| Phase 10 | Knowledge Library Completion | Frozen |
| Phase 11 | Skill Library Expansion | **Frozen** |
| Phase 12 | Scripts Implementation | Planned |
| Phase 13 | Platform Integration | Planned |

Current focus after Phase 11 freeze:

```text
Next Phase: Phase 12 — Scripts Implementation
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

1. **Regression input contract** — `regression-impact` previously treated coverage assessment as the required input while change information was optional. The contract now requires an authoritative change delta plus sufficient baseline context; coverage is supporting evidence.
2. **Risk integration** — scenario, testcase, coverage, and regression contracts now explicitly consume Structured Risk Analysis where relevant without redefining risk ownership.
3. **Coverage baseline** — `coverage-reviewer` now requires both test artifacts and sufficient authoritative source material; it no longer implies that completeness can be judged from testcases alone.
4. **Generic vs technical design** — `testcase-generator` remains technology-neutral; API-specific and SQL-specific details are owned by their specialized skills.
5. **Business-rule authority** — rule extraction may normalize explicit/supported implications but cannot invent project policy, thresholds, defaults, or precedence from generic knowledge.
6. **Dependency-cycle safety** — test-data/testcase and API/SQL enrichment relationships are explicitly optional. No skill has a mandatory dependency on another skill that simultaneously requires its output.
7. **Feedback paths** — coverage/regression remediation may re-invoke generators, but feedback is workflow orchestration rather than a hard circular skill dependency.
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

### Skill Completion Gate

Each expansion skill passed:

- capability/scope definition;
- input/output contract review;
- processing definition;
- dependency/consumer review;
- overlap/exclusion review;
- authoritative-input and assumption-safety review;
- validation criteria review;
- individual self-review and fix.

### Phase Freeze Gate

The full 11-skill library passed:

- ownership review;
- cross-skill input/output compatibility review;
- hard dependency-cycle review;
- workflow-remediation boundary review;
- shared-knowledge dependency review;
- generic-vs-specialized capability review;
- `skills/README.md` / physical inventory / registry consistency review.

No blocking cross-skill issue remains.

### Status

`Frozen — 5/5 expansion skills; 11-skill canonical baseline`

---

## 16. Phase 12 — Scripts Implementation

### Objective

Introduce deterministic tooling that validates, manages, evaluates, and exports QA-AI framework artifacts.

### Planned Scope

```text
scripts/
├── validation/
├── knowledge/
├── prompts/
├── workflows/
├── evaluation/
├── export/
└── utils/
```

Roadmap automation implementation belongs here. Until implemented, `roadmap-status.json` remains the machine-readable registry and roadmap synchronization is performed as part of component completion.

### Exit Criteria

- planned scripts have purposeful implementations;
- validation scripts detect intended structural/contract issues;
- evaluation tooling consumes Phase 8 definitions correctly;
- scripts expose explicit failure behavior;
- automation does not redefine canonical framework semantics.

### Status

`Planned`

---

## 17. Phase 13 — Platform Integration

### Objective

Make the platform-independent framework consumable by supported AI platforms.

### Initial Targets

```text
ChatGPT
Claude
```

### Adapter Principle

```text
QA-AI Core → Platform Adapter → Platform Runtime
```

### Status

`Planned`

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

### 19.5 Future Automation

Phase 12 should implement deterministic status collection, validation, and roadmap synchronization using the existing tracking contract rather than creating a new status model.

---

## 20. Current Implementation Focus

```text
Latest Frozen Phase: Phase 11 — Skill Library Expansion
Canonical Skill Library: 11/11
Knowledge Baseline: 181/181
Next Planned Phase: Phase 12 — Scripts Implementation
```

---

## 21. Change Governance

Roadmap changes must preserve phase boundaries, component ownership, lifecycle semantics, registry synchronization, and traceability between implemented artifacts and reported progress. Changes to canonical phase scope or tracked inventory require explicit review before registry updates.