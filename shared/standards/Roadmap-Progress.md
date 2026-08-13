# Roadmap Progress Tracking Standard

> Version: 1.0.0  
> Status: Draft  
> Last Updated: 2026-08-13

---

## Purpose

Define how QA-AI records component completion, aggregates phase progress, and keeps the implementation roadmap synchronized with repository state.

## Source of Truth

`roadmap-status.json` is the machine-readable source of truth for roadmap progress. `docs/11-Roadmap.md` is the human-readable roadmap view.

The roadmap must not maintain an independent status that conflicts with the registry.

## Tracking Unit

Progress is tracked at the roadmap deliverable or component level, not for every physical file.

A file may be part of a tracked component, but file existence alone does not mean the component is complete.

## Status Lifecycle

Tracked components use:

```text
Planned
  ↓
In Progress
  ↓
Review
  ↓
Completed
  ↓
Frozen
```

`Completed` requires all mandatory artifacts and component quality gates to pass. `Frozen` additionally requires the applicable cross-component review and baseline closure.

## Completion Rules

The following rules are mandatory:

```text
File exists                  ≠ Completed
Content written              ≠ Completed
Self-review pending          ≠ Completed
Quality gate passed          = eligible for Completed
Cross-component review pass  = eligible for Frozen
```

A component status must not be promoted only because its files exist.

## Progress Aggregation

Phase progress is derived from tracked components in `roadmap-status.json`.

For countable components:

```text
progress = completed tracked components / total tracked components
```

Counts must use the canonical inventory for that phase.

## Roadmap Synchronization

Whenever a tracked component changes status, roadmap progress must be recalculated.

The synchronization flow is:

```text
Repository artifact changes
        ↓
Component quality gate
        ↓
roadmap-status.json
        ↓
Progress validation
        ↓
docs/11-Roadmap.md
```

Until Phase 12 automation is implemented, the registry and roadmap are updated together in the same change set. Phase 12 should automate collection, validation, and roadmap rendering.

## Automation Contract

The future automation must:

1. read `roadmap-status.json`;
2. validate allowed statuses and required component fields;
3. verify configured completion evidence where available;
4. calculate component and phase progress;
5. update only generated roadmap progress regions;
6. fail rather than silently infer completion when evidence is incomplete or inconsistent;
7. preserve manually maintained roadmap narrative outside generated regions.

## Quality Gates

A roadmap update passes only when:

- the tracked component belongs to the phase inventory;
- its status transition is valid;
- required review gates are satisfied;
- component counts do not exceed expected totals;
- phase status is consistent with component status;
- `Frozen` is not assigned while mandatory components remain incomplete;
- the human-readable roadmap and machine-readable registry agree.

## Phase Closure

A phase may become `Completed` only after all mandatory deliverables and exit criteria pass.

A phase may become `Frozen` only after its required cross-component review passes and the resulting baseline is approved for downstream use.

## Maintenance

Changes to tracking semantics, status lifecycle, aggregation rules, or automation contracts require review because they affect repository-wide progress reporting.
