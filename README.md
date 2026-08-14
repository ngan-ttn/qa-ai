# QA-AI

> **A reusable, platform-independent AI framework for Software Quality Assurance**

QA-AI is a structured framework for enabling AI systems to perform software Quality Assurance activities consistently using reusable QA knowledge, skills, workflows, standards, examples, evaluation assets, deterministic tooling, and platform adapters.

Instead of embedding QA behavior inside long platform-specific prompts, QA-AI separates reusable QA capabilities into maintainable framework components and keeps platform-specific integrations as thin consumers of the canonical core.

---

## Vision

Build a reusable QA framework where QA knowledge and capabilities remain independent from individual AI models and platforms while producing consistent, traceable, and maintainable QA outputs across supported execution environments.

---

## Goals

- Build reusable QA knowledge and capabilities.
- Standardize AI-generated QA artifacts.
- Separate QA knowledge from platform-specific prompting.
- Reduce duplicated prompt engineering.
- Define reusable QA skills and workflows.
- Provide controlled examples and evaluation datasets.
- Support measurable QA output quality.
- Provide deterministic validation, evaluation, export, and roadmap tooling.
- Support multiple AI runtimes without redefining canonical QA behavior.
- Keep framework components maintainable, reviewable, and extensible.

---

## Core Architecture

QA-AI separates QA behavior into reusable framework layers.

```text
Standards and Conventions
        ↓
Knowledge and Templates
        ↓
Skills
        ↓
Workflows
        ↓
Examples
        ↓
Datasets and Evaluation
        ↓
Deterministic Tooling
        ↓
Platform Integration
```

| Component | Responsibility |
|---|---|
| Standards | Define shared documentation, naming, metadata, output, and prompt conventions. |
| Templates | Define reusable structures for QA artifacts. |
| Checklists | Provide reusable quality-review criteria. |
| Knowledge | Provide reusable QA, testing, API, database, and domain knowledge. |
| Skills | Define focused reusable QA capabilities with explicit input/output contracts. |
| Workflows | Coordinate multiple QA capabilities into ordered processes. |
| Examples | Demonstrate expected input-to-output transformations and traceability. |
| Datasets | Provide controlled requirements, golden references, evaluation definitions, benchmarks, and fixture models. |
| Scripts | Provide deterministic validation, knowledge, prompt, workflow, evaluation, export, utility, and roadmap automation. |
| Platform Integration | Adapt the platform-independent framework for supported AI runtimes without redefining QA semantics. |

Detailed architecture is defined in `docs/01-Architecture.md`.

---

## Repository Structure

```text
QA-AI/
├── README.md
├── FRAMEWORK.md
├── CHANGELOG.md
├── VERSION
├── LICENSE
├── manifest.json
├── roadmap-status.json
│
├── docs/
├── shared/
│   ├── standards/
│   ├── templates/
│   ├── checklists/
│   ├── prompt-patterns/
│   ├── knowledge/
│   └── glossary/
│
├── skills/
├── workflows/
├── examples/
├── datasets/
├── scripts/
└── adapters/
```

### `docs/`

Contains canonical framework architecture, concepts, design decisions, development guidance, usage guidance, versioning, contribution rules, and the implementation roadmap.

### `shared/`

Contains reusable assets shared across skills and workflows: standards, templates, checklists, prompt patterns, glossary content, and the frozen knowledge library.

### `skills/`

Contains the canonical QA skill library.

Current frozen baseline: **11 skills**.

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

`regression-impact` is the canonical regression capability. A separate broad `regression-analyzer` skill is intentionally excluded to avoid overlapping ownership.

### `workflows/`

Contains the canonical multi-step QA workflows.

```text
workflows/
├── testcase-generation/
├── testcase-quality-review/
└── regression-analysis/
```

### `examples/`

Contains representative input and expected-output examples for standalone QA capabilities and end-to-end artifact generation.

### `datasets/`

Contains controlled assets used to evaluate QA-AI behavior.

```text
datasets/
├── requirements/
├── golden-output/
├── evaluation/
├── benchmark/
└── fixtures/
```

The dataset architecture distinguishes canonical definitions from runtime execution artifacts.

```text
Fixture Model → Fixture Instance
Benchmark Definition → Benchmark Execution → Benchmark Record
```

Runtime instances and benchmark records are created only when actual execution requires them.

### `scripts/`

Contains the frozen deterministic tooling baseline.

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

These scripts validate repository contracts, knowledge/catalog state, workflow behavior, evaluation semantics, export/package behavior, metadata/output consistency, and roadmap synchronization.

### `adapters/`

Contains platform-specific integration packages that consume the canonical QA-AI core.

Frozen Phase 13 baseline:

```text
adapters/
├── chatgpt/
├── claude/
└── cursor/
```

Adapters own platform-native loading, packaging, routing, and installation mechanics. They do not redefine skill behavior, workflow contracts, shared standards, knowledge content, or evaluation semantics.

---

## Core Concepts

| Concept | Description |
|---|---|
| Knowledge | Reusable information used to support QA reasoning. |
| Skill | A focused reusable QA capability with explicit ownership and contract. |
| Workflow | An ordered process coordinating QA capabilities. |
| Template | A standardized structure for QA artifacts. |
| Checklist | Criteria used to review QA artifact quality. |
| Standard | Shared framework conventions and rules. |
| Example | A representative input/output reference. |
| Dataset | Controlled data used for examples, evaluation, and benchmarking. |
| Golden Output | A canonical reference used to evaluate expected QA output characteristics. |
| Fixture Model | A reusable definition of controlled execution context. |
| Benchmark Definition | A canonical definition of how a comparison should be performed. |
| Adapter | A platform-native integration layer that consumes the canonical QA-AI core. |

Detailed terminology is defined in `docs/02-Core-Concepts.md` and `shared/glossary/`.

---

## Framework Capabilities

The current canonical framework supports reusable definitions and quality gates for:

- requirement analysis;
- business-rule extraction;
- QA risk analysis;
- test-scenario generation;
- executable test-case generation;
- test-data design;
- coverage review;
- regression impact analysis;
- bug-report review;
- API-specific test design;
- SQL/database validation;
- testcase quality review;
- controlled artifact evaluation and benchmarking;
- deterministic repository validation and export;
- multi-platform runtime integration.

---

## Source Priority and Grounding

QA-AI preserves this precedence across supported runtimes:

```text
Authoritative project requirement / project context
        ↓
Applicable canonical workflow
        ↓
Owning canonical skill
        ↓
Applicable shared standards / templates / checklists / knowledge
        ↓
Platform adapter guidance
        ↓
Generic model knowledge
```

Missing project information must remain explicit. QA-AI does not treat common practice as project fact and does not invent project-specific behavior, thresholds, schemas, dependencies, roles, status values, expected results, API contracts, or implementation details.

---

## Documentation

Canonical framework documentation is maintained under `docs/`.

| Document | Purpose |
|---|---|
| `01-Architecture.md` | Framework and repository architecture |
| `02-Core-Concepts.md` | Core framework terminology |
| `03-Design-Decisions.md` | Architectural design rationale |
| `04-Repository-Convention.md` | Repository conventions |
| `05-Skill-Development-Guide.md` | Skill development guidance |
| `06-Knowledge-Management.md` | Knowledge architecture and management |
| `07-Versioning.md` | Versioning strategy |
| `08-Workflow-Design.md` | Workflow design guidance |
| `09-Contribution.md` | Contribution guidance |
| `10-How-To-Use.md` | Framework usage guidance |
| `11-Roadmap.md` | Canonical implementation roadmap |

---

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Read the core documentation

Recommended order:

1. `README.md`
2. `FRAMEWORK.md`
3. `docs/01-Architecture.md`
4. `docs/02-Core-Concepts.md`
5. `docs/03-Design-Decisions.md`
6. `docs/04-Repository-Convention.md`
7. `docs/10-How-To-Use.md`
8. `docs/11-Roadmap.md`

### 3. Explore reusable QA behavior

```text
shared/
skills/
workflows/
```

### 4. Explore examples and evaluation assets

```text
examples/
datasets/
```

### 5. Run deterministic validation

Representative validation entry points include:

```bash
python scripts/validation/validate_structure.py
python scripts/validation/validate_metadata.py
python scripts/validation/validate_links.py
python scripts/validation/validate_outputs.py
python scripts/knowledge/validate_catalog.py
python scripts/roadmap/validate_progress.py
python scripts/roadmap/update_roadmap.py --check
```

Platform adapter validation:

```bash
python adapters/validate_adapters.py
```

---

## Platform Integration

Phase 13 provides a frozen baseline for three supported runtimes.

| Platform | Integration Model | Status |
|---|---|---|
| ChatGPT | Custom GPT Instructions + bounded generated Knowledge bundles | Frozen |
| Claude | Claude Code repository-root `CLAUDE.md` + canonical repository references | Frozen |
| Cursor | Repository-root `.cursor/rules/*.mdc` + `.cursor/commands/*.md` | Frozen |

Platform adapters may translate loading, packaging, routing, and invocation mechanics, but canonical QA behavior remains owned by the platform-independent core.

See `adapters/README.md` and `adapters/Integration-Contract.md` for the supported runtime topology and installation constraints.

---

## Design Principles

### Knowledge First

QA behavior should be supported by explicit reusable knowledge rather than hidden inside prompts.

### Single Responsibility

Each framework component has a clear responsibility and avoids unnecessary overlap.

### Documentation First

Important framework behavior is documented before downstream automation depends on it.

### Reusability

Knowledge, skills, workflows, and evaluation definitions are reusable across contexts and supported runtimes.

### Platform Independence

Canonical QA behavior does not depend on ChatGPT, Claude, Cursor, or another specific AI runtime.

### Standardization

QA outputs follow shared conventions, templates, and quality criteria.

### Traceability

Generated QA artifacts remain traceable to source requirements, rules, assumptions, and upstream artifacts where applicable.

### Validation Before Expansion

Stable framework layers are reviewed and quality-gated before downstream expansion.

---

## Current Implementation Status

The implemented and quality-gated baseline currently covers **Phase 1 through Phase 13**.

| Phase | Status |
|---|---|
| Phase 1 — Framework Foundation | Completed |
| Phase 2 — Shared Standards and Foundations | Completed |
| Phase 3 — Workflow Library | Completed |
| Phase 4 — Skill Library Foundation | Completed |
| Phase 5 — Knowledge Foundation | Completed |
| Phase 6 — Examples and End-to-End Validation | Completed |
| Phase 7 — Framework Integration and Validation | Completed |
| Phase 8 — Datasets and Evaluation | Frozen |
| Phase 9 — Repository Completion and Alignment | Completed |
| Phase 10 — Knowledge Library Completion | Frozen |
| Phase 11 — Skill Library Expansion | Frozen |
| Phase 12 — Scripts Implementation | Frozen |
| Phase 13 — Platform Integration | Frozen |

Current frozen baseline:

```text
Latest Frozen Phase: Phase 13 — Platform Integration
Canonical Skill Library: 11/11
Knowledge Baseline: 181/181
Canonical Scripts: 25 / 8 groups
Platform Adapters: ChatGPT + Claude + Cursor (3/3 Frozen)
```

Machine-readable status is maintained in `roadmap-status.json`; the synchronized human-readable roadmap is `docs/11-Roadmap.md`.

---

## Current and Future Scope

Phase 1–13 is the implemented and quality-gated baseline.

Future expansion is intentionally **not predefined by stale placeholders**. Any subsequent roadmap phase must be explicitly proposed, scoped, reviewed, and added to the canonical roadmap before implementation begins.

A future capability or adapter should not be added merely because a platform or QA topic exists. New scope must demonstrate a distinct responsibility, avoid overlap with the 11-skill baseline, preserve framework contracts, and pass the applicable quality gates.

---

## Versioning

QA-AI follows the versioning strategy defined in `docs/07-Versioning.md`.

Repository-level version: `VERSION`  
Release/change history: `CHANGELOG.md`

---

## Contributing

Before modifying framework components, review:

- `docs/04-Repository-Convention.md`
- `docs/05-Skill-Development-Guide.md`
- `docs/06-Knowledge-Management.md`
- `docs/08-Workflow-Design.md`
- `docs/09-Contribution.md`

Changes should preserve established ownership boundaries, source priority, artifact contracts, and adapter/core separation.

---

## Roadmap

The canonical implementation roadmap is maintained in `docs/11-Roadmap.md`.

The roadmap defines:

- completed and frozen implementation phases;
- phase dependencies;
- tracked component baselines;
- phase exit/freeze criteria;
- progress synchronization rules;
- explicitly approved future expansion when such scope is added.

`roadmap-status.json` is the machine-readable source of truth for tracked phase status.

---

## Project Status

**Active Development — Stable Phase 1–13 Baseline**

```text
Latest Frozen Phase: Phase 13 — Platform Integration
Current State: Phase 1–13 implemented and quality-gated
Next Phase: Not yet defined
```

Before any Phase 14 implementation, the new phase must first be defined and reviewed in the canonical roadmap.

---

## License

QA-AI is released under the MIT License. Repository licensing terms are defined in `LICENSE`.

---

## Summary

QA-AI provides a structured, reusable foundation for AI-assisted Software Quality Assurance.

The frozen Phase 1–13 baseline combines:

```text
QA Knowledge
    ↓
Standards and Templates
    ↓
11 Canonical Skills
    ↓
3 Canonical Workflows
    ↓
Examples
    ↓
Datasets and Evaluation
    ↓
25 Deterministic Scripts
    ↓
ChatGPT + Claude + Cursor Adapters
```

The framework now has a quality-gated, multi-platform baseline. Any next roadmap phase should be defined from verified repository gaps rather than from outdated planned placeholders.
