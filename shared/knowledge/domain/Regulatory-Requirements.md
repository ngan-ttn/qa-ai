# Regulatory Requirements

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-13

## Overview

**Regulatory requirements** are obligations imposed by applicable laws, regulations, licenses, directives, authorities, or formal industry regimes that influence business behavior and software controls. Applicability depends on jurisdiction, organization, product, data, and activity.

## Purpose

Help QA and QA-AI recognize regulatory influence, trace requirements to authoritative sources, and validate implemented controls without making legal determinations.

## Core Concepts

### Applicability
A regulation applies only under defined scope such as jurisdiction, entity type, product, activity, or data category.

### Obligation
A required behavior, record, control, report, disclosure, approval, or restriction.

### Authority
The regulator, legislature, standard-setting body, contract, or governance source that establishes the requirement.

### Effective Date
Regulatory changes can apply prospectively, retrospectively, or through transition periods depending on authoritative interpretation.

### Control Mapping
Business or technical controls implement obligations; one obligation can map to several controls.

### Evidence
Logs, approvals, reports, records, configurations, and procedures may demonstrate compliance.

### Exception / Exemption
Some obligations have defined exemptions or alternate regimes; QA must not infer them.

### Change Management
Regulatory change can affect requirements, test scope, data, workflows, and historical behavior.

## How It Works

```text
Authoritative requirement
      ↓
Determine applicability with qualified owner
      ↓
Translate into business/control requirement
      ↓
Implement control
      ↓
Test observable behavior + evidence
      ↓
Maintain through regulatory change
```

QA validates the software behavior and evidence specified by approved requirements. Legal interpretation and applicability decisions remain with authorized legal/compliance stakeholders.

## When to Use

Use for regulated products, privacy, payments, healthcare, government services, financial reporting, retention, auditability, security governance, and formal licensing controls.

## When Not to Use

Do not use this article to decide whether a law applies, interpret ambiguous legal text, or define legal obligations. Do not assume a regulation named in another project applies here.

## Advantages

Regulatory awareness improves traceability, evidence quality, high-risk coverage, and change-impact analysis.

## Limitations

Requirements can be jurisdiction-specific, frequently updated, interpreted through guidance, and dependent on organizational facts unavailable to QA.

## Examples

### Effective-Date Change
A policy implementing a regulatory change takes effect on a defined date. QA tests behavior before, at, and after the approved effective boundary using the organization's interpreted requirement.

### Evidence
A regulated approval requires auditable actor, time, decision, and reason. QA verifies the approved evidence fields and immutability behavior rather than inventing what the regulation itself requires.

## Best Practices

- Use authoritative, current sources and approved internal interpretation.
- Record jurisdiction, scope, owner, version, and effective date.
- Trace obligation → requirement → control → test evidence.
- Separate legal interpretation from software verification.
- Include negative and bypass scenarios for critical controls.
- Test policy transitions and historical compatibility.
- Preserve evidence securely and avoid unnecessary sensitive data.
- Re-review impacted coverage when regulations or guidance change.

## Related Knowledge

- `Compliance.md`
- `Audit-Trail.md`
- `Data-Privacy.md`
- `Security-Compliance.md`
- `Data-Retention.md`
- `Government.md`

## References

- Applicable authoritative legal/regulatory sources.
- Approved organization compliance interpretation and control documentation.
