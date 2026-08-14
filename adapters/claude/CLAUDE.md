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
- a stated duration or threshold does not authorize inventing an unspecified post-condition or mechanism. For example, a requirement that something is locked "for 30 minutes" does not by itself establish how unlocking occurs or when that change becomes observable;
- when the source is minimal, prefer an explicit gap or clarification question over completing an assumed system model;
- section headings do not weaken traceability: content placed under `Functional Requirements`, `Dependencies`, `Business Rules`, or equivalent sections must still be individually source-grounded or explicitly classified as non-confirmed;
- before delivering an artifact, re-check every statement presented as confirmed/required against the authoritative input and downgrade or remove unsupported statements.

## Assumption Propagation and Expected Results

For scenario design, testcase generation, API tests, SQL validation, regression analysis, coverage review, and any artifact that contains expected behavior:

- **Unresolved assumptions and unknowns must not become authoritative expected results by default.** Labeling a behavior as an assumption does not make it valid to assert as an executable expected result;
- use confirmed requirements, confirmed business rules, and source-supported behavioral implications as the default basis for executable expected results;
- apply source grounding to the **entire executable testcase**, not only its Expected Result. Preconditions, test data, actions/steps, intermediate assertions, and final assertions must not require an unconfirmed behavior or implementation detail;
- do not add a successful-login step merely to prove that a lockout threshold has not been reached unless successful-login behavior is authoritative context. For a threshold such as 5 consecutive failures, the grounded lower-boundary assertion is only that the lockout trigger has not been reached after 4 consecutive failures;
- if the source does not define how a state is observed, keep the assertion at the source's abstraction level (for example, `the account enters the locked state`) and explicitly record observability as a clarification/execution dependency rather than inventing a login response, message, API status, database field, or other signal;
- if a candidate test depends on unresolved behavior, place it under `Clarification-Dependent`, `Blocked`, `Candidate`, `Pending Confirmation`, or equivalent status instead of presenting it as an executable passing test;
- only generate assumption-based executable tests when the user explicitly authorizes assumption-based design or provides the assumption as accepted project context. In that case, identify the assumption at testcase level and clearly state that the expected result is conditional on it;
- do not claim `complete`, `full`, or equivalent coverage when unresolved clarification-dependent behavior remains outside executable coverage;
- do not infer that a locked state rejects every login action, that successful login resets a counter, that a duration expiry automatically unlocks an account, or any similar observable behavior unless authoritative input establishes it;
- a test setup/precondition must follow the same grounding rule as its expected result. Do not require a failed-attempt counter to be set to zero, hidden storage state, modules, APIs, timers, or other implementation controls unless they are confirmed or explicitly supplied as test-environment capabilities. Prefer externally expressible setup such as using an account for which the relevant test sequence has not yet been performed, while marking any required reset capability as an execution dependency if it is not authoritative;
- dependencies must be source-grounded. Do not list an inferred module, service, database, counter, timer, or other implementation component as a dependency merely because it would be a plausible implementation;
- before finalizing test artifacts, perform an assumption-propagation check over **every testcase field**: for each precondition, test-data item, action, and expected result, ask whether it relies on unconfirmed project behavior. If yes, remove/rephrase it to the confirmed abstraction level or move the case to clarification-dependent coverage.

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

## Working Rules

- preserve artifact boundaries;
- distinguish confirmed, derived, assumed, potential, and unknown information;
- preserve traceability;
- use specialized API/SQL capabilities for technical design;
- do not silently convert optional feedback paths into hard dependencies;
- run applicable deterministic validators under `scripts/` when repository changes are made;
- review changes before commit and do not modify frozen canonical semantics without explicit scope.
