# Workspace Standard

> Version: 1.2.0  
> Status: Draft  
> Last Updated: 2026-08-21

## Purpose

The `Workspace` standard defines the canonical project workspace, identity, provenance, revision, artifact-lifecycle, dependency, freshness, and archive rules used to manage operational QA-AI project artifacts.

It governs workspace placement and artifact management only. It does not redefine canonical QA skills, workflow semantics, artifact content contracts, execution semantics, export semantics, or regression-analysis semantics. Derived export semantics are owned by `shared/standards/Export.md`; execution semantics are owned by `shared/standards/Execution.md`.

---

## Canonical Workspace Structure

```text
workspace/
├── README.md
├── projects/
│   └── <project-id>/
│       ├── README.md
│       └── features/
│           └── <feature-id>/
│               ├── README.md
│               ├── metadata.json
│               ├── source/
│               │   ├── requirements/
│               │   └── supporting/
│               ├── artifacts/
│               ├── exports/
│               │   └── generic/
│               ├── executions/
│               │   └── RUN-*/
│               ├── revisions/
│               └── archive/
└── current/
    └── README.md
```

`workspace/projects/<project-id>/features/<feature-id>/` is the canonical project/feature source of truth. `workspace/current/` is an optional working convenience layer and MUST NOT become the authoritative long-term artifact store.

`artifacts/` contains canonical QA-AI artifacts. `exports/` contains derived operational representations. `executions/` contains Phase 18 structured execution evidence governed by `Execution.md`. An export MUST NOT become a canonical artifact baseline merely because it is edited, executed, or imported elsewhere.

---

## Identity Model

A project uses a stable `project_id`; a feature uses a stable `feature_id` within its project. Renaming a display name MUST NOT silently change the stable identity.

Each registered source uses a stable `source_id`, for example `SRC-001`, and records source type, workspace-relative path, authoritative flag, revision when known, checksum when deterministic bytes are available, and registration timestamp.

A source keeps the same `source_id` when a new revision replaces the content at the same canonical source type/path. The working metadata is updated to the new revision/checksum while the prior revision snapshot preserves the earlier metadata. A changed checksum MUST NOT by itself create a new source identity. A new `source_id` is reserved for a distinct canonical source path/type.

This stable identity allows dependencies such as `required,source:SRC-001` to remain valid across feature revisions while Change Intelligence compares the source checksum recorded in the immutable base snapshot with the checksum in the current working revision.

An artifact is a whole QA document such as `Test-Cases.md`. Record-level IDs such as `BR-*`, `SC-*`, and `TC-*` remain owned by their artifact contracts and MUST NOT be replaced by workspace artifact IDs.

Execution-run identities (`RUN-*`) and execution-result identities (`ER-*`) are owned by `Execution.md` and are not artifact lifecycle IDs.

---

## Feature Metadata

Each feature workspace MUST contain `metadata.json` conforming to `shared/schemas/workspace-metadata.schema.json`.

Feature metadata owns project/feature identity, operational status, current feature revision, framework provenance, source registrations, artifact registrations, dependency relationships, lifecycle/freshness state, and timestamps. It MUST NOT duplicate full QA artifact or execution content.

Derived export provenance is maintained by export sidecars defined by `Export.md`. Execution provenance is maintained within each `executions/RUN-*/execution.json` record defined by `Execution.md`.

---

## Feature Revision Model

A feature revision represents an authoritative product-input baseline, not an arbitrary output-document edit.

Recommended identifiers use `REV-001`, `REV-002`, and so on.

When a new authoritative source baseline replaces the previous one:

1. snapshot the prior canonical baseline as historical evidence;
2. advance the current feature revision;
3. update the stable source registration with the new source revision/checksum;
4. mark prior-baseline downstream artifacts stale according to dependency rules;
5. run change analysis between the immutable base snapshot and the current working target revision;
6. do not silently overwrite historical evidence.

The target revision does not need to be snapshotted before Change Intelligence runs. While it remains the `current_revision`, working `metadata.json`, source registrations, and current artifact files form the target-side deterministic inventory. Once a revision itself becomes historical, its snapshot is the authoritative comparison evidence.

Historical revision metadata MUST conform to `shared/schemas/revision-metadata.schema.json`.

Derived exports MAY be regenerated from preserved canonical artifacts and are not required historical canonical snapshots. Execution evidence preserves the feature/testcase provenance that was actually executed and MUST NOT be silently rewritten when the feature advances.

---

## Artifact Lifecycle

Canonical artifact lifecycle states are:

```text
Draft → Review → Approved → Superseded → Archived
```

AI generation or self-review MUST NOT automatically promote an artifact to `Approved`. Human review or an explicitly authorized approval mechanism is required.

Execution runs do not use this artifact lifecycle; they use the run lifecycle defined in `Execution.md`.

---

## Freshness Model

Artifact freshness is independent from lifecycle:

```text
Current
Stale
Unknown
```

An artifact may therefore be `Approved` and `Stale` simultaneously. Freshness MUST NOT be encoded as an artifact lifecycle status.

Execution run creation must respect the testcase freshness guard defined by `Execution.md`; an execution override does not change the artifact freshness value.

---

## Dependency and Staleness Model

Workspace dependencies use `required`, `supporting`, and `conditional` relationships. Required source/upstream revision changes can mark downstream artifacts `Stale`; supporting/conditional relationships do not become hard dependencies unless the recorded baseline establishes that condition.

Staleness detection MUST NOT automatically regenerate or approve downstream artifacts:

```text
Detect → Report → Human/Workflow Decision → Regenerate or Revalidate
```

Advanced semantic change intelligence belongs to the later change-intelligence phase.

---

## Approved Baseline Preservation

An approved current baseline MUST NOT be destructively overwritten when a new feature revision is introduced. Preserve historical evidence under `revisions/<revision-id>/` or the approved archive mechanism.

Execution history under `executions/` is operational evidence and must retain the actual testcase checksum/revision used by the run.

---

## Provenance

Where available, workspace metadata SHOULD preserve framework Git revision, platform/runtime, artifact revision, source revision/fingerprint, timestamps, and human review/approval evidence. Unknown provenance MUST remain explicit rather than reconstructed.

Export provenance is recorded separately in `<export>.export.json`. Execution provenance is recorded separately in each execution run.

---

## Validation Requirements

Workspace validation MUST detect at least invalid/missing required workspace directories, malformed metadata, invalid lifecycle/freshness values, duplicate source/artifact identities, broken registered paths, broken dependencies, invalid dependency types, revision inconsistencies, and stale required baselines when deterministic evidence exists.

Export validation is performed separately by `scripts/export/validate_export.py`; execution validation is performed separately by `scripts/execution/validate_execution.py`. A valid workspace does not imply a valid export or execution run.

---

## Out of Scope

This standard does not define:

- spreadsheet/CSV field mapping semantics (owned by `Export.md`);
- test execution statuses/results/retest semantics (owned by `Execution.md`);
- external defect lifecycle;
- automatic requirement-diff interpretation;
- automated regression recommendation;
- CI/CD orchestration;
- Jira/TestRail/AIO API synchronization;
- autonomous regeneration or approval.

---

## Related Resources

- `shared/standards/Export.md`
- `shared/standards/Execution.md`
- `shared/schemas/workspace-metadata.schema.json`
- `shared/schemas/revision-metadata.schema.json`
- `shared/schemas/export-metadata.schema.json`
- `shared/schemas/execution-run.schema.json`
- `shared/schemas/execution-results.schema.json`
- `shared/schemas/execution-defects.schema.json`
- `scripts/workspace/`
- `scripts/export/`
- `scripts/execution/`
- `workspace/README.md`
