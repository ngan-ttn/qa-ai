# Phase 14 Run Capture Checklist

Use this checklist for every controlled platform run.

## Before Execution

- Confirm current branch/commit used by the runtime or adapter package.
- Confirm `REQ-AUTH-001` is unchanged from the approved run-set definition.
- Confirm the Phase 13 adapter/instructions are active for the target platform.
- Confirm no extra product requirement context is present in the runtime conversation/session.
- Record platform, model/runtime identifier when visible, adapter version/reference, date/time, and operator.

## Execute

- Submit the controlled prompt from `Runtime-Execution-Prompt.md`.
- Do not add clarifications unless the run is intentionally invalidated and restarted.
- Capture the complete raw response without edits.
- Record any runtime/tool error separately from artifact-quality evaluation.

## Artifact Review

Verify that the response:

- routed to the canonical testcase-generation workflow;
- remained source-grounded in `REQ-AUTH-001`;
- did not invent implementation details;
- produced executable test cases for confirmed behavior;
- preserved meaningful traceability;
- included boundary/state/reset/isolation behavior supported by the dataset;
- did not silently omit critical confirmed rules.

## Evaluation

- Assign rubric level `L4`–`L0` or valid `N/A` to each applicable criterion.
- Record concise evidence for each level.
- Record critical failures separately.
- Calculate the score using `EVAL-SCORING-001` or the deterministic evaluation script when applicable.
- Do not modify criterion levels merely to make a platform pass.

## Benchmark Eligibility

Mark the result baseline-eligible only when:

- score is at least 85;
- result is PASS;
- critical failures are empty;
- execution metadata is complete;
- raw output and evaluation evidence are retained;
- controlled input/configuration was preserved.

## After All Platforms

- Compare criterion-level outcomes, not wording alone.
- Record material platform differences.
- Distinguish harmless formatting differences from QA-AI contract differences.
- Do not claim cross-platform equivalence when a quality-impacting difference remains unresolved.
- Approve baseline records only after review.