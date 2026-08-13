# Risk Analyzer

## Purpose

The `risk-analyzer` skill transforms structured requirement and business context into a structured QA risk analysis that helps downstream QA capabilities prioritize coverage and attention.

The skill focuses on testing risk: what may fail, why it matters, where uncertainty exists, and which areas deserve stronger validation. It does not generate detailed test scenarios or test cases.

---

## Capability

This skill provides reusable risk-based QA analysis.

Capability flow:

```text
Structured Requirement / Business Context
        ↓
Identify Risk Sources
        ↓
Describe Failure Conditions
        ↓
Assess Likelihood and Impact
        ↓
Prioritize Risks
        ↓
Map Risks to QA Focus Areas
        ↓
Structured Risk Analysis
```

Risk analysis must distinguish supported facts from assumptions. Missing information that materially affects risk should be represented explicitly rather than silently invented.

---

## When To Use

Use this skill when:

- requirements contain business-critical or failure-sensitive behavior;
- testing effort needs risk-based prioritization;
- requirement ambiguity may create delivery or quality risk;
- downstream scenario generation needs explicit high-risk focus areas;
- changes affect important workflows, data, permissions, integrations, or state transitions;
- a standalone QA risk assessment is required before test design.

---

## Input

### Required Input

At least one authoritative analysis source is required, such as:

- Structured Requirement Analysis;
- requirement specification or user story with sufficient context;
- structured change description.

### Optional Input

Useful supporting inputs include:

- Structured Business Rule Model;
- domain context;
- existing workflows or state models;
- known defects or historical failure areas;
- integration context;
- security, API, database, or data-flow context;
- existing test coverage;
- release or change scope.

Optional information must refine the analysis without overriding authoritative project inputs.

---

## Processing

### Step 1 — Establish Analysis Scope

Identify the feature, change, actors, affected artifacts, critical outcomes, and known boundaries. Separate confirmed scope from assumptions and unresolved questions.

### Step 2 — Identify Risk Sources

Inspect the available inputs for risk sources including:

- complex or conflicting business rules;
- critical state transitions;
- permissions and role boundaries;
- data integrity and persistence;
- integrations and external dependencies;
- concurrency and timing;
- failure recovery and partial completion;
- sensitive or regulated data handling;
- high-value business outcomes;
- requirement ambiguity or missing acceptance criteria;
- compatibility or regression-sensitive behavior.

Risk sources must be grounded in the available context.

### Step 3 — Formulate Risk Statements

Represent each material risk as a testable failure-oriented statement describing:

- risk condition;
- affected area or actor;
- potential failure;
- potential consequence;
- evidence/source supporting the risk.

Avoid generic statements such as “the feature may fail” when a more specific failure mode can be derived.

### Step 4 — Assess Likelihood and Impact

Assess likelihood and impact using the applicable project or framework scale.

If no authoritative numeric scoring model is supplied, use qualitative levels such as High / Medium / Low and explain the reasoning. Do not invent probability percentages, financial loss, regulatory penalties, or business thresholds.

### Step 5 — Prioritize Risks

Prioritize risks according to the supported likelihood/impact assessment, business criticality, uncertainty, dependency concentration, and recoverability.

Equal scores do not require identical QA treatment when failure consequences or uncertainty differ.

### Step 6 — Map Risks to QA Focus Areas

For each material risk, identify the QA attention required, such as:

- scenario coverage focus;
- boundary or negative testing;
- state-transition validation;
- decision-table coverage;
- API validation;
- database validation;
- permission testing;
- concurrency testing;
- recovery/idempotency checks;
- regression focus.

This mapping provides guidance; it does not generate the detailed tests owned by downstream skills.

### Step 7 — Identify Residual Uncertainty

Capture assumptions, missing evidence, unresolved questions, and risks that cannot be reliably assessed from the available inputs.

### Step 8 — Produce Structured Risk Analysis

Organize findings into a reusable artifact with stable identifiers and traceability to upstream requirements or rules where available.

---

## Output

The skill produces a Structured Risk Analysis.

Typical output fields include:

| Field | Description |
|---|---|
| Risk ID | Stable identifier within the analysis |
| Source / Traceability | Requirement, rule, change, or context supporting the risk |
| Risk Area | Functional, data, integration, permission, state, etc. |
| Risk Statement | Specific failure-oriented risk |
| Likelihood | Supported qualitative or project-defined assessment |
| Impact | Supported qualitative or project-defined assessment |
| Priority | Relative QA priority |
| QA Focus | Recommended validation focus |
| Assumptions | Assumptions affecting assessment |
| Open Questions | Missing information requiring clarification |

The exact rendering should follow applicable shared output standards and templates.

---

## Dependencies

The skill may consume:

| Resource | Purpose |
|---|---|
| `shared/standards/` | Apply documentation, output, and framework conventions |
| `shared/templates/` | Structure supported analysis outputs |
| `shared/checklists/` | Validate requirement/test considerations where applicable |
| `shared/prompt-patterns/` | Apply reusable analytical reasoning patterns |
| `shared/knowledge/qa/` | Risk, requirement, lifecycle, and QA context |
| `shared/knowledge/testing-techniques/` | Map risk to appropriate test-design focus |
| `shared/knowledge/api/` | Support API-specific risk reasoning when relevant |
| `shared/knowledge/database/` | Support persistence/data-integrity risk reasoning when relevant |
| `shared/knowledge/domain/` | Support business/domain reasoning when relevant |

Shared knowledge is generic guidance. Authoritative project requirements and rules take precedence.

---

## Consumers

The Structured Risk Analysis may be consumed by:

- `scenario-generator` for risk-prioritized scenario coverage;
- `testcase-generator` for prioritization context;
- `coverage-reviewer` for checking risk coverage;
- `regression-impact` when change risk affects regression scope;
- workflows that perform requirement-to-test generation or review.

The skill may also be used standalone for QA planning and requirement review.

---

## Limitations

This skill does not:

- generate detailed test scenarios;
- generate executable test cases;
- define project risk appetite or business thresholds;
- calculate unsupported financial, legal, safety, or regulatory impact;
- replace security threat modeling or specialist safety analysis;
- infer production incident probability without evidence;
- override authoritative business priorities;
- perform regression impact analysis;
- execute tests or verify runtime behavior.

When evidence is insufficient, the output must preserve uncertainty.

---

## Validation

The output should be validated to ensure:

- every material risk is grounded in an input, supported inference, or explicitly labeled assumption;
- risk statements describe concrete failure conditions and consequences;
- likelihood, impact, and priority do not imply unsupported precision;
- critical business rules, states, roles, data, integrations, and recovery paths are considered when applicable;
- QA focus recommendations are actionable without duplicating downstream test generation;
- duplicate risks are consolidated without losing distinct consequences;
- assumptions and open questions are visible;
- traceability is preserved where upstream identifiers exist;
- project-specific facts override generic knowledge;
- the output can be consumed by downstream skills without additional interpretation.