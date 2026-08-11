# Test Cases — Account Lock After Failed Login Attempts

## 1. Overview

This artifact defines executable test cases for the confirmed test scenarios of the Account Lock After Failed Login Attempts feature.

The test cases are derived from:

- `Sample-Requirement.md`
- `Requirement-Analysis.md`
- `Business-Rules.md`
- `Risk-Analysis.md`
- `Test-Scenarios.md`

The approved scenario baseline is:

```text
TS-001 → TS-020
```

Clarification-dependent candidates `CTS-001 → CTS-009` are excluded from executable test cases until their expected behavior is defined.

`Coverage-Review.md` is generated after this artifact and evaluates the completed structured test case model.

---

## 2. Test Case Conventions

### Priority

Only the following priorities are used:

```text
High
Medium
Low
```

### Status

Default execution status:

```text
Not Run
```

### Test Data References

Detailed reusable datasets are defined later in:

```text
Test-Data.md
```

This artifact describes the logical data required for execution without assuming implementation-specific setup mechanisms.

---

## 3. Test Case Summary

| Test Case ID | Scenario | Test Title | Priority | Status |
|---|---|---|---|---|
| TC-001 | TS-001 | Login successfully with valid credentials for an unlocked account | Medium | Not Run |
| TC-002 | TS-002 | Reject login with an incorrect password | High | Not Run |
| TC-003 | TS-003 | Track failed-login attempts for the corresponding account | High | Not Run |
| TC-004 | TS-004 | Keep account unlocked after the first consecutive failed login | High | Not Run |
| TC-005 | TS-005 | Keep account unlocked after four consecutive failed logins | High | Not Run |
| TC-006 | TS-006 | Lock account on the fifth consecutive failed login | High | Not Run |
| TC-007 | TS-007 | Reset failed-login sequence after successful login following one failure | High | Not Run |
| TC-008 | TS-008 | Reset failed-login sequence after successful login following four failures | High | Not Run |
| TC-009 | TS-009 | Do not combine failures separated by a successful login | High | Not Run |
| TC-010 | TS-010 | Keep failed-login tracking isolated between two accounts | High | Not Run |
| TC-011 | TS-011 | Allow Account B to authenticate while Account A is locked | High | Not Run |
| TC-012 | TS-012 | Reject correct password while account is locked | High | Not Run |
| TC-013 | TS-013 | Reject login attempt during active lock period | High | Not Run |
| TC-014 | TS-014 | Display required message for locked account | Medium | Not Run |
| TC-015 | TS-015 | Keep account locked before the 30-minute lock period expires | High | Not Run |
| TC-016 | TS-016 | Automatically unlock account after the 30-minute lock period expires | High | Not Run |
| TC-017 | TS-017 | Allow successful authentication after automatic unlock | High | Not Run |
| TC-018 | TS-018 | Start a new failed-login sequence after automatic unlock | High | Not Run |
| TC-019 | TS-019 | Lock account again after five new failures following automatic unlock | High | Not Run |
| TC-020 | TS-020 | Verify complete temporary account-lock lifecycle | High | Not Run |

---

# 4. Detailed Test Cases

## TC-001 — Login Successfully with Valid Credentials for an Unlocked Account

**Scenario:** TS-001  
**Module:** Authentication  
**Priority:** Medium  
**Status:** Not Run

### Preconditions

- A registered user account exists.
- The account is unlocked.
- Valid credentials are available.

### Test Steps

1. Open the login page.
2. Enter the registered user's email address.
3. Enter the correct password.
4. Submit the login request.

### Test Data

```text
Account: Registered and unlocked
Email: Valid registered email
Password: Correct password
```

### Expected Result

- Authentication succeeds.
- The user is successfully logged in.
- The account remains unlocked.

---

## TC-002 — Reject Login with an Incorrect Password

**Scenario:** TS-002  
**Module:** Authentication  
**Priority:** High  
**Status:** Not Run

### Preconditions

- A registered user account exists.
- The account is unlocked.
- The account has no failed-login state that would cause this attempt to reach the lock threshold.

### Test Steps

1. Open the login page.
2. Enter the registered user's email address.
3. Enter an incorrect password.
4. Submit the login request.

### Test Data

```text
Account: Registered and unlocked
Email: Valid registered email
Password: Incorrect password
```

### Expected Result

- Authentication fails.
- The user is not logged in.
- The failed attempt contributes to the account's failed-login tracking.

---

## TC-003 — Track Failed-Login Attempts for the Corresponding Account

**Scenario:** TS-003  
**Module:** Failed Login Tracking  
**Priority:** High  
**Status:** Not Run

### Preconditions

- A registered Account A exists.
- Account A is unlocked.
- Account A begins with a fresh failed-login sequence.

### Test Steps

1. Attempt to log in to Account A using an incorrect password.
2. Repeat the incorrect-password login until Account A has accumulated four consecutive failed attempts.
3. Verify Account A remains unlocked.

### Test Data

```text
Account: Account A
Starting failure sequence: Fresh
Incorrect attempts performed: 4
```

### Expected Result

- Each failed attempt is associated with Account A's failed-login sequence.
- Account A remains unlocked after four consecutive failed attempts.
- No threshold-lock verification is performed in this test case; fifth-failure behavior is covered by TC-006.

---

## TC-004 — Keep Account Unlocked After First Consecutive Failure

**Scenario:** TS-004  
**Module:** Failed Login Threshold  
**Priority:** High  
**Status:** Not Run

### Preconditions

- A registered account exists.
- The account is unlocked.
- A fresh failed-login sequence is available.

### Test Steps

1. Submit a login request using the registered email and an incorrect password.
2. Attempt to log in using the correct password.

### Test Data

```text
Consecutive failures before test: 0
Incorrect attempts performed: 1
```

### Expected Result

- The incorrect-password attempt fails.
- The account remains unlocked after the first failure.
- The subsequent valid login is allowed.

---

## TC-005 — Keep Account Unlocked After Four Consecutive Failures

**Scenario:** TS-005  
**Module:** Failed Login Threshold  
**Priority:** High  
**Status:** Not Run

### Preconditions

- A registered account exists.
- The account is unlocked.
- A fresh failed-login sequence is available.

### Test Steps

1. Submit an incorrect password for the account.
2. Repeat the incorrect-password login until four consecutive failed attempts have occurred.
3. Verify the account has not entered the locked state.

### Test Data

```text
Consecutive incorrect-password attempts: 4
```

### Expected Result

- All four login attempts fail.
- The account remains unlocked after the fourth consecutive failed attempt.
- The temporary lock is not triggered before the fifth failure.

---

## TC-006 — Lock Account on Fifth Consecutive Failure

**Scenario:** TS-006  
**Module:** Account Lock  
**Priority:** High  
**Status:** Not Run

### Preconditions

- A registered account exists.
- The account is unlocked.
- The account currently has four consecutive failed login attempts.

### Test Steps

1. Enter the registered email address.
2. Enter an incorrect password.
3. Submit the login request.

### Test Data

```text
Existing consecutive failures: 4
Next password: Incorrect
```

### Expected Result

- The fifth incorrect-password login fails.
- The account becomes temporarily locked.
- Correct-password behavior during an active lock is covered separately by TC-012.

---

## TC-007 — Reset Sequence After Successful Login Following One Failure

**Scenario:** TS-007  
**Module:** Failed Login Tracking  
**Priority:** High  
**Status:** Not Run

### Preconditions

- A registered account exists.
- The account is unlocked.
- A fresh failed-login sequence is available.

### Test Steps

1. Attempt login using an incorrect password.
2. Log in using the correct password.
3. End the authenticated session as required to return to the login flow.
4. Perform four consecutive incorrect-password login attempts.
5. Verify the account remains unlocked.

### Test Data

```text
Initial failures: 1
Interruption: Successful login
New failures: 4
```

### Expected Result

- The first incorrect-password attempt fails.
- The valid login succeeds.
- The successful login resets the previous failed-login sequence.
- Four subsequent failures form a new sequence.
- The account remains unlocked after those four failures.

---

## TC-008 — Reset Sequence After Successful Login Following Four Failures

**Scenario:** TS-008  
**Module:** Failed Login Tracking  
**Priority:** High  
**Status:** Not Run

### Preconditions

- A registered account exists.
- The account is unlocked.
- A fresh failed-login sequence is available.

### Test Steps

1. Perform four consecutive login attempts using an incorrect password.
2. Verify the account remains unlocked.
3. Log in using the correct password.
4. End the authenticated session as required to return to the login flow.
5. Submit one incorrect-password login attempt.

### Test Data

```text
Initial failures: 4
Interruption: Successful login
New failures: 1
```

### Expected Result

- The account remains unlocked after the initial four failures.
- The valid login succeeds.
- The previous four-failure sequence is reset.
- The subsequent failed login starts a new failure sequence.
- The account does not become locked from the new single failure.

---

## TC-009 — Do Not Combine Failures Separated by Successful Login

**Scenario:** TS-009  
**Module:** Failed Login Tracking  
**Priority:** High  
**Status:** Not Run

### Preconditions

- A registered account exists.
- The account is unlocked.
- A fresh failed-login sequence is available.

### Test Steps

1. Perform three consecutive incorrect-password login attempts.
2. Log in successfully using the correct password.
3. End the authenticated session as required to return to the login flow.
4. Perform two consecutive incorrect-password login attempts.
5. Verify the account state.

### Test Data

```text
Sequence A: 3 failures
Interruption: Successful login
Sequence B: 2 failures
```

### Expected Result

- The first three attempts fail.
- The valid login succeeds and resets the previous sequence.
- The next two failures form a new sequence.
- The two sequences are not combined into five consecutive failures.
- The account remains unlocked.

---

## TC-010 — Keep Failed-Login Tracking Isolated Between Accounts

**Scenario:** TS-010  
**Module:** Failed Login Tracking  
**Priority:** High  
**Status:** Not Run

### Preconditions

- Registered Account A exists.
- Registered Account B exists.
- Both accounts are unlocked.
- Both accounts begin with fresh failed-login sequences.

### Test Steps

1. Perform four consecutive incorrect-password attempts for Account A.
2. Perform one incorrect-password attempt for Account B.
3. Verify both accounts remain unlocked.

### Test Data

```text
Account A: 4 failed attempts
Account B: 1 failed attempt
```

### Expected Result

- Account A remains unlocked after its four consecutive failures.
- Account B remains unlocked after its own single failed attempt.
- Account B's failure does not combine with Account A's failures to trigger a lock on either account.
- Authentication behavior for an unaffected account while another account is locked is covered separately by TC-011.

---

## TC-011 — Allow Account B to Authenticate While Account A Is Locked

**Scenario:** TS-011  
**Module:** Account Isolation  
**Priority:** High  
**Status:** Not Run

### Preconditions

- Registered Account A exists and is temporarily locked.
- Registered Account B exists and is unlocked.
- Valid credentials for Account B are available.

### Test Steps

1. Open the login page.
2. Enter Account B's registered email.
3. Enter Account B's correct password.
4. Submit the login request.

### Test Data

```text
Account A: Locked
Account B: Unlocked
Account B credentials: Valid
```

### Expected Result

- Account B authenticates successfully.
- Account A's locked state does not prevent Account B from logging in.

---

## TC-012 — Reject Correct Password While Account Is Locked

**Scenario:** TS-012  
**Module:** Account Lock  
**Priority:** High  
**Status:** Not Run

### Preconditions

- A registered account exists.
- The account is temporarily locked.
- The 30-minute lock period has not expired.

### Test Steps

1. Open the login page.
2. Enter the locked account's email address.
3. Enter the correct password.
4. Submit the login request.

### Test Data

```text
Account state: Locked
Password: Correct
Lock period: Active
```

### Expected Result

- Authentication is rejected.
- The user is not logged in.
- Correct credentials do not bypass the temporary lock.

No assertion is made about changes to the failed-login counter or lock timer because those behaviors are not defined.

---

## TC-013 — Reject Login Attempt During Active Lock Period

**Scenario:** TS-013  
**Module:** Account Lock  
**Priority:** High  
**Status:** Not Run

### Preconditions

- A registered account is temporarily locked.
- The lock period has not expired.

### Test Steps

1. Attempt to log in using the locked account.
2. Observe the authentication result.

### Test Data

```text
Account state: Locked
Lock period: Active
```

### Expected Result

- Authentication is not allowed.
- The account remains subject to the active temporary lock.

The test does not assert whether the login attempt changes the failure counter or lock duration.

---

## TC-014 — Display Required Message for Locked Account

**Scenario:** TS-014  
**Module:** Login  
**Priority:** Medium  
**Status:** Not Run

### Preconditions

- A registered account is temporarily locked.
- The lock period has not expired.

### Test Steps

1. Open the login page.
2. Submit a login attempt for the locked account.
3. Observe the message displayed by the system.

### Test Data

```text
Account state: Locked
```

### Expected Result

The system displays exactly:

```text
Your account has been temporarily locked. Please try again later.
```

Authentication is not allowed.

---

## TC-015 — Keep Account Locked Before Lock Period Expires

**Scenario:** TS-015  
**Module:** Account Lock Duration  
**Priority:** High  
**Status:** Not Run

### Preconditions

- A registered account has been temporarily locked.
- The lock start time is known or controllable for testing.
- The 30-minute period has not yet expired.

### Test Steps

1. Wait until a point before the 30-minute lock period expires.
2. Attempt to log in using the correct password.

### Test Data

```text
Account state: Locked
Elapsed lock time: Less than 30 minutes
Password: Correct
```

### Expected Result

- The account remains locked.
- Authentication is rejected.

The test does not define behavior at the exact expiration instant.

---

## TC-016 — Automatically Unlock After Lock Period Expires

**Scenario:** TS-016  
**Module:** Account Unlock  
**Priority:** High  
**Status:** Not Run

### Preconditions

- A registered account is temporarily locked.
- The lock start time is known or controllable for testing.

### Test Steps

1. Allow the 30-minute lock period to expire.
2. Attempt to log in using the account's correct credentials.

### Test Data

```text
Account initial state: Locked
Lock duration: 30 minutes
Password after expiration: Correct
```

### Expected Result

- The account is automatically unlocked after the lock period expires.
- No manual unlock action is required.
- The account is no longer blocked by the previous temporary lock.

---

## TC-017 — Authenticate Successfully After Automatic Unlock

**Scenario:** TS-017  
**Module:** Authentication  
**Priority:** High  
**Status:** Not Run

### Preconditions

- A registered account was previously temporarily locked.
- The 30-minute lock period has expired.
- The account has been automatically unlocked.
- Valid credentials are available.

### Test Steps

1. Open the login page.
2. Enter the account's registered email address.
3. Enter the correct password.
4. Submit the login request.

### Test Data

```text
Account state: Automatically unlocked
Credentials: Valid
```

### Expected Result

- Authentication succeeds.
- The user can access the account again after automatic unlock.

---

## TC-018 — Start New Failed-Login Sequence After Automatic Unlock

**Scenario:** TS-018  
**Module:** Failed Login Tracking  
**Priority:** High  
**Status:** Not Run

### Preconditions

- A registered account was previously locked.
- The 30-minute lock period has expired.
- The account has been automatically unlocked.

### Test Steps

1. Submit one incorrect-password login attempt.
2. Continue until four consecutive post-unlock failed attempts have occurred.
3. Verify the account remains unlocked.

### Test Data

```text
Previous state: Locked
Current state: Automatically unlocked
New failed attempts: 4
```

### Expected Result

- Failed-login tracking starts again after automatic unlock.
- The new failures are evaluated as a post-unlock sequence.
- The account remains unlocked after four consecutive new failures.

No assertion is made about the internal numeric counter representation.

---

## TC-019 — Lock Account Again After New Post-Unlock Failure Sequence

**Scenario:** TS-019  
**Module:** Account Lock Lifecycle  
**Priority:** High  
**Status:** Not Run

### Preconditions

- A registered account was previously locked.
- The 30-minute lock period has expired.
- The account has been automatically unlocked.
- A new failed-login sequence can be initiated.

### Test Steps

1. Perform four consecutive incorrect-password login attempts.
2. Verify the account remains unlocked.
3. Perform a fifth consecutive incorrect-password login attempt.
4. Attempt to authenticate using the correct password.

### Test Data

```text
Previous lifecycle: Locked → Automatically Unlocked
New consecutive failures: 5
```

### Expected Result

- The account remains unlocked after the first four new failures.
- The fifth new consecutive failure temporarily locks the account again.
- Authentication using the correct password is rejected while the new lock is active.

---

## TC-020 — Verify Complete Temporary Account-Lock Lifecycle

**Scenario:** TS-020  
**Module:** Authentication / Account Lock  
**Priority:** High  
**Status:** Not Run

### Preconditions

- A registered account exists.
- The account is unlocked.
- A fresh failed-login sequence is available.
- Valid and incorrect passwords are available.
- The lock period can be observed or controlled.

### Test Steps

1. Log in using valid credentials and verify normal authentication is available.
2. Return to the login flow.
3. Perform four consecutive login attempts using an incorrect password.
4. Verify the account remains unlocked.
5. Perform the fifth consecutive incorrect-password login attempt.
6. Verify the account becomes temporarily locked.
7. Attempt to log in using the correct password during the active lock period.
8. Verify authentication is rejected.
9. Verify the required temporary-lock message is displayed.
10. Allow the 30-minute lock period to expire.
11. Attempt to log in using the correct password.

### Test Data

```text
Account: Registered
Initial state: Unlocked
Failed-login sequence: Fresh
Lock threshold: 5 consecutive failures
Lock duration: 30 minutes
```

### Expected Result

1. Normal valid authentication succeeds while the account is unlocked.
2. Failed attempts 1–4 do not lock the account.
3. The fifth consecutive failed attempt locks the account.
4. Correct credentials cannot bypass the active lock.
5. The system displays:

   Your account has been temporarily locked. Please try again later.

6. The account automatically unlocks after the 30-minute period expires.
7. Valid authentication becomes available again.

---

# 5. Clarification-Dependent Test Cases

No executable test cases are generated for:

```text
CTS-001 → CTS-009
```

because the source requirement does not define sufficient expected behavior for those scenarios.

The unresolved areas remain:

| Candidate | Area | Status |
|---|---|---|
| CTS-001 | Failed-login counter during lock | Clarification Required |
| CTS-002 | Lock timer interaction during lock | Clarification Required |
| CTS-003 | Exact 30-minute expiration instant | Clarification Required |
| CTS-004 | Same account across browsers | Clarification Required |
| CTS-005 | Same account across devices | Clarification Required |
| CTS-006 | Concurrent threshold attempts | Clarification / Investigation Required |
| CTS-007 | Existing authenticated sessions after lock | Clarification Required |
| CTS-008 | Password reset/change interaction | Clarification Required |
| CTS-009 | Unregistered email behavior | Clarification Required |

These candidates should be converted into executable test cases only after the applicable business behavior is confirmed.

---

# 6. Scenario-to-Test-Case Traceability

| Scenario | Test Case | Status |
|---|---|---|
| TS-001 | TC-001 | Covered |
| TS-002 | TC-002 | Covered |
| TS-003 | TC-003 | Covered |
| TS-004 | TC-004 | Covered |
| TS-005 | TC-005 | Covered |
| TS-006 | TC-006 | Covered |
| TS-007 | TC-007 | Covered |
| TS-008 | TC-008 | Covered |
| TS-009 | TC-009 | Covered |
| TS-010 | TC-010 | Covered |
| TS-011 | TC-011 | Covered |
| TS-012 | TC-012 | Covered |
| TS-013 | TC-013 | Covered |
| TS-014 | TC-014 | Covered |
| TS-015 | TC-015 | Covered |
| TS-016 | TC-016 | Covered |
| TS-017 | TC-017 | Covered |
| TS-018 | TC-018 | Covered |
| TS-019 | TC-019 | Covered |
| TS-020 | TC-020 | Covered |

```text
20 / 20 confirmed scenarios
→ Detailed test-case coverage available
```

---

# 7. Requirement Traceability

| Requirement / AC | Test Cases |
|---|---|
| R1 | TC-001, TC-020 |
| R2 | TC-001, TC-002, TC-020 |
| R3 | TC-001, TC-017, TC-020 |
| R4 | TC-002, TC-003, TC-020 |
| R5 | TC-003, TC-010, TC-011 |
| R6 | TC-004, TC-005, TC-006, TC-019, TC-020 |
| R7 | TC-007, TC-008, TC-009 |
| R8 | TC-006, TC-019, TC-020 |
| R9 | TC-015, TC-016, TC-020 |
| R10 | TC-012, TC-013, TC-019, TC-020 |
| R11 | TC-014, TC-020 |
| R12 | TC-016, TC-017, TC-019, TC-020 |
| R13 | TC-017, TC-020 |
| R14 | TC-018, TC-019 |
| AC-01 | TC-004, TC-005 |
| AC-02 | TC-006 |
| AC-03 | TC-012, TC-013, TC-014 |
| AC-04 | TC-016, TC-017 |
| AC-05 | TC-007, TC-008, TC-009 |

---

# 8. Generation Validation

The generated test cases satisfy the following baseline before downstream coverage review:

```text
Confirmed scenarios only       → PASS
Scenario traceability          → PASS
Requirement traceability       → PASS
Explicit preconditions         → PASS
Executable actions             → PASS
Verifiable expected results    → PASS
Boundary coverage              → PASS
Sequence coverage              → PASS
Account isolation              → PASS
State-transition coverage      → PASS
Clarification isolation        → PASS
Unsupported API/DB assumptions → NONE
```

The test cases intentionally avoid implementation-specific validation such as:

```text
Database queries
API endpoints
Authentication service calls
Cache inspection
Background-job validation
```

because these mechanisms are not supplied by the current end-to-end input.

Detailed completeness, consistency, duplicate-objective, and traceability assessment is performed downstream in `Coverage-Review.md`.

---

# 9. Test Case Summary

The confirmed test suite contains:

```text
20 Detailed Test Cases
```

covering:

```text
Normal Authentication
Failed Authentication
Failed-Login Tracking
Threshold Boundaries
Consecutive Sequences
Successful-Login Reset
Account Isolation
Temporary Lock
Locked-State Enforcement
Lock Message
Time Boundary
Automatic Unlock
Post-Unlock Authentication
Post-Unlock Tracking
Repeated Lock Lifecycle
End-to-End Lifecycle
```

The relationship is preserved as:

```text
Requirement
    ↓
Business Rules
    ↓
Risks
    ↓
20 Confirmed Scenarios
    ↓
20 Detailed Test Cases
    ↓
Coverage Review
```

Clarification-dependent behavior remains outside the executable baseline until its expected behavior is confirmed.