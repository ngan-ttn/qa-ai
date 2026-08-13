# Business Rule Extractor

## Purpose

The `business-rule-extractor` skill transforms structured requirement analysis and authoritative business context into a structured business rule model.

It owns rule identification, normalization, classification, relationships, exceptions, and uncertainty. It does not invent business policy or generate testing artifacts.

---

## Capability

```text
Structured Requirement Analysis + Authoritative Context
        ↓
Identify Rule Statements / Candidates
        ↓
Normalize Conditions and Outcomes
        ↓
Classify Rules
        ↓
Resolve Relationships / Conflicts / Exceptions
        ↓
Structured Business Rule Model
```

---

## When To Use

Use this skill when requirement analysis contains business logic, decisions, constraints, permissions, calculations, eligibility, state rules, or exceptions that need explicit structured representation.

---

## Input

### Required Input

- Structured Requirement Analysis or equivalent structured authoritative requirement context containing business-rule candidates.

### Optional Input

- original requirement/user story/acceptance criteria;
- business policy/process documentation;
- domain context;
- state/workflow models;
- existing business-rule catalog;
- project-defined rule precedence or effective-date information.

---

## Processing

### Step 1 — Identify Supported Rules

Extract explicit rules and supported rule implications that are necessary to represent stated behavior. An implication must be traceable to source facts; plausible domain behavior is not enough to create a rule.

### Step 2 — Normalize Rule Structure

Represent conditions, triggers, subjects, actions/outcomes, constraints, exceptions, and effective scope without changing source meaning.

### Step 3 — Classify Rules

Classify rules using applicable project/framework categories such as validation, decision, calculation, permission, state, eligibility, constraint, or derivation.

### Step 4 — Resolve Relationships

Identify dependencies, precedence when explicitly known, mutual exclusions, compound conditions, exceptions, and interactions between rules.

### Step 5 — Detect Gaps and Conflicts

Flag missing outcomes, conflicting rules, ambiguous conditions, undefined defaults, unclear precedence, or unsupported thresholds. Do not silently choose a rule when authority is unclear.

### Step 6 — Produce Structured Business Rule Model

Provide stable IDs and traceability to authoritative sources.

---

## Output

Typical fields include:

- Rule ID;
- source traceability;
- rule category;
- condition/trigger;
- action/outcome;
- scope/actor/state;
- dependencies/related rules;
- exception/default behavior when defined;
- precedence/effective period when defined;
- assumptions/conflicts/open questions.

---

## Dependencies

| Resource | Purpose |
|---|---|
| `shared/standards/` | Output/documentation conventions |
| `shared/templates/` | Business-rule structure |
| `shared/checklists/` | Requirement/rule quality review where applicable |
| `shared/prompt-patterns/` | Reusable extraction reasoning |
| `shared/knowledge/domain/` | Business-rule/domain semantics |
| `shared/knowledge/qa/` | Requirement and QA context |

Generic domain knowledge may help interpret terminology but cannot create project-specific rules.

---

## Consumers

The output may be consumed by:

- `risk-analyzer`;
- `scenario-generator`;
- `testcase-generator` as supporting detail;
- `test-data-generator` for rule-constrained data;
- `api-test-generator` when API behavior implements the rule;
- `regression-impact` when rules change;
- testcase-generation and regression workflows.

---

## Limitations

This skill does not:

- analyze raw requirements as its primary responsibility;
- invent unstated policy, thresholds, formulas, precedence, or default behavior;
- score risks;
- generate scenarios/testcases/test data;
- perform regression impact analysis;
- resolve business conflicts without authoritative evidence.

---

## Validation

Validate that:

- every rule is traceable to authoritative content or a clearly labeled supported implication;
- conditions and outcomes preserve source meaning;
- rule classification does not alter semantics;
- dependencies, exceptions, conflicts, and unknown precedence are visible;
- project-specific values are never supplied from generic knowledge;
- duplicate rules are consolidated without losing scope differences;
- downstream consumers can distinguish confirmed rules from unresolved questions.