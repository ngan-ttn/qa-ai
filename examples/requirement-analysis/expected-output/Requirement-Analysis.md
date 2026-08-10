# Requirement Analysis — Account Lock After Failed Login Attempts

## 1. Feature Summary

The feature introduces temporary account locking after repeated consecutive failed login attempts caused by an incorrect password.

A registered user's account is locked after the fifth consecutive failed login attempt. The lock remains active for 30 minutes, during which authentication is not allowed even when the correct password is provided.

After the lock period expires, the account is automatically unlocked and failed-login tracking starts again.

A successful login before the lock threshold is reached resets the failed-login counter.

### Primary User

- Registered user.

### User Goal

- Sign in using valid credentials.
- Protect the account from repeated unauthorized login attempts.

### Primary System Behavior

```text
Login Attempt
     │
     ▼
Account Locked?
   ┌─┴─┐
  Yes  No
   │    │
   │    ▼
   │  Validate Credentials
   │       │
   │    ┌──┴──┐
   │  Valid Invalid Password
   │    │       │
   │    ▼       ▼
   │  Login   Increment Failed Counter
   │  Success       │
   │    │       Threshold Reached?
   │    │          ┌─┴─┐
   │    │         No  Yes
   │    │          │    │
   │    ▼          ▼    ▼
   │  Reset      Remain Lock Account
   │  Counter   Unlocked for 30 Minutes
   │
   ▼
Reject Authentication
```

---

## 2. User Flows

### UF-01 — Successful Login Without Previous Failed Attempts

1. The registered user enters an email address and password.
2. The system validates the submitted credentials.
3. The credentials are valid.
4. The account is not locked.
5. The system authenticates the user successfully.

### UF-02 — Failed Login Below Lock Threshold

1. The registered user enters an email address and an incorrect password.
2. The system validates the submitted credentials.
3. Authentication fails.
4. The system increments the failed-login counter for that account.
5. The failed-login counter remains below five consecutive attempts.
6. The account remains unlocked.

### UF-03 — Successful Login Before Lock Threshold

1. The user has at least one but fewer than five consecutive failed login attempts.
2. The user enters valid credentials.
3. The account is not locked.
4. Authentication succeeds.
5. The failed-login counter is reset.

### UF-04 — Account Reaches Lock Threshold

1. The account has four consecutive failed login attempts.
2. The user attempts to log in with an incorrect password.
3. Authentication fails.
4. The fifth consecutive failed login attempt is recorded.
5. The account becomes temporarily locked.
6. The lock period is 30 minutes.

### UF-05 — Login Attempt While Account Is Locked

1. The account is temporarily locked.
2. The user attempts to log in.
3. Authentication is not allowed.
4. The system displays:

   `Your account has been temporarily locked. Please try again later.`

This behavior applies even when the submitted password is correct.

### UF-06 — Automatic Account Unlock

1. The account is temporarily locked.
2. The 30-minute lock period expires.
3. The system automatically unlocks the account.
4. The user can attempt to log in again.
5. Failed-login tracking starts again.

---

## 3. Business Rules

| Rule ID | Business Rule | Source |
|---|---|---|
| BR-01 | Failed login attempts caused by an incorrect password are tracked separately for each user account. | Requirement 5 |
| BR-02 | Five consecutive failed login attempts caused by an incorrect password trigger temporary account locking. | Requirements 6, 8; AC-02 |
| BR-03 | The account becomes locked on the fifth consecutive failed login attempt. | Requirement 8; AC-02 |
| BR-04 | The account lock duration is 30 minutes. | Requirement 9; AC-04 |
| BR-05 | Authentication is not allowed while the account is locked, including when the correct password is entered. | Requirement 10; AC-03 |
| BR-06 | A login attempt while the account is locked displays the defined temporary-lock message. | Requirement 11; AC-03 |
| BR-07 | The account is automatically unlocked after the 30-minute lock period expires. | Requirement 12; AC-04 |
| BR-08 | After automatic unlock, the user can attempt to log in again. | Requirement 13; AC-04 |
| BR-09 | Failed-login tracking starts again after the account has been unlocked. | Requirement 14 |
| BR-10 | A successful login before five consecutive failed attempts resets the failed-login counter. | Requirement 7; AC-05 |
| BR-11 | Account unlocking after expiration of the lock period does not require manual action. | Notes |

---

## 4. Edge Cases

The following cases are relevant to the feature but are not fully defined by the provided requirement.

### EC-01 — Threshold Boundary

Behavior around the five-attempt threshold should distinguish:

```text
Failed Attempts 1–4
→ Account remains unlocked

Failed Attempt 5
→ Account becomes locked
```

The threshold itself is explicitly defined.

### EC-02 — Successful Login After Previous Failures

A successful login after one to four consecutive failed attempts resets the counter.

The next incorrect-password attempt should therefore begin a new consecutive-failure sequence.

### EC-03 — Login Exactly at Lock Expiration

The requirement does not define how a login attempt occurring exactly at the 30-minute expiration boundary is handled.

### EC-04 — Login Attempts During Lock Period

Authentication must be rejected while the account is locked.

However, the requirement does not define whether login attempts during this period affect the failed-login counter or lock duration.

### EC-05 — Multiple Devices or Sessions

Failed attempts are tracked separately for each account, but the requirement does not explicitly state whether attempts made from different browsers, devices, or sessions contribute to the same account-level counter.

### EC-06 — Unknown Email Address

The requirement defines failed-login tracking for registered user accounts but does not define behavior when the submitted email address does not correspond to an existing account.

### EC-07 — Unlock Followed by Incorrect Password

The requirement states that failed-login tracking starts again after unlock.

It does not explicitly describe the initial counter value, although starting a new tracking sequence implies that previous failed attempts no longer contribute to the next lock threshold.

---

## 5. Assumptions

No additional project-specific behavior is assumed beyond the provided requirement.

For analysis purposes, the following interpretations are derived directly from the requirement but should not be expanded into unsupported implementation rules:

| Assumption ID | Interpretation | Basis |
|---|---|---|
| AS-01 | Previous failed attempts no longer contribute to the lock threshold after a successful login resets the counter. | Requirement 7 |
| AS-02 | Previous failed attempts no longer contribute to the next lock threshold after the account is automatically unlocked and failed-login tracking starts again. | Requirement 14 |

No assumptions are made regarding:

- Notification or email behavior.
- Audit logging.
- Cross-device implementation.
- Lock-duration extension.
- Unknown-account security behavior.
- Failed-attempt persistence mechanism.
- Administrative unlocking.

---

## 6. Clarification Questions

### CQ-01 — Lock Start Time

From what exact event should the 30-minute lock period be calculated?

For example, should it start immediately when the fifth failed login attempt is recorded?

### CQ-02 — Attempts During Lock Period

Should login attempts made while the account is locked:

- Be ignored for failed-login counting?
- Increment any counter?
- Affect the lock expiration time?

### CQ-03 — Lock Duration Extension

Does a login attempt during the lock period restart or extend the 30-minute lock duration, or does the original expiration time remain unchanged?

### CQ-04 — Cross-Device and Cross-Session Tracking

Because failed attempts are account-specific, should failed attempts across different:

- Browsers,
- Devices,
- Sessions,

contribute to the same consecutive failed-login counter?

### CQ-05 — Unknown Email Address

How should a login attempt using an email address that does not belong to a registered account be handled?

Should such attempts participate in any failed-login tracking mechanism?

### CQ-06 — Counter State After Unlock

When failed-login tracking starts again after automatic unlock, should the failed-login counter explicitly reset to zero?

### CQ-07 — Successful Login Counter Reset

When a successful login resets the failed-login counter, is the reset expected to occur immediately after successful authentication?

### CQ-08 — Concurrent Login Attempts

How should simultaneous login attempts against the same account be handled when the account is close to the five-attempt threshold?

For example, if the account currently has four failed attempts and two incorrect-password requests are processed concurrently, the expected counter and locking behavior are not defined.

---

## 7. Analysis Summary

The requirement clearly defines the primary account-locking behavior:

```text
Incorrect Password
      ↓
Consecutive Failure Count
      ↓
Attempts 1–4 → Account Unlocked
      ↓
Attempt 5 → Account Locked
      ↓
30-Minute Lock
      ↓
Automatic Unlock
      ↓
Failed-Login Tracking Starts Again
```

It also clearly defines that:

- Failed attempts are account-specific.
- Successful authentication before the threshold resets the failed-login counter.
- Authentication is blocked while the account is locked.
- The defined lock message is displayed during the locked state.
- Manual unlocking is not required after the lock period expires.

The main unresolved areas concern lock-timer semantics, behavior during the locked period, cross-device/session tracking, unknown email addresses, counter-reset semantics, and concurrent login attempts.

These gaps should remain clarification items rather than being converted into additional business rules without further requirement confirmation.