# Test Cases — Account Lock After Failed Login Attempts

## 1. Test Case Scope

This document contains detailed test cases for the Account Lock After Failed Login Attempts feature.

The test cases cover:

- Successful login.
- Incorrect-password handling.
- Consecutive failed-login tracking.
- Five-attempt lock threshold.
- Successful-login counter reset.
- Authentication while locked.
- Lock-message behavior.
- 30-minute lock duration.
- Automatic unlock.
- Post-unlock failed-login tracking.
- Account-specific tracking.
- Repeated account-lock lifecycle.

Only behavior supported by the provided requirement is included as executable expected behavior.

Requirement gaps that require clarification are documented separately and are not converted into assumed test expectations.

---

## 2. Test Cases

| Test Case ID | Module | Test Title | Preconditions | Test Steps | Test Data | Expected Result | Priority | Status |
|---|---|---|---|---|---|---|---|---|
| TC-001 | Login | Verify successful login for an unlocked account | 1. A registered account exists.<br>2. Account is unlocked.<br>3. Failed-login counter has no active failed sequence. | 1. Open the login page.<br>2. Enter the registered email address.<br>3. Enter the correct password.<br>4. Submit the login request. | Valid registered email.<br>Correct password. | Authentication succeeds and the user is logged in. | Medium | Not Run |
| TC-002 | Login | Verify login fails with an incorrect password | 1. A registered account exists.<br>2. Account is unlocked. | 1. Open the login page.<br>2. Enter the registered email address.<br>3. Enter an incorrect password.<br>4. Submit the login request. | Valid registered email.<br>Incorrect password. | Authentication fails and the failed-login attempt is recorded for the account. | High | Not Run |
| TC-003 | Failed Login Tracking | Verify account remains unlocked after the first failed login attempt | 1. A registered account exists.<br>2. Account is unlocked.<br>3. No consecutive failed login attempts exist for the current sequence. | 1. Attempt to log in using the registered email and an incorrect password.<br>2. Attempt to log in again using the correct password. | Valid registered email.<br>Incorrect password.<br>Correct password. | The first login fails without locking the account. The subsequent valid login is allowed. | High | Not Run |
| TC-004 | Failed Login Tracking | Verify account remains unlocked after four consecutive failed attempts | 1. A registered account exists.<br>2. Account is unlocked.<br>3. Failed-login counter is at the beginning of a new sequence. | 1. Submit an incorrect password four consecutive times.<br>2. Submit the correct password. | Valid registered email.<br>Incorrect password ×4.<br>Correct password. | All four incorrect-password attempts fail. The account remains unlocked after the fourth failure and the valid login is allowed. | High | Not Run |
| TC-005 | Account Lock | Verify account is locked on the fifth consecutive failed attempt | 1. A registered account exists.<br>2. Account is unlocked.<br>3. The account has four consecutive failed login attempts. | 1. Enter the registered email address.<br>2. Enter an incorrect password.<br>3. Submit the login request. | Valid registered email.<br>Incorrect password. | The fifth consecutive login attempt fails and the account becomes temporarily locked. | High | Not Run |
| TC-006 | Counter Reset | Verify successful login resets the failed-login counter before the threshold | 1. A registered account exists.<br>2. Account is unlocked.<br>3. The account has three consecutive failed login attempts. | 1. Log in using the correct password.<br>2. Log out if required to return to the login page.<br>3. Submit four consecutive login attempts using an incorrect password.<br>4. Submit a login attempt using the correct password. | Valid registered email.<br>Correct password.<br>Incorrect password ×4. | The first valid login succeeds and resets the previous failed-login sequence. The following four incorrect attempts do not lock the account, and the final valid login is allowed. | High | Not Run |
| TC-007 | Counter Reset | Verify a new failed-login sequence starts after successful-login reset | 1. A registered account exists.<br>2. Account is unlocked.<br>3. Account has at least one but fewer than five consecutive failed attempts. | 1. Log in successfully using valid credentials.<br>2. Return to the login page.<br>3. Submit one login attempt using an incorrect password.<br>4. Submit a login attempt using the correct password. | Valid registered email.<br>Correct password.<br>Incorrect password. | Successful authentication resets the previous failure sequence. The later incorrect-password attempt is treated as part of a new sequence and does not lock the account. | High | Not Run |
| TC-008 | Account Lock | Verify correct password cannot authenticate while account is locked | 1. A registered account exists.<br>2. Account is temporarily locked.<br>3. The 30-minute lock period has not expired. | 1. Open the login page.<br>2. Enter the registered email address.<br>3. Enter the correct password.<br>4. Submit the login request. | Locked registered account.<br>Correct password. | Authentication is rejected and the user is not logged in. | High | Not Run |
| TC-009 | Account Lock | Verify incorrect password cannot authenticate while account is locked | 1. A registered account exists.<br>2. Account is temporarily locked.<br>3. The 30-minute lock period has not expired. | 1. Open the login page.<br>2. Enter the registered email address.<br>3. Enter an incorrect password.<br>4. Submit the login request. | Locked registered account.<br>Incorrect password. | Authentication is rejected. No expected result is asserted for counter or timer changes because those behaviors are not defined by the requirement. | High | Not Run |
| TC-010 | Account Lock | Verify lock message is displayed for a login attempt while locked | 1. A registered account exists.<br>2. Account is temporarily locked.<br>3. The lock period has not expired. | 1. Attempt to log in to the locked account. | Locked registered account. | Authentication is rejected and the system displays exactly: `Your account has been temporarily locked. Please try again later.` | Medium | Not Run |
| TC-011 | Lock Duration | Verify account remains locked before the 30-minute lock period expires | 1. A registered account has reached five consecutive failed attempts and is locked.<br>2. Less than 30 minutes have elapsed since the applicable lock period began. | 1. Before the 30-minute lock period expires, submit a login attempt using the correct password. | Locked registered account.<br>Correct password. | Authentication is rejected because the account is still locked. | High | Not Run |
| TC-012 | Automatic Unlock | Verify account is automatically unlocked after the 30-minute lock period | 1. A registered account is temporarily locked.<br>2. The account has not been manually modified. | 1. Allow the 30-minute lock period to expire.<br>2. Attempt to log in using the correct password. | Locked registered account.<br>Correct password. | The account is automatically unlocked after the lock period and the valid login is allowed. | High | Not Run |
| TC-013 | Post-Unlock Tracking | Verify failed-login tracking starts again after automatic unlock | 1. A registered account has completed a temporary lock period and is automatically unlocked. | 1. Submit four consecutive login attempts using an incorrect password.<br>2. Submit a login attempt using the correct password. | Valid registered email.<br>Incorrect password ×4.<br>Correct password. | The four post-unlock failures do not lock the account. The valid login is allowed, demonstrating that the previous pre-lock failure sequence does not cause an earlier new lock. | High | Not Run |
| TC-014 | Post-Unlock Tracking | Verify account can be locked again after five new consecutive failures | 1. A registered account was previously locked.<br>2. The 30-minute lock period has expired.<br>3. Account is unlocked and failed-login tracking has started again. | 1. Submit five consecutive login attempts using an incorrect password. | Valid registered email.<br>Incorrect password ×5. | Attempts one through four fail while the account remains unlocked. The fifth consecutive post-unlock failure locks the account again. | High | Not Run |
| TC-015 | Account Isolation | Verify failed attempts for one account do not affect another account | 1. Two registered accounts exist: Account A and Account B.<br>2. Both accounts are unlocked.<br>3. Both accounts begin with independent failed-login tracking states. | 1. Submit four consecutive incorrect-password attempts for Account A.<br>2. Submit a valid login for Account B. | Account A credentials.<br>Account B credentials.<br>Incorrect password for Account A.<br>Correct password for Account B. | Account A's failed attempts do not prevent Account B from authenticating successfully. Account B remains unaffected by Account A's failed-login sequence. | High | Not Run |
| TC-016 | Account Isolation | Verify locking one account does not lock another account | 1. Two registered accounts exist: Account A and Account B.<br>2. Both accounts are initially unlocked. | 1. Submit five consecutive incorrect-password attempts for Account A.<br>2. Verify Account A is locked.<br>3. Submit valid credentials for Account B. | Account A credentials.<br>Account B credentials.<br>Incorrect password for Account A ×5.<br>Correct password for Account B. | Account A becomes locked after its fifth consecutive failure. Account B remains unlocked and can authenticate successfully. | High | Not Run |
| TC-017 | Lock Lifecycle | Verify complete account lock and automatic-unlock lifecycle | 1. A registered account exists.<br>2. Account is unlocked.<br>3. Failed-login tracking is at the beginning of a new sequence. | 1. Submit four consecutive incorrect-password attempts.<br>2. Verify the account remains available for login.<br>3. Submit the fifth incorrect-password attempt.<br>4. Attempt login using the correct password while the lock is active.<br>5. Allow the 30-minute lock period to expire.<br>6. Submit the correct password again. | Valid registered email.<br>Incorrect password ×5.<br>Correct password. | The account remains unlocked through the fourth failure, becomes locked on the fifth failure, rejects authentication while locked, automatically unlocks after the 30-minute period, and then allows valid authentication. | High | Not Run |

---

## 3. Boundary Coverage

### Failed-Login Threshold

The critical business boundary is:

```text
4 Consecutive Failures
        ↓
Account Still Unlocked
        ↓
5th Consecutive Failure
        ↓
Account Locked
```

Covered by:

- `TC-004` — immediately below threshold.
- `TC-005` — at threshold.
- `TC-017` — complete threshold transition.

---

### Lock Duration

The requirement defines:

```text
Lock Duration = 30 minutes
```

Covered by:

- `TC-011` — before expiration.
- `TC-012` — after expiration.

A test case asserting exact behavior at the precise expiration instant is not included because the requirement does not define the timer-boundary semantics with sufficient precision.

---

## 4. State Transition Coverage

### Unlocked → Locked

```text
UNLOCKED
    │
    │ 5 consecutive failed attempts
    ▼
LOCKED
```

Covered by:

- TC-004
- TC-005
- TC-017

### Locked → Unlocked

```text
LOCKED
    │
    │ 30-minute period expires
    ▼
UNLOCKED
```

Covered by:

- TC-011
- TC-012
- TC-017

### Counter Reset

```text
1–4 Failed Attempts
        ↓
Successful Login
        ↓
Counter Reset
        ↓
New Failure Sequence
```

Covered by:

- TC-006
- TC-007

### New Cycle After Unlock

```text
LOCKED
    ↓
Automatic Unlock
    ↓
New Failure Sequence
    ↓
5 New Failures
    ↓
LOCKED
```

Covered by:

- TC-013
- TC-014

---

## 5. Requirement Traceability

| Requirement / Acceptance Criteria | Test Cases |
|---|---|
| Requirement 1 | TC-001, TC-002 |
| Requirement 2 | TC-001, TC-002 |
| Requirement 3 | TC-001 |
| Requirement 4 | TC-002 |
| Requirement 5 | TC-002, TC-015, TC-016 |
| Requirement 6 | TC-003, TC-004, TC-005, TC-014, TC-017 |
| Requirement 7 | TC-006, TC-007 |
| Requirement 8 | TC-005, TC-014, TC-016, TC-017 |
| Requirement 9 | TC-011, TC-012, TC-017 |
| Requirement 10 | TC-008, TC-009, TC-011, TC-017 |
| Requirement 11 | TC-010 |
| Requirement 12 | TC-012, TC-013, TC-014, TC-017 |
| Requirement 13 | TC-012, TC-017 |
| Requirement 14 | TC-013, TC-014 |
| AC-01 | TC-003, TC-004 |
| AC-02 | TC-005 |
| AC-03 | TC-008, TC-009, TC-010 |
| AC-04 | TC-012, TC-017 |
| AC-05 | TC-006, TC-007 |

---

## 6. Clarification-Dependent Coverage

The following areas are intentionally not converted into test cases with assumed expected behavior.

| Item ID | Area | Coverage Needed | Missing Definition |
|---|---|---|---|
| CD-001 | Lock Timer | Login exactly at the 30-minute expiration boundary. | Exact expiration-boundary semantics are not defined. |
| CD-002 | Locked Attempts | Failed-login counter behavior when login is attempted while locked. | Counter behavior during lock is not defined. |
| CD-003 | Lock Extension | Effect of repeated login attempts on the active lock duration. | Lock restart/extension behavior is not defined. |
| CD-004 | Cross-Device | Failed-login tracking across browsers, devices, or sessions. | Cross-device/session behavior is not explicitly defined. |
| CD-005 | Unknown Account | Login attempt using an unregistered email address. | Unknown-account behavior is not defined. |
| CD-006 | Concurrency | Simultaneous failed login attempts near the five-attempt threshold. | Concurrent counter-update behavior is not defined. |
| CD-007 | Post-Unlock Counter | Exact numeric counter value immediately after automatic unlock. | Requirement only states that tracking starts again. |

These items should become executable test cases only after the corresponding expected behavior is clarified.

---

## 7. Test Case Summary

| Coverage Area | Test Cases |
|---|---:|
| Authentication | 2 |
| Failed-login threshold | 3 |
| Counter reset | 2 |
| Locked-state behavior | 3 |
| Lock duration / automatic unlock | 2 |
| Post-unlock behavior | 2 |
| Account isolation | 2 |
| End-to-end lifecycle | 1 |
| **Total** | **17** |

The test set prioritizes the business-critical paths around:

```text
Failed-Login Counter
        +
Five-Attempt Threshold
        +
Account Lock State
        +
30-Minute Timer
        +
Automatic Unlock
```

Undefined requirement behavior remains visible as clarification-dependent coverage instead of being assigned fabricated expected results.