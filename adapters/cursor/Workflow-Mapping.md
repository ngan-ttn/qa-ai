# Cursor Workflow Mapping

| Workflow | Cursor Runtime Behavior |
|---|---|
| `testcase-generation` | Use the canonical workflow README, then invoke the required skills in order |
| `testcase-quality-review` | Use the canonical workflow README and `coverage-reviewer` against authoritative sources |
| `regression-analysis` | Use the canonical workflow README and `regression-impact` with authoritative change context plus baseline evidence |

Project commands under `package/.cursor/commands/` are convenience entry points. They must delegate to the canonical workflow and skill files rather than embed a second copy of workflow logic.
