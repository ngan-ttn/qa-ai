# Business Rules

## Run Context

- Source analysis: `examples/account-lockout/Requirement-Analysis.md`
- Authoritative requirement: `datasets/requirements/simple/REQ-AUTH-001.md`
- Stage: `skills/business-rule-extractor`
- Generation mode: Fresh / full generation

## Rule Summary

Eleven rules cover per-account counting, the below-five unlocked state, the fifth-failure lock, the 15-minute start, rejection during the lock, automatic unlock and reset, successful-login reset, the new sequence at one, and the password-only scope. No rule sets a counter change during an active lock.

## Business Rules

| Rule ID | Rule Type | Business Rule | Conditions / Inputs | Expected Outcome / Constraint | Source Traceability | Dependencies | Status |
|---|---|---|---|---|---|---|---|
| BR-001 | Constraint | Consecutive failed login attempts are tracked separately for each account. | A password-based login attempt is for one account. | That account's failed-attempt counter is independent of every other account. | REQ-AUTH-001 Requirement; Constraints | N/A | Confirmed |
| BR-002 | Decision | An incorrect password increases that account's failed-attempt counter by one. | A password-based login uses a password that is not correct for that account. | The attempt is a failed login. The counter for that account increases by one. | REQ-AUTH-001 Requirement; AC-1 | BR-001 | Confirmed |
| BR-003 | State | The account remains unlocked while its failed-attempt counter is below five. | The counter is below five. This includes one, two, three, or four consecutive failed login attempts. | The account is unlocked. | REQ-AUTH-001 Requirement; AC-2 | BR-002 | Confirmed |
| BR-004 | State | The fifth consecutive failed login attempt locks the account for 15 minutes. | Four consecutive failed attempts are already counted, and the next password-based attempt fails. | The account becomes locked for 15 minutes. | REQ-AUTH-001 Requirement; AC-3 | BR-002; BR-003 | Confirmed |
| BR-005 | Constraint | The 15-minute lock duration starts when the fifth consecutive failed login attempt is recorded. | The fifth consecutive failed login attempt has been recorded. | The duration is measured from that recording, not from an earlier failure. | REQ-AUTH-001 Requirement; AC-4 | BR-004 | Confirmed |
| BR-006 | Decision | While the account is locked, every password-based login attempt for that account is rejected, including the correct password. | The account is inside the 15-minute lock, and a password-based login is attempted for that account. | The attempt is rejected. The account remains locked for the rest of the duration. | REQ-AUTH-001 Requirement; AC-5 | BR-004; BR-005 | Confirmed |
| BR-007 | Postcondition | When the 15-minute lock duration expires, the account is automatically unlocked and its failed-attempt counter is reset to zero. | The duration that started at the recorded fifth consecutive failure has expired. | The account is unlocked. The failed-attempt counter is zero. | REQ-AUTH-001 Requirement; AC-6; AC-7 | BR-005 | Confirmed |
| BR-008 | Postcondition | A successful login before the account becomes locked resets the failed-attempt counter to zero. | The account is not locked, and a password-based login for that account succeeds. | The failed-attempt counter for that account is zero. | REQ-AUTH-001 Requirement; AC-8 | BR-003; BR-011 | Confirmed |
| BR-009 | State | After the failed-attempt counter is reset, the next failed login attempt starts a new consecutive sequence at one. | The counter was reset by BR-007 or BR-008, and the next password-based attempt is incorrect. | That attempt is failure one of a new sequence. That single attempt does not lock the account. | REQ-AUTH-001 Requirement; AC-9 | BR-003; BR-007; BR-008 | Confirmed |
| BR-010 | Constraint | Only username-and-password authentication is in scope. | Authentication behavior under this requirement. | Other authentication methods are outside this requirement. | REQ-AUTH-001 Constraints | N/A | Confirmed |
| BR-011 | Decision | Before the account is locked, the correct password produces a successful login. | The account is not locked, and the password submitted for that registered account is correct. | The login succeeds. | REQ-AUTH-001 Context; AC-8 | BR-003 | Confirmed |

## Rule Dependencies

```text
BR-010 limits scope to username-and-password authentication
BR-001 per-account counter
    → BR-002 incorrect password increments that account
        → BR-003 counter below five stays unlocked
            → BR-011 correct password succeeds before lock
                → BR-008 successful login resets counter to zero
        → BR-004 fifth consecutive failure locks for 15 minutes
            → BR-005 duration starts at that recorded fifth failure
                → BR-006 attempts during the lock are rejected
                → BR-007 expiry unlocks and resets counter to zero
BR-007 or BR-008
    → BR-009 next failure starts a new sequence at one
```

BR-002 is not given an exception for attempts during the lock. Whether those rejected attempts also increment the counter is OQ-01, not a confirmed exception.

## Assumptions

None. A-01 in the requirement analysis is not used as a rule.

## Open Questions

| ID | Question | Related rules | Status |
|---|---|---|---|
| OQ-01 | Does a rejected attempt during the lock increase the counter? | BR-002; BR-006 | Clarification-Dependent |
| OQ-02 | What signal exposes the counter value or lock state? | BR-002; BR-003; BR-004; BR-007; BR-008; BR-009 | Execution dependency |
| OQ-03 | What is the counter before any failure and before a stated reset? | BR-008 | Clarification-Dependent |
| OQ-04 | What is the result at the exact instant the 15 minutes elapse? | BR-005; BR-006; BR-007 | Clarification-Dependent |
| OQ-05 | What rejection text or code is returned? | BR-002; BR-006 | Clarification-Dependent |
| OQ-06 | How does an unregistered username behave? | BR-001 | Clarification-Dependent |
| OQ-07 | How are concurrent attempts for one account counted? | BR-002 | Clarification-Dependent |

## Rule Coverage Summary

- Confirmed rules: 11 (BR-001 through BR-011).
- Clarification-dependent rules: 0. Unresolved items stay in Open Questions.
- Source acceptance criteria AC-1 through AC-9 each appear on at least one confirmed rule.
- No rule states a storage mechanism, clock implementation, message, or admin action.
