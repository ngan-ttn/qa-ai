# Risk Analyzer

## Purpose

The `risk-analyzer` skill transforms structured requirement and business context into a structured QA risk analysis that helps downstream QA capabilities prioritize coverage and attention.

The skill focuses on testing risk: what may fail, why it matters, where uncertainty exists, and which areas deserve stronger validation. It does not generate detailed test scenarios or test cases.

---

## Capability

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

Inspect the available inputs for risk sources including complex or conflicting business rules, critical state transitions, permission boundaries, data integrity, integrations, concurrency/timing, failure recovery, sensitive data, high-value outcomes, ambiguity, and regression-sensitive behavior.

### Step 3 — Formulate Risk Statements

Represent each material risk as a testable failure-oriented statement describing the risk condition, affected area or actor, potential failure, potential consequence, and supporting evidence.

### Step 4 — Assess Likelihood and Impact

Assess likelihood and impact using the applicable project or framework scale. If no authoritative scoring model exists, use supported qualitative levels or `Not Rated`; do not invent probabilities, monetary loss, penalties, or thresholds.

### Step 5 — Prioritize Risks

Prioritize risks according to supported likelihood/impact, business criticality, uncertainty, dependency concentration, and recoverability.

### Step 6 — Map Risks to QA Focus Areas

Identify appropriate QA attention such as boundary, state-transition, decision-table, permission, API, database, concurrency, recovery, or regression focus without generating downstream detailed tests.

### Step 7 — Identify Residual Uncertainty

Capture assumptions, missing evidence, unresolved questions, and risks that cannot be reliably assessed.

### Step 8 — Produce Structured Risk Analysis

Organize findings with stable identifiers and upstream traceability.

---

## Output

The canonical rendering follows `shared/templates/Risk-Analysis.md` and uses a **hybrid document with a table-oriented Risk Register**.

The risk inventory should use these canonical columns:

| Risk ID | Area / Feature | Risk Description | Trigger / Cause | Impact | Likelihood | Severity / Exposure | Mitigation / QA Focus | Traceability | Status |
|---|---|---|---|---|---|---|---|---|---|

Supporting assumptions, dependencies, monitoring notes, and open questions remain separate sections when useful.

Each material risk must remain evidence-grounded, independently reviewable, and traceable to requirement/rule/change context. Unsupported numeric precision is not allowed.

---

## Dependencies

| Resource | Purpose |
|---|---|
| `shared/standards/` | Apply documentation, output, and framework conventions |
| `shared/templates/` | Structure and canonical rendering of risk outputs |
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

---

## Validation

Validate that:

- every material risk is grounded in an input, supported inference, or explicitly labeled assumption;
- risk statements describe concrete failure conditions and consequences;
- likelihood, impact, and priority do not imply unsupported precision;
- critical business rules, states, roles, data, integrations, and recovery paths are considered when applicable;
- QA focus recommendations are actionable without duplicating downstream test generation;
- duplicate risks are consolidated without losing distinct consequences;
- assumptions and open questions are visible;
- traceability is preserved where upstream identifiers exist;
- the canonical risk table remains scanable and export-friendly;
- project-specific facts override generic knowledge.
