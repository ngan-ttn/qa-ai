# Sample Test Scenarios — Account Lock After Failed Login Attempts

## 1. Scope

The following test scenarios provide partial coverage of the Account Lock After Failed Login Attempts requirement.

The scenarios cover the primary authentication, failed-login threshold, account-lock, automatic-unlock, counter-reset, and account-isolation behaviors.

This sample is intentionally not exhaustive so that it can be used as input for the QA-AI coverage-review capability.

---

## 2. Test Scenarios

| Scenario ID | Area | Scenario | Coverage Type | Priority | Requirement Traceability |
|---|---|---|---|---|---|
| TS-001 | Authentication | Verify a registered user with valid credentials can log in when the account is not locked. | Positive | Medium | Requirements 1–3 |
| TS-002 | Authentication | Verify login fails when a registered user enters an incorrect password. | Negative | High | Requirement 4 |
| TS-003 | Failed Login Tracking | Verify the account remains unlocked after four consecutive incorrect-password attempts. | Boundary | High | Requirement 6; AC-01 |
| TS-004 | Account Lock | Verify the account becomes temporarily locked on the fifth consecutive incorrect-password attempt. | Boundary / State Transition | High | Requirements 6, 8; AC-02 |
| TS-005 | Counter Reset | Verify a successful login before reaching five consecutive failed attempts resets the failed-login counter. | Positive / State | High | Requirement 7; AC-05 |
| TS-006 | Account Lock | Verify a locked account cannot authenticate when the correct password is entered. | Negative / State | High | Requirement 10; AC-03 |
| TS-007 | Account Lock | Verify the defined temporary-lock message is displayed when a login attempt is made while the account is locked. | Functional | Medium | Requirement 11; AC-03 |
| TS-008 | Automatic Unlock | Verify the account is automatically unlocked after the 30-minute lock period expires. | Time Boundary / State Transition | High | Requirement 12; AC-04 |
| TS-009 | Automatic Unlock | Verify the user can successfully log in with valid credentials after automatic unlock. | Positive / State | High | Requirement 13; AC-04 |
| TS-010 | Account Isolation | Verify failed login attempts for one account do not affect another registered account. | Isolation | High | Requirement 5 |

---

## 3. Covered Areas

The current scenario set includes coverage for:

### Authentication

- Successful login for an unlocked account.
- Failed login caused by an incorrect password.

### Failed-Login Threshold

- Account state immediately below the lock threshold.
- Account lock on the fifth consecutive failed attempt.

### Counter Reset

- Successful login before the lock threshold resets the failed-login counter.

### Locked State

- Authentication using a correct password is rejected while the account is locked.
- The required temporary-lock message is displayed.

### Automatic Unlock

- Automatic account unlock after the defined 30-minute lock period.
- Successful authentication after automatic unlock.

### Account Isolation

- Failed-login activity for one account does not affect another account.

---

## 4. Requirement Traceability

| Requirement / Acceptance Criteria | Covered By |
|---|---|
| Requirement 1 | TS-001 |
| Requirement 2 | TS-001, TS-002 |
| Requirement 3 | TS-001 |
| Requirement 4 | TS-002 |
| Requirement 5 | TS-010 |
| Requirement 6 | TS-003, TS-004 |
| Requirement 7 | TS-005 |
| Requirement 8 | TS-004 |
| Requirement 9 | — |
| Requirement 10 | TS-006 |
| Requirement 11 | TS-007 |
| Requirement 12 | TS-008 |
| Requirement 13 | TS-009 |
| Requirement 14 | — |
| AC-01 | TS-003 |
| AC-02 | TS-004 |
| AC-03 | TS-006, TS-007 |
| AC-04 | TS-008, TS-009 |
| AC-05 | TS-005 |

---

## 5. Scenario Notes

- Each scenario focuses on one primary testing objective.
- Scenarios are based only on behavior defined by the supplied requirement.
- Undefined behavior is not assigned an assumed expected result.
- Detailed test steps and test data are outside the scope of this scenario artifact.