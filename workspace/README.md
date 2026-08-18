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
│               ├── revisions/
│               └── archive/
└── current/
    └── README.md
```

---

## Initialize a Feature Workspace

From repository root:

```bash
python scripts/workspace/init_workspace.py --project <project-id> --feature <feature-id> --name "<Feature Name>"
```

The initializer creates the canonical directories and a metadata skeleton. It does not generate QA artifacts or promote any artifact to `Approved`.

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

## Freshness

Freshness is separate from lifecycle:

```text
Current
Stale
Unknown
```

An artifact may be `Approved` but `Stale` when its registered required upstream baseline changes.

Workspace tooling detects/reports stale state. It does not silently regenerate downstream artifacts.

---

## Phase Boundary

The workspace does not own:

- Excel/CSV/test-management export;
- execution results;
- defects/retest history;
- semantic change intelligence;
- automatic regression recommendation;
- external platform synchronization.

Those concerns belong to later roadmap phases.

---

## References

- `shared/standards/Workspace.md`
- `shared/schemas/workspace-metadata.schema.json`
- `shared/schemas/revision-metadata.schema.json`
- `scripts/workspace/`
