# P15 Real-Requirement Pilot — My Rewards 3.0

> Version: 1.0.0  
> Status: Completed  
> Last Updated: 2026-08-14

## 1. Source

Authoritative input: `FRS - Webview - My rewards 3.0`, version v1.0, dated 2026-06-15.

Unavailable exported synced-block content remains unresolved and is not reconstructed.

## 2. Structured Requirement Analysis

### Feature Scope

The FRS updates My Rewards webview UX for three reward families: Voucher, Flight, and Coupon. It defines list states, sorting/filtering, detail behavior, indicators, empty states, and selected display rules.

### Confirmed Functional Areas

**Voucher**
- country filter exists on voucher list;
- voucher-list default country filter is stated as `All`;
- applied country filter restricts the list to the selected country;
- pull-to-refresh does not reset the applied country filter;
- switching to Flight/Coupon does not reset the applied country filter;
- while remaining in app, retain the country filter;
- Reset and Apply actions exist;
- each voucher displays country;
- FRS also states Reset returns to default `(Vietnam)`;
- Available list contains available vouchers redeemed by the user;
- default voucher sort is nearest expiry date; alternate sort is most recent redeemed;
- Past Rewards contains Used or Expired vouchers;
- empty state displays no-voucher message and Redeem now CTA to Redemption;
- pending provider response after successful transaction shows processing copy indicating delivery within 24h;
- provider logo is shown from CMS configuration rather than hard-coded;
- voucher name is moved to second position and product text removed;
- Wogi voucher with `https` prefix shows CTA that opens in-app browser;
- detail screen shows brand and country/applicable-at information.

**Flight**
- Flight tab defaults to Available;
- Available list shows available redeemed flights;
- a new-redemption indicator is shown and removed when the user selects the tab;
- Past Rewards stores expired redeemed flights and disables the ticket;
- sort options: Most recent and Nearest flight date, with Nearest default;
- detail information is view-only except reservation-code copy;
- tapping copy copies reservation code to clipboard;
- when present time is overtime relative to flight departure/return, status becomes Expired and QR reservation code is blurred;
- departure and return dates are shown in `dd/mm/yyyy` where applicable;
- fare-class icon and deal tag are displayed when applicable;
- departure/destination airport, time, date, estimated flight time, flight number/plane number are displayed;
- connecting flight displays localized text, with text color based on fare-class color;
- passenger quantity is displayed in EN/VI forms;
- empty state displays no-flight-redemption message.

**Coupon**
- Coupon screen defaults to Available;
- Available shows available coupons;
- a Promotion × Voucherify display rule is referenced;
- new-promotion indicator is shown and removed when the user views the tab;
- View details and Conditions can open coupon detail;
- Past Rewards stores Used coupons;
- sort options: Expiry date default, Newest alternate;
- empty state displays no-promotion message;
- coupon detail loads when Conditions or View details is selected.

### Material Clarification Items

- `CQ-001`: Voucher country-filter default is stated as `All`, while Reset is stated to return to default `(Vietnam)`. Which value is the true default/reset state?
- `CQ-002`: Exact country-option list and country source are not provided.
- `CQ-003`: The phrase “If stay on app, keep the country filter” does not define whether app background/foreground, logout/login, webview close/reopen, or process restart resets it.
- `CQ-004`: Past voucher cleanup is explicitly “Not in this phase”; configured removal time is not available and must not be tested as Phase 15 behavior.
- `CQ-005`: CMS provider-logo mapping/fallback behavior is hidden by an export-restricted synced block.
- `CQ-006`: Wogi `https` prefix source/field and behavior for non-HTTPS values are not specified.
- `CQ-007`: Voucher detail contains duplicated country/applicable-at rows in the exported FRS; whether both represent distinct UI placements is unclear.
- `CQ-008`: Flight expiration wording “overtime with the flight time (departure/return)” is ambiguous for round trips: whether expiry is based on outbound departure, return departure, final arrival, or individual segment.
- `CQ-009`: Flight `disable ticket` behavior is not operationally defined beyond visual example.
- `CQ-010`: Indicator persistence scope is unclear after navigation away/reopen/session restart.
- `CQ-011`: Promotion × Voucherify display rule is referenced but its underlying mapping/content is not described in the exported document.
- `CQ-012`: Coupon Past Rewards explicitly mentions Used coupons; treatment of Expired coupons is not explicitly stated despite bilingual tab label `Used/Expired`.
- `CQ-013`: Coupon detail content is not specified beyond navigation/loading rule.
- `CQ-014`: Empty-state CTA behavior for Flight/Coupon is incomplete compared with Voucher; Flight copy names Redeem ticket now, but navigation destination is not stated; Coupon has no CTA behavior stated.

## 3. Structured Business Rule Model

| ID | Rule | Source State |
|---|---|---|
| BR-V-001 | Applied voucher country filter limits voucher list to selected country. | Confirmed |
| BR-V-002 | Pull-to-refresh does not reset applied voucher country filter. | Confirmed |
| BR-V-003 | Switching to Flight or Coupon does not reset applied voucher country filter. | Confirmed |
| BR-V-004 | Each voucher displays its country. | Confirmed |
| BR-V-005 | Voucher Available list only shows available vouchers redeemed by the user. | Confirmed |
| BR-V-006 | Voucher default sort is nearest expiry; alternate is most recent redeemed. | Confirmed |
| BR-V-007 | Voucher Past Rewards stores Used or Expired vouchers. | Confirmed |
| BR-V-008 | Voucher empty-state Redeem now CTA navigates to Redemption screen. | Confirmed |
| BR-V-009 | Pending fulfillment response after successful transaction displays processing message with 24h delivery statement. | Confirmed |
| BR-V-010 | Provider logo displayed from CMS configuration. | Confirmed at outcome level; mapping details unknown |
| BR-V-011 | Wogi voucher with HTTPS prefix exposes CTA and opens in-app browser after click. | Confirmed |
| BR-F-001 | Flight screen defaults to Available and shows only available redeemed flights. | Confirmed |
| BR-F-002 | New-flight-redemption indicator is removed when user selects Flight tab. | Confirmed |
| BR-F-003 | Past Flight list contains expired redeemed flights and ticket is disabled. | Confirmed |
| BR-F-004 | Flight default sort is nearest flight date; alternate is most recent redeemed. | Confirmed |
| BR-F-005 | Reward-ticket detail is read-only except reservation-code copy action. | Confirmed |
| BR-F-006 | Copy action copies reservation code to clipboard. | Confirmed |
| BR-F-007 | Overtime flight becomes Expired and reservation QR is blurred. | Confirmed outcome; exact time boundary ambiguous |
| BR-F-008 | Departure/return date format is `dd/mm/yyyy`. | Confirmed |
| BR-F-009 | Connecting flight shows localized Connecting flight text; text color follows fare-class color. | Confirmed |
| BR-C-001 | Coupon screen defaults to Available and only displays available coupons. | Confirmed |
| BR-C-002 | New-promotion indicator is removed when user views Coupon tab. | Confirmed |
| BR-C-003 | View details or Conditions loads coupon detail. | Confirmed |
| BR-C-004 | Past coupon list stores Used coupons. | Confirmed |
| BR-C-005 | Coupon default sort is nearest expiry; alternate is Newest campaign/coupon timeframe. | Confirmed |

**Conflict marker:** `BR-V-CONFLICT-001` — FRS says voucher filter default is `All` but Reset returns to default `(Vietnam)`. No executable expected result should choose one until clarified.

## 4. Structured Risk Analysis

| Risk ID | Area | Risk | Priority | Rationale |
|---|---|---|---|---|
| R-001 | Voucher Filter | Wrong persistence/reset behavior may show rewards for unintended country or confuse user state. | High | Multiple navigation/refresh persistence rules plus default conflict. |
| R-002 | Voucher Detail | Provider fulfillment pending state may expose unusable/empty voucher as ready. | High | Direct redemption usability impact. |
| R-003 | Voucher Detail | Wrong provider logo/config mapping can misrepresent fulfillment partner. | Medium | Provider-specific display depends on CMS config. |
| R-004 | Flight Expiry | Incorrect time/expiry logic can expose expired reservation QR or prematurely disable valid ticket. | High | Time/state rule with ambiguity. |
| R-005 | Flight Copy | Reservation code copy failure blocks practical ticket use. | High | Explicit interactive exception on otherwise read-only detail. |
| R-006 | Flight Data | Wrong route/date/passenger/fare information can mislead traveler. | High | Travel-critical information. |
| R-007 | Indicators | Indicator not cleared or cleared too early creates stale/new-state inconsistency. | Medium | State persists across navigation but scope is underspecified. |
| R-008 | Coupon Detail | Wrong Promotion × Voucherify mapping or detail navigation may expose wrong promotion. | High | Integration/display rule is referenced but underspecified. |
| R-009 | Empty State | Wrong empty-state CTA/message may strand user or navigate incorrectly. | Medium | Different behavior completeness across reward families. |
| R-010 | Cross-tab State | Switching tabs may unexpectedly reset voucher country filter. | High | Explicit persistence requirement. |

## 5. Structured Test Scenario Model

### Voucher

| Scenario ID | Scenario | Traceability | Status |
|---|---|---|---|
| SC-V-001 | Open voucher list and verify country-filter initial state. | BR-V-CONFLICT-001 | Clarification-dependent |
| SC-V-002 | Apply a country filter and verify only vouchers for that country are listed. | BR-V-001 | Executable |
| SC-V-003 | Pull to refresh after country filter and verify filter remains applied. | BR-V-002 | Executable |
| SC-V-004 | Switch Voucher → Flight/Coupon → Voucher and verify country filter remains applied. | BR-V-003, R-010 | Executable |
| SC-V-005 | Verify each voucher row displays country. | BR-V-004 | Executable |
| SC-V-006 | Verify Available list excludes non-available/non-redeemed vouchers. | BR-V-005 | Executable with suitable data |
| SC-V-007 | Verify voucher sort default and switch to Most recent. | BR-V-006 | Executable |
| SC-V-008 | Verify Used/Expired vouchers appear in Past Rewards. | BR-V-007 | Executable |
| SC-V-009 | Verify voucher empty state and Redeem now navigation. | BR-V-008 | Executable |
| SC-V-010 | Verify pending provider response displays processing UI/copy. | BR-V-009, R-002 | Executable with pending data |
| SC-V-011 | Verify provider logo follows configured provider. | BR-V-010, R-003 | Partially executable; mapping setup required |
| SC-V-012 | Verify Wogi HTTPS CTA opens in-app browser. | BR-V-011 | Executable with matching data |

### Flight

| Scenario ID | Scenario | Traceability | Status |
|---|---|---|---|
| SC-F-001 | Open Flight tab and verify Available list behavior. | BR-F-001 | Executable |
| SC-F-002 | Verify new redemption indicator appears and clears on selecting Flight tab. | BR-F-002, R-007 | Executable with new redemption state |
| SC-F-003 | Verify expired redeemed flights appear in Past and ticket is disabled. | BR-F-003 | Executable |
| SC-F-004 | Verify default Nearest sort and Most recent alternate sort. | BR-F-004 | Executable |
| SC-F-005 | Verify detail fields are read-only except reservation-code copy. | BR-F-005 | Executable |
| SC-F-006 | Verify reservation code copies exactly to clipboard. | BR-F-006, R-005 | Executable |
| SC-F-007 | Verify expired-state tag and QR blur after qualifying flight time. | BR-F-007, R-004 | Clarification-dependent for exact boundary/round-trip rule |
| SC-F-008 | Verify departure and optional return date formatting. | BR-F-008 | Executable |
| SC-F-009 | Verify fare-class/deal and route/flight information display from test data. | R-006 | Executable with suitable data |
| SC-F-010 | Verify connecting-flight EN/VI label and fare-class color. | BR-F-009 | Executable |
| SC-F-011 | Verify passenger quantity display for Adult/Child/Infant combinations. | R-006 | Executable |
| SC-F-012 | Verify Flight empty state. | FRS empty-state rule | Executable; CTA destination not asserted |

### Coupon

| Scenario ID | Scenario | Traceability | Status |
|---|---|---|---|
| SC-C-001 | Open Coupon tab and verify Available list only contains available coupons. | BR-C-001 | Executable |
| SC-C-002 | Verify new-promotion indicator appears and clears when Coupon tab is viewed. | BR-C-002, R-007 | Executable with new-promotion data |
| SC-C-003 | Verify View details loads coupon detail. | BR-C-003 | Executable |
| SC-C-004 | Verify Conditions loads coupon detail. | BR-C-003 | Executable |
| SC-C-005 | Verify Used coupons appear in Past Rewards. | BR-C-004 | Executable |
| SC-C-006 | Verify default Expiry-date sort and Newest alternate sort. | BR-C-005 | Executable |
| SC-C-007 | Verify Coupon empty state. | FRS empty-state rule | Executable |
| SC-C-008 | Verify Promotion × Voucherify display mapping. | R-008 | Blocked — mapping rule unavailable |
| SC-C-009 | Verify Expired coupon treatment in Past Rewards. | CQ-012 | Blocked — not explicitly specified |

## 6. Structured Test Case Model

The pilot intentionally does not turn every scenario into a case when expected behavior is unresolved. Representative executable cases below demonstrate operational usability and source discipline.

### TC-V-001 — Apply voucher country filter

**Traceability:** SC-V-002 / BR-V-001  
**Preconditions:** User has redeemed available vouchers belonging to at least two countries; country-filter options include the target country.  
**Steps:** Open My Rewards → Voucher; open country filter; select Country A; select Apply.  
**Expected:** Voucher list contains only vouchers identified as Country A.  
**Priority:** High

### TC-V-002 — Preserve voucher country filter on pull-to-refresh

**Traceability:** SC-V-003 / BR-V-002  
**Preconditions:** Country A filter is currently applied.  
**Steps:** Pull to refresh voucher list.  
**Expected:** Country A remains the active filter after refresh; displayed list remains constrained to Country A.  
**Priority:** High

### TC-V-003 — Preserve voucher country filter across reward tabs

**Traceability:** SC-V-004 / BR-V-003 / R-010  
**Preconditions:** Country A filter is applied on Voucher.  
**Steps:** Open Flight tab; open Coupon tab; return to Voucher.  
**Expected:** Country A remains applied on Voucher.  
**Priority:** High

### TC-V-004 — Voucher Available default sorting

**Traceability:** SC-V-007 / BR-V-006  
**Preconditions:** Available vouchers have different expiry dates.  
**Steps:** Open My Rewards → Voucher → Available without changing sort.  
**Expected:** Vouchers are ordered by nearest expiration date.  
**Priority:** Medium

### TC-V-005 — Voucher Past Rewards state

**Traceability:** SC-V-008 / BR-V-007  
**Preconditions:** Account contains at least one Used voucher and one Expired voucher.  
**Steps:** Open Voucher → Past Rewards.  
**Expected:** Used and Expired vouchers are present in Past Rewards.  
**Priority:** High

### TC-V-006 — Voucher empty state redemption CTA

**Traceability:** SC-V-009 / BR-V-008  
**Preconditions:** Selected voucher tab has no items.  
**Steps:** Open the empty voucher tab; select Redeem now.  
**Expected:** Empty state is shown with no-voucher copy and Redeem now CTA; selecting CTA opens Redemption screen.  
**Priority:** Medium

### TC-V-007 — Pending fulfillment response

**Traceability:** SC-V-010 / BR-V-009 / R-002  
**Preconditions:** Redemption transaction is successful and vendor/provider response remains pending.  
**Steps:** Open the voucher detail.  
**Expected:** Processing UI is shown with the FRS-defined message stating the voucher is being processed and will be sent within 24 hours; no unconfirmed ready-to-use behavior is asserted.  
**Priority:** High

### TC-V-008 — Wogi HTTPS voucher CTA

**Traceability:** SC-V-012 / BR-V-011  
**Preconditions:** Wogi voucher data satisfies the FRS condition `prefix = https`.  
**Steps:** Open reward detail; select the displayed CTA.  
**Expected:** CTA is available and opens an in-app browser.  
**Priority:** Medium

### TC-F-001 — Flight Available default state

**Traceability:** SC-F-001 / BR-F-001  
**Preconditions:** Account has at least one available redeemed flight and at least one non-available flight state.  
**Steps:** Open My Rewards → Flight.  
**Expected:** Available tab is selected by default and only available redeemed flights are shown.  
**Priority:** High

### TC-F-002 — Flight indicator lifecycle

**Traceability:** SC-F-002 / BR-F-002  
**Preconditions:** User has a new flight redemption and has not yet selected Flight tab after it became available.  
**Steps:** Observe Flight tab indicator; select Flight tab.  
**Expected:** Indicator is displayed before selection and removed when Flight tab is selected.  
**Priority:** Medium

### TC-F-003 — Reservation code copy

**Traceability:** SC-F-006 / BR-F-006 / R-005  
**Preconditions:** Reward ticket detail contains reservation code `ABC123`.  
**Steps:** Open ticket detail; tap copy icon beside reservation code; inspect clipboard.  
**Expected:** Clipboard contains exactly `ABC123`.  
**Priority:** High

### TC-F-004 — Flight default sorting

**Traceability:** SC-F-004 / BR-F-004  
**Preconditions:** Available redeemed flights have distinct flight dates.  
**Steps:** Open Flight Available list without changing sort.  
**Expected:** Flights are ordered by nearest flight date.  
**Priority:** Medium

### TC-F-005 — Connecting-flight label

**Traceability:** SC-F-010 / BR-F-009  
**Preconditions:** Redeemed flight is a connecting flight and fare-class color is available in display data.  
**Steps:** Open flight detail in EN; repeat in VI.  
**Expected:** EN shows `Connecting flight`; VI shows `Bay nối chuyến`; text uses fare-class color.  
**Priority:** Medium

### TC-C-001 — Coupon Available default state

**Traceability:** SC-C-001 / BR-C-001  
**Preconditions:** Account has available and non-available coupons.  
**Steps:** Open My Rewards → Coupon.  
**Expected:** Available is default and only available coupons are shown.  
**Priority:** High

### TC-C-002 — Coupon View details navigation

**Traceability:** SC-C-003 / BR-C-003  
**Preconditions:** Available coupon exposes View details action.  
**Steps:** Select View details.  
**Expected:** Coupon detail loads.  
**Priority:** Medium

### TC-C-003 — Coupon Conditions navigation

**Traceability:** SC-C-004 / BR-C-003  
**Preconditions:** Coupon exposes Conditions action.  
**Steps:** Select Conditions.  
**Expected:** Coupon detail loads.  
**Priority:** Medium

### TC-C-004 — Coupon default sort

**Traceability:** SC-C-006 / BR-C-005  
**Preconditions:** Available coupons have different expiration dates.  
**Steps:** Open Coupon Available without changing sort.  
**Expected:** Coupons are ordered by nearest expiration date.  
**Priority:** Medium

## 7. Explicitly Non-Executable / Clarification-Dependent Cases

The pilot intentionally does not assert:

- whether voucher initial/reset country is `All` or `Vietnam`;
- exact app/session persistence boundary for country filter;
- provider-logo fallback/mapping rules hidden by synced block;
- Wogi behavior for non-HTTPS prefix;
- exact round-trip flight expiry boundary;
- implementation meaning of disabled flight ticket beyond stated UI behavior;
- expired-coupon placement;
- Promotion × Voucherify field mapping;
- unspecified Flight/Coupon empty-state navigation;
- any API, status code, DB, CMS schema, partner callback, or backend field.

## 8. Test Data Model

| Data ID | Required State | Purpose |
|---|---|---|
| TD-V-001 | User with available vouchers in at least two countries | Country filtering |
| TD-V-002 | Available vouchers with distinct expiry and redemption timestamps | Voucher sorting |
| TD-V-003 | Used voucher + Expired voucher | Past Rewards |
| TD-V-004 | No vouchers for selected tab | Voucher empty state |
| TD-V-005 | Successful redemption with provider response pending | Pending detail state |
| TD-V-006 | Wogi voucher satisfying documented HTTPS-prefix condition | CTA/in-app browser |
| TD-F-001 | Available redeemed flights with distinct flight dates/redemption times | Flight list/sort |
| TD-F-002 | Newly redeemed flight with unseen Flight tab | Indicator |
| TD-F-003 | Expired redeemed flight | Past/disabled state |
| TD-F-004 | Ticket with known reservation code | Clipboard copy |
| TD-F-005 | One-way and round-trip bookings | Departure/return display |
| TD-F-006 | Connecting flight with fare-class color | Connecting-flight display |
| TD-F-007 | Passenger mixes: Adult only; Adult+Child; Adult+Child+Infant | Passenger display |
| TD-C-001 | Available coupons with distinct expiry/campaign times | Coupon list/sort |
| TD-C-002 | New unseen promotion | Coupon indicator |
| TD-C-003 | Used coupon | Coupon Past Rewards |
| TD-C-004 | No coupon for selected tab | Coupon empty state |

Environment-specific IDs, provider codes, country-option inventory, CMS values, Voucherify mappings, and API payloads are intentionally not fabricated.

## 9. Pilot Result

The real-requirement artifact chain was generated with confirmed behavior, clarification-dependent behavior, risks, scenarios, executable cases, and test-data requirements kept distinct.

**15.2 Result: PASS** for generation/source-grounding readiness. Human usability acceptance remains owned by 15.5.
