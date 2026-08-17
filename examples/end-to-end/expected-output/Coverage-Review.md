# Coverage Review — Account Lock After Failed Login Attempts

## Review Overview

This artifact reviews `Test-Cases.md` against the confirmed upstream requirement, business-rule, risk, and scenario baseline.

It reviews coverage only. It does not generate or modify test cases and does not convert unresolved behavior into executable expected results.

---

## Canonical Coverage Status Model

| Status | Meaning |
|---|---|
| Covered | Confirmed obligation is represented clearly enough that downstream execution does not need to reconstruct the primary oracle/objective. |
| Weakly Covered | Relevant coverage exists, but it is too broad, implicit, aggregated, or imprecise for reliable downstream use without remediation. |
| Gap | Confirmed, testable behavior has no adequate coverage. |
| Blocked | Authoritative coverage cannot yet be established because expected behavior, source content, dependency, or executable oracle is unresolved. |

`Duplicate`, `Inconsistent`, and `Not Applicable` may be used as secondary quality labels where needed, but they do not replace the four coverage-sufficiency statuses above.

---

## Overall Coverage Assessment

**Overall Status: PASS WITH BLOCKED OPEN ITEMS**

Reconciled baseline:

| Reviewed Object | Confirmed Count | Covered | Weakly Covered | Gap | Blocked/Open Dependencies |
|---|---:|---:|---:|---:|---:|
| Test Scenarios → Test Cases | 20 | 20 | 0 | 0 | 9 clarification-dependent candidates |
| Functional Requirements | 14 | 14 | 0 | 0 | — |
| Acceptance Criteria | 5 | 5 | 0 | 0 | — |
| Business Rules | 9 | 9 | 0 | 0 | — |
| Confirmed Functional Risks | 9 | 9 | 0 | 0 | — |

All 20 confirmed scenarios have executable testcase coverage. Nine clarification-dependent candidates remain blocked because the requirement does not define a reliable executable oracle for them.

Blocked items are **not counted as confirmed coverage gaps**.

---

## Scenario-to-Testcase Coverage

| Scenario | Test Case | Status | Assessment |
|---|---|---|---|
| TS-001 | TC-001 | Covered | Valid unlocked-account authentication is directly executable. |
| TS-002 | TC-002 | Covered | Incorrect-password rejection is directly executable. |
| TS-003 | TC-003 | Covered | Per-account failed-attempt tracking is represented. |
| TS-004 | TC-004 | Covered | First below-threshold failure is represented. |
| TS-005 | TC-005 | Covered | Four-failure boundary is directly represented. |
| TS-006 | TC-006 | Covered | Fifth-failure lock transition is directly represented. |
| TS-007 | TC-007 | Covered | Reset after one failure and successful login is represented. |
| TS-008 | TC-008 | Covered | Reset immediately below threshold is represented. |
| TS-009 | TC-009 | Covered | Interrupted failure sequences are represented. |
| TS-010 | TC-010 | Covered | Failure-state isolation between accounts is represented. |
| TS-011 | TC-011 | Covered | Authentication availability for an unaffected account is represented. |
| TS-012 | TC-012 | Covered | Correct credentials cannot bypass active lock. |
| TS-013 | TC-013 | Covered | Authentication remains unavailable during active lock without unsupported side-effect assertions. |
| TS-014 | TC-014 | Covered | Required locked-account message is directly verified. |
| TS-015 | TC-015 | Covered | Account remains locked before expiry. |
| TS-016 | TC-016 | Covered | Automatic unlock after the defined period is directly verified. |
| TS-017 | TC-017 | Covered | Valid authentication after automatic unlock is represented. |
| TS-018 | TC-018 | Covered | New failed-login sequence after unlock is represented. |
| TS-019 | TC-019 | Covered | Re-lock after five new failures is represented. |
| TS-020 | TC-020 | Covered | Complete confirmed temporary-lock lifecycle is represented. |

**Scenario coverage count: 20 / 20 confirmed scenarios Covered.**

---

## Requirement / Rule / Risk Coverage Summary

| Coverage Source | Evidence | Status | Assessment |
|---|---|---|---|
| R1–R14 | TC-001–TC-020 as traced in `Test-Cases.md` | Covered | All 14 confirmed functional requirements are represented. |
| AC-01–AC-05 | Threshold, locked-state, unlock, and reset cases | Covered | All 5 acceptance criteria are represented. |
| BR-001–BR-009 | Isolation, threshold, reset, lock duration/state, feedback, recovery cases | Covered | All 9 confirmed business rules are represented. |
| RISK-001–RISK-009 | High/Medium risk-focused cases | Covered | All 9 confirmed functional risks have meaningful testcase coverage. |

No confirmed requirement/rule/risk is classified `Weakly Covered` or `Gap` in this baseline.

---

## Boundary and State Coverage

| Confirmed Obligation | Evidence | Status | Assessment |
|---|---|---|---|
| Four consecutive failures remain below threshold | TC-005 | Covered | Direct lower-side boundary coverage. |
| Fifth consecutive failure locks account | TC-006 | Covered | Direct threshold transition coverage. |
| Active lock remains before expiry | TC-015 | Covered | Direct pre-expiry state coverage. |
| Account automatically unlocks after defined period | TC-016 | Covered | Direct recovery transition coverage. |
| Successful login resets prior sequence | TC-007–TC-009 | Covered | Multiple confirmed sequence partitions represented. |
| Failure state remains account-specific | TC-010, TC-011 | Covered | State isolation and user-visible effect represented. |

The exact behavior at the precise expiration instant is not asserted because the requirement does not define that boundary precisely; it remains Blocked below rather than being treated as a Gap.

---

## Blocked / Clarification-Dependent Dependencies

| Finding ID | Candidate | Status | Reason |
|---|---|---|---|
| COV-BLK-001 | CTS-001 — Counter behavior during active lock | Blocked | Requirement defines rejection but not counter mutation. |
| COV-BLK-002 | CTS-002 — Lock timer behavior during active lock | Blocked | Requirement does not define timer restart/extension. |
| COV-BLK-003 | CTS-003 — Exact expiration instant | Blocked | Exact boundary semantics are undefined. |
| COV-BLK-004 | CTS-004 — Same-account cross-browser tracking | Blocked | Aggregation scope is undefined. |
| COV-BLK-005 | CTS-005 — Same-account cross-device tracking | Blocked | Aggregation scope is undefined. |
| COV-BLK-006 | CTS-006 — Concurrent threshold attempts | Blocked | Concurrency behavior is undefined. |
| COV-BLK-007 | CTS-007 — Existing authenticated session after lock | Blocked | Existing-session behavior is undefined. |
| COV-BLK-008 | CTS-008 — Password-management interaction | Blocked | Reset/change interaction is undefined. |
| COV-BLK-009 | CTS-009 — Unknown/unregistered email behavior | Blocked | Unknown-account behavior is not supplied. |

**Blocked dependency count: 9.** These items are excluded from the confirmed executable coverage denominator.

---

## Duplicate / Over-Detail Review

- No confirmed testcase is classified as a cosmetic duplicate.
- Focused boundary/state cases and the end-to-end lifecycle case provide different coverage value.
- No testcase requires decomposition solely to satisfy the reviewed confirmed obligations.

---

## Readiness

**READY FOR DOWNSTREAM USE WITH BLOCKED OPEN ITEMS**

The confirmed testcase baseline is complete for the authoritative behavior currently defined. Blocked dependencies must remain unresolved until authoritative information supplies an executable oracle.

---

## Count Integrity Self-Check

- Confirmed scenarios: **20**; mapped executable testcases: **20**.
- Functional requirements: **14**; covered: **14**.
- Acceptance criteria: **5**; covered: **5**.
- Business rules: **9**; covered: **9**.
- Confirmed functional risks: **9**; covered: **9**.
- Blocked clarification-dependent candidates: **9**.

All stated counts reconcile with the IDs represented by the upstream/example artifact chain.
