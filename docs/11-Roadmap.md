# QA-AI Implementation Roadmap

> Version: 1.1.0  
> Status: Approved  
> Last Updated: 2026-08-13

---

## 1. Purpose

This document defines the canonical implementation roadmap for the QA-AI framework.

It describes:

- the implementation phases of QA-AI;
- the responsibility and scope of each phase;
- major deliverables and dependencies;
- exit criteria and implementation status;
- the current implementation focus;
- how roadmap progress is synchronized with repository component status.

Detailed component design remains in the corresponding standards, skills, workflows, knowledge articles, datasets, examples, scripts, adapters, and component-level README files.

---

## 2. Roadmap Principles

### 2.1 Foundation Before Automation

Framework concepts, standards, structures, and contracts must be stable before automation is introduced.

### 2.2 Reusable Components Before Platform Integration

Core QA capabilities remain platform-independent. Platform adapters translate packaging and execution mechanics without redefining QA behavior.

### 2.3 Definition Before Execution

Canonical definitions precede runtime artifacts.

```text
Fixture Model → Fixture Instance
Benchmark Definition → Benchmark Execution → Benchmark Record
```

### 2.4 Validation Before Expansion

A framework layer should pass its defined quality gate before downstream layers significantly expand their dependency on it.

### 2.5 Explicit Phase Boundaries

Work intentionally scheduled for a future phase is not incomplete work in the current phase.

```text
Planned ≠ Incomplete
```

### 2.6 Freeze Stable Foundations

A phase may be frozen after its intended scope is complete, required artifacts are present, cross-artifact consistency has been reviewed, blocking issues are resolved, and downstream phases can safely depend on it.

### 2.7 Progress From Verified State

Roadmap progress is derived from verified component state rather than file existence alone.

```text
File exists              ≠ Completed
Content written          ≠ Completed
Quality gate passed      = Completed
Cross-component baseline = Frozen
```

The machine-readable source of truth is:

```text
roadmap-status.json
```

Tracking behavior is governed by:

```text
shared/standards/Roadmap-Progress.md
```

---

## 3. Status Definitions

| Status | Meaning |
|---|---|
| `Planned` | Defined but implementation has not started. |
| `In Progress` | Implementation is actively underway. |
| `Review` | Primary implementation is complete and undergoing quality or consistency review. |
| `Completed` | Defined scope and exit criteria have been satisfied. |
| `Frozen` | Completed and accepted as a stable downstream dependency. |

Canonical lifecycle:

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
| Phase 11 | Skill Library Expansion | In Progress |
| Phase 12 | Scripts Implementation | Planned |
| Phase 13 | Platform Integration | Planned |

Current focus:

```text
Phase 11 — Skill Library Expansion
Progress: 0 / 5 expansion skills
```

---

## 5. Phase 1 — Framework Foundation

### Objective

Establish the conceptual and architectural foundation of QA-AI.

### Primary Scope

```text
docs/
```

### Exit Criteria

- framework purpose is defined;
- major components and boundaries are documented;
- repository architecture is understandable;
- downstream implementation can follow a stable conceptual model.

### Status

`Completed`

---

## 6. Phase 2 — Shared Standards and Foundations

### Objective

Create reusable standards and shared assets that ensure consistent behavior across QA-AI components.

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

- reusable standards are documented;
- templates exist for core QA artifacts;
- review checklists exist for supported activities;
- reusable prompt patterns are available;
- shared terminology is defined.

### Status

`Completed`

---

## 7. Phase 3 — Workflow Library

### Objective

Define reusable multi-step QA workflows that coordinate framework capabilities.

### Baseline

```text
workflows/
├── testcase-generation/
├── testcase-quality-review/
└── regression-analysis/
```

### Exit Criteria

- core workflows are documented;
- workflow and skill responsibilities are separated;
- stages have clear inputs and outputs;
- workflows remain platform-independent.

### Status

`Completed`

---

## 8. Phase 4 — Skill Library Foundation

### Objective

Establish the initial reusable QA skill architecture.

### Canonical Foundation Baseline

```text
skills/
├── requirement-analyzer/
├── business-rule-extractor/
├── scenario-generator/
├── testcase-generator/
├── coverage-reviewer/
└── regression-impact/
```

Foundation capability chain:

```text
Requirement Analysis
        ↓
Business Rule Extraction
        ↓
Scenario Generation
        ↓
Testcase Generation
        ↓
Coverage Review
        ↓
Regression Impact
```

These six skills belong to the Phase 4 baseline and are not counted as Phase 11 expansion progress.

### Exit Criteria

- initial skill architecture exists;
- capability boundaries are explicit;
- skills can participate in workflows;
- skills consume shared resources where appropriate;
- behavior is platform-independent.

### Status

`Completed — 6/6 foundation skills`

---

## 9. Phase 5 — Knowledge Foundation

### Objective

Establish the knowledge architecture used by skills and workflows.

### Scope

```text
shared/knowledge/
├── testing-techniques/
├── qa/
├── api/
├── database/
└── domain/
```

### Exit Criteria

- knowledge architecture is stable;
- categories and catalogs are defined;
- article structure is standardized;
- downstream components can reference the knowledge layer.

### Status

`Completed`

Full population was completed later in Phase 10.

---

## 10. Phase 6 — Examples and End-to-End Validation

### Objective

Demonstrate how framework components transform QA inputs into expected QA artifacts.

### Representative Chain

```text
Sample Requirement
        ↓
Requirement Analysis
        ↓
Business Rules
        ↓
Risk Analysis
        ↓
Test Scenarios
        ↓
Coverage Review
        ↓
Test Cases
        ↓
Regression Analysis
        ↓
Test Data
```

### Exit Criteria

- major QA artifacts have representative examples;
- inputs and outputs are traceable;
- end-to-end relationships are demonstrated;
- examples align with framework standards.

### Status

`Completed`

---

## 11. Phase 7 — Framework Integration and Validation

### Objective

Validate that standards, templates, checklists, knowledge, skills, workflows, and examples operate coherently as one framework.

### Exit Criteria

- terminology is compatible across components;
- upstream/downstream contracts align;
- duplicate responsibilities are minimized;
- examples represent intended framework behavior;
- blocking cross-artifact inconsistencies are resolved.

### Status

`Completed`

---

## 12. Phase 8 — Datasets and Evaluation

### Objective

Establish controlled datasets and evaluation definitions for measuring QA-AI output quality.

### Scope

```text
datasets/
├── requirements/
├── golden-output/
├── evaluation/
├── benchmark/
└── fixtures/
```

### Architectural Boundaries

```text
Fixture Model → Fixture Instance
Benchmark Definition → Benchmark Execution → Benchmark Record
```

### Exit Criteria

- representative requirement datasets exist;
- golden references exist;
- evaluation criteria, rubrics, and scoring are defined;
- benchmark definitions are available;
- fixture models are documented;
- source integrity and assumption boundaries are explicit.

### Status

`Frozen`

---

## 13. Phase 9 — Repository Completion and Alignment

### Objective

Align repository-level documentation and governance with the implemented framework.

### Scope

- roadmap synchronization;
- root README synchronization;
- governance alignment;
- foundation cleanup;
- cross-repository consistency review.

### Exit Criteria

- roadmap and root navigation reflect actual implementation;
- governance artifacts are aligned;
- intended placeholders are distinguishable from accidental incompleteness;
- repository-level review has no blocking findings.

### Status

`Completed`

---

## 14. Phase 10 — Knowledge Library Completion

### Objective

Complete and quality-gate the established knowledge architecture so it can serve as a stable dependency for skills, workflows, scripts, and platform integration.

### Frozen Baseline

| Knowledge Domain | Articles | Status |
|---|---:|---|
| Testing Techniques | 30 | Frozen |
| QA | 28 | Frozen |
| API | 40 | Frozen |
| Database | 42 | Frozen |
| Domain | 41 | Frozen |
| **Total** | **181** | **Frozen** |

All articles follow the approved knowledge-article standard and passed folder-level plus cross-domain review.

### Exit Criteria

- planned catalogs are backed by physical content;
- articles follow `shared/standards/Knowledge-Article.md`;
- knowledge is discoverable and ownership boundaries are clear;
- cross-article and cross-domain duplication/contradiction review passes;
- downstream skills can consume knowledge consistently.

### Status

`Frozen — 181/181 knowledge articles`

---

## 15. Phase 11 — Skill Library Expansion

### Objective

Expand the reusable skill library with QA capabilities that are not already owned by the six Phase 4 foundation skills.

### Inventory Decision

The Phase 4 baseline was reviewed before expansion. The following existing skills remain canonical and are not reimplemented in Phase 11:

```text
requirement-analyzer
business-rule-extractor
scenario-generator
testcase-generator
coverage-reviewer
regression-impact
```

`regression-analyzer` is not added as a separate skill because the proposed capability materially overlaps `regression-impact`, which already owns change-impact analysis, affected-area identification, regression-scope identification, and regression prioritization.

### Canonical Expansion Scope

Phase 11 tracks exactly five new skills:

| Skill | Primary Responsibility | Status |
|---|---|---|
| `risk-analyzer` | Analyze and structure QA/product risk for downstream prioritization and coverage decisions. | Planned |
| `bug-report-reviewer` | Assess bug-report completeness, clarity, reproducibility, evidence, and actionable quality. | Planned |
| `api-test-generator` | Generate API-specific test artifacts using API knowledge and confirmed interface contracts. | Planned |
| `sql-validation` | Define SQL/database validation logic for confirmed data requirements without inventing schema assumptions. | Planned |
| `test-data-generator` | Generate structured test-data requirements and datasets within confirmed constraints and privacy boundaries. | Planned |

Progress:

```text
0 / 5 expansion skills Completed
```

### Skill Completion Gate

A Phase 11 skill counts as completed only when:

1. the canonical skill artifact exists;
2. purpose and capability boundary are explicit;
3. input and output contracts are defined;
4. processing/workflow behavior is defined;
5. dependencies on standards, templates, knowledge, and upstream artifacts are explicit;
6. exclusions prevent overlap with other skills;
7. validation and quality controls are defined;
8. self-review is complete and blocking issues are fixed.

File creation alone does not increment Phase 11 progress.

### Phase Freeze Gate

Phase 11 may move from `Completed` to `Frozen` only after:

- all 5 expansion skills pass their completion gates;
- cross-skill ownership review passes;
- workflow compatibility is reviewed;
- shared-knowledge dependencies are consistent;
- `skills/README.md`, physical folders, and roadmap registry agree;
- no blocking cross-skill issue remains.

### Boundaries

Phase 11 does not:

- duplicate Phase 4 skills;
- implement deterministic scripts planned for Phase 12;
- create platform-specific adapters planned for Phase 13;
- invent project-specific requirements, API contracts, schemas, policies, or data rules.

### Status

`In Progress — 0/5 expansion skills`

### Implementation Order

```text
1. risk-analyzer
2. bug-report-reviewer
3. api-test-generator
4. sql-validation
5. test-data-generator
```

The order may be changed only when a reviewed dependency requires it.

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

Roadmap automation implementation also belongs to this phase. Until then, `roadmap-status.json` is the canonical machine-readable registry and roadmap synchronization is performed as part of the component completion workflow.

### Exit Criteria

- required scripts have purposeful implementations;
- validation scripts detect intended structural issues;
- evaluation tooling consumes Phase 8 definitions correctly;
- scripts have explicit failure behavior;
- automation does not redefine canonical framework semantics.

### Status

`Planned`

---

## 17. Phase 13 — Platform Integration

### Objective

Make the platform-independent QA-AI framework consumable by supported AI platforms.

### Initial Targets

```text
ChatGPT
Claude
```

### Adapter Principle

```text
QA-AI Core → Platform Adapter → Platform Runtime
```

Adapters may translate packaging and execution mechanics but must preserve skill semantics, workflow contracts, knowledge meaning, output expectations, and evaluation criteria.

### Exit Criteria

A platform integration is complete when required framework assets can be consumed by that platform, configuration is documented, representative workflows execute successfully, and platform-specific behavior does not redefine core QA-AI architecture.

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

Later phases may depend on multiple earlier layers even though the roadmap is presented sequentially.

---

## 19. Roadmap Progress Tracking

### 19.1 Source of Truth

`roadmap-status.json` is the machine-readable source of truth for implementation status and tracked component progress.

`docs/11-Roadmap.md` is the human-readable canonical roadmap and must remain synchronized with the registry.

### 19.2 Tracking Unit

Progress is measured at the roadmap deliverable/component level, not by arbitrary file count.

Examples:

```text
Knowledge article → valid Phase 10 tracking unit
Expansion skill   → valid Phase 11 tracking unit
README edit       → not automatically a progress increment
```

### 19.3 Synchronization Trigger

Roadmap status must be recalculated when a tracked component passes or loses its defined quality gate.

Until Phase 12 implements deterministic automation, the completion workflow must update both:

```text
roadmap-status.json
        ↕
docs/11-Roadmap.md
```

### 19.4 Validation Rule

A phase cannot be marked `Completed` merely because all expected physical files exist.

A phase cannot be marked `Frozen` until its phase-level cross-component review passes.

### 19.5 Future Automation

Phase 12 should implement deterministic collection, validation, and roadmap synchronization based on this contract rather than introducing a new status model.

---

## 20. Current Implementation Focus

```text
Current Phase: Phase 11 — Skill Library Expansion
Foundation Skills: 6/6 Completed (Phase 4 baseline)
Expansion Skills: 0/5 Completed
Next Component: risk-analyzer
```

The next implementation activity is to define and build `skills/risk-analyzer/` using the established skill architecture and the Phase 11 completion gate.

---

## 21. Change Governance

Roadmap changes must preserve:

- phase boundaries;
- component ownership;
- status lifecycle semantics;
- machine-readable/human-readable synchronization;
- traceability between implemented artifacts and reported progress.

Changes to canonical phase scope or tracked component inventory require explicit review before the registry is updated.
