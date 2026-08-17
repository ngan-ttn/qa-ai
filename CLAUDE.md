# QA-AI Claude Code Instructions

Use QA-AI as a platform-independent QA framework. Do not redefine canonical QA behavior inside this adapter.

## Canonical Sources

- Framework overview: @README.md and @FRAMEWORK.md
- Skills: @skills/README.md
- Workflows: @workflows/README.md
- Shared standards: @shared/standards/README.md
- Templates/checklists/prompt patterns: @shared/templates/README.md @shared/checklists/README.md @shared/prompt-patterns/README.md
- Knowledge: @shared/knowledge/README.md
- Evaluation: @datasets/README.md

Load the specific owning skill/workflow and only the relevant shared/knowledge sources for the current task rather than reading the entire repository by default.

## Source Priority

1. authoritative project requirement and user-provided project context;
2. owning QA-AI workflow;
3. owning QA-AI skill;
4. applicable shared standards/templates/checklists/knowledge;
5. generic model knowledge.

Never invent project-specific behavior, thresholds, schemas, dependencies, roles, status values, expected results, implementation mechanisms, storage models, or architectural components when authoritative context is absent.

## Source-Grounding Enforcement

For requirement understanding and every downstream QA artifact:

- classify an item as **Confirmed** only when the authoritative project input directly states it or when the item is a behavioral implication that cannot be false while the stated requirement remains true;
- do not treat an implementation mechanism as a necessary implication. A threshold may require the product to determine whether the threshold is reached, but it does not confirm a counter, persistence strategy, per-account tracking implementation, timestamp, module, service, database field, or other mechanism;
- do not promote a plausible inference into a functional requirement, dependency, business rule, expected result, or system fact merely because it would be a common implementation;
- keep derived observations and assumptions explicitly separate from confirmed requirements, and include them only when they materially help the requested artifact;
- implementation mechanisms such as counters, persistence/storage, timestamps, database fields, services/modules, server-side enforcement, API behavior, and architectural dependencies remain unknown unless authoritative project context establishes them;
- a stated duration or threshold does not authorize inventing an unspecified post-condition or mechanism;
- when the source is minimal, prefer an explicit gap or clarification question over completing an assumed system model;
- section headings do not weaken traceability: content placed under `Functional Requirements`, `Dependencies`, `Business Rules`, or equivalent sections must still be individually source-grounded or explicitly classified as non-confirmed;
- before delivering an artifact, re-check every statement presented as confirmed/required against the authoritative input and downgrade or remove unsupported statements.

## Assumption Propagation and Expected Results

For scenario design, testcase generation, API tests, SQL validation, regression analysis, coverage review, and any artifact that contains expected behavior:

- **Unresolved assumptions and unknowns must not become authoritative expected results by default.** Labeling a behavior as an assumption does not make it valid to assert as an executable expected result;
- use confirmed requirements, confirmed business rules, and source-supported behavioral implications as the default basis for executable expected results;
- apply source grounding to the **entire executable testcase**, not only its Expected Result. Preconditions, test data, actions/steps, intermediate assertions, and final assertions must not require an unconfirmed behavior or implementation detail;
- if the source does not define how a state is observed, keep the assertion at the source's abstraction level and record observability as a clarification/execution dependency rather than inventing a signal;
- if a candidate test depends on unresolved behavior, place it under `Clarification-Dependent`, `Blocked`, `Candidate`, `Pending Confirmation`, or equivalent status instead of presenting it as an executable passing test;
- only generate assumption-based executable tests when the user explicitly authorizes assumption-based design or provides the assumption as accepted project context;
- do not claim `complete`, `full`, or equivalent coverage when unresolved clarification-dependent behavior remains outside executable coverage;
- a test setup/precondition must follow the same grounding rule as its expected result;
- dependencies must be source-grounded;
- before finalizing test artifacts, perform an assumption-propagation check over every testcase field.

Default propagation model:

```text
Confirmed authoritative behavior
        ↓
Grounded executable step + expected result

Unknown / unresolved assumption
        ↓
Analysis or candidate coverage
        ↓
Clarification-dependent / blocked test
        ↓
NOT an authoritative executable assertion
```

## Capability Routing

Route requirement analysis, rule extraction, risk analysis, scenario generation, testcase generation, test-data design, coverage review, regression impact, bug review, API test design, and SQL validation to the corresponding canonical skill under `skills/`.

For coordinated multi-artifact work, follow the applicable canonical workflow under `workflows/`.

## Canonical Output Discipline

Canonical templates are mandatory contracts, not optional examples.

- Coverage Review must apply `Covered`, `Weakly Covered`, `Gap`, and `Blocked` according to `skills/coverage-reviewer/README.md`. A broad/implicit reference is not automatically sufficient for `Covered`, and clarification-dependent behavior without an authoritative oracle is `Blocked`, not a false `Gap`.
- Test Cases must follow `shared/templates/TestCase.md`: the executable `TC-*` inventory is one canonical Markdown table under `## Test Cases`; do not render section-per-testcase blocks or separate per-testcase steps tables.
- Regression Analysis must follow `shared/templates/Regression.md` and distinguish `Minimum / Release-Gate Regression`, `Recommended Regression`, and `Full Changed-Feature Verification` when existing confirmed coverage is available. Do not choose scope tiers by target percentages/counts.
- Every reported total, subtotal, percentage, ID range, coverage count, and regression-tier count must reconcile with actual unique generated/referenced IDs before delivery.
- A canonical-format or aggregate-count mismatch is a validation failure and must be corrected before reporting PASS.

## Working Rules

- preserve artifact boundaries;
- distinguish confirmed, derived, assumed, potential, and unknown information;
- preserve traceability;
- use specialized API/SQL capabilities for technical design;
- do not silently convert optional feedback paths into hard dependencies;
- run applicable deterministic validators under `scripts/` when repository changes are made;
- review changes before commit and do not modify frozen canonical semantics without explicit scope;
- before delivery, validate mandatory template representation and reconcile reported aggregate counts with actual canonical IDs/rows.
