# Workspace Standard

> Version: 1.0.0  
> Status: Draft  
> Last Updated: 2026-08-18

## Purpose

The `Workspace` standard defines the canonical project workspace, identity, provenance, revision, artifact-lifecycle, dependency, freshness, and archive rules used to manage operational QA-AI project artifacts.

It governs project artifact management only. It does not redefine canonical QA skills, workflow semantics, artifact content contracts, test execution, export semantics, or regression-analysis semantics. Derived export semantics are owned by `shared/standards/Export.md`.

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
│               ├── revisions/
│               └── archive/
└── current/
    └── README.md
```

`workspace/projects/<project-id>/features/<feature-id>/` is the canonical project/feature source of truth. `workspace/current/` is an optional working convenience layer and MUST NOT become the authoritative long-term artifact store.

`artifacts/` contains canonical QA-AI artifacts. `exports/` contains derived operational representations. An export MUST NOT become a canonical artifact baseline merely because it is edited, executed, or imported elsewhere.

---

## Identity Model

A project uses a stable `project_id`; a feature uses a stable `feature_id` within its project. Renaming a display name MUST NOT silently change the stable identity.

Each registered source uses a stable `source_id`, for example `SRC-001`, and records source type, workspace-relative path, authoritative flag, revision when known, checksum when deterministic bytes are available, and registration timestamp.

An artifact is a whole QA document such as `Test-Cases.md`. Record-level IDs such as `BR-*`, `SC-*`, and `TC-*` remain owned by their artifact contracts and MUST NOT be replaced by workspace artifact IDs.

---

## Feature Metadata

Each feature workspace MUST contain `metadata.json` conforming to `shared/schemas/workspace-metadata.schema.json`.

Feature metadata owns project/feature identity, operational status, current feature revision, framework provenance, source registrations, artifact registrations, dependency relationships, lifecycle/freshness state, and timestamps. It MUST NOT duplicate full QA artifact content.

Derived export provenance is maintained by export sidecars defined by `shared/standards/Export.md`; it does not replace feature metadata.

---

## Feature Revision Model

A feature revision represents an authoritative product-input baseline, not an arbitrary output-document edit.

Recommended identifiers use `REV-001`, `REV-002`, and so on.

When a new authoritative source baseline replaces the previous one:

1. preserve the prior approved baseline as historical evidence;
2. advance the current feature revision;
3. register the new/changed authoritative source;
4. mark affected downstream artifacts stale according to dependency rules;
5. do not silently overwrite historical evidence.

Historical revision metadata MUST conform to `shared/schemas/revision-metadata.schema.json`.

Derived exports MAY be regenerated from preserved canonical artifacts and are not required historical canonical snapshots.

---

## Artifact Lifecycle

Canonical artifact lifecycle states are:

```text
Draft → Review → Approved → Superseded → Archived
```

| Status | Meaning |
|---|---|
| `Draft` | Artifact is being generated or edited and is not an approved downstream baseline. |
| `Review` | Artifact is awaiting or undergoing human review. |
| `Approved` | Artifact is accepted as a valid downstream baseline for the registered revision. |
| `Superseded` | A newer approved artifact/revision has replaced it as the active baseline. |
| `Archived` | Artifact is retained as historical evidence and is no longer active. |

AI generation or self-review MUST NOT automatically promote an artifact to `Approved`. Human review or an explicitly authorized approval mechanism is required.

Valid baseline transitions are `Draft → Review`, `Review → Draft`, `Review → Approved`, `Approved → Superseded`, and `Superseded → Archived`. Direct transitions outside this lifecycle require explicit maintenance justification.

Derived exports do not use this lifecycle; their freshness is checksum-based under `Export.md`.

---

## Freshness Model

Artifact freshness is independent from lifecycle:

```text
Current
Stale
Unknown
```

An artifact may therefore be `Approved` and `Stale` simultaneously. Freshness MUST NOT be encoded as an artifact lifecycle status.

`Current` means registered upstream/source revisions match; `Stale` means a dependency revision/source fingerprint no longer matches; `Unknown` means available metadata cannot determine freshness.

---

## Dependency Model

Workspace dependencies use three relationship types:

| Type | Meaning |
|---|---|
| `required` | The downstream artifact requires the registered upstream baseline to remain valid; a changed upstream revision marks it stale. |
| `supporting` | The upstream artifact provides evidence/context but is not automatically invalidating; a change creates a review condition. |
| `conditional` | The dependency applies only when the associated workflow/gate/feature condition was used. |

The workspace dependency graph MUST NOT redefine canonical workflow order or convert optional feedback paths into hard dependencies. Metadata MUST represent relationships actually used for an artifact rather than generic presumed dependencies.

Typical relationships may include Requirement Analysis from authoritative requirement source; Business Rules from Requirement Analysis; Scenario/Test Case/Coverage dependencies based on the actual generation/review path; and Regression Analysis from authoritative change plus existing baseline coverage. Optional risk/coverage paths remain supporting/conditional unless the actual baseline establishes otherwise.

---

## Staleness Rules

When an authoritative source revision/checksum changes, directly `required` dependent artifacts become `Stale`. When a downstream artifact depends on a specific upstream artifact revision and that revision changes, each `required` dependent becomes `Stale`.

A changed `supporting` dependency does not automatically mark the downstream artifact stale. A changed `conditional` dependency does so only when its recorded condition applies.

Staleness detection MUST NOT automatically regenerate or approve downstream artifacts:

```text
Detect → Report → Human/Workflow Decision → Regenerate or Revalidate
```

Advanced semantic change intelligence belongs to the later change-intelligence phase.

---

## Approved Baseline Preservation

An approved current baseline MUST NOT be destructively overwritten when a new feature revision is introduced. Preserve historical evidence under `revisions/<revision-id>/` or the approved archive mechanism.

A revision snapshot SHOULD preserve revision metadata, registered artifact content required for audit, source identity/fingerprint references, framework provenance, and approval/lifecycle state.

---

## Provenance

Where available, workspace metadata SHOULD preserve framework Git revision, platform/runtime, artifact revision, source revision/fingerprint, timestamps, and human review/approval evidence. Unknown provenance MUST remain explicit rather than reconstructed.

Export provenance is recorded separately in the `<export>.export.json` sidecar and MUST identify the canonical source checksum.

---

## Validation Requirements

Workspace validation MUST detect at least invalid/missing required workspace directories, malformed metadata, invalid lifecycle/freshness values, duplicate source/artifact identities, broken registered paths, broken dependencies, invalid dependency types, invalid requested lifecycle transitions, revision inconsistencies, and stale required baselines when deterministic evidence exists.

Export validation is performed separately by `scripts/export/validate_export.py`; a valid workspace does not imply a valid derived export.

Validation SHOULD report uncertainty instead of manufacturing missing metadata.

---

## Out of Scope

This standard does not define:

- spreadsheet/CSV field mapping semantics (owned by `Export.md`);
- test execution status/results;
- defect lifecycle;
- automatic requirement-diff interpretation;
- automated regression recommendation;
- CI/CD orchestration;
- Jira/TestRail/AIO API synchronization;
- autonomous regeneration or approval.

---

## Related Resources

- `shared/standards/Export.md`
- `shared/schemas/workspace-metadata.schema.json`
- `shared/schemas/revision-metadata.schema.json`
- `shared/schemas/export-metadata.schema.json`
- `scripts/workspace/`
- `scripts/export/`
- `workspace/README.md`
- `shared/standards/Output.md`
- `shared/standards/Metadata.md`
- `shared/standards/Roadmap-Progress.md`
