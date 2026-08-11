# Test Scenarios — Account Lockout After Failed Login Attempts

## Golden Output Metadata

- Dataset ID: `REQ-AUTH-001`
- Source Requirement: `datasets/requirements/simple/REQ-AUTH-001.md`
- Artifact Type: `Test Scenarios`
- Review Status: `Approved`
- Evaluation Purpose: Reference output for evaluating scenario coverage, boundary analysis, state-transition coverage, sequence behavior, risk-based prioritization, traceability, and assumption control

---

## Scenario Scope

The scenario set validates the confirmed behavior of the account-lockout feature across:

- Normal authentication before lock
- Failed-attempt tracking
- Account-level isolation
- Failed-attempt threshold boundaries
- Successful-login counter reset
- Active locked-state enforcement
- Lock-duration boundaries
- Automatic unlock
- Post-unlock counter reset
- New consecutive failure sequences

Each confirmed scenario verifies one primary objective.

Detailed execution steps and concrete test data belong to downstream test-case and test-data artifacts.

Behavior not defined by the source requirement is separated into clarification-dependent candidates and is not assigned a confirmed expected result.

---

## Coverage Strategy

| Test Perspective | Application |
|---|---|
| Positive Testing | Successful authentication and post-unlock recovery |
| Negative Testing | Incorrect-password attempts and authentication while locked |
| Boundary Value Analysis | Failed attempts 1, 4, and 5; 15-minute lock boundary |
| State Transition Testing | `Unlocked → Locked → Unlocked` |
| Sequence Testing | Consecutive failures, reset, and new sequences |
| Isolation Testing | Independent failed-attempt tracking between accounts |
| Risk-Based Testing | Security-sensitive threshold, lock, timer, reset, and isolation behavior |

---

## Scenario Summary

| Scenario ID | Area | Scenario | Coverage Type | Priority | Primary Traceability |
|---|---|---|---|---|---|
| TS-AUTH-001 | Authentication | Verify an unlocked account can authenticate successfully using the correct password. | Positive | Medium | AC-08, BR-AUTH-011 |
| TS-AUTH-002 | Failed Attempt Tracking | Verify an incorrect password increments the failed-attempt counter for the corresponding account. | Functional / Negative | High | AC-01, BR-AUTH-001, BR-AUTH-002 |
| TS-AUTH-003 | Threshold | Verify the account remains unlocked after the first consecutive failed login attempt. | Boundary | High | AC-02, BR-AUTH-003 |
| TS-AUTH-004 | Threshold | Verify the account remains unlocked after four consecutive failed login attempts. | Boundary | High | AC-02, BR-AUTH-003, RISK-AUTH-001 |
| TS-AUTH-005 | Threshold / Lock | Verify the fifth consecutive failed login attempt locks the account. | Boundary / State Transition | High | AC-03, BR-AUTH-004, RISK-AUTH-002 |
| TS-AUTH-006 | Lock Timing | Verify the 15-minute lock duration starts when the fifth consecutive failed attempt is recorded. | Time Boundary | High | AC-04, BR-AUTH-005, BR-AUTH-006, RISK-AUTH-009 |
| TS-AUTH-007 | Locked State | Verify the correct password cannot authenticate while the account is locked. | Negative / State | High | AC-05, BR-AUTH-007, BR-AUTH-008, RISK-AUTH-003 |
| TS-AUTH-008 | Locked State | Verify an incorrect-password login attempt is rejected while the account is locked. | Negative / State | High | AC-05, BR-AUTH-007 |
| TS-AUTH-009 | Lock Duration | Verify the account remains locked before the 15-minute lock duration expires. | Time Boundary | High | AC-05, AC-06, BR-AUTH-005, RISK-AUTH-007 |
| TS-AUTH-010 | Automatic Unlock | Verify the account automatically unlocks when the 15-minute lock duration expires. | Time Boundary / State Transition | High | AC-06, BR-AUTH-009, RISK-AUTH-008 |
| TS-AUTH-011 | Automatic Unlock | Verify automatic unlock resets the failed-attempt counter to zero. | State / Data | High | AC-07, BR-AUTH-010, RISK-AUTH-006 |
| TS-AUTH-012 | Counter Reset | Verify a successful login after one failed attempt resets the failed-attempt counter. | Sequence | High | AC-08, BR-AUTH-011 |
| TS-AUTH-013 | Counter Reset | Verify a successful login after four consecutive failed attempts resets the counter before the lock threshold is reached. | Boundary / Sequence | High | AC-08, BR-AUTH-011, RISK-AUTH-005 |
| TS-AUTH-014 | Consecutive Sequence | Verify failed attempts before and after a successful login are treated as separate consecutive sequences. | Sequence | High | AC-08, AC-09, BR-AUTH-011, BR-AUTH-012, RISK-AUTH-010 |
| TS-AUTH-015 | Account Isolation | Verify failed-attempt tracking for one account does not affect another account. | Isolation | High | AC-01, BR-AUTH-001, RISK-AUTH-004 |
| TS-AUTH-016 | Post-Unlock Sequence | Verify the first failed login attempt after automatic unlock starts a new consecutive sequence at one. | State / Sequence | High | AC-07, AC-09, BR-AUTH-010, BR-AUTH-012, RISK-AUTH-006 |
| TS-AUTH-017 | Repeated Lifecycle | Verify an automatically unlocked account becomes locked again only after five new consecutive failed login attempts. | State Transition / Boundary / Sequence | High | AC-02, AC-03, AC-06, AC-07, AC-09 |

---

## Confirmed Test Scenarios

### TS-AUTH-001 — Successful Authentication While Unlocked

**Objective**

Verify normal password-based authentication remains available when the account is unlocked and the correct password is submitted.

**Expected Behavior**

Authentication succeeds.

If a failed-attempt sequence exists below the lock threshold, the successful login resets that sequence according to BR-AUTH-011.

**Priority**

Medium

**Traceability**

- AC-08
- BR-AUTH-011

---

### TS-AUTH-002 — Increment Failed-Attempt Counter for Corresponding Account

**Objective**

Verify one incorrect-password attempt increments the failed-attempt counter for the account receiving the attempt.

**Expected Behavior**

- Authentication is rejected.
- The corresponding account's failed-attempt counter increases by one.
- No other account's failed-attempt counter is affected.

**Priority**

High

**Traceability**

- AC-01
- BR-AUTH-001
- BR-AUTH-002
- RISK-AUTH-004

---

### TS-AUTH-003 — First Failure Remains Below Lock Threshold

**Objective**

Verify the account remains unlocked after the first consecutive failed login attempt.

**Expected Behavior**

- Failed-attempt counter = `1`
- Account state = `Unlocked`

**Priority**

High

**Traceability**

- AC-01
- AC-02
- BR-AUTH-002
- BR-AUTH-003

---

### TS-AUTH-004 — Fourth Failure Remains Below Lock Threshold

**Objective**

Verify the account remains unlocked at the highest failed-attempt count below the lock threshold.

**Expected Behavior**

- Failed-attempt counter = `4`
- Account state = `Unlocked`

**Priority**

High

**Traceability**

- AC-02
- BR-AUTH-003
- RISK-AUTH-001
- RISK-AUTH-010

---

### TS-AUTH-005 — Fifth Failure Triggers Account Lock

**Objective**

Verify the exact transition from four to five consecutive failed login attempts.

**Expected Behavior**

After the fifth consecutive incorrect-password attempt is recorded:

- Failed-attempt counter reaches `5`.
- Account transitions from `Unlocked` to `Locked`.

**Priority**

High

**Traceability**

- AC-03
- BR-AUTH-004
- RISK-AUTH-001
- RISK-AUTH-002
- RISK-AUTH-010

---

### TS-AUTH-006 — Lock Duration Starts at Fifth Recorded Failure

**Objective**

Verify the defined 15-minute lock duration begins from the recorded fifth consecutive failed login attempt.

**Expected Behavior**

The lock-period start point corresponds to the time the fifth consecutive failed attempt is recorded.

The scenario does not prescribe how the timer is technically stored or processed.

**Priority**

High

**Traceability**

- AC-04
- BR-AUTH-005
- BR-AUTH-006
- RISK-AUTH-009

---

### TS-AUTH-007 — Correct Password Is Rejected While Locked

**Objective**

Verify valid credentials cannot bypass an active account lock.

**Expected Behavior**

When:

- Account state = `Locked`
- Password = Correct
- Lock duration has not expired

authentication is rejected.

**Priority**

High

**Traceability**

- AC-05
- BR-AUTH-007
- BR-AUTH-008
- RISK-AUTH-003

---

### TS-AUTH-008 — Incorrect Password Is Rejected While Locked

**Objective**

Verify an incorrect-password login attempt is rejected while the account remains locked.

**Expected Behavior**

Authentication is rejected.

This scenario does not assert whether the locked-state attempt:

- Changes the failed-attempt counter
- Restarts the lock duration
- Extends the lock duration

because those behaviors are not defined by the source requirement.

**Priority**

High

**Traceability**

- AC-05
- BR-AUTH-007
- RISK-AUTH-011

---

### TS-AUTH-009 — Account Remains Locked Before Expiry

**Objective**

Verify the account remains locked before the full 15-minute lock duration has expired.

**Expected Behavior**

Before expiry:

- Account remains `Locked`.
- Password-based authentication remains rejected.

**Priority**

High

**Traceability**

- AC-05
- AC-06
- BR-AUTH-005
- BR-AUTH-007
- BR-AUTH-009
- RISK-AUTH-007

---

### TS-AUTH-010 — Automatic Unlock at Lock Expiry

**Objective**

Verify the account automatically transitions to the unlocked state when the defined 15-minute duration expires.

**Expected Behavior**

When the 15-minute lock duration expires:

- Account transitions from `Locked` to `Unlocked`.
- No administrative action is required by the defined flow.

**Priority**

High

**Traceability**

- AC-06
- BR-AUTH-005
- BR-AUTH-009
- RISK-AUTH-007
- RISK-AUTH-008
- RISK-AUTH-009

---

### TS-AUTH-011 — Counter Reset on Automatic Unlock

**Objective**

Verify automatic unlock resets the failed-attempt counter.

**Expected Behavior**

After automatic unlock:

- Account state = `Unlocked`
- Failed-attempt counter = `0`

**Priority**

High

**Traceability**

- AC-07
- BR-AUTH-010
- RISK-AUTH-006

---

### TS-AUTH-012 — Successful Login Resets Counter After One Failure

**Objective**

Verify successful authentication interrupts an early failed-login sequence.

**Sequence**

`1 failed attempt → successful login`

**Expected Behavior**

After the successful login:

- Failed-attempt counter = `0`
- Previous failure does not contribute to a later sequence.

**Priority**

High

**Traceability**

- AC-08
- BR-AUTH-011
- BR-AUTH-012

---

### TS-AUTH-013 — Successful Login Resets Counter Immediately Below Threshold

**Objective**

Verify successful authentication after four consecutive failures prevents those failures from contributing to a later lock.

**Sequence**

`4 consecutive failures → successful login`

**Expected Behavior**

- Authentication succeeds.
- Failed-attempt counter resets to `0`.
- Account does not become locked from the previous four failures.

**Priority**

High

**Traceability**

- AC-08
- BR-AUTH-011
- BR-AUTH-012
- RISK-AUTH-005
- RISK-AUTH-010

---

### TS-AUTH-014 — Failures Across a Successful Login Are Not Consecutive

**Objective**

Verify the lock threshold is based on consecutive failures rather than cumulative historical failures.

**Sequence Example**

`3 failures → successful login → 2 failures`

**Expected Behavior**

The final state represents two consecutive failures after the reset, not five consecutive failures.

The account remains unlocked.

**Priority**

High

**Traceability**

- AC-02
- AC-08
- AC-09
- BR-AUTH-003
- BR-AUTH-011
- BR-AUTH-012
- RISK-AUTH-005
- RISK-AUTH-010

---

### TS-AUTH-015 — Failed-Attempt Tracking Is Isolated Per Account

**Objective**

Verify failed login activity for Account A does not change the failed-attempt state of Account B.

**Expected Behavior**

Each account maintains its own independent consecutive failed-attempt sequence.

Example:

- Account A = `4` consecutive failures
- Account B receives its first incorrect-password attempt

Account B is treated as having `1` consecutive failure, not `5`.

**Priority**

High

**Traceability**

- AC-01
- BR-AUTH-001
- BR-AUTH-002
- RISK-AUTH-004

---

### TS-AUTH-016 — First Failure After Automatic Unlock Starts at One

**Objective**

Verify a failed login after automatic unlock begins a new consecutive sequence.

**Expected Behavior**

After automatic unlock and counter reset:

- Next incorrect-password attempt is rejected.
- Failed-attempt counter becomes `1`.
- Account remains unlocked.

**Priority**

High

**Traceability**

- AC-01
- AC-02
- AC-07
- AC-09
- BR-AUTH-002
- BR-AUTH-003
- BR-AUTH-010
- BR-AUTH-012
- RISK-AUTH-006

---

### TS-AUTH-017 — Repeated Lock Lifecycle After Automatic Unlock

**Objective**

Verify an account that has automatically unlocked can start a completely new failure sequence and reach the lock threshold again.

**Sequence**

- Previous lock expires.
- Counter resets to zero.
- New failures 1–4 occur.
- Account remains unlocked.
- Fifth new consecutive failure occurs.

**Expected Behavior**

The account becomes locked again only when the fifth failure of the new sequence is recorded.

**Priority**

High

**Traceability**

- AC-02
- AC-03
- AC-06
- AC-07
- AC-09
- BR-AUTH-003
- BR-AUTH-004
- BR-AUTH-009
- BR-AUTH-010
- BR-AUTH-012
- RISK-AUTH-002
- RISK-AUTH-006
- RISK-AUTH-010

---

## Clarification-Dependent Scenario Candidates

The following areas are relevant to QA analysis but do not have sufficient source-defined behavior to become confirmed test scenarios with deterministic expected results.

| Candidate ID | Area | Scenario Candidate | Missing Definition |
|---|---|---|---|
| CTS-AUTH-001 | Locked State | Verify whether a login attempt during active lock changes the failed-attempt counter. | Locked-attempt counter behavior |
| CTS-AUTH-002 | Lock Timing | Verify whether a login attempt during active lock restarts or extends the timer. | Locked-attempt timer behavior |
| CTS-AUTH-003 | Concurrency | Verify simultaneous failed login attempts when the account is immediately below the threshold. | Concurrent request semantics |
| CTS-AUTH-004 | User Feedback | Verify the user-facing message for a locked account. | Message requirement |
| CTS-AUTH-005 | Administrative Flow | Verify manual or administrative unlock behavior. | Administrative unlock requirement |
| CTS-AUTH-006 | Authentication Scope | Verify whether non-password authentication methods are affected by the lock. | Alternative authentication behavior |

These candidates must not be converted into confirmed expected behavior until the missing rules are defined.

---

## Acceptance Criteria Coverage

| Source Acceptance Criterion | Confirmed Scenario Coverage |
|---|---|
| AC-01 — Incorrect password increments the corresponding account counter | TS-AUTH-002, TS-AUTH-003, TS-AUTH-015, TS-AUTH-016 |
| AC-02 — Account remains unlocked after failures 1–4 | TS-AUTH-003, TS-AUTH-004, TS-AUTH-014, TS-AUTH-016, TS-AUTH-017 |
| AC-03 — Fifth consecutive failure locks the account | TS-AUTH-005, TS-AUTH-017 |
| AC-04 — Lock duration starts when the fifth failure is recorded | TS-AUTH-006 |
| AC-05 — All password-based attempts are rejected while locked | TS-AUTH-007, TS-AUTH-008, TS-AUTH-009 |
| AC-06 — Account automatically unlocks after 15 minutes | TS-AUTH-009, TS-AUTH-010 |
| AC-07 — Automatic unlock resets the counter | TS-AUTH-011, TS-AUTH-016, TS-AUTH-017 |
| AC-08 — Successful login before lock resets the counter | TS-AUTH-001, TS-AUTH-012, TS-AUTH-013, TS-AUTH-014 |
| AC-09 — Next failed attempt after reset starts a new sequence at one | TS-AUTH-012, TS-AUTH-013, TS-AUTH-014, TS-AUTH-016, TS-AUTH-017 |

All nine source acceptance criteria have confirmed scenario coverage.

---

## Business Rule Coverage

| Business Rule | Confirmed Scenario Coverage |
|---|---|
| BR-AUTH-001 | TS-AUTH-002, TS-AUTH-015 |
| BR-AUTH-002 | TS-AUTH-002, TS-AUTH-003, TS-AUTH-015, TS-AUTH-016 |
| BR-AUTH-003 | TS-AUTH-003, TS-AUTH-004, TS-AUTH-014, TS-AUTH-016, TS-AUTH-017 |
| BR-AUTH-004 | TS-AUTH-005, TS-AUTH-017 |
| BR-AUTH-005 | TS-AUTH-006, TS-AUTH-009, TS-AUTH-010 |
| BR-AUTH-006 | TS-AUTH-006 |
| BR-AUTH-007 | TS-AUTH-007, TS-AUTH-008, TS-AUTH-009 |
| BR-AUTH-008 | TS-AUTH-007 |
| BR-AUTH-009 | TS-AUTH-009, TS-AUTH-010, TS-AUTH-017 |
| BR-AUTH-010 | TS-AUTH-011, TS-AUTH-016, TS-AUTH-017 |
| BR-AUTH-011 | TS-AUTH-001, TS-AUTH-012, TS-AUTH-013, TS-AUTH-014 |
| BR-AUTH-012 | TS-AUTH-012, TS-AUTH-013, TS-AUTH-014, TS-AUTH-016, TS-AUTH-017 |

All confirmed business rules have scenario coverage.

---

## Risk Coverage

| Risk | Confirmed Scenario Coverage |
|---|---|
| RISK-AUTH-001 — Premature lock | TS-AUTH-004, TS-AUTH-005 |
| RISK-AUTH-002 — Missing lock at fifth failure | TS-AUTH-005, TS-AUTH-017 |
| RISK-AUTH-003 — Correct-password lock bypass | TS-AUTH-007 |
| RISK-AUTH-004 — Cross-account counter contamination | TS-AUTH-002, TS-AUTH-015 |
| RISK-AUTH-005 — Successful-login reset failure | TS-AUTH-013, TS-AUTH-014 |
| RISK-AUTH-006 — Counter carries over after automatic unlock | TS-AUTH-011, TS-AUTH-016, TS-AUTH-017 |
| RISK-AUTH-007 — Early unlock | TS-AUTH-009, TS-AUTH-010 |
| RISK-AUTH-008 — Missing or late automatic unlock | TS-AUTH-010 |
| RISK-AUTH-009 — Incorrect lock start time | TS-AUTH-006, TS-AUTH-010 |
| RISK-AUTH-010 — Incorrect consecutive-sequence calculation | TS-AUTH-004, TS-AUTH-005, TS-AUTH-014, TS-AUTH-017 |
| RISK-AUTH-011 — Undefined locked-attempt effects | CTS-AUTH-001, CTS-AUTH-002 |
| RISK-AUTH-012 — Concurrent threshold processing | CTS-AUTH-003 |

Confirmed risks with deterministic source-defined behavior are covered by confirmed scenarios.

Clarification-dependent risks remain explicitly separated.

---

## Coverage Summary

The confirmed scenario set provides coverage for:

- Normal unlocked authentication
- Per-account failure tracking
- Counter increment
- First-failure boundary
- Immediately-below-threshold boundary
- Exact lock threshold
- Lock-start timing
- Correct-password rejection while locked
- Incorrect-password rejection while locked
- Pre-expiry locked state
- Automatic unlock
- Automatic-unlock counter reset
- Successful-login counter reset
- Consecutive-sequence separation
- Account isolation
- Post-unlock sequence restart
- Repeated lock lifecycle

The scenario set intentionally does not define expected behavior for unspecified counter, timer, concurrency, administrative, messaging, or alternative-authentication behavior.

No confirmed scenario depends on a fabricated business rule.
