# Sample Bug Report — Account Not Locked After Multiple Failed Login Attempts

## Bug ID

BUG-LOGIN-001

---

## Title

Account is not locked after failed login attempts

---

## Module

Login

---

## Environment

QA

---

## Preconditions

- A registered user account exists.
- The account is not locked.

---

## Steps to Reproduce

1. Open the login page.
2. Enter a registered email address.
3. Enter an incorrect password.
4. Click Login several times.

---

## Actual Result

The login fails but the account is still not locked.

---

## Expected Result

The account should be locked after multiple failed login attempts.

---

## Severity

High

---

## Evidence

Screenshot attached.