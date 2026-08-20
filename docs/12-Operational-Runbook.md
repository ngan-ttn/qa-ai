# QA-AI Operational Runbook

> Version: 1.0.0
> Status: Draft
> Last Updated: 2026-08-20

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
10. Snapshot and advance the feature revision when authoritative change occurs.
11. Run Change Intelligence between immutable revision evidence.
12. Review the incremental QA plan: Reuse, Review, Regenerate, Revalidate, Re-execute, or Blocked.
13. Route each action back to its owning skill/workflow/lifecycle process and begin the next QA cycle.

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
