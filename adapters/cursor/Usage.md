# Cursor Adapter Usage

## Installation

Copy the contents of `adapters/cursor/package/.cursor/` into the target repository root `.cursor/` directory.

Result:

```text
<target-repo>/
└── .cursor/
    ├── rules/
    └── commands/
```

## Runtime

Use Cursor Agent/Chat in the repository. Project rules provide persistent QA-AI routing and grounding guidance. Reusable commands provide explicit entry points for common QA workflows.

## Validation

Confirm that:

- Cursor detects the QA-AI project rules;
- commands appear in the command list;
- skill/workflow references resolve to canonical repository paths;
- authoritative requirements override generic knowledge;
- missing information remains explicit;
- repository changes can run the applicable deterministic validators in `scripts/`.

## Maintenance

Keep rules focused and composable. When canonical skill/workflow contracts change, update mappings and commands rather than copying the changed logic into rule files.
