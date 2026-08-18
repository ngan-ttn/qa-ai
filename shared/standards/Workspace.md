# Workspace Standard

> Version: 1.0.0  
> Status: Draft  
> Last Updated: 2026-08-18

## Purpose

The `Workspace` standard defines the canonical project workspace, identity, provenance, revision, artifact-lifecycle, dependency, freshness, and archive rules used to manage operational QA-AI project artifacts.

It governs project artifact management only. It does not redefine canonical QA skills, workflow semantics, artifact content contracts, test execution, export behavior, or regression-analysis semantics.

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
│               ├── revisions/
│               └── archive/
└── current/
    └── README.md
```

`workspace/projects/<project-id>/features/<feature-id>/` is the canonical project/feature source of truth. `workspace/current/` is an optional working convenience layer and MUST NOT become the authoritative long-term artifact store.

---

## Identity Model

### Project Identity

A project is identified by a stable `project_id` suitable for repository paths.

### Feature Identity

A feature is identified by a stable `feature_id` within its project. Renaming a display name MUST NOT silently change the stable feature identity.

### Source Identity

Each registered source uses a stable `source_id`, for example `SRC-001`.

A source registration records at minimum:

- source identity;
- source type;
- repository-relative path within the feature workspace;
- whether the source is authoritative;
- source revision when known;
- checksum when deterministic source bytes are available;
- registration timestamp.

### Artifact Identity

An artifact is a whole QA document such as `Test-Cases.md`. Record-level IDs such as `BR-*`, `SC-*`, and `TC-*` remain owned by the corresponding artifact contracts and MUST NOT be replaced by workspace artifact IDs.

---

## Feature Metadata

Each feature workspace MUST contain `metadata.json` conforming to `shared/schemas/workspace-metadata.schema.json`.

The feature metadata owns:

- project and feature identity;
- feature display name;
- feature operational status;
- current feature revision;
- framework revision/provenance;
- source registrations;
- artifact registrations;
- dependency relationships;
- lifecycle/freshness state;
- created/updated timestamps.

It MUST NOT duplicate the full content of QA artifacts.

---

## Feature Revision Model

A feature revision represents an authoritative product-input baseline, not an arbitrary edit to an output document.

Recommended identifiers use:

```text
REV-001
REV-002
REV-003
```

When a new authoritative source baseline replaces the previous one:

1. preserve the prior approved baseline as historical evidence;
2. advance the current feature revision;
3. register the new/changed authoritative source;
4. mark affected downstream artifacts stale according to dependency rules;
5. do not silently overwrite historical evidence.

Historical revision metadata MUST conform to `shared/schemas/revision-metadata.schema.json`.

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

### Lifecycle Authority

AI generation or self-review MUST NOT automatically promote an artifact to `Approved`. Human review or an explicitly authorized approval mechanism is required.

### Valid Transitions

Baseline transitions are:

```text
Draft → Review
Review → Draft
Review → Approved
Approved → Superseded
Superseded → Archived
```

Direct transitions outside the defined lifecycle require explicit maintenance justification and MUST NOT be performed silently by workspace tooling.

---

## Freshness Model

Freshness is independent from artifact lifecycle.

Canonical freshness values are:

```text
Current
Stale
Unknown
```

An artifact may therefore be `Approved` and `Stale` simultaneously: approval records review state; freshness records whether its registered upstream baseline still matches.

| Freshness | Meaning |
|---|---|
| `Current` | Registered upstream/source revisions match the artifact dependency baseline. |
| `Stale` | At least one dependency revision/source fingerprint no longer matches the artifact baseline. |
| `Unknown` | Freshness cannot be determined from available metadata. |

Freshness MUST NOT be encoded as an artifact lifecycle status.

---

## Dependency Model

Workspace dependencies use three relationship types:

| Type | Meaning |
|---|---|
| `required` | The downstream artifact requires the registered upstream baseline to remain valid. A changed upstream revision marks the dependent artifact stale. |
| `supporting` | The upstream artifact provides evidence/context but is not automatically invalidating. A change requires review before stale propagation. |
| `conditional` | The dependency applies only when the associated workflow/gate/feature condition was used. Staleness is evaluated only when the condition is active for that artifact baseline. |

The workspace dependency graph MUST NOT redefine canonical workflow order or convert optional feedback paths into hard dependencies.

---

## Baseline Dependency Guidance

Typical relationships include:

```text
Requirement Analysis
  ← authoritative requirement source (required)

Business Rules
  ← Requirement Analysis (required)

Risk Analysis
  ← Requirement Analysis (required)
  ← Business Rules (supporting or required according to the actual generation basis)

Test Scenarios
  ← Requirement Analysis (required)
  ← Business Rules (required when used)
  ← Risk Analysis (supporting/conditional when used)

Coverage Review
  ← reviewed Test Scenarios/Test Cases (required)
  ← sufficient authoritative upstream artifacts (required)

Test Cases
  ← Test Scenarios (required)
  ← Coverage Review (conditional when used as an active quality gate)

Regression Analysis
  ← authoritative change delta (required)
  ← baseline artifacts and existing coverage (required/supporting according to actual evidence)
```

Metadata MUST represent the relationships actually used for an artifact. It MUST NOT claim dependencies merely because they are common in a generic workflow.

---

## Staleness Rules

### Source Change

When an authoritative source revision/checksum changes, each directly `required` dependent artifact becomes `Stale`.

### Upstream Artifact Change

When an artifact baseline depends on a specific upstream artifact revision and that upstream approved revision changes, each `required` dependent artifact becomes `Stale`.

### Supporting Change

A changed `supporting` dependency MUST NOT automatically mark the downstream artifact stale. It creates a review condition unless project/workflow metadata explicitly establishes it as invalidating.

### Conditional Change

A changed `conditional` dependency marks the downstream artifact stale only when the recorded condition applies to that artifact baseline.

### No Auto-Regeneration

Staleness detection MUST NOT automatically regenerate or approve downstream artifacts. The baseline sequence is:

```text
Detect → Report → Human/Workflow Decision → Regenerate or Revalidate
```

Advanced semantic change intelligence is outside this standard and belongs to the later change-intelligence phase.

---

## Approved Baseline Preservation

An approved current baseline MUST NOT be destructively overwritten when a new feature revision is introduced.

Before replacement, preserve historical evidence under `revisions/<revision-id>/` or the approved archive mechanism.

A revision snapshot SHOULD preserve at minimum:

- revision metadata;
- registered artifact paths/content required for audit;
- source identity/fingerprint references;
- framework revision/provenance;
- approval/lifecycle state.

---

## Provenance

Where available, workspace metadata SHOULD preserve:

- framework Git revision;
- platform/runtime that generated the artifact;
- artifact revision;
- source revision/fingerprint;
- generation/update timestamps;
- human review/approval evidence identifier or note.

Unknown provenance MUST remain explicit rather than reconstructed.

---

## Validation Requirements

Workspace validation MUST detect at least:

- invalid/missing required workspace directories;
- malformed metadata;
- invalid lifecycle or freshness values;
- duplicate source/artifact identities;
- broken registered paths;
- broken dependency references;
- invalid dependency types;
- invalid lifecycle transitions when state updates are requested;
- revision inconsistencies;
- stale `required` dependency baselines when deterministic revision/fingerprint evidence exists.

Validation SHOULD report uncertainty instead of manufacturing missing metadata.

---

## Out of Scope

This standard does not define:

- spreadsheet/test-management export;
- test execution status/results;
- defect lifecycle;
- automatic requirement-diff interpretation;
- automated regression recommendation;
- CI/CD orchestration;
- Jira/TestRail/AIO synchronization;
- autonomous regeneration or approval.

---

## Related Resources

- `shared/schemas/workspace-metadata.schema.json`
- `shared/schemas/revision-metadata.schema.json`
- `scripts/workspace/`
- `workspace/README.md`
- `shared/standards/Output.md`
- `shared/standards/Metadata.md`
- `shared/standards/Roadmap-Progress.md`
