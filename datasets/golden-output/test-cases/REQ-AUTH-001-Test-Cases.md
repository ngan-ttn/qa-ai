# Test Cases — Account Lockout After Failed Login Attempts

## Golden Output Metadata

- Dataset ID: `REQ-AUTH-001`
- Source Requirement: `datasets/requirements/simple/REQ-AUTH-001.md`
- Source Scenarios: `datasets/golden-output/test-scenarios/REQ-AUTH-001-Test-Scenarios.md`
- Artifact Type: `Test Cases`
- Review Status: `Approved`
- Evaluation Purpose: Reference output for evaluating testcase executability, boundary/state coverage, traceability, expected-result precision, and assumption control

---

## Test Suite Summary

The executable set covers all confirmed scenarios for username-and-password account lockout: normal authentication, per-account failure tracking, threshold boundaries, lock timing, active-lock rejection, automatic unlock/reset, successful-login reset, new sequences, isolation, and repeated lifecycle.

---

## Shared Preconditions / Environment

Unless a row states otherwise: username-and-password authentication is available; the test account is registered/active; accounts are independent; and state is established through supported behavior rather than assumed direct database modification.

---

## Test Cases

| Test Case ID | Module / Function | Scenario ID | Test Case Title | Preconditions / Setup | Test Steps | Test Data | Expected Result | Priority | Traceability |
|---|---|---|---|---|---|---|---|---|---|
| TC-AUTH-001 | Authentication | TS-AUTH-001 | Successful authentication while account is unlocked | Account A unlocked; counter = 0. | 1. Open password login.<br>2. Enter Account A username.<br>3. Enter correct password.<br>4. Submit. | Account A; correct password. | Authentication succeeds; account remains unlocked; counter = 0. | Medium | AC-08; BR-AUTH-011 |
| TC-AUTH-002 | Failed Attempt Tracking | TS-AUTH-002 | Incorrect password increments counter for corresponding account | Account A unlocked; counter = 0. | 1. Submit incorrect-password login for A.<br>2. Observe auth result.<br>3. Verify resulting failed-attempt state through observable behavior/instrumentation. | Account A; incorrect password. | Authentication rejected; A counter = 1; A remains unlocked. | High | AC-01; BR-AUTH-001, BR-AUTH-002; RISK-AUTH-004 |
| TC-AUTH-003 | Threshold | TS-AUTH-003 | Account remains unlocked after first consecutive failure | Account A unlocked; counter = 0. | 1. Submit one incorrect-password attempt.<br>2. Submit correct password. | Account A; incorrect + correct password. | First attempt rejected; counter reaches 1; account remains unlocked; correct-password login succeeds and resets counter to 0. | High | AC-01, AC-02; BR-AUTH-002, BR-AUTH-003 |
| TC-AUTH-004 | Threshold | TS-AUTH-004 | Account remains unlocked after four consecutive failures | Account A unlocked; counter = 0. | 1. Submit four consecutive incorrect-password attempts.<br>2. Confirm each fails.<br>3. Submit correct password before a fifth failure. | Account A; incorrect password ×4; correct password. | Counter reaches 4; account remains unlocked; valid login succeeds and resets counter to 0. | High | AC-02; BR-AUTH-003; RISK-AUTH-001, RISK-AUTH-010 |
| TC-AUTH-005 | Threshold / Lock | TS-AUTH-005 | Fifth consecutive failure locks the account | Account A unlocked; counter = 0. | 1. Submit four consecutive incorrect-password attempts.<br>2. Verify account remains unlocked.<br>3. Submit fifth incorrect-password attempt.<br>4. Observe state. | Account A; incorrect password ×5. | Attempts 1–4 rejected without lock; fifth rejected; counter = 5; account transitions to locked. | High | AC-03; BR-AUTH-004; RISK-AUTH-001, RISK-AUTH-002, RISK-AUTH-010 |
| TC-AUTH-006 | Lock Timing | TS-AUTH-006 | Lock duration starts when fifth failure is recorded | Account A unlocked; counter = 4; reliable test clock available. | 1. Record time before next attempt.<br>2. Submit fifth incorrect password.<br>3. Record observed completion time.<br>4. Verify lock.<br>5. Use fifth-failure time as expiry reference. | Account A; incorrect password; test clock. | Fifth failure locks account; defined 15-minute duration is measured from recorded fifth failure, not an earlier attempt. | High | AC-04; BR-AUTH-005, BR-AUTH-006; RISK-AUTH-009 |
| TC-AUTH-007 | Locked State | TS-AUTH-007 | Correct password is rejected during active lock | Account A locked; less than 15 minutes elapsed. | 1. Submit correct-password login while lock active. | Account A; correct password. | Authentication rejected; account remains locked. No counter/timer side effect is asserted. | High | AC-05; BR-AUTH-007, BR-AUTH-008; RISK-AUTH-003 |
| TC-AUTH-008 | Locked State | TS-AUTH-008 | Incorrect password is rejected during active lock | Account A locked; less than 15 minutes elapsed. | 1. Submit incorrect-password login while lock active. | Account A; incorrect password. | Authentication rejected; account remains locked. Counter/timer restart/extension is not asserted. | High | AC-05; BR-AUTH-007; RISK-AUTH-011 |
| TC-AUTH-009 | Lock Duration | TS-AUTH-009 | Account remains locked immediately before expiry | Account A locked; fifth-failure lock-start time known. | 1. Wait until immediately before 15-minute expiry.<br>2. Submit correct-password login. | Account A; correct password; test clock. | Authentication rejected while full duration has not expired; account remains locked. | High | AC-05, AC-06; BR-AUTH-005, BR-AUTH-007; RISK-AUTH-007 |
| TC-AUTH-010 | Automatic Unlock | TS-AUTH-010 | Account automatically unlocks after fifteen minutes | Account A locked; lock-start time known. | 1. Allow full 15-minute duration to expire.<br>2. Submit correct-password login. | Account A; correct password; test clock. | Account is treated as unlocked after expiry; correct-password authentication succeeds; no admin unlock required. | High | AC-06; BR-AUTH-005, BR-AUTH-009; RISK-AUTH-007, RISK-AUTH-008, RISK-AUTH-009 |
| TC-AUTH-011 | Automatic Unlock | TS-AUTH-011 | Automatic unlock resets failed-attempt counter | Account A locked after five failures; 15-minute duration expired. | 1. Confirm lock expired.<br>2. Submit one incorrect-password login.<br>3. Observe state. | Account A; incorrect password. | Previous lock is expired; new attempt rejected and treated as failure 1 of a new sequence; account remains unlocked. | High | AC-07, AC-09; BR-AUTH-010, BR-AUTH-012; RISK-AUTH-006 |
| TC-AUTH-012 | Counter Reset | TS-AUTH-012 | Successful login resets counter after one failure | Account A unlocked; counter = 0. | 1. Submit one incorrect password.<br>2. Submit correct password.<br>3. Submit another incorrect password. | Account A; incorrect + correct password. | First failure sets counter 1; valid login succeeds/reset 0; next failure becomes failure 1 of new sequence; account remains unlocked. | High | AC-08, AC-09; BR-AUTH-011, BR-AUTH-012 |
| TC-AUTH-013 | Counter Reset | TS-AUTH-013 | Successful login resets counter after four failures | Account A unlocked; counter = 0. | 1. Submit four incorrect-password attempts.<br>2. Verify unlocked.<br>3. Submit correct password.<br>4. Submit one new incorrect password. | Account A; incorrect password ×5 total across sequences; correct password. | Initial counter reaches 4/unlocked; valid login succeeds/reset 0; next failure starts at 1; account remains unlocked. | High | AC-08, AC-09; BR-AUTH-011, BR-AUTH-012; RISK-AUTH-005, RISK-AUTH-010 |
| TC-AUTH-014 | Consecutive Sequence | TS-AUTH-014 | Failures across successful login are not consecutive | Account A unlocked; counter = 0. | 1. Submit three incorrect passwords.<br>2. Submit correct password.<br>3. Submit two incorrect passwords.<br>4. Observe state. | Account A; incorrect password ×5 across two sequences; correct password. | Valid login resets first sequence; later two failures form a new sequence with counter 2; account remains unlocked. | High | AC-02, AC-08, AC-09; BR-AUTH-003, BR-AUTH-011, BR-AUTH-012; RISK-AUTH-005, RISK-AUTH-010 |
| TC-AUTH-015 | Account Isolation | TS-AUTH-015 | Failed-attempt tracking is isolated between accounts | Account A/B unlocked; each counter = 0. | 1. Submit four incorrect passwords for A.<br>2. Submit one incorrect password for B.<br>3. Observe both states.<br>4. Submit correct password for B. | Account A/B; incorrect passwords; B correct password. | A counter = 4/unlocked; B counter = 1/unlocked; B is not treated as threshold 5; B valid login succeeds. | High | AC-01; BR-AUTH-001, BR-AUTH-002; RISK-AUTH-004 |
| TC-AUTH-016 | Post-Unlock Sequence | TS-AUTH-016 | First failure after automatic unlock starts at one | Account A previously locked; 15-minute duration expired; automatic unlock occurred. | 1. Submit one incorrect-password login after unlock.<br>2. Observe counter/state. | Account A; incorrect password. | Authentication rejected; counter = 1; account remains unlocked; prior lifecycle failures do not contribute. | High | AC-01, AC-02, AC-07, AC-09; BR-AUTH-002, BR-AUTH-003, BR-AUTH-010, BR-AUTH-012; RISK-AUTH-006 |
| TC-AUTH-017 | Repeated Lifecycle | TS-AUTH-017 | Account enters a new lock lifecycle after automatic unlock | Prior lock expired; account auto-unlocked; counter reset to 0. | 1. Submit four new incorrect-password attempts.<br>2. Verify unlocked.<br>3. Submit fifth new incorrect password.<br>4. Observe state. | Account A; incorrect password ×5. | New failures 1–4 keep account unlocked; fifth new failure sets counter 5 and locks account; previous lifecycle does not contribute. | High | AC-02, AC-03, AC-06, AC-07, AC-09; BR-AUTH-003, BR-AUTH-004, BR-AUTH-009, BR-AUTH-010, BR-AUTH-012; RISK-AUTH-002, RISK-AUTH-006, RISK-AUTH-010 |

---

## Shared Test Data / Dependencies

| Test Data ID | Description |
|---|---|
| TD-AUTH-001 | Registered Account A, unlocked, counter = 0 |
| TD-AUTH-002 | Registered Account B, unlocked, counter = 0 |
| TD-AUTH-003 | Correct password for Account A |
| TD-AUTH-004 | Correct password for Account B |
| TD-AUTH-005 | Incorrect password for Account A |
| TD-AUTH-006 | Incorrect password for Account B |

---

## Execution Notes

Where a specific counter state is needed, prepare it through the defined login flow rather than assuming direct database modification. A reliable test clock may be used for timing observation, but timer implementation is not part of the expected result.

---

## Open Questions

None required by `REQ-AUTH-001`. The source intentionally has no known ambiguity. No expected result is added for unspecified implementation side effects of attempts made while locked.

---

## Coverage Summary

All confirmed scenarios `TS-AUTH-001` through `TS-AUTH-017` have executable coverage. The table preserves the critical 1/4/5 boundary, lock start/expiry behavior, active-lock rejection, reset paths, per-account isolation, and repeated lifecycle while keeping unspecified implementation behavior outside authoritative expected results.
