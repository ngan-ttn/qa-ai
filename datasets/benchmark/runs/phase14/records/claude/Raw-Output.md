**Routing:** The request ("generate executable test cases" for `REQ-AUTH-001`, plus explicit instruction to use the canonical `testcase-generation` workflow) is resolved as **Workflow Mode**, using `workflows/testcase-generation`. Required skill sequence: `requirement-analyzer` → `business-rule-extractor` → `scenario-generator` → `testcase-generator`. Authoritative source: `datasets/requirements/simple/REQ-AUTH-001.md`. The Structured Test Case Model is the final evaluated deliverable; the three upstream artifacts are produced and retained in this response to preserve visible traceability, per workflow output rules.

---

# Requirement Analysis

## Requirement Summary

REQ-AUTH-001 defines account-lockout behavior for username-and-password authentication. After five consecutive failed login attempts on a given account, the account is locked for 15 minutes. While locked, all password-based login attempts for that account are rejected, including attempts using the correct password. The lock is lifted automatically when the 15-minute duration expires, and the failed-attempt counter is reset to zero at that point. The counter is also reset to zero by a successful login occurring before the account becomes locked. Failed-attempt tracking is maintained separately for each account.

## Functional Requirements

- FR1 (Confirmed — AC1): Each incorrect password attempt increases the failed-attempt counter for the corresponding account by one.
- FR2 (Confirmed — AC2): The account remains unlocked while the counter is below five (i.e., after 1, 2, 3, or 4 consecutive failed attempts).
- FR3 (Confirmed — AC3): The fifth consecutive failed login attempt locks the account.
- FR4 (Confirmed — AC4): The 15-minute lock duration begins when the fifth consecutive failed attempt is recorded.
- FR5 (Confirmed — AC5): While locked, all password-based login attempts for that account are rejected, including attempts using the correct password.
- FR6 (Confirmed — AC6, AC7): When the 15-minute duration expires, the account is automatically unlocked and its failed-attempt counter is reset to zero.
- FR7 (Confirmed — AC8): A successful login before the account becomes locked resets the failed-attempt counter to zero.
- FR8 (Confirmed — AC9): After a counter reset, the next failed login attempt starts a new consecutive sequence at one.
- FR9 (Confirmed — Constraints/Notes): Failed-attempt tracking is maintained separately for each account.

## Non-Functional Requirements

Not defined by the dataset. No performance, security, usability, or compatibility attributes are stated.

## Assumptions

None were required to represent the confirmed scope above. Any point requiring interpretation beyond the stated text is recorded under Open Questions instead of being assumed.

## Dependencies

Not defined by the dataset beyond the general username-and-password authentication capability described in the Context section. No specific module, service, database, or timing/scheduling mechanism is stated, and none is introduced here.

## Business Constraints

- Only username-and-password authentication behavior is in scope (Constraints/Notes).
- The technical mechanism used to track lock expiration or perform automatic unlock is explicitly stated as not defined by the dataset (Constraints/Notes).

## Validation Rules

Candidates for downstream business-rule extraction (not yet finalized as rules):

- Incorrect password → increment counter (line 30 / AC1).
- Counter < 5 → account unlocked (line 32 / AC2).
- Counter reaches 5 → account locked (line 34 / AC3).
- Locked → reject all password-based attempts, including correct password (line 38 / AC5).
- Duration expiry → unlock + reset counter (line 40 / AC6, AC7).
- Successful login before lock → reset counter (line 42 / AC8).

## Edge Cases

- Exactly 4 consecutive failed attempts (upper boundary while still unlocked).
- Exactly 5 consecutive failed attempts (boundary crossing into the locked state).
- A login attempt using the correct password occurring while the account is locked.
- A login attempt occurring at/after the moment the 15-minute duration expires.
- A successful login occurring at an attempt count below 5 (resets the counter).
- Two different accounts accumulating failed attempts independently (isolation).

## Open Questions

- OQ1: Does a login attempt made while the account is already locked (and therefore rejected under AC5) itself increase the failed-attempt counter, or does the counter remain unaffected while locked? The dataset does not state this.
- OQ2: The dataset does not define how the 15-minute lock expiry/automatic unlock is measured or observed (no timestamp, timer, or persistence mechanism is defined). This affects test-execution mechanics only, not the confirmed business behavior itself.
- OQ3: The dataset does not define the specific response, message, or signal returned to the user on a rejected attempt or on a successful login — only the accept/reject outcome is confirmed.

## Risks

- Verifying the 15-minute lock duration and automatic unlock depends on an execution mechanism to reach or simulate elapsed time; this is a test-execution risk, not a requirement ambiguity, since the dataset intentionally leaves the mechanism undefined.
- Boundary testing around the fifth attempt must be sequenced carefully, since any attempt made after the account is already locked is rejected under AC5 regardless of the password used, and must not be conflated with the fifth attempt itself triggering the lock.

## Impact Analysis

The requirement affects only login/authentication behavior for username-and-password authentication, scoped per account. No other feature area is defined by the dataset.

## Testability Assessment

The counter-increment, sub-threshold boundary (4th vs. 5th attempt), locked-state rejection (both incorrect and correct password), reset-on-success, new-sequence-after-reset, and per-account isolation behaviors are directly testable from the stated text. The automatic-unlock/duration-expiry behavior is testable in principle but depends on an execution mechanism (elapsed-time control) that the dataset does not define; this is a non-blocking execution dependency rather than a blocking gap.

## Analysis Summary

The requirement is clear, internally consistent, and testable for its defined scope. One non-blocking open question remains regarding counter behavior on an attempt made while already locked, and one non-blocking execution dependency remains regarding how 15-minute elapsed time is reached/observed during test execution. Both are surfaced explicitly rather than resolved by assumption.

---

# Business Rules

## Rule Summary

This model represents the business logic governing account lockout after repeated failed login attempts: counter increment, lockout threshold, lock-duration start, locked-state rejection, automatic unlock, reset behavior, new-sequence restart, and per-account isolation. Every rule below is traceable to REQ-AUTH-001's requirement text or acceptance criteria; no unstated policy is introduced.

## Business Rules

**BR-01 — Failed-Attempt Counter Increment**
- Condition/Trigger: An incorrect password is submitted for a given account.
- Action/Outcome: The failed-attempt counter for that account increases by one.
- Source: REQ-AUTH-001 line 30; AC1.

**BR-02 — Unlocked Below Threshold**
- Condition/Trigger: The account's failed-attempt counter is below five.
- Action/Outcome: The account remains unlocked.
- Source: REQ-AUTH-001 line 32; AC2.

**BR-03 — Lockout Trigger**
- Condition/Trigger: The failed-attempt counter reaches five (the fifth consecutive failed login attempt).
- Action/Outcome: The account becomes locked.
- Source: REQ-AUTH-001 line 34; AC3.

**BR-04 — Lock Duration Start**
- Condition/Trigger: The account becomes locked under BR-03.
- Action/Outcome: A 15-minute lock duration begins at the moment the fifth consecutive failed attempt is recorded.
- Source: REQ-AUTH-001 line 36; AC4.

**BR-05 — Locked-State Rejection**
- Condition/Trigger: The account is in the locked state.
- Action/Outcome: All password-based login attempts for that account are rejected, including attempts using the correct password.
- Source: REQ-AUTH-001 line 38; AC5.

**BR-06 — Automatic Unlock and Counter Reset**
- Condition/Trigger: The 15-minute lock duration expires.
- Action/Outcome: The account is automatically unlocked, and its failed-attempt counter is reset to zero.
- Source: REQ-AUTH-001 line 40; AC6, AC7.

**BR-07 — Reset on Pre-Lock Success**
- Condition/Trigger: A successful login occurs for an account before that account becomes locked.
- Action/Outcome: The failed-attempt counter for that account is reset to zero.
- Source: REQ-AUTH-001 line 42; AC8.

**BR-08 — New Sequence After Reset**
- Condition/Trigger: The failed-attempt counter has been reset to zero (via BR-06 or BR-07).
- Action/Outcome: The next failed login attempt is counted as the first attempt of a new consecutive sequence.
- Source: REQ-AUTH-001 line 44; AC9.

**BR-09 — Per-Account Isolation**
- Condition/Trigger: Applies at all times, across all accounts.
- Action/Outcome: Failed-attempt counters and lock state are tracked independently for each account; failed attempts against one account do not affect another account's counter or lock state.
- Source: REQ-AUTH-001 Constraints/Notes, line 64.

## Validation Rules

BR-01, BR-02, BR-03 govern when an attempt is treated as a failure and when the threshold is crossed.

## Decision Rules

BR-03, BR-06, BR-07 govern the lock/unlock state transition and its triggering condition.

## Exception Rules

BR-05 is the exception path that overrides normal password validation while locked, rejecting even an otherwise-correct password.

## Preconditions

A registered user account exists and uses username-and-password authentication (Context).

## Postconditions

- After BR-01: counter = previous value + 1.
- After BR-03/BR-04: account state = locked; the 15-minute lock duration is active.
- After BR-06: account state = unlocked; counter = 0.
- After BR-07: counter = 0 (account remains unlocked, since it had not yet become locked).

## Business Constraints

Only username-and-password authentication behavior is in scope; the technical mechanism for tracking or enforcing lock expiration is explicitly not defined by the dataset (Constraints/Notes).

## Rule Dependencies

- BR-03 depends on BR-01 (the counter must reach five through successive increments).
- BR-04 depends on BR-03 (the duration begins only once the account becomes locked).
- BR-05 depends on the locked state established by BR-03/BR-04.
- BR-06 depends on BR-04 (expiry is measured from the duration BR-04 establishes).
- BR-07 is an alternate reset path that applies only while the account has not yet been locked (mutually exclusive, for the same failure sequence, with the lock path BR-03).
- BR-08 depends on either BR-06 or BR-07 having reset the counter.

## Open Questions

- Whether an attempt rejected under BR-05 (while locked) also affects the failed-attempt counter is not defined by REQ-AUTH-001. No rule is asserted for this interaction; it remains an open question rather than an assumed increment or freeze.
- BR-04's start instant is defined only as "when the fifth consecutive failed login attempt is recorded"; no additional timestamp field or mechanism is defined, and none is introduced here.

## Rule Summary

Nine business rules were extracted, all directly traceable to REQ-AUTH-001's requirement text and acceptance criteria, with no unsupported policy invented. One rule interaction (counter behavior during an active lock) remains an explicit open question rather than being resolved by assumption.

---

# Test Scenarios

## Scenario Summary

This model defines scenario-level coverage for the account-lockout behavior in REQ-AUTH-001/BR-01–BR-09: the failed-attempt counter, the sub-threshold boundary, the lockout threshold, locked-state rejection, lock-duration/automatic-unlock behavior, reset-on-success, new-sequence-after-reset, and per-account isolation.

## Scope

Username-and-password login behavior for a single registered account's failed-attempt counter and lock state, and the same behavior compared across two independent accounts for isolation coverage.

## Assumptions

None required. Every scenario below traces directly to a REQ-AUTH-001 acceptance criterion or business rule. Where a scenario's execution depends on an undefined mechanism (elapsed time), this is flagged at the scenario level rather than assumed away.

## Test Scenarios

| Scenario ID | Title | Traces To | Priority | Technique | Notes |
|---|---|---|---|---|---|
| SC-01 | Failed-attempt counter increments by one per incorrect password attempt | BR-01 / AC1 | Medium | Equivalence partitioning | |
| SC-02 | Account remains unlocked after the 1st consecutive failed attempt | BR-02 / AC2 | Medium | Boundary value analysis | |
| SC-03 | Account remains unlocked after the 2nd consecutive failed attempt | BR-02 / AC2 | Medium | Boundary value analysis | |
| SC-04 | Account remains unlocked after the 3rd consecutive failed attempt | BR-02 / AC2 | Medium | Boundary value analysis | |
| SC-05 | Account remains unlocked after the 4th consecutive failed attempt (upper boundary below threshold) | BR-02 / AC2 | Medium | Boundary value analysis | |
| SC-06 | Account becomes locked on the 5th consecutive failed attempt (threshold boundary) | BR-03 / AC3 | High | Boundary value analysis, state transition | |
| SC-07 | The lock takes effect immediately at the 5th consecutive failure (duration-start proxy) | BR-04 / AC4 | Medium | State transition | Observability limited to the immediate next attempt; no timestamp signal is defined. |
| SC-08 | Login attempts using an incorrect password are rejected while locked | BR-05 / AC5 | High | State transition | |
| SC-09 | Login attempts using the correct password are rejected while locked | BR-05 / AC5 | High | State transition, decision table | Explicitly called out by AC5 as a critical case. |
| SC-10 | Account is automatically unlocked once the 15-minute lock duration has fully elapsed | BR-06 / AC6 | High | State transition | Execution dependency: elapsed-time verification mechanism not defined by the dataset. |
| SC-11 | Failed-attempt counter is reset to zero at automatic unlock | BR-06 / AC7 | High | State transition | Same execution dependency as SC-10. |
| SC-12 | A successful login before the account becomes locked resets the failed-attempt counter to zero | BR-07 / AC8 | Medium | Equivalence partitioning | |
| SC-13 | After a counter reset via successful login, the next failed attempt starts a new sequence at one | BR-08 / AC9 | Medium | State transition | |
| SC-14 | After a counter reset via automatic unlock, the next failed attempt starts a new sequence at one | BR-08 / AC9 | Medium | State transition | |
| SC-15 | Failed-attempt counters and lock state are tracked independently per account | BR-09 / Constraints | High | Equivalence partitioning | |

## Out of Scope

Any authentication behavior beyond username-and-password (Constraints/Notes). Any behavior not stated by REQ-AUTH-001 — such as UI messaging/content, notifications, audit logging, or an administrative unlock capability — since none of these are defined by the dataset.

## Coverage Summary

All nine acceptance criteria (AC1–AC9) and all nine business rules (BR-01–BR-09) have at least one tracing scenario. SC-10 and SC-11 carry a non-blocking execution dependency related to elapsed-time verification. The rule-level open question (counter behavior on an attempt made while already locked) does not have a corresponding scenario, since asserting either behavior would exceed the dataset's confirmed scope.

---

# Test Cases

## Test Suite Summary

Executable test cases for the account-lockout behavior defined in REQ-AUTH-001, covering the failed-attempt counter, the sub-threshold boundary, the lockout threshold, locked-state rejection (incorrect and correct password), lock-duration/automatic-unlock behavior, reset-on-success, new-sequence-after-reset, and per-account isolation.

## Preconditions

- The system supports username-and-password authentication for registered users (Context).
- At least two distinct registered accounts are available for testing: Account A (primary subject account) and Account B (used only for isolation verification), each with its own known valid credentials.

## Test Cases

### TC-001 — Failed-attempt counter increments correctly and the account remains unlocked below the lockout threshold

- Traceability: SC-01, SC-02, SC-03, SC-04, SC-05 / BR-01, BR-02 / AC1, AC2
- Priority: Medium
- Preconditions: Account A is a registered account for which no failed login attempts have been recorded since its most recent counter reset (or since account creation).
- Steps:
  1. Attempt to log in to Account A using an incorrect password (1st consecutive failed attempt).
  2. Attempt to log in to Account A using an incorrect password (2nd consecutive failed attempt).
  3. Attempt to log in to Account A using an incorrect password (3rd consecutive failed attempt).
  4. Attempt to log in to Account A using an incorrect password (4th consecutive failed attempt).
- Expected Results:
  - After step 1: the failed-attempt counter for Account A is 1, and Account A has not entered the locked state.
  - After step 2: the failed-attempt counter for Account A is 2, and Account A has not entered the locked state.
  - After step 3: the failed-attempt counter for Account A is 3, and Account A has not entered the locked state.
  - After step 4: the failed-attempt counter for Account A is 4, and Account A has not entered the locked state.

### TC-002 — Account enters the locked state on the fifth consecutive failed login attempt

- Traceability: SC-06 / BR-03 / AC3
- Priority: High
- Preconditions: Account A has exactly 4 consecutive failed login attempts recorded (e.g., immediately following TC-001) and has not entered the locked state.
- Steps:
  1. Attempt to log in to Account A using an incorrect password (5th consecutive failed attempt).
- Expected Results:
  - Account A enters the locked state immediately upon this attempt.

### TC-003 — The lock takes effect immediately following the fifth consecutive failed attempt

- Traceability: SC-07 / BR-04 / AC4
- Priority: Medium
- Preconditions: Account A has just recorded its fifth consecutive failed login attempt and entered the locked state (e.g., immediately following TC-002).
- Steps:
  1. Immediately attempt to log in to Account A again, using either the correct or an incorrect password.
- Expected Results:
  - The login attempt in step 1 is rejected, evidencing that the 15-minute lock duration is already in effect starting from the fifth consecutive failed attempt.

### TC-004 — Login attempts using an incorrect password are rejected while the account is locked

- Traceability: SC-08 / BR-05 / AC5
- Priority: High
- Preconditions: Account A is currently in the locked state (e.g., following TC-002).
- Steps:
  1. Attempt to log in to Account A using an incorrect password.
- Expected Results:
  - The login attempt is rejected.
- Note: Whether this rejected attempt itself affects the failed-attempt counter is not defined by the dataset (see Requirement Analysis, OQ1); no counter assertion is made for this case.

### TC-005 — Login attempts using the correct password are rejected while the account is locked

- Traceability: SC-09 / BR-05 / AC5
- Priority: High
- Preconditions: Account A is currently in the locked state (e.g., following TC-002).
- Steps:
  1. Attempt to log in to Account A using the correct password.
- Expected Results:
  - The login attempt is rejected, even though the password used is correct.
- Note: Same counter-effect caveat as TC-004 applies; no counter assertion is made for this case.

### TC-006 — Automatic unlock at duration expiry unlocks the account and resets the failed-attempt counter

- Traceability: SC-10, SC-11 / BR-06 / AC6, AC7
- Priority: High
- Preconditions: Account A entered the locked state upon its fifth consecutive failed login attempt, and the full 15-minute lock duration has since elapsed. (Execution Dependency: see Execution Notes — the dataset does not define how elapsed time is reached or observed in the test environment.)
- Steps:
  1. After the 15-minute lock duration has elapsed, attempt to log in to Account A using the correct password.
- Expected Results:
  - Account A is no longer in the locked state; it has been automatically unlocked.
  - The failed-attempt counter for Account A is reset to zero.

### TC-007 — A successful login before the account becomes locked resets the failed-attempt counter to zero

- Traceability: SC-12 / BR-07 / AC8
- Priority: Medium
- Preconditions: Account A has between 1 and 4 consecutive failed login attempts recorded and has not entered the locked state.
- Steps:
  1. Attempt to log in to Account A using the correct password.
- Expected Results:
  - The failed-attempt counter for Account A is reset to zero.

### TC-008 — After a reset via successful login, the next failed attempt starts a new consecutive sequence at one

- Traceability: SC-13 / BR-08 / AC9
- Priority: Medium
- Preconditions: Account A's failed-attempt counter was most recently reset to zero by a successful login (e.g., following TC-007).
- Steps:
  1. Attempt to log in to Account A using an incorrect password.
- Expected Results:
  - The failed-attempt counter for Account A is 1, reflecting the first attempt of a new consecutive sequence.

### TC-009 — After a reset via automatic unlock, the next failed attempt starts a new consecutive sequence at one

- Traceability: SC-14 / BR-08 / AC9
- Priority: Medium
- Preconditions: Account A's failed-attempt counter was most recently reset to zero by an automatic unlock (e.g., following TC-006).
- Steps:
  1. Attempt to log in to Account A using an incorrect password.
- Expected Results:
  - The failed-attempt counter for Account A is 1, reflecting the first attempt of a new consecutive sequence.

### TC-010 — Failed-attempt counters and lock state are tracked independently per account

- Traceability: SC-15 / BR-09 / Constraints/Notes
- Priority: High
- Preconditions: Account A and Account B are two independent registered accounts, neither of which has any failed login attempts recorded since its most recent counter reset.
- Steps:
  1. Attempt to log in to Account A using an incorrect password 5 consecutive times, so that Account A enters the locked state.
  2. Check Account B's failed-attempt counter and lock state.
- Expected Results:
  - After step 1: Account A is in the locked state.
  - After step 2: Account B's failed-attempt counter remains 0, and Account B has not entered the locked state.

## Test Data

- **Account A** — a registered account with known valid credentials (username and correct password), used as the primary subject account; starts each test sequence with no recorded failed login attempts since its last reset.
- **Account B** — a second, independent registered account with its own valid credentials, used only for isolation verification in TC-010.
- **Incorrect password value** — any password value that does not match the subject account's correct password.
- Exact credential values, specific password strings, and the account-provisioning mechanism are not defined by the dataset and are treated as generic, environment-specific execution inputs rather than invented project-specific data.

## Dependencies

No project-specific system, module, service, or database dependency is defined by REQ-AUTH-001. Only the general username-and-password authentication capability described in the requirement's Context is required for execution. No endpoint, database field, or architectural component is asserted, since none is defined by the dataset.

## Execution Notes

- **Elapsed-time dependency (TC-006, and indirectly TC-009):** These cases require the full 15-minute lock duration to elapse before the final verification step. The dataset does not define a mechanism to observe, control, or accelerate elapsed time in the test environment (no timer, scheduler, or clock-control capability is stated). Reaching this state is recorded here as an execution dependency to be resolved by the test environment/execution team, not as an assumed implementation.
- **Response/message content:** The dataset does not define the specific response content, error message, or status signal returned on a rejected or accepted login attempt. Expected results throughout this artifact are therefore expressed as the confirmed outcome (accepted/rejected, counter value, lock state) rather than as any specific message, code, or payload.
- **Counter behavior while locked (TC-004, TC-005):** Whether a rejected attempt made while the account is already locked itself affects the failed-attempt counter is not defined by REQ-AUTH-001. TC-004 and TC-005 assert only the confirmed rejection outcome and intentionally do not assert any counter effect. This should be raised as a clarification item before any test asserting counter behavior in that state is added.

## Traceability

| Requirement (AC) | Business Rule | Scenario(s) | Test Case(s) |
|---|---|---|---|
| AC1 | BR-01 | SC-01 | TC-001 |
| AC2 | BR-02 | SC-02, SC-03, SC-04, SC-05 | TC-001 |
| AC3 | BR-03 | SC-06 | TC-002 |
| AC4 | BR-04 | SC-07 | TC-003 |
| AC5 | BR-05 | SC-08, SC-09 | TC-004, TC-005 |
| AC6 | BR-06 | SC-10 | TC-006 |
| AC7 | BR-06 | SC-11 | TC-006 |
| AC8 | BR-07 | SC-12 | TC-007 |
| AC9 | BR-08 | SC-13, SC-14 | TC-008, TC-009 |
| Constraints/Notes (per-account isolation) | BR-09 | SC-15 | TC-010 |

## Coverage Summary

All nine confirmed acceptance criteria (AC1–AC9) and the per-account isolation constraint are covered by at least one executable test case (TC-001–TC-010). TC-006 (and TC-009, which depends on TC-006's state) carries a non-blocking execution dependency on elapsed-time verification that the dataset does not define a mechanism for. One rule-level open question — counter behavior on an attempt made while already locked — is intentionally not covered by an executable assertion, since the dataset does not confirm that behavior; asserting either outcome would exceed source-grounded scope. No project-specific endpoints, database fields, UI messages, or timing infrastructure were introduced anywhere in this artifact chain.

---

## Workflow Execution Summary

- Workflow: `workflows/testcase-generation`.
- Skills executed in sequence: `requirement-analyzer` → `business-rule-extractor` → `scenario-generator` → `testcase-generator`; no required stage was skipped or reordered.
- Business rules (BR-01–BR-09) remain consistent with the analyzed requirement (all trace to REQ-AUTH-001 text/AC1–AC9/Constraints).
- Test scenarios (SC-01–SC-15) remain traceable to business rules; test cases (TC-001–TC-010) remain aligned with scenarios.
- Applicable templates (`Requirement-Analysis.md`, `Business-Rule.md`, `Scenario.md`, `TestCase.md`) were followed for structure.
- Open items are surfaced rather than hidden: (1) counter behavior on an attempt made while already locked is undefined by the dataset; (2) the mechanism for verifying 15-minute elapsed time is undefined by the dataset and is recorded as an execution dependency on TC-006/TC-009.
- Completion Status: **COMPLETE WITH OPEN ITEMS** — the Structured Test Case Model is ready for delivery; the two open items above are non-blocking and explicitly identified rather than silently resolved.
