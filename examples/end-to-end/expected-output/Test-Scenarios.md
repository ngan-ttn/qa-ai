# Test Scenarios — Account Lock After Failed Login Attempts

## Scenario Summary

This artifact defines the scenario-level coverage derived from `Sample-Requirement.md`, `Requirement-Analysis.md`, `Business-Rules.md`, and `Risk-Analysis.md`. It covers authentication, per-account failed-login tracking, threshold boundaries, reset, account isolation, locked-state enforcement/message, 30-minute automatic unlock, post-unlock tracking, and repeated lifecycle.

---

## Scope

Confirmed requirement behavior only. Detailed execution steps belong to `Test-Cases.md`; implementation-specific persistence, timer mechanism, cross-device aggregation, and concurrency behavior are not invented.

---

## Assumptions

No project behavior beyond the end-to-end input artifacts is assumed. Clarification-dependent test ideas remain separate from the confirmed table.

---

## Test Scenarios

| Scenario ID | Module / Feature | Scenario | Type | Preconditions / Conditions | Expected Behavior | Requirement / Rule Traceability | Risk Traceability | Priority |
|---|---|---|---|---|---|---|---|---|
| TS-001 | Authentication | Verify an unlocked registered account can authenticate using valid credentials. | Positive | Registered account; unlocked; valid credentials. | Authentication succeeds. | R1–R3 | N/A | Medium |
| TS-002 | Authentication | Verify login fails when an unlocked registered account submits an incorrect password. | Negative | Registered account; unlocked; incorrect password. | Authentication fails. | R4, BR-001 | N/A | High |
| TS-003 | Failed Login Tracking | Verify an incorrect-password attempt contributes to tracking for the corresponding account. | Functional | Registered account; unlocked; incorrect password. | Failed attempt is recorded against that account. | R5, BR-001 | RISK-004 | High |
| TS-004 | Threshold | Verify the account remains unlocked after the first consecutive failed login. | Boundary / Sequence | Fresh sequence; one incorrect-password attempt. | Account remains unlocked. | R6, BR-002 | RISK-002 | High |
| TS-005 | Threshold | Verify the account remains unlocked after four consecutive failed logins. | Boundary | Four consecutive failures; no reset. | Account remains unlocked immediately below threshold. | R6, AC-01, BR-002 | RISK-002 | High |
| TS-006 | Account Lock | Verify the fifth consecutive failed login temporarily locks the account. | Boundary / State | Four consecutive failures already recorded; fifth incorrect password submitted. | Fifth failure is rejected and account transitions to locked. | R6, R8, AC-02, BR-002 | RISK-001, RISK-002 | High |
| TS-007 | Counter Reset | Verify successful login after one failure resets the current sequence. | Sequence / State | Account unlocked with one failure; valid credentials. | Authentication succeeds; prior failure sequence resets. | R7, AC-05, BR-003 | RISK-003 | High |
| TS-008 | Counter Reset | Verify successful login after four failures resets the current sequence. | Boundary / Sequence | Account unlocked with four failures; valid credentials. | Authentication succeeds; sequence resets before threshold. | R7, AC-05, BR-003 | RISK-003 | High |
| TS-009 | Counter Reset | Verify failures before and after a successful login are not one consecutive sequence. | Sequence | Example: 3 failures → successful login → 2 failures. | Final state represents two new consecutive failures, not five; account remains unlocked. | R7, BR-003 | RISK-003 | High |
| TS-010 | Account Isolation | Verify failed-login tracking for Account A does not affect Account B. | Isolation | Two independent registered accounts. | Failure state remains isolated per account. | R5, BR-001 | RISK-004 | High |
| TS-011 | Account Isolation | Verify Account B can authenticate normally while Account A is near/at lock threshold. | Isolation / Positive | Account A has accumulated failures or is locked; B is unlocked with valid credentials. | Account B authenticates independently. | R5, BR-001 | RISK-004 | High |
| TS-012 | Locked State | Verify a locked account cannot authenticate using the correct password. | Negative / State | Account locked; lock period active; correct password. | Authentication is rejected. | R10, AC-03, BR-005 | RISK-005 | High |
| TS-013 | Locked State | Verify a login attempt made while the account is locked is rejected. | Negative / State | Account locked; lock period active; login attempted. | Authentication is not allowed; counter/timer side effects are not asserted. | R10, AC-03, BR-005 | N/A | High |
| TS-014 | User Feedback | Verify the required temporary-lock message is displayed during a locked-account login attempt. | Functional / Feedback | Account locked; login attempted. | `Your account has been temporarily locked. Please try again later.` is displayed. | R11, AC-03, BR-006 | RISK-008 | Medium |
| TS-015 | Lock Duration | Verify the account remains locked before the 30-minute period expires. | Time Boundary | Account locked; less than 30 minutes elapsed. | Account remains locked and authentication rejected. | R9, BR-004 | RISK-006 | High |
| TS-016 | Automatic Unlock | Verify the account automatically unlocks after the 30-minute period expires. | Time Boundary / State | Account locked; defined period expires. | Account transitions to unlocked automatically. | R12, AC-04, BR-007 | RISK-006, RISK-007 | High |
| TS-017 | Post-Unlock Authentication | Verify authentication is available again after automatic unlock. | Positive / State | Automatic unlock completed; valid credentials. | Normal valid authentication succeeds. | R13, AC-04, BR-008 | RISK-007 | High |
| TS-018 | Post-Unlock Tracking | Verify failed-login tracking starts again after automatic unlock. | State / Sequence | Automatic unlock completed; new incorrect-password attempt. | New post-unlock failure sequence begins. | R14, BR-009 | RISK-009 | High |
| TS-019 | Repeated Lifecycle | Verify an automatically unlocked account can lock again after five new consecutive failures. | State / Boundary | Prior lock expired; new failure sequence begins. | New failures 1–4 remain unlocked; fifth new failure locks again. | R6, R8, R12–R14, BR-002, BR-007, BR-009 | RISK-001, RISK-009 | High |
| TS-020 | End-to-End Lifecycle | Verify the complete account lifecycle from unlocked through failures, temporary lock, automatic unlock, and successful authentication. | End-to-End | Account initially unlocked; supported login/timing conditions available. | Confirmed rules integrate coherently across the full lifecycle. | R1–R14 | RISK-001–RISK-009 | High |

---

## Out of Scope

- Implementation storage/timer mechanisms.
- Counter/timer side effects of attempts during active lock unless clarified.
- Cross-browser/device aggregation semantics.
- Concurrency semantics.
- Existing-session and password-management behavior not defined by the requirement.

---

## Open Questions / Clarification-Dependent Scenarios

| Candidate ID | Test Idea | Related Risk | Missing Rule |
|---|---|---|---|
| CTS-001 | Failed-counter behavior for attempt during active lock | RISK-010 | Locked-attempt counter side effect |
| CTS-002 | Lock-timer behavior for attempt during active lock | RISK-010 | Timer restart/extension rule |
| CTS-003 | Login exactly at the 30-minute expiration instant | RISK-006, RISK-007 | Exact expiration semantics |
| CTS-004 | Same-account tracking across browsers | RISK-011 | Cross-browser aggregation rule |
| CTS-005 | Same-account tracking across devices | RISK-011 | Cross-device aggregation rule |
| CTS-006 | Simultaneous failures immediately below threshold | RISK-012 | Concurrent request semantics |
| CTS-007 | Existing authenticated session after account becomes locked | N/A | Existing-session behavior |
| CTS-008 | Password reset/change during active lock | N/A | Password-management interaction |
| CTS-009 | Failed-login behavior for unregistered email | N/A | Unknown-account behavior |

---

## Coverage Summary

All confirmed requirements R1–R14 and acceptance criteria AC-01–AC-05 have scenario-level coverage. The table also preserves risk traceability and keeps clarification-dependent behavior outside deterministic expected results.
