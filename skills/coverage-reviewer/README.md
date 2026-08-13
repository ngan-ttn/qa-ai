# Coverage Reviewer

## Purpose

The `coverage-reviewer` skill evaluates whether structured QA test artifacts adequately cover their authoritative requirements, business rules, risks, and relevant technical validation needs.

It owns coverage assessment and traceability review. It does not generate missing tests itself or perform change-impact analysis.

---

## Capability

```text
Test Artifacts + Coverage Sources
        ↓
Establish Coverage Baseline
        ↓
Map Traceability
        ↓
Assess Requirement / Rule / Risk Coverage
        ↓
Assess Technical and Data Coverage
        ↓
Detect Gaps / Duplication / Inconsistency
        ↓
Structured Coverage Assessment
```

---

## When To Use

Use this skill when test scenarios/cases or specialized technical test models need completeness, consistency, traceability, or risk-coverage review.

---

## Input

### Required Input

At least one test artifact set plus sufficient upstream source material to judge coverage, for example:

- Structured Test Case Model and its scenario/requirement sources; or
- Structured Test Scenario Model and requirement/rule sources; or
- specialized API/SQL test artifacts with authoritative technical sources.

Coverage cannot be assessed reliably from tests alone when the expected coverage source is unknown.

### Optional Input

- Structured Requirement Analysis;
- Structured Business Rule Model;
- Structured Risk Analysis;
- Structured API Test Model;
- Structured SQL Validation Model;
- Structured Test Data Model;
- existing traceability matrix;
- project coverage criteria.

---

## Processing

### Step 1 — Establish Coverage Baseline

Identify which requirements, rules, risks, flows, interfaces, states, data conditions, and project criteria are in scope for review.

### Step 2 — Map Traceability

Map each test artifact to supported upstream sources. Flag orphan tests and uncovered sources without inventing links.

### Step 3 — Assess Behavioral Coverage

Review positive, negative, boundary, state, role/permission, exception, dependency, and recovery coverage where applicable.

### Step 4 — Assess Risk Coverage

When risk analysis exists, verify material risks have appropriate coverage and identify high-risk gaps. Do not redefine risk scores.

### Step 5 — Assess Technical and Data Coverage

Where applicable, review whether API assertions, persistence checks, and test-data partitions required by the source behavior are represented. Specialized outputs are assessed for coverage, not regenerated.

### Step 6 — Assess Consistency and Duplication

Identify contradictory expectations, duplicate tests with no distinct value, broken traceability, inconsistent priority, or incompatible preconditions/data.

### Step 7 — Classify Findings

Separate blocking gaps, material gaps, duplication/maintenance issues, and optional improvements. Preserve uncertainty when the source itself is incomplete.

### Step 8 — Produce Structured Coverage Assessment

Provide traceable findings and recommended coverage actions without creating the missing tests.

---

## Output

Typical fields include:

- Coverage Finding ID;
- source requirement/rule/risk;
- covered-by artifact references;
- coverage status;
- gap/duplication/inconsistency description;
- impact/priority;
- recommended action;
- assumptions/open questions.

---

## Dependencies

| Resource | Purpose |
|---|---|
| `shared/standards/` | Output/documentation conventions |
| `shared/templates/` | Coverage assessment structure |
| `shared/checklists/` | Scenario/testcase review criteria |
| `shared/prompt-patterns/` | Reusable review reasoning |
| `shared/knowledge/qa/` | Coverage, traceability, quality context |
| `shared/knowledge/testing-techniques/` | Expected test-design dimensions |
| `shared/knowledge/api/` | API coverage interpretation when relevant |
| `shared/knowledge/database/` | Persistence coverage interpretation when relevant |
| `shared/knowledge/domain/` | Business coverage semantics when relevant |

---

## Consumers

The output may be consumed by:

- `regression-impact` as coverage evidence;
- `scenario-generator` when scenario gaps require generation;
- `testcase-generator` when testcase gaps require generation;
- `api-test-generator`, `sql-validation`, or `test-data-generator` when specialized gaps are identified;
- testcase-quality-review and regression workflows.

These feedback paths are conditional remediation paths, not mandatory circular dependencies.

---

## Limitations

This skill does not:

- create or modify test artifacts;
- invent requirements or expected behavior;
- recalculate risk models;
- perform regression change-impact analysis;
- execute tests;
- claim completeness when authoritative coverage sources are missing.

---

## Validation

Validate that:

- the coverage baseline is explicit;
- findings trace to authoritative sources and test artifacts;
- requirement, rule, and risk coverage are distinguished where useful;
- technical/data gaps are identified only when relevant;
- duplicate coverage is not confused with deliberate multi-layer validation;
- missing source information is reported as uncertainty rather than a false gap;
- recommendations identify which owning skill should remediate the gap;
- the assessment does not silently generate replacement artifacts;
- downstream consumers can act on findings without reconstructing traceability.