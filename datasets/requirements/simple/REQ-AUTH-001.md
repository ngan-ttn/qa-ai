# Account Lockout After Failed Login Attempts

## Dataset Metadata

- Dataset ID: `REQ-AUTH-001`
- Complexity: `Simple`
- Domain: `Authentication`
- Primary Evaluation Focus: Requirement analysis, business-rule extraction, boundary identification, state-transition identification, and basic test coverage

---

## Context

The application provides username-and-password authentication for registered users.

To reduce repeated password-guessing attempts, the system temporarily locks an account after a defined number of consecutive failed login attempts.

---

## Requirement

As a registered user,

I want my account to be temporarily locked after repeated failed login attempts,

So that unauthorized users cannot continuously attempt to guess my password.

The system must track consecutive failed login attempts separately for each account.

An incorrect password increases the failed-attempt counter for that account by one.

The account remains unlocked while the failed-attempt counter is below five.

The fifth consecutive failed login attempt locks the account for 15 minutes.

The 15-minute lock duration starts when the fifth consecutive failed login attempt is recorded.

While the account is locked, all password-based login attempts for that account must be rejected, including attempts using the correct password.

When the 15-minute lock duration expires, the account is automatically unlocked and its failed-attempt counter is reset to zero.

A successful login before the account becomes locked resets the failed-attempt counter to zero.

After the counter is reset, subsequent failed login attempts are counted as a new consecutive sequence.

---

## Acceptance Criteria

1. Each incorrect password increases the failed-attempt counter for the corresponding account by one.
2. The account remains unlocked after one, two, three, or four consecutive failed login attempts.
3. The fifth consecutive failed login attempt locks the account.
4. The 15-minute lock duration begins when the fifth consecutive failed login attempt is recorded.
5. All password-based login attempts are rejected while the account is locked, including attempts using the correct password.
6. The account is automatically unlocked when the 15-minute lock duration expires.
7. Automatic unlock resets the failed-attempt counter to zero.
8. A successful login before the account becomes locked resets the failed-attempt counter to zero.
9. After the failed-attempt counter is reset, the next failed login attempt starts a new consecutive sequence at one.

---

## Constraints / Notes

- Failed-attempt tracking is maintained separately for each account.
- Only username-and-password authentication behavior is in scope.
- The technical mechanism used to track lock expiration or perform automatic unlock is not defined by this dataset.

---

## Known Ambiguities

None intentionally introduced for this dataset.
