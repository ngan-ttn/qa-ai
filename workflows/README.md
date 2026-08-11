# Workflows

## Overview

The `workflows` directory contains reusable QA execution flows that coordinate one or more QA skills to complete specific testing activities.

A workflow defines how QA capabilities are sequenced, how artifacts move between stages, which shared resources are applied, and how workflow outputs are validated.

Examples of workflows include:

- Requirement-based testcase generation
- Testcase quality review
- Regression impact analysis

Workflows define orchestration. They do not own the internal capability logic of skills or the detailed content of shared resources.

---

## Purpose

The purpose of workflows is to provide a repeatable and explicit execution process for multi-stage QA tasks.

Skills provide atomic QA capabilities. Shared resources provide reusable standards, templates, checklists, prompt patterns, knowledge, and terminology. Workflows coordinate these components into a defined task flow.

A workflow may define:

- Required inputs
- Required skills
- Skill execution order
- Artifact dependencies
- Applicable shared resources
- Review or validation points
- Intermediate artifacts
- Final outputs
- Completion conditions

---

## Role in QA-AI

The primary runtime relationship is:

```text
User Request
      │
      ▼
FRAMEWORK.md
      │
      ▼
Workflow
      │
      ▼
Skills
      │
      ▼
Shared Resources
      │
      ▼
QA Artifacts
```

Responsibilities remain separated:

```text
FRAMEWORK.md
    → Defines how QA-AI operates and resolves execution

workflows/
    → Defines which capabilities execute and in what sequence

skills/
    → Defines atomic QA capabilities and their input/output contracts

shared/
    → Provides reusable standards, templates, checklists, prompt patterns,
      knowledge, and glossary resources
```

The workflow layer does not replace skill capabilities or shared resources. It coordinates them.

---

## Relationship With Other Components

| Component | Responsibility |
|---|---|
| `FRAMEWORK.md` | Define framework operating and resolution rules |
| `skills/` | Define atomic QA capabilities and capability contracts |
| `shared/standards/` | Define common QA and artifact rules |
| `shared/templates/` | Define output structures and formats |
| `shared/checklists/` | Define reusable validation criteria |
| `shared/prompt-patterns/` | Provide reusable instruction patterns |
| `shared/knowledge/` | Provide reusable QA knowledge |
| `shared/glossary/` | Provide shared terminology |
| `workflows/` | Define multi-skill orchestration and artifact dependencies |

Example:

```text
Requirement Information
        │
        ▼
Testcase Generation Workflow
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
```

Each participating skill may resolve the shared resources required by its own capability contract.

---

## Workflow Concept

A workflow is a reusable orchestration definition for completing a QA task that requires coordinated capabilities or explicit artifact dependencies.

A workflow should define the following.

### Input

Information or artifacts required to start the workflow.

Examples:

- Requirement information
- Structured QA artifacts
- Existing test cases
- Change information
- Coverage assessment

### Process

The ordered stages required to complete the task.

A workflow may:

- Validate input readiness
- Invoke required skills
- Pass validated artifacts between skills
- Reuse existing valid upstream artifacts
- Apply workflow-level review points
- Validate workflow completion

A workflow should not reproduce the detailed processing steps already owned by participating skills.

### Output

The artifacts produced by workflow execution.

Outputs may include:

- Intermediate artifacts consumed by downstream skills
- Final user-facing QA artifacts
- Review assessments
- Regression impact analysis

The workflow should distinguish intermediate artifacts from final deliverables where relevant.

---

## Artifact Dependencies

Workflows must preserve declared artifact dependencies.

Example:

```text
Structured Test Scenario Model
        ↓
Testcase Generator
        ↓
Structured Test Case Model
        ↓
Coverage Reviewer
        ↓
Structured Coverage Assessment
        ↓
Regression Impact
        ↓
Structured Regression Impact Analysis
```

A downstream skill must not execute before its required upstream artifact is available.

When a valid upstream artifact already exists and remains applicable to the current scope, the workflow should reuse it rather than regenerate equivalent information unnecessarily.

---

## Workflow Structure

Each workflow should be organized as:

```text
workflow-name/
└── README.md
```

Each workflow README should normally describe:

```md
## Purpose

## When To Use

## Input

## Workflow Flow

## Workflow Steps

## Required Skills

## Required Resources

## Output

## Validation
```

A section may be omitted only when it is not applicable to the workflow.

Workflow documentation should explain orchestration without duplicating:

- Skill processing logic
- Knowledge articles
- Standards
- Templates
- Checklist definitions

---

## Available Workflows

Current workflows:

| Workflow | Purpose |
|---|---|
| `testcase-generation` | Transform requirement information into structured test scenarios and test cases |
| `testcase-quality-review` | Evaluate completeness, consistency, and traceability of structured test cases |
| `regression-analysis` | Analyze regression impact and determine regression scope from validated QA artifacts |

These workflows may be executed independently when their required inputs are already available or composed as part of a broader QA-AI execution path.

---

## Workflow Boundaries

A workflow owns orchestration only.

A workflow should not:

- Redefine the internal capability logic of a skill
- Store QA knowledge that belongs under `shared/knowledge/`
- Define output formats that belong under `shared/templates/`
- Redefine common rules owned by `shared/standards/`
- Duplicate validation criteria maintained under `shared/checklists/`
- Introduce platform-specific QA behavior
- Invent missing business or system behavior

When another framework component already owns a concern, the workflow should reference or consume that component instead of duplicating it.

---

## Adding a New Workflow

A new workflow should be added when a QA activity requires a reusable orchestration path that is not already covered by an existing workflow.

Before adding a workflow, confirm that:

- The QA objective is distinct from existing workflows
- Multiple capabilities or explicit artifact dependencies require orchestration
- Required skills already exist or are separately defined
- Inputs and outputs can be clearly identified
- Execution order can be explicitly defined
- Workflow-level validation or completion criteria are meaningful

A new workflow should:

- Have a clear purpose
- Define required and optional inputs
- Define participating skills
- Define execution order
- Define artifact dependencies
- Identify relevant shared resources
- Define outputs
- Define validation and completion conditions

New workflows should extend QA-AI orchestration while preserving the responsibility boundaries defined by `FRAMEWORK.md`, `skills/`, and `shared/`.