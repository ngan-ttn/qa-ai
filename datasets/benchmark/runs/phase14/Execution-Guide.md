# Phase 14 Execution Guide

## 1. Prepare Local Branch

```powershell
git switch phase14-runtime-evaluation
git pull origin phase14-runtime-evaluation
git status
```

Use a clean working tree before every controlled run.

## 2. Run Each Platform

Execute the prompt in `Runtime-Execution-Prompt.md` against the exact dataset `datasets/requirements/simple/REQ-AUTH-001.md` on:

1. ChatGPT Custom GPT configured with the frozen Phase 13 QA-AI adapter.
2. Claude Code with the frozen Phase 13 repository `CLAUDE.md` installation.
3. Cursor with the frozen Phase 13 `.cursor/` rules/commands installation.

Use run IDs:

```text
P14-RUN-CHATGPT-001
P14-RUN-CLAUDE-001
P14-RUN-CURSOR-001
```

## 3. Capture Raw Outputs

Create runtime evidence locally under ignored `output/` first:

```text
output/phase14/P14-RUN-CHATGPT-001/raw-output.md
output/phase14/P14-RUN-CLAUDE-001/raw-output.md
output/phase14/P14-RUN-CURSOR-001/raw-output.md
```

Also copy and complete `templates/Execution-Metadata.json` for each run.

Do not edit raw runtime responses before evaluation.

## 4. Evaluate Criterion Levels

Review each raw output against:

- `EVAL-CRITERIA-001`
- `EVAL-RUBRIC-001`
- `EVAL-SCORING-001`

Prepare one scoring input per run using `templates/Scoring-Input.json`:

```text
output/phase14/<RUN-ID>/scoring-input.json
```

Keep evaluator evidence/notes separately so rubric-level decisions remain reviewable.

## 5. Calculate Deterministic Score

For each run:

```powershell
python scripts/evaluation/score_format.py output/phase14/<RUN-ID>/scoring-input.json --output output/phase14/<RUN-ID>/score.json
```

A PASS requires the canonical scoring gate and no critical failures.

## 6. Build Benchmark Evidence

When a reviewed score exists, benchmark evidence may be built against the applicable golden reference where an artifact-compatible golden output exists:

```powershell
python scripts/evaluation/benchmark.py <golden-artifact> output/phase14/<RUN-ID>/raw-output.md --score-file output/phase14/<RUN-ID>/score.json --output output/phase14/<RUN-ID>/benchmark-evidence.json
```

Textual comparison remains supporting evidence only. Quality PASS/FAIL comes from canonical evaluation scoring.

## 7. Promote Reviewed Evidence

Only after a run is reviewed should stable evidence be promoted from ignored runtime `output/` into a committed benchmark-record location.

Do not commit unreviewed raw runs merely to satisfy Phase 14 structure.

A promoted record must preserve:

- immutable/reviewable dataset reference;
- framework/repository reference;
- platform/runtime metadata;
- raw artifact evidence or stable reference;
- evaluator levels and reasoning;
- deterministic scoring result;
- baseline eligibility/approval state.

## 8. Cross-Platform Review

After all three runs are evaluated, complete `templates/Cross-Platform-Comparison.md` using criterion-level results.

Do not use wording similarity as the primary comparison measure.

## 9. Final Baseline

A baseline candidate may be approved only when the applicable `BENCH-BASELINE-001` eligibility and review conditions are met.

Once approved, it becomes the regression-ready comparison point for later controlled QA-AI changes.