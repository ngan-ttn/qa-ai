# Test Scenarios — Account Lock After Failed Login Attempts

## 1. Scenario Scope

This document defines test scenarios for the Account Lock After Failed Login Attempts feature.

The scenario coverage focuses on:

- Successful authentication.
- Failed-login tracking.
- Five-attempt lock threshold.
- Successful-login counter reset.
- Locked-state authentication.
- Lock-message behavior.
- Automatic unlock.
- Post-unlock failed-login tracking.
- Account-specific failed-login isolation.
- Relevant boundary and state-transition behavior.

Behaviors that are not sufficiently defined by the requirement are identified separately and are not assigned invented expected results.

---

## 2. Test Scenarios

| Scenario ID | Area | Scenario | Coverage Type | Priority | Requirement Traceability |
|---|---|---|---|---|---|
| TS-001 | Authentication | Verify a registered user with valid credentials can log in when the account is not locked. | Positive | Medium | Requirements 1–3 |
| TS-002 | Authentication | Verify login fails when a registered user enters an incorrect password. | Negative | High | Requirement 4 |
| TS-003 | Failed Login Tracking | Verify the first consecutive incorrect-password attempt is recorded and the account remains unlocked. | Boundary | High | Requirements 5–6; AC-01 |
| TS-004 | Failed Login Tracking | Verify the account remains unlocked after four consecutive incorrect-password attempts. | Boundary | High | Requirement 6; AC-01 |
| TS-005 | Account Lock | Verify the account becomes temporarily locked on the fifth consecutive incorrect-password attempt. | Boundary / State Transition | High | Requirements 6, 8; AC-02 |
| TS-006 | Failed Login Tracking | Verify a successful login after one or more but fewer than five consecutive failed attempts resets the failed-login counter. | Positive / State | High | Requirement 7; AC-05 |
| TS-007 | Failed Login Tracking | Verify a new failed-login sequence starts after the counter has been reset by a successful login. | State | High | Requirement 7; AC-05 |
| TS-008 | Account Lock | Verify a locked account cannot authenticate when the correct password is entered. | Negative / State | High | Requirement 10; AC-03 |
| TS-009 | Account Lock | Verify a login attempt against a locked account is rejected when an incorrect password is entered. | Negative / State | High | Requirements 10–11; AC-03 |
| TS-010 | Account Lock | Verify the defined temporary-lock message is displayed when a login attempt is made while the account is locked. | UI / Functional | Medium | Requirement 11; AC-03 |
| TS-011 | Lock Duration | Verify the account remains locked before the 30-minute lock period has expired. | Time Boundary | High | Requirements 9–10 |
| TS-012 | Automatic Unlock | Verify the account is automatically unlocked after the 30-minute lock period expires. | Time Boundary / State Transition | High | Requirement 12; AC-04 |
| TS-013 | Automatic Unlock | Verify the user can successfully log in with valid credentials after the account is automatically unlocked. | Positive / State | High | Requirements 12–13; AC-04 |
| TS-014 | Post-Unlock Tracking | Verify failed-login tracking starts again after the account has been automatically unlocked. | State | High | Requirement 14 |
| TS-015 | Post-Unlock Tracking | Verify previous failed attempts from before the lock do not cause an earlier lock in the new post-unlock tracking sequence. | State / Boundary | High | Requirement 14 |
| TS-016 | Account Isolation | Verify failed login attempts for one registered account do not affect the failed-login state of another registered account. | Isolation | High | Requirement 5; Notes |
| TS-017 | Account Isolation | Verify one account can remain available for authentication while another account is temporarily locked. | Isolation / State | High | Requirements 5, 8–10 |
| TS-018 | Repeated Lifecycle | Verify an account can enter a new lock cycle after automatic unlock when five new consecutive incorrect-password attempts occur. | End-to-End State | High | Requirements 6, 8, 12–14 |
| TS-019 | Counter Reset | Verify multiple successful-login resets do not carry failed attempts from earlier consecutive-failure sequences into later sequences. | State | Medium | Requirement 7 |
| TS-020 | Lock Lifecycle | Verify the complete defined lifecycle from unlocked state through five consecutive failures, temporary lock, automatic unlock, and successful login. | End-to-End | High | Requirements 5–14; AC-01–AC-05 |

---

## 3. Positive Coverage

### TS-001 — Successful Login While Unlocked

Verify a registered user can authenticate successfully when:

- Valid credentials are provided.
- The account is not locked.

Expected behavior is defined by Requirements 1–3.

---

### TS-006 — Successful Login Resets Failed Counter

Verify a successful login resets the failed-login counter when the account has between one and four consecutive failed login attempts.

Representative sequences include:

```text
Fail → Success
Fail → Fail → Success
Fail → Fail → Fail → Success
Fail → Fail → Fail → Fail → Success
```

Each successful login ends the current consecutive-failure sequence.

---

### TS-013 — Successful Login After Automatic Unlock

Verify the user can authenticate again after the defined lock period expires and the account is automatically unlocked.

---

## 4. Negative Coverage

### TS-002 — Incorrect Password

Verify an incorrect password:

- Causes authentication to fail.
- Contributes to the consecutive failed-login sequence for the account.

---

### TS-008 — Correct Password While Locked

Verify valid credentials do not bypass an active account lock.

```text
Account = Locked
Password = Correct

Expected:
Authentication Rejected
```

This is a high-priority scenario because allowing authentication would violate the primary locked-state rule.

---

### TS-009 — Incorrect Password While Locked

Verify authentication remains unavailable when an incorrect password is submitted against an already locked account.

The requirement supports rejection of authentication.

The effect of this attempt on the counter or lock timer is not defined and must not be assumed.

---

## 5. Boundary Coverage

### Failed-Login Threshold

The critical threshold is five consecutive failed login attempts.

```text
0 → Unlocked
1 → Unlocked
2 → Unlocked
3 → Unlocked
4 → Unlocked
5 → Locked
```

Primary scenarios:

- TS-003 verifies the lower sequence begins correctly.
- TS-004 verifies the account remains unlocked immediately below the threshold.
- TS-005 verifies the transition at the threshold.

The most critical boundary is:

```text
4 Failed Attempts
       ↓
5th Failed Attempt
       ↓
Locked
```

---

### Lock Duration

The lock duration is 30 minutes.

Relevant defined coverage:

```text
Before 30-minute expiration
→ Locked

After 30-minute period expires
→ Automatically Unlocked
```

The exact behavior at the precise expiration instant requires clarification before assigning a more specific expected result.

---

## 6. State Transition Coverage

The primary states are:

```text
UNLOCKED
LOCKED
```

### Transition 1 — Unlocked to Locked

```text
UNLOCKED
   │
   │ 5 consecutive incorrect-password attempts
   ▼
LOCKED
```

Covered by:

- TS-003
- TS-004
- TS-005

### Transition 2 — Locked to Unlocked

```text
LOCKED
   │
   │ 30-minute lock period expires
   ▼
UNLOCKED
```

Covered by:

- TS-011
- TS-012
- TS-013

### Counter Reset Without Lock-State Change

```text
UNLOCKED
   │
   │ 1–4 failed attempts
   │ followed by successful login
   ▼
UNLOCKED
Failed Counter Reset
```

Covered by:

- TS-006
- TS-007
- TS-019

### Repeated Lock Cycle

```text
UNLOCKED
    ↓
5 Failures
    ↓
LOCKED
    ↓
30-Minute Expiration
    ↓
UNLOCKED
    ↓
5 New Failures
    ↓
LOCKED
```

Covered by TS-018.

---

## 7. Account Isolation Coverage

The requirement explicitly states that failed-login attempts are tracked separately for each account.

Representative coverage:

```text
Account A
Failed Count = 4

Account B
Failed Count = 0
```

A failed attempt against Account A must not modify Account B's failed-login state.

The following scenarios cover account isolation:

- TS-016 — independent failed-login tracking.
- TS-017 — independent account lock state.

---

## 8. Requirement Coverage Matrix

| Requirement / AC | Covered By |
|---|---|
| Requirement 1 | TS-001 |
| Requirement 2 | TS-001, TS-002 |
| Requirement 3 | TS-001 |
| Requirement 4 | TS-002 |
| Requirement 5 | TS-003, TS-016, TS-017 |
| Requirement 6 | TS-003, TS-004, TS-005, TS-018 |
| Requirement 7 | TS-006, TS-007, TS-019 |
| Requirement 8 | TS-005, TS-017, TS-018 |
| Requirement 9 | TS-011, TS-012 |
| Requirement 10 | TS-008, TS-009, TS-011 |
| Requirement 11 | TS-009, TS-010 |
| Requirement 12 | TS-012, TS-013, TS-018 |
| Requirement 13 | TS-013 |
| Requirement 14 | TS-014, TS-015, TS-018 |
| AC-01 | TS-003, TS-004 |
| AC-02 | TS-005 |
| AC-03 | TS-008, TS-009, TS-010 |
| AC-04 | TS-012, TS-013 |
| AC-05 | TS-006, TS-007 |

---

## 9. Clarification-Dependent Scenarios

The following areas are relevant to testing but do not have sufficiently defined expected behavior.

They should not be converted into executable scenarios with assumed expected results until clarification is available.

| Item ID | Area | Potential Scenario | Missing Information |
|---|---|---|---|
| CD-001 | Lock Timer | Login exactly at the 30-minute expiration boundary. | Exact timer-boundary semantics are undefined. |
| CD-002 | Locked Attempts | Verify counter behavior when login attempts occur while locked. | Effect on failed-login counter is undefined. |
| CD-003 | Lock Extension | Verify whether repeated attempts while locked affect lock expiration. | Timer extension/restart behavior is undefined. |
| CD-004 | Cross-Device | Verify failed-login accumulation across multiple devices or browsers. | Cross-device/session tracking behavior is not explicit. |
| CD-005 | Unknown Account | Verify failed-login behavior for an unregistered email address. | Unknown-account behavior is undefined. |
| CD-006 | Concurrency | Verify two simultaneous failed attempts when the account currently has four failures. | Concurrent counter/locking semantics are undefined. |
| CD-007 | Post-Unlock Counter | Verify the exact numeric counter immediately after automatic unlock. | Requirement states tracking starts again but does not explicitly define the numeric reset value. |

---

## 10. Scenario Coverage Summary

The scenario set covers the requirement-defined behavior across:

```text
Authentication
      +
Failed-Login Tracking
      +
Threshold Boundary
      +
Counter Reset
      +
Account Lock
      +
Locked-State Enforcement
      +
Lock Duration
      +
Automatic Unlock
      +
Post-Unlock Tracking
      +
Account Isolation
      +
Repeated State Lifecycle
```

The highest-priority coverage focuses on:

1. The `4 → 5` failed-attempt boundary.
2. Authentication rejection while locked.
3. The 30-minute lock lifecycle.
4. Successful-login counter reset.
5. Post-unlock tracking.
6. Account-specific isolation.

Behavior not defined by the requirement remains explicitly separated as clarification-dependent coverage rather than receiving invented expected results.