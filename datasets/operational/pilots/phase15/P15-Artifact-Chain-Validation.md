# P15 Artifact Chain Validation

> Version: 1.0.0  
> Status: Completed  
> Last Updated: 2026-08-17

## 1. Validation Objective

Validate that the Phase 15 pilot artifact chain remains grounded in the supplied FRS, preserves uncertainty, and does not lose or mutate material behavior while moving from requirement understanding to executable test design.

Validated artifacts:

- `P15-Real-Requirement-Pilot.md`
- `P15-Full-Test-Case-Set.md`

## 2. Cross-Artifact Checks

| Check | Result | Finding |
|---|---|---|
| Requirement → Business Rules | PASS | Confirmed rules are traceable to stated FRS behavior; unresolved/default conflict is not normalized away. |
| Business Rules → Risk | PASS | Risks identify QA exposure without redefining product policy. |
| Business Rules/Risk → Scenarios | PASS | High-risk behaviors have scenario coverage; blocked areas are explicitly marked. |
| Scenarios → Test Cases | PASS | Executable cases exist only where expected behavior is sufficiently grounded. |
| Scenario/Test Case ID consistency | PASS | Material traceability references were reconciled against the full executable test-case set; stale representative-case numbering was corrected. |
| Scenarios → Test Data | PASS | Required data states support coverage without fabricated environment values. |
| Uncertainty propagation | PASS | Country default conflict, flight-expiry boundary, Coupon/Voucherify mapping, provider-logo hidden rule, and other gaps remain visible. |
| Specialized technical boundary | PASS | No endpoint, status code, schema, SQL, backend field, CMS internals, or partner callback was invented. |
| Scope retention | PASS | Voucher, Flight, and Coupon remain represented in downstream coverage. |

## 3. Material Traceability Review

### Voucher

`BR-V-001..011` map into Voucher scenarios and the full executable Voucher case set where behavior is confirmed.

Material chains include:

- country filter apply: `BR-V-001 → SC-V-002 → TC-V-001`;
- filter persistence on refresh: `BR-V-002 → SC-V-003 → TC-V-002`;
- cross-tab filter persistence: `BR-V-003 / R-010 → SC-V-004 → TC-V-003, TC-V-004`;
- pending fulfillment: `BR-V-009 / R-002 → SC-V-010 → TC-V-015`;
- Wogi HTTPS CTA: `BR-V-011 → SC-V-012 → TC-V-018, TC-V-019`.

The voucher default/reset conflict remains `BR-V-CONFLICT-001 / CQ-001` and has no authoritative executable expected result.

### Flight

`BR-F-001..009` map into Flight scenarios and the full executable Flight case set where behavior is confirmed.

Material chains include:

- default Available behavior: `BR-F-001 → SC-F-001 → TC-F-001, TC-F-002`;
- new-redemption indicator: `BR-F-002 / R-007 → SC-F-002 → TC-F-003, TC-F-004`;
- Past/disabled ticket: `BR-F-003 → SC-F-003 → TC-F-005, TC-F-006`;
- sorting: `BR-F-004 → SC-F-004 → TC-F-007, TC-F-008`;
- read-only detail: `BR-F-005 → SC-F-005 → TC-F-009`;
- reservation-code copy: `BR-F-006 / R-005 → SC-F-006 → TC-F-010`;
- flight expiry/QR blur: `BR-F-007 / R-004 → SC-F-007 → TC-F-011`, executable only after the qualifying expiry condition is clarified;
- date formatting: `BR-F-008 → SC-F-008 → TC-F-012, TC-F-013, TC-F-014`;
- connecting-flight localization/color: `BR-F-009 → SC-F-010 → TC-F-020, TC-F-021, TC-F-022`.

The earlier stale reference `R-005 → SC-F-006 → TC-F-003` was incorrect because `TC-F-003` is the new-flight-redemption indicator case. It is corrected to `R-005 → SC-F-006 → TC-F-010`.

### Coupon

`BR-C-001..005` map into Coupon scenarios and the full executable Coupon case set where behavior is confirmed.

Material chains include:

- default Available behavior: `BR-C-001 → SC-C-001 → TC-C-001, TC-C-002`;
- new-promotion indicator: `BR-C-002 / R-007 → SC-C-002 → TC-C-003, TC-C-004`;
- detail navigation: `BR-C-003 → SC-C-003, SC-C-004 → TC-C-005, TC-C-006`;
- Used Past Rewards: `BR-C-004 → SC-C-005 → TC-C-007`;
- sorting: `BR-C-005 → SC-C-006 → TC-C-008, TC-C-009`.

Promotion × Voucherify (`SC-C-008`) and expired-coupon treatment (`SC-C-009`) remain blocked rather than converted into assumed rules.

## 4. Coverage Findings

### Covered and Executable

- voucher country apply/persistence across refresh and tabs;
- voucher Available/Past/empty states;
- voucher pending state and Wogi HTTPS CTA;
- Flight Available/Past, sorting, indicator, copy, date formatting, route/passenger display, and localized connecting-flight display;
- Coupon Available, details/conditions navigation, Used Past Rewards, sorting, and empty state;
- core test-data states for all three reward families.

### Covered but Clarification-Dependent

- voucher initial/reset country default;
- exact persistence boundary after leaving/restarting app;
- exact flight expiry boundary for round trip/segments;
- provider-logo fallback/mapping;
- expired coupon treatment;
- Promotion × Voucherify mapping;
- unspecified empty-state CTA destinations outside Voucher.

### Intentionally Not Expanded

- Jira/Figma details not supplied as content;
- export-restricted synced blocks;
- API/database/CMS implementation specifics;
- partner fulfillment internals;
- removal timing marked outside current phase.

## 5. Consistency Findings

The source-level country-filter conflict is preserved rather than resolved:

- voucher country filter default = `All`;
- Reset returns to default `(Vietnam)`.

This is correctly represented as `BR-V-CONFLICT-001` / `CQ-001`. No test case asserts a single default value.

The full executable test-case set also keeps other unresolved behavior under Clarification-Dependent Coverage rather than assigning authoritative expected results.

A final ID reconciliation found and corrected one stale traceability reference in this validation document: reservation-code copy now points to `TC-F-010`, matching the full test-case set. No product behavior changed as part of this correction.

## 6. Quality Assessment

The chain is operationally coherent because:

- product behavior is separated from QA-derived risk/coverage;
- test cases do not silently fill requirement gaps;
- executable coverage spans all three functional groups;
- blocked areas remain visible for requirement clarification;
- test-data requirements are actionable without pretending environment setup is known;
- material BR/Risk → Scenario → Test Case references are aligned with the full executable test-case set.

## 7. 15.3 Quality Gate

**PASS**

No blocking cross-artifact contradiction, silent source mutation, invented project-specific technical contract, or known stale material traceability reference remains after final reconciliation.

This PASS is a framework/artifact consistency result. It does not replace the Human QC usability decision in 15.5.
