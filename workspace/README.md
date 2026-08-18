# QA-AI Project Workspace

## Purpose

The `workspace/` directory stores operational project/feature sources and QA-AI artifacts under the lifecycle and provenance rules defined by `shared/standards/Workspace.md`.

The canonical project/feature location is:

```text
workspace/projects/<project-id>/features/<feature-id>/
```

`workspace/current/` is only a convenience working area. It is not the authoritative long-term source of truth.

Real project workspaces may contain proprietary requirements, account/test data, evidence, or generated artifacts. `workspace/projects/` is ignored by Git by default. Do not commit real project content unless repository policy and project confidentiality explicitly allow it.

---

## Canonical Structure

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

`artifacts/` contains canonical QA-AI Markdown artifacts. `exports/` contains derived operational representations and is not a canonical artifact baseline.

---

## Initialize a Feature Workspace

From repository root:

```bash
python scripts/workspace/init_workspace.py --project <project-id> --feature <feature-id> --name "<Feature Name>"
```

The initializer creates the canonical directories, `exports/generic/`, and a metadata skeleton. It does not generate QA artifacts or promote any artifact to `Approved`.

---

## Validate a Workspace

```bash
python scripts/workspace/validate_workspace.py workspace/projects/<project-id>/features/<feature-id>
```

Validation checks structure, metadata, registered paths, identities, dependency references, lifecycle/freshness values, revision consistency, and deterministic staleness signals.

---

## Artifact Lifecycle

```text
Draft → Review → Approved → Superseded → Archived
```

Use:

```bash
python scripts/workspace/update_artifact_state.py <feature-path> <artifact-key> <new-status>
```

Promotion to `Approved` requires explicit operator evidence:

```bash
python scripts/workspace/update_artifact_state.py <feature-path> <artifact-key> Approved --approved-by "<reviewer>"
```

AI generation/self-review does not itself authorize `Approved`.

---

## Feature Revisions

A feature revision represents an authoritative product-input baseline.

Preserve the current baseline without changing active state:

```bash
python scripts/workspace/snapshot_revision.py <feature-path>
```

When intentionally opening the next authoritative feature revision, snapshot and advance together:

```bash
python scripts/workspace/snapshot_revision.py <feature-path> --advance
```

`--advance` increments the `REV-*` baseline and marks artifacts registered against the prior source revision as `Stale`. It does not regenerate them.

Historical evidence is retained under `revisions/<revision-id>/`.

---

## Derived Exports

Phase 17 exports canonical Markdown through a strict normalized model:

```text
artifacts/Test-Cases.md
→ exports/generic/Test-Cases.xlsx
→ exports/generic/Test-Cases.xlsx.export.json
```

Example:

```bash
python scripts/export/export_artifact.py <feature-path>/artifacts/Test-Cases.md --type test-cases --format xlsx --output <feature-path>/exports/generic/Test-Cases.xlsx
python scripts/export/validate_export.py <feature-path>/artifacts/Test-Cases.md <feature-path>/exports/generic/Test-Cases.xlsx --type test-cases
```

Exports follow `shared/standards/Export.md`. Editing an export does not update the canonical Markdown source.

---

## Freshness

Artifact freshness is separate from lifecycle:

```text
Current
Stale
Unknown
```

An artifact may be `Approved` but `Stale` when its registered required upstream baseline changes.

Export freshness is checksum-based and is validated separately by `scripts/export/validate_export.py`.

---

## Phase Boundary

The workspace does not own:

- execution results;
- defects/retest history;
- semantic change intelligence;
- automatic regression recommendation;
- external API/platform synchronization.

File-based export interoperability is governed by Phase 17. Test execution and later lifecycle concerns belong to subsequent phases.

---

## References

- `shared/standards/Workspace.md`
- `shared/standards/Export.md`
- `shared/schemas/workspace-metadata.schema.json`
- `shared/schemas/revision-metadata.schema.json`
- `scripts/workspace/`
- `scripts/export/`
