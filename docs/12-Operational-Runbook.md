# QA-AI Operational Runbook

> Version: 1.0.1
> Status: Draft
> Last Updated: 2026-08-21

## Purpose

Provide the operational path for using QA-AI as a closed QA lifecycle while preserving canonical ownership boundaries and explicit Human QC authority.

## Operational Loop

1. Validate repository readiness.
2. Initialize a project/feature workspace.
3. Register authoritative requirement sources.
4. Generate requirement analysis and downstream canonical QA artifacts through the owning skills/workflows.
5. Perform Human QC review and explicit artifact lifecycle approval.
6. Export approved/current deliverables where an interoperable representation is required.
7. Initialize an execution run from existing canonical testcase IDs.
8. Record Pass, Fail, Blocked, Not Run, or Not Applicable evidence; link defects without taking ownership of external defect lifecycle.
9. Record retests as new immutable attempts and reconcile current disposition.
10. Before introducing an authoritative source revision, snapshot the prior canonical feature baseline and advance the workspace revision.
11. Register the changed source revision using the same stable source identity when its canonical type/path is unchanged.
12. Run Change Intelligence between the immutable prior snapshot and the current working target revision; the target does not need a historical snapshot before analysis.
13. Review the incremental QA plan: Reuse, Review, Regenerate, Revalidate, Re-execute, or Blocked.
14. Route each action back to its owning skill/workflow/lifecycle process and begin the next QA cycle.

## Source Revision Identity

A canonical source keeps a stable `SRC-*` identity across content revisions when its source type and workspace-relative path are unchanged. The prior snapshot preserves the older revision/checksum, while current workspace metadata records the new revision/checksum.

Example:

```text
REV-001 snapshot: SRC-001 revision 1.0 checksum A
REV-002 working:  SRC-001 revision 2.0 checksum B
```

This permits deterministic Change Intelligence to classify `source:SRC-001` as `Modified` and propagate supported dependency impact without inventing a new source relationship.

## Release Readiness

For a system release candidate:

```text
python scripts/release/build_manifest.py --release-id QA-AI-1.0.0 --status Candidate
python scripts/release/validate_manifest.py
python scripts/release/validate_release.py --workspace <feature-path> --revision <REV-N> --execution <run-path>
python scripts/release/generate_release_report.py
```

Release validation is fail-closed. Human QC reviews the generated evidence before a candidate is promoted to Released.

## Ownership Boundaries

- Workspace lifecycle owns artifact/revision state.
- Export owns interoperable representations, never canonical source truth.
- Execution owns run/result/retest evidence.
- Regression analysis owns regression scope selection.
- Change Intelligence owns change/impact evidence and incremental recommendations only.
- Release tooling owns release-level inventory and readiness orchestration only.

## Change After Release Validation

Any repository change invalidates revision-bound release evidence for the new repository state. Rebuild the manifest and rerun release validation before asserting readiness for the changed revision.
