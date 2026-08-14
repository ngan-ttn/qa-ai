# Structured Test Case Model — REQ-AUTH-001

Version: 1.0.0  
Status: Draft  
Last Updated: 2026-08-14

## Execution Routing

| Item | Value |
|---|---|
| Workflow | `workflows/testcase-generation` |
| Authoritative source | `datasets/requirements/simple/REQ-AUTH-001.md` (`REQ-AUTH-001`) |
| Evaluated deliverable | Structured Test Case Model |
| Supporting artifacts | Structured Requirement Analysis → Structured Business Rule Model → Structured Test Scenario Model |
| Skills executed | `requirement-analyzer` → `business-rule-extractor` → `scenario-generator` → `testcase-generator` |
| Techniques applied | Equivalence partitioning, boundary-value analysis, state-transition testing |
| Risk analysis | Not executed (`risk-analyzer` is not a stage in this workflow) |

Classification used below:

| Label | Meaning |
|---|---|
| **Confirmed** | Directly stated by `REQ-AUTH-001`, or a behavioral implication that cannot be false while that statement remains true |
| **Derived** | Downstream QA structuring (IDs, grouping, technique choice) that does not add product behavior |
| **Unknown** | Not defined by the dataset; not used as an executable expected result |

No external requirement and no prior conversation behavior is used to modify this dataset.

---

# Structured Requirement Analysis

## Requirement Summary

`REQ-AUTH-001` defines username-and-password authentication lockout for registered users. Consecutive failed login attempts are tracked separately per account. An incorrect password increases that account’s failed-attempt counter by one. The account remains unlocked while the counter is below five. The fifth consecutive failed login attempt locks the account for 15 minutes. That 15-minute duration starts when the fifth consecutive failed login attempt is recorded. While locked, all password-based login attempts for that account are rejected, including attempts using the correct password. When the 15-minute duration expires, the account is automatically unlocked and the failed-attempt counter is reset to zero. A successful login before the account becomes locked also resets the counter to zero. After any such reset, subsequent failed login attempts are counted as a new consecutive sequence.

**Business objective (Confirmed):** Reduce repeated password-guessing by temporarily locking an account after repeated failed login attempts.

## Functional Requirements

All items below are **Confirmed**.

| ID | Statement | Source |
|---|---|---|
| FR-01 | The application provides username-and-password authentication for registered users. | Context |
| FR-02 | Consecutive failed login attempts are tracked separately for each account. | Requirement; Constraints / Notes |
| FR-03 | An incorrect password increases the failed-attempt counter for that account by one. | Requirement; AC1 |
| FR-04 | The account remains unlocked while the failed-attempt counter is below five, including after one, two, three, or four consecutive failed login attempts. | Requirement; AC2 |
| FR-05 | The fifth consecutive failed login attempt locks the account for 15 minutes. | Requirement; AC3 |
| FR-06 | The 15-minute lock duration starts when the fifth consecutive failed login attempt is recorded. | Requirement; AC4 |
| FR-07 | While the account is locked, all password-based login attempts for that account are rejected, including attempts using the correct password. | Requirement; AC5 |
| FR-08 | When the 15-minute lock duration expires, the account is automatically unlocked. | Requirement; AC6 |
| FR-09 | Automatic unlock resets the failed-attempt counter to zero. | Requirement; AC7 |
| FR-10 | A successful login before the account becomes locked resets the failed-attempt counter to zero. | Requirement; AC8 |
| FR-11 | After the failed-attempt counter is reset, the next failed login attempt starts a new consecutive sequence at one. | Requirement; AC9 |

## Non-Functional Requirements

None quantified by the dataset beyond the functional 15-minute lock duration in FR-05/FR-06/FR-08.

The user-story purpose (reducing password guessing) is a **Confirmed** business objective, not a separate measurable quality attribute.

## In Scope (Confirmed)

- Username-and-password authentication behavior for registered users
- Per-account consecutive failed-attempt tracking
- Lock at the fifth consecutive failed login attempt
- 15-minute lock duration starting at that fifth recorded failed attempt
- Rejection of all password-based login attempts while locked, including correct-password attempts
- Automatic unlock at duration expiry, with counter reset to zero
- Successful-login reset before lock, and a new consecutive sequence after reset

## Out of Scope (Confirmed)

- Authentication mechanisms other than username-and-password
- The technical mechanism used to track lock expiration or perform automatic unlock

## Actors / Roles (Confirmed)

| Actor | Role in this requirement |
|---|---|
| Registered user | Account holder authenticating with username and password |

No other roles are defined.

## User / System Flows (Confirmed)

1. **Unlocked authentication with incorrect password:** incorrect password → failed-attempt counter for that account increases by one → account remains unlocked if the counter is below five.
2. **Lock trigger:** fifth consecutive failed login attempt is recorded → account is locked for 15 minutes → duration starts at that recording.
3. **Locked authentication:** any password-based login attempt for that account is rejected, including a correct-password attempt.
4. **Automatic unlock:** 15-minute duration expires → account is automatically unlocked → failed-attempt counter is reset to zero → next failed login attempt starts a new consecutive sequence at one.
5. **Successful-login reset (before lock):** successful login while the account is not locked → failed-attempt counter is reset to zero → subsequent failed login attempts are a new consecutive sequence.

## Inputs / Outputs / Entities / States

**Inputs (Confirmed):** username and password for a login attempt; distinction between an incorrect password and a successful login.

**Outputs / observable signals:** **Unknown.** The dataset does not define UI messages, API status codes, session artifacts, or other signals for success, rejection, lock, unlock, or counter value.

**Entities (Confirmed):** account; failed-attempt counter associated with an account.

**States (Confirmed):**

| State | Meaning |
|---|---|
| Unlocked | Failed-attempt counter is below five; lockout has not been triggered |
| Locked | Account has been locked by the fifth consecutive failed login attempt; lock duration has not expired |

**Derived necessary implication:** while the account is locked, it remains locked until the 15-minute duration expires.

## Dependencies

**Confirmed:** username-and-password authentication; per-account identity sufficient to keep failed-attempt tracking separate.

**Unknown / not to be treated as dependencies:** endpoints, services, modules, databases, caches, clocks, schedulers, timers, notifications, or other implementation mechanisms.

## Business Constraints (Confirmed)

- Failed-attempt tracking is maintained separately for each account.
- Only username-and-password authentication behavior is in scope.
- Lock duration is 15 minutes from the recording of the fifth consecutive failed login attempt.

## Validation Rules (business-rule candidates; not finalized here)

- Incorrect password → increment that account’s failed-attempt counter by one
- Counter below five → account remains unlocked
- Fifth consecutive failed login attempt → lock for 15 minutes, duration starts at recording
- Locked → reject all password-based login attempts for that account, including correct password
- Duration expiry → automatic unlock and counter reset to zero
- Successful login before lock → counter reset to zero
- After reset → next failed login attempt starts a new consecutive sequence at one
- Tracking is per account

## Edge Cases

**Confirmed boundaries / state edges:**

- Consecutive failed attempts 1, 2, 3, and 4: account remains unlocked
- Consecutive failed attempt 5: account locks
- Immediately after the fifth consecutive failed attempt is recorded: lock duration has started
- While locked: correct-password attempt is rejected
- When 15-minute duration expires: automatic unlock and counter reset
- After reset: next failed attempt is the first of a new consecutive sequence
- Two accounts: tracking remains separate

**Unknown (not designed as confirmed product behavior):**

- Unregistered username, empty credentials, or non-password authentication
- Whether attempts made while locked increment the counter or extend the lock duration
- Sub-minute precision, time-source, or clock-skew rules for “15 minutes”
- Concurrent login attempts
- Direct inspectability of the failed-attempt counter

## Assumptions

No product-behavior assumptions are adopted as authoritative.

The following are **execution dependencies**, not product requirements:

- A tester can perform username-and-password login attempts against registered accounts.
- A tester can distinguish accounts.
- A tester can determine whether an account is locked or unlocked, and whether a password-based login attempt was rejected or successful, even though the dataset does not define the observable signal.
- A tester can determine whether 15 minutes have elapsed after the fifth consecutive failed login attempt is recorded, even though the dataset does not define the timing mechanism.

## Conflicts

None identified in `REQ-AUTH-001`. Known Ambiguities: none intentionally introduced.

## Open Questions

1. How are successful login, rejected login, locked state, and unlocked state observed?
2. How is elapsed lock duration determined, given that the timing/unlock mechanism is undefined?
3. Do password-based attempts made while locked increment the failed-attempt counter or change remaining lock duration?
4. What happens for unregistered usernames or non-password authentication (out of scope / undefined)?

These questions do not block executable coverage of the confirmed rules at the dataset’s abstraction level.

## Risks

`risk-analyzer` was not executed. QA focus implied by confirmed behavior (not a scored risk model): lock-threshold correctness, locked-state rejection of a correct password, duration start/expiry, counter reset, and per-account isolation.

## Impact Analysis

Confirmed impact is limited to username-and-password authentication of registered accounts and per-account lockout state. No other features, integrations, or components are named.

## Testability Assessment

Confirmed behavior is testable at the dataset’s abstraction level (unlocked vs locked; rejected vs successful password-based login; sequence counts 1–5; 15-minute duration origin and expiry; per-account isolation).

Testability constraints: counter value, lock/unlock signal, rejection signal, and unlock mechanism are **Unknown**. Assertions must remain at source abstraction and must not invent those signals.

## Analysis Summary

The requirement is internally consistent and sufficient for business-rule extraction and test design. Threshold (5), duration (15 minutes), reset, locked-state rejection, and per-account isolation are explicit. Implementation mechanisms and observability signals are undefined and must remain unlabeled as product behavior.

---

# Structured Business Rule Model

## Rule Summary

Ten confirmed rules cover increment, per-account scope, unlock-below-five, lock-at-five, duration origin, locked-state rejection, automatic unlock, unlock reset, successful-login reset, and new-sequence-after-reset.

## Business Rules

| Rule ID | Category | Condition / trigger | Action / outcome | Scope | Source |
|---|---|---|---|---|---|
| BR-AUTH-001 | Calculation / state | An incorrect password is submitted for an account | The failed-attempt counter for that account increases by one | Per account; username-and-password | FR-03; AC1 |
| BR-AUTH-002 | Constraint | Failed-attempt tracking is performed | Consecutive failed login attempts are tracked separately for each account | Per account | FR-02; Constraints / Notes |
| BR-AUTH-003 | State | Failed-attempt counter for the account is below five | The account remains unlocked | Per account | FR-04; AC2 |
| BR-AUTH-004 | State / decision | Fifth consecutive failed login attempt for the account is recorded | The account is locked for 15 minutes | Per account | FR-05; AC3 |
| BR-AUTH-005 | Constraint / state | Fifth consecutive failed login attempt is recorded | The 15-minute lock duration starts at that recording | Per account | FR-06; AC4 |
| BR-AUTH-006 | Constraint / permission | Account is locked; a password-based login attempt is made for that account | The attempt is rejected, including when the password is correct | Per account; password-based login only | FR-07; AC5 |
| BR-AUTH-007 | State | 15-minute lock duration expires | The account is automatically unlocked | Per account | FR-08; AC6 |
| BR-AUTH-008 | State / calculation | Automatic unlock occurs | Failed-attempt counter for that account is reset to zero | Per account | FR-09; AC7 |
| BR-AUTH-009 | State / calculation | Successful login occurs before the account becomes locked | Failed-attempt counter for that account is reset to zero | Per account | FR-10; AC8 |
| BR-AUTH-010 | State | Failed-attempt counter has been reset | The next failed login attempt starts a new consecutive sequence at one | Per account | FR-11; AC9 |

Every rule above is **Confirmed**.

## Validation Rules

Covered by BR-AUTH-001, BR-AUTH-003, BR-AUTH-004, and BR-AUTH-006. No additional input-format rules are defined.

## Decision Rules

Covered by BR-AUTH-003, BR-AUTH-004, BR-AUTH-006, BR-AUTH-007, BR-AUTH-009, and BR-AUTH-010.

## Exception Rules

BR-AUTH-006 is the confirmed exception path for password-based login while locked. No other exception policy is defined.

## Preconditions

| Rule | Precondition (Confirmed) |
|---|---|
| BR-AUTH-001 | Password-based login attempt with an incorrect password against an account |
| BR-AUTH-004 / BR-AUTH-005 | Four consecutive failed login attempts have already been recorded for that account in the current sequence, and the next attempt is also a failed login |
| BR-AUTH-006 | The account is in the locked state |
| BR-AUTH-007 / BR-AUTH-008 | The account was locked and the 15-minute duration that started at the fifth recorded consecutive failed attempt has expired |
| BR-AUTH-009 | The account has not become locked |

## Postconditions

| Rule | Postcondition (Confirmed) |
|---|---|
| BR-AUTH-001 | Counter increased by one for that account |
| BR-AUTH-003 | Account remains unlocked |
| BR-AUTH-004 / BR-AUTH-005 | Account is locked; 15-minute duration is running from the fifth recorded consecutive failed attempt |
| BR-AUTH-006 | The password-based login attempt is rejected; the account remains locked while the duration has not expired |
| BR-AUTH-007 / BR-AUTH-008 | Account is unlocked; counter is zero |
| BR-AUTH-009 | Counter is zero; account remains unlocked |
| BR-AUTH-010 | Next failed login attempt is counted as one in a new consecutive sequence |

## Business Constraints

- Username-and-password authentication only
- Per-account tracking
- Lock duration mechanism is undefined (**Unknown**), but expiry outcome is **Confirmed**

## Rule Dependencies

```text
BR-AUTH-002 (per-account scope)
    → BR-AUTH-001 (increment)
        → BR-AUTH-003 (unlocked while counter < 5)
            → BR-AUTH-004 + BR-AUTH-005 (lock at 5; duration starts)
                → BR-AUTH-006 (reject password-based attempts while locked)
                    → BR-AUTH-007 (auto-unlock at expiry)
                        → BR-AUTH-008 (counter = 0)
                            → BR-AUTH-010 (new sequence starts at 1)

BR-AUTH-009 (successful login before lock resets counter to 0)
    → BR-AUTH-010 (new sequence starts at 1)
```

No precedence conflict is stated.

## Open Questions

Same unknowns as the requirement analysis. None of the ten rules is unresolved.

No fabricated rules are included for lock-extension, attempts-during-lock increment, observability signals, or implementation mechanisms.

---

# Structured Test Scenario Model

## Scenario Summary

Scenario-level coverage for confirmed lockout behavior: increment, 1–4 unlocked partition, lock at 5, duration origin, locked-state rejection (incorrect and correct password), duration persistence, automatic unlock, post-unlock reset/new sequence, pre-lock successful-login reset/new sequence, and per-account isolation.

## Scope

In scope: confirmed FR/BR behavior listed above.  
Out of scope: non-password authentication; undefined unlock mechanism; undefined observability signals; unregistered-user behavior; concurrent/timing-infrastructure behavior.

## Assumptions

No product-behavior assumptions. Execution depends on being able to perform password-based logins on registered accounts and to observe locked/unlocked and rejected/successful outcomes at the dataset’s abstraction level.

## Test Scenarios

| Scenario ID | Title | Type | Technique | Priority | Traceability | Expected behavior (scenario level) |
|---|---|---|---|---|---|---|
| TS-AUTH-001 | One consecutive incorrect password leaves the account unlocked | Positive / lower bound | BVA; EP | High | REQ-AUTH-001; AC1; AC2; FR-03; FR-04; BR-AUTH-001; BR-AUTH-003 | After one consecutive incorrect-password login, the account remains unlocked; that attempt counts as one toward the consecutive-failure sequence |
| TS-AUTH-002 | Four consecutive incorrect passwords leave the account unlocked | Positive / off-point below threshold | BVA | High | REQ-AUTH-001; AC2; FR-04; BR-AUTH-003 | After four consecutive failed login attempts, the account remains unlocked |
| TS-AUTH-003 | Fifth consecutive failed login attempt locks the account and starts the 15-minute duration | Negative / on-point threshold | BVA; state transition | High | REQ-AUTH-001; AC3; AC4; FR-05; FR-06; BR-AUTH-004; BR-AUTH-005 | The fifth consecutive failed login attempt locks the account for 15 minutes; the duration starts when that attempt is recorded |
| TS-AUTH-004 | Incorrect-password login is rejected while locked | Negative / locked state | State transition | High | REQ-AUTH-001; AC5; FR-07; BR-AUTH-006 | While locked, a password-based login using an incorrect password is rejected |
| TS-AUTH-005 | Correct-password login is rejected while locked | Negative / locked state | State transition | High | REQ-AUTH-001; AC5; FR-07; BR-AUTH-006 | While locked, a password-based login using the correct password is rejected |
| TS-AUTH-006 | Account remains locked before the 15-minute duration expires | State / duration | State transition; BVA (before expiry) | High | REQ-AUTH-001; AC4; AC5; AC6; FR-06; FR-07; FR-08; BR-AUTH-005; BR-AUTH-006; BR-AUTH-007 | Before the 15-minute duration expires, the account remains locked and password-based login remains rejected |
| TS-AUTH-007 | Account is automatically unlocked when the 15-minute duration expires | State / duration expiry | State transition; BVA (at expiry) | High | REQ-AUTH-001; AC6; FR-08; BR-AUTH-007 | When the 15-minute duration expires, the account is automatically unlocked |
| TS-AUTH-008 | Automatic unlock resets the counter; subsequent failures start a new sequence at one | Reset / new sequence | State transition | High | REQ-AUTH-001; AC7; AC9; FR-09; FR-11; BR-AUTH-008; BR-AUTH-010 | After automatic unlock, four consecutive failed attempts leave the account unlocked; the fifth consecutive failed attempt of the new sequence locks the account |
| TS-AUTH-009 | Successful login before lock resets the counter; subsequent failures start a new sequence at one | Reset / new sequence | State transition | High | REQ-AUTH-001; AC8; AC9; FR-10; FR-11; BR-AUTH-009; BR-AUTH-010 | After a successful login before lock, four consecutive failed attempts leave the account unlocked; the fifth consecutive failed attempt of the new sequence locks the account |
| TS-AUTH-010 | Failed-attempt tracking is isolated between accounts | Isolation | Dependency / isolation | High | REQ-AUTH-001; FR-02; BR-AUTH-002; BR-AUTH-004 | Locking one account does not lock a different account; each account’s consecutive failed-attempt sequence is separate |

Interior values 2 and 3 consecutive failures are the same unlocked partition as 1 and 4 (**Confirmed** by AC2). They are not given separate scenarios, to avoid duplicate objectives. Coverage of AC2 is represented by the 1-failure and 4-failure bounds plus the explicit AC2 statement that 2 and 3 also remain unlocked.

## Out of Scope

- Non-password authentication
- Unregistered-user behavior (**Unknown**)
- Whether locked-state attempts increment the counter or extend duration (**Unknown**)
- Direct inspection of a counter store, database field, endpoint, or timer (**Unknown**)

## Coverage Summary

Every acceptance criterion AC1–AC9 has scenario coverage. Isolation is covered by TS-AUTH-010. Unknown items are listed, not converted into scenarios with invented expected results.

---

# Structured Test Case Model

## Test Suite Summary

This suite verifies confirmed account-lockout behavior for `REQ-AUTH-001`: per-account increment of consecutive failed username-and-password login attempts, unlocked behavior below five, lock at the fifth consecutive failed attempt, 15-minute duration origin and expiry, rejection of all password-based attempts while locked (including the correct password), counter reset on automatic unlock and on successful login before lock, new consecutive sequence after reset, and isolation between accounts.

Each test case has one primary objective. Expected results use the dataset’s abstraction (account remains unlocked / account is locked / password-based login attempt is rejected / successful login / counter reset verified by subsequent sequence). They do not invent endpoints, database fields, UI messages, HTTP statuses, timers, schedulers, or other undefined mechanisms.

## Preconditions

Suite-level preconditions (**execution setup**, not hidden product state):

1. Username-and-password authentication is available for registered users (**Confirmed** capability).
2. Each case uses a registered account for which the consecutive failed-login sequence under test has not yet been performed, unless the case itself establishes that sequence.
3. Isolation cases require two distinct registered accounts.
4. Reset-before-lock cases require the ability to perform a successful username-and-password login for the account under test while it is still unlocked (**Confirmed** behavior).
5. Locked-state and duration cases require the ability to determine locked versus unlocked state and rejected versus successful password-based login. The observable signal for those outcomes is **Unknown** and is an execution dependency, not a product specification.
6. Duration cases require the ability to relate elapsed time to the recording of the fifth consecutive failed login attempt. The technical timing/unlock mechanism is **Unknown** and is an execution dependency.

Do not set an internal failed-attempt counter, database field, or timer as a precondition. Those mechanisms are not defined.

## Test Cases

### TC-AUTH-001 — One consecutive incorrect password leaves the account unlocked

| Field | Value |
|---|---|
| Objective | Verify that a single consecutive incorrect-password login increases that account’s failed-attempt count by one and does not lock the account |
| Priority | High |
| Traceability | `REQ-AUTH-001`; AC1; AC2; FR-03; FR-04; BR-AUTH-001; BR-AUTH-003; TS-AUTH-001 |
| Behavior class | Confirmed |

**Preconditions**

- Registered Account A, for which the consecutive failed-login sequence under test has not yet been performed.
- A password that is incorrect for Account A is available.

**Test data**

| Data | Requirement | Notes |
|---|---|---|
| Account A | Registered account with a known correct password | Logical account identity only |
| Incorrect password for Account A | Password that is not Account A’s correct password | No format rule is defined |

**Steps**

| Step | Action | Expected result |
|---|---|---|
| 1 | Submit a username-and-password login attempt for Account A using the incorrect password. | The attempt is a failed login. The failed-attempt counter for Account A increases by one. Account A remains unlocked. The lockout trigger has not been reached. |

**Observability**

- Direct inspection of the numeric counter is **Unknown**. The executable assertion is that Account A remains unlocked after this one consecutive failed login attempt.
- Increment-by-one at threshold magnitude is corroborated by TC-AUTH-002 and TC-AUTH-003 (unlocked at 4, locked at 5).

**Open questions**

- Observable signal for failed login and unlocked state is **Unknown**.

---

### TC-AUTH-002 — Four consecutive incorrect passwords leave the account unlocked

| Field | Value |
|---|---|
| Objective | Verify the lower boundary of lockout: after four consecutive failed login attempts the account remains unlocked |
| Priority | High |
| Traceability | `REQ-AUTH-001`; AC2; FR-04; BR-AUTH-003; TS-AUTH-002 |
| Behavior class | Confirmed |

**Preconditions**

- Registered Account A, for which the consecutive failed-login sequence under test has not yet been performed.
- An incorrect password for Account A is available.

**Test data**

Same logical data as TC-AUTH-001 (Account A; incorrect password for Account A).

**Steps**

| Step | Action | Expected result |
|---|---|---|
| 1 | Submit four consecutive username-and-password login attempts for Account A, each using an incorrect password. | After the first, second, third, and fourth consecutive failed login attempts, Account A remains unlocked. The lockout trigger has not been reached. |

Do not add a successful-login step to prove that lockout has not been reached. The confirmed assertion is that the account remains unlocked.

**Open questions**

- Observable signal for unlocked state is **Unknown**.

---

### TC-AUTH-003 — Fifth consecutive failed login attempt locks the account and starts the 15-minute duration

| Field | Value |
|---|---|
| Objective | Verify that the fifth consecutive failed login attempt locks the account for 15 minutes and that the duration starts when that attempt is recorded |
| Priority | High |
| Traceability | `REQ-AUTH-001`; AC3; AC4; FR-05; FR-06; BR-AUTH-004; BR-AUTH-005; TS-AUTH-003 |
| Behavior class | Confirmed |

**Preconditions**

- Registered Account A, for which the consecutive failed-login sequence under test has not yet been performed.
- An incorrect password for Account A is available.

**Test data**

Same logical data as TC-AUTH-001.

**Steps**

| Step | Action | Expected result |
|---|---|---|
| 1 | Submit four consecutive username-and-password login attempts for Account A, each using an incorrect password. | Account A remains unlocked. |
| 2 | Submit a fifth consecutive username-and-password login attempt for Account A using an incorrect password. | This fifth consecutive failed login attempt locks Account A for 15 minutes. The 15-minute lock duration starts when this fifth consecutive failed login attempt is recorded. |

This case does not also verify later login rejection; that is TC-AUTH-004 and TC-AUTH-005.

**Open questions**

- Observable signal for entering the locked state is **Unknown**.
- Technical mechanism that starts or tracks the 15-minute duration is **Unknown**.

---

### TC-AUTH-004 — Incorrect-password login is rejected while the account is locked

| Field | Value |
|---|---|
| Objective | Verify that a password-based login using an incorrect password is rejected while the account is locked |
| Priority | High |
| Traceability | `REQ-AUTH-001`; AC5; FR-07; BR-AUTH-006; TS-AUTH-004 |
| Behavior class | Confirmed |

**Preconditions**

- Registered Account A is locked because its fifth consecutive failed login attempt has been recorded and the 15-minute lock duration has not expired.
- Establish that locked state by performing the TC-AUTH-003 sequence on Account A, using an account for which that sequence has not yet been performed.
- An incorrect password for Account A is available.

**Test data**

Account A (locked); incorrect password for Account A.

**Steps**

| Step | Action | Expected result |
|---|---|---|
| 1 | While Account A is locked, submit a username-and-password login attempt for Account A using an incorrect password. | The password-based login attempt is rejected. Account A remains locked. |

The dataset does not define whether this attempt changes the failed-attempt counter or remaining lock duration. Do not assert increment, non-increment, extension, or non-extension.

**Open questions**

- Observable signal for rejection is **Unknown**.
- Effect of locked-state attempts on counter or remaining duration is **Unknown**.

---

### TC-AUTH-005 — Correct-password login is rejected while the account is locked

| Field | Value |
|---|---|
| Objective | Verify that a password-based login using the correct password is rejected while the account is locked |
| Priority | High |
| Traceability | `REQ-AUTH-001`; AC5; FR-07; BR-AUTH-006; TS-AUTH-005 |
| Behavior class | Confirmed |

**Preconditions**

- Registered Account A is locked because its fifth consecutive failed login attempt has been recorded and the 15-minute lock duration has not expired.
- The correct password for Account A is available.

**Test data**

Account A (locked); correct password for Account A.

**Steps**

| Step | Action | Expected result |
|---|---|---|
| 1 | While Account A is locked, submit a username-and-password login attempt for Account A using the correct password. | The password-based login attempt is rejected. Account A remains locked. |

**Open questions**

- Observable signal for rejection is **Unknown**.
- Rejection presentation (message, status, or other signal) is **Unknown** and must not be invented.

---

### TC-AUTH-006 — Account remains locked before the 15-minute duration expires

| Field | Value |
|---|---|
| Objective | Verify that the account remains locked, and password-based login remains rejected, at a time after lock start and before the 15-minute duration expires |
| Priority | High |
| Traceability | `REQ-AUTH-001`; AC4; AC5; AC6; FR-06; FR-07; FR-08; BR-AUTH-005; BR-AUTH-006; BR-AUTH-007; TS-AUTH-006 |
| Behavior class | Confirmed necessary implication of “locked for 15 minutes” until expiry |

**Preconditions**

- Registered Account A is locked; the 15-minute duration started when its fifth consecutive failed login attempt was recorded; that duration has not expired.
- The correct password for Account A is available.

**Test data**

Account A (locked); correct password for Account A.

**Steps**

| Step | Action | Expected result |
|---|---|---|
| 1 | At a time after the fifth consecutive failed login attempt has been recorded and before the 15-minute lock duration expires, submit a username-and-password login attempt for Account A using the correct password. | Account A remains locked. The password-based login attempt is rejected. |

The dataset does not define sub-minute precision. Any time that is still before expiry is valid for this case. Do not invent a required wait of 14 minutes 59 seconds or a specific clock implementation.

**Open questions**

- How elapsed time is measured, and the exact precision of “15 minutes”, is **Unknown**.

---

### TC-AUTH-007 — Account is automatically unlocked when the 15-minute duration expires

| Field | Value |
|---|---|
| Objective | Verify that the account is automatically unlocked when the 15-minute lock duration expires |
| Priority | High |
| Traceability | `REQ-AUTH-001`; AC6; FR-08; BR-AUTH-007; TS-AUTH-007 |
| Behavior class | Confirmed |

**Preconditions**

- Registered Account A was locked by its fifth consecutive failed login attempt.
- The 15-minute lock duration started when that fifth consecutive failed login attempt was recorded.

**Test data**

Account A (locked pending expiry).

**Steps**

| Step | Action | Expected result |
|---|---|---|
| 1 | Wait until the 15-minute lock duration that started at the recording of Account A’s fifth consecutive failed login attempt has expired. | Account A is automatically unlocked. |

Do not invent a scheduler, job, token, or timestamp field. Waiting until the confirmed duration expires is the executable action.

This case does not also verify counter reset; that is TC-AUTH-008.

**Open questions**

- Observable signal for unlocked state is **Unknown**.
- Technical unlock mechanism is **Unknown**.

---

### TC-AUTH-008 — Automatic unlock resets the failed-attempt counter and starts a new consecutive sequence at one

| Field | Value |
|---|---|
| Objective | Verify that automatic unlock resets the failed-attempt counter to zero and that the next failed login attempts form a new consecutive sequence starting at one |
| Priority | High |
| Traceability | `REQ-AUTH-001`; AC7; AC9; FR-09; FR-11; BR-AUTH-008; BR-AUTH-010; TS-AUTH-008 |
| Behavior class | Confirmed (counter value observed through subsequent lockout sequence, not through an undefined store) |

**Preconditions**

- Account A has been automatically unlocked after expiry of the 15-minute lock duration that started at its fifth consecutive failed login attempt (TC-AUTH-007 sequence).
- An incorrect password for Account A is available.

**Test data**

Account A (automatically unlocked after expiry); incorrect password for Account A.

**Steps**

| Step | Action | Expected result |
|---|---|---|
| 1 | After automatic unlock, submit four consecutive username-and-password login attempts for Account A, each using an incorrect password. | After each of these four consecutive failed login attempts, Account A remains unlocked. |
| 2 | Submit a fifth consecutive username-and-password login attempt for Account A using an incorrect password. | This fifth consecutive failed login attempt of the new sequence locks Account A for 15 minutes. |

Step 1 is the executable demonstration that the counter was reset to zero (if it had not been reset to zero, four post-unlock failures would not all remain below the lock threshold). Step 2 confirms the new consecutive sequence reaches lock at five.

Do not inspect a counter field. Direct counter observation is **Unknown**.

**Open questions**

- Direct counter observability is **Unknown**.

---

### TC-AUTH-009 — Successful login before lock resets the failed-attempt counter and starts a new consecutive sequence at one

| Field | Value |
|---|---|
| Objective | Verify that a successful login before the account becomes locked resets the failed-attempt counter to zero and that subsequent failed attempts form a new consecutive sequence starting at one |
| Priority | High |
| Traceability | `REQ-AUTH-001`; AC8; AC9; FR-10; FR-11; BR-AUTH-009; BR-AUTH-010; TS-AUTH-009 |
| Behavior class | Confirmed |

**Preconditions**

- Registered Account A, for which the consecutive failed-login sequence under test has not yet been performed.
- The correct password and an incorrect password for Account A are available.

**Test data**

Account A; correct password for Account A; incorrect password for Account A.

**Steps**

| Step | Action | Expected result |
|---|---|---|
| 1 | Submit four consecutive username-and-password login attempts for Account A, each using an incorrect password. | Account A remains unlocked. |
| 2 | Submit a username-and-password login attempt for Account A using the correct password. | The login is successful. The failed-attempt counter for Account A is reset to zero. Account A remains unlocked. |
| 3 | Submit four consecutive username-and-password login attempts for Account A, each using an incorrect password. | After each of these four consecutive failed login attempts, Account A remains unlocked. |
| 4 | Submit a fifth consecutive username-and-password login attempt for Account A using an incorrect password. | This fifth consecutive failed login attempt of the new sequence locks Account A for 15 minutes. |

Step 3 is the executable demonstration that the counter was reset to zero. If the counter had remained at four, the first post-success failed attempt would have been the fifth consecutive failed attempt and would have locked the account.

Successful login is used here because it is the confirmed reset trigger, not as a probe that lockout was not reached in Step 1.

**Open questions**

- Observable signal for successful login is **Unknown**.
- Direct counter observability is **Unknown**.

---

### TC-AUTH-010 — Failed-attempt tracking is isolated between accounts

| Field | Value |
|---|---|
| Objective | Verify that consecutive failed login attempts are tracked separately for each account, so locking one account does not lock a different account |
| Priority | High |
| Traceability | `REQ-AUTH-001`; FR-02; BR-AUTH-002; BR-AUTH-003; BR-AUTH-004; TS-AUTH-010 |
| Behavior class | Confirmed |

**Preconditions**

- Two distinct registered accounts, Account A and Account B, each of which has not yet had the consecutive failed-login sequence under test performed.
- An incorrect password is available for each account.

**Test data**

| Data | Requirement |
|---|---|
| Account A | Registered account, distinct from Account B |
| Account B | Registered account, distinct from Account A |
| Incorrect password for Account A | Not Account A’s correct password |
| Incorrect password for Account B | Not Account B’s correct password |

**Steps**

| Step | Action | Expected result |
|---|---|---|
| 1 | Submit four consecutive username-and-password login attempts for Account A, each using an incorrect password. | Account A remains unlocked. |
| 2 | Submit four consecutive username-and-password login attempts for Account B, each using an incorrect password. | Account B remains unlocked. |
| 3 | Submit a fifth consecutive username-and-password login attempt for Account A using an incorrect password. | Account A is locked for 15 minutes. Account B remains unlocked. |

Account B remaining unlocked after Account A is locked is the executable isolation assertion. Do not invent shared-session, IP, device, or database-key mechanisms.

**Open questions**

- Observable signals for each account’s locked/unlocked state are **Unknown**.

---

## Test Data

Logical data only. No concrete usernames, password strings, environment URLs, or storage records are defined by the dataset.

| ID | Description | Used by |
|---|---|---|
| TD-AUTH-001 | Registered Account A with a known correct password and a known incorrect password | TC-AUTH-001 … TC-AUTH-009; isolation as Account A |
| TD-AUTH-002 | Registered Account B, distinct from Account A, with a known incorrect password | TC-AUTH-010 |
| TD-AUTH-003 | Correct password for Account A | TC-AUTH-005; TC-AUTH-006; TC-AUTH-009 |
| TD-AUTH-004 | Incorrect password for Account A | All Account A failed-attempt steps |
| TD-AUTH-005 | Incorrect password for Account B | TC-AUTH-010 |

Values may be any credentials that satisfy those logical roles. No password-policy or identifier format is specified.

Reusable-dataset derivation is owned by `test-data-generator` and is not required for this workflow.

## Dependencies

**Confirmed / execution-level only:**

- Username-and-password authentication for registered users
- Ability to use at least two distinct registered accounts
- Ability to submit correct and incorrect passwords
- Execution dependency: observe success, rejection, locked, and unlocked at the dataset’s abstraction level
- Execution dependency: determine when 15 minutes have elapsed after the fifth consecutive failed login attempt is recorded

**Not dependencies (undefined; must not be listed as required product components):**

- APIs, endpoints, HTTP codes
- Database tables or fields
- Counters, caches, lock services, modules
- Clocks, schedulers, jobs, timestamps
- UI copy or notification channels

## Execution Notes

1. Keep assertions at source abstraction. Do not replace “the account is locked” or “the password-based login attempt is rejected” with invented messages or status codes.
2. Do not treat an undefined counter store as a setup control. Use an account for which the sequence under test has not yet been performed.
3. Interior consecutive-failure counts 2 and 3 are the same unlocked partition as 1 and 4. They are not separate cases.
4. Attempts made while locked are confirmed as rejected. Their effect on counter or remaining duration is **Unknown** and is not asserted.
5. Duration cases measure time from the recording of the fifth consecutive failed login attempt. The unlock mechanism is undefined.
6. Technical specialization (`api-test-generator`, `sql-validation`) is not applicable: no API or schema is defined.
7. Coverage review is outside this workflow.

## Traceability

| Test case | Requirement | Acceptance criteria | Functional reqs | Business rules | Scenario |
|---|---|---|---|---|---|
| TC-AUTH-001 | REQ-AUTH-001 | AC1, AC2 | FR-03, FR-04 | BR-AUTH-001, BR-AUTH-003 | TS-AUTH-001 |
| TC-AUTH-002 | REQ-AUTH-001 | AC2 | FR-04 | BR-AUTH-003 | TS-AUTH-002 |
| TC-AUTH-003 | REQ-AUTH-001 | AC3, AC4 | FR-05, FR-06 | BR-AUTH-004, BR-AUTH-005 | TS-AUTH-003 |
| TC-AUTH-004 | REQ-AUTH-001 | AC5 | FR-07 | BR-AUTH-006 | TS-AUTH-004 |
| TC-AUTH-005 | REQ-AUTH-001 | AC5 | FR-07 | BR-AUTH-006 | TS-AUTH-005 |
| TC-AUTH-006 | REQ-AUTH-001 | AC4, AC5, AC6 | FR-06, FR-07, FR-08 | BR-AUTH-005, BR-AUTH-006, BR-AUTH-007 | TS-AUTH-006 |
| TC-AUTH-007 | REQ-AUTH-001 | AC6 | FR-08 | BR-AUTH-007 | TS-AUTH-007 |
| TC-AUTH-008 | REQ-AUTH-001 | AC7, AC9 | FR-09, FR-11 | BR-AUTH-008, BR-AUTH-010 | TS-AUTH-008 |
| TC-AUTH-009 | REQ-AUTH-001 | AC8, AC9 | FR-10, FR-11 | BR-AUTH-009, BR-AUTH-010 | TS-AUTH-009 |
| TC-AUTH-010 | REQ-AUTH-001 | Isolation constraint; AC2/AC3 interaction across accounts | FR-02, FR-04, FR-05 | BR-AUTH-002, BR-AUTH-003, BR-AUTH-004 | TS-AUTH-010 |

AC2 interior values 2 and 3 are covered by the unlocked partition represented by TC-AUTH-001 and TC-AUTH-002, together with the confirmed statement that the account remains unlocked after two or three consecutive failed login attempts.

## Coverage Summary

| Required behavior | Coverage | Status |
|---|---|---|
| Incorrect password increments that account’s failed-attempt counter by one | TC-AUTH-001; magnitude corroborated by TC-AUTH-002 + TC-AUTH-003 | Covered (Confirmed) |
| Account remains unlocked after 1 consecutive failure | TC-AUTH-001 | Covered (Confirmed) |
| Account remains unlocked after 2 or 3 consecutive failures | Same unlocked partition as 1 and 4; AC2 statement retained | Covered at partition level (Confirmed) |
| Account remains unlocked after 4 consecutive failures | TC-AUTH-002 | Covered (Confirmed) |
| Fifth consecutive failed attempt locks the account | TC-AUTH-003 | Covered (Confirmed) |
| 15-minute duration starts when the fifth failed attempt is recorded | TC-AUTH-003; origin used by TC-AUTH-006 and TC-AUTH-007 | Covered (Confirmed) |
| Incorrect-password attempt rejected while locked | TC-AUTH-004 | Covered (Confirmed) |
| Correct-password attempt rejected while locked | TC-AUTH-005 | Covered (Confirmed) |
| Remains locked before duration expires | TC-AUTH-006 | Covered (Confirmed implication) |
| Automatic unlock when duration expires | TC-AUTH-007 | Covered (Confirmed) |
| Automatic unlock resets counter to zero | TC-AUTH-008 | Covered (Confirmed; observed via new sequence) |
| Successful login before lock resets counter to zero | TC-AUTH-009 | Covered (Confirmed) |
| After reset, next failed attempt starts a new sequence at one | TC-AUTH-008; TC-AUTH-009 | Covered (Confirmed) |
| Per-account isolation | TC-AUTH-010 | Covered (Confirmed) |

| Intentionally not converted into executable expected results | Reason |
|---|---|
| UI messages, API statuses, database fields, endpoints | Not defined |
| Lock-expiration / automatic-unlock implementation | Explicitly undefined |
| Counter increment or duration change from attempts made while locked | Not defined |
| Unregistered users; non-password authentication | Out of scope / undefined |
| Exact sub-minute precision of 15 minutes | Not defined |

No clarification-dependent case is presented as an executable passing test.

## Workflow Validation

| Check | Result |
|---|---|
| Upstream artifacts produced in workflow order | Yes |
| Business rules consistent with analyzed requirement | Yes; ten confirmed rules; no invented policy |
| Scenarios traceable to confirmed rules | Yes |
| Test cases aligned to scenarios, one primary objective each | Yes |
| Expected results source-grounded | Yes |
| Unknowns labeled and not used as confirmed expected results | Yes |
| Coverage review / regression / API / SQL | Not in this workflow |

The Structured Test Case Model is suitable for downstream QA activities at the dataset’s abstraction level, subject to the stated observability and timing execution dependencies.
