# P15 Full Executable Test Case Set — My Rewards 3.0

> Version: 1.0.0  
> Status: Completed  
> Last Updated: 2026-08-14

## 1. Scope

This file expands the executable scenarios from `P15-Real-Requirement-Pilot.md` into an operational test-case set. Cases whose expected behavior is unresolved in the FRS remain excluded and are listed under Clarification-Dependent Coverage.

Default status for all cases: `Not Run`.

## 2. Voucher Test Cases

| ID | Title | Preconditions | Steps | Expected Result | Priority | Traceability |
|---|---|---|---|---|---|---|
| TC-V-001 | Apply voucher country filter | User has available vouchers from Country A and Country B | Open Voucher → open country filter → select Country A → Apply | Only vouchers identified as Country A are listed | High | BR-V-001 / SC-V-002 |
| TC-V-002 | Preserve country filter on refresh | Country A filter is applied | Pull to refresh | Country A remains applied; list remains filtered to Country A | High | BR-V-002 / SC-V-003 |
| TC-V-003 | Preserve country filter across Flight tab | Country A filter is applied | Open Flight → return Voucher | Country A remains applied | High | BR-V-003 / SC-V-004 |
| TC-V-004 | Preserve country filter across Coupon tab | Country A filter is applied | Open Coupon → return Voucher | Country A remains applied | High | BR-V-003 / SC-V-004 |
| TC-V-005 | Voucher row displays country | Voucher list has vouchers with known country values | Open Voucher list | Each displayed voucher shows its country | Medium | BR-V-004 / SC-V-005 |
| TC-V-006 | Available list includes available redeemed vouchers | User has available redeemed vouchers | Open Voucher → Available | Available redeemed vouchers are displayed | High | BR-V-005 / SC-V-006 |
| TC-V-007 | Available list excludes Used/Expired vouchers | User has Available, Used and Expired redeemed vouchers | Open Voucher → Available | Used and Expired vouchers are not displayed in Available | High | BR-V-005 / SC-V-006 |
| TC-V-008 | Default voucher sort by nearest expiry | Available vouchers have distinct expiry dates | Open Voucher → Available without changing sort | Items are ordered by nearest expiration date | Medium | BR-V-006 / SC-V-007 |
| TC-V-009 | Voucher sort by Most recent | Available vouchers have distinct redemption timestamps | Select Most recent → Apply | Items are ordered by most recent redeemed | Medium | BR-V-006 / SC-V-007 |
| TC-V-010 | Past Rewards includes Used voucher | User has a Used voucher | Open Voucher → Past Rewards | Used voucher is displayed | High | BR-V-007 / SC-V-008 |
| TC-V-011 | Past Rewards includes Expired voucher | User has an Expired voucher | Open Voucher → Past Rewards | Expired voucher is displayed | High | BR-V-007 / SC-V-008 |
| TC-V-012 | Open voucher detail from list | User has a selectable voucher | Select voucher | Voucher detail screen opens | Medium | FRS Available/Past detail rule |
| TC-V-013 | Voucher empty state | Selected Voucher tab contains no item | Open that Voucher tab | Empty state and no-voucher message are displayed | Medium | SC-V-009 |
| TC-V-014 | Voucher empty-state Redeem now | Voucher empty state is displayed | Select Redeem now | Redemption screen opens | Medium | BR-V-008 / SC-V-009 |
| TC-V-015 | Pending provider response UI | Successful redemption exists; provider response is pending | Open voucher detail | Processing UI shows FRS-defined processing message including within-24h statement | High | BR-V-009 / SC-V-010 |
| TC-V-016 | Provider logo shown for configured provider | Test environment can configure/provider-map a voucher | Open voucher detail | Provider logo is shown at top for the configured provider; exact fallback mapping is not asserted | Medium | BR-V-010 / SC-V-011 |
| TC-V-017 | Voucher name placement | Redeemed voucher has a name | Open voucher detail | Voucher name is shown in second position as described; product text is removed | Medium | FRS voucher detail enhancement |
| TC-V-018 | Wogi HTTPS CTA visibility | Wogi voucher satisfies documented `prefix = https` condition | Open voucher detail | CTA is displayed | Medium | BR-V-011 / SC-V-012 |
| TC-V-019 | Wogi HTTPS CTA opens in-app browser | Same as TC-V-018 | Select CTA | In-app browser opens | Medium | BR-V-011 / SC-V-012 |
| TC-V-020 | Voucher brand display | Voucher has brand data | Open voucher detail | Brand is displayed | Low | FRS voucher detail brand rule |
| TC-V-021 | Voucher country/applicable-at display | Voucher has known country | Open voucher detail | Country/applicable-at information is displayed under Expiry date as stated | Medium | FRS voucher detail country rule |

## 3. Flight Test Cases

| ID | Title | Preconditions | Steps | Expected Result | Priority | Traceability |
|---|---|---|---|---|---|---|
| TC-F-001 | Flight defaults to Available | User has available redeemed flight | Open Flight tab | Available is selected by default and available redeemed flight is shown | High | BR-F-001 / SC-F-001 |
| TC-F-002 | Flight Available excludes expired item | User has Available and Expired redeemed flights | Open Flight → Available | Expired redeemed flight is not shown in Available | High | BR-F-001 / SC-F-001 |
| TC-F-003 | New flight redemption indicator displayed | User has a new redemption not yet viewed in Flight tab | Observe Flight tab | New-redemption indicator is displayed | Medium | BR-F-002 / SC-F-002 |
| TC-F-004 | Flight indicator clears on tab selection | Indicator is displayed | Select Flight tab | Indicator is removed | Medium | BR-F-002 / SC-F-002 |
| TC-F-005 | Past Flight contains expired redemption | User has expired redeemed flight | Open Flight → Past Rewards | Expired redeemed flight is displayed | High | BR-F-003 / SC-F-003 |
| TC-F-006 | Past Flight ticket disabled | Expired redeemed flight exists | Open Past Rewards and inspect ticket interaction/state | Ticket is disabled as specified by FRS; unspecified implementation details are not asserted | High | BR-F-003 / SC-F-003 |
| TC-F-007 | Default Flight sort by nearest date | Available flights have distinct flight dates | Open Available without changing sort | Flights ordered by nearest flight date | Medium | BR-F-004 / SC-F-004 |
| TC-F-008 | Flight sort by Most recent redeemed | Flights have distinct redemption timestamps | Select Most recent → Apply | Flights ordered by most recent redeemed | Medium | BR-F-004 / SC-F-004 |
| TC-F-009 | Flight detail is read-only except copy | Flight detail is available | Open detail and inspect controls | Detail information is view-only; copy icon remains actionable at reservation code | High | BR-F-005 / SC-F-005 |
| TC-F-010 | Copy reservation code | Reservation code is known, e.g. `ABC123` | Tap copy icon → inspect clipboard | Clipboard contains exactly `ABC123` | High | BR-F-006 / SC-F-006 |
| TC-F-011 | Expired flight QR blurred | Test data satisfies clarified expiry condition | Open expired flight detail | Status is Expired and QR reservation code is blurred | High | BR-F-007 / SC-F-007 |
| TC-F-012 | Departure date format | Booking has departure date | Open detail | Departure date displayed in `dd/mm/yyyy` | Medium | BR-F-008 / SC-F-008 |
| TC-F-013 | Return date shown when present | Round-trip booking has return date | Open detail | Return date is displayed in `dd/mm/yyyy` | Medium | BR-F-008 / SC-F-008 |
| TC-F-014 | No invented return date for one-way | One-way booking has no return date | Open detail | No return-date value is fabricated; UI follows available booking data | Medium | BR-F-008 / SC-F-008 |
| TC-F-015 | Fare-class icon displayed | Booking has fare-class data | Open detail | Fare-class icon is displayed | Medium | SC-F-009 |
| TC-F-016 | Deal tag displayed when present | Booking has a deal/promotion tag | Open detail | Deal tag is displayed | Low | SC-F-009 |
| TC-F-017 | Departure airport/time/date | Booking has known departure info | Open detail | Departure airport code, boarding time, and flight date are displayed | High | SC-F-009 / R-006 |
| TC-F-018 | Destination airport/time/date | Booking has known destination info | Open detail | Destination airport code, boarding time, and flight date are displayed | High | SC-F-009 / R-006 |
| TC-F-019 | Flight duration and flight/plane number | Booking has values | Open detail | Estimated flight time and flight number-plane number are displayed | Medium | SC-F-009 |
| TC-F-020 | Connecting-flight English label | Connecting flight; app language EN | Open detail | `Connecting flight` is displayed | Medium | BR-F-009 / SC-F-010 |
| TC-F-021 | Connecting-flight Vietnamese label | Connecting flight; app language VI | Open detail | `Bay nối chuyến` is displayed | Medium | BR-F-009 / SC-F-010 |
| TC-F-022 | Connecting-flight label color | Connecting flight has fare-class color | Open detail | Connecting-flight text color follows fare-class color | Medium | BR-F-009 / SC-F-010 |
| TC-F-023 | Passenger quantity — Adult only | Booking has adults only | Open detail | Total passenger quantity and Adult breakdown are shown in selected language | Medium | SC-F-011 |
| TC-F-024 | Passenger quantity — Adult/Child/Infant | Booking contains all three passenger types | Open detail | Total and Adult/Child/Infant quantities are displayed using EN/VI wording from FRS | Medium | SC-F-011 |
| TC-F-025 | Flight empty state | Flight tab has no available item | Open empty Flight tab | Empty state and no-flight-redemption message are displayed | Medium | SC-F-012 |

## 4. Coupon Test Cases

| ID | Title | Preconditions | Steps | Expected Result | Priority | Traceability |
|---|---|---|---|---|---|---|
| TC-C-001 | Coupon defaults to Available | Account has available coupon | Open Coupon tab | Available is selected by default and available coupon is shown | High | BR-C-001 / SC-C-001 |
| TC-C-002 | Available excludes non-available coupon | Account has available and used coupons | Open Coupon → Available | Used coupon is not displayed in Available | High | BR-C-001 / SC-C-001 |
| TC-C-003 | New promotion indicator displayed | New promotion exists and tab not yet viewed | Observe Coupon tab | Indicator is displayed | Medium | BR-C-002 / SC-C-002 |
| TC-C-004 | Coupon indicator clears on view | Indicator is displayed | Select Coupon tab | Indicator is removed | Medium | BR-C-002 / SC-C-002 |
| TC-C-005 | View details opens coupon detail | Available coupon exposes View details | Select View details | Coupon detail loads | Medium | BR-C-003 / SC-C-003 |
| TC-C-006 | Conditions opens coupon detail | Coupon exposes Conditions | Select Conditions | Coupon detail loads | Medium | BR-C-003 / SC-C-004 |
| TC-C-007 | Used coupon appears in Past Rewards | Account has Used coupon | Open Coupon → Past Rewards | Used coupon is displayed | High | BR-C-004 / SC-C-005 |
| TC-C-008 | Default Coupon sort by nearest expiry | Available coupons have distinct expiry dates | Open Coupon without changing sort | Coupons ordered by nearest expiration date | Medium | BR-C-005 / SC-C-006 |
| TC-C-009 | Coupon sort by Newest | Available coupons have distinct campaign/coupon timeframes | Select Newest → Apply | Coupons ordered by newest campaign/coupon timeframe | Medium | BR-C-005 / SC-C-006 |
| TC-C-010 | Coupon empty state | Selected Coupon tab has no available coupon | Open tab | Empty state and no-promotion message are displayed | Medium | SC-C-007 |

## 5. Clarification-Dependent Coverage — No Authoritative Expected Result Yet

| Item | Why blocked |
|---|---|
| Voucher initial/reset country value | FRS conflicts between `All` and `(Vietnam)` |
| Country-filter persistence after app/session lifecycle changes | Persistence boundary not defined |
| Provider-logo fallback/mapping | Export-restricted synced block hides details |
| Wogi non-HTTPS behavior | Not stated |
| Duplicate voucher country/applicable-at row | Exported FRS does not clarify whether duplicate is intentional |
| Exact Flight expiry boundary | Round-trip/segment timing semantics ambiguous |
| Exact disabled-ticket interactions | FRS only says `Disable ticket` |
| Flight empty-state CTA destination | Destination not stated |
| Promotion × Voucherify mapping | Rule referenced without mapping detail |
| Expired coupon treatment | Past Rewards explicitly states Used only despite Used/Expired tab label |
| Coupon detail content | Not specified |
| Coupon empty-state CTA/navigation | Not specified |

## 6. Test Data Notes

Use the Test Data Model in `P15-Real-Requirement-Pilot.md`. Environment-specific account IDs, coupon codes, reservation codes, provider identifiers, country catalogs, CMS values, Voucherify data, or backend setup mechanisms must be supplied by the project/test environment and are not invented here.

## 7. Quality Result

**PASS — executable cases remain within confirmed FRS behavior; unresolved behaviors remain excluded from authoritative assertions.**
