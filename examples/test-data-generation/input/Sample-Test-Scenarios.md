# Sample Test Scenarios — Account Lock After Failed Login Attempts

## 1. Scope

The following test scenarios define the testing objectives for which test data must be prepared.

The scenarios focus on authentication credentials, failed-login state, lock-threshold boundaries, counter reset, lock duration, automatic unlock, post-unlock tracking, and account isolation.

---

## 2. Test Scenarios

| Scenario ID | Area | Scenario | Coverage Type | Priority | Requirement Traceability |
|---|---|---|---|---|---|
| TS-001 | Authentication | Verify a registered user with valid credentials can log in when the account is not locked. | Positive | Medium | Requirements 1–3 |
| TS-002 | Authentication | Verify login fails when a registered user enters an incorrect password. | Negative | High | Requirement 4 |
| TS-003 | Failed Login Tracking | Verify the account remains unlocked after four consecutive incorrect-password attempts. | Boundary | High | Requirement 6; AC-01 |
| TS-004 | Account Lock | Verify the account becomes temporarily locked on the fifth consecutive incorrect-password attempt. | Boundary / State Transition | High | Requirements 6, 8; AC-02 |
| TS-005 | Counter Reset | Verify a successful login before the fifth consecutive failed attempt resets the failed-login counter. | Positive / State | High | Requirement 7; AC-05 |
| TS-006 | Locked State | Verify a temporarily locked account cannot authenticate even when the correct password is entered. | Negative / State | High | Requirement 10; AC-03 |
| TS-007 | Lock Duration | Verify the account remains locked before the 30-minute lock period expires. | Time Boundary | High | Requirements 9–10 |
| TS-008 | Automatic Unlock | Verify the account is automatically unlocked after the 30-minute lock period expires. | Time Boundary / State Transition | High | Requirements 12–13; AC-04 |
| TS-009 | Post-Unlock Tracking | Verify failed-login tracking starts again after the account has been automatically unlocked. | State | High | Requirement 14 |
| TS-010 | Account Isolation | Verify failed login attempts for one registered account do not affect another registered account. | Isolation | High | Requirement 5; Notes |
| TS-011 | Repeated Lifecycle | Verify an automatically unlocked account can be locked again after five new consecutive incorrect-password attempts. | State / Boundary | High | Requirements 6, 8, 12–14 |

---

## 3. Test Data Needs

The scenario set requires representative data for the following states and conditions.

### Authentication Credentials

- Registered account with valid credentials.
- Correct password.
- Incorrect password.

### Failed-Login States

Representative account states are required for:

```text
Failed Count = 0
Failed Count = 1
Failed Count = 3
Failed Count = 4
```

These states support normal, reset, and threshold-boundary scenarios.

### Account Lock States

Representative accounts are required for:

```text
Unlocked
Locked
Automatically Unlocked
```

### Time-Based States

Test data must support distinguishing:

```text
Active Lock
→ Lock period has not expired

Expired Lock
→ 30-minute lock period has expired
```

The exact implementation used to establish these states is outside the scope of this input.

### Account Isolation

At least two independent registered accounts are required so that failed-login state can be manipulated for one account without affecting the other.

---

## 4. Data Constraints

The generated test data must respect the following confirmed requirement constraints:

```text
Lock Threshold = 5 consecutive failed attempts

Lock Duration = 30 minutes

Tracking Scope = Per account

Successful Login Before Threshold
→ Failed-login counter reset

Automatic Unlock
→ Failed-login tracking starts again
```

---

## 5. Undefined Data Conditions

The following potential data states depend on behavior that is not sufficiently defined by the requirement:

- Failed-login state across different browsers or devices.
- Concurrent failed-login updates.
- Failed-login tracking for an unregistered email address.
- Counter changes caused by attempts during an active lock.
- Lock expiration changes caused by attempts during an active lock.
- Exact numeric failed-login counter immediately after automatic unlock.

These conditions should not be assigned assumed system states by the test-data generator.

---

## 6. Scenario Notes

- Test data should be reusable across scenarios where isolation can be maintained.
- Account state must be clearly identified before execution.
- Test data must distinguish input values from required system state.
- Sensitive or real-user credentials must not be used in example test data.
- Undefined system behavior must not be converted into fabricated data constraints.