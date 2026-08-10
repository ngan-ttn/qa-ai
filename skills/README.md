# Skills

## Purpose

The `skills` module defines the core QA capabilities of the system.

Each skill is responsible for a single capability within the QA lifecycle and transforms one structured artifact into another through a well-defined processing flow.

Together, these skills form a progressive capability pipeline that supports requirement understanding, QA artifact generation, and quality assessment.

---

## Architecture Overview

The QA capability pipeline is organized into three logical layers.

```text
                 QA Capability Pipeline

               Raw Requirement
                      │
                      ▼
        ┌──────────────────────────┐
        │     Analysis Layer       │
        └──────────────────────────┘
                      │
                      ▼
        Requirement Analyzer
                      │
                      ▼
    Structured Requirement Analysis
                      │
                      ▼
      Business Rule Extractor
                      │
                      ▼
     Structured Business Rule Model
                      │
                      ▼
        ┌──────────────────────────┐
        │    Generation Layer      │
        └──────────────────────────┘
                      │
                      ▼
         Scenario Generator
                      │
                      ▼
     Structured Test Scenario Model
                      │
                      ▼
         Testcase Generator
                      │
                      ▼
      Structured Test Case Model
                      │
                      ▼
        ┌──────────────────────────┐
        │    Assessment Layer      │
        └──────────────────────────┘
                      │
                      ▼
        Coverage Reviewer
                      │
                      ▼
   Structured Coverage Assessment
                      │
                      ▼
         Regression Impact
                      │
                      ▼
Structured Regression Impact Analysis
```

---

## Architecture Principles

The skills module follows several architectural principles.

### Progressive Refinement

Each skill consumes the structured output of the previous skill and produces a new structured artifact for downstream capabilities.

---

### Single Responsibility

Each skill owns exactly one QA capability.

Responsibilities do not overlap.

---

### Capability-Based Design

Skills describe capabilities rather than implementation details.

The internal implementation of a capability may evolve without changing its external contract.

---

### Reusable Components

Skills are designed to be reusable across different workflows.

A workflow orchestrates multiple skills to accomplish a larger QA objective.

---

### Shared Standards

Skills consume common standards, templates, prompt patterns, and checklists from the `shared` module instead of redefining them.

---

## Skill Categories

### Analysis Layer

Transforms raw requirement information into structured analytical artifacts.

| Skill | Output |
|--------|--------|
| `requirement-analyzer` | Structured Requirement Analysis |
| `business-rule-extractor` | Structured Business Rule Model |

---

### Generation Layer

Transforms structured analytical artifacts into structured testing artifacts.

| Skill | Output |
|--------|--------|
| `scenario-generator` | Structured Test Scenario Model |
| `testcase-generator` | Structured Test Case Model |

---

### Assessment Layer

Evaluates structured QA artifacts and produces decision-support artifacts.

| Skill | Output |
|--------|--------|
| `coverage-reviewer` | Structured Coverage Assessment |
| `regression-impact` | Structured Regression Impact Analysis |

---

## Skill Structure

Every skill follows the same documentation structure.

```text
Purpose

Capability

When To Use

Input

Processing

Output

Dependencies

Consumers

Limitations

Validation
```

This consistent structure makes every skill easier to understand, maintain, and extend.

---

## Dependencies

Skills may consume reusable resources from the shared module.

```text
shared/
├── standards/
├── templates/
├── checklists/
└── prompt-patterns/
```

Skills reference these resources but do not redefine them.

---

## Workflows

Skills are building blocks rather than end-user features.

Multiple skills can be composed into workflows such as:

- Testcase Generation
- Regression Analysis

Workflow definitions are maintained separately under the `workflows` module.

---

## Design Goals

The skills module is designed to provide:

- Clear capability boundaries
- Progressive artifact refinement
- High reusability
- Consistent documentation
- Scalable architecture
- Maintainable QA capabilities