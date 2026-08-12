# Experience-Based Testing

## Purpose

The **Experience-Based Testing** knowledge base covers testing techniques that primarily use tester experience, intuition, domain knowledge, historical defect patterns, observation, and continuous learning to guide testing activities.

Unlike techniques that derive tests mainly from formal specifications or internal code structure, Experience-Based Testing uses accumulated knowledge and adaptive investigation to identify risks and defects that structured techniques may not fully reveal.

This knowledge category provides reusable guidance for applying experience-driven testing systematically rather than relying on undocumented intuition or random testing.

---

## Scope

The Experience-Based Testing knowledge base contains four techniques:

- Error Guessing
- Checklist-Based Testing
- Exploratory Testing
- Session-Based Testing

Each technique applies tester experience in a different way.

| Technique | Primary Focus |
|---|---|
| Error Guessing | Predict likely defects using experience, historical failures, and known defect patterns. |
| Checklist-Based Testing | Convert accumulated testing knowledge into reusable verification guidance. |
| Exploratory Testing | Combine learning, test design, execution, and analysis during active investigation. |
| Session-Based Testing | Organize exploratory testing into focused, timeboxed, documented, and reviewable sessions. |

The category focuses on **experience-driven test design and investigation**.

Broader QA processes such as test planning, test strategy, test management, regression strategy, and defect management belong to their respective QA knowledge areas.

---

## Learning Objectives

After completing this knowledge category, readers should be able to:

- Explain the principles of Experience-Based Testing.
- Understand how tester experience contributes to test design and defect detection.
- Recognize recurring defect patterns and use them to guide testing.
- Apply Error Guessing systematically.
- Build and maintain reusable testing checklists.
- Perform adaptive Exploratory Testing.
- Organize exploratory work using Session-Based Testing.
- Define focused exploratory testing charters.
- Capture meaningful session observations and findings.
- Conduct session debriefs and identify follow-up testing.
- Combine experience-based techniques with structured testing techniques.
- Recognize the strengths and limitations of experience-driven testing.

---

## Knowledge Structure

```text
Experience-Based/
│
├── README.md
├── Error-Guessing.md
├── Checklist-Based-Testing.md
├── Exploratory-Testing.md
└── Session-Based-Testing.md
```

Each technique article follows the standardized knowledge-article conventions defined by the QA-AI framework.

---

## Knowledge Map

```text
Experience-Based Testing
        │
        ├── Error Guessing
        │       │
        │       └── Predict likely defects
        │
        ├── Checklist-Based Testing
        │       │
        │       └── Reuse accumulated testing knowledge
        │
        └── Exploratory Testing
                │
                ├── Learn
                ├── Design
                ├── Execute
                └── Investigate
                        │
                        ▼
                Session-Based Testing
                        │
                        ├── Charter
                        ├── Timebox
                        ├── Session Notes
                        └── Debrief
```

The techniques are related but serve different purposes.

**Error Guessing** helps testers anticipate likely failures.

**Checklist-Based Testing** converts accumulated experience into reusable testing guidance.

**Exploratory Testing** enables adaptive investigation based on continuous learning.

**Session-Based Testing** adds structure and visibility to exploratory work while preserving its adaptive nature.

---

## Learning Roadmap

A recommended learning sequence is:

```text
Error Guessing
        │
        ▼
Checklist-Based Testing
        │
        ▼
Exploratory Testing
        │
        ▼
Session-Based Testing
```

### Error Guessing

Start by learning how previous defects, technical experience, domain knowledge, and common failure patterns can guide testing.

This develops the ability to recognize areas where defects are likely to occur.

### Checklist-Based Testing

Learn how experience can be converted from individual knowledge into reusable testing guidance.

Checklists help preserve important verification ideas and reduce dependence on tester memory.

### Exploratory Testing

Apply experience dynamically while interacting with the system.

Exploratory Testing combines learning, test design, execution, observation, and investigation.

The tester continuously adjusts testing based on newly discovered information.

### Session-Based Testing

After understanding Exploratory Testing, learn how exploratory work can be organized into focused sessions.

Session-Based Testing introduces:

- Testing missions.
- Charters.
- Timeboxes.
- Session notes.
- Findings.
- Debriefs.
- Follow-up actions.

This provides greater visibility and reviewability without converting exploration into scripted testing.

---

## Technique Relationships

The four techniques can reinforce each other.

```text
Historical Defects
        │
        ▼
Error Guessing
        │
        ▼
Reusable Testing Knowledge
        │
        ▼
Checklist-Based Testing
        │
        ▼
Adaptive Investigation
        │
        ▼
Exploratory Testing
        │
        ▼
Structured Exploration
        │
        ▼
Session-Based Testing
```

This represents a possible learning and knowledge-reuse progression rather than a mandatory execution sequence.

For example:

- Error Guessing may provide ideas for exploratory testing.
- Exploratory Testing may reveal new defect patterns.
- Repeated findings may become checklist items.
- A checklist may identify an area requiring deeper investigation.
- An exploratory investigation may become a dedicated Session-Based Testing charter.
- Session findings may generate regression tests or additional exploratory charters.

Experience-Based Testing therefore supports continuous learning rather than a fixed linear process.

---

## Relationship with Other Testing Techniques

Experience-Based Testing complements other testing techniques rather than replacing them.

### Specification-Based Testing

Specification-Based Testing derives tests from requirements, business rules, functional specifications, and externally observable behavior.

Experience-Based Testing supplements this by identifying likely failures, unexpected behavior, and areas requiring deeper investigation.

### Structure-Based Testing

Structure-Based Testing evaluates internal implementation structures and execution coverage.

Experience-Based Testing instead uses practical knowledge, historical patterns, and investigation to identify defect-prone behavior.

### Combined Application

A comprehensive testing approach may combine:

```text
Requirements
        │
        ▼
Specification-Based Testing
        │
        ▼
Expected Functional Coverage
        │
        ▼
Experience-Based Testing
        │
        ▼
Risk and Exploratory Coverage
        │
        ▼
Structure-Based Testing
        │
        ▼
Implementation Coverage
```

The exact combination depends on system risk, available information, testing objectives, and development context.

---

## Core Characteristics

Experience-Based Testing commonly has the following characteristics:

- Experience-driven decision making.
- Knowledge of recurring defect patterns.
- Domain awareness.
- Critical thinking.
- Adaptive investigation.
- Risk awareness.
- Flexible test execution.
- Continuous learning.
- Reuse of accumulated testing knowledge.

Experience becomes increasingly valuable when it is documented and shared rather than remaining only in individual tester memory.

---

## Practical Applications

Experience-Based Testing is particularly useful when:

- Requirements are incomplete or evolving.
- A feature contains uncertain behavior.
- Historical defects indicate recurring risk.
- Time for formal test design is limited.
- High-risk functionality requires deeper investigation.
- Scripted test cases provide insufficient confidence.
- Unexpected behavior appears during execution.
- Production issues require investigation.
- Complex integrations require adaptive testing.
- New functionality requires rapid learning.

Experience-Based Testing should normally complement, rather than automatically replace, systematic test design.

---

## Common Experience Patterns

Experienced testers frequently recognize recurring failure patterns.

### Authentication

```text
Authentication
        │
        ├── Invalid Credentials
        ├── Session Timeout
        ├── Expired Token
        ├── Permission Changes
        ├── Concurrent Login
        └── Logout / Token Invalidation
```

### Import and Upload

```text
Import / Upload
        │
        ├── Invalid File Type
        ├── Duplicate Records
        ├── Large Files
        ├── File Encoding
        ├── Special Characters
        ├── Interrupted Upload
        └── Repeated Submission
```

### Search

```text
Search
        │
        ├── Empty Input
        ├── Whitespace
        ├── Case Sensitivity
        ├── Special Characters
        ├── Sorting
        ├── Filtering
        └── Pagination
```

### Transactions

```text
Transaction
        │
        ├── Duplicate Submission
        ├── Timeout
        ├── Retry
        ├── Concurrent Requests
        ├── Partial Failure
        └── State Inconsistency
```

These patterns can support Error Guessing, checklist creation, exploratory investigation, and session charter design.

---

## Selecting a Technique

Use the following guide as a practical starting point.

```text
Known likely defect patterns?
        │
        ├── Yes → Error Guessing
        │
        └── No
             │
             ▼
Reusable verification knowledge?
        │
        ├── Yes → Checklist-Based Testing
        │
        └── No
             │
             ▼
Adaptive investigation required?
        │
        ├── No → Use another suitable technique
        │
        └── Yes
             │
             ▼
Need explicit focus, timeboxing,
documentation, and reviewability?
        │
        ├── No → Exploratory Testing
        │
        └── Yes → Session-Based Testing
```

This is not an exclusive decision tree.

Multiple experience-based techniques may be combined when appropriate.

---

## Best Practices

To maximize the effectiveness of Experience-Based Testing:

- Learn from previous defects.
- Validate assumptions through actual testing.
- Maintain reusable testing checklists.
- Document meaningful testing observations.
- Continuously refine testing heuristics.
- Use focused exploratory objectives.
- Capture reusable findings from exploratory sessions.
- Combine experience with structured testing techniques.
- Share testing knowledge across the QA team.
- Convert recurring findings into reusable QA assets.

Experience should guide investigation, not replace evidence.

---

## Common Mistakes

Common mistakes include:

- Treating experience-based testing as random testing.
- Relying on intuition without validating assumptions.
- Replacing structured test design completely.
- Keeping important testing knowledge only in individual memory.
- Treating Exploratory Testing as uncontrolled clicking.
- Over-scripting exploratory investigation.
- Treating Session-Based Testing as scripted testing.
- Using defect count as the only measure of testing value.
- Failing to reuse lessons from previous defects and sessions.

---

## Knowledge Reuse in QA-AI

Experience-Based Testing knowledge can support QA-AI capabilities by helping them:

- Identify likely defect areas.
- Generate additional edge cases.
- Recognize recurring failure patterns.
- Improve scenario diversity.
- Suggest exploratory testing areas.
- Build reusable QA checklists.
- Identify risk-focused follow-up testing.
- Generate candidate exploratory charters.
- Identify gaps in structured test coverage.

Experience-based knowledge supports QA reasoning.

It must not silently introduce project-specific business rules that are absent from authoritative requirements or other trusted project sources.

---

## Related Knowledge

### Prerequisites

- Foundation Testing Techniques
- Black Box Testing

### Related Testing Techniques

- Specification-Based Testing
- Structure-Based Testing
- Risk-Based Testing

### Related QA Topics

- Test Design
- Test Strategy
- Regression Testing
- Defect Analysis
- Risk Analysis

### Articles in This Category

- `Error-Guessing.md`
- `Checklist-Based-Testing.md`
- `Exploratory-Testing.md`
- `Session-Based-Testing.md`

---

## References

Related repository resources include:

- `shared/knowledge/testing-techniques/Catalog.md`
- `shared/knowledge/testing-techniques/Foundation/`
- `shared/knowledge/testing-techniques/Specification-Based/`
- `shared/knowledge/testing-techniques/Structure-Based/`
- `shared/knowledge/qa/`
- `shared/glossary/QA-Terms.md`
- `shared/standards/Knowledge-Article.md`
- `shared/templates/`
- `shared/checklists/`
- `skills/`
- `workflows/`

---

## Summary

Experience-Based Testing uses tester experience, domain knowledge, historical defects, observation, and adaptive learning to improve software testing.

The category contains four complementary techniques:

```text
Error Guessing
        ↓
Predict likely defects

Checklist-Based Testing
        ↓
Reuse accumulated knowledge

Exploratory Testing
        ↓
Investigate and learn dynamically

Session-Based Testing
        ↓
Structure and review exploratory work
```

Together, these techniques transform individual testing experience into focused, reusable, and continuously improving QA knowledge.

They are most effective when combined with systematic testing techniques and grounded in actual requirements, observed behavior, and evidence.