# QA-AI Implementation Roadmap

> Version: 1.4.0  
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
| Phase 14 | Controlled Runtime Evaluation & Benchmark Baseline | Frozen | 6/6 phase14_stages |
| Phase 15 | Operational Usage & Project Adoption | Frozen | 6/6 phase15_stages |
| Phase 16 | Project Workspace & Artifact Lifecycle | Frozen | 6/6 phase16_stages |
| Phase 17 | Operational Export & Interoperability | Frozen | 6/6 phase17_stages |

<!-- ROADMAP_STATUS:END -->

Current baseline and active phase:

```text
Latest Frozen Phase: Phase 17 — Operational Export & Interoperability
Canonical Skill Library: 6/6
Knowledge Baseline: 181/181
Canonical Scripts: 25 / 8 groups
Platform Adapters: ChatGPT + Claude + Cursor (3/3 Frozen)
Active Phase: None — next phase not yet opened
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

## 18. Phase 14 — Controlled Runtime Evaluation & Benchmark Baseline

### Objective

Convert the frozen evaluation definitions, deterministic evaluation tooling, and supported platform adapters into measured runtime evidence and a reproducible benchmark baseline.

Phase 14 validates the behavior of the existing QA-AI framework under controlled execution. It does not redefine canonical QA semantics.

### Dependencies

Phase 14 depends on the frozen baselines established by:

- Phase 8 — controlled datasets, golden references, evaluation criteria, rubrics, scoring definitions, and benchmark definitions;
- Phase 12 — deterministic evaluation and benchmark tooling;
- Phase 13 — frozen ChatGPT, Claude, and Cursor platform adapters.

### Tracking Unit

`evaluation_run_set`

A controlled evaluation run set uses equivalent authoritative inputs and a defined evaluation configuration across the supported runtime targets.

The minimum Phase 14 baseline is:

```text
At least 1 controlled dataset
        ×
ChatGPT + Claude + Cursor
        ×
Defined evaluation configuration
```

### Scope

#### 14.1 Evaluation Execution Definition

Define the controlled execution contract before any measured run is treated as benchmark evidence.

This includes:

- controlled requirement dataset selection;
- evaluated artifacts/capabilities;
- applicable criteria, rubrics, and scoring configuration;
- runtime and adapter configuration metadata;
- evidence and traceability requirements.

#### 14.2 Controlled Runtime Execution

Execute the approved controlled input set through the frozen supported adapters:

```text
ChatGPT
Claude
Cursor
```

Equivalent source inputs and evaluation semantics must be preserved across platforms. Platform-native mechanics may differ, but they must not redefine the evaluated QA behavior.

#### 14.3 Evaluation Results

Produce measured evaluation evidence using the existing Phase 8 evaluation semantics and Phase 12 tooling.

Evaluation should cover the applicable quality dimensions, including:

- requirement fidelity;
- assumption control;
- traceability;
- coverage;
- output/contract compliance.

Measured results must be derived from actual generated artifacts. Scores must not be invented to complete the benchmark structure.

#### 14.4 Benchmark Records

Create benchmark records only from actual controlled execution and evaluation results.

The Phase 14 benchmark baseline should support:

- baseline benchmark evidence;
- cross-platform comparison;
- regression-ready comparison for future framework changes.

Benchmark definitions remain definitions until execution evidence exists; they must not be represented as measured benchmark records prematurely.

#### 14.5 Reproducibility & Traceability

Each accepted run set must preserve sufficient metadata to reconstruct what was evaluated.

At minimum, traceability should identify:

- dataset and dataset version/reference;
- framework version or repository revision;
- platform/runtime;
- adapter/configuration;
- generated artifact set;
- evaluation configuration;
- run identifier and timestamp.

#### 14.6 Final Quality Gate

Perform a cross-platform review of the measured evidence before freezing the baseline.

The gate must confirm:

- equivalent controlled inputs were used;
- scoring semantics were applied consistently;
- benchmark records are backed by actual execution evidence;
- reproducibility and traceability are sufficient;
- unresolved platform differences are documented rather than normalized away;
- the resulting baseline is suitable for future regression comparison.

### Deliverables

Phase 14 is expected to produce:

1. an approved controlled evaluation execution definition;
2. controlled runtime outputs for ChatGPT, Claude, and Cursor;
3. measured evaluation results for the selected run set;
4. baseline and cross-platform benchmark records backed by execution evidence;
5. reproducibility/traceability metadata for accepted runs;
6. an approved regression-ready quality baseline.

Runtime-generated artifacts remain runtime evidence and must not silently become canonical framework definitions.

### Out of Scope

Phase 14 does not include:

- adding new canonical skills;
- adding new canonical workflows;
- redesigning platform adapters;
- changing canonical QA semantics;
- inventing benchmark scores or records without controlled execution;
- using textual similarity as the primary quality gate.

A new skill, workflow, adapter change, or semantic change requires separate evidence and roadmap review rather than being absorbed into benchmark execution.

### Exit Criteria

Phase 14 may move toward freeze only when:

1. at least one controlled dataset has been executed on ChatGPT, Claude, and Cursor under a defined evaluation configuration;
2. each accepted run preserves generated artifacts, evaluation results, and sufficient runtime metadata for traceability;
3. at least one baseline benchmark record has been produced from actual controlled execution and reviewed;
4. cross-platform comparison uses equivalent controlled inputs and evaluation semantics;
5. a regression-ready baseline exists for future framework changes;
6. no unresolved blocking issue remains for reproducibility, traceability, or scoring semantics.

### Status

`In Progress — 1/6 Phase 14 stages`

---

## 19. Phase Dependencies

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
   ↓
Phase 14 Controlled Runtime Evaluation & Benchmark Baseline
```

Phase 14 specifically consumes the frozen Phase 8 evaluation definitions, Phase 12 deterministic tooling, and Phase 13 runtime adapters.

---

## 20. Roadmap Progress Tracking

### 20.1 Source of Truth

`roadmap-status.json` is the machine-readable source of truth. This roadmap is its synchronized human-readable representation.

### 20.2 Tracking Unit

Progress is measured at roadmap deliverable/component level, not arbitrary file count.

### 20.3 Update Rule

When roadmap status changes:

1. update `roadmap-status.json`;
2. validate it;
3. regenerate/synchronize the roadmap status block;
4. review the resulting diff;
5. commit the status update.

### 20.4 Validation Commands

```bash
python scripts/roadmap/validate_progress.py
python scripts/roadmap/update_roadmap.py --check
```

---

## 21. Roadmap Quality Gate

Before a phase is frozen, verify:

- scope is complete;
- deliverables exist and are internally consistent;
- cross-component dependencies are valid;
- validation scripts pass;
- examples/runtime evidence are sufficient where applicable;
- unresolved issues are non-blocking or explicitly deferred;
- roadmap status matches verified repository state.

---

## 22. Current Framework Baseline

```text
Latest Frozen Phase: Phase 13 — Platform Integration

Canonical Skills:      11
Canonical Workflows:   3
Knowledge Articles:    181
Canonical Scripts:     25
Platform Adapters:     3

Active Phase:
Phase 14 — Controlled Runtime Evaluation & Benchmark Baseline
```

---

## 23. Next Implementation Order

```text
Phase 14
  1. Evaluation Execution Definition
  2. Controlled Runtime Execution
  3. Evaluation Results
  4. Benchmark Records
  5. Reproducibility & Traceability
  6. Final Quality Gate
```

Phase 14 should not be frozen until measured runtime evidence, benchmark records, reproducibility metadata, and cross-platform review all pass the defined quality gate.
