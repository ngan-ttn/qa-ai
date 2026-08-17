# Testcase Generation Workflow

## Purpose

The `testcase-generation` workflow defines the coordinated process for transforming requirement information into structured test scenarios and executable test cases.

This workflow orchestrates the QA capabilities required to analyze requirement information, extract business rules, generate test scenarios, and generate test cases while reusing intermediate artifacts across stages.

The workflow defines execution order and artifact dependencies. It does not duplicate the internal capability logic owned by individual skills or the output structures owned by shared templates.

---

## When To Use

This workflow should be used when:

- New requirements need test coverage
- New user stories need validation scenarios and test cases
- Acceptance criteria need to be transformed into executable test cases
- Business rules need to be carried through scenario and testcase generation
- Existing feature changes require new or updated test coverage

This workflow should not be used for:

- Reviewing existing testcase quality
- Performing coverage review of an existing testcase set
- Analyzing regression impact
- Executing test cases
- Managing test execution results

---

## Input

### Required Input

The workflow requires requirement information that can be processed by the upstream analysis capability.

Examples:

- Requirement document
- User story
- Acceptance criteria
- Feature specification

### Optional Input

Examples:

- Existing structured requirement analysis
- Existing structured business rule model
- Existing structured test scenario model
- Structured Coverage Assessment
- Business context
- Related QA documents
- Existing test cases for reference

Valid existing upstream artifacts should be reused instead of regenerated when they remain applicable to the current scope.

Missing, ambiguous, or conflicting information should be identified according to the participating skill contracts and framework rules.

---

## Workflow Flow

```text
Requirement Information
        ↓
Requirement Analyzer
        ↓
Structured Requirement Analysis
        ↓
Business Rule Extractor
        ↓
Structured Business Rule Model
        ↓
Scenario Generator
        ↓
Structured Test Scenario Model
        ↓
Testcase Generator
        ↓
Structured Test Case Model
```

Each downstream stage should consume the validated artifact produced by the preceding stage rather than independently reinterpreting the original requirement.

---

## Workflow Steps

### Step 1: Analyze Requirement

Execute `skills/requirement-analyzer` when a valid structured requirement analysis is not already available.

The resulting structured requirement analysis becomes the authoritative upstream artifact for business rule extraction within this workflow execution.

---

### Step 2: Extract Business Rules

Execute `skills/business-rule-extractor` using the structured requirement analysis.

The resulting structured business rule model should preserve relevant rules, relationships, dependencies, constraints, exceptions, and unresolved items required by downstream scenario generation.

The canonical rule inventory must follow the table-oriented core format defined in `shared/templates/Business-Rule.md`.

---

### Step 3: Generate Test Scenarios

Execute `skills/scenario-generator` using the structured business rule model.

The resulting structured test scenario model should represent meaningful validation objectives, relevant user journeys, scenario relationships, dependencies, and identified gaps.

The user-facing scenario inventory must be rendered as the canonical table defined in `shared/templates/Scenario.md`; supporting scope/assumption/open-question context may remain section-based.

---

### Step 4: Generate Test Cases

Execute `skills/testcase-generator` using the structured test scenario model.

When a Structured Coverage Assessment is supplied, use it according to the canonical coverage semantics from `skills/coverage-reviewer`:

- `Covered` — do not add artificial cases merely to increase count.
- `Weakly Covered` — improve testcase precision/decomposition when authoritative behavior already supports it.
- `Gap` — close at testcase level only when the confirmed missing behavior can be represented without changing upstream scenario ownership; otherwise route remediation upstream.
- `Blocked` — do not convert into executable expected results until the authoritative oracle/dependency is resolved.

Generated test cases must be executable, organized, source-grounded, and aligned with the applicable testcase template and standards.

The user-facing executable inventory MUST be rendered as **one canonical Markdown table under `## Test Cases`** as defined in `shared/templates/TestCase.md`.

- Every executable `TC-*` appears exactly once as a row.
- Section-per-testcase rendering such as `### TC-*` is not canonical and must not be used.
- Separate per-testcase steps tables must not be used.
- Ordered steps remain in the `Test Steps` cell using numbered text and `<br>` separators.

---

### Step 5: Validate Workflow Output

Validate that the workflow completed its required artifact chain and that each output satisfies the applicable skill contract.

Validation must confirm:

- Required upstream artifacts are available.
- Business rules remain consistent with the analyzed requirement.
- Test scenarios remain traceable to applicable business behavior.
- Test cases remain aligned with confirmed structured test scenarios.
- Canonical table rendering is used for Business Rules, Test Scenarios, and Test Cases.
- The testcase artifact contains one canonical executable inventory and no section-per-testcase alternate representation.
- Clarification-dependent/blocked behavior without an authoritative oracle is excluded from executable testcase rows.
- Applicable QA standards and templates are followed.
- Missing, duplicate, ambiguous, or conflicting information identified by participating skills remains visible where relevant.
- All reported scenario/testcase/category counts reconcile with actual unique IDs/rows.

Detailed artifact-specific validation criteria remain in the applicable shared checklists and skill definitions.

Coverage review of a generated testcase set is outside this core workflow's mandatory responsibility and may be performed by the applicable quality-review capability/workflow. When an existing Coverage Review is explicitly supplied as input, it is active downstream design evidence rather than a mandatory pipeline stage.

---

## Required Skills

This workflow coordinates the following skills:

| Skill | Purpose |
|---|---|
| `skills/requirement-analyzer` | Transform requirement information into structured requirement analysis |
| `skills/business-rule-extractor` | Transform structured requirement analysis into a structured business rule model |
| `skills/scenario-generator` | Transform structured business rules into a structured test scenario model |
| `skills/testcase-generator` | Transform structured test scenarios into a structured test case model |

The workflow defines how these capabilities are sequenced and connected but does not redefine their internal processing logic.

---

## Required Resources

The participating skills may resolve applicable resources from the shared module, including:

| Resource | Purpose |
|---|---|
| `shared/standards/` | Apply applicable QA and artifact standards |
| `shared/templates/` | Structure generated QA artifacts and canonical table rendering |
| `shared/checklists/` | Support applicable validation activities |
| `shared/prompt-patterns/` | Provide reusable instruction patterns where required by participating skills |

The workflow references shared resources through participating skill dependencies and does not duplicate their detailed content.

---

## Output

The workflow produces the following artifact chain:

- Structured requirement analysis
- Structured business rule model
- Structured test scenario model
- Structured test case model

The primary user-facing deliverables for testcase-generation execution are typically:

- Test scenarios — canonical table-oriented core output
- Test cases — canonical hybrid + table-oriented output with one executable testcase inventory table

Intermediate business-rule output also uses its canonical table-oriented core when exposed. Narrative sections may surround the tables where the shared template requires document-level context.

---

## Validation

The workflow is complete when:

- Required stages have completed or valid existing upstream artifacts have been reused.
- Artifact dependencies are satisfied.
- The structured test scenario model is suitable for testcase generation.
- The structured test case model is suitable for downstream QA activities.
- Applicable standards/templates and canonical table rendering are followed.
- Testcase representation complies with `shared/templates/TestCase.md`.
- Reported aggregate counts reconcile with the actual generated IDs/rows.
- Blocking information gaps are resolved or explicitly reported.

This workflow does not perform testcase coverage review, regression impact analysis, test execution, or test result management.
