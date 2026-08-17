# Test Cases — Account Lock After Failed Login Attempts

## Test Suite Summary

This executable test set covers successful login, incorrect-password handling, consecutive failed-login tracking, the five-attempt threshold, successful-login reset, locked-state behavior, 30-minute automatic unlock, post-unlock tracking, account isolation, and repeated lock lifecycle.

Only requirement-supported behavior is asserted as an expected result. Undefined behavior is retained as clarification-dependent coverage.

---

## Shared Preconditions / Environment

- A functional login page is available.
- Registered test accounts and valid passwords are available where required.
- Test setup can establish or observe account lock/failure state as needed without changing the business behavior under test.

---

## Test Cases

| Test Case ID | Module / Function | Scenario ID | Test Case Title | Preconditions / Setup | Test Steps | Test Data | Expected Result | Priority | Traceability |
|---|---|---|---|---|---|---|---|---|---|
| TC-001 | Login | TS-001 | Verify successful login for an unlocked account | Registered account exists; account unlocked; no active failed sequence. | 1. Open login page.<br>2. Enter registered email.<br>3. Enter correct password.<br>4. Submit login. | Registered email; correct password. | Authentication succeeds and the user is logged in. | Medium | Requirements 1–3 |
| TC-002 | Login | TS-002 | Verify login fails with an incorrect password | Registered account exists; account unlocked. | 1. Open login page.<br>2. Enter registered email.<br>3. Enter incorrect password.<br>4. Submit login. | Registered email; incorrect password. | Authentication fails and the failed attempt is recorded for that account. | High | Requirements 4–5 |
| TC-003 | Failed Login Tracking | TS-003 | Verify account remains unlocked after the first failed attempt | Registered account exists; account unlocked; new failure sequence. | 1. Submit one incorrect-password login attempt.<br>2. Submit valid credentials. | Registered email; incorrect password; correct password. | First attempt fails without locking the account; subsequent valid login is allowed. | High | Requirements 5–6; AC-01 |
| TC-004 | Failed Login Tracking | TS-004 | Verify account remains unlocked after four consecutive failed attempts | Registered account exists; account unlocked; new failure sequence. | 1. Submit incorrect password four consecutive times.<br>2. Submit correct password. | Registered email; incorrect password ×4; correct password. | Four attempts fail; account remains unlocked after failure 4; valid login is allowed. | High | Requirement 6; AC-01 |
| TC-005 | Account Lock | TS-005 | Verify account locks on the fifth consecutive failed attempt | Registered account exists; account unlocked; four consecutive failures already recorded. | 1. Enter registered email.<br>2. Enter incorrect password.<br>3. Submit login. | Registered email; incorrect password. | Fifth consecutive attempt fails and the account becomes temporarily locked. | High | Requirements 6, 8; AC-02 |
| TC-006 | Counter Reset | TS-006 | Verify successful login resets failed-login sequence before threshold | Registered account exists; account unlocked; three consecutive failures recorded. | 1. Log in with correct password.<br>2. Return to login page if needed.<br>3. Submit four consecutive incorrect-password attempts.<br>4. Submit correct password. | Registered email; correct password; incorrect password ×4. | Initial valid login succeeds and resets prior failures; four later failures do not lock the account; final valid login succeeds. | High | Requirement 7; AC-05 |
| TC-007 | Counter Reset | TS-007 | Verify a new failed-login sequence starts after successful-login reset | Registered account exists; account unlocked; 1–4 failures recorded. | 1. Log in successfully.<br>2. Return to login page.<br>3. Submit one incorrect-password attempt.<br>4. Submit correct password. | Registered email; correct password; incorrect password. | Successful login resets previous failures; later failure belongs to a new sequence and does not lock the account. | High | Requirement 7; AC-05 |
| TC-008 | Account Lock | TS-008 | Verify correct password cannot authenticate while locked | Registered account temporarily locked; 30-minute period not expired. | 1. Open login page.<br>2. Enter registered email.<br>3. Enter correct password.<br>4. Submit login. | Locked account; correct password. | Authentication is rejected and no login occurs. | High | Requirement 10; AC-03 |
| TC-009 | Account Lock | TS-009 | Verify incorrect password cannot authenticate while locked | Registered account temporarily locked; 30-minute period not expired. | 1. Open login page.<br>2. Enter registered email.<br>3. Enter incorrect password.<br>4. Submit login. | Locked account; incorrect password. | Authentication is rejected. No counter or timer change is asserted because that behavior is undefined. | High | Requirements 10–11; AC-03 |
| TC-010 | Account Lock | TS-010 | Verify lock message is displayed for a login attempt while locked | Registered account temporarily locked; lock period not expired. | 1. Attempt to log in to the locked account. | Locked registered account. | Authentication is rejected and exactly `Your account has been temporarily locked. Please try again later.` is displayed. | Medium | Requirement 11; AC-03 |
| TC-011 | Lock Duration | TS-011 | Verify account remains locked before the 30-minute period expires | Account reached five consecutive failures and is locked; less than 30 minutes elapsed. | 1. Before lock expiration, submit correct password. | Locked account; correct password. | Authentication is rejected because the account remains locked. | High | Requirements 9–10 |
| TC-012 | Automatic Unlock | TS-012, TS-013 | Verify account automatically unlocks after 30 minutes and permits valid login | Registered account temporarily locked; account not manually modified. | 1. Allow the 30-minute lock period to expire.<br>2. Submit valid credentials. | Locked account; correct password. | Account automatically unlocks after the lock period and valid login succeeds. | High | Requirements 12–13; AC-04 |
| TC-013 | Post-Unlock Tracking | TS-014, TS-015 | Verify post-unlock failures start a new sequence | Account completed temporary lock and automatically unlocked. | 1. Submit four consecutive incorrect-password attempts.<br>2. Submit correct password. | Registered email; incorrect password ×4; correct password. | Four post-unlock failures do not lock the account; valid login succeeds, demonstrating prior pre-lock failures do not cause earlier lock. | High | Requirement 14 |
| TC-014 | Repeated Lifecycle | TS-018 | Verify account can be locked again after five new post-unlock failures | Account previously locked; 30-minute period expired; account unlocked; new tracking sequence active. | 1. Submit five consecutive incorrect-password attempts. | Registered email; incorrect password ×5. | Attempts 1–4 fail while account remains unlocked; fifth new consecutive failure locks the account again. | High | Requirements 6, 8, 12–14 |
| TC-015 | Account Isolation | TS-016 | Verify failed attempts for one account do not affect another account | Two registered unlocked accounts A and B with independent tracking state. | 1. Submit four incorrect-password attempts for A.<br>2. Submit valid login for B. | Account A/B credentials; A incorrect password; B correct password. | A's failed attempts do not prevent B from authenticating; B remains unaffected. | High | Requirement 5; Notes |
| TC-016 | Account Isolation | TS-017 | Verify locking one account does not lock another account | Two registered accounts initially unlocked. | 1. Submit five incorrect-password attempts for A.<br>2. Verify A is locked.<br>3. Submit valid credentials for B. | Account A/B credentials; A incorrect password ×5; B correct password. | A locks on its fifth consecutive failure; B remains unlocked and authenticates successfully. | High | Requirements 5, 8–10 |
| TC-017 | Lock Lifecycle | TS-020 | Verify complete lock and automatic-unlock lifecycle | Registered account exists; account unlocked; new failure sequence. | 1. Submit four incorrect-password attempts.<br>2. Verify account still available.<br>3. Submit fifth incorrect password.<br>4. Attempt correct password while locked.<br>5. Allow 30-minute period to expire.<br>6. Submit correct password again. | Registered email; incorrect password ×5; correct password. | Account remains unlocked through failure 4, locks on failure 5, rejects authentication while locked, automatically unlocks after 30 minutes, and then allows valid authentication. | High | Requirements 5–14; AC-01–AC-05 |

---

## Shared Test Data / Dependencies

| Data / Dependency | Purpose |
|---|---|
| Registered unlocked account | Normal authentication and failed-attempt scenarios |
| Second registered account | Account-isolation scenarios |
| Valid password | Successful-login verification |
| Incorrect password | Failed-login and lock-threshold verification |
| Ability to wait/control test timing without changing business rules | 30-minute lock lifecycle verification |

---

## Execution Notes

- Preserve test-case independence by resetting account state between cases where required.
- Do not infer failed-counter or timer effects for attempts made while locked.
- Exact behavior at the precise 30-minute expiration instant requires clarification before a deterministic expected result is added.

---

## Open Questions / Clarification-Dependent Coverage

| Item ID | Area | Coverage Needed | Missing Definition |
|---|---|---|---|
| CD-001 | Lock Timer | Login exactly at the 30-minute expiration boundary. | Exact expiration-boundary semantics are undefined. |
| CD-002 | Locked Attempts | Failed-counter behavior for attempts made while locked. | Counter behavior during lock is undefined. |
| CD-003 | Lock Extension | Effect of attempts during lock on active lock duration. | Timer restart/extension behavior is undefined. |
| CD-004 | Cross-Device | Failed-login tracking across browsers/devices/sessions. | Cross-device/session behavior is not explicit. |
| CD-005 | Unknown Account | Login using an unregistered email. | Unknown-account behavior is undefined. |
| CD-006 | Concurrency | Simultaneous failures near threshold. | Concurrent counter-update behavior is undefined. |
| CD-007 | Post-Unlock Counter | Exact numeric counter immediately after automatic unlock. | Requirement only states tracking starts again. |

---

## Coverage Summary

| Coverage Area | Test Cases |
|---|---:|
| Authentication | TC-001, TC-002 |
| Failed-login threshold | TC-003, TC-004, TC-005 |
| Counter reset | TC-006, TC-007 |
| Locked-state behavior | TC-008, TC-009, TC-010 |
| Lock duration / automatic unlock | TC-011, TC-012 |
| Post-unlock behavior | TC-013, TC-014 |
| Account isolation | TC-015, TC-016 |
| End-to-end lifecycle | TC-017 |

Undefined behavior remains outside the executable expected-result set until authoritative clarification is available.
