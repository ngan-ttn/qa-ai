# Requirement Analyzer

## Purpose

The `requirement-analyzer` skill transforms unstructured requirement information into structured requirement understanding that serves as the foundation for downstream QA capabilities.

It organizes what the source says, its scope, actors, flows, constraints, dependencies, assumptions, and unresolved questions. It does not own business-rule extraction, risk assessment, or test design.

---

## Capability

```text
Requirement Information
        ↓
Establish Source and Context
        ↓
Identify Scope / Actors / Flows
        ↓
Identify Inputs / Outputs / Dependencies
        ↓
Separate Facts / Assumptions / Gaps
        ↓
Structured Requirement Analysis
```

---

## When To Use

Use this skill when a requirement, user story, specification, acceptance criteria, change request, or related project material must be converted into structured QA-consumable understanding.

---

## Input

### Required Input

At least one authoritative requirement source, such as:

- requirement document;
- user story;
- feature specification;
- acceptance criteria;
- change description.

### Optional Input

- business/domain context;
- UI mockups;
- API/interface specifications;
- existing workflow/state documentation;
- implementation notes explicitly supplied as context;
- related historical requirements.

Source authority and conflicts should be preserved rather than silently reconciled.

---

## Processing

### Step 1 — Establish Source Context

Identify the requested outcome, source documents, stated scope, and any source-authority information available.

### Step 2 — Identify Functional Scope

Capture included behavior, excluded/out-of-scope behavior, actors, entry/exit conditions, and important user/system flows.

### Step 3 — Identify Information Elements

Capture inputs, outputs, entities, states, dependencies, constraints, interfaces, permissions, and stated acceptance expectations.

### Step 4 — Preserve Business-Rule Candidates

Identify statements that appear to contain conditions, constraints, calculations, permissions, or decisions as candidates for downstream extraction. Do not fully classify or normalize them as business rules here.

### Step 5 — Detect Uncertainty

Separate confirmed facts, supported interpretations, assumptions, conflicts, missing information, and clarification questions.

### Step 6 — Produce Structured Requirement Analysis

Organize the result with traceability to source material where identifiers are available.

---

## Output

Typical fields include:

- feature summary and objective;
- in-scope/out-of-scope behavior;
- actors/roles;
- user/system flows;
- inputs/outputs/entities/states;
- dependencies/interfaces;
- constraints;
- business-rule candidates;
- assumptions;
- conflicts;
- clarification questions;
- source traceability.

---

## Dependencies

| Resource | Purpose |
|---|---|
| `shared/standards/` | Documentation/output conventions |
| `shared/templates/` | Requirement analysis structure |
| `shared/checklists/` | Requirement review controls |
| `shared/prompt-patterns/` | Reusable analysis reasoning |
| `shared/knowledge/qa/` | Requirement-engineering and QA context |
| `shared/knowledge/domain/` | Domain vocabulary/context when relevant |
| `shared/knowledge/api/` | Interface interpretation when requirements contain API behavior |
| `shared/knowledge/database/` | Persistence interpretation when explicitly relevant |

Generic knowledge must not override authoritative project requirements.

---

## Consumers

The output may be consumed by:

- `business-rule-extractor`;
- `risk-analyzer`;
- `scenario-generator`;
- `regression-impact` when analyzing an authoritative change;
- technical skills when requirement context is relevant;
- testcase-generation and regression workflows.

---

## Limitations

This skill does not:

- finalize/classify business rules;
- score QA risks;
- generate test scenarios or test cases;
- perform coverage review;
- perform regression impact analysis;
- invent missing requirements;
- treat implementation observations as requirements unless the project identifies them as authoritative.

---

## Validation

Validate that:

- source meaning and terminology are preserved;
- scope, actors, flows, dependencies, and constraints are represented;
- business-rule candidates are not prematurely converted into invented rules;
- facts, assumptions, conflicts, and questions are distinguishable;
- traceability is retained where possible;
- generic knowledge does not introduce project-specific behavior;
- downstream skills can consume the analysis without needing to reread the raw source for basic structure.