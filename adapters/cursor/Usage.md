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

For revision-aware work where Change Intelligence recommends `Regenerate`, Cursor must read the prior canonical artifact baseline and applicable change/impact evidence from the repository before regenerating. `Regenerate` means baseline-preserving evolution, not fresh reconstruction from the target requirement alone. Preserve stable semantic IDs, and reconcile Preserved/Modified/Added/Removed IDs according to `shared/standards/Change-Intelligence.md` and the owning workflow. If the expected prior baseline cannot be resolved, block incremental regeneration rather than silently falling back to fresh generation.

## Validation

Confirm that:

- Cursor detects both QA-AI Project Rules;
- commands appear when `/` is invoked in Chat;
- skill/workflow references resolve to canonical repository paths;
- authoritative requirements override generic knowledge;
- missing information remains explicit;
- incremental regeneration reads the prior canonical baseline and preserves unchanged semantic IDs;
- repository changes can run applicable deterministic validators in `scripts/`;
- one direct skill task, one multi-skill workflow, one review workflow, one regression workflow, and one specialized API/SQL request route correctly.

## Maintenance

Keep rules focused and composable. When canonical skill/workflow contracts change, update mappings and commands rather than copying the changed logic into rule files. Revalidate the installed `.cursor/` package after any path or contract change.
