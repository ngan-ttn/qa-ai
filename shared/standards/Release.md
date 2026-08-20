# QA-AI Release Standard

> Version: 1.0.0
> Status: Draft
> Last Updated: 2026-08-20

## Purpose

Define the canonical QA-AI system-release contract. A release is a reproducible repository baseline plus validation evidence; it does not replace the canonical repository, artifact lifecycle, workspace state, regression analysis, execution history, or change-intelligence evidence.

## Release Lifecycle

`Draft → Candidate → Validated → Released → Superseded`

- **Draft** — release metadata is being assembled.
- **Candidate** — scope and repository revision are fixed for validation.
- **Validated** — all mandatory release gates passed for that exact revision.
- **Released** — explicit human release approval was recorded after validation.
- **Superseded** — a later released baseline replaces this release.

No state transition may imply artifact approval or execution success.

## Release Identity

Every release MUST record a unique `release_id`, semantic `version`, lifecycle `status`, repository revision, generation timestamp, capability inventory, validation requirements, and release evidence references.

## Canonical Authority

`release/manifest.json` is a release snapshot, not the source of truth for framework semantics. Counts and capability flags MUST be derived from or reconciled with canonical repository state. Existing Phase 16–19 evidence MUST remain immutable.

## Readiness Rule

Release readiness is fail-closed. Every mandatory validator must PASS. Partial success MUST NOT be reported as release readiness PASS. A skipped mandatory gate is a failure unless the release contract explicitly marks it not applicable with human-approved evidence.

## Evidence Freshness

Validation evidence is valid only for the repository revision recorded in the report. Any repository change after validation requires a new validation run before `Released` may be asserted.

## Human Authority

Automation may build a manifest, run validators, and generate reports. Only an explicit human decision may promote a validated candidate to `Released`.

## Boundary

Phase 20 orchestrates and verifies existing capabilities. It MUST NOT generate or approve QA artifacts, mutate freshness, select regression tiers, execute testcases, modify execution results, infer missing requirements, or introduce autonomous/self-learning behavior.
