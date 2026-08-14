# Claude Workflow Mapping

| Workflow | Claude Code Behavior |
|---|---|
| `testcase-generation` | Read `workflows/testcase-generation/README.md`, then resolve each owning skill and required shared resources |
| `testcase-quality-review` | Read `workflows/testcase-quality-review/README.md` and use `coverage-reviewer` against authoritative coverage sources |
| `regression-analysis` | Read `workflows/regression-analysis/README.md` and use `regression-impact` with authoritative change context plus baseline evidence |

Workflow files own orchestration. Skill files own capability logic. Claude Code must preserve that separation.
