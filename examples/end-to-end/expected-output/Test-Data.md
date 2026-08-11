# Test Data — Account Lock After Failed Login Attempts

## 1. Overview

This artifact defines the logical test data required to execute the confirmed test cases for the Account Lock After Failed Login Attempts feature.

The data is derived from:

- `Sample-Requirement.md`
- `Requirement-Analysis.md`
- `Business-Rules.md`
- `Risk-Analysis.md`
- `Test-Scenarios.md`
- `Test-Cases.md`
- `Coverage-Review.md`

The confirmed executable baseline is:

```text
TC-001 → TC-020
```

Clarification-dependent candidates are excluded from confirmed test-data generation.

This artifact defines the data and system states required for testing.

It does not define implementation-specific setup mechanisms such as:

- SQL scripts.
- API calls.
- Database fields.
- Admin portals.
- Internal service endpoints.

Those details require additional system context.

---

## 2. Test Data Principles

The test data should satisfy the following principles:

1. Use synthetic, non-production accounts.
2. Keep account states isolated between scenarios where required.
3. Distinguish input data from system state.
4. Preserve the requirement-defined five-attempt threshold.
5. Preserve the 30-minute lock duration.
6. Avoid relying on uncontrolled state left by previous test execution.
7. Reuse accounts only when the required initial state can be restored reliably.
8. Do not assign values for undefined behavior.
9. Use placeholders for environment-specific secrets and credentials.

---

## 3. Data Categories

The feature requires four primary data categories:

```text
Credential Data
      +
Account State
      +
Failed-Login Sequence State
      +
Time-Based Lock State
```

Additional isolation data is required for multi-account scenarios.

---

## 4. Account Test Data

| Data ID | Account | Example Email | Valid Password Reference | Initial Logical State | Primary Purpose |
|---|---|---|---|---|---|
| TD-ACC-001 | Account A | `qa.lock.a@example.com` | `<VALID_PASSWORD_A>` | Registered / Unlocked / Fresh failure sequence | Normal authentication and threshold testing |
| TD-ACC-002 | Account B | `qa.lock.b@example.com` | `<VALID_PASSWORD_B>` | Registered / Unlocked / Fresh failure sequence | Account-isolation testing |
| TD-ACC-003 | Account C | `qa.lock.c@example.com` | `<VALID_PASSWORD_C>` | Registered / Unlocked / Fresh failure sequence | Successful-login reset testing |
| TD-ACC-004 | Account D | `qa.lock.d@example.com` | `<VALID_PASSWORD_D>` | Registered / Unlocked / Four consecutive failures | Fifth-failure lock testing |
| TD-ACC-005 | Account E | `qa.lock.e@example.com` | `<VALID_PASSWORD_E>` | Registered / Locked / Active lock period | Locked-state authentication testing |
| TD-ACC-006 | Account F | `qa.lock.f@example.com` | `<VALID_PASSWORD_F>` | Registered / Locked / Lock period ready to expire | Automatic-unlock testing |
| TD-ACC-007 | Account G | `qa.lock.g@example.com` | `<VALID_PASSWORD_G>` | Registered / Automatically unlocked | Post-unlock tracking |
| TD-ACC-008 | Account H | `qa.lock.h@example.com` | `<VALID_PASSWORD_H>` | Registered / Automatically unlocked / Fresh post-unlock sequence | Repeated lifecycle testing |

The account names and email addresses are illustrative synthetic values.

Password references are placeholders and must be resolved to approved non-production credentials in the execution environment.

---

## 5. Password Data

| Data ID | Type | Placeholder | Usage |
|---|---|---|---|
| TD-PWD-001 | Correct password for Account A | `<VALID_PASSWORD_A>` | Normal successful authentication |
| TD-PWD-002 | Correct password for Account B | `<VALID_PASSWORD_B>` | Account-isolation authentication |
| TD-PWD-003 | Correct password for Account C | `<VALID_PASSWORD_C>` | Counter-reset authentication |
| TD-PWD-004 | Generic incorrect password | `<INVALID_PASSWORD_1>` | Failed-login generation |
| TD-PWD-005 | Alternate incorrect password | `<INVALID_PASSWORD_2>` | Optional repeated-failure variation |
| TD-PWD-006 | Correct password for locked Account E | `<VALID_PASSWORD_E>` | Verify valid credentials cannot bypass lock |

The requirement does not require different incorrect values for each failed attempt.

The same incorrect password may therefore be reused unless the execution environment imposes additional constraints.

Placeholder values do not imply any password-format or password-policy requirement.

---

## 6. Failed-Login State Data

The threshold logic requires representative failure-sequence states.

| State ID | Consecutive Failed Attempts | Required Account State | Purpose |
|---|---:|---|---|
| TD-STATE-000 | 0 | Unlocked | Fresh baseline |
| TD-STATE-001 | 1 | Unlocked | First-failure coverage |
| TD-STATE-003 | 3 | Unlocked | Sequence-reset coverage |
| TD-STATE-004 | 4 | Unlocked | Immediately below threshold |
| TD-STATE-005 | 5 reached | Locked | Threshold transition result |

Confirmed relationship:

```text
0–4 consecutive failures
→ Account remains unlocked

5th consecutive failure
→ Account becomes locked
```

These represent logical business states, not assumed database values.

---

## 7. Successful-Login Reset Data

### TD-SET-RESET-001 — Reset After One Failure

```text
Account:
TD-ACC-003

Initial State:
Unlocked

Current Consecutive Failures:
1

Next Input:
Correct Password
```

Expected transition:

```text
1 Failure
   ↓
Successful Login
   ↓
Previous Failure Sequence Reset
```

Supports:

- TC-007

---

### TD-SET-RESET-002 — Reset Immediately Below Threshold

```text
Account:
TD-ACC-003

Initial State:
Unlocked

Current Consecutive Failures:
4

Next Input:
Correct Password
```

Expected transition:

```text
4 Failures
   ↓
Successful Login
   ↓
Previous Sequence Reset
```

Supports:

- TC-008

---

### TD-SET-RESET-003 — Interrupted Sequences

```text
Sequence A:
3 consecutive failures

Interruption:
Successful login

Sequence B:
2 consecutive failures
```

Required relationship:

```text
3 + Success + 2
≠
5 Consecutive Failures
```

Supports:

- TC-009

---

## 8. Threshold Data

### TD-SET-THRESHOLD-001 — Below Threshold

```text
Account State:
Unlocked

Consecutive Failures:
4
```

Expected state:

```text
Unlocked
```

Supports:

- TC-005

---

### TD-SET-THRESHOLD-002 — Threshold Transition

```text
Initial Consecutive Failures:
4

Next Input:
Incorrect Password
```

Expected transition:

```text
4
↓
5th Failure
↓
Locked
```

Supports:

- TC-006

---

## 9. Account Isolation Data

### TD-SET-ISOLATION-001 — Independent Failure Sequences

| Attribute | Account A | Account B |
|---|---|---|
| Account | TD-ACC-001 | TD-ACC-002 |
| Initial State | Unlocked | Unlocked |
| Failure Sequence | 4 failures | 1 failure |
| Required State | Unlocked | Unlocked |
| Required Isolation | Account A failures remain Account A-specific | Account B failure remains Account B-specific |

Confirmed requirement relationship:

```text
Account A Failed State
        │
        └── MUST NOT become Account B Failed State
```

Supports:

- TC-010

---

### TD-SET-ISOLATION-002 — Authentication of Unaffected Account

| Attribute | Account A | Account B |
|---|---|---|
| Account | Account A | TD-ACC-002 |
| State | Locked | Unlocked |
| Next Action | None | Valid authentication |
| Required Result | Remains independent | Authentication succeeds |

Supports:

- TC-011

---

## 10. Locked-State Data

### TD-SET-LOCKED-001 — Correct Password During Active Lock

```text
Account:
TD-ACC-005

State:
Locked

Lock Period:
Active

Input:
Correct Password
```

Required behavior:

```text
Locked + Correct Password
→ Authentication Rejected
```

Supports:

- TC-012

---

### TD-SET-LOCKED-002 — Generic Login During Active Lock

```text
Account:
TD-ACC-005

State:
Locked

Lock Period:
Active
```

Required behavior:

```text
Authentication Not Allowed
```

The data does not define whether the attempt affects:

- Failed-login counter.
- Lock timer.

Those behaviors remain undefined.

Supports:

- TC-013
- TC-014

---

## 11. Lock Message Data

Required message:

```text
Your account has been temporarily locked. Please try again later.
```

This exact value is used as expected data for:

```text
TC-014
TC-020
```

No alternative text is defined by the requirement.

---

## 12. Time-Based Data

The requirement defines:

```text
Temporary Lock Duration = 30 minutes
```

Logical time states:

| Data ID | Time Condition | Required Business State | Purpose |
|---|---|---|---|
| TD-TIME-001 | Lock period has not expired | Locked | Pre-expiration verification |
| TD-TIME-002 | 30-minute lock period has expired | Automatically unlocked | Expiration/recovery verification |

### TD-TIME-001

Supports:

- TC-015

Required relationship:

```text
Before expiration
→ Account remains locked
```

### TD-TIME-002

Supports:

- TC-016
- TC-017

Required relationship:

```text
Lock period expired
→ Automatic unlock
```

The exact behavior at the precise expiration instant is not encoded because it is clarification-dependent.

---

## 13. Automatic-Unlock Data

### TD-SET-UNLOCK-001

```text
Account:
TD-ACC-006

Previous State:
Locked

Lock Duration:
30 minutes

Current Condition:
Lock period expired
```

Expected transition:

```text
LOCKED
   ↓
Expiration
   ↓
UNLOCKED
```

Supports:

- TC-016

---

### TD-SET-POST-UNLOCK-001

```text
Account:
TD-ACC-007

Previous State:
Locked

Current State:
Automatically unlocked

Credentials:
Valid
```

Expected behavior:

```text
Authentication Available Again
```

Supports:

- TC-017

---

## 14. Post-Unlock Tracking Data

### TD-SET-POST-TRACK-001

```text
Account:
TD-ACC-007

Current State:
Automatically unlocked

New Incorrect Attempts:
4
```

Expected relationship:

```text
Post-Unlock Failures 1–4
→ Account remains unlocked
```

This demonstrates that a new failure sequence is being evaluated after unlock.

The artifact does not assign an internal numeric reset value unless the implementation provides one.

Supports:

- TC-018

---

## 15. Repeated Lifecycle Data

### TD-SET-LIFECYCLE-001

```text
Account:
TD-ACC-008

Previous Lifecycle:
Unlocked
→ 5 failures
→ Locked
→ 30-minute expiration
→ Automatically unlocked

Next Sequence:
5 new consecutive incorrect-password attempts
```

Expected relationship:

```text
Automatically Unlocked
        ↓
New Failures 1–4
→ Unlocked
        ↓
New Failure 5
→ Locked Again
```

Supports:

- TC-019

---

## 16. End-to-End Lifecycle Data

### TD-SET-E2E-001

```text
Account:
Registered synthetic account

Initial State:
Unlocked

Failure Sequence:
Fresh

Valid Credential:
Available through approved non-production credential reference

Incorrect Credential:
Available through synthetic invalid-password reference

Lock Threshold:
5 consecutive failures

Lock Duration:
30 minutes
```

Execution states required:

```text
Unlocked
   ↓
Valid Authentication
   ↓
Return to Login Flow
   ↓
Failures 1–4
   ↓
Unlocked
   ↓
Failure 5
   ↓
Locked
   ↓
Correct Password During Lock
   ↓
Rejected
   ↓
30-Minute Expiration
   ↓
Automatically Unlocked
   ↓
Valid Authentication
```

Supports:

- TC-020

---

## 17. Test Case-to-Data Mapping

| Test Case | Required Test Data |
|---|---|
| TC-001 | TD-ACC-001, TD-PWD-001, TD-STATE-000 |
| TC-002 | TD-ACC-001, TD-PWD-004, TD-STATE-000 |
| TC-003 | TD-ACC-001, TD-PWD-004, TD-STATE-000 through TD-STATE-004 |
| TC-004 | TD-ACC-001, TD-PWD-004, TD-STATE-000 |
| TC-005 | TD-SET-THRESHOLD-001 |
| TC-006 | TD-SET-THRESHOLD-002 |
| TC-007 | TD-SET-RESET-001 |
| TC-008 | TD-SET-RESET-002 |
| TC-009 | TD-SET-RESET-003 |
| TC-010 | TD-SET-ISOLATION-001 |
| TC-011 | TD-SET-ISOLATION-002, TD-PWD-002 |
| TC-012 | TD-SET-LOCKED-001 |
| TC-013 | TD-SET-LOCKED-002 |
| TC-014 | TD-SET-LOCKED-002, Required Lock Message |
| TC-015 | TD-ACC-005, TD-TIME-001 |
| TC-016 | TD-SET-UNLOCK-001, TD-TIME-002 |
| TC-017 | TD-SET-POST-UNLOCK-001 |
| TC-018 | TD-SET-POST-TRACK-001 |
| TC-019 | TD-SET-LIFECYCLE-001 |
| TC-020 | TD-SET-E2E-001 |

```text
20 / 20 confirmed test cases
→ Test-data support available
```

---

## 18. Data Reuse Rules

Account data may be reused only when the required initial state is known and controllable.

For example:

```text
TC modifies failed-login state
        ↓
State must be restored
        OR
Use isolated account
```

Stateful test cases include:

- Failed-login tracking.
- Counter reset.
- Lock threshold.
- Locked state.
- Automatic unlock.
- Post-unlock tracking.
- Repeated lifecycle.

Uncontrolled reuse may cause false results.

---

## 19. Data Isolation Requirements

Because failed-login tracking is account-specific:

- Accounts used for independent scenarios should not unintentionally share modified state.
- Account A and Account B must remain independent during isolation tests.
- A locked account should not be reused for an unlocked-state test unless its required state has been restored.
- A failure sequence should not be assumed fresh unless the test setup guarantees it.

These constraints are derived from the requirement's account-specific behavior.

---

## 20. Sensitive Data Guidance

The example uses synthetic account identifiers and credential placeholders only.

Do not use:

```text
Production user email
Production password
Real customer authentication data
Copied production credentials
```

Actual execution should resolve placeholders to approved non-production credentials without committing real secrets to the example artifact.

---

## 21. Clarification-Dependent Data

No confirmed test data is generated for the unresolved candidates:

| Candidate | Potential Data Need | Status |
|---|---|---|
| CTS-001 | Locked account with additional attempts and observable counter state | Clarification Required |
| CTS-002 | Locked account with repeated attempts and observable timer state | Clarification Required |
| CTS-003 | Account positioned exactly at expiration boundary | Clarification Required |
| CTS-004 | Same account across multiple browsers | Clarification Required |
| CTS-005 | Same account across multiple devices | Clarification Required |
| CTS-006 | Account at four failures with concurrent requests | Clarification / Investigation Required |
| CTS-007 | Account locked while an authenticated session exists | Clarification Required |
| CTS-008 | Locked account combined with password reset/change state | Clarification Required |
| CTS-009 | Unregistered email input with failed-login tracking behavior | Clarification Required |

These states may be added after expected behavior is confirmed.

---

## 22. Implementation-Dependent Setup

The requirement does not specify how test states are created.

For example, this artifact may require logical states such as:

```text
Account with 4 consecutive failures
Locked account
Lock period expired
Automatically unlocked account
```

But it does not define whether those states should be prepared through:

```text
UI actions
API
Database
Test fixture
Administrative tool
Clock control
Mock
```

The appropriate setup mechanism must be determined from the actual test environment and system architecture.

---

## 23. Data Coverage Summary

The generated test-data model supports:

```text
20 Confirmed Test Cases
```

across:

```text
Credentials
      +
Failure Sequences
      +
Threshold States
      +
Reset States
      +
Account Isolation
      +
Locked State
      +
Time Conditions
      +
Automatic Unlock
      +
Post-Unlock Tracking
      +
Repeated Lifecycle
```

The confirmed chain is:

```text
Requirement
    ↓
Business Rules
    ↓
Risks
    ↓
Test Scenarios
    ↓
Test Cases
    ↓
Coverage Review
    ↓
Test Data
```

No implementation-specific setup mechanism, real credential value, or clarification-dependent business behavior is fabricated.