# Government

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Government** software supports public administration, licensing, permits, benefits, taxation, records, case management, inspections, public services, and inter-agency processes. Rules are often policy- and jurisdiction-specific and may carry formal audit or transparency requirements.

## Purpose

Give QA reusable public-sector context while avoiding unsupported claims about law, policy, eligibility, retention, or statutory deadlines.

## Core Concepts

### Applicant / Citizen / Organization
The party requesting or receiving a government service. Identity and representation rules can differ by service.

### Case / Application
A managed request with evidence, status, decisions, and lifecycle.

### Eligibility
Qualification may depend on policy, documentation, jurisdiction, dates, and authority.

### Review / Approval
Government workflows commonly involve role-based review, segregation of duties, and formal decisions.

### Permit / License
An authorization can have scope, effective period, conditions, suspension, renewal, or revocation.

### Official Record
Some records require controlled history, provenance, and access.

### Public / Restricted Information
Disclosure rules can vary; data classification must come from applicable policy/law.

### Inter-Agency Dependency
One agency or system may rely on data or decisions from another.

## How It Works

A service typically progresses from submission → validation → review/verification → decision → issuance/payment/service → renewal, amendment, appeal, or closure. Actual lifecycle varies by program.

## When to Use

Use for permits, licensing, public benefits, case management, taxation, inspections, citizen portals, and government integrations.

## When Not to Use

Do not infer statutory response periods, disclosure requirements, eligibility criteria, or legal meaning without jurisdiction-specific authority.

## Advantages

Government context highlights auditability, role separation, effective dates, formal decision state, accessibility, and evidence risks.

## Limitations

Policy and legal requirements can vary by agency and change through legislation or administrative procedure.

## Examples

A permit is approved for a defined period and scope. An amendment may be allowed without reopening all approval fields; the exact exception requires policy evidence.

An application is submitted before a policy change but decided after it. QA must confirm which effective-date rule applies rather than choosing one assumption.

## Best Practices

- Trace rules to current authoritative policy or law.
- Define actor authority and segregation of duties.
- Test effective dates and policy version transitions.
- Preserve decision and audit history where required.
- Validate accessibility/localization requirements from approved scope.
- Cover appeal, amendment, renewal, suspension, and cancellation where applicable.
- Protect sensitive applicant data.

## Related Knowledge

- `Regulatory-Requirements.md`
- `Compliance.md`
- `Audit-Trail.md`
- `Data-Retention.md`
- `Eligibility-Rules.md`

## References

- Applicable agency policy, legislation, program rules, and approved service documentation.
