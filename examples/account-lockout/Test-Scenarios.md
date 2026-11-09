# Test Scenarios

## Run Context

- Source rules: `examples/account-lockout/Business-Rules.md`
- Stage: `skills/scenario-generator`
- Generation mode: Fresh / full generation
- Structured Risk Analysis: not supplied. Risk Traceability is `N/A`.

## Scenario Summary

The scenarios check per-account password lockout at the behavior level: counting incorrect passwords, the unlocked range below five, the fifth-failure lock, where the 15 minutes start, rejection of both incorrect and correct passwords during the lock, behavior before expiry, automatic unlock and reset, reset by a successful login, a new sequence after reset, and isolation between two accounts.

## Scope

Username-and-password login for registered accounts, including the lock and the two confirmed ways the failed-attempt counter returns to zero.

## Assumptions

None used as expected behavior.

## Test Scenarios

| Scenario ID | Module / Feature | Scenario | Type | Preconditions / Conditions | Expected Behavior | Requirement / Rule Traceability | Risk Traceability | Priority |
|---|---|---|---|---|---|---|---|---|
| SC-001 | Account lockout | One incorrect password increases that account's counter by one and does not lock it | State | The account is unlocked and a confirmed reset has set its counter to zero. One incorrect password is submitted. | The attempt fails, the counter is 1, and the account stays unlocked. | REQ-AUTH-001; AC-1; AC-2; BR-002; BR-003 | N/A | High |
| SC-002 | Account lockout | Four consecutive incorrect passwords leave the account unlocked with counter 4 | Boundary | The counter is zero after a confirmed reset. Four incorrect passwords are submitted with no successful login between them. | Each attempt fails. After the fourth, the counter is 4 and the account stays unlocked. | REQ-AUTH-001; AC-2; BR-002; BR-003 | N/A | High |
| SC-003 | Account lockout | The fifth consecutive incorrect password locks the account | Boundary | Four consecutive failures are already counted. The next password is incorrect. | The fifth attempt fails and the account becomes locked. | REQ-AUTH-001; AC-3; BR-004 | N/A | High |
| SC-004 | Account lockout | The 15-minute lock starts when the fifth failure is recorded | State | The fifth consecutive failure is the event being timed. | The 15 minutes are measured from the recording of that fifth failure, not from an earlier failure. | REQ-AUTH-001; AC-4; BR-005 | N/A | High |
| SC-005 | Account lockout | An incorrect password is rejected while the account is locked | Negative | The account is locked and 15 minutes have not elapsed since the fifth failure was recorded. | The incorrect-password attempt is rejected and the account stays locked. | REQ-AUTH-001; AC-5; BR-006 | N/A | High |
| SC-006 | Account lockout | The correct password is rejected while the account is locked | Negative | The account is locked and 15 minutes have not elapsed since the fifth failure was recorded. | The correct-password attempt is rejected and the account stays locked. | REQ-AUTH-001; AC-5; BR-006 | N/A | High |
| SC-007 | Account lockout | The account stays locked before the 15-minute duration expires | Boundary | The fifth failure has been recorded and the 15-minute duration has not yet expired. | A password-based attempt is rejected and the account remains locked. | REQ-AUTH-001; AC-5; AC-6; BR-005; BR-006 | N/A | High |
| SC-008 | Account lockout | Expiry unlocks the account and resets the counter to zero | State | 15 minutes have elapsed since the fifth consecutive failure was recorded. | The account is unlocked and the failed-attempt counter is zero. | REQ-AUTH-001; AC-6; AC-7; BR-007 | N/A | High |
| SC-009 | Account lockout | A successful login before lock resets the counter to zero | State | The account is unlocked and its counter is 1, 2, 3, or 4. The correct password is submitted. | The login succeeds and the counter is zero. | REQ-AUTH-001; AC-8; BR-008; BR-011 | N/A | High |
| SC-010 | Account lockout | The first failure after a reset starts a new sequence at one | State | The counter has been reset to zero by a successful login or by expiry. The next password is incorrect. | The attempt fails, the counter is 1, and the account stays unlocked. | REQ-AUTH-001; AC-9; BR-009 | N/A | High |
| SC-011 | Account lockout | A new sequence locks on its own fifth consecutive failure | Boundary | The counter has been reset to zero. Five new consecutive incorrect passwords follow, with no success between them. | The account stays unlocked through the fourth new failure and locks on the fifth. | REQ-AUTH-001; AC-3; AC-9; BR-004; BR-009 | N/A | High |
| SC-012 | Account lockout | Failures and lock on one account do not change another account | State | Two registered accounts. Account A is accumulating failures or is locked. Account B is unlocked. | Account B's counter and lock state stay independent of Account A. Account B's correct password still succeeds while Account A is locked. | REQ-AUTH-001 Constraints; BR-001 | N/A | High |

## Out of Scope

- Authentication methods other than username and password (BR-010).
- The mechanism that stores the counter, tracks expiry, or performs automatic unlock.
- Unregistered usernames, concurrent attempts, rejection text, and the exact expiry instant (OQ-04, OQ-05, OQ-06, OQ-07).
- Whether an attempt during the lock changes the counter (OQ-01).

## Open Questions

The open questions are OQ-01 through OQ-07 from the business-rule model. None of them is given a scenario expected result.

## Coverage Summary

- Scenarios: 12 (SC-001 through SC-012).
- Confirmed rules referenced: BR-001, BR-002, BR-003, BR-004, BR-005, BR-006, BR-007, BR-008, BR-009, BR-011.
- BR-010 is the scope constraint recorded under Out of Scope, not a separate behavior scenario.
- AC-1 through AC-9 each have at least one scenario.
- Counts 2 and 3 are the same confirmed outcome as the below-five rule. They are represented by SC-001 and SC-002 at the ends of that range, not by extra scenarios.
- No risk IDs exist because risk analysis was not run.
