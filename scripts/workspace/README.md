# Workspace Scripts

Deterministic tooling for Phase 16 project/feature workspace lifecycle management.

| Script | Responsibility |
|---|---|
| `init_workspace.py` | Initialize canonical project/feature directories and metadata skeleton. |
| `register_source.py` | Copy/register authoritative or supporting source files with stable source IDs and SHA-256 fingerprints. |
| `register_artifact.py` | Register artifact provenance, freshness, and actual dependency metadata for an existing artifact file. |
| `validate_workspace.py` | Validate structure, metadata, paths, identities, dependency references, lifecycle/freshness values, and deterministic stale revision signals. |
| `snapshot_revision.py` | Preserve the current revision baseline under `revisions/<revision-id>/` and optionally advance the feature revision. |
| `update_artifact_state.py` | Apply controlled artifact lifecycle transitions; approval requires explicit reviewer evidence. |

These scripts manage workspace state only. They do not generate QA artifacts, approve artifacts automatically, perform semantic change analysis, export test cases, execute tests, or recommend regression scope.

## Typical Operational Sequence

```text
init_workspace
  ↓
register_source
  ↓
copy/generate canonical QA artifacts
  ↓
register_artifact
  ↓
validate_workspace
  ↓
Draft → Review → Approved
  ↓
snapshot_revision before replacing an approved baseline
```

Canonical rules: `shared/standards/Workspace.md`.
