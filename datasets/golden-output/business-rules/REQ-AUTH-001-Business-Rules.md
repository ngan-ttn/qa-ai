# Business Rules — Account Lockout After Failed Login Attempts

## Golden Output Metadata

- Dataset ID: `REQ-AUTH-001`
- Source Requirement: `datasets/requirements/simple/REQ-AUTH-001.md`
- Artifact Type: `Business Rules`
- Review Status: `Approved`
- Evaluation Purpose: Reference output for evaluating business-rule extraction accuracy, boundary/state preservation, traceability, and assumption control

---

## Rule Summary

The confirmed business-rule model covers per-account failed-attempt tracking, counter increment, below-threshold behavior, lock at five consecutive failures, 15-minute lock timing, locked-state password rejection, automatic unlock, counter reset, and new consecutive sequences after reset.

---

## Business Rules

| Rule ID | Rule Type | Business Rule | Conditions / Inputs | Expected Outcome / Constraint | Source Traceability | Dependencies | Status |
|---|---|---|---|---|---|---|---|
| BR-AUTH-001 | Constraint | Consecutive failed login attempts are tracked separately for each registered account. | Password-based login attempts occur for registered accounts. | One account's failed attempts do not contribute to another account's sequence. | Requirement; AC-01; Constraints/Notes | N/A | Confirmed |
| BR-AUTH-002 | Validation | Each incorrect password entered for an unlocked account increases that account's consecutive failed-attempt counter by one. | Account unlocked; incorrect password submitted. | Authentication fails and the corresponding account counter increments by 1. | Requirement; AC-01 | BR-AUTH-001 | Confirmed |
| BR-AUTH-003 | Decision | An account remains unlocked while its consecutive failed-attempt counter is below five. | Counter after current failed attempt = 1–4. | Account remains unlocked. | Requirement; AC-02 | BR-AUTH-002 | Confirmed |
| BR-AUTH-004 | State | The fifth consecutive failed login attempt locks the account. | Counter before attempt = 4; next password is incorrect. | Counter reaches 5 and account transitions to locked. | Requirement; AC-03 | BR-AUTH-002, BR-AUTH-003 | Confirmed |
| BR-AUTH-005 | Constraint | A temporary account lock lasts 15 minutes. | Account has entered locked state. | Lock remains active until the defined duration expires. | Requirement; AC-06 | BR-AUTH-004 | Confirmed |
| BR-AUTH-006 | Time / State | The 15-minute lock duration begins when the fifth consecutive failed login attempt is recorded. | Fifth consecutive failure is recorded. | Lock timer starts at that event. | Requirement; AC-04 | BR-AUTH-004, BR-AUTH-005 | Confirmed |
| BR-AUTH-007 | Permission | All password-based login attempts for a locked account are rejected while the lock remains active. | Account locked; password-based login attempted. | Authentication is rejected. | Requirement; AC-05 | BR-AUTH-004 | Confirmed |
| BR-AUTH-008 | Permission | Correct password does not bypass an active account lock. | Account locked; correct password submitted. | Authentication remains rejected. | Requirement; AC-05 | BR-AUTH-007 | Confirmed |
| BR-AUTH-009 | State | The account automatically unlocks when the 15-minute lock duration expires. | Account locked; 15-minute duration expires. | Account transitions to unlocked automatically. | Requirement; AC-06 | BR-AUTH-005, BR-AUTH-006 | Confirmed |
| BR-AUTH-010 | State | Automatic unlock resets the failed-attempt counter to zero. | Automatic unlock occurs. | Counter = 0. | Requirement; AC-07 | BR-AUTH-009 | Confirmed |
| BR-AUTH-011 | State | A successful login before account lock resets the failed-attempt counter to zero. | Account unlocked with 1–4 consecutive failures; valid credentials submitted. | Authentication succeeds; counter = 0. | Requirement; AC-08 | BR-AUTH-003 | Confirmed |
| BR-AUTH-012 | Sequence | After the counter is reset, the next failed login starts a new consecutive sequence at one. | Counter reset by successful login or automatic unlock; next incorrect password occurs. | New sequence begins with counter = 1. | Requirement; AC-09 | BR-AUTH-010, BR-AUTH-011 | Confirmed |

---

## Decision / Boundary Reference

| Condition / Event | Expected Business State |
|---|---|
| Consecutive failures = 1–4 | Account remains unlocked. |
| Fifth consecutive failure recorded | Account locks; 15-minute duration starts. |
| Locked + correct or incorrect password | Password-based authentication rejected. |
| 15-minute duration expires | Account unlocks automatically; counter resets to 0. |
| Successful login before lock | Counter resets to 0. |
| First failure after reset | New consecutive sequence starts at 1. |

---

## Assumptions

None. The dataset intentionally introduces no known ambiguity. Implementation mechanisms for persistence, timer tracking, and automatic unlock are outside the source contract and are not converted into business rules.

---

## Open Questions

None required by the controlled dataset. Potential implementation questions do not change the confirmed business behavior above.

---

## Rule Coverage Summary

All nine acceptance criteria and the account-specific tracking constraint are represented. No confirmed rule is derived from implementation assumptions.
