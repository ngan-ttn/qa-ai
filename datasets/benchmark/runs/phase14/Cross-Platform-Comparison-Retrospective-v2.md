# Phase 14 Cross-Platform Comparison — Retrospective Review v2

> Comparison ID: `P14-XPLAT-RETRO-002`  
> Run Set: `P14-RUNSET-001`  
> Dataset: `REQ-AUTH-001`  
> Artifact: `Structured Test Case Model`  
> Evaluation configuration: `EVAL-CRITERIA-001` + `EVAL-RUBRIC-001` + `EVAL-SCORING-001`  
> Status: **Proposed — project-owner approval pending**  
> Review date: 2026-10-29

## Purpose and record handling

This version records a retrospective C07 review of the preserved ChatGPT output. It does not modify the original `Cross-Platform-Comparison-Candidate.md`, raw outputs, or original evaluation files. This comparison must not be treated as an approved replacement baseline until the project owner approves the retrospective evaluation.

## Platform results

| Platform | Run ID | Original score | Retrospective score used here | Result | Critical failures | Review status |
|---|---|---:|---:|---|---:|---|
| ChatGPT | `P14-RUN-CHATGPT-003` | 100 | 97 (proposed) | PASS | 0 | C07 review complete; owner approval pending |
| Claude | `P14-RUN-CLAUDE-001` | 99 | 99 (original evaluation) | PASS | 0 | Not re-evaluated |
| Cursor | `P14-RUN-CURSOR-001` | 99 | 99 (original evaluation) | PASS | 0 | Not re-evaluated |

**Important:** this is not a fresh, simultaneous re-run of all platforms. Only ChatGPT C07 was retrospectively re-evaluated. The results therefore provide a provisional score comparison, not evidence of current runtime performance or repeatability.

## C07 review rationale

The ChatGPT raw output contains repeated malformed Markdown table headers that merge intended column labels, including:

- `Rule IDConfirmed business rule`
- `Scenario IDObjectiveRule trace`
- `StepActionExpected result`

These defects recur across business-rule, scenario, testcase, and test-data tables. Much of the data remains readable, but the table structure reduces reviewability and requires correction. Under the canonical C07 rubric, L2 (Partial) is recommended over the original L4. The reviewed Claude and Cursor outputs do not exhibit the same repeated merged-header pattern in the inspected sections; their original C07 L3 ratings remain unchanged.

## Score calculation

For ChatGPT, all other criterion levels remain unchanged and C11 remains N/A:

- Raw weighted score: `92.50`
- Active weight: `95`
- Normalized score: `(92.50 / 95) × 100 = 97.3684...`
- Final rounded score: `97`
- Numeric threshold: `PASS` (threshold 85)
- Critical failures identified in this isolated review: `0`

Claude and Cursor retain their original recorded scores of 99. Their results were not retrospectively rescored in this review.

## Interpretation

- The provisional score spread is 2 points (ChatGPT 97; Claude 99; Cursor 99).
- This difference should not be interpreted as a definitive platform ranking: ChatGPT received a targeted retrospective review, while Claude and Cursor retain their original evaluation records.
- The C07 issue is an artifact-formatting/reviewability defect; this review did not identify a source contradiction or critical QA-coverage omission.
- The original Phase 14 gate approval on 2026-08-17 remains historical evidence. It is not silently revoked or rewritten by this retrospective document.

## Approval and next actions

1. Project owner reviews and approves/rejects the proposed ChatGPT C07 L2 rating and score 97.
2. If approved, publish this comparison as the superseding comparison and update the status register accordingly.
3. If rejected or adjusted, record the decision and rationale in a new version; do not edit historical evidence.
4. Fix the table-generation issue in a new runtime output and run a new controlled set before claiming the defect is resolved.
5. For a definitive current platform comparison, re-evaluate Claude and Cursor under the same retrospective checklist or rerun all platforms with the corrected framework, using new run IDs and complete metadata.
