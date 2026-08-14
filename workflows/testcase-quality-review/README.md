# Testcase Quality Review Workflow

## Purpose

The `testcase-quality-review` workflow coordinates coverage review of an existing structured test artifact set against sufficient authoritative coverage sources.

It orchestrates `skills/coverage-reviewer`. It does not generate or modify tests, invent missing source behavior, or redefine the coverage-review capability.

---

## When To Use

Use this workflow when:

- existing test cases or scenarios need completeness, consistency, or traceability review;
- test coverage must be evaluated before execution, reuse, or release decisions;
- requirement, rule, risk, or technical source material is available to establish the expected coverage baseline.

Do not use it to generate tests, execute tests, perform regression impact analysis, or review automation code.

---

## Input

### Required Input

The workflow requires both:

1. at least one structured test artifact set to review; and
2. sufficient authoritative source material to establish what that artifact set is expected to cover.

Valid combinations include:

- Structured Test Case Model + scenario/requirement sources;
- Structured Test Scenario Model + requirement/business-rule sources;
- specialized API/SQL test artifacts + authoritative technical sources.

A test artifact set alone is not sufficient evidence for completeness when the expected source scope is unknown.

### Optional Input

Supporting context may include:

- Structured Requirement Analysis;
- Structured Business Rule Model;
- Structured Risk Analysis;
- Structured API Test Model;
- Structured SQL Validation Model;
- Structured Test Data Model;
- existing traceability matrix;
- project-specific coverage criteria;
- previous coverage assessment.

Missing or conflicting source material must remain visible as a review limitation rather than being reconstructed as confirmed behavior.

---

## Workflow Flow

```text
Test Artifact Set + Authoritative Coverage Sources
        ↓
Validate Review Baseline
        ↓
Coverage Reviewer
        ↓
Structured Coverage Assessment
```

---

## Workflow Steps

### Step 1: Validate Review Input

Confirm that the review target and sufficient coverage sources are available. Identify review scope, source authority, missing evidence, and any limitation that affects confidence.

### Step 2: Establish Coverage Baseline

Identify the applicable requirements, business rules, risks, flows, interfaces, states, data conditions, and technical expectations that define the expected review scope.

### Step 3: Review Coverage and Traceability

Execute `skills/coverage-reviewer` using the test artifacts and authoritative coverage sources. Map test artifacts to supported source behavior and identify uncovered sources or orphan tests without inventing links.

### Step 4: Review Consistency and Duplication

Assess incompatible expectations, duplicate coverage with no distinct value, inconsistent preconditions/data, and broken traceability.

### Step 5: Review Risk and Technical Coverage

When applicable source material exists, assess material risk coverage and relevant API, SQL, persistence, and data-partition coverage without regenerating specialized tests.

### Step 6: Produce and Validate Coverage Assessment

Produce the structured coverage assessment and verify that every finding is supported by the supplied artifacts or explicitly labeled as a limitation/open question.

---

## Required Skills

| Skill | Purpose |
|---|---|
| `skills/coverage-reviewer` | Evaluate coverage, traceability, gaps, duplication, and consistency against authoritative coverage sources |

Other skills are not implicitly executed. Their existing outputs may be supplied as source or supporting context when valid.

---

## Required Resources

Participating capabilities may resolve applicable resources from:

| Resource | Purpose |
|---|---|
| `shared/standards/` | Artifact and output conventions |
| `shared/templates/` | Coverage assessment structure |
| `shared/checklists/` | Review quality controls |
| `shared/prompt-patterns/` | Reusable review instructions |
| `shared/knowledge/` | Generic QA/technical knowledge where relevant |

Authoritative project sources override generic framework knowledge.

---

## Output

The workflow produces a Structured Coverage Assessment that may contain:

- coverage findings and gaps;
- source-to-test traceability;
- risk and technical coverage findings where applicable;
- duplication and consistency findings;
- recommended coverage actions;
- assumptions, limitations, and open questions.

The workflow produces findings only; it does not automatically regenerate, modify, or approve tests.

---

## Validation

The workflow is complete when:

- a valid test artifact set and sufficient authoritative coverage sources were reviewed;
- the expected coverage baseline is explicit;
- findings are traceable to supplied evidence;
- material gaps, duplication, and inconsistencies are represented;
- missing evidence remains visible rather than being invented;
- the output satisfies `coverage-reviewer` and applicable shared standards/templates.
