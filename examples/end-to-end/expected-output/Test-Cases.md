# Test Cases — Account Lock After Failed Login Attempts

## Test Suite Summary

This artifact contains executable test cases for confirmed scenarios `TS-001` through `TS-020`. Clarification-dependent candidates remain excluded until expected behavior is defined. Logical test-data needs are recorded without assuming implementation-specific setup mechanisms.

---

## Shared Preconditions / Environment

- Username-and-password login flow is available.
- Registered test accounts with valid credentials are available.
- Account lock/failure state can be established through supported behavior or approved test instrumentation.
- Detailed reusable datasets are defined in `Test-Data.md`.

---

## Test Cases

| Test Case ID | Module / Function | Scenario ID | Test Case Title | Preconditions / Setup | Test Steps | Test Data | Expected Result | Priority | Traceability |
|---|---|---|---|---|---|---|---|---|---|
| TC-001 | Authentication | TS-001 | Login successfully with valid credentials for an unlocked account | Registered account; unlocked; valid credentials. | 1. Open login page.<br>2. Enter registered email.<br>3. Enter correct password.<br>4. Submit login. | Unlocked registered account; correct password. | Authentication succeeds; user is logged in; account remains unlocked. | Medium | R1–R3; TS-001 |
| TC-002 | Authentication | TS-002 | Reject login with an incorrect password | Registered account; unlocked; not near threshold. | 1. Open login page.<br>2. Enter registered email.<br>3. Enter incorrect password.<br>4. Submit login. | Registered account; incorrect password. | Authentication fails; user is not logged in; failure contributes to that account's tracking. | High | R4–R5; BR-001; TS-002 |
| TC-003 | Failed Login Tracking | TS-003 | Track failed-login attempts for the corresponding account | Account A registered/unlocked; fresh failure sequence. | 1. Submit incorrect-password attempts for A until four consecutive failures occur.<br>2. Verify A remains unlocked. | Account A; incorrect password ×4. | Each failure belongs to A's sequence; A remains unlocked after four failures. | High | R5–R6; BR-001, BR-002; TS-003 |
| TC-004 | Threshold | TS-004 | Keep account unlocked after first consecutive failed login | Registered account; unlocked; fresh sequence. | 1. Submit one incorrect-password attempt.<br>2. Submit correct password. | Account; incorrect + correct password. | First attempt fails; account remains unlocked; subsequent valid login is allowed. | High | R6; BR-002; TS-004 |
| TC-005 | Threshold | TS-005 | Keep account unlocked after four consecutive failed logins | Registered account; unlocked; fresh sequence. | 1. Submit four consecutive incorrect-password attempts.<br>2. Verify account state. | Account; incorrect password ×4. | All four attempts fail; account remains unlocked; temporary lock is not triggered before fifth failure. | High | R6; AC-01; BR-002; RISK-002; TS-005 |
| TC-006 | Account Lock | TS-006 | Lock account on fifth consecutive failed login | Registered account; unlocked; four consecutive failures already recorded. | 1. Submit fifth incorrect-password attempt.<br>2. Observe account state. | Account; incorrect password. | Fifth attempt fails and account becomes temporarily locked. | High | R6, R8; AC-02; BR-002; RISK-001; TS-006 |
| TC-007 | Counter Reset | TS-007 | Reset failed-login sequence after successful login following one failure | Registered account; unlocked; fresh sequence. | 1. Submit one incorrect password.<br>2. Log in with correct password.<br>3. Return to login flow.<br>4. Submit four new incorrect-password attempts.<br>5. Verify state. | Account; incorrect password ×5 across sequences; correct password. | Successful login resets first sequence; four later failures form a new sequence and do not lock account. | High | R7; AC-05; BR-003; RISK-003; TS-007 |
| TC-008 | Counter Reset | TS-008 | Reset failed-login sequence after successful login following four failures | Registered account; unlocked; fresh sequence. | 1. Submit four incorrect-password attempts.<br>2. Verify unlocked.<br>3. Log in with correct password.<br>4. Return to login flow.<br>5. Submit one new incorrect-password attempt. | Account; incorrect password ×5 across sequences; correct password. | Valid login resets initial four failures; next failure starts a new sequence; account remains unlocked. | High | R7; AC-05; BR-003; RISK-003; TS-008 |
| TC-009 | Counter Reset | TS-009 | Do not combine failures separated by a successful login | Registered account; unlocked; fresh sequence. | 1. Submit three incorrect passwords.<br>2. Log in successfully.<br>3. Return to login flow.<br>4. Submit two incorrect passwords.<br>5. Observe state. | Account; sequence A=3 failures; valid login; sequence B=2 failures. | Sequences are separated by successful login; final state represents two consecutive failures and account remains unlocked. | High | R7; BR-003; RISK-003; TS-009 |
| TC-010 | Account Isolation | TS-010 | Keep failed-login tracking isolated between two accounts | Accounts A/B registered/unlocked; fresh sequences. | 1. Submit four incorrect passwords for A.<br>2. Submit one incorrect password for B.<br>3. Observe both states. | Accounts A/B; incorrect passwords. | A has four failures/unlocked; B has one failure/unlocked; failures are not shared. | High | R5; BR-001; RISK-004; TS-010 |
| TC-011 | Account Isolation | TS-011 | Allow Account B to authenticate while Account A is locked | A locked; B unlocked; valid B credentials. | 1. Open login page.<br>2. Enter B credentials.<br>3. Submit login. | Account A locked; Account B valid credentials. | B authenticates successfully; A's lock state does not affect B. | High | R5; BR-001; RISK-004; TS-011 |
| TC-012 | Locked State | TS-012 | Reject correct password while account is locked | Registered account locked; 30-minute period active. | 1. Submit login using correct password. | Locked account; correct password. | Authentication rejected; user not logged in; correct credentials do not bypass lock. | High | R10; AC-03; BR-005; RISK-005; TS-012 |
| TC-013 | Locked State | TS-013 | Reject login attempt during active lock period | Registered account locked; lock period active. | 1. Attempt login for locked account.<br>2. Observe result. | Locked account. | Authentication is not allowed; no counter/timer side effect is asserted. | High | R10; AC-03; BR-005; TS-013 |
| TC-014 | User Feedback | TS-014 | Display required message for locked account | Registered account locked; lock period active. | 1. Open login page.<br>2. Submit login attempt for locked account.<br>3. Observe message. | Locked account. | Authentication rejected and exactly `Your account has been temporarily locked. Please try again later.` is displayed. | Medium | R11; AC-03; BR-006; RISK-008; TS-014 |
| TC-015 | Lock Duration | TS-015 | Keep account locked before 30-minute period expires | Registered account locked; lock start known/controllable; less than 30 minutes elapsed. | 1. Before expiry, submit correct-password login. | Locked account; correct password; elapsed time <30 minutes. | Account remains locked and authentication is rejected. | High | R9; BR-004; RISK-006; TS-015 |
| TC-016 | Automatic Unlock | TS-016 | Automatically unlock account after 30-minute period expires | Registered account locked; lock start known/controllable. | 1. Allow 30-minute period to expire.<br>2. Observe account availability. | Locked account; 30-minute duration. | Account automatically transitions to unlocked; no manual unlock is required. | High | R12; AC-04; BR-007; RISK-006, RISK-007; TS-016 |
| TC-017 | Post-Unlock Authentication | TS-017 | Allow successful authentication after automatic unlock | Automatic unlock completed; valid credentials. | 1. Submit valid login credentials. | Automatically unlocked account; correct password. | Authentication succeeds according to normal login behavior. | High | R13; AC-04; BR-008; RISK-007; TS-017 |
| TC-018 | Post-Unlock Tracking | TS-018 | Start a new failed-login sequence after automatic unlock | Automatic unlock completed; new failure sequence available. | 1. Submit one incorrect-password login after unlock.<br>2. Continue up to four new failures as needed to verify below-threshold behavior. | Automatically unlocked account; incorrect password. | New failures belong to a new post-unlock sequence and do not inherit the pre-lock sequence. | High | R14; BR-009; RISK-009; TS-018 |
| TC-019 | Repeated Lifecycle | TS-019 | Lock account again after five new failures following automatic unlock | Prior lock expired; account automatically unlocked; new sequence active. | 1. Submit four new incorrect-password attempts.<br>2. Verify unlocked.<br>3. Submit fifth new incorrect password.<br>4. Observe state. | Automatically unlocked account; incorrect password ×5. | New failures 1–4 remain below threshold; fifth new failure locks account again. | High | R6, R8, R12–R14; BR-002, BR-007, BR-009; TS-019 |
| TC-020 | End-to-End | TS-020 | Verify complete temporary account-lock lifecycle | Registered account initially unlocked; supported timing available. | 1. Verify valid login while unlocked.<br>2. Create failures 1–4 and verify unlocked.<br>3. Submit fifth failure and verify lock.<br>4. Attempt login during active lock and verify rejection.<br>5. Allow 30-minute period to expire.<br>6. Verify valid login after automatic unlock. | Registered account; incorrect password ×5; correct password; timing support. | Confirmed account-lock lifecycle works coherently from unlocked through lock, active rejection, automatic unlock, and restored valid authentication. | High | R1–R14; TS-020 |

---

## Shared Test Data / Dependencies

Detailed reusable data is defined in `Test-Data.md`. At minimum the suite needs independent registered accounts, valid/invalid passwords, controllable failure-state setup, and timing support for the 30-minute lifecycle.

---

## Execution Notes

- Default execution status may be tracked externally as `Not Run` before execution; status is not part of the canonical testcase definition table.
- Preserve test independence and reset account state between cases when required.
- Do not assert counter or timer changes for attempts during active lock unless clarified.

---

## Open Questions

Clarification-dependent candidates `CTS-001` through `CTS-009` from `Test-Scenarios.md` remain outside executable expected results until their missing rules are defined.

---

## Coverage Summary

All confirmed scenarios `TS-001` through `TS-020` have testcase coverage. The canonical table makes scenario, rule/risk, and requirement traceability visible without repeating each testcase as a separate section.
