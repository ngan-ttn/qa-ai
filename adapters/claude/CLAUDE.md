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

- classify an item as **Confirmed** only when the authoritative project input directly states or necessarily entails it;
- do not promote a plausible inference into a functional requirement, dependency, business rule, expected result, or system fact merely because it would be a common implementation;
- keep derived observations and assumptions explicitly separate from confirmed requirements, and include them only when they materially help the requested artifact;
- implementation mechanisms such as counters, persistence/storage, timestamps, database fields, services/modules, server-side enforcement, API behavior, and architectural dependencies remain unknown unless authoritative project context establishes them;
- a stated duration or threshold does not authorize inventing an unspecified post-condition or mechanism. For example, a requirement that something is locked "for 30 minutes" does not by itself establish how unlocking occurs or when that change becomes observable;
- when the source is minimal, prefer an explicit gap or clarification question over completing an assumed system model;
- section headings do not weaken traceability: content placed under `Functional Requirements`, `Dependencies`, `Business Rules`, or equivalent sections must still be individually source-grounded or explicitly classified as non-confirmed;
- before delivering an artifact, re-check every statement presented as confirmed/required against the authoritative input and downgrade or remove unsupported statements.

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
