# Requirement Analysis — Account Lock After Failed Login Attempts

## 1. Feature Summary

The feature protects a registered user account from repeated incorrect-password login attempts by applying a temporary account lock.

Confirmed behavior from the supplied requirement:

- Login uses a registered email address and password.
- Submitted credentials are validated when login is attempted.
- Valid credentials authenticate the user only when the account is not locked.
- Incorrect-password attempts are tracked separately for each account.
- Five consecutive incorrect-password attempts temporarily lock the account.
- A successful login before the fifth consecutive failure resets the failed-login counter.
- A locked account cannot authenticate, including with the correct password.
- A login attempt while locked displays the defined temporary-lock message.
- The lock remains active for 30 minutes.
- The account automatically unlocks after the 30-minute period expires.
- After automatic unlock, the user may attempt to log in again and failed-login tracking starts again.

The feature therefore combines authentication behavior, account-specific failed-login tracking, threshold-based state transition, time-based recovery, and user feedback.

---

## 2. Actors

### Registered User

The only explicitly defined actor is a registered user attempting to authenticate using an email address and password.

No administrator, support, security-operations, or other role-specific behavior is defined in the supplied requirement.

---

## 3. Functional Requirement Model

| ID | Area | Confirmed Requirement |
|---|---|---|
| R1 | Login | A registered user can attempt to log in using an email address and password. |
| R2 | Login | The system validates submitted credentials when login is attempted. |
| R3 | Login | Valid credentials successfully authenticate the user when the account is not locked. |
| R4 | Login | An incorrect password causes the login attempt to fail. |
| R5 | Failed Login Tracking | Incorrect-password failed login attempts are tracked separately for each user account. |
| R6 | Failed Login Tracking | Five consecutive incorrect-password attempts temporarily lock the account. |
| R7 | Failed Login Tracking | A successful login before the fifth consecutive failure resets the failed-login counter. |
| R8 | Account Lock | The account becomes locked after the fifth consecutive failed login attempt. |
| R9 | Account Lock | The account remains locked for 30 minutes. |
| R10 | Account Lock | While locked, the user cannot log in even with the correct password. |
| R11 | Account Lock | A login attempt while locked displays `Your account has been temporarily locked. Please try again later.` |
| R12 | Account Unlock | The account automatically unlocks after the 30-minute lock period expires. |
| R13 | Account Unlock | After unlock, the user can attempt to log in again. |
| R14 | Account Unlock | Failed-login tracking starts again after the account has been unlocked. |

---

## 4. Acceptance Criteria Model

| ID | Confirmed Behavior |
|---|---|
| AC-01 | When an unlocked account has fewer than four consecutive failed login attempts and another incorrect password is entered, the login fails, the failed-login counter increases by one, and the account remains unlocked. |
| AC-02 | When an unlocked account already has four consecutive failed login attempts and another incorrect password is entered, the login fails and the account is temporarily locked. |
| AC-03 | When the account is temporarily locked and the user attempts to log in, authentication is not allowed and the defined temporary-lock message is displayed. |
| AC-04 | When the 30-minute lock period expires, the account is automatically unlocked and the user can attempt to log in again. |
| AC-05 | When an unlocked account has at least one but fewer than five consecutive failed login attempts and the user logs in successfully, the failed-login counter is reset. |

---

## 5. User Flows

### Flow 1 — Successful Login While Unlocked

```text
Registered User
      ↓
Enter Email + Correct Password
      ↓
Submit Login
      ↓
Credentials Validated
      ↓
Account Not Locked
      ↓
Authentication Succeeds
```

### Flow 2 — Failed Login Below Threshold

```text
Registered User
      ↓
Enter Incorrect Password
      ↓
Login Fails
      ↓
Track Failure for That Account
      ↓
Consecutive Failures < 5
      ↓
Account Remains Unlocked
```

### Flow 3 — Lock at Fifth Consecutive Failure

```text
Account Has 4 Consecutive Failures
      ↓
Another Incorrect Password
      ↓
5th Consecutive Failure
      ↓
Login Fails
      ↓
Account Becomes Temporarily Locked
```

### Flow 4 — Successful Login Resets Failure Sequence

```text
Account Has 1–4 Consecutive Failures
      ↓
Correct Credentials
      ↓
Successful Login
      ↓
Failed-Login Counter Resets
```

### Flow 5 — Login Attempt During Active Lock

```text
Account Locked
      ↓
User Attempts Login
      ↓
Authentication Not Allowed
      ↓
Temporary-Lock Message Displayed
```

This flow applies even when the submitted password is correct because R10 explicitly prohibits login while the account is locked.

### Flow 6 — Automatic Unlock

```text
Account Locked
      ↓
30-Minute Lock Period Expires
      ↓
Account Automatically Unlocks
      ↓
User Can Attempt Login Again
      ↓
Failed-Login Tracking Starts Again
```

---

## 6. State Model

The confirmed account-lock state model is:

```text
UNLOCKED
    │
    │ 5 consecutive incorrect-password failures
    ▼
LOCKED
    │
    │ 30-minute lock period expires
    ▼
UNLOCKED
```

Additional confirmed behavior while `UNLOCKED`:

```text
1–4 Consecutive Failures
        ↓
Remain UNLOCKED
```

and:

```text
1–4 Consecutive Failures
        ↓
Successful Login
        ↓
Counter Reset
        ↓
Remain UNLOCKED
```

While `LOCKED`, authentication is not allowed.

---

## 7. Boundary Conditions

### Failed-Login Threshold

The confirmed threshold is five consecutive incorrect-password attempts.

Relevant boundary conditions are:

```text
4 consecutive failures
→ Account remains unlocked

5th consecutive failure
→ Account becomes locked
```

The requirement also confirms that a successful login at any point from one through four consecutive failures resets the counter.

### Lock Duration

The confirmed lock duration is 30 minutes.

The supplied requirement defines:

```text
During the 30-minute lock period
→ Account remains locked

After the 30-minute lock period expires
→ Account automatically unlocks
```

The exact system behavior at the precise expiration instant is not further defined.

---

## 8. Account Isolation

Failed-login attempts are explicitly tracked separately for each user account.

Therefore:

```text
Account A failed-login state
≠
Account B failed-login state
```

Failures associated with one account must not be combined with failures associated with another account when determining whether the five-consecutive-failure threshold has been reached.

The requirement does not define how account-specific tracking is implemented or synchronized across browsers, devices, sessions, services, or data stores.

---

## 9. User Feedback

The requirement defines one exact message for a login attempt while the account is locked:

```text
Your account has been temporarily locked. Please try again later.
```

The requirement does not define:

- The presentation component used to display the message.
- Message styling.
- Message placement.
- Whether remaining lock time is displayed.
- Any separate message for the fifth failed attempt beyond the locked-account behavior.

---

## 10. Derived Analysis

The following conclusions are directly derived from the confirmed requirement without introducing additional business behavior:

1. The lock threshold depends on a **consecutive** failure sequence, not lifetime failed-login count.
2. A successful login breaks the current failure sequence because the failed-login counter is reset.
3. The fifth consecutive incorrect-password attempt is both a failed authentication attempt and the trigger for transition into the locked state.
4. Account lock status overrides otherwise valid credentials while the lock is active.
5. Unlock is time-driven and automatic; no manual action is required according to the supplied notes.
6. Failed-login tracking after automatic unlock belongs to a new tracking sequence because tracking starts again after unlock.
7. Account-specific tracking requires isolation between different user accounts, but the technical storage or synchronization mechanism is unspecified.

These are analytical consequences of the supplied requirements and acceptance criteria; they are not additional source requirements.

---

## 11. Edge and Test-Relevant Conditions Supported by the Requirement

The supplied requirement supports analysis of the following test-relevant conditions:

- Valid login with an unlocked account.
- Incorrect-password login failure.
- First failed attempt.
- Immediately below the lock threshold.
- Exact lock threshold.
- Successful login after one or more failures but before threshold.
- Failure sequences separated by a successful login.
- Independent failed-login state for different accounts.
- Correct credentials while the account is locked.
- Login attempt during active lock.
- Account remaining locked before the lock period expires.
- Automatic unlock after the lock period expires.
- Login after automatic unlock.
- New failed-login tracking after automatic unlock.
- Repeated lock lifecycle after a new post-unlock failure sequence.

These conditions do not define behavior beyond what the requirement supports.

---

## 12. Missing or Ambiguous Information

The following behavior is not defined by the supplied requirement and must not be treated as confirmed:

| ID | Area | Missing / Ambiguous Information | Potential QA Impact |
|---|---|---|---|
| Q-001 | Active Lock | Whether login attempts during the active lock change the failed-login counter. | Expected counter behavior during locked-state attempts cannot be asserted. |
| Q-002 | Active Lock | Whether login attempts during the active lock affect or restart the 30-minute lock timer. | Timer mutation behavior cannot be asserted. |
| Q-003 | Lock Expiration | Exact expected behavior at the precise 30-minute expiration boundary. | Exact-time boundary assertion requires clarification or an authoritative timing contract. |
| Q-004 | Tracking Scope | Whether the same account's failed-login sequence is shared across browser sessions. | Cross-browser sequence testing cannot have a confirmed expected result. |
| Q-005 | Tracking Scope | Whether the same account's failed-login sequence is shared across devices. | Cross-device sequence testing cannot have a confirmed expected result. |
| Q-006 | Concurrency | Behavior when multiple failed login attempts reach the threshold concurrently. | Race-condition expectations are undefined. |
| Q-007 | Existing Session | Effect of account lock on a session that was authenticated before the lock occurred. | Existing-session behavior cannot be asserted. |
| Q-008 | Password Management | Interaction between temporary lock and password reset/change flows. | Recovery-flow interaction is undefined. |
| Q-009 | Unknown Account | Expected behavior when login is attempted using an unregistered email address. | Unknown-account authentication and messaging are outside the confirmed behavior. |

---

## 13. Assumptions

No additional project-specific behavior is assumed in this analysis.

Where the source requirement is incomplete, the information remains recorded as a clarification item rather than being converted into a requirement.

Test setup may require an account to begin in a logical state such as:

- Unlocked with zero consecutive failures.
- Unlocked with four consecutive failures.
- Locked with an active lock period.

These are test-state representations derived from confirmed feature states and do not imply a particular database schema, API, admin tool, or setup mechanism.

---

## 14. Clarification Questions

1. During the 30-minute lock period, do additional login attempts change the failed-login counter?
2. During the 30-minute lock period, do additional login attempts restart or extend the lock timer?
3. What is the expected behavior exactly at the 30-minute expiration instant?
4. Is failed-login tracking for the same account shared across browser sessions?
5. Is failed-login tracking for the same account shared across different devices?
6. What is the expected result when multiple incorrect-password attempts reach the lock threshold concurrently?
7. What happens to an already authenticated session if that same account becomes locked elsewhere?
8. How does temporary account lock interact with password reset or password change flows?
9. What behavior and user feedback are expected when an unregistered email address is submitted?

These questions are non-blocking for the confirmed baseline behavior but are required before reliable assertions can be created for the corresponding additional conditions.

---

## 15. Analysis Summary

The confirmed feature baseline is:

```text
Registered Account
      ↓
Authentication Attempt
      ↓
Incorrect Password
      ↓
Account-Specific Consecutive Failure Tracking
      ↓
5th Consecutive Failure
      ↓
Temporary Lock for 30 Minutes
      ↓
Authentication Blocked + Defined Message
      ↓
Automatic Unlock
      ↓
Authentication Available Again
      ↓
Failed-Login Tracking Starts Again
```

The supplied requirement is sufficient to define the core lock lifecycle, threshold behavior, successful-login reset behavior, account isolation, active-lock authentication prohibition, required locked-account message, and automatic recovery.

Nine areas remain clarification-dependent and should remain visible to downstream QA artifacts rather than being silently resolved through assumptions.