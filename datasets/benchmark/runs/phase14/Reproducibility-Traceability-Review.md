# Phase 14 Reproducibility & Traceability Review

> Version: 1.0.0  
> Status: Completed  
> Last Updated: 2026-08-17

## 1. Purpose

Validate that the accepted Phase 14 controlled runs contain sufficient evidence to understand what was executed, what was evaluated, how scores were produced, and which limitations remain unknown.

The goal is reproducibility and traceability of the evaluation contract, not byte-for-byte reproduction of platform wording.

## 2. Accepted Run Set

| Platform | Accepted Run | Raw Output | Metadata | Scoring Input | Evaluation Result | Baseline Candidate |
|---|---|---|---|---|---|---|
| ChatGPT | `P14-RUN-CHATGPT-003` | Present | Present | Present | Present | Present |
| Claude | `P14-RUN-CLAUDE-001` | Present | Present | Present | Present | Present |
| Cursor | `P14-RUN-CURSOR-001` | Present | Present | Present | Present | Present |

## 3. Common Evaluation Contract

All accepted runs are traceable to:

- run set: `P14-RUNSET-001`;
- dataset: `datasets/requirements/simple/REQ-AUTH-001.md`;
- workflow: `workflows/testcase-generation`;
- target artifact: Structured Test Case Model;
- prompt: `datasets/benchmark/runs/phase14/Runtime-Execution-Prompt.md`;
- criteria: `EVAL-CRITERIA-001`;
- rubric: `EVAL-RUBRIC-001`;
- scoring: `EVAL-SCORING-001`;
- profile: `canonical-default`.

## 4. Platform Traceability

### ChatGPT

Captured execution metadata includes repository branch/commit, execution timestamp, platform, adapter reference, prompt reference, and evaluation configuration. Exact model identifier was not visible/captured and remains explicitly unknown.

### Claude

Captured execution metadata includes repository branch/commit, execution timestamp, Claude runtime/model label, adapter reference, prompt reference, and evaluation configuration. The temporary repository-root `CLAUDE.md` installation used the adapter file unchanged for execution and was not committed as runtime evidence.

### Cursor

Captured execution metadata identifies platform, branch, adapter/rules, dataset, workflow, prompt, and evaluation configuration. Exact model identifier, execution timestamp, and execution commit were not captured and remain explicitly unknown.

## 5. Score Reproducibility

The accepted scores are derived from stored criterion-level scoring inputs and canonical `scripts/evaluation/score_format.py` semantics.

| Platform | Stored Criterion Result | Final Score | Critical Failures |
|---|---|---:|---|
| ChatGPT | All applicable criteria L4; C11 N/A | 100 | None |
| Claude | C07 L3; other applicable criteria L4; C11 N/A | 99 | None |
| Cursor | C07 L3; other applicable criteria L4; C11 N/A | 99 | None |

The Claude score was produced by the canonical scoring script after normalizing the Scoring-Input JSON to UTF-8 without BOM. The encoding correction changed file transport encoding only, not criterion content or scoring semantics.

## 6. Raw-Evidence Integrity

- Raw runtime outputs are preserved separately from evaluator annotations.
- Historical ChatGPT failed/blocked runs remain preserved and are not overwritten by the accepted run.
- The Claude runtime blocker is retained and marked resolved rather than removed.
- Unknown runtime metadata is left unknown rather than reconstructed.
- Platform wording/format differences are not used as the primary quality criterion.

## 7. Reproduction Expectations

A future reviewer can reconstruct the evaluation meaning by identifying:

1. the authoritative dataset;
2. the controlled prompt/run set;
3. the platform adapter/runtime context;
4. the raw generated artifact;
5. the criterion-level review input;
6. the canonical scoring implementation;
7. the resulting baseline candidate.

A future rerun is not required to reproduce identical prose. It must preserve the controlled contract and be evaluated under compatible semantics.

## 8. Findings

### Blocking Findings

None.

### Explicit Limitations

- ChatGPT exact model identifier was not captured.
- Cursor exact model, execution timestamp, and execution commit were not captured.
- Claude required adapter installation at repository root for execution because the root `CLAUDE.md` was absent; the installed content matched `adapters/claude/CLAUDE.md` unchanged.

These limitations are documented, do not require unsupported reconstruction, and do not prevent a reviewer from tracing the dataset, workflow, output, evaluation configuration, criterion levels, and measured scores.

## 9. Stage 14.5 Decision

**PASS — Reproducibility and traceability are sufficient for the defined Phase 14 pilot baseline.**

No unresolved blocking issue remains for source traceability, accepted-run evidence, or scoring semantics.

`14.5 Reproducibility & Traceability — Completed`
