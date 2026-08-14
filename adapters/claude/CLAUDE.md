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

Never invent project-specific behavior, thresholds, schemas, dependencies, roles, status values, or expected results when authoritative context is absent.

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
