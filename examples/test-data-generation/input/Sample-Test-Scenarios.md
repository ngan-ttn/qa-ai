# Sample Test Scenarios — Account Lock After Failed Login Attempts

## Scenario Summary

These scenarios define the testing objectives for which reusable test data must be prepared. The set focuses on credentials, failed-login states, threshold boundaries, reset, lock duration, automatic unlock, post-unlock tracking, account isolation, and repeated lifecycle.

---

## Test Scenarios

| Scenario ID | Module / Feature | Scenario | Type | Preconditions / Conditions | Expected Behavior | Requirement / Rule Traceability | Risk Traceability | Priority |
|---|---|---|---|---|---|---|---|---|
| TS-001 | Authentication | Verify a registered user with valid credentials can log in when the account is not locked. | Positive | Registered account; unlocked; valid credentials. | Authentication succeeds. | Requirements 1–3 | N/A | Medium |
| TS-002 | Authentication | Verify login fails when a registered user enters an incorrect password. | Negative | Registered account; unlocked; incorrect password. | Authentication fails. | Requirement 4 | N/A | High |
| TS-003 | Failed Login Tracking | Verify the account remains unlocked after four consecutive incorrect-password attempts. | Boundary | New sequence; four consecutive failures. | Account remains unlocked after failure 4. | Requirement 6; AC-01 | N/A | High |
| TS-004 | Account Lock | Verify the account becomes temporarily locked on the fifth consecutive incorrect-password attempt. | Boundary / State | Four consecutive failures; fifth failure occurs. | Account becomes temporarily locked. | Requirements 6, 8; AC-02 | N/A | High |
| TS-005 | Counter Reset | Verify successful login before the fifth failure resets the failed-login sequence. | Positive / State | Account unlocked with 1–4 failures; valid credentials. | Login succeeds and current failure sequence resets. | Requirement 7; AC-05 | N/A | High |
| TS-006 | Locked State | Verify a temporarily locked account cannot authenticate with the correct password. | Negative / State | Account locked; lock period active; correct password. | Authentication is rejected. | Requirement 10; AC-03 | N/A | High |
| TS-007 | Lock Duration | Verify the account remains locked before the 30-minute lock period expires. | Time Boundary | Account locked; less than 30 minutes elapsed. | Account remains locked; authentication rejected. | Requirements 9–10 | N/A | High |
| TS-008 | Automatic Unlock | Verify the account automatically unlocks after the 30-minute lock period expires. | Time Boundary / State | Account locked; defined period expires. | Account automatically unlocks and normal login becomes available. | Requirements 12–13; AC-04 | N/A | High |
| TS-009 | Post-Unlock Tracking | Verify failed-login tracking starts again after automatic unlock. | State | Automatic unlock completed; new incorrect-password attempt. | New failure participates in a new post-unlock sequence. | Requirement 14 | N/A | High |
| TS-010 | Account Isolation | Verify failed attempts for one registered account do not affect another account. | Isolation | Two registered accounts with independent states. | Failed-login state remains isolated per account. | Requirement 5; Notes | N/A | High |
| TS-011 | Repeated Lifecycle | Verify an automatically unlocked account can be locked again after five new consecutive failures. | State / Boundary | Automatic unlock completed; fresh sequence. | Failures 1–4 remain below threshold; failure 5 locks account again. | Requirements 6, 8, 12–14 | N/A | High |

---

## Test Data Needs

| Data Category | Required State / Value | Purpose |
|---|---|---|
| Credentials | Registered account with valid email/password | Positive authentication |
| Credentials | Incorrect password | Failure/threshold scenarios |
| Failed-login state | Counts 0, 1, 3, 4 | Normal, reset, and boundary setup |
| Account state | Unlocked | Normal and threshold testing |
| Account state | Locked | Locked-state and duration testing |
| Account state | Automatically unlocked | Post-unlock testing |
| Time state | Active lock, less than 30 minutes | Before-expiry behavior |
| Time state | Expired 30-minute lock | Automatic-unlock behavior |
| Isolation | Two independent registered accounts | Per-account tracking verification |

---

## Data Constraints

- Lock threshold = 5 consecutive failed attempts.
- Lock duration = 30 minutes.
- Failed-login tracking scope = per account.
- Successful login before threshold resets the current sequence.
- After automatic unlock, failed-login tracking starts again.

---

## Open Questions / Undefined Data Conditions

Do not fabricate test states for cross-device/session aggregation, concurrent failed updates, unregistered-account handling, counter effects during lock, timer extension/restart during lock, or the exact numeric failed counter immediately after automatic unlock unless those behaviors are clarified.

---

## Coverage Summary

The fixture supplies enough scenario context for test-data generation while preserving the boundary between input values and system state. Sensitive or real-user credentials must not be used in generated example data.
