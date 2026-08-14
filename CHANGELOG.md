# Changelog

All notable changes to the QA-AI framework are documented in this file.

The project is currently under active development. The current repository version remains `1.0.0`; roadmap phase completion does not by itself create a new release version.

---

## [Unreleased] - 2026-08-14

### Added

- Completed the canonical QA knowledge library with 181 frozen articles across testing techniques, QA, API, database, and domain knowledge.
- Expanded the canonical skill library to 11 skills, including risk analysis, bug-report review, API test design, SQL validation, and test-data generation.
- Implemented the scripts foundation with 25 scripts across 8 groups for validation, knowledge, prompts, workflows, evaluation, export, utilities, and roadmap automation.
- Added platform adapters for ChatGPT, Claude, and Cursor.
- Added platform-specific runtime instructions, mappings, installation guidance, and validation assets for the supported adapter baseline.

### Changed

- Completed repository alignment and canonical ownership review across skills, workflows, knowledge, scripts, and adapters.
- Standardized regression ownership on `regression-impact`; `regression-analyzer` remains intentionally excluded to avoid overlapping canonical ownership.
- Validated source-priority, capability-routing, workflow orchestration, missing-input handling, and no-fabrication behavior across supported platform adapters.
- Synchronized repository roadmap/status surfaces through the Phase 13 frozen baseline.
- Updated the root README to describe the implemented Phase 13 repository state rather than earlier planned scope.

### Validation

- Phase 10 — Knowledge Library Completion: Frozen (`181/181` articles).
- Phase 11 — Skill Library Expansion: Frozen (`5/5` expansion skills; `11` canonical skills total).
- Phase 12 — Scripts Implementation: Frozen (`8/8` script groups; `25` scripts total).
- Phase 13 — Platform Integration: Frozen (`3/3` adapters).
- ChatGPT, Claude, and Cursor passed platform-specific runtime smoke validation and final cross-platform review.

### Framework Status

- Phase 1 — Framework Foundation: Completed
- Phase 2 — Shared Standards and Foundations: Completed
- Phase 3 — Workflow Library: Completed
- Phase 4 — Skill Library Foundation: Completed
- Phase 5 — Knowledge Foundation: Completed
- Phase 6 — Examples and End-to-End Validation: Completed
- Phase 7 — Framework Integration and Validation: Completed
- Phase 8 — Datasets and Evaluation: Frozen
- Phase 9 — Repository Completion and Alignment: Completed
- Phase 10 — Knowledge Library Completion: Frozen
- Phase 11 — Skill Library Expansion: Frozen
- Phase 12 — Scripts Implementation: Frozen
- Phase 13 — Platform Integration: Frozen

### Notes

- No Phase 14 scope is defined by this alignment entry.
- `VERSION` and `manifest.json` remain at `1.0.0`; a future version change should be made through an explicit release/versioning decision.

---

## [1.0.0] - 2026-08-12

### Added

- Established the QA-AI framework architecture and core concepts.
- Added shared standards, templates, checklists, prompt patterns, and glossaries.
- Added the initial reusable QA skill library.
- Added reusable QA workflow definitions.
- Established the QA knowledge-library architecture and testing-technique knowledge base.
- Added standalone and end-to-end QA examples.
- Added controlled requirement datasets and golden reference outputs.
- Added artifact-quality evaluation criteria, rubrics, and scoring definitions.
- Added baseline, cross-platform, and regression benchmark definitions.
- Added reusable API, database, UI, and domain fixture models.

### Changed

- Synchronized the implementation roadmap with the repository state available at the time.
- Updated the root README to reflect the framework architecture and implementation status available at the time.

### Framework Status At Baseline Creation

- Phase 1 — Framework Foundation: Completed
- Phase 2 — Shared Standards and Foundations: Completed
- Phase 3 — Workflow Library: Completed
- Phase 4 — Skill Library Foundation: Completed
- Phase 5 — Knowledge Foundation: Completed
- Phase 6 — Examples and End-to-End Validation: Completed
- Phase 7 — Framework Integration and Validation: Completed
- Phase 8 — Datasets and Evaluation: Frozen
- Phase 9 — Repository Completion and Alignment: In Progress

### Notes

This entry establishes the initial repository-level changelog baseline.

Earlier framework development was performed incrementally before repository-level changelog tracking was introduced. The entries above summarize the framework state represented by version `1.0.0` rather than reconstructing undocumented historical releases.