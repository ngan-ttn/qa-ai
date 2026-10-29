# Phase 14 Benchmark Status Register

> Register ID: P14-STATUS-REGISTER-001  
> Last reviewed: 2026-10-29  
> Status: Retrospective score review open

## Purpose and precedence

This register resolves status-label conflicts without rewriting historical execution evidence.

1. `Final-Gate-Readiness.md` records that the original Phase 14 gate was approved on 2026-08-17.
2. The per-platform `Baseline-Candidate.json` files are immutable snapshots of candidate state at the time they were created. Their `Candidate` status is historical and is not, by itself, the current status of the overall run set.
3. The original `Cross-Platform-Comparison-Candidate.md` remains a historical comparison record. It must not be treated as the latest score authority after this retrospective review.
4. This register is the current status index until a superseding evaluation/comparison is approved.

## Current status

| Scope | Status | Interpretation |
|---|---|---|
| Original Phase 14 execution and final gate | Approved (historical decision, 2026-08-17) | The original gate decision remains part of the audit trail. |
| Raw runtime outputs and original evaluation records | Frozen / immutable evidence | Do not edit historical raw outputs or rewrite the original scores in place. |
| ChatGPT C07 score | Re-evaluated: 97/100; project-owner approval pending | C07 is recommended to change from L4 to L2 because of repeated malformed table headers. See `Retrospective-C07-Reevaluation.md` and `records/chatgpt/run-003/Evaluation-Result-Retrospective-v2.json`. |
| Claude score | 99/100, original evaluation | No retrospective re-evaluation was performed in this change. |
| Cursor score | 99/100, original evaluation | No retrospective re-evaluation was performed in this change. |
| Cross-platform score comparison | Review hold | `Cross-Platform-Comparison-Retrospective-v2.md` is a provisional comparison only; ChatGPT was re-evaluated while Claude and Cursor retain original scores. Do not treat it as an approved replacement baseline. |
| Future benchmark expansion | Planned, not executed | See `Benchmark-Expansion-Plan.md`; no new measured results are implied. |

## Baseline governance decision

The original Phase 14 gate remains historically approved, but the current score comparison is **not considered fully reconciled** until the project owner approves the retrospective C07 review and decides whether the provisional comparison is acceptable. Keep the raw run evidence frozen. The versioned retrospective evaluation and comparison have been created as proposals only; they do not promote a new baseline.

The status words mean:
- **Candidate** — eligible for review, not promoted.
- **Approved** — passed the defined review/gate at a stated point in time.
- **Frozen** — immutable evidence/version; corrections are recorded in a new version, not by editing history.
- **Review hold** — do not use the affected aggregate/comparison as the latest verified decision while a material review is unresolved.

## Required closure actions

1. Project owner approves/rejects the C07 re-evaluation and score 97.
2. If approved, accept or revise the provisional comparison and update this register in a new commit.
3. Keep the original 100/99/99 records available as historical evidence, clearly marked as superseded for current comparison purposes only after approval.
4. Execute the expanded benchmark only as a new run set with new run IDs and captured metadata.
5. For a definitive platform comparison, re-evaluate all platforms under the same retrospective checklist or rerun all platforms with the corrected framework.
