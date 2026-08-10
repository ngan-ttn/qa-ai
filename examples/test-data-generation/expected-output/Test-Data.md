# Test Data — Account Lock After Failed Login Attempts

## 1. Test Data Summary

This document defines representative test data for the Account Lock After Failed Login Attempts feature.

The test data supports the supplied test scenarios covering:

- Successful authentication.
- Incorrect-password authentication.
- Failed-login threshold boundaries.
- Successful-login counter reset.
- Temporary account lock.
- Lock-duration validation.
- Automatic unlock.
- Post-unlock failed-login tracking.
- Account isolation.
- Repeated lock/unlock lifecycle.

The data is illustrative and must not contain real user credentials or production-sensitive information.

System states that are not fully defined by the requirement are not assigned fabricated values.

---

## 2. Data Conventions

The following conventions are used throughout this example.

| Convention | Description |
|---|---|
| `TD-ACC-*` | Registered account test data |
| `TD-PWD-*` | Password input data |
| `TD-STATE-*` | Required account/system state |
| `TD-TIME-*` | Time-based lock condition |
| `TD-SET-*` | Reusable combined test-data set |

Example email addresses use the reserved `example.com` domain.

Passwords shown in this document are synthetic example values only.

---

## 3. Registered Account Data

| Data ID | Account | Email | Valid Password | Required Initial State | Purpose |
|---|---|---|---|---|---|
| TD-ACC-001 | Account A | `qa.lock.a@example.com` | `ValidPass_A1!` | Registered / Unlocked | Primary authentication and failed-login testing |
| TD-ACC-002 | Account B | `qa.lock.b@example.com` | `ValidPass_B1!` | Registered / Unlocked | Account-isolation testing |
| TD-ACC-003 | Account C | `qa.lock.c@example.com` | `ValidPass_C1!` | Registered / Unlocked | Counter-reset testing |
| TD-ACC-004 | Account D | `qa.lock.d@example.com` | `ValidPass_D1!` | Registered / Unlocked | Lock-threshold testing |
| TD-ACC-005 | Account E | `qa.lock.e@example.com` | `ValidPass_E1!` | Registered / Locked | Active-lock testing |
| TD-ACC-006 | Account F | `qa.lock.f@example.com` | `ValidPass_F1!` | Registered / Lock period expired | Automatic-unlock testing |
| TD-ACC-007 | Account G | `qa.lock.g@example.com` | `ValidPass_G1!` | Registered / Automatically unlocked | Post-unlock tracking |
| TD-ACC-008 | Account H | `qa.lock.h@example.com` | `ValidPass_H1!` | Registered / Automatically unlocked | Repeated lock-cycle testing |

The actual mechanism used to establish a required account state is environment-dependent and is not defined by this example.

---

## 4. Password Input Data

| Data ID | Data Type | Example Value | Purpose |
|---|---|---|---|
| TD-PWD-001 | Correct password for Account A | `ValidPass_A1!` | Successful authentication |
| TD-PWD-002 | Incorrect password | `WrongPass_01!` | Failed-login generation |
| TD-PWD-003 | Incorrect password | `WrongPass_02!` | Repeated failed-login generation |
| TD-PWD-004 | Correct password for Account B | `ValidPass_B1!` | Account-isolation verification |
| TD-PWD-005 | Correct password for Account C | `ValidPass_C1!` | Counter-reset verification |
| TD-PWD-006 | Correct password for locked account | `ValidPass_E1!` | Verify correct password cannot bypass lock |

For consecutive-failure scenarios, the same incorrect password may be reused unless the execution environment imposes a different constraint.

---

## 5. Failed-Login State Data

The following account states support threshold and counter-reset scenarios.

| State ID | Account State | Consecutive Failed Attempts | Expected Requirement State | Primary Use |
|---|---|---:|---|---|
| TD-STATE-001 | Unlocked | 0 | Account unlocked | Baseline authentication |
| TD-STATE-002 | Unlocked | 1 | Account unlocked | Counter-reset coverage |
| TD-STATE-003 | Unlocked | 3 | Account unlocked | Counter-reset coverage |
| TD-STATE-004 | Unlocked | 4 | Account unlocked | Immediately below lock threshold |
| TD-STATE-005 | Locked | 5 consecutive failures reached | Account temporarily locked | Locked-state validation |

The requirement-defined threshold is:

```text
0–4 Consecutive Failed Attempts
→ Account Unlocked

5th Consecutive Failed Attempt
→ Account Locked
```

`TD-STATE-005` describes the resulting business state rather than requiring a particular internal database representation.

---

## 6. Counter Reset Data

Counter-reset testing requires an unlocked account with an active failed-login sequence below the threshold.

### Data Set: TD-SET-RESET-001

```text
Account:
TD-ACC-003

Initial State:
Unlocked

Consecutive Failed Attempts:
3

Next Credential:
Correct Password
```

Expected requirement transition:

```text
3 Consecutive Failures
        ↓
Successful Login
        ↓
Failed-Login Counter Reset
```

After the successful login, subsequent failed attempts must belong to a new consecutive-failure sequence according to the reset rule.

The exact internal representation of the reset counter is not assumed.

---

## 7. Lock Threshold Data

### Data Set: TD-SET-LOCK-001

```text
Account:
TD-ACC-004

Initial State:
Unlocked

Consecutive Failed Attempts:
4

Next Credential:
Incorrect Password
```

Expected requirement transition:

```text
4 Consecutive Failures
        ↓
Incorrect Password
        ↓
5th Consecutive Failure
        ↓
Account Locked
```

This data set supports the critical `4 → 5` boundary.

---

## 8. Locked Account Data

### Data Set: TD-SET-LOCKED-001

```text
Account:
TD-ACC-005

State:
Temporarily Locked

Lock Period:
Active

Credential Used:
Correct Password
```

Expected requirement behavior:

```text
Locked Account
      +
Correct Password
      ↓
Authentication Rejected
```

The test data does not define whether the attempted login modifies the failed-login counter or lock timer because those behaviors are not specified.

---

## 9. Lock Duration Data

The feature requires a 30-minute temporary lock.

The following logical time states are required.

| Data ID | Lock Condition | Elapsed-Time Relationship | Required Account State | Purpose |
|---|---|---|---|---|
| TD-TIME-001 | Active lock | Less than 30 minutes elapsed | Locked | Verify account remains locked before expiration |
| TD-TIME-002 | Expired lock | 30-minute lock period has expired | Eligible for automatic unlock | Verify automatic unlock |

The example intentionally expresses time as a relationship to the lock period rather than inventing exact timestamps.

For example:

```text
TD-TIME-001
Lock period has not expired

TD-TIME-002
30-minute lock period has expired
```

The precise timer-start event and exact expiration-instant semantics require clarification and therefore are not encoded as assumed data rules.

---

## 10. Automatic Unlock Data

### Data Set: TD-SET-UNLOCK-001

```text
Account:
TD-ACC-006

Previous State:
Temporarily Locked

Lock Duration:
30 minutes

Current Condition:
Lock period has expired

Credential:
Correct Password
```

Expected requirement transition:

```text
Locked
   ↓
30-Minute Period Expires
   ↓
Automatically Unlocked
   ↓
Login Available Again
```

No manual unlock action should be required.

---

## 11. Post-Unlock Tracking Data

### Data Set: TD-SET-POST-UNLOCK-001

```text
Account:
TD-ACC-007

Previous State:
Temporarily Locked

Current State:
Automatically Unlocked

Tracking Condition:
Failed-login tracking has started again

Input:
Incorrect Password
```

This data set supports verification that new failed-login activity can be tracked after automatic unlock.

The requirement states that failed-login tracking starts again.

It does not explicitly define the numeric internal counter value immediately after unlock, so this data set does not assign one.

---

## 12. Account Isolation Data

Account-specific tracking requires at least two independent registered accounts.

### Data Set: TD-SET-ISOLATION-001

| Attribute | Account A | Account B |
|---|---|---|
| Account Data | TD-ACC-001 | TD-ACC-002 |
| Email | `qa.lock.a@example.com` | `qa.lock.b@example.com` |
| Initial State | Unlocked | Unlocked |
| Failed-Login Activity | Four consecutive incorrect-password attempts | None |
| Authentication Input | Incorrect password | Correct password |
| Required Isolation | Failed state belongs only to Account A | Must remain unaffected by Account A |

Required relationship:

```text
Account A
Failed Count = 4
        │
        └──── must not affect ────► Account B
                                    Login Available
```

This data set validates account-level isolation without assuming implementation details for state storage.

---

## 13. Repeated Lifecycle Data

### Data Set: TD-SET-LIFECYCLE-001

```text
Account:
TD-ACC-008

Previous Lifecycle:
5 Consecutive Failures
→ Locked
→ 30-Minute Period Expired
→ Automatically Unlocked

Current Requirement State:
Failed-login tracking has started again

Next Inputs:
5 Consecutive Incorrect Password Attempts
```

Expected requirement transition:

```text
Automatically Unlocked
        ↓
New Failed-Login Tracking
        ↓
Failures 1–4
        ↓
Remain Unlocked
        ↓
Failure 5
        ↓
Locked Again
```

This data set supports repeated account-lock lifecycle verification.

---

## 14. Scenario-to-Data Mapping

| Scenario ID | Required Test Data |
|---|---|
| TS-001 | TD-ACC-001, TD-PWD-001, TD-STATE-001 |
| TS-002 | TD-ACC-001, TD-PWD-002, TD-STATE-001 |
| TS-003 | TD-ACC-004, TD-PWD-002, TD-STATE-001 through TD-STATE-004 |
| TS-004 | TD-SET-LOCK-001 |
| TS-005 | TD-SET-RESET-001 |
| TS-006 | TD-SET-LOCKED-001 |
| TS-007 | TD-ACC-005, TD-TIME-001, TD-PWD-006 |
| TS-008 | TD-SET-UNLOCK-001, TD-TIME-002 |
| TS-009 | TD-SET-POST-UNLOCK-001 |
| TS-010 | TD-SET-ISOLATION-001 |
| TS-011 | TD-SET-LIFECYCLE-001 |

All supplied test scenarios have corresponding test-data support.

---

## 15. Data Reuse Strategy

Test accounts may be reused only when the required initial state can be reliably restored.

For example:

```text
Authentication Test
      ↓
State Modified?
   ┌──┴──┐
  No    Yes
  │      │
Reuse   Restore / Use
Data    Isolated Account
```

Stateful scenarios involving:

- Failed-login counters.
- Account locking.
- Lock expiration.
- Automatic unlock.

should not rely on uncontrolled state left by previous test execution.

Independent accounts are preferable when state restoration cannot be guaranteed.

---

## 16. Data Isolation Requirements

Because failed-login tracking is account-specific:

- Each account's failed-login state must remain independent.
- Parallel or sequential execution must not unintentionally reuse modified account state.
- A test that changes an account's failure count must account for that state before the account is reused.
- Locked accounts must not be reused for unlocked-state scenarios unless the required state has been restored.

These are test-data management constraints derived from the account-specific requirement, not implementation assumptions.

---

## 17. Sensitive Data Guidance

The example credentials in this document are synthetic.

Actual test execution should use approved non-production test accounts.

Do not use:

- Production user credentials.
- Real customer email addresses.
- Real customer passwords.
- Credentials copied from production environments.
- Other sensitive production authentication data.

Test data should remain appropriate for the target QA environment.

---

## 18. Clarification-Dependent Test Data

The following data conditions should not be generated as confirmed expected-state data until the corresponding behavior is clarified.

| Item ID | Area | Potential Data Need | Reason |
|---|---|---|---|
| CD-001 | Cross-Device | Same account with failure state distributed across multiple devices or browsers | Cross-device/session tracking behavior is not explicit |
| CD-002 | Concurrency | Account positioned near threshold for simultaneous login requests | Concurrent update semantics are undefined |
| CD-003 | Unknown Account | Email address not associated with a registered account | Unknown-account failed-login behavior is undefined |
| CD-004 | Locked Attempts | Locked account with additional failed attempts | Counter behavior during lock is undefined |
| CD-005 | Lock Extension | Locked account receiving attempts before expiration | Timer restart/extension behavior is undefined |
| CD-006 | Exact Expiration | Lock state positioned exactly at the expiration instant | Exact timer-boundary semantics are undefined |
| CD-007 | Post-Unlock Counter | Explicit numeric counter immediately after automatic unlock | Numeric reset value is not explicitly defined |

These data needs may be added after the relevant expected behavior is confirmed.

---

## 19. Test Data Coverage Summary

The generated test data supports all supplied test scenarios across:

```text
Valid Credentials
      +
Invalid Credentials
      +
Failed-Login States
      +
4 → 5 Threshold
      +
Counter Reset
      +
Locked Account
      +
Active Lock Period
      +
Expired Lock Period
      +
Automatic Unlock
      +
Post-Unlock Tracking
      +
Account Isolation
      +
Repeated Lock Lifecycle
```

The data set separates:

```text
Input Data
→ Email / Password

System State
→ Failed Count / Lock State

Time Condition
→ Active / Expired Lock

Combined Data Set
→ Scenario-ready data
```

Undefined requirement behavior remains clarification-dependent and is not represented as confirmed test-data constraints.