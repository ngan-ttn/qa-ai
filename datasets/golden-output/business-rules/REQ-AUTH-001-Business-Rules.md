# Business Rules — Account Lockout After Failed Login Attempts

## Golden Output Metadata

- Dataset ID: `REQ-AUTH-001`
- Source Requirement: `datasets/requirements/simple/REQ-AUTH-001.md`
- Artifact Type: `Business Rules`
- Review Status: `Approved`
- Evaluation Purpose: Reference output for evaluating business-rule extraction accuracy, rule decomposition, boundary preservation, state-dependent behavior, traceability, and assumption control

---

## Business Rule Summary

The feature is governed by twelve confirmed business rules covering:

- Per-account failed-login tracking
- Failed-attempt counter increments
- Lock threshold behavior
- Lock duration
- Locked-state authentication
- Automatic unlock
- Counter reset behavior
- Consecutive-sequence restart behavior

These rules are derived directly from the source requirement and acceptance criteria.

No additional business behavior is introduced.

---

## Confirmed Business Rules

### BR-AUTH-001 — Failed Attempts Are Tracked Per Account

**Rule**

Consecutive failed login attempts must be tracked separately for each registered account.

**Business Meaning**

Failed attempts belonging to one account must not contribute to the failed-attempt sequence of another account.

**Source Basis**

- Requirement: Failed login attempts are tracked separately for each account.
- Constraint: Failed-attempt tracking is maintained separately for each account.
- AC-01

---

### BR-AUTH-002 — Incorrect Password Increments the Failed-Attempt Counter

**Rule**

Each incorrect password entered for an unlocked account increases that account's consecutive failed-attempt counter by one.

**Business Meaning**

The failed-attempt sequence advances one step for each incorrect-password authentication failure.

**Source Basis**

- Requirement: An incorrect password increases the failed-attempt counter for that account by one.
- AC-01

---

### BR-AUTH-003 — Account Remains Unlocked Below the Threshold

**Rule**

An account remains unlocked while its consecutive failed-attempt counter is below five.

**Business Meaning**

One, two, three, or four consecutive failed login attempts must not lock the account.

**Boundary**

- Counter = `1–4` → Account remains unlocked.
- Counter = `5` → BR-AUTH-004 applies.

**Source Basis**

- Requirement: The account remains unlocked while the failed-attempt counter is below five.
- AC-02

---

### BR-AUTH-004 — Fifth Consecutive Failure Locks the Account

**Rule**

The fifth consecutive failed login attempt locks the account.

**Business Meaning**

The transition from unlocked to locked occurs when the failed-attempt counter reaches five as part of a consecutive failed-login sequence.

**Boundary**

- Counter before attempt = `4`
- Next incorrect-password attempt → Counter reaches `5`
- Result → Account becomes locked

**Source Basis**

- Requirement: The fifth consecutive failed login attempt locks the account for 15 minutes.
- AC-03

---

### BR-AUTH-005 — Lock Duration Is Fifteen Minutes

**Rule**

A temporary account lock lasts for 15 minutes.

**Business Meaning**

Once the account enters the locked state, the temporary lock remains active until the defined lock duration expires.

**Source Basis**

- Requirement: The fifth consecutive failed login attempt locks the account for 15 minutes.
- AC-06

---

### BR-AUTH-006 — Lock Duration Starts at the Fifth Recorded Failure

**Rule**

The 15-minute lock duration begins when the fifth consecutive failed login attempt is recorded.

**Business Meaning**

The lock-period start point is tied to the recorded fifth consecutive authentication failure.

**Source Basis**

- Requirement: The 15-minute lock duration starts when the fifth consecutive failed login attempt is recorded.
- AC-04

---

### BR-AUTH-007 — Password-Based Login Is Blocked While Locked

**Rule**

All password-based login attempts for a locked account must be rejected while the lock remains active.

**Business Meaning**

A locked account is not eligible for password-based authentication during the active lock period.

**Source Basis**

- Requirement: While the account is locked, all password-based login attempts for that account must be rejected.
- AC-05

---

### BR-AUTH-008 — Correct Password Does Not Bypass the Lock

**Rule**

Submitting the correct password while the account is locked must not allow authentication.

**Business Meaning**

The account lock takes precedence over otherwise valid password credentials.

**Source Basis**

- Requirement: Locked login attempts are rejected, including attempts using the correct password.
- AC-05

---

### BR-AUTH-009 — Account Automatically Unlocks After Lock Expiry

**Rule**

The account is automatically unlocked when the 15-minute lock duration expires.

**Business Meaning**

The temporary lock ends automatically after the defined duration.

No user or administrative action is required within the scope of this requirement.

**Source Basis**

- Requirement: When the 15-minute lock duration expires, the account is automatically unlocked.
- AC-06

---

### BR-AUTH-010 — Automatic Unlock Resets the Counter

**Rule**

When the account is automatically unlocked, its failed-attempt counter is reset to zero.

**Business Meaning**

The failed-login sequence that triggered the lock does not carry over after automatic unlock.

**Source Basis**

- Requirement: Automatic unlock resets the failed-attempt counter to zero.
- AC-07

---

### BR-AUTH-011 — Successful Login Before Lock Resets the Counter

**Rule**

A successful login before the account becomes locked resets the failed-attempt counter to zero.

**Business Meaning**

A successful authentication interrupts the current consecutive failed-login sequence.

**Example**

`3 failed attempts → successful login → counter reset to 0`

The next failed login attempt belongs to a new sequence.

**Source Basis**

- Requirement: A successful login before the account becomes locked resets the failed-attempt counter to zero.
- AC-08

---

### BR-AUTH-012 — A Reset Starts a New Consecutive Sequence

**Rule**

After the failed-attempt counter is reset, the next failed login attempt starts a new consecutive sequence at one.

**Business Meaning**

Failures occurring before a reset must not be combined with failures occurring after the reset when evaluating the five-attempt threshold.

**Example**

`3 failures → successful login → 2 failures`

must be treated as:

`2 consecutive failures`

and not:

`5 consecutive failures`

**Source Basis**

- Requirement: After the counter is reset, subsequent failed login attempts are counted as a new consecutive sequence.
- AC-09

---

## Rule Relationships

### Failed-Login Sequence

Incorrect Password  
↓  
BR-AUTH-002  
Counter + 1  
↓  
Counter < 5  
↓  
BR-AUTH-003  
Remain Unlocked

At the threshold:

Counter = 4  
↓  
Incorrect Password  
↓  
Counter = 5  
↓  
BR-AUTH-004  
Account Locked

### Lock Lifecycle

5th Consecutive Failure  
↓  
BR-AUTH-004  
Account Locked  
↓  
BR-AUTH-006  
15-Minute Timer Starts  
↓  
BR-AUTH-007 / BR-AUTH-008  
Password Login Rejected  
↓  
15 Minutes Expire  
↓  
BR-AUTH-009  
Account Unlocked  
↓  
BR-AUTH-010  
Counter Reset to 0

### Successful-Login Reset

1–4 Consecutive Failures  
↓  
Correct Password  
↓  
Successful Authentication  
↓  
BR-AUTH-011  
Counter Reset to 0  
↓  
BR-AUTH-012  
Next Failure Starts New Sequence at 1

---

## Decision Rules

### Lock Threshold Decision

| Consecutive Failed Attempts After Current Attempt | Expected Account State |
|---:|---|
| 1 | Unlocked |
| 2 | Unlocked |
| 3 | Unlocked |
| 4 | Unlocked |
| 5 | Locked |

### Authentication Eligibility Decision

| Account State | Password Result | Authentication Outcome |
|---|---|---|
| Unlocked | Correct | Allowed |
| Unlocked | Incorrect | Rejected and failed-attempt counter increases |
| Locked | Correct | Rejected |
| Locked | Incorrect | Rejected |

The source requirement does not define whether a login attempt made while locked changes the failed-attempt counter.

### Counter Reset Decision

| Event | Counter Result |
|---|---|
| Incorrect password while unlocked | Increment by 1 |
| Successful login before lock | Reset to 0 |
| Automatic unlock after lock expiry | Reset to 0 |
| Login attempt while locked | Not specified |

---

## State Rules

The confirmed account states for this feature are:

- `Unlocked`
- `Locked`

Confirmed transitions are:

| From | Trigger | To |
|---|---|---|
| Unlocked | Failed-attempt counter remains below 5 | Unlocked |
| Unlocked | Successful login before lock | Unlocked |
| Unlocked | Fifth consecutive failed login | Locked |
| Locked | 15-minute lock duration expires | Unlocked |

No additional account-lock states are defined by the source requirement.

---

## Boundary Rules

### Counter Boundary

The critical business boundary is:

- `4` consecutive failures → Account remains unlocked.
- `5` consecutive failures → Account becomes locked.

### Time Boundary

The time-based business boundary is:

- Before the 15-minute lock duration expires → Account remains locked.
- When the 15-minute lock duration expires → Account automatically unlocks.

The requirement does not define any smaller timing tolerance or implementation-specific timer behavior.

---

## Rule Constraints

The confirmed scope constraints are:

1. The feature applies to username-and-password authentication.
2. Failed-attempt tracking is account-specific.
3. The lock is temporary.
4. The lock duration is 15 minutes.
5. The source does not prescribe the technical mechanism used to:
   - Store the failed-attempt counter.
   - Store lock state.
   - Track lock expiration.
   - Perform automatic unlock.

Implementation details must not be converted into business rules.

---

## Unspecified Behavior

The following behaviors are not defined by the source requirement and therefore must not be represented as confirmed business rules:

1. Whether login attempts during an active lock increment the failed-attempt counter.
2. Whether login attempts during an active lock restart or extend the lock duration.
3. The user-facing message shown for a locked account.
4. Manual or administrative unlock behavior.
5. Password-reset interaction with account lock.
6. Multi-factor or alternative authentication behavior.
7. Concurrent authentication behavior near the five-attempt threshold.
8. Persistence or distributed synchronization behavior.

These areas may generate clarification questions or risks in downstream artifacts but are not confirmed rules.

---

## Source Traceability

| Business Rule | Source Acceptance Criteria |
|---|---|
| BR-AUTH-001 | AC-01 |
| BR-AUTH-002 | AC-01 |
| BR-AUTH-003 | AC-02 |
| BR-AUTH-004 | AC-03 |
| BR-AUTH-005 | AC-06 |
| BR-AUTH-006 | AC-04 |
| BR-AUTH-007 | AC-05 |
| BR-AUTH-008 | AC-05 |
| BR-AUTH-009 | AC-06 |
| BR-AUTH-010 | AC-07 |
| BR-AUTH-011 | AC-08 |
| BR-AUTH-012 | AC-09 |

---

## Coverage Summary

The extracted rule set covers all confirmed source behavior:

- Per-account tracking
- Counter increment
- Below-threshold behavior
- Exact lock threshold
- Lock duration
- Lock start time
- Locked-state enforcement
- Correct-password lock enforcement
- Automatic unlock
- Counter reset
- Consecutive-sequence restart

All nine source acceptance criteria are represented.

No confirmed business rule is derived from implementation assumptions or unspecified behavior.
