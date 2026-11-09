# Test Cases

## Run Context

- Source scenarios: `examples/account-lockout/Test-Scenarios.md`
- Stage: `skills/testcase-generator`
- Generation mode: Fresh / full generation
- Structured Coverage Assessment: not supplied
- Specialized API or SQL design: not requested

## Test Suite Summary

Executable cases for username-and-password account lockout on `REQ-AUTH-001`. Each case checks one confirmed outcome. Counter values are stated at the level the requirement uses. No case asserts a counter change during an active lock, a rejection message, an unregistered username, or the exact expiry instant.

## Shared Preconditions / Environment

- Password-based login is available for registered accounts.
- Account A and Account B are two different registered accounts.
- P-correct-A and P-correct-B are the correct passwords for those accounts. The source does not define password values, so the cases use these logical names.
- P-incorrect is a password that is not correct for the account under test.
- Where a case needs the counter at zero, the setup includes a successful login while the account is not locked. That is the confirmed reset. The counter of an account that has never failed is not treated as zero.
- The tester records the moment the fifth consecutive failed attempt is recorded and uses that moment to judge the 15 minutes. This does not define a product clock.
- Seeing the numeric counter is an execution dependency (OQ-02). Do not invent a page, API, or database field. Where a step uses a later password attempt, the expected result says what that attempt is allowed to prove.

## Test Cases

| Test Case ID | Module / Function | Scenario ID | Test Case Title | Preconditions / Setup | Test Steps | Test Data | Expected Result | Priority | Traceability |
|---|---|---|---|---|---|---|---|---|---|
| TC-001 | Account lockout | SC-001 | One incorrect password sets the counter to 1 and leaves the account unlocked | Account A is not locked. A successful login has reset its counter to zero. | 1. Submit a password login for Account A with P-incorrect. | Account A; P-incorrect | 1. The login fails. The failed-attempt counter for Account A is 1. Account A is unlocked. | High | REQ-AUTH-001; AC-1; AC-2; BR-002; BR-003 |
| TC-002 | Account lockout | SC-002 | Four consecutive incorrect passwords leave the counter at 4 and the account unlocked | Account A is not locked. A successful login has reset its counter to zero. | 1. Submit four consecutive password logins for Account A with P-incorrect, and no successful login between them. | Account A; P-incorrect | 1. Each login fails. After the fourth failure the counter is 4 and Account A is unlocked. | High | REQ-AUTH-001; AC-1; AC-2; BR-002; BR-003 |
| TC-003 | Account lockout | SC-003 | The fifth consecutive incorrect password locks the account | Account A is not locked and its counter is 4 after four consecutive incorrect passwords. | 1. Submit one more password login for Account A with P-incorrect. | Account A; P-incorrect | 1. The login fails and Account A is locked. | High | REQ-AUTH-001; AC-3; BR-004 |
| TC-004 | Account lockout | SC-004 | The 15-minute duration starts at the recorded fifth failure | Account A is not locked and its counter is 4. The tester can record the time the next attempt is recorded. | 1. Record the time immediately before the next attempt.<br>2. Submit P-incorrect for Account A.<br>3. Record the time that fifth failure is recorded. | Account A; P-incorrect; tester time record | 1. The time before the attempt is not the lock start.<br>2. The login fails and Account A is locked.<br>3. The 15-minute duration starts at the recorded time of this fifth failure. | High | REQ-AUTH-001; AC-4; BR-004; BR-005 |
| TC-005 | Account lockout | SC-005 | An incorrect password is rejected during the lock | Account A is locked. Less than 15 minutes have elapsed since its fifth consecutive failure was recorded. | 1. Submit P-incorrect for Account A. | Account A; P-incorrect | 1. The login is rejected and Account A remains locked. No counter change is asserted. | High | REQ-AUTH-001; AC-5; BR-006 |
| TC-006 | Account lockout | SC-006 | The correct password is rejected during the lock | Account A is locked. Less than 15 minutes have elapsed since its fifth consecutive failure was recorded. | 1. Submit P-correct-A for Account A. | Account A; P-correct-A | 1. The login is rejected and Account A remains locked. No counter change is asserted. | High | REQ-AUTH-001; AC-5; BR-006 |
| TC-007 | Account lockout | SC-007 | The account is still locked before 15 minutes have elapsed | Account A is locked. The tester has the recorded time of the fifth consecutive failure. | 1. Wait until a time that is after that recording and before 15 minutes have elapsed.<br>2. Submit P-correct-A for Account A. | Account A; P-correct-A; tester time record | 1. The 15-minute duration has not expired.<br>2. The login is rejected and Account A remains locked. | High | REQ-AUTH-001; AC-5; AC-6; BR-005; BR-006 |
| TC-008 | Account lockout | SC-008 | After 15 minutes the account is unlocked and the counter is zero | Account A is locked. The tester has the recorded time of the fifth consecutive failure. | 1. Wait until 15 minutes after that recorded time have elapsed.<br>2. Observe the lock state and failed-attempt counter without submitting a new password. | Account A; tester time record | 1. The lock duration has expired.<br>2. Account A is unlocked and its failed-attempt counter is zero. | High | REQ-AUTH-001; AC-6; AC-7; BR-007 |
| TC-009 | Account lockout | SC-009 | A successful login before lock resets the counter to zero | Account A is unlocked and its counter is 3 after three consecutive incorrect passwords. | 1. Submit P-correct-A for Account A. | Account A; P-incorrect; P-correct-A | 1. The login succeeds and the failed-attempt counter for Account A is zero. | High | REQ-AUTH-001; AC-8; BR-008; BR-011 |
| TC-010 | Account lockout | SC-010 | The first failure after a reset starts a new sequence at one | Account A is unlocked and its counter is zero because TC-009's successful login just reset it. | 1. Submit P-incorrect for Account A. | Account A; P-incorrect | 1. The login fails, the counter is 1, and Account A is unlocked. | High | REQ-AUTH-001; AC-9; BR-009 |
| TC-011 | Account lockout | SC-011 | The new sequence locks on its fifth consecutive failure | Account A is unlocked and its counter is zero because a confirmed reset has occurred. | 1. Submit four consecutive logins for Account A with P-incorrect.<br>2. Submit a fifth consecutive login for Account A with P-incorrect. | Account A; P-incorrect | 1. All four logins fail, the counter is 4, and Account A stays unlocked.<br>2. The fifth login fails and Account A is locked. | High | REQ-AUTH-001; AC-3; AC-9; BR-004; BR-009 |
| TC-012 | Account lockout | SC-012 | Account B stays independent while Account A is locked | Account A is locked and 15 minutes have not elapsed. Account B is unlocked and a successful login has reset Account B's counter to zero. | 1. Submit P-incorrect for Account A.<br>2. Submit P-correct-B for Account B. | Account A; Account B; P-incorrect; P-correct-B | 1. Account A's login is rejected and Account A stays locked.<br>2. Account B's login succeeds. Account A's failures do not change Account B's counter or lock state. | High | REQ-AUTH-001 Constraints; AC-5; BR-001; BR-006; BR-011 |

## Shared Test Data / Dependencies

| Data | Use |
|---|---|
| Account A | Registered account under lockout checks. |
| Account B | Second registered account for isolation. |
| P-correct-A | Correct password for Account A. Value is not defined by the source. |
| P-correct-B | Correct password for Account B. Value is not defined by the source. |
| P-incorrect | A password that is not correct for the account submitting it. |

No API contract or database schema is in the source. This suite does not add API tests or SQL checks.

## Execution Notes

- OQ-02: if the counter or lock state cannot be observed except by another password attempt, TC-008 cannot be completed as written, because a correct-password success also resets the counter and would hide whether expiry had already set it to zero. Do not replace that observation with an invented signal.
- TC-010 and TC-011 may follow a confirmed reset. They do not claim to observe the counter during a lock.
- TC-005 and TC-006 must not be failed or passed on a counter change. That change is OQ-01.
- Elapsed time is judged by the tester from the recorded fifth failure. The source does not define the product's timing mechanism.
- This file is a fresh generation. It does not preserve or replace any earlier testcase IDs.

## Open Questions

| ID | Why it is not an executable row |
|---|---|
| OQ-01 | No oracle for the counter while the account is locked. |
| OQ-02 | No defined observation signal. It limits how TC-008 is executed. It does not remove the confirmed expiry outcome. |
| OQ-03 | No initial counter for an account that has never failed. Cases use a confirmed reset instead. |
| OQ-04 | No oracle for the exact expiry instant. |
| OQ-05 | No oracle for rejection text or codes. |
| OQ-06 | No oracle for an unregistered username. |
| OQ-07 | No oracle for concurrent attempts. |

## Coverage Summary

- Executable test cases: 12 (TC-001 through TC-012).
- Scenarios: 12 (SC-001 through SC-012). Each scenario has one executable row.
- Acceptance criteria AC-1 through AC-9 each appear in at least one row.
- Counts 2 and 3 are not separate rows. They are the same unlocked outcome as AC-2, already bounded by TC-001 and TC-002.
- Clarification-dependent behavior excluded from the executable table: OQ-01, OQ-04, OQ-05, OQ-06, OQ-07.
- No case is marked blocked inside the executable table.
