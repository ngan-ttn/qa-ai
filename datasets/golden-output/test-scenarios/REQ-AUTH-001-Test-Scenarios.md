# Test Scenarios — Account Lockout After Failed Login Attempts

## Golden Output Metadata

- Dataset ID: `REQ-AUTH-001`
- Source Requirement: `datasets/requirements/simple/REQ-AUTH-001.md`
- Artifact Type: `Test Scenarios`
- Review Status: `Approved`
- Evaluation Purpose: Reference output for evaluating scenario coverage, boundary/state-transition coverage, sequence behavior, risk-based prioritization, traceability, and assumption control

---

## Scenario Summary

The scenario set validates normal authentication, per-account failed-attempt tracking, the 1–4 / 5 threshold boundary, lock timing, locked-state password rejection, automatic unlock, both counter-reset paths, new consecutive sequences, account isolation, and repeated lifecycle.

---

## Scope

Only username-and-password authentication behavior defined by `REQ-AUTH-001` is in scope. Implementation-specific persistence, timer mechanism, and automatic-unlock mechanism remain outside the scenario contract.

---

## Assumptions

None. The controlled dataset intentionally introduces no known ambiguity. Scenarios do not assign behavior to implementation mechanisms that the source does not define.

---

## Test Scenarios

| Scenario ID | Module / Feature | Scenario | Type | Preconditions / Conditions | Expected Behavior | Requirement / Rule Traceability | Risk Traceability | Priority |
|---|---|---|---|---|---|---|---|---|
| TS-AUTH-001 | Authentication | Verify an unlocked account can authenticate successfully using the correct password. | Positive | Registered account; unlocked; correct password. | Authentication succeeds; any below-threshold prior sequence resets according to BR-AUTH-011. | AC-08; BR-AUTH-011 | N/A | Medium |
| TS-AUTH-002 | Failed Attempt Tracking | Verify an incorrect password increments the failed-attempt counter for the corresponding account. | Negative / Functional | Account unlocked; incorrect password. | Authentication is rejected and that account's counter increments by 1. | AC-01; BR-AUTH-001, BR-AUTH-002 | RISK-AUTH-004 | High |
| TS-AUTH-003 | Threshold | Verify the account remains unlocked after the first consecutive failed login attempt. | Boundary | Fresh sequence; first incorrect password. | Counter = 1; account remains unlocked. | AC-01, AC-02; BR-AUTH-002, BR-AUTH-003 | N/A | High |
| TS-AUTH-004 | Threshold | Verify the account remains unlocked after four consecutive failed login attempts. | Boundary | Four consecutive incorrect-password failures. | Counter = 4; account remains unlocked. | AC-02; BR-AUTH-003 | RISK-AUTH-001, RISK-AUTH-010 | High |
| TS-AUTH-005 | Threshold / Lock | Verify the fifth consecutive failed login attempt locks the account. | Boundary / State | Counter before attempt = 4; next password incorrect. | Counter reaches 5; account transitions from unlocked to locked. | AC-03; BR-AUTH-004 | RISK-AUTH-001, RISK-AUTH-002, RISK-AUTH-010 | High |
| TS-AUTH-006 | Lock Timing | Verify the 15-minute lock duration starts when the fifth consecutive failed attempt is recorded. | Time Boundary | Fifth consecutive failure is recorded. | Lock-period start point is the fifth recorded failure. | AC-04; BR-AUTH-005, BR-AUTH-006 | RISK-AUTH-009 | High |
| TS-AUTH-007 | Locked State | Verify the correct password cannot authenticate while the account is locked. | Negative / State | Account locked; lock duration active; correct password. | Authentication is rejected. | AC-05; BR-AUTH-007, BR-AUTH-008 | RISK-AUTH-003 | High |
| TS-AUTH-008 | Locked State | Verify an incorrect-password login attempt is rejected while the account is locked. | Negative / State | Account locked; lock duration active; incorrect password. | Authentication is rejected; no additional counter/timer behavior is asserted. | AC-05; BR-AUTH-007 | RISK-AUTH-011 | High |
| TS-AUTH-009 | Lock Duration | Verify the account remains locked before the 15-minute duration expires. | Time Boundary | Account locked; less than 15 minutes elapsed. | Account remains locked and password-based authentication remains rejected. | AC-05, AC-06; BR-AUTH-005, BR-AUTH-007, BR-AUTH-009 | RISK-AUTH-007 | High |
| TS-AUTH-010 | Automatic Unlock | Verify the account automatically unlocks when the 15-minute duration expires. | Time Boundary / State | Account locked; 15-minute duration expires. | Account transitions to unlocked automatically. | AC-06; BR-AUTH-005, BR-AUTH-009 | RISK-AUTH-007, RISK-AUTH-008, RISK-AUTH-009 | High |
| TS-AUTH-011 | Automatic Unlock | Verify automatic unlock resets the failed-attempt counter to zero. | State / Data | Automatic unlock occurs. | Account = unlocked; failed-attempt counter = 0. | AC-07; BR-AUTH-010 | RISK-AUTH-006 | High |
| TS-AUTH-012 | Counter Reset | Verify a successful login after one failed attempt resets the counter. | Sequence | One failed attempt; account unlocked; correct password submitted. | Authentication succeeds; counter resets to 0; next failure begins a new sequence. | AC-08; BR-AUTH-011, BR-AUTH-012 | N/A | High |
| TS-AUTH-013 | Counter Reset | Verify a successful login after four consecutive failed attempts resets the counter before lock. | Boundary / Sequence | Four consecutive failures; account unlocked; correct password submitted. | Authentication succeeds; counter resets to 0; account does not lock from prior failures. | AC-08; BR-AUTH-011, BR-AUTH-012 | RISK-AUTH-005, RISK-AUTH-010 | High |
| TS-AUTH-014 | Consecutive Sequence | Verify failures before and after a successful login are separate sequences. | Sequence | Example: 3 failures → successful login → 2 failures. | Final state represents two consecutive failures; account remains unlocked. | AC-02, AC-08, AC-09; BR-AUTH-003, BR-AUTH-011, BR-AUTH-012 | RISK-AUTH-005, RISK-AUTH-010 | High |
| TS-AUTH-015 | Account Isolation | Verify failed-attempt tracking for one account does not affect another account. | Isolation | Account A and B registered; failures applied independently. | Each account maintains its own consecutive sequence. | AC-01; BR-AUTH-001, BR-AUTH-002 | RISK-AUTH-004 | High |
| TS-AUTH-016 | Post-Unlock Sequence | Verify the first failed login after automatic unlock starts a new sequence at one. | State / Sequence | Automatic unlock completed; next password incorrect. | Attempt is rejected; counter becomes 1; account remains unlocked. | AC-01, AC-02, AC-07, AC-09; BR-AUTH-002, BR-AUTH-003, BR-AUTH-010, BR-AUTH-012 | RISK-AUTH-006 | High |
| TS-AUTH-017 | Repeated Lifecycle | Verify an automatically unlocked account locks again only after five new consecutive failures. | State / Boundary / Sequence | Prior lock expired and counter reset; five new failures occur. | New failures 1–4 remain unlocked; fifth new failure locks account again. | AC-02, AC-03, AC-06, AC-07, AC-09; BR-AUTH-003, BR-AUTH-004, BR-AUTH-009, BR-AUTH-010, BR-AUTH-012 | RISK-AUTH-002, RISK-AUTH-006, RISK-AUTH-010 | High |

---

## Out of Scope

- Technical storage of counter/lock state.
- Technical timer implementation.
- Non-password authentication.
- Administrative/manual unlock behavior.
- Behavior not specified by the controlled dataset.

---

## Open Questions

None are required by the source dataset. Test ideas involving implementation-specific mechanisms remain outside confirmed scenario behavior.

---

## Coverage Summary

All nine acceptance criteria are represented. Critical boundary coverage includes failed counts 1, 4, and 5 plus before/at 15-minute expiry; state coverage includes `Unlocked → Locked → Unlocked`; sequence coverage includes successful-login reset, automatic-unlock reset, new sequences, account isolation, and repeated lock lifecycle.
