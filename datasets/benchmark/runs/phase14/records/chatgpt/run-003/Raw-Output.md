# Structured Test Case Model — REQ-AUTH-001

**Workflow:** `testcase-generation`
 **Authoritative product source:** `datasets/requirements/simple/REQ-AUTH-001.md`
 **Evaluated deliverable:** Structured Test Case Model

The canonical workflow preserves the chain **Structured Requirement Analysis → Structured Business Rule Model → Structured Test Scenario Model → Structured Test Case Model**, with each downstream stage consuming its validated predecessor.  The testcase-generator contract requires executable steps, observable expected results, traceability, test-data needs, priority, and explicit handling of unknowns without unsupported implementation detail. 

## Traceability basis

| Rule IDConfirmed business rule |                                                                                                                              |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| BR-AUTH-001                    | An incorrect password increments that account's failed-attempt counter by one.                                               |
| BR-AUTH-002                    | Failed-attempt tracking is maintained separately for each account.                                                           |
| BR-AUTH-003                    | The account remains unlocked while its consecutive failed-attempt count is below 5.                                          |
| BR-AUTH-004                    | The fifth consecutive failed login attempt locks the account.                                                                |
| BR-AUTH-005                    | The lock lasts 15 minutes, beginning when the fifth consecutive failed login attempt is recorded.                            |
| BR-AUTH-006                    | While locked, all password-based login attempts for that account are rejected, including attempts with the correct password. |
| BR-AUTH-007                    | When the 15-minute duration expires, the account is automatically unlocked.                                                  |
| BR-AUTH-008                    | Automatic unlock resets the failed-attempt counter to zero.                                                                  |
| BR-AUTH-009                    | A successful login before lockout resets the failed-attempt counter to zero.                                                 |
| BR-AUTH-010                    | After a reset, the next failed login attempt starts a new consecutive sequence at 1.                                         |

### Derived scenarios

| Scenario IDObjectiveRule trace |                                                                                    |                                       |
| ------------------------------ | ---------------------------------------------------------------------------------- | ------------------------------------- |
| TS-AUTH-001                    | Verify lower unlocked boundary after one failed attempt                            | BR-AUTH-001, BR-AUTH-003              |
| TS-AUTH-002                    | Verify upper unlocked boundary after four consecutive failed attempts              | BR-AUTH-003                           |
| TS-AUTH-003                    | Verify lockout at exactly the fifth consecutive failed attempt and duration origin | BR-AUTH-004, BR-AUTH-005              |
| TS-AUTH-004                    | Verify incorrect-password attempts are rejected while locked                       | BR-AUTH-006                           |
| TS-AUTH-005                    | Verify correct-password attempts are rejected while locked                         | BR-AUTH-006                           |
| TS-AUTH-006                    | Verify the account remains locked before duration expiry                           | BR-AUTH-005, BR-AUTH-006, BR-AUTH-007 |
| TS-AUTH-007                    | Verify automatic unlock at duration expiry                                         | BR-AUTH-007                           |
| TS-AUTH-008                    | Verify automatic-unlock reset and new failure sequence                             | BR-AUTH-008, BR-AUTH-010              |
| TS-AUTH-009                    | Verify successful-login reset before lock and new failure sequence                 | BR-AUTH-009, BR-AUTH-010              |
| TS-AUTH-010                    | Verify failed-attempt tracking is isolated per account                             | BR-AUTH-002, BR-AUTH-003, BR-AUTH-004 |

## Test cases

### TC-AUTH-001 — One incorrect password starts the sequence without locking the account

**Traceability:** `REQ-AUTH-001 → BR-AUTH-001, BR-AUTH-003 → TS-AUTH-001`
 **Priority:** High

**Preconditions:** A registered account is available and is not locked; the consecutive-failure sequence under test has not already been performed for that account.

**Test data:** Account A and an incorrect password for Account A.

| StepActionExpected result |                                                                                         |                                                                                     |
| ------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| 1                         | Submit a username-and-password login attempt for Account A using an incorrect password. | The attempt counts as one failed attempt for Account A. Account A remains unlocked. |

Direct inspection of a counter field or storage mechanism is **Unknown** and is not required.

---

### TC-AUTH-002 — Four consecutive incorrect passwords remain below the lock threshold

**Traceability:** `REQ-AUTH-001 → BR-AUTH-003 → TS-AUTH-002`
 **Priority:** High

**Preconditions:** A registered Account A is available and not locked; the failure sequence under test has not already been performed.

**Test data:** Account A and an incorrect password for Account A.

| StepActionExpected result |                                                                                                               |                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 1                         | Submit four consecutive username-and-password login attempts for Account A, each using an incorrect password. | After the fourth consecutive failed attempt, Account A remains unlocked. |

Counts 2 and 3 belong to the same confirmed below-threshold partition and do not require duplicate standalone cases.

---

### TC-AUTH-003 — Fifth consecutive failed login locks the account for 15 minutes

**Traceability:** `REQ-AUTH-001 → BR-AUTH-004, BR-AUTH-005 → TS-AUTH-003`
 **Priority:** High

**Preconditions:** Registered Account A is available and not locked; an incorrect password is available.

**Test data:** Account A and an incorrect password for Account A.

| StepActionExpected result |                                                                                                            |                                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 1                         | Submit four consecutive username-and-password login attempts for Account A using the incorrect password.   | Account A remains unlocked.                                                                                        |
| 2                         | Submit a fifth consecutive username-and-password login attempt for Account A using the incorrect password. | Account A becomes locked for 15 minutes. The 15-minute duration starts when this fifth failed attempt is recorded. |

No UI message, API response, database value, timer implementation, or timestamp field is asserted.

---

### TC-AUTH-004 — Incorrect password is rejected while the account is locked

**Traceability:** `REQ-AUTH-001 → BR-AUTH-006 → TS-AUTH-004`
 **Priority:** High

**Preconditions:** Account A is locked following its fifth consecutive failed login attempt, and the 15-minute lock duration has not expired.

**Test data:** Locked Account A and an incorrect password.

| StepActionExpected result |                                                                                            |                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| 1                         | While Account A remains locked, submit a password-based login using an incorrect password. | The login attempt is rejected and Account A remains locked. |

Whether a locked-state attempt increments the counter or modifies the remaining lock duration is **Unknown** and is not asserted.

---

### TC-AUTH-005 — Correct password is rejected while the account is locked

**Traceability:** `REQ-AUTH-001 → BR-AUTH-006 → TS-AUTH-005`
 **Priority:** High

**Preconditions:** Account A is locked and its 15-minute lock duration has not expired; Account A's correct password is available.

**Test data:** Locked Account A and its correct password.

| StepActionExpected result |                                                                                           |                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| 1                         | While Account A remains locked, submit a password-based login using its correct password. | The login attempt is rejected and Account A remains locked. |

The dataset does not define a rejection message, status code, or presentation mechanism.

---

### TC-AUTH-006 — Account remains locked before the 15-minute duration expires

**Traceability:** `REQ-AUTH-001 → BR-AUTH-005, BR-AUTH-006, BR-AUTH-007 → TS-AUTH-006`
 **Priority:** High

**Preconditions:** Account A was locked by its fifth consecutive failed login attempt; the start of the lock duration is the recording of that attempt.

**Test data:** Locked Account A and a password for a password-based login attempt.

| StepActionExpected result |                                                                                                                                                            |                                                                            |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| 1                         | At a point after the fifth failed attempt was recorded but before the 15-minute duration has expired, submit a password-based login attempt for Account A. | Account A remains locked and the password-based login attempt is rejected. |

The dataset does not define sub-minute timing precision or timing infrastructure; therefore no invented `14:59` boundary or clock mechanism is required.

---

### TC-AUTH-007 — Account automatically unlocks when 15 minutes expire

**Traceability:** `REQ-AUTH-001 → BR-AUTH-007 → TS-AUTH-007`
 **Priority:** High

**Preconditions:** Account A was locked by its fifth consecutive failed login attempt, and the 15-minute duration began when that failed attempt was recorded.

**Test data:** Locked Account A.

| StepActionExpected result |                                              |                                      |
| ------------------------- | -------------------------------------------- | ------------------------------------ |
| 1                         | Allow the 15-minute lock duration to expire. | Account A is automatically unlocked. |

The mechanism performing automatic unlock is **Unknown** and is not part of the expected result.

---

### TC-AUTH-008 — Automatic unlock resets the failure sequence

**Traceability:** `REQ-AUTH-001 → BR-AUTH-008, BR-AUTH-010 → TS-AUTH-008`
 **Priority:** High

**Preconditions:** Account A has automatically unlocked after expiration of its 15-minute lock duration.

**Test data:** Automatically unlocked Account A and an incorrect password.

| StepActionExpected result |                                                                                                           |                                                                                                                                              |
| ------------------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| 1                         | After automatic unlock, submit four consecutive login attempts for Account A using an incorrect password. | Account A remains unlocked after all four attempts, demonstrating that the prior failed-attempt count no longer contributes to the sequence. |
| 2                         | Submit a fifth consecutive incorrect-password attempt in this new sequence.                               | Account A becomes locked for 15 minutes.                                                                                                     |

This validates the reset behavior through externally observable lockout behavior rather than an invented counter store.

---

### TC-AUTH-009 — Successful login before lockout resets the consecutive-failure sequence

**Traceability:** `REQ-AUTH-001 → BR-AUTH-009, BR-AUTH-010 → TS-AUTH-009`
 **Priority:** High

**Preconditions:** Registered Account A is unlocked; correct and incorrect passwords are available.

**Test data:** Account A, its correct password, and an incorrect password.

| StepActionExpected result |                                                                                   |                                                                                              |
| ------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| 1                         | Submit four consecutive login attempts for Account A using an incorrect password. | Account A remains unlocked.                                                                  |
| 2                         | Perform a successful login for Account A using the correct password.              | Login succeeds and Account A's failed-attempt counter is reset to zero.                      |
| 3                         | Submit four new consecutive login attempts using an incorrect password.           | These attempts form a new consecutive sequence; Account A remains unlocked after the fourth. |
| 4                         | Submit the fifth consecutive incorrect-password attempt in the new sequence.      | Account A becomes locked for 15 minutes.                                                     |

Direct counter observability is **Unknown**; the post-reset sequence supplies executable behavioral evidence of the reset.

---

### TC-AUTH-010 — Failed-attempt tracking is isolated between accounts

**Traceability:** `REQ-AUTH-001 → BR-AUTH-002, BR-AUTH-003, BR-AUTH-004 → TS-AUTH-010`
 **Priority:** High

**Preconditions:** Two distinct registered accounts, Account A and Account B, are available and not locked; each has its own incorrect password.

**Test data:** Account A, Account B, incorrect password for Account A, incorrect password for Account B.

| StepActionExpected result |                                                                          |                                                                      |
| ------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| 1                         | Submit four consecutive incorrect-password login attempts for Account A. | Account A remains unlocked.                                          |
| 2                         | Submit four consecutive incorrect-password login attempts for Account B. | Account B remains unlocked.                                          |
| 3                         | Submit the fifth consecutive incorrect-password attempt for Account A.   | Account A becomes locked for 15 minutes. Account B remains unlocked. |
| 4                         | Submit the fifth consecutive incorrect-password attempt for Account B.   | Account B becomes locked based on its own consecutive sequence.      |

No shared IP, session, device, cache, database key, or other isolation mechanism is assumed.

## Logical test data

| Data IDRequirement |                                                                                   |
| ------------------ | --------------------------------------------------------------------------------- |
| TD-AUTH-001        | Registered Account A with a known correct password and a known incorrect password |
| TD-AUTH-002        | Registered Account B, distinct from Account A, with a known incorrect password    |
| TD-AUTH-003        | Correct password for Account A                                                    |
| TD-AUTH-004        | Incorrect password for Account A                                                  |
| TD-AUTH-005        | Incorrect password for Account B                                                  |

Concrete usernames, password strings, endpoint URLs, database records, or environment-specific fixtures are not defined by the dataset and are therefore not invented.

## Explicit unknowns / non-assertions

The following are not defined by the controlled requirement and are excluded from executable expected results: UI messages; API endpoints, payloads, HTTP statuses, or response bodies; database schemas or counter fields; timer/clock/scheduler implementation; exact sub-minute interpretation of the 15-minute duration; effects of login attempts made while locked on the counter or remaining duration; concurrent-attempt behavior; and behavior for unregistered users or non-password authentication.

The generated model remains technology-neutral, as required by the canonical testcase-generator boundary; API-specific and SQL-specific expansion belongs to separate specialized skills only when authoritative technical context exists.