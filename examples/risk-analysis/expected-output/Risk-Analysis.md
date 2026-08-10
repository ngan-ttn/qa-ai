# Risk Analysis — Account Lock After Failed Login Attempts

## 1. Risk Analysis Summary

The account-lock feature affects authentication state, failed-login tracking, time-based unlocking, and account isolation.

Because the feature is intended to protect user accounts from unauthorized access, incorrect behavior may create two major classes of impact:

- **Security exposure** — an account is not locked when the defined threshold is reached or a lock can be bypassed.
- **Availability impact** — a legitimate user is incorrectly locked or remains locked longer than intended.

The highest-risk areas are:

1. Lock threshold enforcement.
2. Authentication enforcement during the locked state.
3. Automatic unlock after the defined duration.
4. Failed-login counter reset behavior.
5. Account-specific failed-login tracking.

Several secondary risks depend on behaviors that are not fully defined by the requirement and therefore require clarification rather than assumed system behavior.

---

## 2. Risk Assessment

| Risk ID | Area | Risk Description | Requirement Basis | Impact | Likelihood | Risk Level |
|---|---|---|---|---|---|---|
| RISK-001 | Lock Threshold | The account may not become locked exactly on the fifth consecutive failed login attempt. | Requirements 6, 8; AC-02 | High | Medium | High |
| RISK-002 | Lock Threshold | The account may become locked before five consecutive failed attempts. | Requirements 6, 8; AC-01 | High | Medium | High |
| RISK-003 | Authentication | A locked account may still authenticate when valid credentials are submitted. | Requirement 10; AC-03 | High | Medium | High |
| RISK-004 | Lock Duration | The account may unlock before the required 30-minute lock period expires. | Requirements 9, 12; AC-04 | High | Medium | High |
| RISK-005 | Automatic Unlock | The account may remain locked after the 30-minute period expires. | Requirements 9, 12–13; AC-04 | High | Medium | High |
| RISK-006 | Counter Reset | A successful login before the threshold may fail to reset the failed-login counter. | Requirement 7; AC-05 | High | Medium | High |
| RISK-007 | Counter Reset | Previous failed attempts may incorrectly contribute to a later sequence after a successful login. | Requirement 7; AC-05 | High | Medium | High |
| RISK-008 | Account Isolation | Failed login attempts for one account may incorrectly affect another account. | Requirement 5; Notes | High | Low | High |
| RISK-009 | Unlock State | Previous failed attempts may incorrectly contribute to the next threshold after automatic unlock. | Requirement 14 | High | Medium | High |
| RISK-010 | Lock Message | The required temporary-lock message may not be displayed when a login is attempted during the locked state. | Requirement 11; AC-03 | Medium | Medium | Medium |
| RISK-011 | State Consistency | Account lock state and failed-login counter may become inconsistent across consecutive authentication actions. | Requirements 5–14 | High | Medium | High |
| RISK-012 | Time Boundary | Authentication behavior may be inconsistent around the 30-minute unlock boundary. | Requirements 9, 12 | High | Medium | High |

---

## 3. High-Risk Areas

### 3.1 Lock Threshold

The transition from the fourth to the fifth consecutive failed login attempt is a critical boundary.

Expected requirement behavior:

```text
Attempt 1 → Failed / Unlocked
Attempt 2 → Failed / Unlocked
Attempt 3 → Failed / Unlocked
Attempt 4 → Failed / Unlocked
Attempt 5 → Failed / Locked
```

Primary risks:

- Lock occurs too early.
- Lock occurs too late.
- Fifth failure is recorded but lock state is not applied.
- Counter and account state become inconsistent.

**Risk Level: High**

---

### 3.2 Authentication During Locked State

The requirement explicitly prohibits authentication while an account is locked, including when the correct password is entered.

```text
Locked Account
      +
Correct Password
      ↓
Authentication Rejected
```

Failure of this behavior would undermine the primary protection introduced by the feature.

**Risk Level: High**

---

### 3.3 Lock Duration and Automatic Unlock

The account must remain locked for 30 minutes and then automatically unlock.

Relevant state transition:

```text
Locked
  │
  │ 30 minutes
  ▼
Unlocked
```

Primary risks include:

- Premature unlock.
- Delayed unlock.
- Failure to unlock automatically.
- Incorrect behavior at the expiration boundary.
- Account becomes unlocked but authentication remains unavailable.

**Risk Level: High**

---

### 3.4 Failed-Login Counter Reset

A successful login before reaching the fifth consecutive failure resets the counter.

Example:

```text
Fail
  ↓
Fail
  ↓
Fail
  ↓
Successful Login
  ↓
Counter Reset
```

If reset behavior fails, later failed attempts could lock a legitimate user's account earlier than defined.

**Risk Level: High**

---

### 3.5 Account-Specific Tracking

Failed-login attempts must be tracked independently for each user account.

Expected isolation:

```text
Account A
Failed Count = 4

Account B
Failed Count = 0
```

A failed login against Account A must not alter Account B's failed-login state.

Incorrect account isolation could cause unauthorized lockouts or incorrect authentication state across users.

**Risk Level: High**

---

## 4. Boundary and State Risks

### Failed-Login Boundary

Critical values:

| Consecutive Failed Attempts | Expected State |
|---:|---|
| 0 | Unlocked |
| 1 | Unlocked |
| 2 | Unlocked |
| 3 | Unlocked |
| 4 | Unlocked |
| 5 | Locked |

The highest-risk transition is:

```text
4 → 5
```

### Lock-Time Boundary

The defined lock duration is:

```text
30 minutes
```

Relevant boundary conditions include:

```text
Before expiration
At expiration
After expiration
```

The exact semantics of a login occurring precisely at the expiration boundary are not defined by the requirement.

### Counter Reset Boundary

Relevant sequences include:

```text
1–4 Failures
     +
Successful Login
     ↓
Counter Reset
```

and:

```text
Locked
  ↓
30-Minute Expiration
  ↓
Tracking Starts Again
```

The second sequence is defined functionally, although the requirement does not explicitly state the resulting numeric counter value.

---

## 5. State Transition Risks

The feature introduces at least two relevant account states:

```text
UNLOCKED
LOCKED
```

Primary transitions are:

```text
UNLOCKED
   │
   │ 5th consecutive failed login
   ▼
LOCKED
   │
   │ 30-minute period expires
   ▼
UNLOCKED
```

A successful login before reaching the threshold does not change the lock state but resets the failure sequence:

```text
UNLOCKED
   │
   │ Successful Login
   ▼
UNLOCKED
Counter Reset
```

Risk exists if the account state, timer, and failed-login counter are updated inconsistently during these transitions.

---

## 6. Risk Areas Requiring Clarification

Some potential risks cannot be fully assessed because the corresponding expected behavior is not defined.

| Gap ID | Area | Undefined Behavior | Risk if Implementations Differ |
|---|---|---|---|
| RG-001 | Lock Start Time | Exact start point of the 30-minute period is not stated. | Unlock timing may differ from expected behavior. |
| RG-002 | Locked Attempts | Effect of login attempts during lock on the failed-login counter is undefined. | Counter state after unlock may be inconsistent. |
| RG-003 | Lock Extension | Whether attempts during lock extend/restart the timer is undefined. | Users may remain locked for an unintended duration. |
| RG-004 | Cross-Device Tracking | Cross-browser/device/session contribution to the account counter is not explicitly defined. | Account-level tracking may behave inconsistently across access channels. |
| RG-005 | Unknown Email | Behavior for an email address not associated with an account is undefined. | Authentication and failed-attempt handling may differ from intended security behavior. |
| RG-006 | Concurrency | Simultaneous attempts near the threshold are undefined. | Counter or lock state may become inconsistent. |
| RG-007 | Unlock Counter | Numeric counter state immediately after automatic unlock is not explicit. | The next failed-login sequence may start from an incorrect state. |

These areas should not receive invented expected behavior during test design.

---

## 7. Risk Prioritization

Based on the available requirement, testing attention should be prioritized as follows:

### Priority 1 — Critical Feature Behavior

```text
Lock threshold
Authentication while locked
30-minute lock enforcement
Automatic unlock
```

Failures in these areas directly compromise the primary purpose or availability of the feature.

### Priority 2 — State and Counter Integrity

```text
Successful-login reset
Post-unlock tracking
Account-specific tracking
State/counter consistency
```

Failures may cause incorrect lockouts or incorrect account protection.

### Priority 3 — User-Facing and Secondary Behavior

```text
Lock message
Undefined timer boundaries
Cross-device behavior
Concurrent attempts
Other clarification-dependent behavior
```

Undefined behavior must first be clarified where an expected result cannot be established reliably.

---

## 8. Recommended Testing Focus

The risk analysis indicates that downstream testing should emphasize:

- Boundary behavior around the fifth failed attempt.
- Locked-state authentication enforcement.
- Correct 30-minute state transition.
- Successful-login counter reset.
- New failure sequence after automatic unlock.
- Isolation of failed-login tracking between accounts.
- Repeated transitions between unlocked and locked states.
- Time-boundary behavior.
- Consistency under rapid or concurrent login attempts when expected concurrency behavior is clarified.

These are testing-focus recommendations derived from risk analysis and are not test scenarios or test cases.

---

## 9. Risk Analysis Summary

The feature has a concentrated high-risk area around the relationship between:

```text
Failed-Login Counter
        +
Lock Threshold
        +
Account State
        +
Lock Timer
```

The most important failure modes are:

- Account not locked at the required threshold.
- Account locked earlier than required.
- Authentication allowed during an active lock.
- Incorrect automatic-unlock timing.
- Counter not reset after successful login.
- Failed-login state leaking between accounts.
- Incorrect counter state after automatic unlock.

The requirement provides enough information to assess the primary functional risks.

Risks involving locked-period attempts, timer extension, cross-device tracking, unknown accounts, concurrency, and exact post-unlock counter semantics remain clarification-dependent and must not be assigned invented expected system behavior.