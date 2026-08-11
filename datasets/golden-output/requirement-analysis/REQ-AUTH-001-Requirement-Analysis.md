# Requirement Analysis — Account Lockout After Failed Login Attempts

## Golden Output Metadata

- Dataset ID: `REQ-AUTH-001`
- Source Requirement: `datasets/requirements/simple/REQ-AUTH-001.md`
- Artifact Type: `Requirement Analysis`
- Review Status: `Approved`
- Evaluation Purpose: Reference output for evaluating requirement analysis quality, requirement comprehension, boundary identification, state-transition identification, assumption control, and clarification handling

---

## Feature Summary

The feature protects registered user accounts from repeated password-guessing attempts by temporarily locking an account after five consecutive failed password-based login attempts.

Failed login attempts are tracked separately for each account.

The account remains unlocked after the first four consecutive failed attempts.

The fifth consecutive failed attempt locks the account for 15 minutes.

While the account is locked, all password-based login attempts for that account are rejected, including attempts using the correct password.

When the 15-minute lock period expires, the account is automatically unlocked and the failed-attempt counter is reset to zero.

A successful login before the lock threshold is reached also resets the failed-attempt counter to zero.

---

## Actors

### Registered User

The registered user attempts to authenticate using a username and password.

The user's login outcome affects the failed-attempt counter and account lock state.

---

## Preconditions

- The user has a registered account.
- Username-and-password authentication is available.
- The account has an independently maintained failed-attempt counter.
- The account can be in either an unlocked or temporarily locked state.

---

## User Flows

### Flow 1 — Successful Login Before Lock Threshold

1. The account is unlocked.
2. The user has fewer than five consecutive failed login attempts.
3. The user submits the correct password.
4. Authentication succeeds.
5. The failed-attempt counter is reset to zero.
6. Any later failed login attempt starts a new consecutive sequence at one.

### Flow 2 — Failed Login Below Lock Threshold

1. The account is unlocked.
2. The user submits an incorrect password.
3. Authentication fails.
4. The failed-attempt counter increases by one.
5. The counter remains below five.
6. The account remains unlocked.

### Flow 3 — Fifth Consecutive Failed Login

1. The account is unlocked.
2. The failed-attempt counter is four.
3. The user submits an incorrect password.
4. Authentication fails.
5. The failed-attempt counter reaches five.
6. The account becomes locked.
7. The 15-minute lock duration starts when the fifth failed attempt is recorded.

### Flow 4 — Login Attempt While Account Is Locked

1. The account is within the 15-minute lock period.
2. The user submits a password-based login attempt.
3. The login attempt is rejected.
4. The attempt remains rejected regardless of whether the submitted password is correct or incorrect.
5. The account remains locked until the lock duration expires.

### Flow 5 — Automatic Unlock

1. The account is locked.
2. The 15-minute lock duration expires.
3. The account is automatically unlocked.
4. The failed-attempt counter is reset to zero.
5. The next failed login attempt starts a new consecutive sequence at one.

---

## Business Rules Identified

| Rule ID | Business Rule |
|---|---|
| BR-AUTH-001 | Failed login attempts are tracked separately for each account. |
| BR-AUTH-002 | An incorrect password increases the account's failed-attempt counter by one. |
| BR-AUTH-003 | An account remains unlocked while its consecutive failed-attempt counter is below five. |
| BR-AUTH-004 | The fifth consecutive failed login attempt locks the account. |
| BR-AUTH-005 | The lock duration is 15 minutes. |
| BR-AUTH-006 | The lock duration starts when the fifth consecutive failed attempt is recorded. |
| BR-AUTH-007 | All password-based login attempts are rejected while the account is locked. |
| BR-AUTH-008 | A correct password does not bypass an active account lock. |
| BR-AUTH-009 | The account is automatically unlocked when the 15-minute lock duration expires. |
| BR-AUTH-010 | Automatic unlock resets the failed-attempt counter to zero. |
| BR-AUTH-011 | A successful login before the account becomes locked resets the failed-attempt counter to zero. |
| BR-AUTH-012 | After the counter is reset, the next failed login attempt begins a new consecutive sequence at one. |

---

## State Analysis

### Account States

The requirement implies two relevant account states for this feature:

- `Unlocked`
- `Locked`

### State Transitions

| Current State | Condition / Event | Resulting State | Counter Behavior |
|---|---|---|---|
| Unlocked | Incorrect password and resulting counter is 1–4 | Unlocked | Increment by 1 |
| Unlocked | Successful login before lock | Unlocked | Reset to 0 |
| Unlocked | Fifth consecutive failed login | Locked | Reaches 5 |
| Locked | Password-based login attempt before lock expiry | Locked | Not specified |
| Locked | 15-minute lock duration expires | Unlocked | Reset to 0 |

---

## Boundary Analysis

### Failed-Attempt Threshold

The critical threshold is five consecutive failed attempts.

Important boundaries are:

- `0` failed attempts — initial/reset state.
- `1` failed attempt — beginning of a consecutive failed sequence.
- `4` failed attempts — highest value that still leaves the account unlocked.
- `5` failed attempts — lock-triggering threshold.

### Lock Duration

The lock duration is exactly 15 minutes starting from the fifth consecutive failed attempt.

Relevant timing boundaries include:

- Immediately after the fifth failed attempt.
- During the 15-minute lock period.
- Immediately before lock expiry.
- At the point the 15-minute duration expires.
- Immediately after expiry.

---

## Edge Cases Identified

1. Successful login after four consecutive failed attempts.
2. Incorrect login immediately after a successful login resets the sequence.
3. Correct password submitted while the account is locked.
4. Incorrect password submitted while the account is locked.
5. Login attempted immediately before the 15-minute lock expires.
6. Login attempted when the 15-minute lock duration expires.
7. First failed attempt immediately after automatic unlock.
8. Failed attempts occurring independently on different accounts.
9. Multiple failed sequences separated by successful logins.

---

## Assumptions

No additional business behavior should be assumed beyond the source requirement.

In particular, this analysis does not assume:

- How locked-login attempts affect the failed-attempt counter.
- Whether a locked-login attempt extends or restarts the 15-minute lock duration.
- Which user-facing error message is displayed for a locked account.
- Whether administrators can manually unlock an account.
- Whether another authentication method is affected by the lock.
- How simultaneous login attempts are processed.

These behaviors are not defined by the source requirement.

---

## Clarification Questions

The source dataset intentionally declares no known ambiguities.

However, deeper QA analysis identifies several implementation-relevant behaviors that are not explicitly defined and should not be inferred:

1. Do password-based login attempts made while the account is locked change the failed-attempt counter?

2. Does a password-based login attempt during the lock period restart or extend the 15-minute lock duration?

3. What response or error message should be returned when a user attempts to log in while the account is locked?

4. How should simultaneous failed login attempts against the same account be handled when the account is near the five-attempt threshold?

5. Is manual or administrative account unlock supported, and if so, what happens to the failed-attempt counter?

6. Are authentication methods other than username and password affected by the account lock?

These questions represent unspecified implementation or extended-scope behavior rather than contradictions in the supplied requirement.

---

## Scope

### In Scope

- Username-and-password login.
- Per-account consecutive failed-attempt tracking.
- Failed-attempt counter increment.
- Five-attempt lock threshold.
- Temporary 15-minute account lock.
- Rejection of password-based login during the lock.
- Automatic unlock after lock expiry.
- Counter reset after automatic unlock.
- Counter reset after successful login before lock.

### Out of Scope / Not Defined

- Administrative unlock.
- Password reset behavior.
- Multi-factor authentication.
- Alternative authentication methods.
- User notifications.
- Lockout error-message content.
- Persistence implementation.
- Timer implementation.
- Distributed/concurrent request handling.

---

## Traceability Summary

| Source Acceptance Criterion | Analysis Coverage |
|---|---|
| AC-01 — Incorrect password increments failed-attempt counter | BR-AUTH-002, Flow 2 |
| AC-02 — Account remains unlocked after attempts 1–4 | BR-AUTH-003, Flow 2, Boundary Analysis |
| AC-03 — Fifth consecutive failed attempt locks account | BR-AUTH-004, Flow 3, Boundary Analysis |
| AC-04 — Lock duration starts at fifth failed attempt | BR-AUTH-006, Flow 3, Lock Duration Analysis |
| AC-05 — All password-based attempts rejected while locked | BR-AUTH-007, BR-AUTH-008, Flow 4 |
| AC-06 — Automatic unlock after 15 minutes | BR-AUTH-005, BR-AUTH-009, Flow 5 |
| AC-07 — Automatic unlock resets counter | BR-AUTH-010, Flow 5 |
| AC-08 — Successful login before lock resets counter | BR-AUTH-011, Flow 1 |
| AC-09 — Next failed attempt after reset starts at one | BR-AUTH-012, Flow 1, Flow 5 |

All nine source acceptance criteria are represented in the analysis.

No source acceptance criterion is intentionally omitted.
