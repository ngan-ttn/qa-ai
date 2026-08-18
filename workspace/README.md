# QA-AI Project Workspace

## Purpose

The `workspace/` directory stores operational project/feature sources, QA-AI artifacts, derived exports, and execution evidence under the lifecycle and provenance rules defined by the shared standards.

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
│               ├── executions/
│               │   └── RUN-*/
│               ├── revisions/
│               └── archive/
└── current/
    └── README.md
```

`artifacts/` contains canonical QA-AI Markdown artifacts. `exports/` contains derived operational representations and is not a canonical artifact baseline. `executions/` contains structured execution evidence and derived execution summaries.

---

## Initialize a Feature Workspace

```bash
python scripts/workspace/init_workspace.py --project <project-id> --feature <feature-id> --name "<Feature Name>"
```

The initializer creates canonical source/artifact/export/execution/revision/archive directories and a metadata skeleton. It does not generate QA artifacts or promote any artifact to `Approved`.

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

Use `scripts/workspace/update_artifact_state.py`. Promotion to `Approved` requires explicit operator evidence. AI generation/self-review does not itself authorize `Approved`.

---

## Feature Revisions

A feature revision represents an authoritative product-input baseline. Preserve or advance revisions with `scripts/workspace/snapshot_revision.py`. Historical evidence is retained under `revisions/<revision-id>/` and advancement marks prior-baseline artifacts stale without regenerating them.

---

## Derived Exports

Phase 17 exports canonical Markdown through strict normalized models. Exports follow `shared/standards/Export.md`. Editing an export does not update canonical Markdown.

---

## Test Execution

Phase 18 execution evidence lives under `executions/RUN-*`:

```text
RUN-001/
├── execution.json
├── results.json
├── defects.json
├── Execution-Summary.md
└── evidence/
```

Initialize and record a run with `scripts/execution/`. Execution records follow `shared/standards/Execution.md`.

Important rules:

- `Pass`, `Fail`, `Blocked`, `Not Run`, and `Not Applicable` are the canonical result statuses;
- `Blocked` requires an explicit blocker type and reason;
- retests create new `ER-*` records and never overwrite earlier attempts;
- execution summaries use the latest valid attempt as current disposition;
- status totals must reconcile with unique scoped testcase IDs;
- stale Test Cases are blocked by default and require an explicit audited override;
- defect references link execution evidence but do not redefine external defect lifecycle.

---

## Freshness

Artifact freshness is separate from lifecycle:

```text
Current
Stale
Unknown
```

An artifact may be `Approved` but `Stale` when its registered required upstream baseline changes. Export freshness is checksum-based. Execution provenance preserves the testcase source checksum used for the run.

---

## Phase Boundary

The workspace itself does not own QA generation semantics, external defect workflow, automatic test execution, semantic change intelligence, automatic regression recommendation, or external API/platform synchronization.

- Phase 17 owns file-based export interoperability.
- Phase 18 owns structured test execution evidence and defect/retest linkage.
- Later phases may consume this evidence without redefining it.

---

## References

- `shared/standards/Workspace.md`
- `shared/standards/Export.md`
- `shared/standards/Execution.md`
- `shared/schemas/workspace-metadata.schema.json`
- `shared/schemas/revision-metadata.schema.json`
- `shared/schemas/execution-run.schema.json`
- `shared/schemas/execution-results.schema.json`
- `shared/schemas/execution-defects.schema.json`
- `scripts/workspace/`
- `scripts/export/`
- `scripts/execution/`
