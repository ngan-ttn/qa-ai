# Business Rules — Account Lock After Failed Login Attempts

## Rule Summary

The feature defines account-level protection against repeated failed login attempts: incorrect-password failures are tracked per account, five consecutive failures trigger a temporary 30-minute lock, authentication is blocked while locked, and the account automatically unlocks afterward. A successful login before the threshold resets the consecutive-failure sequence.

---

## Business Rules

| Rule ID | Rule Type | Business Rule | Conditions / Inputs | Expected Outcome / Constraint | Source Traceability | Dependencies | Status |
|---|---|---|---|---|---|---|---|
| BR-001 | Core | A registered user may authenticate using an email address and password. | Registered user uses the login flow. | Email/password authentication is available. | Requirement 1 | N/A | Confirmed |
| BR-002 | Decision | Authentication succeeds only when submitted credentials are valid and the account is not locked. | Valid credentials; account unlocked. | Authentication succeeds. | Requirements 2–3 | BR-001 | Confirmed |
| BR-003 | Validation | An incorrect password causes the login attempt to fail. | Registered account; incorrect password. | Authentication fails. | Requirement 4 | BR-001 | Confirmed |
| BR-004 | Constraint | Failed login attempts caused by an incorrect password are tracked separately for each user account. | Incorrect-password failure occurs. | Only the corresponding account's failure sequence is affected. | Requirement 5; Notes | BR-003 | Confirmed |
| BR-005 | Decision | The lock threshold is five consecutive failed login attempts caused by an incorrect password. | Consecutive incorrect-password failures for one account. | Failures 1–4 remain below threshold; the fifth reaches the lock threshold. | Requirement 6 | BR-003, BR-004 | Confirmed |
| BR-006 | State | A successful login before reaching five consecutive failed attempts resets the failed-login counter. | Account unlocked; 1–4 consecutive failures; valid credentials submitted. | Authentication succeeds and the current failed-login sequence is reset. | Requirement 7; AC-05 | BR-002, BR-005 | Confirmed |
| BR-007 | State | The account becomes temporarily locked on the fifth consecutive failed login attempt. | Current consecutive failed count = 4; next attempt uses an incorrect password. | Login fails, count reaches 5, account becomes temporarily locked. | Requirement 8; AC-02 | BR-005 | Confirmed |
| BR-008 | Constraint | The temporary account lock duration is 30 minutes. | Account is temporarily locked. | Lock duration is 30 minutes. | Requirement 9 | BR-007 | Confirmed |
| BR-009 | Permission | Authentication is prohibited while the account is locked, even when the submitted password is correct. | Account locked; login attempted. | Authentication is rejected. | Requirement 10; AC-03 | BR-007 | Confirmed |
| BR-010 | Core | A login attempt while the account is locked displays `Your account has been temporarily locked. Please try again later.` | Account locked; login attempted. | Authentication is rejected and the defined lock message is displayed. | Requirement 11; AC-03 | BR-009 | Confirmed |
| BR-011 | State | The account is automatically unlocked when the 30-minute lock period expires. | Account locked; 30-minute lock period expires. | Account transitions to unlocked automatically. | Requirement 12; AC-04 | BR-008 | Confirmed |
| BR-012 | Permission | The user may attempt to log in again after the account is automatically unlocked. | Automatic unlock completed. | Login is available again. | Requirement 13; AC-04 | BR-011 | Confirmed |
| BR-013 | State | Failed-login tracking starts again after the account has been unlocked. | Automatic unlock completed; subsequent login activity occurs. | A new failed-login tracking sequence begins. | Requirement 14 | BR-011 | Confirmed |
| BR-014 | Constraint | No manual action is required to unlock the account after the lock period expires. | Defined temporary lock expires. | Unlock occurs automatically. | Notes | BR-011 | Confirmed |
| DR-001 | Derivation | Failed attempts one through four do not lock the account when no successful login interrupts the sequence. | Consecutive failed count = 1–4. | Account remains unlocked. | BR-005, BR-007; AC-01 | BR-005, BR-007 | Confirmed |
| DR-002 | Derivation | A successful login after one to four consecutive failures breaks the current consecutive-failure sequence. | 1–4 failures followed by successful login. | Prior failure sequence no longer contributes to the next threshold. | BR-006 | BR-006 | Confirmed |
| DR-003 | Derivation | A failed attempt after a successful-login reset belongs to a new consecutive-failure sequence. | Successful-login reset occurred; a later incorrect password is submitted. | New sequence starts. | BR-006 | DR-002 | Confirmed |
| DR-004 | Derivation | Previous failed attempts do not contribute to the next lock threshold after tracking starts again following automatic unlock. | Automatic unlock completed. | New post-unlock failures form a new sequence. | BR-013 | BR-011, BR-013 | Confirmed |
| DR-005 | Derivation | Providing a correct password does not bypass an active account lock. | Account locked; correct password submitted. | Authentication remains rejected. | BR-009 | BR-009 | Confirmed |

---

## Assumptions

No project-specific behavior beyond the supplied requirement is assumed. Derived rules above are logical consequences of confirmed rules and remain traceable to them.

---

## Open Questions

| Question ID | Area | Clarification Question | Related Undefined Behavior |
|---|---|---|---|
| CQ-001 | Lock Timer | Does the 30-minute lock period begin immediately when the fifth consecutive failed login attempt is recorded? | Exact timer-start event is not explicitly defined. |
| CQ-002 | Locked Attempts | Should login attempts made while the account is locked affect the failed-login counter? | Counter behavior during lock is undefined. |
| CQ-003 | Lock Extension | Does a login attempt during the locked period restart or extend the 30-minute duration? | Timer restart/extension behavior is undefined. |
| CQ-004 | Account Tracking | Should failed attempts across browsers, devices, and sessions contribute to the same account-level counter? | Cross-device/session behavior is not explicit. |
| CQ-005 | Unknown Account | How should login attempts using an unregistered email address be handled? | Unknown-account behavior is undefined. |
| CQ-006 | Unlock Counter | Should the failed-login counter explicitly reset to zero when the account is automatically unlocked? | Requirement states tracking starts again but does not state the numeric value. |
| CQ-007 | Concurrency | How should simultaneous failed attempts be counted near the five-attempt threshold? | Concurrent counter/locking semantics are undefined. |

---

## Rule Coverage Summary

The confirmed rule inventory covers authentication, per-account failed-login tracking, the five-attempt threshold, successful-login reset, temporary lock, locked-state rejection/message, 30-minute duration, automatic unlock, and post-unlock tracking. Timer internals, locked-attempt effects, cross-device behavior, unknown accounts, concurrency, and exact post-unlock counter value remain clarification-dependent rather than being promoted to confirmed rules.
