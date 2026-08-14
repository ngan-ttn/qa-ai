# Cursor Adapter Usage

## Installation

Phase 13 validates Cursor directly against the QA-AI repository.

Copy the contents of `adapters/cursor/package/.cursor/` into the QA-AI repository root `.cursor/` directory.

Result:

```text
<qa-ai-repository>/
├── skills/
├── workflows/
├── shared/
├── scripts/
└── .cursor/
    ├── rules/
    └── commands/
```

Do not copy only `.cursor/` into an unrelated repository: the packaged rules and commands use canonical QA-AI root paths and require the QA-AI core to be available in the same supported topology.

## Runtime

Open the QA-AI repository in Cursor and use Agent/Chat. Project Rules provide persistent QA-AI routing and grounding guidance. Reusable commands provide explicit entry points for common QA workflows.

Authoritative project requirements may be pasted into the conversation or provided through files accessible in the workspace/runtime. They remain higher authority than reusable QA-AI knowledge.

## Validation

Confirm that:

- Cursor detects both QA-AI Project Rules;
- commands appear when `/` is invoked in Chat;
- skill/workflow references resolve to canonical repository paths;
- authoritative requirements override generic knowledge;
- missing information remains explicit;
- repository changes can run applicable deterministic validators in `scripts/`;
- one direct skill task, one multi-skill workflow, one review workflow, one regression workflow, and one specialized API/SQL request route correctly.

## Maintenance

Keep rules focused and composable. When canonical skill/workflow contracts change, update mappings and commands rather than copying the changed logic into rule files. Revalidate the installed `.cursor/` package after any path or contract change.
