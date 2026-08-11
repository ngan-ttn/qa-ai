# Business Rules — Account Lock After Failed Login Attempts

## 1. Overview

This artifact structures the business rules derived from `Requirement-Analysis.md` for the temporary account-locking feature.

Only behavior supported by the supplied requirement and requirement analysis is treated as confirmed. Undefined behavior remains clarification-dependent and is not converted into business rules.

---

## 2. Business Rule Summary

| Rule ID | Rule | Category | Source |
|---|---|---|---|
| BR-001 | Incorrect-password attempts are tracked separately for each registered account. | Tracking | R5 |
| BR-002 | Five consecutive incorrect-password attempts temporarily lock the account. | Threshold | R6, R8, AC-01, AC-02 |
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

**Rule:** Incorrect-password login attempts MUST be tracked separately for each registered account.

**Trigger:** A registered user submits an incorrect password.

**Expected Behavior:**

```text
Authentication Fails
        ↓
Failed Attempt Recorded
        ↓
Tracking Associated with That Account
```

Failed attempts belonging to one account must not contribute to another account's failed-login state.

**Traceability:** R5; Requirement Analysis §8 Account Isolation.

---

### BR-002 — Temporary Lock After Five Consecutive Failures

**Rule:** A registered account MUST become temporarily locked after the fifth consecutive incorrect-password login attempt.

**Boundary:**

```text
4 consecutive failures → Account remains unlocked
5th consecutive failure → Account becomes locked
```

**Dependencies:** BR-001 and BR-003.

**Traceability:** R6, R8, AC-01, AC-02; Requirement Analysis §6 State Model and §7 Boundary Conditions.

---

### BR-003 — Reset After Successful Login

**Rule:** A successful login occurring before the fifth consecutive failure MUST reset failed-login tracking for the account.

**Condition:**

```text
Consecutive Failed Attempts = 1–4
+
Valid Credentials
+
Account Not Locked
```

A subsequent incorrect-password attempt begins a new consecutive failure sequence.

**Traceability:** R7, AC-05; Requirement Analysis §5 Flow 4 and §6 State Model.

---

### BR-004 — Thirty-Minute Lock Duration

**Rule:** A temporarily locked account MUST remain locked for 30 minutes.

```text
Lock Begins
    ↓
30-Minute Lock Period
    ↓
Lock Period Expires
```

The exact evaluation semantics for a request occurring precisely at the expiration instant are not defined.

**Dependency:** BR-002.

**Traceability:** R9; Requirement Analysis §6 State Model and §7 Lock Duration.

---

### BR-005 — Authentication Rejection During Lock

**Rule:** A locked account MUST NOT authenticate while the temporary lock is active, including when the submitted password is correct.

```text
Account State = Locked
        ↓
Login Attempt
        ↓
Authentication Rejected
```

**Traceability:** R10, AC-03; Requirement Analysis §5 Flow 5 and §6 State Model.

---

### BR-006 — Locked-Account Message

**Rule:** A login attempt while the account is locked MUST display:

```text
Your account has been temporarily locked. Please try again later.
```

Authentication is rejected and the defined message is displayed.

**Dependency:** BR-005.

**Traceability:** R11, AC-03; Requirement Analysis §9 User Feedback.

---

### BR-007 — Automatic Unlock

**Rule:** A temporarily locked account MUST automatically return to the unlocked state after the 30-minute lock period expires.

```text
LOCKED
   ↓
30-Minute Period Expires
   ↓
UNLOCKED
```

No manual unlock action is required by the supplied requirement.

**Dependency:** BR-004.

**Traceability:** R12, AC-04; Requirement Analysis §5 Flow 6 and §6 State Model.

---

### BR-008 — Authentication Available After Unlock

**Rule:** After automatic unlock, the user MUST be able to attempt authentication again.

Successful authentication still depends on valid credentials.

**Dependency:** BR-007.

**Traceability:** R13, AC-04; Requirement Analysis §5 Flow 6.

---

### BR-009 — Restart Failed-Login Tracking After Unlock

**Rule:** Failed-login tracking MUST start again after the account has been automatically unlocked.

Subsequent incorrect-password attempts participate in a new failed-login sequence. The internal numeric counter representation immediately after unlock is not explicitly defined.

**Dependency:** BR-007.

**Traceability:** R14; Requirement Analysis §5 Flow 6 and §10 Derived Analysis.

---

## 4. Rule Relationships

```text
BR-001 Account-Specific Tracking
        ↓
BR-002 Five-Failure Threshold
        ↓
Temporary Lock
        ↓
BR-004 30-Minute Duration
        ↓
BR-007 Automatic Unlock
        ↓
┌───────────────┐
│               │
▼               ▼
BR-008          BR-009
Authentication  Tracking
Available       Restarts
```

Successful-login reset operates alongside this chain:

```text
Failed Attempts 1–4
        ↓
Successful Login
        ↓
BR-003 Tracking Reset
        ↓
New Failure Sequence
```

Locked-state behavior is governed by BR-005 and BR-006.

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

The effect of login attempts during the active lock period on the counter or timer is not defined.

---

## 6. Clarification-Dependent Behavior

The following behaviors MUST NOT be converted into confirmed business rules without additional requirement information.

| ID | Area | Undefined Behavior | Requirement Analysis Source |
|---|---|---|---|
| BR-CL-001 | Active Lock | Whether locked-state login attempts change failed-login tracking. | Q-001 |
| BR-CL-002 | Active Lock | Whether locked-state login attempts restart or extend the lock timer. | Q-002 |
| BR-CL-003 | Lock Expiration | Exact behavior at the precise 30-minute expiration instant. | Q-003 |
| BR-CL-004 | Tracking Scope | Same-account tracking across browser sessions and devices. | Q-004, Q-005 |
| BR-CL-005 | Concurrency | Ordering/evaluation of simultaneous attempts near threshold. | Q-006 |
| BR-CL-006 | Existing Session | Effect of lock on an already authenticated session. | Q-007 |
| BR-CL-007 | Password Management | Interaction with password reset/change. | Q-008 |
| BR-CL-008 | Unknown Account | Failed-login behavior for an unregistered email address. | Q-009 |

---

## 7. Rule Traceability

| Business Rule | Requirement Analysis Evidence | Source Requirement / AC |
|---|---|---|
| BR-001 | §8 Account Isolation | R5 |
| BR-002 | §6 State Model; §7 Failed-Login Threshold | R6, R8, AC-01, AC-02 |
| BR-003 | §5 Flow 4; §6 State Model | R7, AC-05 |
| BR-004 | §6 State Model; §7 Lock Duration | R9 |
| BR-005 | §5 Flow 5; §6 State Model | R10, AC-03 |
| BR-006 | §9 User Feedback | R11, AC-03 |
| BR-007 | §5 Flow 6; §6 State Model | R12, AC-04 |
| BR-008 | §5 Flow 6 | R13, AC-04 |
| BR-009 | §5 Flow 6; §10 Derived Analysis | R14 |

All confirmed business rules are now traceable directly to identifiers and sections that exist in `Requirement-Analysis.md`.

---

## 8. Business Rule Summary

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

Critical boundaries remain:

```text
4 failures → Account remains unlocked
5 failures → Account becomes locked
Active lock → Authentication prohibited
30-minute expiration → Automatic unlock
```

Undefined behavior remains explicitly separated from confirmed rules and is carried downstream as clarification-dependent information.