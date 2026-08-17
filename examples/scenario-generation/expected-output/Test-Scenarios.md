# Test Scenarios — Account Lock After Failed Login Attempts

## Scenario Summary

This scenario set covers successful authentication, failed-login tracking, the five-attempt lock threshold, successful-login reset, locked-state behavior, 30-minute automatic unlock, post-unlock tracking, account isolation, and repeated lock lifecycle. Undefined behavior remains clarification-dependent.

---

## Scope

- Authentication and incorrect-password handling.
- Consecutive failed-login tracking per account.
- Threshold boundary at five failures.
- Successful-login counter reset.
- Temporary account lock and locked-state authentication rejection.
- 30-minute lock duration and automatic unlock.
- Post-unlock tracking and repeated lifecycle.
- Account isolation.

---

## Assumptions

No expected behavior is added for timer-boundary semantics, attempts during lock, cross-device aggregation, unknown-account handling, concurrency, or exact post-unlock numeric counter state unless defined by the requirement.

---

## Test Scenarios

| Scenario ID | Module / Feature | Scenario | Type | Preconditions / Conditions | Expected Behavior | Requirement / Rule Traceability | Risk Traceability | Priority |
|---|---|---|---|---|---|---|---|---|
| TS-001 | Authentication | Verify a registered user with valid credentials can log in when the account is not locked. | Positive | Registered account; account unlocked; valid credentials. | Authentication succeeds. | Requirements 1–3 | N/A | Medium |
| TS-002 | Authentication | Verify login fails when a registered user enters an incorrect password. | Negative | Registered account; account unlocked; incorrect password. | Authentication fails and the failed attempt is recorded for that account. | Requirements 4–5 | N/A | High |
| TS-003 | Failed Login Tracking | Verify the first consecutive incorrect-password attempt is recorded and the account remains unlocked. | Boundary | New failure sequence; first incorrect-password attempt. | Failure is recorded; account remains unlocked. | Requirements 5–6; AC-01 | N/A | High |
| TS-004 | Failed Login Tracking | Verify the account remains unlocked after four consecutive incorrect-password attempts. | Boundary | Four consecutive incorrect-password attempts; no successful login between attempts. | All attempts fail; account remains unlocked after attempt 4. | Requirement 6; AC-01 | N/A | High |
| TS-005 | Account Lock | Verify the account becomes temporarily locked on the fifth consecutive incorrect-password attempt. | Boundary / State | Account unlocked with four consecutive failures; fifth incorrect-password attempt occurs. | Fifth attempt fails and account transitions to temporarily locked. | Requirements 6, 8; AC-02 | N/A | High |
| TS-006 | Counter Reset | Verify a successful login after one to four consecutive failures resets the failed-login sequence. | Positive / State | Account unlocked with 1–4 consecutive failures; valid credentials submitted. | Login succeeds and the previous failed-login sequence is reset. | Requirement 7; AC-05 | N/A | High |
| TS-007 | Counter Reset | Verify a new failed-login sequence starts after the counter is reset by successful login. | State | Successful-login reset completed; later incorrect password submitted. | Later failure belongs to a new sequence and does not inherit previous failures. | Requirement 7; AC-05 | N/A | High |
| TS-008 | Account Lock | Verify a locked account cannot authenticate when the correct password is entered. | Negative / State | Account locked; 30-minute period not expired; correct password submitted. | Authentication is rejected. | Requirement 10; AC-03 | N/A | High |
| TS-009 | Account Lock | Verify a login attempt against a locked account is rejected when an incorrect password is entered. | Negative / State | Account locked; incorrect password submitted. | Authentication is rejected; no counter/timer effect is asserted. | Requirements 10–11; AC-03 | N/A | High |
| TS-010 | Account Lock | Verify the defined temporary-lock message is displayed for a login attempt while locked. | Functional | Account locked; login attempted. | Authentication is rejected and `Your account has been temporarily locked. Please try again later.` is displayed. | Requirement 11; AC-03 | N/A | Medium |
| TS-011 | Lock Duration | Verify the account remains locked before the 30-minute lock period expires. | Time Boundary | Account locked; less than 30 minutes elapsed. | Account remains locked and authentication is rejected. | Requirements 9–10 | N/A | High |
| TS-012 | Automatic Unlock | Verify the account is automatically unlocked after the 30-minute lock period expires. | Time Boundary / State | Account locked; defined lock period expires. | Account automatically transitions to unlocked. | Requirement 12; AC-04 | N/A | High |
| TS-013 | Automatic Unlock | Verify valid credentials can authenticate after automatic unlock. | Positive / State | Automatic unlock completed; valid credentials submitted. | Authentication succeeds. | Requirements 12–13; AC-04 | N/A | High |
| TS-014 | Post-Unlock Tracking | Verify failed-login tracking starts again after automatic unlock. | State | Automatic unlock completed; new incorrect-password attempts occur. | New failed-login tracking sequence begins. | Requirement 14 | N/A | High |
| TS-015 | Post-Unlock Tracking | Verify previous pre-lock failures do not cause an earlier lock in the new post-unlock sequence. | State / Boundary | Account automatically unlocked; four new failures occur. | Account remains unlocked through the fourth new failure. | Requirement 14 | N/A | High |
| TS-016 | Account Isolation | Verify failed-login attempts for one registered account do not affect another account. | Isolation | Two registered unlocked accounts; failures applied to Account A. | Account B's failed-login state remains unaffected. | Requirement 5; Notes | N/A | High |
| TS-017 | Account Isolation | Verify one account can remain available while another account is temporarily locked. | Isolation / State | Account A locked; Account B registered and unlocked. | Account B remains able to authenticate independently. | Requirements 5, 8–10 | N/A | High |
| TS-018 | Repeated Lifecycle | Verify an account can enter a new lock cycle after automatic unlock when five new consecutive failures occur. | End-to-End State | Prior lock expired; new failure sequence begins. | Account locks again only on the fifth new consecutive failure. | Requirements 6, 8, 12–14 | N/A | High |
| TS-019 | Counter Reset | Verify multiple successful-login resets do not carry failures from earlier sequences into later sequences. | State | Multiple below-threshold failure sequences separated by successful logins. | Each successful login resets its current sequence; earlier failures do not accumulate. | Requirement 7 | N/A | Medium |
| TS-020 | Lock Lifecycle | Verify the complete lifecycle from unlocked state through five failures, temporary lock, automatic unlock, and successful login. | End-to-End | New sequence; account unlocked initially. | Account remains unlocked through failure 4, locks on failure 5, rejects login while locked, unlocks after 30 minutes, then permits valid authentication. | Requirements 5–14; AC-01–AC-05 | N/A | High |

---

## Out of Scope

No implementation-specific persistence, API, database, timer-storage, device/session aggregation, or concurrency behavior is asserted unless it is explicitly defined by the requirement.

---

## Open Questions / Clarification-Dependent Coverage

| Item ID | Area | Potential Scenario | Missing Information |
|---|---|---|---|
| CD-001 | Lock Timer | Login exactly at the 30-minute expiration boundary. | Exact timer-boundary semantics are undefined. |
| CD-002 | Locked Attempts | Counter behavior for login attempts made while locked. | Effect on failed-login counter is undefined. |
| CD-003 | Lock Extension | Whether repeated attempts while locked affect lock expiration. | Timer extension/restart behavior is undefined. |
| CD-004 | Cross-Device | Failed-login accumulation across devices/browsers/sessions. | Cross-device/session tracking behavior is not explicit. |
| CD-005 | Unknown Account | Login using an unregistered email address. | Unknown-account behavior is undefined. |
| CD-006 | Concurrency | Simultaneous failed attempts when the account has four failures. | Concurrent counter/locking semantics are undefined. |
| CD-007 | Post-Unlock Counter | Exact numeric counter immediately after automatic unlock. | Requirement states tracking starts again but does not explicitly define the numeric value. |

---

## Coverage Summary

| Coverage Area | Scenario IDs |
|---|---|
| Authentication | TS-001, TS-002 |
| Failed-login threshold | TS-003, TS-004, TS-005 |
| Counter reset / new sequence | TS-006, TS-007, TS-019 |
| Locked-state behavior | TS-008, TS-009, TS-010 |
| Lock duration / automatic unlock | TS-011, TS-012, TS-013 |
| Post-unlock tracking | TS-014, TS-015 |
| Account isolation | TS-016, TS-017 |
| Repeated / E2E lifecycle | TS-018, TS-020 |

The highest-priority coverage remains the `4 → 5` threshold, authentication rejection while locked, the 30-minute lifecycle, successful-login reset, post-unlock tracking, and account isolation.
