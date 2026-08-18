# Execution Tooling

Phase 18 deterministic tooling records execution evidence without inferring product behavior or replacing canonical Test Cases.

## Scripts

- `init_execution.py` — create a run from a testcase suite, custom scope, or canonical regression tier.
- `record_result.py` — append an immutable execution attempt.
- `link_defect.py` — link a local/external defect reference to an execution result.
- `record_retest.py` — append a retest attempt linked to a prior result.
- `summarize_execution.py` — derive current dispositions and `Execution-Summary.md`.
- `validate_execution.py` — validate scope, provenance, statuses, history, defects, retest chains, and aggregate reconciliation.

## Example

```bash
python scripts/execution/init_execution.py workspace/projects/demo/features/login --run-id RUN-001 --scope-type Custom --testcase-id TC-001 --testcase-id TC-002 --environment UAT --build 1.0.0 --executor qa
python scripts/execution/record_result.py workspace/projects/demo/features/login/executions/RUN-001 TC-001 Pass --actual-result "Login succeeds" --executed-by qa
python scripts/execution/record_result.py workspace/projects/demo/features/login/executions/RUN-001 TC-002 Fail --actual-result "Account remains unlocked" --executed-by qa
python scripts/execution/link_defect.py workspace/projects/demo/features/login/executions/RUN-001 ER-0002 BUG-001 --title "Account does not lock"
python scripts/execution/record_retest.py workspace/projects/demo/features/login/executions/RUN-001 ER-0002 Pass --actual-result "Account locks after fix" --executed-by qa
python scripts/execution/summarize_execution.py workspace/projects/demo/features/login/executions/RUN-001
python scripts/execution/validate_execution.py workspace/projects/demo/features/login/executions/RUN-001
```

A `Blocked` result requires `--blocker-type` and `--blocker-reason`. Run creation rejects stale testcase artifacts by default; `--allow-stale --reason "..."` is an explicit audited override.

See `shared/standards/Execution.md`.
