# Execution Standard

## Purpose

This standard defines the canonical QA-AI model for test execution runs, execution results, defect linkage, evidence, retest history, current disposition, execution summaries, and provenance.

Execution records are operational evidence. They do not redefine canonical requirements, test cases, expected results, defect policy, or external defect workflow.

---

## Canonical Execution Statuses

Only these result statuses are canonical:

- `Pass`
- `Fail`
- `Blocked`
- `Not Run`
- `Not Applicable`

`Blocked` means reliable execution cannot complete because a dependency, environment, test-data, access, or authoritative-oracle problem prevents a valid result. It is not equivalent to `Fail`.

`Not Run` means the testcase is in scope but has not been executed. `Not Applicable` is an explicit disposition that the testcase does not apply to the current execution context.

---

## Execution Run Lifecycle

```text
Planned → In Progress → Completed → Closed
```

- `Planned` — run created; no testcase result has yet been executed.
- `In Progress` — at least one scoped testcase has an execution attempt.
- `Completed` — every scoped testcase has a current disposition other than `Not Run`.
- `Closed` — completed run finalized for audit; historical results must not be destructively rewritten.

Run lifecycle is independent of canonical artifact lifecycle.

---

## Execution Run

An execution run must preserve:

- stable `RUN-*` identity;
- feature revision;
- testcase artifact path, checksum, revision/freshness when known;
- execution scope type and scoped testcase IDs;
- optional regression source/tier provenance;
- build/version and environment;
- executor;
- timestamps;
- lifecycle state;
- explicit stale/unknown-source override reason when used.

Supported scope types are:

- `Full Test Suite`
- `Minimum / Release-Gate Regression`
- `Recommended Regression`
- `Full Changed-Feature Verification`
- `Custom`

Execution scope must be based on actual testcase IDs. A reported scope count must reconcile with unique scoped IDs.

---

## Execution Result

Each attempt is an immutable historical record with a stable `ER-*` identity and must reference one scoped testcase.

A result records, where applicable:

- testcase ID;
- status;
- actual result;
- executor and timestamp;
- environment/build snapshot;
- evidence references;
- defect references;
- notes;
- `retest_of` for retest attempts;
- blocker type/reason for `Blocked`.

The authoritative expected result remains in the referenced testcase artifact. Execution data must not silently replace it.

---

## Blocked Result Requirements

A `Blocked` result requires both a blocker type and a blocker reason.

Canonical blocker types:

- `Environment`
- `Test Data`
- `Access`
- `Dependency`
- `Requirement / Oracle`
- `Other`

Unresolved expected behavior without an authoritative oracle must not be reported as `Fail`; use `Blocked` when it prevents reliable execution.

---

## Retest and History

Retest never overwrites an earlier result.

```text
ER-0001  TC-001  Fail
ER-0042  TC-001  Pass  retest_of=ER-0001
```

`retest_of` must reference an earlier result for the same testcase. The full attempt chain is preserved.

The current disposition for a testcase is the latest valid attempt in that run. Execution summaries use current dispositions, not the total number of attempts.

---

## Defect Linkage

Phase 18 owns only traceable linkage between execution evidence and defect references.

A defect reference may preserve:

- local `BUG-*` identity;
- optional external ID;
- title;
- source execution-result IDs;
- external status snapshot when supplied;
- optional URL/reference.

QA-AI does not own the external defect state machine, assignment, triage decision, or root-cause conclusion.

`bug-report-reviewer` may review bug-report quality, but does not manage defect lifecycle.

---

## Evidence

Evidence is referenced by path; binary content is not embedded in canonical JSON records.

Baseline evidence types:

- `screenshot`
- `video`
- `log`
- `request-response`
- `database`
- `other`

Each evidence record should contain stable identity, type, relative path, and description where useful.

---

## Freshness Guard

Execution should normally use a `Current` testcase artifact.

- `Current` — normal run creation.
- `Unknown` — explicit warning/override may be accepted with reason.
- `Stale` — blocked by default; only explicit `--allow-stale` plus a reason may create the run.

The override is evidence, not a freshness change.

---

## Summary Reconciliation

For a run:

```text
Pass + Fail + Blocked + Not Run + Not Applicable
= unique scoped testcase IDs
```

Retest attempts do not increase the scope count.

All reported status totals must reconcile with actual current dispositions.

---

## Storage

Canonical Phase 18 operational storage under a feature workspace:

```text
executions/
└── RUN-001/
    ├── execution.json
    ├── results.json
    ├── defects.json
    ├── Execution-Summary.md
    └── evidence/
```

`execution.json`, `results.json`, and `defects.json` are the structured source records. `Execution-Summary.md` is derived and may be regenerated.

---

## Boundaries

This standard does not define:

- test automation runners;
- automatic Pass/Fail inference;
- Jira/AIO/TestRail API synchronization;
- automatic defect creation;
- external defect workflow policy;
- defect assignment;
- root-cause analysis automation;
- release decisions.

---

## Validation

Execution validation must check at minimum:

- valid run/result/status identities;
- scoped testcase uniqueness and existence in the referenced testcase artifact;
- checksum/provenance consistency;
- legal lifecycle state;
- required blocker reason/type;
- unique result IDs;
- valid retest chains for the same testcase;
- defect references to existing execution results;
- current-disposition determinism;
- aggregate count reconciliation;
- Closed runs are not silently mutated.
