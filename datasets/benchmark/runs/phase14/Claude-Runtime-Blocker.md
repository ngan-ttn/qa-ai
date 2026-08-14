# Phase 14 Claude Runtime Blocker

## Status

`Open — runtime connectivity unavailable`

## Affected Stage

- 14.2 Controlled Runtime Execution
- downstream completion of 14.3, 14.4, 14.5, and 14.6

## Required Run

- Run ID: `P14-RUN-CLAUDE-001`
- Run Set: `P14-RUNSET-001`
- Dataset: `REQ-AUTH-001`
- Prompt: `datasets/benchmark/runs/phase14/Runtime-Execution-Prompt.md`
- Adapter: repository-root `CLAUDE.md` / Claude Code integration

## Observed Condition

The Claude runtime is currently not connected/available in the operator environment. No controlled Claude runtime output has been captured for Phase 14.

## Evaluation Treatment

This condition is a runtime availability blocker, not a measured QA-AI quality failure.

Do not:

- assign Claude a synthetic score;
- mark Claude PASS or FAIL;
- infer Claude output from ChatGPT or Cursor;
- use a previous unrelated Claude conversation as Phase 14 evidence;
- approve the three-platform cross-platform baseline without the actual controlled run.

## Unblock Condition

The blocker is resolved only when Claude can execute the exact controlled Phase 14 prompt under the active QA-AI repository instructions and the full raw output can be captured unchanged.

After execution, create the same evidence set used by the other accepted platforms:

```text
records/claude/
├── Raw-Output.md
├── Execution-Metadata.json
├── Scoring-Input.json
├── Evaluation-Result.json
└── Baseline-Candidate.json   # only if evaluation passes eligibility rules
```

## Current Impact

ChatGPT and Cursor candidate evidence may continue to be prepared and reviewed while this blocker is open. Phase 14 must remain In Progress and the final cross-platform baseline/freeze gate must remain unapproved.
