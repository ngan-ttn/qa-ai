# Workspace Scripts

Deterministic tooling for Phase 16 project/feature workspace lifecycle management.

| Script | Responsibility |
|---|---|
| `init_workspace.py` | Initialize canonical project/feature directories and metadata skeleton. |
| `validate_workspace.py` | Validate structure, metadata, paths, identities, dependency references, lifecycle/freshness values, and deterministic stale revision signals. |
| `snapshot_revision.py` | Preserve the current revision baseline under `revisions/<revision-id>/`. |
| `update_artifact_state.py` | Apply controlled artifact lifecycle transitions. |

These scripts manage workspace state only. They do not generate QA artifacts, approve artifacts automatically, perform semantic change analysis, export test cases, execute tests, or recommend regression scope.

Canonical rules: `shared/standards/Workspace.md`.
