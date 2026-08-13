# Skills

## Purpose

The `skills` module defines reusable, platform-independent QA capabilities for QA-AI. Each skill owns one primary capability, exposes explicit input/output contracts, and composes with other skills without embedding workflow orchestration.

The frozen target baseline contains six Phase 4 foundation skills plus five Phase 11 expansion skills.

---

## Canonical Skill Inventory

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

`regression-impact` remains the canonical regression capability. `regression-analyzer` is intentionally excluded because a second broad regression analyzer would overlap its ownership.

---

## Architecture Overview

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

These groups are capability ownership areas, not a mandatory linear execution pipeline.

---

## Architecture Principles

### Single Responsibility

Each skill owns one primary QA capability. Commonly related activities remain separate when their contracts and outputs are materially different.

### Contract-Based Composition

Skills exchange explicit structured artifacts. Consumers should not depend on hidden reasoning from an upstream skill.

### Authoritative Inputs Before Generic Knowledge

Project requirements, rules, schemas, API contracts, policies, and other authoritative sources override generic shared knowledge. Skills must surface missing information rather than use generic knowledge to invent project behavior.

### Progressive Refinement Without Mandatory Linearity

Requirement-to-test work can form a refinement chain, while review and technical skills can run standalone when their required inputs exist.

### Generic Core vs Technical Specialization

`scenario-generator` and `testcase-generator` own technology-neutral test design. `api-test-generator` owns API-specific expansion; `sql-validation` owns database/SQL verification logic. Specialized skills must add technical evidence rather than duplicate generic cases unchanged.

### Feedback Is Not a Hard Dependency Cycle

Some skills can feed corrections back to earlier capabilities. For example, `coverage-reviewer` may identify a gap that causes `scenario-generator` to run again. This is a workflow remediation path, not a required circular dependency.

Likewise:

- `testcase-generator` may consume pre-generated test data, or `test-data-generator` may derive data from already generated cases;
- `api-test-generator` may identify persistence assertions for `sql-validation`, while SQL validation output may later enrich an API test artifact.

No skill may require another skill's output if that other skill simultaneously requires the first skill's output. Workflows choose a direction based on the available authoritative input.

### Platform Independence

Skills define QA behavior, not ChatGPT/Claude/platform packaging.

---

## Capability Ownership

### Requirement Understanding

| Skill | Owns | Does Not Own |
|---|---|---|
| `requirement-analyzer` | Structured requirement understanding, scope, actors, flows, constraints, uncertainty | Final business-rule extraction, risk scoring, test design |
| `business-rule-extractor` | Supported business-rule extraction, normalization, relationships, conflicts | Inventing policy, test generation |
| `risk-analyzer` | QA risk identification, assessment, prioritization, risk-to-test focus | Detailed test generation, regression impact |

### Test Design

| Skill | Owns | Does Not Own |
|---|---|---|
| `scenario-generator` | Technology-neutral scenario-level coverage | Executable testcase detail, API/SQL specialization |
| `testcase-generator` | Executable technology-neutral test cases | API-specific design, SQL logic, reusable data derivation |
| `test-data-generator` | Test-data requirements, partitions, reusable datasets | Runtime provisioning, fixture infrastructure |

### Quality Assessment

| Skill | Owns | Does Not Own |
|---|---|---|
| `coverage-reviewer` | Coverage baseline, traceability, gaps, duplication, consistency | Creating missing tests, change-impact analysis |
| `regression-impact` | Change delta, affected areas, regression scope, priority | Test generation, execution planning |
| `bug-report-reviewer` | Bug-report completeness, reproducibility, evidence, actionability | Defect lifecycle ownership, proving/fixing defects |

### Technical Validation

| Skill | Owns | Does Not Own |
|---|---|---|
| `api-test-generator` | API-specific test design, contract/protocol/security/reliability assertions | Generic test-design ownership, API implementation |
| `sql-validation` | QA-oriented database/SQL verification logic | Schema design, DBA work, query optimization |

---

## Primary Composition Contracts

| Producer | Primary Output | Typical Consumers |
|---|---|---|
| `requirement-analyzer` | Structured Requirement Analysis | business rules, risk, scenarios, regression/technical context |
| `business-rule-extractor` | Structured Business Rule Model | risk, scenarios, data, technical specialization |
| `risk-analyzer` | Structured Risk Analysis | scenarios, testcases, coverage, regression |
| `scenario-generator` | Structured Test Scenario Model | testcases, test data, API specialization, coverage |
| `testcase-generator` | Structured Test Case Model | coverage, test data, API/SQL specialization, regression evidence |
| `test-data-generator` | Structured Test Data Model | testcases, API/SQL tests, QA execution |
| `api-test-generator` | Structured API Test Model | coverage, test data, SQL validation where persistence is relevant |
| `sql-validation` | Structured SQL Validation Model | testcases/API tests as optional enrichment, coverage, QA execution |
| `coverage-reviewer` | Structured Coverage Assessment | regression and conditional remediation paths |
| `regression-impact` | Structured Regression Impact Analysis | regression decision-making and conditional regeneration |
| `bug-report-reviewer` | Structured Bug Report Review | reporter/triage quality workflow |

The table describes typical composition, not mandatory execution order.

---

## Skill Structure

Every skill README uses:

```text
# Skill Name
## Purpose
## Capability
## When To Use
## Input
### Required Input
### Optional Input
## Processing
## Output
## Dependencies
## Consumers
## Limitations
## Validation
```

Additional subsections are allowed when they clarify the contract without changing ownership.

---

## Shared Dependencies

Skills may consume `shared/standards/`, `shared/templates/`, `shared/checklists/`, `shared/prompt-patterns/`, `shared/knowledge/`, and `shared/glossary/` as relevant. They reference shared resources rather than redefining canonical content.

---

## Workflows

Workflows under `workflows/` decide orchestration, optional branches, remediation loops, and execution order. A workflow invokes only the skills needed for its objective; the existence of 11 canonical skills does not imply every workflow uses all 11.

---

## Phase 11 Baseline

Phase 11 adds:

1. `risk-analyzer`
2. `bug-report-reviewer`
3. `api-test-generator`
4. `sql-validation`
5. `test-data-generator`

A skill is complete only after its contract, boundaries, dependencies, consumers, assumptions, and validation criteria pass review. Phase 11 is frozen only after all five expansion skills are complete and the full 11-skill cross-skill review has no blocking overlap or contract issue.

---

## Design Goals

The skill library targets:

- non-overlapping capability ownership;
- explicit and composable artifact contracts;
- safe handling of authoritative vs generic information;
- reusable technology-neutral test design;
- isolated technical specialization;
- traceable quality assessment;
- optional feedback without hard dependency cycles;
- consistent documentation;
- platform independence;
- maintainable workflow composition.