# How To Use

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-14

---

# 1. Purpose

## Overview

This document explains how end users consume the QA-AI framework after the Phase 13 baseline.

It covers repository navigation, capability selection, workflow execution, shared knowledge usage, and the supported ChatGPT, Claude, and Cursor integration paths.

QA-AI is platform-independent at its core. Platform adapters package the canonical framework for a runtime; they do not redefine QA behavior.

## Objectives

This guide aims to:

- Help users start from the correct framework entry points.
- Route QA requests to the owning skill or canonical workflow.
- Reuse relevant standards, templates, checklists, and knowledge without loading unrelated context.
- Preserve source grounding and traceability.
- Explain the supported platform-adapter baseline.
- Reduce onboarding and integration mistakes.

---

# 2. Who Should Use This Guide?

This guide is intended for:

- QA Engineers
- Test Analysts
- Test Leads
- Automation Engineers
- AI-assisted QA users
- Contributors consuming existing QA-AI capabilities

---

# 3. Before You Begin

Start with:

1. `README.md` — repository overview and current baseline.
2. `FRAMEWORK.md` — canonical framework operating model.
3. `docs/01-Architecture.md` — architecture details.
4. `docs/02-Core-Concepts.md` — framework concepts.
5. `skills/README.md` and `workflows/README.md` — canonical capability and orchestration inventories.

For platform-specific use, also read `adapters/README.md` and the README under the selected adapter.

---

# 4. Repository Overview

```text
qa-ai/
├── FRAMEWORK.md
├── manifest.json
├── shared/
├── skills/
├── workflows/
├── adapters/
├── docs/
├── examples/
├── datasets/
├── scripts/
└── output/
```

The core QA semantics live in `FRAMEWORK.md`, `skills/`, `workflows/`, and `shared/`.

`adapters/` exposes that canonical behavior to supported AI runtimes. `datasets/`, `scripts/`, and `examples/` support development, evaluation, validation, and usage; they do not redefine skill ownership.

---

# 5. Source Priority

When sources differ or context is incomplete, use this precedence:

```text
Authoritative project requirement / user-provided project context
        ↓
Applicable canonical workflow
        ↓
Owning canonical skill
        ↓
Applicable shared standards / templates / checklists / knowledge
        ↓
Generic model knowledge
```

Do not invent project-specific rules, thresholds, roles, schemas, endpoints, status values, dependencies, or expected results to fill missing information.

Keep confirmed, derived, assumed, potential, and unknown information distinguishable.

---

# 6. Choose the Execution Mode

## 6.1 Single-Capability Request

When the user asks for one QA artifact or objective, route to the owning skill.

| QA Objective | Canonical Skill |
|---|---|
| Requirement understanding | `requirement-analyzer` |
| Business-rule extraction | `business-rule-extractor` |
| Risk analysis | `risk-analyzer` |
| Test-scenario generation | `scenario-generator` |
| Executable test cases | `testcase-generator` |
| Test data | `test-data-generator` |
| Coverage review | `coverage-reviewer` |
| Regression impact | `regression-impact` |
| Bug-report review | `bug-report-reviewer` |
| API-specific test design | `api-test-generator` |
| SQL/database validation | `sql-validation` |

Read the owning `skills/<skill>/README.md` before execution. Do not merge ownership merely because one request mentions several artifact types.

## 6.2 Coordinated Multi-Artifact Request

When the requested outcome requires multiple dependent capabilities, use the applicable canonical workflow rather than inventing a skill sequence.

Current canonical workflows include:

- `testcase-generation`
- `testcase-quality-review`
- `regression-analysis`

Read `workflows/<workflow>/README.md`, preserve its stage order, reuse valid upstream artifacts, and do not silently skip required dependencies.

---

# 7. Canonical Testcase-Generation Example

For a request to transform requirement information into scenarios and executable test cases, use `workflows/testcase-generation`:

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

Risk analysis and coverage review are not implicit stages of this workflow. Run them only when requested or when another canonical workflow/capability owns that objective.

Unknown behavior must remain visible. Do not convert clarification-dependent behavior into executable expected results.

---

# 8. Using Shared Resources

Skills may depend on relevant resources under `shared/`:

- `shared/standards/` — documentation and output conventions.
- `shared/templates/` — canonical artifact structures.
- `shared/checklists/` — review criteria.
- `shared/prompt-patterns/` — reusable reasoning/instruction patterns.
- `shared/knowledge/` — reusable QA knowledge.
- `shared/glossary/` — terminology.

Load only the resources relevant to the selected skill/workflow. Generic knowledge must not override authoritative project behavior.

---

# 9. Using Platform Adapters

The Phase 13 baseline supports three adapters.

| Platform | Supported Mechanism | Baseline State |
|---|---|---|
| ChatGPT | Custom GPT Instructions + bounded Knowledge bundles | Frozen |
| Claude | Claude Code repository-root `CLAUDE.md` + repository references | Frozen |
| Cursor | Repository-root `.cursor/rules/*.mdc` + `.cursor/commands/*.md` | Frozen |

All three passed platform-specific runtime smoke validation and final cross-platform review.

## 9.1 ChatGPT

Use `adapters/chatgpt/` for Custom GPT instructions, Knowledge-bundle preparation, mappings, usage guidance, and validation.

ChatGPT consumes prepared/uploaded framework context and does not require direct repository access for the Phase 13 baseline.

## 9.2 Claude

Use `adapters/claude/` for the Claude Code integration package and instructions.

The supported Phase 13 installation model places the adapter's runtime `CLAUDE.md` at the QA-AI repository root so canonical repository paths can be resolved.

## 9.3 Cursor

Use `adapters/cursor/` for Cursor rules, commands, mappings, and usage guidance.

The supported Phase 13 installation model places the packaged `.cursor/` directory at the QA-AI repository root so the rules and commands can reference canonical QA-AI paths.

For exact installation steps and platform limitations, follow the selected adapter's `README.md` and `Usage.md` rather than duplicating those details here.

---

# 10. Specialized API and Database Work

Do not turn generic functional test cases into invented API or SQL tests.

For API-specific test design, use `api-test-generator` and provide an authoritative API source such as an API contract, endpoint requirement, or equivalent interface description with sufficient behavior.

If endpoint, method, schema, status/error behavior, or authentication semantics are missing, report the gap instead of fabricating the interface.

For SQL/database validation, use `sql-validation` and rely on authoritative schema/query/database context. Do not invent tables, columns, relationships, or persistence behavior.

---

# 11. Reviewing Outputs

After execution:

- Verify source grounding and factual accuracy.
- Check traceability across dependent artifacts.
- Confirm assumptions and unknowns remain explicit.
- Review against applicable shared checklists.
- Verify output structure against the applicable template.
- Confirm that the selected skill/workflow stayed within its ownership boundary.

Generated QA artifacts require human review before project use, especially when requirements are ambiguous, incomplete, or high risk.

---

# 12. Validation and Repository Changes

When modifying QA-AI repository artifacts, use the deterministic validators under `scripts/` where applicable.

Examples include adapter validation, roadmap/progress validation, workflow validation, knowledge validation, and other script groups defined by the repository.

Do not treat generated or runtime installation copies as canonical sources when an owning repository artifact already exists.

---

# 13. Common Mistakes

Avoid:

- Treating generic model knowledge as authoritative project behavior.
- Inventing missing rules or implementation details to make an artifact look complete.
- Using the wrong skill for the requested artifact.
- Improvising a multi-stage sequence when a canonical workflow exists.
- Re-running upstream skills when valid upstream artifacts can be reused.
- Treating optional feedback loops as mandatory workflow cycles.
- Duplicating specialized API/SQL behavior inside generic test-generation capabilities.
- Copying adapter runtime files into unsupported locations without the canonical QA-AI path contract.
- Assuming AI-generated output is automatically project-approved.

---

# 14. Frequently Asked Questions

## Where should I start?

Start with `README.md` and `FRAMEWORK.md`, then read the owning skill/workflow for the task you want to perform.

## Can I create my own Skill?

Yes. Follow `docs/05-Skill-Development-Guide.md`. New skills should have distinct ownership and must not duplicate an existing canonical capability.

## How do I add Knowledge?

Follow `docs/06-Knowledge-Management.md` and the applicable knowledge standards.

## How do I build a Workflow?

Follow `docs/08-Workflow-Design.md`. A workflow should orchestrate existing capabilities rather than duplicate skill logic.

## How do I contribute?

Follow `docs/09-Contribution.md`.

## Which platform should I use?

Choose the runtime that fits your environment. ChatGPT, Claude, and Cursor are all supported by the frozen Phase 13 adapter baseline; the canonical QA behavior remains the same across them.

---

# 15. Troubleshooting

If results appear inconsistent:

1. Confirm the authoritative project input.
2. Confirm the owning skill or workflow.
3. Check that required upstream artifacts are available.
4. Check that the runtime loaded only the relevant canonical QA-AI sources.
5. Verify adapter installation/location for the selected platform.
6. Run applicable deterministic validators after repository changes.
7. Re-check unresolved assumptions or missing project information before changing expected results.

---

# 16. References

- `README.md`
- `FRAMEWORK.md`
- `manifest.json`
- `skills/README.md`
- `workflows/README.md`
- `adapters/README.md`
- `docs/01-Architecture.md`
- `docs/02-Core-Concepts.md`
- `docs/05-Skill-Development-Guide.md`
- `docs/06-Knowledge-Management.md`
- `docs/08-Workflow-Design.md`
- `docs/09-Contribution.md`
- `docs/11-Roadmap.md`
