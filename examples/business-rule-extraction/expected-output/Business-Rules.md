# Business Rules — Account Lock After Failed Login Attempts

## 1. Business Rule Summary

The feature defines account-level protection against repeated failed login attempts.

The core rule chain is:

```text
Incorrect Password
        ↓
Increment Consecutive Failed-Login Count
        ↓
Failed Count < 5
        │
        └── Account Remains Unlocked

Failed Count = 5
        │
        └── Account Becomes Locked
                    ↓
               30 Minutes
                    ↓
             Automatic Unlock
                    ↓
        Failed-Login Tracking Starts Again
```

A successful login before the lock threshold is reached breaks the consecutive failure sequence by resetting the failed-login counter.

---

## 2. Business Rule Catalog

| Rule ID | Category | Business Rule | Type | Source |
|---|---|---|---|---|
| BR-001 | Authentication | A registered user may authenticate using an email address and password. | Explicit | Requirement 1 |
| BR-002 | Authentication | Authentication succeeds only when the submitted credentials are valid and the account is not locked. | Explicit | Requirements 2–3 |
| BR-003 | Authentication | An incorrect password causes the login attempt to fail. | Explicit | Requirement 4 |
| BR-004 | Failed Login Tracking | Failed login attempts caused by an incorrect password are tracked separately for each user account. | Explicit | Requirement 5; Notes |
| BR-005 | Failed Login Tracking | The lock threshold is five consecutive failed login attempts caused by an incorrect password. | Explicit | Requirement 6 |
| BR-006 | Failed Login Tracking | A successful login before reaching five consecutive failed attempts resets the failed-login counter. | Explicit | Requirement 7; AC-05 |
| BR-007 | Account Lock | The account becomes temporarily locked on the fifth consecutive failed login attempt. | Explicit | Requirement 8; AC-02 |
| BR-008 | Account Lock | The temporary account lock duration is 30 minutes. | Explicit | Requirement 9 |
| BR-009 | Account Lock | Authentication is prohibited while the account is locked, even when the submitted password is correct. | Explicit | Requirement 10; AC-03 |
| BR-010 | Account Lock | A login attempt while the account is locked displays `Your account has been temporarily locked. Please try again later.` | Explicit | Requirement 11; AC-03 |
| BR-011 | Account Unlock | The account is automatically unlocked when the 30-minute lock period expires. | Explicit | Requirement 12; AC-04 |
| BR-012 | Account Unlock | The user may attempt to log in again after the account is automatically unlocked. | Explicit | Requirement 13; AC-04 |
| BR-013 | Failed Login Tracking | Failed-login tracking starts again after the account has been unlocked. | Explicit | Requirement 14 |
| BR-014 | Account Unlock | No manual action is required to unlock the account after the lock period expires. | Explicit | Notes |

---

## 3. Derived Rules

The following rules are logical consequences of explicit requirement statements. They do not introduce additional project-specific behavior.

| Rule ID | Derived Business Rule | Derived From |
|---|---|---|
| DR-001 | Failed attempts one through four do not lock the account when no successful login has interrupted the sequence. | BR-005, BR-007, AC-01 |
| DR-002 | A successful login after one to four consecutive failed attempts breaks the current consecutive-failure sequence. | BR-006 |
| DR-003 | A failed attempt after a successful-login reset belongs to a new consecutive-failure sequence. | BR-006 |
| DR-004 | Previous failed attempts do not contribute to the next lock threshold after failed-login tracking starts again following automatic unlock. | BR-013 |
| DR-005 | Providing a correct password does not bypass an active account lock. | BR-009 |

Derived rules must remain traceable to explicit rules and must not be treated as independently supplied requirements.

---

## 4. Rule Conditions and Outcomes

### BR-005 / BR-007 — Account Lock Threshold

**Condition**

```text
Account is unlocked
AND
Current consecutive failed-login count = 4
AND
Next login attempt uses an incorrect password
```

**Outcome**

```text
Login fails
AND
Failed-login count reaches 5
AND
Account becomes temporarily locked
```

---

### BR-006 — Successful Login Counter Reset

**Condition**

```text
Account is unlocked
AND
Consecutive failed-login count is between 1 and 4
AND
Submitted credentials are valid
```

**Outcome**

```text
Authentication succeeds
AND
Failed-login counter is reset
```

---

### BR-009 / BR-010 — Authentication During Lock

**Condition**

```text
Account is temporarily locked
AND
User attempts to log in
```

**Outcome**

```text
Authentication is rejected
AND
Lock message is displayed
```

The authentication rejection applies even when the submitted password is correct.

---

### BR-011 / BR-013 — Automatic Unlock

**Condition**

```text
Account is temporarily locked
AND
30-minute lock period expires
```

**Outcome**

```text
Account is automatically unlocked
AND
User may attempt to log in again
AND
Failed-login tracking starts again
```

---

## 5. Rule Boundaries

### Failed-Login Threshold

```text
0 failures → Unlocked
1 failure  → Unlocked
2 failures → Unlocked
3 failures → Unlocked
4 failures → Unlocked
5 failures → Locked
```

The fifth consecutive failure is the transition point between the unlocked and locked states.

### Lock Duration

```text
Lock Duration = 30 minutes
```

The requirement defines the duration but does not define the precise timer-start or expiration-boundary semantics.

### Successful Login Reset

The reset rule applies when:

```text
1–4 consecutive failures
        ↓
Successful Login
        ↓
Failed-Login Counter Reset
```

A successful login at five failures is not an applicable condition because the account is already locked when the fifth failure occurs.

---

## 6. Rule Relationships

The business rules are dependent on one another.

```text
BR-003
Incorrect Password
    │
    ▼
BR-004
Track Failure Per Account
    │
    ▼
BR-005
Evaluate Consecutive Failure Threshold
    │
    ├── Below 5 ──► Remain Unlocked
    │
    └── At 5
          │
          ▼
        BR-007
        Lock Account
          │
          ├──► BR-008 — 30-Minute Duration
          ├──► BR-009 — Block Authentication
          └──► BR-010 — Display Lock Message
                        │
                        ▼
                      BR-011
                  Automatic Unlock
                        │
                 ┌──────┴──────┐
                 ▼             ▼
              BR-012         BR-013
            Login Again   Tracking Restarts
```

`BR-006` provides an alternate transition before the threshold:

```text
Failures 1–4
     │
Successful Login
     │
     ▼
Reset Counter
```

---

## 7. Rule Gaps and Ambiguities

The following behaviors cannot be converted into confirmed business rules from the available requirement.

| Gap ID | Area | Undefined Behavior |
|---|---|---|
| BG-001 | Lock Timer | The exact event from which the 30-minute lock period begins is not explicitly defined. |
| BG-002 | Locked Attempts | It is not defined whether login attempts made during the locked state affect the failed-login counter. |
| BG-003 | Lock Extension | It is not defined whether attempts during the locked state restart or extend the lock duration. |
| BG-004 | Account Tracking | It is not explicitly stated whether attempts across different browsers, devices, or sessions contribute to the same account-level counter. |
| BG-005 | Unknown Account | Behavior for login attempts using an email address that does not correspond to a registered account is not defined. |
| BG-006 | Unlock Counter | The requirement says failed-login tracking starts again after unlock but does not explicitly state the counter value after unlock. |
| BG-007 | Concurrency | Behavior for simultaneous login attempts against the same account near the lock threshold is not defined. |

These gaps must not be converted into project-specific business rules without clarification.

---

## 8. Clarification Questions

| Question ID | Related Gap | Clarification Question |
|---|---|---|
| CQ-001 | BG-001 | Does the 30-minute lock period begin immediately when the fifth consecutive failed login attempt is recorded? |
| CQ-002 | BG-002 | Should login attempts made while the account is locked be ignored for failed-login counting, or should they affect the counter? |
| CQ-003 | BG-003 | Does a login attempt during the locked period restart or extend the 30-minute lock duration? |
| CQ-004 | BG-004 | Should failed attempts made across different browsers, devices, and sessions contribute to the same account-level failed-login counter? |
| CQ-005 | BG-005 | How should login attempts using an email address that does not belong to a registered account be handled? |
| CQ-006 | BG-006 | Should the failed-login counter explicitly reset to zero when the account is automatically unlocked? |
| CQ-007 | BG-007 | How should concurrent failed login attempts be counted when an account is close to the five-attempt threshold? |

---

## 9. Business Rule Extraction Summary

The requirement provides a clear core business-rule chain:

```text
Account-Level Failed Login Tracking
              ↓
5 Consecutive Incorrect Password Attempts
              ↓
Temporary Account Lock
              ↓
Authentication Blocked
              ↓
30-Minute Lock Period
              ↓
Automatic Unlock
              ↓
Failed-Login Tracking Starts Again
```

A successful login before reaching the threshold resets the consecutive failed-login counter.

The extracted rules are sufficient to define the primary account-lock lifecycle.

Several secondary behaviors remain undefined, particularly around timer semantics, login attempts during the locked state, cross-device tracking, unknown accounts, concurrency, and exact counter state after automatic unlock.

Those behaviors remain documented as rule gaps and clarification questions rather than being promoted to confirmed business rules.