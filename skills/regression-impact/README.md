# Regression Impact

## Purpose

The `regression-impact` skill transforms an authoritative change description plus relevant baseline QA context into a structured regression impact analysis.

It owns change-impact reasoning, affected-area identification, regression-scope definition, and regression prioritization. It does not generate new test scenarios or test cases, review testcase quality, or create an execution schedule.

---

## Capability

```text
Authoritative Change Description + Baseline Context
        ↓
Establish Change Delta
        ↓
Trace Directly Affected Behavior
        ↓
Trace Dependent / Indirect Impact
        ↓
Map Existing Coverage
        ↓
Define and Prioritize Regression Scope
        ↓
Structured Regression Impact Analysis
```

Regression scope must be derived from the actual change and known dependencies. Existing coverage is evidence used during the analysis; it is not a substitute for the change description.

---

## When To Use

Use this skill when:

- a requirement, rule, interface, workflow, schema, or implementation behavior changes;
- regression scope must be identified or reprioritized;
- existing QA artifacts need change-impact assessment;
- a release/change requires traceable regression reasoning;
- downstream QA activities need a structured affected-area model.

---

## Input

### Required Input

At least:

- an authoritative change description or structured before/after requirement context; and
- sufficient baseline context to identify what existing behavior may be affected.

Baseline context may be supplied through requirement analysis, business rules, architecture/dependency information, or existing QA artifacts.

### Optional Input

- Structured Coverage Assessment;
- Structured Risk Analysis;
- Structured Test Case Model;
- Structured Test Scenario Model;
- Structured Business Rule Model;
- Structured Requirement Analysis;
- API/interface dependencies;
- database/data dependencies;
- historical defect or regression information;
- release scope.

A coverage assessment is strongly useful when available, but it is not a mandatory prerequisite for every standalone impact analysis.

---

## Processing

### Step 1 — Establish the Change Delta

Identify what changed, what did not change, affected actors/interfaces/data, and the authoritative source of the change. If before/after behavior is unclear, record the ambiguity rather than inventing a delta.

### Step 2 — Identify Direct Impact

Trace the change to directly affected requirements, rules, flows, states, interfaces, data, and existing QA artifacts.

### Step 3 — Identify Indirect Impact

Follow known dependencies to identify adjacent or shared behavior that may regress, including shared rules, integrations, permissions, persistence, state transitions, reusable components, and downstream/upstream effects.

Do not infer implementation coupling that is not supported by project context.

### Step 4 — Map Existing Coverage

When coverage/test artifacts are available, determine which existing scenarios/cases already cover affected behavior, which require update, which remain valid, and where gaps exist.

### Step 5 — Incorporate Risk Context

Use Structured Risk Analysis or supported risk reasoning to distinguish business-critical, failure-sensitive, uncertain, or high-blast-radius areas. Risk informs priority; this skill does not redefine the risk model.

### Step 6 — Define Regression Scope

Classify regression areas as required, recommended, unaffected/retained, or uncertain according to supported evidence. Preserve traceability from each scope decision to the change/dependency that justifies it.

### Step 7 — Prioritize Regression Areas

Prioritize based on change proximity, dependency strength, business criticality, failure consequence, historical evidence, and coverage gaps. Do not invent project-specific probability, cost, or release thresholds.

### Step 8 — Produce Structured Regression Impact Analysis

Organize the result into a reusable decision-support artifact with assumptions and open questions visible.

---

## Output

Typical fields include:

| Field | Description |
|---|---|
| Impact ID | Stable identifier |
| Change Trace | Source change driving the impact |
| Affected Area | Requirement, flow, API, data, role, state, etc. |
| Impact Type | Direct, indirect, coverage update, uncertainty |
| Existing Coverage | Relevant existing scenario/test references |
| Regression Decision | Required, recommended, retained/unaffected, uncertain |
| Priority | Supported relative priority |
| Rationale | Evidence supporting scope decision |
| Dependencies | Known impact paths |
| Assumptions / Questions | Missing information affecting confidence |

The exact rendering follows applicable shared output standards and templates.

---

## Dependencies

| Resource | Purpose |
|---|---|
| `shared/standards/` | Output and documentation conventions |
| `shared/templates/` | Regression analysis structure where applicable |
| `shared/checklists/` | Review/coverage quality controls where applicable |
| `shared/prompt-patterns/` | Reusable impact-analysis reasoning |
| `shared/knowledge/qa/` | Regression, risk, lifecycle, traceability context |
| `shared/knowledge/api/` | API dependency reasoning when relevant |
| `shared/knowledge/database/` | Persistence/data dependency reasoning when relevant |
| `shared/knowledge/domain/` | Business dependency/context reasoning when relevant |

Project change information and architecture/dependency evidence override generic knowledge.

---

## Consumers

The output supports:

- regression planning and execution decisions;
- `coverage-reviewer` when post-change coverage needs reassessment;
- `scenario-generator` or `testcase-generator` only when the analysis identifies genuinely missing/changed coverage requiring regeneration;
- `workflows/regression-analysis`;
- future deterministic reporting/export tooling.

These are optional feedback paths, not a mandatory circular pipeline.

---

## Limitations

This skill does not:

- invent a change when no authoritative delta is supplied;
- generate detailed test scenarios or executable test cases;
- review testcase quality as its primary responsibility;
- create regression execution plans or schedules;
- infer undocumented implementation coupling;
- determine release approval;
- execute regression tests;
- replace specialist security/safety impact analysis.

---

## Validation

Validate that:

- every impact finding traces to an authoritative change and supported dependency;
- direct and indirect impact are distinguished;
- unchanged areas are not included merely because they are nearby;
- existing coverage is reused where valid rather than duplicated;
- coverage gaps and outdated tests are explicit;
- risk influences priority without being redefined;
- regression decisions include rationale;
- unsupported implementation assumptions are visible;
- uncertainty and missing dependency information are explicit;
- the output is actionable without requiring downstream consumers to reconstruct the impact reasoning.