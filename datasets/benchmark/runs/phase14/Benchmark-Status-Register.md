# Phase 14 Benchmark Status Register

> Register ID: P14-STATUS-REGISTER-001  
> Last reviewed: 2026-10-29  
> Status: Retrospective ChatGPT C07 decision approved; cross-platform comparison remains on review hold

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
| ChatGPT C07 score | Approved retrospective re-evaluation: 97/100; owner approval recorded 2026-10-29 | C07 is recommended to change from L4 to L2 because of repeated malformed table headers. See `Retrospective-C07-Reevaluation.md` and `records/chatgpt/run-003/Evaluation-Result-Retrospective-v2.json`. |
| Claude score | 99/100, original evaluation | No retrospective re-evaluation was performed in this change. |
| Cursor score | 99/100, original evaluation | No retrospective re-evaluation was performed in this change. |
| Cross-platform score comparison | Review hold | `Cross-Platform-Comparison-Retrospective-v2.md` is a provisional comparison only; ChatGPT was re-evaluated while Claude and Cursor retain original scores. Do not treat it as an approved replacement baseline. |
| Future benchmark expansion | Planned, not executed | See `Benchmark-Expansion-Plan.md`; no new measured results are implied. |

## Baseline governance decision

The original Phase 14 gate remains historically approved. The project owner approved the retrospective ChatGPT C07=L2 rating and score 97/100 on 2026-10-29. This approval applies to that retrospective evaluation only; it does not approve a definitive cross-platform ranking or promote a new baseline. Claude and Cursor have not been retrospectively rescored under the same checklist. Keep raw run evidence frozen and the aggregate comparison on review hold.

The status words mean:
- **Candidate** — eligible for review, not promoted.
- **Approved** — passed the defined review/gate at a stated point in time.
- **Frozen** — immutable evidence/version; corrections are recorded in a new version, not by editing history.
- **Review hold** — do not use the affected aggregate/comparison as the latest verified decision while a material review is unresolved.

## Required closure actions

1. Record the approved ChatGPT C07=L2 and score 97/100 decision in versioned retrospective records; do not overwrite original evidence.
2. Keep the cross-platform comparison on review hold until Claude and Cursor are evaluated under the same checklist or all platforms are rerun with the corrected framework.
3. Fix and verify malformed Markdown table generation in a new runtime output.
4. Execute expanded benchmarks only as a new run set with new run IDs and captured metadata.
5. Keep the original 100/99/99 records as historical evidence; do not claim a definitive ranking from non-equivalent evaluations.
