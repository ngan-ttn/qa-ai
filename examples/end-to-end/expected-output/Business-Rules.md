# Business Rules — Account Lock After Failed Login Attempts

## Rule Summary

This artifact structures the confirmed business rules derived from `Sample-Requirement.md` and `Requirement-Analysis.md`. Undefined behavior remains clarification-dependent and is not promoted to a business rule.

---

## Business Rules

| Rule ID | Rule Type | Business Rule | Conditions / Inputs | Expected Outcome / Constraint | Source Traceability | Dependencies | Status |
|---|---|---|---|---|---|---|---|
| BR-001 | Constraint / Tracking | Incorrect-password attempts are tracked separately for each registered account. | Registered account receives incorrect-password login attempt. | Failed attempt contributes only to that account's sequence. | R5 | N/A | Confirmed |
| BR-002 | Threshold / State | Five consecutive incorrect-password attempts temporarily lock the account. | Same account reaches five consecutive failures. | Attempts 1–4 remain below threshold; fifth causes locked state. | R6, R8, AC-01, AC-02 | BR-001, BR-003 | Confirmed |
| BR-003 | Reset / Sequence | A successful login before the fifth consecutive failure resets failed-login tracking. | Account unlocked with 1–4 failures; valid credentials submitted. | Authentication succeeds; current sequence resets; later failure starts a new sequence. | R7, AC-05 | BR-002 | Confirmed |
| BR-004 | Time Constraint | A temporarily locked account remains locked for 30 minutes. | Account is in temporary locked state. | Lock remains active for the defined period. | R9 | BR-002 | Confirmed |
| BR-005 | Access Control | Authentication is rejected while the account is locked, including when the correct password is provided. | Account locked; login attempted. | Authentication is rejected. | R10, AC-03 | BR-002, BR-004 | Confirmed |
| BR-006 | User Feedback | A login attempt while locked displays the defined temporary-lock message. | Account locked; login attempted. | `Your account has been temporarily locked. Please try again later.` is displayed. | R11, AC-03 | BR-005 | Confirmed |
| BR-007 | State Transition | The account automatically unlocks after the 30-minute lock period expires. | Account locked; defined period expires. | Account transitions to unlocked automatically. | R12, AC-04 | BR-004 | Confirmed |
| BR-008 | Access | After automatic unlock, the user can attempt authentication again. | BR-007 completed. | Normal login becomes available again. | R13, AC-04 | BR-007 | Confirmed |
| BR-009 | Reset / Tracking | Failed-login tracking starts again after automatic unlock. | BR-007 completed; subsequent failures occur. | A new post-unlock failure sequence is tracked. | R14 | BR-007 | Confirmed |

---

## Rule Dependencies

The primary rule chain is `BR-001 → BR-002 → BR-004/BR-005/BR-006 → BR-007 → BR-008/BR-009`, with `BR-003` resetting the sequence before threshold.

---

## Assumptions

No implementation storage, timer mechanism, cross-device aggregation, or concurrency rule is assumed.

---

## Open Questions

| Question ID | Area | Clarification Needed |
|---|---|---|
| CQ-001 | Lock Expiration Boundary | Exact behavior for a request occurring precisely at the 30-minute expiration instant. |
| CQ-002 | Locked Attempts | Whether attempts during lock modify failure count. |
| CQ-003 | Lock Extension | Whether attempts during lock restart/extend the timer. |
| CQ-004 | Cross-Session / Device | Whether account-level failure state is aggregated across sessions/devices. |
| CQ-005 | Concurrency | How simultaneous attempts near threshold are processed. |

---

## Rule Coverage Summary

The canonical rule table preserves all nine confirmed rules used by downstream risk, scenario, testcase, coverage, and regression artifacts while keeping undefined behavior explicitly outside the confirmed model.
