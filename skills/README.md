# Skills

## Purpose

The `skills` module defines reusable, platform-independent QA capabilities for the QA-AI framework.

Each skill owns one primary capability, declares a clear input/output contract, consumes shared framework resources where appropriate, and can participate in one or more workflows without embedding workflow orchestration inside the skill itself.

The skill library contains a six-skill foundation established in Phase 4 and five expansion skills introduced in Phase 11.

---

## Canonical Skill Inventory

The canonical target baseline contains 11 skills.

| Capability Group | Skill | Phase | Primary Output |
|---|---|---|---|
| Requirement Understanding | `requirement-analyzer` | Phase 4 | Structured Requirement Analysis |
| Requirement Understanding | `business-rule-extractor` | Phase 4 | Structured Business Rule Model |
| Requirement Understanding | `risk-analyzer` | Phase 11 | Structured Risk Analysis |
| Test Design | `scenario-generator` | Phase 4 | Structured Test Scenario Model |
| Test Design | `testcase-generator` | Phase 4 | Structured Test Case Model |
| Test Design | `test-data-generator` | Phase 11 | Structured Test Data Model |
| Quality Assessment | `coverage-reviewer` | Phase 4 | Structured Coverage Assessment |
| Quality Assessment | `regression-impact` | Phase 4 | Structured Regression Impact Analysis |
| Quality Assessment | `bug-report-reviewer` | Phase 11 | Structured Bug Report Review |
| Technical Validation | `api-test-generator` | Phase 11 | Structured API Test Model |
| Technical Validation | `sql-validation` | Phase 11 | Structured SQL Validation Model |

`regression-impact` remains the canonical regression-impact capability. A separate `regression-analyzer` skill is intentionally not introduced because it would materially overlap with the existing capability.

---

## Architecture Overview

The skill library is organized into four capability groups rather than one mandatory linear pipeline.

```text
                         QA Skill Library

        ┌───────────────────────────────────────────┐
        │ Requirement Understanding                 │
        │                                           │
        │ requirement-analyzer                      │
        │ business-rule-extractor                   │
        │ risk-analyzer                             │
        └───────────────────────────────────────────┘
                         │
                         ▼
        ┌───────────────────────────────────────────┐
        │ Test Design                               │
        │                                           │
        │ scenario-generator                        │
        │ testcase-generator                        │
        │ test-data-generator                       │
        └───────────────────────────────────────────┘
                         │
                         ▼
        ┌───────────────────────────────────────────┐
        │ Quality Assessment                        │
        │                                           │
        │ coverage-reviewer                         │
        │ regression-impact                         │
        │ bug-report-reviewer                       │
        └───────────────────────────────────────────┘

        ┌───────────────────────────────────────────┐
        │ Technical Validation                      │
        │                                           │
        │ api-test-generator                        │
        │ sql-validation                            │
        └───────────────────────────────────────────┘
```

The main requirement-to-test flow may progressively refine artifacts, but specialized skills can also run independently when their required inputs are available.

---

## Architecture Principles

### Single Responsibility

Each skill owns one primary QA capability. A skill must not absorb responsibilities already owned by another skill merely because those responsibilities are commonly used together.

### Contract-Based Composition

Skills communicate through explicit input and output artifacts. Downstream consumers should not need to infer hidden intermediate reasoning.

### Progressive Refinement Without Mandatory Linearity

Some capabilities naturally form a refinement chain, but the library does not require every skill to execute in one universal sequence. Specialized technical or review capabilities may be invoked independently.

### Generic Core and Specialized Capabilities

Generic test-design skills own technology-neutral reasoning. Technical skills specialize that reasoning for a technical surface without redefining the generic capability.

For example:

```text
scenario-generator / testcase-generator
        ↓ generic test design
api-test-generator
        ↓ API-specific test design

requirement/business/test artifacts
        ↓ persistence validation need
sql-validation
        ↓ database/SQL-specific validation
```

### Shared Knowledge and Standards

Skills consume reusable resources from `shared/` and should reference relevant knowledge rather than duplicate it.

Authoritative project inputs always take precedence over generic shared knowledge.

### Platform Independence

Skills define QA capabilities, not ChatGPT-, Claude-, or other platform-specific execution behavior. Platform packaging belongs to adapters/integration layers.

---

## Capability Groups

### Requirement Understanding

| Skill | Owns | Does Not Own |
|---|---|---|
| `requirement-analyzer` | Requirement interpretation and structured requirement analysis | Business-rule extraction, test generation |
| `business-rule-extractor` | Explicit and derived business-rule structuring | Requirement rewriting, test generation |
| `risk-analyzer` | QA risk identification, assessment, prioritization, and risk-to-test guidance | Detailed scenario/testcase generation |

### Test Design

| Skill | Owns | Does Not Own |
|---|---|---|
| `scenario-generator` | Technology-neutral test scenario generation | Detailed executable test cases |
| `testcase-generator` | Detailed technology-neutral test-case generation | Coverage review or technical specialization |
| `test-data-generator` | Test-data requirements, partitions, datasets, and constraints | Environment provisioning or runtime fixture architecture |

### Quality Assessment

| Skill | Owns | Does Not Own |
|---|---|---|
| `coverage-reviewer` | Completeness, consistency, and traceability assessment | Generating missing test artifacts |
| `regression-impact` | Change impact, affected areas, regression scope, and priority | Regression execution planning or test execution |
| `bug-report-reviewer` | Bug-report completeness, reproducibility, evidence, and actionability review | Defect lifecycle ownership or fixing defects |

### Technical Validation

| Skill | Owns | Does Not Own |
|---|---|---|
| `api-test-generator` | API-specific test design and validation coverage | Generic test-design ownership or API implementation |
| `sql-validation` | Structured database/SQL validation logic for QA verification | Database implementation, schema design, or query optimization |

---

## Skill Structure

Every skill README follows the same canonical structure:

```text
# Skill Name

## Purpose
## Capability
## When To Use
## Input
### Required Input
### Optional Input
## Processing
### Step 1 — ...
### Step 2 — ...
## Output
## Dependencies
## Consumers
## Limitations
## Validation
```

Additional subsections may be added when they materially improve the capability contract, but the canonical sections must remain recognizable and responsibility boundaries must stay explicit.

---

## Dependencies

Skills may consume reusable resources from:

```text
shared/
├── standards/
├── templates/
├── checklists/
├── prompt-patterns/
├── knowledge/
└── glossary/
```

A skill references these resources but does not redefine their canonical content.

Knowledge should be selected according to the task. For example, `api-test-generator` may consume API and testing-technique knowledge, while `sql-validation` may consume database and QA knowledge.

---

## Consumers and Workflows

Skills are reusable building blocks. Workflows coordinate multiple skills when a larger QA objective requires orchestration.

A workflow may use only the skills required for its objective. The existence of 11 canonical skills does not imply that every workflow must invoke all 11.

Workflow definitions remain under `workflows/`.

---

## Phase 11 Expansion

Phase 11 adds five capabilities to the six-skill Phase 4 foundation:

1. `risk-analyzer`
2. `bug-report-reviewer`
3. `api-test-generator`
4. `sql-validation`
5. `test-data-generator`

The expansion order is intentional: establish cross-cutting risk reasoning first, then review quality, then technical specialization, and finally reusable test-data generation.

A Phase 11 skill is counted as completed only after its capability contract is complete, self-review issues are fixed, dependencies and boundaries are validated, and the artifact passes the applicable quality gate.

The Phase 11 baseline is frozen only after all five expansion skills pass cross-skill consistency review.

---

## Design Goals

The skills module is designed to provide:

- clear and non-overlapping capability ownership;
- explicit reusable contracts;
- progressive artifact refinement where appropriate;
- standalone specialized capabilities where appropriate;
- consistent documentation;
- shared-knowledge reuse;
- platform independence;
- scalable workflow composition;
- maintainable QA reasoning boundaries.