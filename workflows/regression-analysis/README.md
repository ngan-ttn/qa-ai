# Regression Analysis Workflow

## Purpose

The `regression-analysis` workflow coordinates regression impact analysis from an authoritative change description plus sufficient baseline context.

It orchestrates `skills/regression-impact`. Existing coverage is supporting evidence when available; it is not a substitute for the source change itself. The workflow does not generate tests, execute regression, or invent undocumented dependencies.

---

## When To Use

Use this workflow when:

- a requirement, rule, interface, workflow, schema, or implementation behavior changes;
- a bug fix or enhancement may affect existing behavior;
- release scope requires traceable regression-impact reasoning;
- existing QA assets need assessment against a confirmed change delta.

Do not use it to create tests, review testcase quality as the primary objective, execute regression, schedule execution, or approve releases.

---

## Input

### Required Input

The workflow requires both:

1. an authoritative change description or structured before/after context; and
2. sufficient baseline context to identify existing behavior that may be affected.

Baseline context may include requirement analysis, business rules, known architecture/dependencies, existing test artifacts, or other authoritative QA/project evidence.

If the change delta cannot be established, the workflow must stop short of a confirmed regression conclusion and surface the missing information.

### Optional Input

Supporting context may include:

- Structured Coverage Assessment;
- Structured Risk Analysis;
- Structured Test Case Model;
- Structured Test Scenario Model;
- Structured Business Rule Model;
- Structured Requirement Analysis;
- API/interface dependencies;
- database/data dependencies;
- historical defect or regression evidence;
- release scope.

Coverage information strengthens regression decisions when available but is not mandatory for every valid standalone impact analysis.

---

## Workflow Flow

```text
Authoritative Change Description + Baseline Context
        ↓
Establish Change Delta
        ↓
Regression Impact
        ↓
Map Existing Coverage / Known Dependencies
        ↓
Structured Regression Impact Analysis
```

---

## Workflow Steps

### Step 1: Validate Regression Input

Confirm the authoritative source of change and verify that enough baseline context exists to reason about affected behavior. Record missing or conflicting evidence explicitly.

### Step 2: Establish Change Delta

Execute the change-delta activity owned by `skills/regression-impact`. Identify what changed, what did not change, and which actors, rules, flows, interfaces, states, or data are directly involved.

### Step 3: Analyze Direct and Indirect Impact

Trace directly affected behavior, then follow only known dependencies to identify supported indirect impact. Unsupported implementation coupling must remain unknown rather than being promoted to confirmed impact.

### Step 4: Map Existing Coverage

When coverage/test artifacts are available, identify existing coverage that remains valid, requires update, or leaves gaps. Absence of a coverage assessment must not erase otherwise supported change-impact evidence.

### Step 5: Incorporate Risk Context

When Structured Risk Analysis or other supported risk evidence exists, use it to inform regression priority without redefining the risk model.

### Step 6: Define and Prioritize Regression Scope

Classify affected areas as required, recommended, retained/unaffected, or uncertain according to evidence. Preserve the rationale and change/dependency trace for each scope decision.

### Step 7: Produce and Validate Regression Analysis

Produce the Structured Regression Impact Analysis and verify that change traces, impact findings, scope decisions, priorities, assumptions, and open questions are internally consistent and evidence-based.

The canonical impact inventory must be rendered as the table defined in `shared/templates/Regression.md`. Supporting change overview, excluded scope, criteria, assumptions, and execution notes remain section-based where appropriate.

---

## Required Skills

| Skill | Purpose |
|---|---|
| `skills/regression-impact` | Transform an authoritative change delta and baseline context into structured regression impact analysis |

Other skills are not implicitly re-executed. Their existing outputs may be supplied as supporting context when valid.

---

## Required Resources

The participating skill may resolve applicable resources from:

| Resource | Purpose |
|---|---|
| `shared/standards/` | Artifact and output conventions |
| `shared/templates/` | Regression analysis structure and canonical table rendering |
| `shared/checklists/` | Review/coverage quality controls where applicable |
| `shared/prompt-patterns/` | Reusable impact-analysis instructions |
| `shared/knowledge/qa/` | Regression/risk context |
| `shared/knowledge/api/` | API dependency context when relevant |
| `shared/knowledge/database/` | Persistence/data dependency context when relevant |
| `shared/knowledge/domain/` | Business dependency context when relevant |

Authoritative project change/dependency evidence overrides generic framework knowledge.

---

## Output

The workflow produces a Structured Regression Impact Analysis using a hybrid document with a table-oriented core:

| Impact ID | Area / Module | Change Relationship | Regression Scope / Behavior to Revalidate | Impact Type | Evidence / Traceability | Priority | Existing Coverage Reference | Decision |
|---|---|---|---|---|---|---|---|---|

The table records the actionable impact inventory. Change overview, exclusions, entry/exit criteria, assumptions, and execution notes may remain narrative sections.

The workflow does not execute regression tests, create an execution schedule, generate missing tests automatically, or approve release readiness.

---

## Validation

The workflow is complete when:

- the authoritative change delta is explicit;
- sufficient baseline context was used;
- impact findings are traceable to change/dependency evidence;
- coverage evidence is applied when available without being treated as the source change;
- unsupported dependencies remain uncertain;
- regression scope and priorities are justified;
- canonical regression table rendering is used;
- output satisfies `regression-impact` and applicable shared standards/templates.
