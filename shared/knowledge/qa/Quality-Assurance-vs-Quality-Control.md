# Quality Assurance vs Quality Control

> Version: 1.0.0  
> Status: Draft  
> Last Updated: 2026-08-14

## Overview

**Quality Assurance (QA)** and **Quality Control (QC)** are complementary approaches used to support software quality.

They share the same overall objective but focus on different aspects of quality:

- **Quality Assurance** focuses primarily on the processes used to prevent quality problems.
- **Quality Control** focuses primarily on evaluating products and deliverables to detect quality problems.

A simplified relationship is:

```text
Software Quality
        │
        ├── Quality Assurance
        │       └── Process-oriented
        │
        └── Quality Control
                └── Product-oriented
```

The distinction is conceptual rather than an absolute organizational boundary.

A person working in a QA role may perform both QA-oriented and QC-oriented activities depending on the organization and project.

---

## Purpose

The purpose of this article is to establish a clear distinction between Quality Assurance and Quality Control so that QA practitioners can reason correctly about:

- defect prevention;
- defect detection;
- process quality;
- product quality;
- testing responsibilities;
- quality improvement;
- quality ownership.

This distinction is particularly important because the terms **QA**, **QC**, and **testing** are sometimes used interchangeably in software organizations even though they represent different concepts.

Within QA-AI, this knowledge helps distinguish between:

```text
Process-oriented reasoning
        │
        └── How can quality problems be prevented?

Product-oriented reasoning
        │
        └── Does the actual product satisfy expectations?
```

The distinction should guide reasoning without assuming how a specific organization assigns responsibilities or job titles.

---

## Core Concepts

### Quality Assurance

**Quality Assurance** consists of planned and systematic activities intended to provide confidence that appropriate processes and practices are established, followed, evaluated, and improved to support required software quality.

QA is primarily:

- process-oriented;
- preventive;
- systematic;
- lifecycle-oriented;
- improvement-focused.

Its primary concern is:

> Are appropriate processes and practices being used to support quality?

Typical QA-oriented activities may include:

- defining quality standards;
- establishing review practices;
- improving requirement-quality processes;
- defining testing guidelines;
- establishing quality gates;
- reviewing process effectiveness;
- analyzing recurring quality problems;
- improving defect-prevention practices;
- supporting continuous improvement.

QA attempts to reduce the likelihood that quality problems are introduced or repeatedly occur.

---

### Quality Control

**Quality Control** consists of activities used to evaluate actual products or deliverables and determine whether they satisfy defined quality expectations.

QC is primarily:

- product-oriented;
- detection-focused;
- verification-focused;
- evidence-based;
- result-oriented.

Its primary concern is:

> Does the actual product or deliverable satisfy expected quality?

Typical QC-oriented activities may include:

- reviewing deliverables;
- executing tests;
- comparing actual and expected behavior;
- identifying defects;
- verifying defect fixes;
- performing regression testing;
- validating data;
- evaluating product behavior;
- recording quality evidence.

Testing is one of the primary Quality Control activities in software development.

---

### Prevention vs Detection

A useful distinction is:

```text
Quality Assurance
        │
        ▼
Prevent Quality Problems

Quality Control
        │
        ▼
Detect Quality Problems
```

For example, suppose a team repeatedly releases defects caused by ambiguous requirements.

A QC activity may detect a specific incorrect implementation during testing.

A QA activity may investigate why ambiguous requirements repeatedly reach development and improve the requirement-review process.

Both activities address quality, but at different levels.

---

### Process Quality vs Product Quality

QA and QC can also be viewed through process and product perspectives.

```text
Process Quality
        │
        ▼
How Software Is Produced
        │
        ▼
Quality Assurance
```

```text
Product Quality
        │
        ▼
How the Actual Product Behaves
        │
        ▼
Quality Control
```

Good processes can reduce quality risk.

However:

```text
Good Process
    ≠
Guaranteed Defect-Free Product
```

Likewise:

```text
Extensive Product Testing
    ≠
Replacement for Effective Process
```

Effective quality management combines both perspectives.

---

### QA vs QC Comparison

| Aspect | Quality Assurance | Quality Control |
|---|---|---|
| Primary focus | Process | Product |
| Primary objective | Prevent quality problems | Detect quality problems |
| Orientation | Preventive | Detective |
| Main question | Are appropriate quality processes being used? | Does the product satisfy expected quality? |
| Scope | Processes and practices across the lifecycle | Products and deliverables |
| Typical activities | Standards, process reviews, prevention, improvement | Testing, inspection, verification, evaluation |
| Typical evidence | Process effectiveness and improvement information | Test results, findings, defects, product evidence |
| Relationship to testing | Establishes and improves testing practices | Performs product evaluation through testing |

The comparison describes conceptual emphasis.

It does not define mandatory organizational responsibilities.

---

### QA Is Not the Same as Testing

A common simplification is:

```text
QA = Testing
```

This is incomplete.

Testing primarily evaluates actual software behavior and is therefore mainly a Quality Control activity.

Quality Assurance has a broader process-oriented perspective.

For example:

```text
Quality Assurance
│
├── Standards
├── Review Practices
├── Quality Processes
├── Defect Prevention
└── Continuous Improvement
```

```text
Quality Control
│
├── Test Design
├── Test Execution
├── Defect Detection
├── Fix Verification
└── Product Evaluation
```

In practice, a person with the title **QA Engineer** may perform activities from both groups.

---

### Role Title vs Quality Discipline

The conceptual meaning of QA and QC should not be inferred solely from job titles.

Organizations may use titles such as:

- QA Engineer;
- QC Engineer;
- Software Tester;
- Test Engineer;
- Quality Engineer.

Responsibilities may overlap significantly.

For example, a QA Engineer may:

- review requirements;
- design test scenarios;
- execute tests;
- report defects;
- analyze regression impact;
- improve testing practices.

Some of these activities are primarily QC-oriented, while others contribute to QA.

Therefore:

> Organizational role naming does not redefine the conceptual distinction between Quality Assurance and Quality Control.

---

### Quality Ownership

QA and QC contribute to quality, but neither implies that a QA or QC team independently owns all software quality.

Quality is influenced by multiple roles.

```text
Business
   +
Product
   +
Analysis
   +
Development
   +
QA / QC
   +
Operations
   │
   ▼
Software Quality
```

Quality should therefore be treated as a shared responsibility.

---

## How It Works

Quality Assurance and Quality Control operate most effectively as a feedback loop.

```text
Quality Process
      │
      ▼
Product Development
      │
      ▼
Quality Control
      │
      ▼
Quality Evidence
      │
      ├── Product Finding
      │
      └── Recurring Pattern
                 │
                 ▼
          Process Analysis
                 │
                 ▼
        Quality Assurance
                 │
                 ▼
        Process Improvement
                 │
                 └──────────► Future Development
```

Consider repeated authorization defects.

### Step 1 — QC Detects Product Problems

Testing identifies that users with incorrect roles can perform restricted actions.

This provides evidence about the current product.

### Step 2 — Patterns Are Identified

Multiple releases show similar authorization defects.

The issue is no longer only an isolated product problem.

### Step 3 — QA Investigates the Process

Possible process weaknesses may include:

- permission requirements are unclear;
- role matrices are incomplete;
- authorization design is not reviewed;
- test coverage is inconsistent.

### Step 4 — Process Improvements Are Introduced

Examples may include:

- clearer permission specifications;
- reusable authorization review checklists;
- earlier role-matrix review;
- standardized authorization testing guidance.

### Step 5 — QC Evaluates Future Products

Testing verifies whether later implementations satisfy the clarified expectations.

This creates a continuous feedback loop between product evaluation and process improvement.

---

## When to Use

The QA/QC distinction is useful when reasoning about whether a quality problem should be addressed at the product level, process level, or both.

### Recurring Defects

Use QA-oriented reasoning when similar defects repeatedly occur.

Instead of only asking:

> Has this defect been fixed?

also ask:

> What process weakness allows this type of defect to recur?

---

### Product Verification

Use QC-oriented reasoning when evaluating whether a specific product or change behaves correctly.

Examples include:

- executing functional tests;
- verifying a defect fix;
- validating API responses;
- checking database changes;
- performing regression testing.

---

### Requirement Quality

QA-oriented reasoning can help establish better requirement-review practices.

QC-oriented review can evaluate the quality of a specific requirement or deliverable.

---

### Test Process Improvement

Use QA reasoning when evaluating whether testing practices themselves should improve.

Examples include:

- recurring coverage gaps;
- regression suites becoming ineffective;
- inconsistent test-case quality;
- unclear entry or exit criteria.

---

### Quality Analysis

Use both perspectives when quality findings suggest both:

```text
Immediate Product Problem
        +
Underlying Process Problem
```

Fixing only one side may leave the other unresolved.

---

## When Not to Use

The QA/QC distinction should not be used to create unnecessary organizational boundaries.

Do not use it to conclude that:

- QA engineers should never execute tests;
- developers cannot perform QC activities;
- only a QA department can perform Quality Assurance;
- QC occurs only after development;
- QA owns all software quality;
- every organization must maintain separate QA and QC teams.

Avoid reasoning such as:

```text
This is QC work
      │
      ▼
QA must not do it
```

The conceptual distinction explains the purpose of activities.

It does not dictate project staffing or ownership.

Project-specific responsibilities must come from authoritative organizational or project information.

---

## Advantages

Understanding QA and QC separately provides several benefits.

### Better Root-Cause Thinking

Teams can distinguish between:

- fixing an individual product defect;
- improving the process that allowed the defect to occur.

### Better Defect Prevention

QA-oriented activities help reduce repeated quality problems rather than relying entirely on later detection.

### Better Product Evaluation

QC provides direct evidence about actual product behavior.

### Better Quality Ownership

The distinction helps demonstrate that quality involves both process and product responsibilities.

### Better Continuous Improvement

QC findings can become evidence for QA process improvement.

### Better QA-AI Reasoning

QA-AI can distinguish between:

```text
Product Risk
        │
        └── What could fail in the product?
```

and:

```text
Process Risk
        │
        └── What weakness could allow
            quality problems to occur?
```

---

## Limitations

The QA/QC distinction has several limitations when applied mechanically.

### Organizational Terminology Varies

Different organizations use QA and QC terminology differently.

Role titles may not reflect the conceptual definitions.

### Activities Can Overlap

Some activities contribute to both process improvement and product evaluation.

Strict classification may provide little practical value.

### Prevention Cannot Eliminate All Defects

Good QA practices reduce risk but cannot guarantee defect-free software.

### QC Cannot Prove Complete Quality

Testing provides evidence about tested conditions but cannot prove that no undiscovered defects remain.

### Generic Definitions Cannot Assign Project Responsibilities

Whether a specific activity belongs to QA, development, product, or another team is project-specific.

---

## Examples

### Example 1 — Requirement Ambiguity

Suppose a requirement does not clearly define whether duplicate submissions are allowed.

#### QC Perspective

Testing the implemented feature may reveal that duplicate records are created unexpectedly.

The current product behavior is evaluated.

#### QA Perspective

The team identifies that duplicate-handling expectations are frequently missing from requirements.

The requirement-review process is improved to explicitly consider duplicate behavior.

Together:

```text
QC
└── Detect current duplicate behavior

QA
└── Improve process to prevent recurring ambiguity
```

---

### Example 2 — Regression Defects

Suppose releases repeatedly introduce defects in existing functionality.

#### QC Response

Regression testing identifies which existing behaviors are broken.

#### QA Response

The team investigates whether:

- change-impact analysis is weak;
- regression coverage is outdated;
- shared dependencies are poorly understood;
- release practices need improvement.

QC provides evidence.

QA uses that evidence to improve the process.

---

### Example 3 — Authorization

Requirement:

```text
Viewer users cannot approve requests.
```

QC may verify:

```text
Viewer Account
      │
      ▼
Open Request
      │
      ▼
Attempt Approval
      │
      ▼
Compare Actual and Expected Behavior
```

If authorization defects repeatedly occur across features, QA may improve:

- role-permission documentation;
- requirement-review checklists;
- authorization design reviews;
- reusable testing guidance.

---

### Example 4 — Import Processing

Suppose an import feature repeatedly creates duplicate records during retries.

QC may test:

- duplicate files;
- duplicate rows;
- retry behavior;
- concurrent submissions.

QA may investigate whether the development process adequately addresses:

- idempotency;
- duplicate-handling requirements;
- integration review;
- failure-recovery design.

Both perspectives contribute to improving quality.

---

## Best Practices

When applying QA and QC concepts:

1. Treat QA and QC as complementary rather than competing disciplines.
2. Use QC evidence to identify potential process improvements.
3. Analyze recurring defects rather than repeatedly fixing symptoms only.
4. Include quality activities throughout the lifecycle.
5. Maintain clear quality standards and review practices.
6. Evaluate actual product behavior objectively.
7. Distinguish process risk from product risk.
8. Keep quality ownership shared across relevant roles.
9. Adapt responsibilities to project context.
10. Avoid interpreting organizational titles as strict conceptual boundaries.

For QA-AI:

- distinguish product findings from process observations;
- avoid assigning responsibilities without project evidence;
- do not assume QA means testing only;
- do not infer organizational structure from generic QA/QC definitions;
- treat recurring patterns as signals for possible process analysis, not proof of a specific root cause.

---

## Related Knowledge

### Software Quality

`Software-Quality.md` defines the broader concept that QA and QC both support.

Software Quality describes **what quality means**, while this article explains two complementary approaches for supporting and evaluating that quality.

### Software Development Life Cycle

`SDLC.md` explains the broader lifecycle in which QA and QC activities can occur.

QA and QC should not be restricted to a single lifecycle stage.

### Software Testing Life Cycle

`STLC.md` describes the lifecycle of testing activities.

Testing within STLC primarily contributes to Quality Control by producing product-quality evidence.

### Verification and Validation

`Verification-and-Validation.md` explains complementary evaluation concepts concerned with whether software is built correctly and whether it satisfies intended needs.

Verification and validation are related to QA/QC but are not synonymous with them.

### Defect Analysis

`Defect-Analysis.md` can use QC findings to identify recurring defect patterns that may indicate broader quality-process concerns.

### Continuous Improvement

`Continuous-Improvement.md` describes how quality evidence and learning can be used to improve future processes and practices.

---

## References

This article is conceptually aligned with established software quality and testing bodies of knowledge, including:

- ISO 9000 quality management concepts concerning quality assurance and quality control.
- ISO/IEC/IEEE 29119 software testing concepts and processes.
- ISTQB Certified Tester Foundation Level syllabus — fundamental testing and quality concepts.

Terminology may vary across standards and organizations.

These references provide conceptual guidance only.

Project-specific responsibilities, quality processes, role definitions, and organizational structures must come from authoritative project sources.