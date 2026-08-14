# ChatGPT Workflow Mapping

| Workflow | Runtime Behavior |
|---|---|
| `testcase-generation` | Follow canonical requirement → rule/risk → scenario → testcase orchestration and preserve artifact boundaries |
| `testcase-quality-review` | Review existing test artifacts against authoritative coverage sources using `coverage-reviewer` |
| `regression-analysis` | Consume authoritative change information plus baseline context and orchestrate `regression-impact` |

## Rule

When a workflow is selected, ChatGPT must follow the workflow README as the orchestration authority and each referenced skill README as the capability authority. Optional feedback paths must not become mandatory circular dependencies.
