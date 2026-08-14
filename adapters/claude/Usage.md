# Claude Adapter Usage

## Installation

Use `adapters/claude/CLAUDE.md` as the project instruction source. For a target repository, copy or adapt its contents into the repository-root `CLAUDE.md`, preserving the referenced QA-AI paths available to that runtime.

## Runtime

Start Claude Code in the repository and provide the project requirement or artifact to analyze. Claude should read the specific workflow/skill contract required for the task and then load only applicable shared resources.

## Validation

Confirm that Claude Code:

- detects project instructions;
- routes each QA objective to the correct skill;
- follows canonical workflow order for multi-step tasks;
- uses project requirements as authority;
- does not duplicate or rewrite skill behavior inside the adapter;
- can execute applicable deterministic validation scripts when changing QA-AI repository content.

## Maintenance

When a canonical skill/workflow path or contract changes, update mappings and revalidate imports/references. Keep `CLAUDE.md` concise; do not mirror the entire knowledge library into memory instructions.
