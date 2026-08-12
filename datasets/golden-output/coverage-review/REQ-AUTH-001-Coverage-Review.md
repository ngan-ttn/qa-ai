# Coverage Review — Account Lockout After Failed Login Attempts

## Golden Output Metadata

- Dataset ID: `REQ-AUTH-001`
- Source Requirement: `datasets/requirements/simple/REQ-AUTH-001.md`
- Source Scenarios: `datasets/golden-output/test-scenarios/REQ-AUTH-001-Test-Scenarios.md`
- Source Test Cases: `datasets/golden-output/test-cases/REQ-AUTH-001-Test-Cases.md`
- Artifact Type: `Coverage Review`
- Review Status: `Approved`
- Evaluation Purpose: Reference output for evaluating requirement coverage, business-rule coverage, risk coverage, scenario-to-test-case traceability, duplicate detection, gap identification, assumption control, and release-readiness of QA artifacts

---

## Review Scope

This review evaluates whether the confirmed QA artifacts for `REQ-AUTH-001` provide sufficient and traceable coverage of the source requirement.

The review covers:

- Source Acceptance Criteria coverage
- Confirmed Business Rule coverage
- Identified Risk coverage
- Scenario-to-Test-Case coverage
- Boundary coverage
- State-transition coverage
- Sequence coverage
- Account-isolation coverage
- Clarification-dependent gaps
- Duplicate or redundant coverage
- Unsupported behavior leakage

This review evaluates coverage quality.

It does not execute the test cases or validate the implementation.

---

## Coverage Review Summary

| Review Area | Result |
|---|---|
| Acceptance Criteria Coverage | PASS |
| Business Rule Coverage | PASS |
| Risk Coverage | PASS |
| Scenario Coverage | PASS |
| Test Case Coverage | PASS |
| Boundary Coverage | PASS |
| State-Transition Coverage | PASS |
| Sequence Coverage | PASS |
| Account-Isolation Coverage | PASS |
| Assumption Control | PASS |
| Duplicate Coverage Control | PASS |
| Clarification-Dependent Separation | PASS |
| Unsupported Behavior Leakage | PASS |
| Overall Coverage Status | PASS |

No blocking coverage gap is identified in the confirmed behavior defined by the source requirement.

---

## Coverage Metrics

### Acceptance Criteria Coverage

- Total source acceptance criteria: `9`
- Acceptance criteria with confirmed scenario coverage: `9`
- Acceptance criteria with executable test-case coverage: `9`
- Uncovered acceptance criteria: `0`

Coverage:

`9 / 9 = 100%`

### Scenario Coverage

- Total confirmed test scenarios: `17`
- Confirmed scenarios with executable test-case coverage: `17`
- Confirmed scenarios without test-case coverage: `0`

Coverage:

`17 / 17 = 100%`

### Clarification-Dependent Candidates

- Total clarification-dependent scenario candidates: `6`
- Candidates intentionally excluded from confirmed executable coverage: `6`

These exclusions are valid because the source requirement does not define deterministic expected behavior for those areas.

---

## Acceptance Criteria Coverage Review

### AC-01 — Incorrect Password Increments the Corresponding Account Counter

**Confirmed Scenario Coverage**

- TS-AUTH-002
- TS-AUTH-003
- TS-AUTH-015
- TS-AUTH-016

**Executable Test Coverage**

- TC-AUTH-002
- TC-AUTH-003
- TC-AUTH-015
- TC-AUTH-016

**Coverage Assessment**

PASS

Coverage validates:

- Counter increment
- First failure behavior
- Per-account isolation
- Counter behavior after automatic unlock

No confirmed gap is identified.

---

### AC-02 — Account Remains Unlocked After Failures 1–4

**Confirmed Scenario Coverage**

- TS-AUTH-003
- TS-AUTH-004
- TS-AUTH-014
- TS-AUTH-016
- TS-AUTH-017

**Executable Test Coverage**

- TC-AUTH-003
- TC-AUTH-004
- TC-AUTH-014
- TC-AUTH-016
- TC-AUTH-017

**Coverage Assessment**

PASS

The key lower and upper boundaries below the threshold are covered:

- Failure count = `1`
- Failure count = `4`

Sequence-reset and repeated-lifecycle coverage also validate that historical failures are not incorrectly accumulated.

---

### AC-03 — Fifth Consecutive Failure Locks the Account

**Confirmed Scenario Coverage**

- TS-AUTH-005
- TS-AUTH-017

**Executable Test Coverage**

- TC-AUTH-005
- TC-AUTH-017

**Coverage Assessment**

PASS

The primary threshold transition and repeated lifecycle are both covered.

---

### AC-04 — Lock Duration Starts When the Fifth Failure Is Recorded

**Confirmed Scenario Coverage**

- TS-AUTH-006

**Executable Test Coverage**

- TC-AUTH-006

**Coverage Assessment**

PASS

The source-defined timer start point is covered without assuming an implementation-specific timer field or persistence mechanism.

---

### AC-05 — All Password-Based Attempts Are Rejected While Locked

**Confirmed Scenario Coverage**

- TS-AUTH-007
- TS-AUTH-008
- TS-AUTH-009

**Executable Test Coverage**

- TC-AUTH-007
- TC-AUTH-008
- TC-AUTH-009

**Coverage Assessment**

PASS

Coverage includes:

- Correct password while locked
- Incorrect password while locked
- Authentication before lock expiry

No expected behavior is invented for counter or timer side effects during the lock.

---

### AC-06 — Account Automatically Unlocks After Fifteen Minutes

**Confirmed Scenario Coverage**

- TS-AUTH-009
- TS-AUTH-010
- TS-AUTH-017

**Executable Test Coverage**

- TC-AUTH-009
- TC-AUTH-010
- TC-AUTH-017

**Coverage Assessment**

PASS

Both sides of the time boundary are covered:

- Before expiry → Locked
- After expiry → Unlocked

Repeated lifecycle confirms the account can return to the feature flow after automatic unlock.

---

### AC-07 — Automatic Unlock Resets the Counter

**Confirmed Scenario Coverage**

- TS-AUTH-011
- TS-AUTH-016
- TS-AUTH-017

**Executable Test Coverage**

- TC-AUTH-011
- TC-AUTH-016
- TC-AUTH-017

**Coverage Assessment**

PASS

Coverage validates both the reset itself and observable downstream behavior after the reset.

---

### AC-08 — Successful Login Before Lock Resets the Counter

**Confirmed Scenario Coverage**

- TS-AUTH-001
- TS-AUTH-012
- TS-AUTH-013
- TS-AUTH-014

**Executable Test Coverage**

- TC-AUTH-001
- TC-AUTH-012
- TC-AUTH-013
- TC-AUTH-014

**Coverage Assessment**

PASS

Coverage includes reset behavior:

- After one failed attempt
- Immediately below the lock threshold
- Across separated failure sequences

---

### AC-09 — Next Failed Attempt After Reset Starts at One

**Confirmed Scenario Coverage**

- TS-AUTH-012
- TS-AUTH-013
- TS-AUTH-014
- TS-AUTH-016
- TS-AUTH-017

**Executable Test Coverage**

- TC-AUTH-012
- TC-AUTH-013
- TC-AUTH-014
- TC-AUTH-016
- TC-AUTH-017

**Coverage Assessment**

PASS

Both reset paths are covered:

- Successful-login reset
- Automatic-unlock reset

---

## Business Rule Coverage Review

| Business Rule | Scenario Coverage | Test Case Coverage | Status |
|---|---|---|---|
| BR-AUTH-001 | TS-AUTH-002, TS-AUTH-015 | TC-AUTH-002, TC-AUTH-015 | PASS |
| BR-AUTH-002 | TS-AUTH-002, TS-AUTH-003, TS-AUTH-015, TS-AUTH-016 | TC-AUTH-002, TC-AUTH-003, TC-AUTH-015, TC-AUTH-016 | PASS |
| BR-AUTH-003 | TS-AUTH-003, TS-AUTH-004, TS-AUTH-014, TS-AUTH-016, TS-AUTH-017 | TC-AUTH-003, TC-AUTH-004, TC-AUTH-014, TC-AUTH-016, TC-AUTH-017 | PASS |
| BR-AUTH-004 | TS-AUTH-005, TS-AUTH-017 | TC-AUTH-005, TC-AUTH-017 | PASS |
| BR-AUTH-005 | TS-AUTH-006, TS-AUTH-009, TS-AUTH-010 | TC-AUTH-006, TC-AUTH-009, TC-AUTH-010 | PASS |
| BR-AUTH-006 | TS-AUTH-006 | TC-AUTH-006 | PASS |
| BR-AUTH-007 | TS-AUTH-007, TS-AUTH-008, TS-AUTH-009 | TC-AUTH-007, TC-AUTH-008, TC-AUTH-009 | PASS |
| BR-AUTH-008 | TS-AUTH-007 | TC-AUTH-007 | PASS |
| BR-AUTH-009 | TS-AUTH-009, TS-AUTH-010, TS-AUTH-017 | TC-AUTH-009, TC-AUTH-010, TC-AUTH-017 | PASS |
| BR-AUTH-010 | TS-AUTH-011, TS-AUTH-016, TS-AUTH-017 | TC-AUTH-011, TC-AUTH-016, TC-AUTH-017 | PASS |
| BR-AUTH-011 | TS-AUTH-001, TS-AUTH-012, TS-AUTH-013, TS-AUTH-014 | TC-AUTH-001, TC-AUTH-012, TC-AUTH-013, TC-AUTH-014 | PASS |
| BR-AUTH-012 | TS-AUTH-012, TS-AUTH-013, TS-AUTH-014, TS-AUTH-016, TS-AUTH-017 | TC-AUTH-012, TC-AUTH-013, TC-AUTH-014, TC-AUTH-016, TC-AUTH-017 | PASS |

All twelve confirmed business rules have scenario and executable test-case coverage.

---

## Risk Coverage Review

| Risk ID | Confirmed Coverage | Clarification-Dependent Coverage | Status |
|---|---|---|---|
| RISK-AUTH-001 | TS-AUTH-004, TS-AUTH-005 / TC-AUTH-004, TC-AUTH-005 | — | PASS |
| RISK-AUTH-002 | TS-AUTH-005, TS-AUTH-017 / TC-AUTH-005, TC-AUTH-017 | — | PASS |
| RISK-AUTH-003 | TS-AUTH-007 / TC-AUTH-007 | — | PASS |
| RISK-AUTH-004 | TS-AUTH-002, TS-AUTH-015 / TC-AUTH-002, TC-AUTH-015 | — | PASS |
| RISK-AUTH-005 | TS-AUTH-013, TS-AUTH-014 / TC-AUTH-013, TC-AUTH-014 | — | PASS |
| RISK-AUTH-006 | TS-AUTH-011, TS-AUTH-016, TS-AUTH-017 / TC-AUTH-011, TC-AUTH-016, TC-AUTH-017 | — | PASS |
| RISK-AUTH-007 | TS-AUTH-009, TS-AUTH-010 / TC-AUTH-009, TC-AUTH-010 | — | PASS |
| RISK-AUTH-008 | TS-AUTH-010 / TC-AUTH-010 | — | PASS |
| RISK-AUTH-009 | TS-AUTH-006, TS-AUTH-010 / TC-AUTH-006, TC-AUTH-010 | — | PASS |
| RISK-AUTH-010 | TS-AUTH-004, TS-AUTH-005, TS-AUTH-014, TS-AUTH-017 / corresponding test cases | — | PASS |
| RISK-AUTH-011 | — | CTS-AUTH-001, CTS-AUTH-002 | PASS — Deferred |
| RISK-AUTH-012 | — | CTS-AUTH-003 | PASS — Deferred |

The final two risks are not executable coverage gaps.

They are requirement-definition gaps and are correctly represented as clarification-dependent candidates rather than tests with fabricated expected results.

---

## Scenario-to-Test-Case Traceability Review

| Scenario | Test Case | Status |
|---|---|---|
| TS-AUTH-001 | TC-AUTH-001 | PASS |
| TS-AUTH-002 | TC-AUTH-002 | PASS |
| TS-AUTH-003 | TC-AUTH-003 | PASS |
| TS-AUTH-004 | TC-AUTH-004 | PASS |
| TS-AUTH-005 | TC-AUTH-005 | PASS |
| TS-AUTH-006 | TC-AUTH-006 | PASS |
| TS-AUTH-007 | TC-AUTH-007 | PASS |
| TS-AUTH-008 | TC-AUTH-008 | PASS |
| TS-AUTH-009 | TC-AUTH-009 | PASS |
| TS-AUTH-010 | TC-AUTH-010 | PASS |
| TS-AUTH-011 | TC-AUTH-011 | PASS |
| TS-AUTH-012 | TC-AUTH-012 | PASS |
| TS-AUTH-013 | TC-AUTH-013 | PASS |
| TS-AUTH-014 | TC-AUTH-014 | PASS |
| TS-AUTH-015 | TC-AUTH-015 | PASS |
| TS-AUTH-016 | TC-AUTH-016 | PASS |
| TS-AUTH-017 | TC-AUTH-017 | PASS |

Traceability coverage:

`17 / 17 = 100%`

No orphan confirmed scenario exists.

No executable test case lacks a source confirmed scenario.

---

## Boundary Coverage Review

### Failed-Attempt Boundary

| Boundary | Coverage | Status |
|---|---|---|
| Counter = 0 | Common preconditions and reset cases | PASS |
| Counter = 1 | TS/TC-AUTH-003, TS/TC-AUTH-016 | PASS |
| Counter = 4 | TS/TC-AUTH-004, TS/TC-AUTH-013 | PASS |
| Counter = 5 | TS/TC-AUTH-005, TS/TC-AUTH-017 | PASS |

The critical `4 → 5` transition is explicitly covered.

### Time Boundary

| Boundary | Coverage | Status |
|---|---|---|
| Lock start at fifth recorded failure | TS/TC-AUTH-006 | PASS |
| Before 15-minute expiry | TS/TC-AUTH-009 | PASS |
| After 15-minute expiry | TS/TC-AUTH-010 | PASS |

No implementation-specific timing tolerance is assumed.

---

## State-Transition Coverage Review

Confirmed state transitions are:

| From State | Trigger | To State | Coverage | Status |
|---|---|---|---|---|
| Unlocked | Failure count remains below 5 | Unlocked | TS/TC-AUTH-003, 004 | PASS |
| Unlocked | Successful login before lock | Unlocked with counter reset | TS/TC-AUTH-012, 013 | PASS |
| Unlocked | Fifth consecutive failure | Locked | TS/TC-AUTH-005 | PASS |
| Locked | Active lock login attempt | Locked | TS/TC-AUTH-007, 008, 009 | PASS |
| Locked | 15-minute duration expires | Unlocked | TS/TC-AUTH-010 | PASS |
| Unlocked after reset | New failed sequence | Unlocked, then potentially Locked | TS/TC-AUTH-016, 017 | PASS |

All confirmed state transitions have coverage.

---

## Sequence Coverage Review

The suite covers the key consecutive-failure sequences:

- `1 failure`
- `4 failures`
- `5 failures`
- `1 failure → successful login → reset`
- `4 failures → successful login → reset`
- `3 failures → successful login → 2 new failures`
- `automatic unlock → first new failure`
- `automatic unlock → five new failures → locked again`

**Result: PASS**

The suite distinguishes consecutive failures from cumulative historical failures.

---

## Isolation Coverage Review

Account-level isolation is covered by:

- TS-AUTH-002 / TC-AUTH-002
- TS-AUTH-015 / TC-AUTH-015

The suite verifies that failed-attempt state is maintained independently per account.

**Result: PASS**

---

## Duplicate Coverage Review

Some test cases exercise overlapping behavior, but the overlap is purposeful and not duplicate coverage.

Examples:

- TC-AUTH-004 validates the upper boundary below the lock threshold.
- TC-AUTH-013 uses the same counter value to validate reset behavior.
- TC-AUTH-005 validates the first lock transition.
- TC-AUTH-017 validates the same threshold after an automatic-unlock lifecycle.
- TC-AUTH-011 validates reset through observable post-unlock behavior.
- TC-AUTH-016 focuses specifically on the first failure of the new sequence.

These cases have different primary objectives and therefore should remain separate.

**Result: PASS — No redundant test case requires removal.**

---

## Clarification-Dependent Coverage Review

The following candidates are intentionally excluded from confirmed executable coverage:

| Candidate | Reason for Deferral |
|---|---|
| CTS-AUTH-001 | Counter behavior during active lock is undefined |
| CTS-AUTH-002 | Timer restart or extension behavior is undefined |
| CTS-AUTH-003 | Concurrent threshold-processing semantics are undefined |
| CTS-AUTH-004 | Locked-account message is undefined |
| CTS-AUTH-005 | Administrative unlock is outside defined scope |
| CTS-AUTH-006 | Alternative authentication methods are outside defined scope |

These are not considered coverage failures.

Generating deterministic expected results for these areas would introduce unsupported assumptions.

**Result: PASS**

---

## Unsupported Behavior Review

The confirmed scenario and test-case suites do not introduce requirements for:

- A specific locked-account message
- Counter increment while locked
- Timer restart while locked
- Timer extension while locked
- Administrative unlock
- Password reset interaction
- Multi-factor authentication
- Alternative authentication methods
- Database schema
- API contract
- Timer implementation
- Distributed locking behavior

**Result: PASS**

---

## Coverage Gaps

### Blocking Gaps

None.

### Confirmed Behavior Gaps

None.

### Clarification-Dependent Gaps

The following remain intentionally unresolved:

1. Counter behavior during active lock.
2. Lock-timer behavior for attempts during active lock.
3. Concurrent attempts near the lock threshold.
4. Locked-account user-facing message.
5. Administrative unlock behavior.
6. Alternative authentication behavior.

These gaps require additional product or system definition before deterministic test coverage can be added.

---

## Final Coverage Assessment

| Metric | Result |
|---|---|
| Acceptance Criteria Coverage | 100% |
| Confirmed Business Rule Coverage | 100% |
| Confirmed Scenario-to-Test-Case Coverage | 100% |
| Critical Boundary Coverage | Complete |
| Confirmed State-Transition Coverage | Complete |
| Sequence Coverage | Complete |
| Account-Isolation Coverage | Complete |
| Blocking Coverage Gaps | 0 |
| Unsupported Assumptions Introduced | 0 |
| Confirmed Orphan Scenarios | 0 |
| Confirmed Orphan Test Cases | 0 |

## Final Verdict

**PASS — Coverage is sufficient for all confirmed behavior in `REQ-AUTH-001`.**

The current scenario and test-case suites provide complete traceable coverage of the defined requirement while correctly deferring behaviors that lack deterministic source rules.

No additional confirmed scenario or test case is required before this golden set is frozen.
