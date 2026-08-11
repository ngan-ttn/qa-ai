# Account Lockout After Failed Login Attempts

## Dataset Metadata

- Dataset ID: `REQ-AUTH-001`
- Complexity: `Simple`
- Domain: `Authentication`
- Primary Evaluation Focus: Requirement analysis, business-rule extraction, boundary identification, and basic test coverage

---

## Context

The application provides username-and-password authentication for registered users.

To reduce repeated password-guessing attempts, the system must temporarily lock an account after multiple consecutive failed login attempts.

---

## Requirement

As a registered user,

I want my account to be temporarily locked after repeated failed login attempts,

So that unauthorized users cannot continuously attempt to guess my password.

The system must track consecutive failed login attempts for each account.

When a user enters an incorrect password, the failed-attempt counter for that account increases by one.

After five consecutive failed login attempts, the account becomes locked for 15 minutes.

While the account is locked, login attempts must be rejected even when the correct password is entered.

After 15 minutes, the account is automatically unlocked and the failed-attempt counter is reset.

A successful login before the lock threshold is reached resets the failed-attempt counter to zero.

---

## Acceptance Criteria

1. An incorrect password increases the account's consecutive failed-login counter by one.
2. The account remains unlocked after the first four consecutive failed login attempts.
3. The fifth consecutive failed login attempt locks the account.
4. The lock duration is 15 minutes.
5. Login is rejected while the account is locked, including login with the correct password.
6. The account is automatically unlocked after the 15-minute lock duration expires.
7. Automatic unlock resets the failed-attempt counter to zero.
8. A successful login before the fifth consecutive failure resets the failed-attempt counter to zero.
9. After automatic unlock, a new sequence of failed login attempts starts from zero.

---

## Constraints / Notes

- Failed-attempt tracking is maintained per account.
- Only password-based login behavior is in scope for this dataset.
- Password reset, multi-factor authentication, CAPTCHA, notifications, administrative unlock, and device-specific behavior are outside the defined scope.

---

## Known Ambiguities

None intentionally introduced for this dataset.
