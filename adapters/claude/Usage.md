# Claude Adapter Usage

## Installation

Phase 13 validates Claude Code directly against the QA-AI repository.

From the QA-AI repository root, copy the adapter instruction file to the root location Claude Code loads as project memory:

```text
copy adapters\claude\CLAUDE.md CLAUDE.md
```

Equivalent shell/file-copy commands may be used on other operating systems.

Do not copy only this adapter into an unrelated repository unless the canonical QA-AI core paths are also exposed under a separately validated path contract.

## Runtime

Start Claude Code from the QA-AI repository root and provide the authoritative project requirement or artifact to analyze. Project input may be pasted into the session or provided through files accessible to the runtime.

Claude should read the specific owning workflow/skill contract required for the task and then load only applicable shared resources rather than reading the entire repository by default.

## Validation

Confirm that Claude Code:

- loads the repository-root `CLAUDE.md` (the `/memory` view can be used to inspect loaded project memory);
- resolves the canonical repository references used by the instructions;
- routes each QA objective to the correct skill;
- follows canonical workflow order for multi-step tasks;
- uses project requirements as authority;
- does not duplicate or rewrite skill behavior inside the adapter;
- can execute applicable deterministic validation scripts when changing QA-AI repository content.

Recommended smoke prompts should cover requirement analysis, testcase generation, testcase quality review, regression impact, and one specialized API/SQL task.

## Maintenance

When a canonical skill/workflow path or contract changes, update mappings and revalidate imports/references. Keep `CLAUDE.md` concise; do not mirror the entire knowledge library into project memory instructions.
