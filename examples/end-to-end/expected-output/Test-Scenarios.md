# Test Scenarios — Account Lock After Failed Login Attempts

## 1. Overview

This artifact defines test scenarios for the Account Lock After Failed Login Attempts feature.

The scenarios are derived from:

- `Sample-Requirement.md`
- `Requirement-Analysis.md`
- `Business-Rules.md`
- `Risk-Analysis.md`

The scenario set focuses on:

- Authentication.
- Failed-login tracking.
- Consecutive-failure behavior.
- Lock threshold boundaries.
- Counter reset.
- Account isolation.
- Locked-state enforcement.
- Lock message.
- Lock duration.
- Automatic unlock.
- Post-unlock tracking.
- Repeated lock lifecycle.

Each scenario defines what should be verified.

Detailed execution steps belong to `Test-Cases.md`.

---

## 2. Coverage Strategy

The scenario set applies the following test-design perspectives:

| Perspective | Primary Application |
|---|---|
| Positive Testing | Successful authentication and recovery |
| Negative Testing | Incorrect-password and locked-account authentication |
| Boundary Value Analysis | Failed-attempt threshold and lock duration |
| State Transition Testing | Unlocked → Locked → Unlocked |
| Sequence Testing | Consecutive failures and successful-login reset |
| Isolation Testing | Independent failed-login state between accounts |
| Risk-Based Testing | High-priority risks identified in `Risk-Analysis.md` |

The techniques guide scenario generation but do not introduce behavior that is absent from the requirement.

---

## 3. Scenario Summary

| Scenario ID | Area | Scenario | Coverage Type | Priority | Traceability |
|---|---|---|---|---|---|
| TS-001 | Authentication | Verify an unlocked registered account can authenticate using valid credentials. | Positive | Medium | R1–R3 |
| TS-002 | Authentication | Verify login fails when an unlocked registered account submits an incorrect password. | Negative | High | R4, BR-001 |
| TS-003 | Failed Login Tracking | Verify an incorrect-password attempt increases failed-login tracking for the corresponding account. | Functional | High | R5, BR-001 |
| TS-004 | Threshold | Verify the account remains unlocked after the first consecutive failed login attempt. | Boundary / Sequence | High | R6, BR-002 |
| TS-005 | Threshold | Verify the account remains unlocked after four consecutive failed login attempts. | Boundary | High | R6, AC-01, BR-002, RISK-002 |
| TS-006 | Account Lock | Verify the account becomes temporarily locked on the fifth consecutive failed login attempt. | Boundary / State Transition | High | R6, R8, AC-02, BR-002, RISK-001 |
| TS-007 | Counter Reset | Verify successful login after one failed attempt resets the current consecutive-failure sequence. | Sequence / State | High | R7, AC-05, BR-003, RISK-003 |
| TS-008 | Counter Reset | Verify successful login after four consecutive failed attempts resets the current consecutive-failure sequence. | Boundary / Sequence | High | R7, AC-05, BR-003, RISK-003 |
| TS-009 | Counter Reset | Verify failed attempts before and after a successful login are not treated as one consecutive sequence. | Sequence | High | R7, BR-003, RISK-003 |
| TS-010 | Account Isolation | Verify failed-login tracking for Account A does not affect Account B. | Isolation | High | R5, BR-001, RISK-004 |
| TS-011 | Account Isolation | Verify Account B can authenticate normally while Account A is approaching or has reached its lock threshold. | Isolation / Positive | High | R5, BR-001, RISK-004 |
| TS-012 | Locked State | Verify a locked account cannot authenticate using the correct password. | Negative / State | High | R10, AC-03, BR-005, RISK-005 |
| TS-013 | Locked State | Verify a login attempt made while the account is locked is rejected. | Negative / State | High | R10, AC-03, BR-005 |
| TS-014 | User Feedback | Verify the required temporary-lock message is displayed when login is attempted while locked. | Functional / User Feedback | Medium | R11, AC-03, BR-006, RISK-008 |
| TS-015 | Lock Duration | Verify the account remains locked before the 30-minute lock period expires. | Time Boundary | High | R9, BR-004, RISK-006 |
| TS-016 | Automatic Unlock | Verify the account automatically unlocks after the 30-minute lock period expires. | Time Boundary / State Transition | High | R12, AC-04, BR-007, RISK-007 |
| TS-017 | Post-Unlock Authentication | Verify authentication is available again after automatic unlock. | Positive / State | High | R13, AC-04, BR-008, RISK-007 |
| TS-018 | Post-Unlock Tracking | Verify failed-login tracking starts again after automatic unlock. | State / Sequence | High | R14, BR-009, RISK-009 |
| TS-019 | Repeated Lifecycle | Verify an automatically unlocked account can enter a new failure sequence and become locked again after five new consecutive failures. | State Transition / Boundary | High | R6, R8, R12–R14, BR-002, BR-007, BR-009 |
| TS-020 | End-to-End Lifecycle | Verify the complete account lifecycle from unlocked state through failed attempts, temporary lock, automatic unlock, and successful authentication. | End-to-End | High | R1–R14 |

---

## 4. Authentication Scenarios

### TS-001 — Successful Login for Unlocked Account

**Objective**

Verify that the new account-lock behavior does not prevent normal authentication when:

```text
Account = Unlocked
Credentials = Valid
```

**Expected Behavior**

Authentication succeeds.

**Priority:** Medium

**Traceability**

- R1
- R2
- R3

---

### TS-002 — Incorrect Password Login

**Objective**

Verify authentication fails when a registered user submits an incorrect password.

**Expected Behavior**

```text
Incorrect Password
        ↓
Authentication Failure
```

**Priority:** High

**Traceability**

- R4
- BR-001

---

### TS-003 — Track Failed Attempt for Correct Account

**Objective**

Verify an incorrect-password attempt contributes to failed-login tracking for the account on which the attempt was made.

**Expected Behavior**

The failed attempt is tracked against that account.

**Priority:** High

**Traceability**

- R5
- BR-001

---

## 5. Threshold Scenarios

### TS-004 — First Failed Attempt

**Objective**

Verify the account remains unlocked after the first consecutive incorrect-password attempt.

**Expected Behavior**

```text
Failure Count = 1
→ Account Unlocked
```

**Priority:** High

---

### TS-005 — Immediately Below Lock Threshold

**Objective**

Verify the account remains unlocked after four consecutive incorrect-password attempts.

**Expected Behavior**

```text
Failure Count = 4
→ Account Unlocked
```

**Priority:** High

**Risk Coverage**

- RISK-002

---

### TS-006 — At Lock Threshold

**Objective**

Verify the fifth consecutive incorrect-password attempt causes temporary account locking.

**Expected Behavior**

```text
Failure Count = 4
        ↓
5th Incorrect Password
        ↓
Account = Locked
```

**Priority:** High

**Risk Coverage**

- RISK-001
- RISK-002

---

## 6. Counter Reset Scenarios

### TS-007 — Reset After One Failure

**Objective**

Verify successful authentication after one failed attempt resets the current failed-login sequence.

**Expected Behavior**

```text
1 Failure
   ↓
Successful Login
   ↓
Failure Sequence Reset
```

**Priority:** High

---

### TS-008 — Reset Immediately Below Threshold

**Objective**

Verify successful authentication after four consecutive failed attempts resets the sequence and prevents those failures from contributing to a later lock.

**Expected Behavior**

```text
4 Failures
   ↓
Successful Login
   ↓
Sequence Reset
```

**Priority:** High

**Risk Coverage**

- RISK-003

---

### TS-009 — Failures Across Successful Login Are Not Consecutive

**Objective**

Verify failed attempts occurring before and after a successful login are treated as separate failure sequences.

Example:

```text
3 Failures
   ↓
Successful Login
   ↓
2 Failures
```

must not be interpreted as:

```text
5 Consecutive Failures
```

**Priority:** High

**Risk Coverage**

- RISK-003

---

## 7. Account Isolation Scenarios

### TS-010 — Independent Failure Tracking

**Objective**

Verify failed-login activity for Account A does not contribute to the failure state of Account B.

Example:

```text
Account A
4 Failed Attempts

Account B
1 Failed Attempt
```

must not behave as a shared five-attempt sequence.

**Priority:** High

**Risk Coverage**

- RISK-004

---

### TS-011 — Authentication of Independent Account

**Objective**

Verify Account B remains able to authenticate normally when Account A has accumulated failures or becomes locked.

**Expected Behavior**

Account A's failed-login state does not prevent valid authentication for Account B.

**Priority:** High

**Risk Coverage**

- RISK-004

---

## 8. Locked-State Scenarios

### TS-012 — Correct Password While Locked

**Objective**

Verify correct credentials cannot bypass an active temporary lock.

**Expected Behavior**

```text
Account = Locked
+
Password = Correct
        ↓
Authentication Rejected
```

**Priority:** High

**Risk Coverage**

- RISK-005

---

### TS-013 — Authentication Attempt During Lock

**Objective**

Verify authentication is rejected when login is attempted during the active lock period.

**Expected Behavior**

Authentication is not allowed.

The scenario does not assume whether the attempt changes the failed-login counter or lock timer.

**Priority:** High

---

### TS-014 — Locked-Account Message

**Objective**

Verify the required message is displayed when authentication is attempted while the account is locked.

**Expected Result**

```text
Your account has been temporarily locked. Please try again later.
```

**Priority:** Medium

**Risk Coverage**

- RISK-008

---

## 9. Time-Based Scenarios

### TS-015 — Before Lock Expiration

**Objective**

Verify the account remains locked while the required 30-minute lock period has not yet expired.

**Expected Behavior**

```text
Lock Period < Expiration
→ Account remains locked
```

**Priority:** High

**Risk Coverage**

- RISK-006

---

### TS-016 — Automatic Unlock After Expiration

**Objective**

Verify the account automatically transitions to the unlocked state after the 30-minute lock period expires.

**Expected Behavior**

```text
LOCKED
   ↓
30-Minute Period Expires
   ↓
UNLOCKED
```

**Priority:** High

**Risk Coverage**

- RISK-006
- RISK-007

The exact behavior at the precise expiration instant is excluded until clarified.

---

## 10. Post-Unlock Scenarios

### TS-017 — Login Available After Automatic Unlock

**Objective**

Verify the user can attempt authentication again after automatic unlock.

With valid credentials, authentication should succeed according to the normal login rule.

**Priority:** High

---

### TS-018 — Restart Failed-Login Tracking

**Objective**

Verify failed-login tracking starts again after automatic unlock.

**Expected Behavior**

A new incorrect-password attempt participates in the post-unlock failure sequence.

The scenario does not assume a specific internal counter representation immediately after unlock.

**Priority:** High

**Risk Coverage**

- RISK-009

---

### TS-019 — Repeated Lock Lifecycle

**Objective**

Verify an automatically unlocked account can begin a new failed-login sequence and become temporarily locked again after five new consecutive incorrect-password attempts.

**Expected Behavior**

```text
Automatic Unlock
        ↓
New Failure Sequence
        ↓
Failures 1–4
→ Unlocked
        ↓
Failure 5
→ Locked Again
```

**Priority:** High

---

## 11. End-to-End Scenario

### TS-020 — Complete Account-Lock Lifecycle

**Objective**

Verify the complete confirmed feature lifecycle.

```text
Unlocked Account
      ↓
Valid Login Available
      ↓
Consecutive Incorrect Passwords
      ↓
Failures 1–4 → Unlocked
      ↓
Failure 5 → Locked
      ↓
Login During Lock → Rejected
      ↓
30-Minute Lock Period
      ↓
Automatic Unlock
      ↓
Authentication Available Again
```

**Priority:** High

This scenario verifies integration of the confirmed business behaviors but does not replace the focused scenarios above.

---

## 12. Clarification-Dependent Scenario Candidates

The following are valid test ideas, but executable expected results cannot be finalized from the supplied requirement.

They are therefore separated from the confirmed scenario set.

| Candidate ID | Test Idea | Related Risk | Missing Rule |
|---|---|---|---|
| CTS-001 | Verify failed-login counter behavior when login is attempted during an active lock. | RISK-010 | Effect of locked attempts on counter |
| CTS-002 | Verify lock timer behavior when login is attempted during an active lock. | RISK-010 | Timer restart/extension rule |
| CTS-003 | Verify login exactly at the 30-minute expiration instant. | RISK-006 / RISK-007 | Exact expiration semantics |
| CTS-004 | Verify failed-login tracking for the same account across different browsers. | RISK-011 | Cross-browser tracking rule |
| CTS-005 | Verify failed-login tracking for the same account across different devices. | RISK-011 | Cross-device tracking rule |
| CTS-006 | Verify simultaneous failed-login attempts when the account is immediately below threshold. | RISK-012 | Concurrent request semantics |
| CTS-007 | Verify an existing authenticated session after the same account becomes locked. | — | Existing-session behavior |
| CTS-008 | Verify password reset or password change during an active lock. | — | Password-management interaction |
| CTS-009 | Verify failed-login behavior for an unregistered email address. | — | Unknown-account behavior |

These candidates should become confirmed scenarios only after the corresponding behavior is defined.

---

## 13. Requirement Coverage Matrix

| Requirement | Covered By |
|---|---|
| R1 | TS-001, TS-020 |
| R2 | TS-001, TS-002, TS-020 |
| R3 | TS-001, TS-017, TS-020 |
| R4 | TS-002, TS-003, TS-020 |
| R5 | TS-003, TS-010, TS-011 |
| R6 | TS-004, TS-005, TS-006, TS-019, TS-020 |
| R7 | TS-007, TS-008, TS-009 |
| R8 | TS-006, TS-019, TS-020 |
| R9 | TS-015, TS-016, TS-020 |
| R10 | TS-012, TS-013, TS-020 |
| R11 | TS-014 |
| R12 | TS-016, TS-019, TS-020 |
| R13 | TS-017, TS-020 |
| R14 | TS-018, TS-019 |
| AC-01 | TS-004, TS-005 |
| AC-02 | TS-006 |
| AC-03 | TS-012, TS-013, TS-014 |
| AC-04 | TS-016, TS-017 |
| AC-05 | TS-007, TS-008, TS-009 |

All explicitly defined requirements and acceptance criteria have scenario coverage.

---

## 14. Business Rule Coverage Matrix

| Business Rule | Covered By |
|---|---|
| BR-001 | TS-003, TS-010, TS-011 |
| BR-002 | TS-004, TS-005, TS-006, TS-019 |
| BR-003 | TS-007, TS-008, TS-009 |
| BR-004 | TS-015, TS-016 |
| BR-005 | TS-012, TS-013 |
| BR-006 | TS-014 |
| BR-007 | TS-016, TS-019 |
| BR-008 | TS-017 |
| BR-009 | TS-018, TS-019 |

All confirmed business rules have scenario coverage.

---

## 15. Risk Coverage Matrix

| Risk | Coverage | Scenario(s) |
|---|---|---|
| RISK-001 | Covered | TS-006 |
| RISK-002 | Covered | TS-005, TS-006 |
| RISK-003 | Covered | TS-007, TS-008, TS-009 |
| RISK-004 | Covered | TS-010, TS-011 |
| RISK-005 | Covered | TS-012 |
| RISK-006 | Covered within defined requirement boundary | TS-015, TS-016 |
| RISK-007 | Covered within defined requirement boundary | TS-016, TS-017 |
| RISK-008 | Covered | TS-014 |
| RISK-009 | Covered | TS-018, TS-019 |
| RISK-010 | Clarification-Dependent | CTS-001, CTS-002 |
| RISK-011 | Clarification-Dependent | CTS-004, CTS-005 |
| RISK-012 | Clarification-Dependent | CTS-006 |

Risk visibility is preserved without fabricating expected behavior for undefined requirements.

---

## 16. Scenario Coverage Summary

The confirmed scenario set contains:

```text
20 Test Scenarios
```

covering:

```text
Authentication
      +
Failed-Login Tracking
      +
Threshold Boundary
      +
Consecutive Sequence
      +
Counter Reset
      +
Account Isolation
      +
Locked-State Enforcement
      +
User Feedback
      +
Time Boundary
      +
Automatic Unlock
      +
Post-Unlock Tracking
      +
Repeated Lifecycle
      +
End-to-End Lifecycle
```

Additionally:

```text
9 Clarification-Dependent Test Candidates
```

remain visible for future expansion once their expected behavior is confirmed.

The scenario set covers all currently defined requirements, acceptance criteria, and confirmed business rules while preserving unresolved behavior for downstream clarification.