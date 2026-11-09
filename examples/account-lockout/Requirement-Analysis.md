# Requirement Analysis

## Run Context

- Source: `datasets/requirements/simple/REQ-AUTH-001.md`
- Dataset ID: `REQ-AUTH-001`
- Workflow: `workflows/testcase-generation`
- Stage: `skills/requirement-analyzer`
- Generation mode: Fresh / full generation
- Risk analysis: not an input to this stage

## Requirement Summary

Registered users authenticate with a username and password. To limit password guessing, the system tracks consecutive failed login attempts separately for each account. The account stays unlocked while that counter is below five. The fifth consecutive failed attempt locks the account for 15 minutes, starting when that fifth attempt is recorded. While locked, every password-based login attempt is rejected, including the correct password. When the 15 minutes expire, the account unlocks automatically and the counter returns to zero. A successful login before lock also resets the counter to zero. The next failed attempt after a reset starts a new consecutive sequence at one.

The stated objective is to stop unauthorized users from continuously guessing the password.

## Functional Requirements

| ID | Statement | Source | Classification |
|---|---|---|---|
| FR-01 | The application provides username-and-password authentication for registered users. | Context | Confirmed |
| FR-02 | Consecutive failed login attempts are tracked separately for each account. | Requirement; Constraints | Confirmed |
| FR-03 | An incorrect password increases that account's failed-attempt counter by one, and the attempt is a failed login. | Requirement; AC-1 | Confirmed |
| FR-04 | The account remains unlocked while its failed-attempt counter is below five, including after one, two, three, or four consecutive failed attempts. | Requirement; AC-2 | Confirmed |
| FR-05 | The fifth consecutive failed login attempt locks the account for 15 minutes. | Requirement; AC-3 | Confirmed |
| FR-06 | The 15-minute lock duration starts when the fifth consecutive failed login attempt is recorded. | Requirement; AC-4 | Confirmed |
| FR-07 | While the account is locked, all password-based login attempts for that account are rejected, including the correct password. | Requirement; AC-5 | Confirmed |
| FR-08 | When the 15-minute lock duration expires, the account is automatically unlocked and its failed-attempt counter is reset to zero. | Requirement; AC-6; AC-7 | Confirmed |
| FR-09 | A successful login before the account becomes locked resets the failed-attempt counter to zero. | Requirement; AC-8 | Confirmed |
| FR-10 | After a reset, the next failed login attempt starts a new consecutive sequence at one. | Requirement; AC-9 | Confirmed |

## Non-Functional Requirements

The source does not state performance, availability, message text, audit, or usability requirements. The purpose of the lock is to reduce continuous password guessing. That purpose is not a separate measurable threshold.

## Assumptions

No assumption is promoted to confirmed behavior.

| ID | Statement | Why it is not confirmed |
|---|---|---|
| A-01 | A registered account that has not reached five consecutive failed attempts is not in the locked state defined by this requirement. | Used only to allow a successful login that the source already names. It does not assign an initial counter value. |

## Dependencies

The source does not name a module, service, API, database, screen, or clock. Those mechanisms stay unknown.

Execution of later tests depends on some way to tell whether a password attempt succeeded or was rejected, and whether the account is locked. The source does not define that signal.

## Business Constraints

- Failed-attempt tracking is per account.
- Only username-and-password authentication is in scope.
- The lock lasts 15 minutes from the recorded fifth consecutive failure.
- The technical mechanism that tracks lock expiration or performs automatic unlock is explicitly not defined.

## Validation Rules

These are candidates for business-rule extraction. This stage does not assign rule IDs.

- Incorrect password increases the account counter by one.
- Counter below five keeps the account unlocked.
- The fifth consecutive failure locks the account.
- Lock duration starts at the fifth recorded failure and lasts 15 minutes.
- Password attempts during the lock are rejected, including the correct password.
- Expiry unlocks the account and resets the counter to zero.
- Successful login before lock resets the counter to zero.
- The next failure after a reset starts at one.

## Edge Cases

| ID | Condition | Classification |
|---|---|---|
| EC-01 | One consecutive failure, and four consecutive failures, are the stated ends of the unlocked range. Two and three are inside the same below-five range. | Confirmed |
| EC-02 | The fifth consecutive failure is the lock boundary. | Confirmed |
| EC-03 | A time before 15 minutes have elapsed is still inside the lock. The source does not define a finer instant at the exact expiry boundary. | Confirmed behavior before expiry; exact-instant boundary unknown |
| EC-04 | A correct password during the lock is rejected. | Confirmed |
| EC-05 | A second registered account is independent of the first account's counter and lock. | Confirmed |

## Open Questions

| ID | Question | Effect |
|---|---|---|
| OQ-01 | Does a rejected password attempt while the account is locked also increase the failed-attempt counter, or leave it unchanged? | Do not assert a counter change during the lock. |
| OQ-02 | What signal shows the numeric failed-attempt counter or the lock state? | Keep assertions at the source's level. Do not invent a screen, API, or database field. |
| OQ-03 | What is the counter value of a registered account that has never failed and has not passed through a stated reset? | Do not treat an unseen initial value as zero. A named successful login before lock is the confirmed way to reach zero. |
| OQ-04 | Is an attempt at the exact instant the 15 minutes elapse locked or unlocked? | Assert only before the duration expires, and after it has expired. |
| OQ-05 | What text, code, or other rejection signal is shown? | Assert rejection, not message content. |
| OQ-06 | How does the system behave for a username that is not a registered account? | Out of the stated account behavior. Not an executable oracle. |
| OQ-07 | How are concurrent password attempts for the same account counted? | Not an executable oracle. |

## Risks

This stage does not score QA risk. `risk-analyzer` was not run. No risk IDs are created.

## Impact Analysis

The source describes password-based authentication and the lockout behavior of an account. It does not name other features, integrations, or components, so no further impact is confirmed.

## Testability Assessment

Login success, login rejection, remaining locked, and becoming unlocked are stated outcomes. Counter values are also stated, but the source does not say how a tester sees the counter. Duration can be judged from the moment the fifth failure is recorded, without defining the product's clock mechanism.

Behavior that depends on OQ-01, OQ-04, OQ-06, or OQ-07 has no authoritative oracle and must stay out of executable expected results.

## Analysis Summary

The requirement is specific enough for business-rule extraction and scenario design. Ten functional statements are confirmed from the source. Seven questions stay open. No project mechanism is added.
