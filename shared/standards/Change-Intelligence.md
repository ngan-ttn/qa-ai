# Change Intelligence Standard

> Version: 1.0.0
> Status: Draft
> Last Updated: 2026-08-19

## Purpose

Define deterministic revision-delta, impact-propagation, and incremental-QA semantics for QA-AI without automatically regenerating, approving, or executing QA artifacts.

## Boundary

Change Intelligence answers: **what changed, what supported QA assets are affected, why, and what QA action is justified next**.

It does not replace artifact freshness, regression-impact analysis, artifact generation, human approval, or test execution.

## Canonical Change Classification

Every compared item MUST use one of:

- `Added` — present only in the target revision.
- `Modified` — present in both revisions but QA-relevant normalized content differs.
- `Removed` — present only in the base revision.
- `Unchanged` — equivalent normalized content exists in both revisions.
- `Unknown` — deterministic comparison cannot establish semantic equivalence or change safely.

Textual difference alone MUST NOT be promoted into a confirmed business-behavior change. Formatting-only normalization may be reported as `Unchanged` when the deterministic normalization rule explains why.

## Impact Classification

Impact records use:

- `Direct` — changed source/artifact is itself the affected item.
- `Dependency` — a registered dependency path connects the changed item to the affected artifact.
- `Potential` — evidence suggests possible impact but the registered model cannot prove it.
- `Unknown` — impact cannot be resolved from available evidence.

Unsupported implementation coupling MUST NOT be invented.

## Incremental QA Actions

Each affected or evaluated asset receives exactly one recommended action:

- `Reuse` — no supported change impact requires QA work.
- `Review` — evidence indicates human review is required before deciding regeneration/revalidation.
- `Regenerate` — upstream confirmed change invalidates generated content owned by its generator.
- `Revalidate` — artifact content may remain usable but its correctness/freshness must be re-established.
- `Re-execute` — existing executable coverage remains valid but confirmed change justifies execution again.
- `Blocked` — authoritative change meaning, oracle, source, or dependency is unresolved.

The recommendation is a plan only. It MUST NOT perform the action.

## Evidence and Traceability

Every non-`Reuse` recommendation MUST include:

1. a change ID;
2. affected asset key/path;
3. supported relationship or dependency path;
4. reason;
5. evidence reference.

`Potential` and `Unknown` impacts cannot silently produce authoritative `Regenerate` or `Re-execute` actions. They normally produce `Review` or `Blocked` unless stronger evidence is supplied.

## Revision Placement

Change-intelligence evidence belongs under the target revision:

```text
revisions/<REV-N>/change-intelligence/
├── change-set.json
├── impact-analysis.json
├── incremental-plan.json
└── Change-Impact.md
```

These files are revision evidence, not canonical QA artifacts.

## Reconciliation

Reported totals MUST reconcile with actual unique IDs/records. An affected artifact may have multiple impact records, but the incremental plan MUST contain one final recommended action per artifact key.

## Relationship to Freshness

Phase 16 freshness remains authoritative workspace state. Phase 19 may explain and recommend a narrower action but MUST NOT silently mark an artifact `Current`, regenerate it, approve it, or override deterministic stale propagation.

## Relationship to Regression and Execution

Change Intelligence identifies supported affected coverage and recommends whether regression analysis/re-execution should occur. Regression Analysis still owns regression scope selection. Execution lifecycle still owns actual results and retests.

## Validation Rules

Validation MUST fail when:

- IDs are duplicated or referenced IDs do not exist;
- revision IDs are malformed or base equals target;
- plan actions are outside the canonical set;
- non-Reuse actions lack evidence/reason;
- an artifact receives multiple final plan actions;
- impact references an unknown change or artifact;
- reported counts do not reconcile;
- `Unknown` change is promoted into an unsupported authoritative action.
