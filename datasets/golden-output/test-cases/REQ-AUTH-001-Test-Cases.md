# Test Cases — Account Lockout After Failed Login Attempts

## Golden Output Metadata

- Dataset ID: `REQ-AUTH-001`
- Source Requirement: `datasets/requirements/simple/REQ-AUTH-001.md`
- Source Scenarios: `datasets/golden-output/test-scenarios/REQ-AUTH-001-Test-Scenarios.md`
- Artifact Type: `Test Cases`
- Review Status: `Approved`
- Evaluation Purpose: Reference output for evaluating test-case executability, scenario decomposition, boundary coverage, state-transition validation, traceability, expected-result precision, and assumption control

---

## Test Case Scope

This artifact contains executable test cases for all confirmed test scenarios of the account-lockout feature.

The test cases validate:

- Successful password authentication while unlocked
- Failed-attempt counter increments
- Threshold boundaries at attempts 1, 4, and 5
- Lock start timing
- Authentication rejection during active lock
- Lock expiry after 15 minutes
- Automatic counter reset
- Successful-login counter reset
- Consecutive-sequence behavior
- Per-account isolation
- Post-unlock failure tracking
- Repeated lock lifecycle

Behavior not defined by the requirement is not assigned an invented expected result.

---

## Common Test Data

Use the following logical test data.

| Test Data ID | Description |
|---|---|
| TD-AUTH-001 | Registered Account A in unlocked state with failed-attempt counter = 0 |
| TD-AUTH-002 | Registered Account B in unlocked state with failed-attempt counter = 0 |
| TD-AUTH-003 | Correct password for Account A |
| TD-AUTH-004 | Correct password for Account B |
| TD-AUTH-005 | Incorrect password that does not match Account A |
| TD-AUTH-006 | Incorrect password that does not match Account B |

Where a test requires a specific counter state, prepare that state through the login flow defined in the test rather than assuming direct database modification.

---

## Common Preconditions

Unless a test case states otherwise:

1. Username-and-password authentication is available.
2. The test account is registered and active.
3. The account begins in the `Unlocked` state.
4. The failed-attempt counter begins at `0`.
5. No active 15-minute lock exists for the account.
6. Test accounts are independent.

---

## TC-AUTH-001 — Successful Authentication While Account Is Unlocked

**Scenario**

TS-AUTH-001

**Objective**

Verify an unlocked registered account can authenticate using the correct password.

**Preconditions**

- Apply the common preconditions for Account A.

**Test Data**

- Account A
- Correct password for Account A

**Steps**

1. Open the password-based login flow.
2. Enter Account A's username.
3. Enter the correct password.
4. Submit the login request.

**Expected Result**

1. Authentication succeeds.
2. Account A remains unlocked.
3. Failed-attempt counter is `0`.

**Priority**

Medium

**Traceability**

- TS-AUTH-001
- AC-08
- BR-AUTH-011

---

## TC-AUTH-002 — Incorrect Password Increments Counter for Corresponding Account

**Scenario**

TS-AUTH-002

**Objective**

Verify one incorrect-password attempt increments only the corresponding account's failed-attempt counter.

**Preconditions**

- Apply the common preconditions for Account A.

**Test Data**

- Account A
- Incorrect password for Account A

**Steps**

1. Submit a login attempt for Account A using the incorrect password.
2. Observe the authentication result.
3. Verify the resulting failed-attempt state for Account A through subsequent observable login behavior or available test instrumentation.

**Expected Result**

1. Authentication is rejected.
2. Account A's failed-attempt counter becomes `1`.
3. Account A remains unlocked.

**Priority**

High

**Traceability**

- TS-AUTH-002
- AC-01
- BR-AUTH-001
- BR-AUTH-002
- RISK-AUTH-004

---

## TC-AUTH-003 — Account Remains Unlocked After First Consecutive Failure

**Scenario**

TS-AUTH-003

**Objective**

Verify the first consecutive failed login remains below the lock threshold.

**Preconditions**

- Apply the common preconditions for Account A.

**Test Data**

- Account A
- Incorrect password
- Correct password

**Steps**

1. Submit one incorrect-password login attempt for Account A.
2. Submit a second login attempt using the correct password.

**Expected Result**

1. The first attempt is rejected.
2. Failed-attempt counter becomes `1`.
3. Account A remains unlocked after the first failure.
4. The subsequent correct-password login is allowed.
5. Successful authentication resets the counter to `0`.

**Priority**

High

**Traceability**

- TS-AUTH-003
- AC-01
- AC-02
- BR-AUTH-002
- BR-AUTH-003

---

## TC-AUTH-004 — Account Remains Unlocked After Four Consecutive Failures

**Scenario**

TS-AUTH-004

**Objective**

Verify the account remains unlocked at the highest count below the lock threshold.

**Preconditions**

- Apply the common preconditions for Account A.

**Test Data**

- Account A
- Incorrect password
- Correct password

**Steps**

1. Submit four consecutive login attempts for Account A using the incorrect password.
2. Confirm each attempt is rejected.
3. Submit a fifth login request using the correct password.

**Expected Result**

1. Each of the four incorrect-password attempts is rejected.
2. Failed-attempt counter reaches `4`.
3. Account A remains unlocked after the fourth failure.
4. The correct-password login submitted before a fifth failure succeeds.
5. The successful login resets the counter to `0`.

**Priority**

High

**Traceability**

- TS-AUTH-004
- AC-02
- BR-AUTH-003
- RISK-AUTH-001
- RISK-AUTH-010

---

## TC-AUTH-005 — Fifth Consecutive Failure Locks the Account

**Scenario**

TS-AUTH-005

**Objective**

Verify the exact lock transition at the fifth consecutive failed login attempt.

**Preconditions**

- Apply the common preconditions for Account A.

**Test Data**

- Account A
- Incorrect password

**Steps**

1. Submit four consecutive incorrect-password login attempts for Account A.
2. Verify Account A remains unlocked.
3. Submit a fifth consecutive incorrect-password attempt.
4. Observe the account state after the fifth failure.

**Expected Result**

1. Attempts 1 through 4 are rejected and do not lock the account.
2. The fifth attempt is rejected.
3. Failed-attempt counter reaches `5`.
4. Account A transitions to `Locked`.

**Priority**

High

**Traceability**

- TS-AUTH-005
- AC-03
- BR-AUTH-004
- RISK-AUTH-001
- RISK-AUTH-002
- RISK-AUTH-010

---

## TC-AUTH-006 — Lock Duration Starts When Fifth Failure Is Recorded

**Scenario**

TS-AUTH-006

**Objective**

Verify the 15-minute lock period begins from the fifth recorded consecutive failed attempt.

**Preconditions**

- Account A is unlocked with failed-attempt counter = `4`.
- A reliable test clock is available to observe elapsed time.

**Test Data**

- Account A
- Incorrect password

**Steps**

1. Record the test time immediately before submitting the next login attempt.
2. Submit the fifth consecutive incorrect-password attempt.
3. Record the time at which the fifth failed attempt is observed as completed.
4. Verify Account A becomes locked.
5. Use the recorded fifth-failure time as the reference point for subsequent lock-expiry validation.

**Expected Result**

1. The fifth attempt causes Account A to become locked.
2. The defined 15-minute lock period is measured from the recorded fifth failed attempt.
3. No earlier failed attempt is used as the defined lock-period start point.

**Priority**

High

**Traceability**

- TS-AUTH-006
- AC-04
- BR-AUTH-005
- BR-AUTH-006
- RISK-AUTH-009

---

## TC-AUTH-007 — Correct Password Is Rejected During Active Lock

**Scenario**

TS-AUTH-007

**Objective**

Verify valid credentials cannot bypass an active account lock.

**Preconditions**

- Account A is locked.
- Less than 15 minutes have elapsed since the fifth failed attempt.

**Test Data**

- Account A
- Correct password

**Steps**

1. Submit a login request for Account A using the correct password while the lock is active.

**Expected Result**

1. Authentication is rejected.
2. Account A remains locked.

No assertion is made about whether the attempt changes the failed-attempt counter or lock timer because the requirement does not define those behaviors.

**Priority**

High

**Traceability**

- TS-AUTH-007
- AC-05
- BR-AUTH-007
- BR-AUTH-008
- RISK-AUTH-003

---

## TC-AUTH-008 — Incorrect Password Is Rejected During Active Lock

**Scenario**

TS-AUTH-008

**Objective**

Verify an incorrect-password login request is rejected while the account is locked.

**Preconditions**

- Account A is locked.
- Less than 15 minutes have elapsed since the fifth failed attempt.

**Test Data**

- Account A
- Incorrect password

**Steps**

1. Submit an incorrect-password login request for Account A while the lock is active.

**Expected Result**

1. Authentication is rejected.
2. Account A remains locked.

No expected result is defined for:

- Failed-attempt counter changes
- Lock-period restart
- Lock-period extension

because those behaviors are unspecified.

**Priority**

High

**Traceability**

- TS-AUTH-008
- AC-05
- BR-AUTH-007
- RISK-AUTH-011

---

## TC-AUTH-009 — Account Remains Locked Immediately Before Expiry

**Scenario**

TS-AUTH-009

**Objective**

Verify the account cannot authenticate before the complete 15-minute lock duration expires.

**Preconditions**

- Account A is locked.
- The lock-start time from the fifth failed attempt is known.

**Test Data**

- Account A
- Correct password

**Steps**

1. Wait until a point immediately before the 15-minute lock duration has expired.
2. Submit a correct-password login request.

**Expected Result**

1. Authentication is rejected while the full 15-minute duration has not expired.
2. Account A remains locked.

**Priority**

High

**Traceability**

- TS-AUTH-009
- AC-05
- AC-06
- BR-AUTH-005
- BR-AUTH-007
- RISK-AUTH-007

---

## TC-AUTH-010 — Account Automatically Unlocks After Fifteen Minutes

**Scenario**

TS-AUTH-010

**Objective**

Verify automatic unlock after the defined lock duration.

**Preconditions**

- Account A is locked.
- The lock-start time from the fifth failed attempt is known.

**Test Data**

- Account A
- Correct password

**Steps**

1. Allow the full 15-minute lock duration to expire.
2. Submit a password-based login request for Account A using the correct password.

**Expected Result**

1. Account A is treated as unlocked after the 15-minute duration expires.
2. Authentication with the correct password succeeds.
3. No administrative unlock action is required by this flow.

**Priority**

High

**Traceability**

- TS-AUTH-010
- AC-06
- BR-AUTH-005
- BR-AUTH-009
- RISK-AUTH-007
- RISK-AUTH-008
- RISK-AUTH-009

---

## TC-AUTH-011 — Automatic Unlock Resets Failed-Attempt Counter

**Scenario**

TS-AUTH-011

**Objective**

Verify the failed-attempt counter is reset when automatic unlock occurs.

**Preconditions**

- Account A was locked after five consecutive failed attempts.
- The 15-minute lock duration has expired.

**Test Data**

- Account A
- Incorrect password

**Steps**

1. Confirm the lock duration has expired.
2. Submit one incorrect-password login attempt for Account A.
3. Observe the resulting failed-attempt state.

**Expected Result**

1. The account is no longer locked because the previous lock has expired.
2. The new incorrect-password attempt is rejected.
3. The new attempt is treated as the first failed attempt of a new sequence.
4. Failed-attempt counter becomes `1`.
5. Account A remains unlocked.

**Priority**

High

**Traceability**

- TS-AUTH-011
- AC-07
- AC-09
- BR-AUTH-010
- BR-AUTH-012
- RISK-AUTH-006

---

## TC-AUTH-012 — Successful Login Resets Counter After One Failure

**Scenario**

TS-AUTH-012

**Objective**

Verify a successful login resets an early failed-attempt sequence.

**Preconditions**

- Apply the common preconditions for Account A.

**Test Data**

- Account A
- Incorrect password
- Correct password

**Steps**

1. Submit one incorrect-password login attempt.
2. Submit the next login attempt using the correct password.
3. Submit another incorrect-password login attempt.

**Expected Result**

1. First incorrect-password attempt is rejected and counter becomes `1`.
2. Correct-password attempt succeeds.
3. Successful authentication resets the counter to `0`.
4. The next incorrect-password attempt is treated as failure `1` of a new sequence.
5. Account A remains unlocked.

**Priority**

High

**Traceability**

- TS-AUTH-012
- AC-08
- AC-09
- BR-AUTH-011
- BR-AUTH-012

---

## TC-AUTH-013 — Successful Login Resets Counter After Four Failures

**Scenario**

TS-AUTH-013

**Objective**

Verify successful authentication immediately below the threshold resets the failed-attempt sequence.

**Preconditions**

- Apply the common preconditions for Account A.

**Test Data**

- Account A
- Incorrect password
- Correct password

**Steps**

1. Submit four consecutive incorrect-password login attempts.
2. Verify Account A remains unlocked.
3. Submit a correct-password login attempt.
4. Submit one new incorrect-password attempt.

**Expected Result**

1. The first four failed attempts are rejected.
2. Account A remains unlocked with counter = `4`.
3. Correct-password authentication succeeds.
4. The counter resets to `0`.
5. The next incorrect-password attempt becomes failure `1` of a new sequence.
6. Account A remains unlocked.

**Priority**

High

**Traceability**

- TS-AUTH-013
- AC-08
- AC-09
- BR-AUTH-011
- BR-AUTH-012
- RISK-AUTH-005
- RISK-AUTH-010

---

## TC-AUTH-014 — Failures Across Successful Login Are Not Consecutive

**Scenario**

TS-AUTH-014

**Objective**

Verify failures separated by a successful login are not accumulated as one consecutive sequence.

**Preconditions**

- Apply the common preconditions for Account A.

**Test Data**

- Account A
- Incorrect password
- Correct password

**Steps**

1. Submit three consecutive incorrect-password login attempts.
2. Submit a correct-password login attempt.
3. Submit two additional consecutive incorrect-password login attempts.
4. Observe the account state.

**Expected Result**

1. Initial three failures are rejected.
2. Correct-password authentication succeeds.
3. Successful login resets the failed-attempt counter to `0`.
4. The subsequent two failures form a new sequence with counter = `2`.
5. Account A remains unlocked.
6. The two failures are not combined with the previous three as five consecutive failures.

**Priority**

High

**Traceability**

- TS-AUTH-014
- AC-02
- AC-08
- AC-09
- BR-AUTH-003
- BR-AUTH-011
- BR-AUTH-012
- RISK-AUTH-005
- RISK-AUTH-010

---

## TC-AUTH-015 — Failed-Attempt Tracking Is Isolated Between Accounts

**Scenario**

TS-AUTH-015

**Objective**

Verify failed-attempt state is maintained independently for different accounts.

**Preconditions**

- Account A and Account B are unlocked.
- Both accounts have failed-attempt counter = `0`.

**Test Data**

- Account A
- Account B
- Incorrect password for each account

**Steps**

1. Submit four consecutive incorrect-password attempts for Account A.
2. Submit one incorrect-password attempt for Account B.
3. Observe the state of both accounts.
4. Submit a correct-password login for Account B.

**Expected Result**

1. Account A has four consecutive failures and remains unlocked.
2. Account B's first failed attempt is counted as `1`.
3. Account B is not treated as reaching the five-attempt threshold.
4. Account B remains unlocked.
5. Correct-password authentication for Account B succeeds.

**Priority**

High

**Traceability**

- TS-AUTH-015
- AC-01
- BR-AUTH-001
- BR-AUTH-002
- RISK-AUTH-004

---

## TC-AUTH-016 — First Failed Attempt After Automatic Unlock Starts at One

**Scenario**

TS-AUTH-016

**Objective**

Verify failure tracking starts as a new sequence after automatic unlock.

**Preconditions**

- Account A was locked after five consecutive failures.
- The 15-minute lock duration has expired.
- Automatic unlock has occurred.

**Test Data**

- Account A
- Incorrect password

**Steps**

1. Submit one incorrect-password login attempt after automatic unlock.
2. Observe the failed-attempt state and account state.

**Expected Result**

1. Authentication is rejected.
2. Failed-attempt counter becomes `1`.
3. Account A remains unlocked.
4. Previous failed attempts that caused the earlier lock do not contribute to the new sequence.

**Priority**

High

**Traceability**

- TS-AUTH-016
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

## TC-AUTH-017 — Account Can Enter a New Lock Lifecycle After Automatic Unlock

**Scenario**

TS-AUTH-017

**Objective**

Verify a previously locked account can begin a new independent failed sequence and lock again at the fifth new failure.

**Preconditions**

- Account A was previously locked.
- The 15-minute duration has expired.
- Account A has automatically unlocked.
- Previous failed-attempt counter has been reset to `0`.

**Test Data**

- Account A
- Incorrect password

**Steps**

1. Submit four consecutive incorrect-password login attempts after automatic unlock.
2. Verify Account A remains unlocked.
3. Submit a fifth consecutive incorrect-password attempt in the new sequence.
4. Observe the account state.

**Expected Result**

1. New failed attempts 1 through 4 are rejected.
2. Account A remains unlocked through the fourth new failure.
3. The fifth new consecutive failed attempt is rejected.
4. Failed-attempt counter reaches `5`.
5. Account A becomes locked again.
6. Failures from the previous lock lifecycle do not contribute to the new threshold calculation.

**Priority**

High

**Traceability**

- TS-AUTH-017
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

## Deferred Clarification-Dependent Test Cases

Executable test cases are intentionally not defined for the following scenario candidates because their deterministic expected behavior is absent from the requirement:

| Candidate | Deferred Area |
|---|---|
| CTS-AUTH-001 | Effect of locked-state attempts on failed-attempt counter |
| CTS-AUTH-002 | Effect of locked-state attempts on lock timer |
| CTS-AUTH-003 | Concurrent attempts near threshold |
| CTS-AUTH-004 | Locked-account user-facing message |
| CTS-AUTH-005 | Administrative unlock |
| CTS-AUTH-006 | Alternative authentication methods |

These areas must remain deferred until the applicable business behavior is defined.

---

## Scenario-to-Test-Case Traceability

| Scenario | Test Case |
|---|---|
| TS-AUTH-001 | TC-AUTH-001 |
| TS-AUTH-002 | TC-AUTH-002 |
| TS-AUTH-003 | TC-AUTH-003 |
| TS-AUTH-004 | TC-AUTH-004 |
| TS-AUTH-005 | TC-AUTH-005 |
| TS-AUTH-006 | TC-AUTH-006 |
| TS-AUTH-007 | TC-AUTH-007 |
| TS-AUTH-008 | TC-AUTH-008 |
| TS-AUTH-009 | TC-AUTH-009 |
| TS-AUTH-010 | TC-AUTH-010 |
| TS-AUTH-011 | TC-AUTH-011 |
| TS-AUTH-012 | TC-AUTH-012 |
| TS-AUTH-013 | TC-AUTH-013 |
| TS-AUTH-014 | TC-AUTH-014 |
| TS-AUTH-015 | TC-AUTH-015 |
| TS-AUTH-016 | TC-AUTH-016 |
| TS-AUTH-017 | TC-AUTH-017 |

All confirmed scenarios have executable test-case coverage.

---

## Acceptance Criteria Coverage

| Acceptance Criterion | Test Case Coverage |
|---|---|
| AC-01 | TC-AUTH-002, TC-AUTH-003, TC-AUTH-015, TC-AUTH-016 |
| AC-02 | TC-AUTH-003, TC-AUTH-004, TC-AUTH-014, TC-AUTH-016, TC-AUTH-017 |
| AC-03 | TC-AUTH-005, TC-AUTH-017 |
| AC-04 | TC-AUTH-006 |
| AC-05 | TC-AUTH-007, TC-AUTH-008, TC-AUTH-009 |
| AC-06 | TC-AUTH-009, TC-AUTH-010, TC-AUTH-017 |
| AC-07 | TC-AUTH-011, TC-AUTH-016, TC-AUTH-017 |
| AC-08 | TC-AUTH-001, TC-AUTH-012, TC-AUTH-013, TC-AUTH-014 |
| AC-09 | TC-AUTH-011, TC-AUTH-012, TC-AUTH-013, TC-AUTH-014, TC-AUTH-016, TC-AUTH-017 |

All nine source acceptance criteria have executable confirmed test coverage.

---

## Coverage Summary

The test-case suite covers:

- Normal unlocked login
- Incorrect-password rejection
- Counter increment
- First-failure boundary
- Four-failure boundary
- Exact fifth-failure lock threshold
- Lock-period start point
- Correct-password rejection while locked
- Incorrect-password rejection while locked
- Pre-expiry locked behavior
- Automatic unlock after 15 minutes
- Counter reset after automatic unlock
- Counter reset after successful login
- Separation of consecutive failure sequences
- Cross-account isolation
- First failure after automatic unlock
- Repeated lock lifecycle

The suite does not invent behavior for any clarification-dependent area.

Every confirmed test case has a measurable expected result and traceability back to its source scenario and requirement behavior.
