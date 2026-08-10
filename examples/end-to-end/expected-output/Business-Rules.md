# Business Rules — Account Lock After Failed Login Attempts

## 1. Overview

This artifact structures the business rules derived from the analyzed requirements for the temporary account-locking feature.

The rules define:

- Failed-login tracking.
- Consecutive-failure handling.
- Account-lock threshold.
- Counter reset behavior.
- Temporary lock duration.
- Authentication behavior while locked.
- Automatic unlock.
- Post-unlock failed-login tracking.

Only behavior supported by the supplied requirement and `Requirement-Analysis.md` is treated as confirmed.

---

## 2. Business Rule Summary

| Rule ID | Rule | Category | Source |
|---|---|---|---|
| BR-001 | Incorrect-password attempts are tracked separately for each registered account. | Tracking | R5 |
| BR-002 | Five consecutive incorrect-password attempts temporarily lock the account. | Threshold | R6, R8, AC-02 |
| BR-003 | A successful login before the fifth consecutive failure resets failed-login tracking. | Reset | R7, AC-05 |
| BR-004 | A temporarily locked account remains locked for 30 minutes. | Time-Based | R9 |
| BR-005 | Authentication is rejected while the account is locked, including when the correct password is provided. | Access Control | R10, AC-03 |
| BR-006 | A login attempt while locked displays the defined temporary-lock message. | User Feedback | R11, AC-03 |
| BR-007 | The account automatically unlocks after the 30-minute lock period expires. | State Transition | R12, AC-04 |
| BR-008 | After automatic unlock, the user can attempt authentication again. | State Transition | R13, AC-04 |
| BR-009 | Failed-login tracking starts again after automatic unlock. | Reset / Tracking | R14 |

---

## 3. Detailed Business Rules

### BR-001 — Account-Specific Failed-Login Tracking

**Category:** Tracking

**Rule**

Incorrect-password login attempts MUST be tracked separately for each registered account.

**Trigger**

A registered user submits an incorrect password.

**Condition**

```text
Registered Account
+
Incorrect Password
```

**Expected Behavior**

```text
Authentication Fails
        ↓
Failed Attempt Recorded
        ↓
Tracking Associated with That Account
```

Failed attempts belonging to one account must not contribute to the failed-login state of another account.

**Related Requirements**

- R5
- RA-RULE-001

---

### BR-002 — Temporary Lock After Five Consecutive Failures

**Category:** Threshold

**Rule**

A registered account MUST become temporarily locked after the fifth consecutive incorrect-password login attempt.

**Trigger**

The fifth consecutive incorrect-password attempt is submitted.

**Condition**

```text
Consecutive Failed Attempts = 5
```

**Expected Behavior**

```text
Attempts 1–4
→ Account remains unlocked

Attempt 5
→ Account becomes locked
```

**Boundary**

```text
4 failures → Unlocked
5 failures → Locked
```

**Dependency**

Depends on:

- BR-001 — Account-specific tracking.
- BR-003 — Reset of the consecutive sequence after successful authentication.

**Related Requirements**

- R6
- R8
- AC-01
- AC-02
- RA-RULE-002

---

### BR-003 — Reset After Successful Login

**Category:** Reset

**Rule**

A successful login occurring before the fifth consecutive failure MUST reset failed-login tracking for the account.

**Trigger**

Authentication succeeds before the lock threshold is reached.

**Condition**

```text
Consecutive Failed Attempts = 1–4
+
Valid Credentials
+
Account Not Locked
```

**Expected Behavior**

```text
Failed Login Sequence
        ↓
Successful Login
        ↓
Sequence Reset
```

A subsequent incorrect-password attempt begins a new consecutive failure sequence.

**Dependency**

The account must still be eligible for authentication.

**Related Requirements**

- R7
- AC-05
- RA-RULE-003

---

### BR-004 — Thirty-Minute Lock Duration

**Category:** Time-Based

**Rule**

A temporarily locked account MUST remain locked for 30 minutes.

**Trigger**

BR-002 causes the account to enter the locked state.

**Condition**

```text
Account State = Locked
```

**Expected Behavior**

```text
Lock Begins
    ↓
30-Minute Lock Period
    ↓
Lock Period Expires
```

The requirement does not define the exact evaluation semantics for a request occurring precisely at the expiration instant.

**Dependency**

Depends on BR-002.

**Related Requirements**

- R9
- RA-RULE-004

---

### BR-005 — Authentication Rejection During Lock

**Category:** Access Control

**Rule**

A locked account MUST NOT authenticate while the temporary lock is active.

This restriction applies even when the submitted password is correct.

**Trigger**

A login attempt is submitted while the account is locked.

**Condition**

```text
Account State = Locked
```

**Expected Behavior**

```text
Login Attempt
      ↓
Authentication Rejected
```

**Exception**

No exception allowing authentication during the active lock period is defined.

**Related Requirements**

- R10
- AC-03
- RA-RULE-005

---

### BR-006 — Locked-Account Message

**Category:** User Feedback

**Rule**

When authentication is attempted while the account is locked, the system MUST display:

```text
Your account has been temporarily locked. Please try again later.
```

**Trigger**

A login attempt occurs while the account is locked.

**Condition**

```text
Account State = Locked
```

**Expected Behavior**

Authentication is rejected and the defined message is displayed.

**Dependency**

Depends on BR-005.

**Related Requirements**

- R11
- AC-03
- RA-RULE-006

---

### BR-007 — Automatic Unlock

**Category:** State Transition

**Rule**

A temporarily locked account MUST automatically return to the unlocked state after the 30-minute lock period expires.

**Trigger**

Expiration of the temporary lock period.

**Condition**

```text
Account State = Locked
+
Lock Period = Expired
```

**Expected Behavior**

```text
LOCKED
   ↓
30-Minute Period Expires
   ↓
UNLOCKED
```

No manual unlock action is required by the supplied requirement.

**Dependency**

Depends on BR-004.

**Related Requirements**

- R12
- AC-04
- RA-RULE-007

---

### BR-008 — Authentication Available After Unlock

**Category:** State Transition

**Rule**

After automatic unlock, the user MUST be able to attempt authentication again.

**Trigger**

BR-007 completes the automatic unlock.

**Condition**

```text
Previous State = Locked
+
Lock Period = Expired
```

**Expected Behavior**

The account is eligible for login attempts again.

Successful authentication still depends on valid credentials.

**Dependency**

Depends on BR-007.

**Related Requirements**

- R13
- AC-04

---

### BR-009 — Restart Failed-Login Tracking After Unlock

**Category:** Reset / Tracking

**Rule**

Failed-login tracking MUST start again after the account has been automatically unlocked.

**Trigger**

Automatic unlock completes.

**Condition**

```text
Account Transitions
LOCKED → UNLOCKED
```

**Expected Behavior**

Subsequent incorrect-password attempts participate in a new failed-login tracking sequence.

The requirement does not explicitly define the internal numeric counter representation immediately after unlock.

**Dependency**

Depends on BR-007.

**Related Requirements**

- R14
- RA-RULE-008

---

## 4. Rule Relationships

The core rule dependency chain is:

```text
BR-001
Account-Specific Tracking
        ↓
BR-002
Five-Failure Threshold
        ↓
Temporary Lock
        ↓
BR-004
30-Minute Duration
        ↓
BR-007
Automatic Unlock
        ↓
┌───────────────┐
│               │
▼               ▼
BR-008          BR-009
Authentication  Tracking
Available       Restarts
```

Counter-reset behavior operates alongside this chain:

```text
Failed Attempts 1–4
        ↓
Successful Login
        ↓
BR-003
Tracking Reset
        ↓
New Failure Sequence
```

Locked-state authentication behavior is governed by:

```text
Account Locked
      ↓
BR-005
Authentication Rejected
      ↓
BR-006
Lock Message Displayed
```

---

## 5. Rule Interaction Matrix

| Condition | Account State | Authentication | Failed-Login Tracking | Result |
|---|---|---|---|---|
| Correct password before threshold | Unlocked | Allowed | Reset | Login succeeds |
| Incorrect password, failures 1–4 | Unlocked | Rejected | Incremented | Account remains unlocked |
| 5th consecutive incorrect password | Unlocked → Locked | Rejected | Threshold reached | Account locked |
| Correct password during lock | Locked | Rejected | Not defined | Lock remains active |
| Incorrect password during lock | Locked | Rejected | Not defined | Lock remains active |
| Lock period expires | Locked → Unlocked | Available again | Starts again | Account unlocked |

The effect of login attempts during the active lock period on the counter or timer is not defined by the requirement.

---

## 6. Rule Classification

### Tracking Rules

```text
BR-001
BR-009
```

These rules govern how failed-login behavior is associated with an account and restarted after unlock.

### Threshold Rules

```text
BR-002
```

This rule defines the transition boundary from normal failed authentication to account locking.

### Reset Rules

```text
BR-003
BR-009
```

These rules define when a previous failed-login sequence stops affecting future authentication behavior.

### Time-Based Rules

```text
BR-004
```

This rule governs the duration of the temporary lock.

### Access-Control Rules

```text
BR-005
```

This rule controls whether authentication is permitted while locked.

### User-Feedback Rules

```text
BR-006
```

This rule defines the required response communicated to the user during lock.

### State-Transition Rules

```text
BR-007
BR-008
```

These rules govern recovery from the locked state and restoration of authentication availability.

---

## 7. Clarification-Dependent Behavior

The following behaviors MUST NOT be converted into confirmed business rules without additional requirement information.

### BR-CL-001 — Attempts During Lock and Failure Counter

It is not defined whether a login attempt made during the active lock period affects failed-login tracking.

---

### BR-CL-002 — Attempts During Lock and Lock Timer

It is not defined whether login attempts during the lock:

- Restart the timer.
- Extend the timer.
- Have no effect on the timer.

---

### BR-CL-003 — Exact Expiration Boundary

Behavior for a login request occurring exactly at the 30-minute expiration instant is not explicitly defined.

---

### BR-CL-004 — Cross-Session Tracking

The requirement defines account-specific tracking but does not state whether failed attempts are shared across:

- Browsers.
- Devices.
- Sessions.

---

### BR-CL-005 — Concurrent Login Attempts

The requirement does not define how simultaneous login attempts near the five-failure threshold are ordered or evaluated.

---

### BR-CL-006 — Existing Authenticated Sessions

The requirement does not define whether an already-authenticated session remains valid after the same account becomes locked.

---

### BR-CL-007 — Password Management Interaction

The requirement does not define whether password reset or password change:

- Resets failed-login tracking.
- Removes an active temporary lock.

---

### BR-CL-008 — Unknown Email Addresses

Failed-login behavior for an email address that does not correspond to a registered account is not defined.

---

## 8. Rule Traceability

| Business Rule | Requirement Analysis | Source Requirement / AC |
|---|---|---|
| BR-001 | RA-RULE-001 | R5 |
| BR-002 | RA-RULE-002 | R6, R8, AC-01, AC-02 |
| BR-003 | RA-RULE-003 | R7, AC-05 |
| BR-004 | RA-RULE-004 | R9 |
| BR-005 | RA-RULE-005 | R10, AC-03 |
| BR-006 | RA-RULE-006 | R11, AC-03 |
| BR-007 | RA-RULE-007 | R12, AC-04 |
| BR-008 | Post-Unlock Behavior | R13, AC-04 |
| BR-009 | RA-RULE-008 | R14 |

All confirmed business rules remain traceable to the analyzed requirement.

---

## 9. Business Rule Summary

The feature is governed by three connected rule groups:

```text
Failed-Login Control
├── Account-specific tracking
├── Consecutive-failure threshold
└── Successful-login reset

Temporary Lock
├── Lock after fifth failure
├── 30-minute duration
├── Reject authentication
└── Display lock message

Recovery
├── Automatic unlock
├── Authentication available again
└── Failed-login tracking restarts
```

The most critical rule boundaries are:

```text
4 failures → Account remains unlocked

5 failures → Account becomes locked

Active lock → Authentication prohibited

30-minute expiration → Automatic unlock
```

Undefined behavior remains explicitly separated from confirmed rules and must be carried forward as clarification-dependent behavior rather than assumed by downstream QA artifacts.