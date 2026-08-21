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

### Required Inputs for Incremental Regeneration

When this workflow is executed because Change Intelligence recommends `Regenerate` for an artifact that has a prior canonical revision, the prior canonical baseline is no longer optional reference material. It is a required active input for baseline-preserving incremental regeneration.

Revision-aware regeneration therefore requires:

- the authoritative target-revision requirement/upstream artifact;
- the prior canonical version of each artifact being regenerated;
- the applicable change-set and impact/incremental-plan evidence.

If a known prior canonical baseline cannot be retrieved by the runtime, incremental regeneration is `Blocked`. The runtime MUST NOT silently regenerate from the target requirement alone and describe that result as incremental regeneration.

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

For incremental revisions, each regenerated stage also consumes the prior canonical version of its own artifact plus supported change evidence so unchanged semantic inventory can be preserved.

---

## Workflow Steps

### Step 1: Analyze Requirement

Execute `skills/requirement-analyzer` when a valid structured requirement analysis is not already available.

The resulting structured requirement analysis becomes the authoritative upstream artifact for business rule extraction within this workflow execution.

For revision-aware regeneration, compare the prior Requirement Analysis with the target requirement/change evidence. Preserve unaffected analysis identity/content where still valid and modify only supported affected content or explicit corrections.

---

### Step 2: Extract Business Rules

Execute `skills/business-rule-extractor` using the structured requirement analysis.

The resulting structured business rule model should preserve relevant rules, relationships, dependencies, constraints, exceptions, and unresolved items required by downstream scenario generation.

The canonical rule inventory must follow the table-oriented core format defined in `shared/templates/Business-Rule.md`.

For revision-aware regeneration, stable `BR-*` identities MUST be preserved for semantically unchanged rules. A rule may be added, removed, or assigned a new identity only when supported change evidence or an explicit correction rationale justifies that change.

---

### Step 3: Generate Test Scenarios

Execute `skills/scenario-generator` using the structured business rule model.

The resulting structured test scenario model should represent meaningful validation objectives, relevant user journeys, scenario relationships, dependencies, and identified gaps.

The user-facing scenario inventory must be rendered as the canonical table defined in `shared/templates/Scenario.md`; supporting scope/assumption/open-question context may remain section-based.

For revision-aware regeneration, preserve stable scenario identity for semantically unchanged coverage, including clarification-dependent candidates. Do not add/remove/renumber scenarios solely because a different decomposition is aesthetically preferable.

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

For revision-aware regeneration, preserve stable `TC-*` identities where the testcase objective remains semantically the same. Modify the affected row in place when supported change evidence changes data/steps/expected outcome without changing the testcase identity. Do not delete or replace an unaffected testcase merely because a fresh generation would choose different coverage decomposition.

---

## Baseline-Preserving Incremental Regeneration

When Change Intelligence recommends `Regenerate`, apply `shared/standards/Change-Intelligence.md` as an execution contract, not merely planning context.

The workflow MUST distinguish:

```text
Fresh / full generation
    target source only

Incremental regeneration
    target source
    + prior canonical artifact baseline
    + supported change/impact evidence
```

For incremental regeneration:

1. Preserve stable IDs for semantically unchanged `BR-*`, `SC-*`, clarification-dependent scenario IDs, and `TC-*` records.
2. Modify existing records in place when the supported change affects their content but not their semantic identity.
3. Add records only for genuinely new supported behavior/coverage.
4. Remove records only when the authoritative change removes the obligation/coverage or when an explicit correction rationale is documented.
5. Do not renumber surviving IDs simply to close gaps.
6. Do not restructure unresolved behavior into a different candidate inventory unless evidence or explicit correction justifies the decomposition change.
7. Keep no-fabrication and clarification propagation rules unchanged.

The workflow result MUST include a cross-revision reconciliation for each record-oriented artifact:

- Preserved IDs
- Modified IDs
- Added IDs
- Removed IDs + rationale

A changed aggregate count is allowed only when the item-level reconciliation explains it.

If the runtime cannot retrieve the known prior baseline, report incremental regeneration as `Blocked` and request that baseline. Do not substitute nearby examples, memory, File Library artifacts from another run, or a fresh reconstruction.

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

For incremental regeneration, validation must additionally confirm:

- the prior canonical baseline was actually available to the runtime;
- target-revision change evidence was actually available;
- unchanged semantic records preserve their stable IDs;
- every Added/Removed record has a supported reason;
- Removed IDs are not silently dropped;
- surviving IDs are not renumbered without identity-change rationale;
- Preserved/Modified/Added/Removed reconciliation matches the resulting canonical inventories.

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

For incremental regeneration, the workflow also produces a revision reconciliation summary showing Preserved, Modified, Added, and Removed IDs for each record-oriented artifact that changed.

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
- For incremental regeneration, prior-baseline availability and record-level revision reconciliation satisfy the baseline-preserving contract.

This workflow does not perform testcase coverage review, regression impact analysis, test execution, or test result management.
