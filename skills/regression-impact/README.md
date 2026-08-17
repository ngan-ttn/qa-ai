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
Define Minimum / Recommended / Full Changed-Feature Scope
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

### Step 6 — Define Regression Scope Tiers

Use the canonical tiers in `shared/templates/Regression.md`:

1. **Minimum / Release-Gate Regression** — smallest defensible release-critical set focused on direct change paths, critical boundaries/states, highest-risk confirmed behavior, and strongly supported dependencies.
2. **Recommended Regression** — Minimum plus justified adjacent/dependent behavior, important alternate partitions/states, and material Medium/High-risk coverage.
3. **Full Changed-Feature Verification** — all valid confirmed functional coverage for the changed feature, including depth/display cases that are not required in smaller tiers.

Do not target a fixed percentage or testcase count. If Minimum necessarily approaches Full verification, explain the evidence for that result.

### Step 7 — Prioritize Regression Areas

Prioritize based on change proximity, dependency strength, business criticality, failure consequence, historical evidence, and coverage gaps. Do not invent project-specific probability, cost, or release thresholds.

### Step 8 — Produce Structured Regression Impact Analysis

Organize the result into a reusable decision-support artifact with assumptions and open questions visible.

---

## Output

The canonical rendering follows `shared/templates/Regression.md` and uses a **hybrid document with a table-oriented Regression Impact / Coverage section**.

The impact inventory should use these canonical columns:

| Impact ID | Area / Module | Change Relationship | Regression Scope / Behavior to Revalidate | Impact Type | Evidence / Traceability | Priority | Existing Coverage Reference | Decision |
|---|---|---|---|---|---|---|---|---|

Supporting change overview, excluded scope, entry/exit criteria, assumptions/open questions, execution notes, and regression-tier summaries remain section-based.

The regression output must make clear:

- what changed and why an area is related;
- direct/indirect/potential impact distinction;
- the behavior to revalidate, not only a broad module name;
- existing scenario/testcase coverage that can be reused;
- evidence supporting Include / Exclude / Clarify decisions;
- Minimum / Release-Gate scope;
- Recommended Regression scope;
- Full Changed-Feature Verification scope;
- uncertainty without inventing implementation coupling.

---

## Dependencies

| Resource | Purpose |
|---|---|
| `shared/standards/` | Output and documentation conventions |
| `shared/templates/` | Regression analysis structure and canonical rendering |
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
- regression decisions include rationale/evidence;
- unsupported implementation assumptions are visible;
- uncertainty and missing dependency information are explicit;
- Minimum / Release-Gate, Recommended, and Full Changed-Feature tiers follow their canonical selection semantics rather than arbitrary counts;
- every selected testcase/scenario reference exists in supplied artifacts;
- reported scope counts reconcile exactly with unique selected IDs;
- Recommended is a justified superset of Minimum where both are produced;
- the canonical regression table remains scanable and export-friendly;
- the output is actionable without requiring downstream consumers to reconstruct the impact reasoning.
