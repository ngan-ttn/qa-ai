# Session-Based Testing

> Version: 1.0.0
> Status: Draft
> Last Updated: YYYY-MM-DD

---

# Overview

Session-Based Testing is a structured approach to Exploratory Testing in which testing is organized into focused, timeboxed sessions with explicit objectives, documented observations, and reviewable results.

Exploratory Testing emphasizes simultaneous learning, test design, execution, and analysis. Session-Based Testing adds a management and documentation structure around that exploration without turning it into fully scripted testing.

The technique answers one fundamental question:

> **How can exploratory testing remain flexible while still being focused, observable, and reviewable?**

A session normally combines:

- A clear testing mission.
- A focused charter.
- A defined timebox.
- Exploratory execution.
- Session notes.
- Defect and issue recording.
- A post-session debrief.

The purpose is not to prescribe every test step in advance.

The purpose is to give exploratory work enough structure that teams can understand what was tested, what was learned, what was discovered, and what should happen next.

---

# Purpose

The primary purpose of Session-Based Testing is to provide structure, visibility, and accountability for exploratory testing while preserving tester autonomy and adaptive investigation.

Its objectives include:

- Focus exploratory testing on meaningful risks.
- Prevent unfocused or random exploration.
- Organize testing into manageable sessions.
- Capture observations and learning during execution.
- Improve visibility into exploratory testing activities.
- Support review and debrief after testing.
- Identify follow-up testing opportunities.
- Preserve useful knowledge for future testing.

---

# Learning Objectives

After completing this article, readers should be able to:

- Explain the concept of Session-Based Testing.
- Understand its relationship with Exploratory Testing.
- Define an effective testing charter.
- Understand the purpose of a session timebox.
- Record meaningful session notes.
- Conduct a session debrief.
- Interpret session results.
- Recognize when Session-Based Testing is appropriate.
- Distinguish structured exploration from scripted testing.

---

# Knowledge Map

    Experience-Based Testing
            │
            ▼
    Exploratory Testing
            │
            ▼
    Session-Based Testing
            │
            ├── Charter
            ├── Timebox
            ├── Exploration
            ├── Session Notes
            └── Debrief

Session-Based Testing provides a structured execution model for exploratory testing.

---

# Why Session-Based Testing Exists

Exploratory Testing provides significant flexibility.

That flexibility is valuable because testers can continuously adapt their testing based on observations and newly discovered risks.

However, completely unstructured exploration can create practical problems.

For example:

- It may be unclear what was actually tested.
- Multiple testers may unknowingly explore the same area.
- Important risks may receive insufficient attention.
- Testing effort may be difficult to review.
- Valuable observations may not be documented.
- Follow-up investigations may be forgotten.
- Stakeholders may interpret exploratory testing as random testing.

Consider a tester who spends two hours exploring a checkout feature.

Several issues are discovered.

However, after the activity, the team cannot clearly answer:

- What was the original testing objective?
- Which areas were explored?
- Which areas were not explored?
- What risks were discovered?
- What questions remain?
- What should be tested next?

Session-Based Testing exists to solve this problem.

It adds enough structure to exploratory testing so that the activity remains flexible while its purpose, effort, findings, and learning remain visible.

---

# History and Background

Session-Based Test Management was developed to provide a practical way to organize and manage exploratory testing.

The approach is closely associated with James Bach and Jonathan Bach.

The central idea is that exploratory testing does not need detailed predefined test scripts to become manageable.

Instead, exploratory work can be organized into focused sessions.

Each session has:

- A mission.
- A charter.
- A time boundary.
- Recorded testing activity.
- Reviewable results.

This allows teams to preserve the adaptive nature of exploratory testing while improving transparency and accountability.

---

# Core Concepts

## Testing Session

A testing session is a focused period of exploratory testing performed against a defined mission or charter.

A session should have a clear beginning and end.

During the session, the tester actively:

- Learns about the system.
- Designs tests.
- Executes tests.
- Observes behavior.
- Investigates findings.
- Records useful information.

The session provides a manageable unit of exploratory work.

---

## Mission

The mission describes the broader purpose of the testing activity.

Example:

    Investigate the reliability of the authentication flow.

A mission may lead to one or multiple testing charters.

---

## Testing Charter

A testing charter defines the focus of a particular session.

A useful charter typically describes:

- What will be explored.
- What risk or behavior deserves attention.
- What perspective or testing approach may be useful.

Example:

    Explore the login flow with a focus on
    session expiration, repeated authentication,
    and recovery after network interruption.

A charter provides direction.

It should not define every action the tester must execute.

---

## Timebox

A timebox limits the duration of a testing session.

The objective is to keep exploration focused and reviewable.

A session may be relatively short or long depending on:

- Feature complexity.
- Risk.
- Investigation depth.
- Team practice.
- Availability of the test environment.

The exact duration is less important than maintaining a deliberate boundary around the activity.

The timebox should not force a tester to ignore a critical discovery.

If a finding requires significant additional investigation, it may become the focus of another session.

---

## Exploration

Exploration is the active investigation performed during the session.

The tester continuously decides what to test next based on:

- Current understanding.
- Observed behavior.
- Known risks.
- Unexpected results.
- Defect patterns.
- Business knowledge.
- Technical knowledge.

Exploration remains adaptive even though the session itself has structure.

---

## Session Notes

Session notes record meaningful information generated during testing.

Typical notes may include:

- Areas explored.
- Test ideas.
- Actions performed.
- Important observations.
- Defects.
- Risks.
- Questions.
- Environment issues.
- Test data used.
- Follow-up ideas.

Session notes do not need to reproduce every click.

They should preserve enough information to understand the investigation and its outcomes.

---

## Issues

Not every observation is immediately a confirmed defect.

A session may identify:

- Defects.
- Requirement questions.
- Environment problems.
- Data problems.
- Usability concerns.
- Risks.
- Areas requiring further investigation.

These should be recorded appropriately rather than forced into a defect classification.

---

## Debrief

A debrief is a review performed after the session.

The tester and reviewer discuss:

- What was tested?
- What was learned?
- What defects were discovered?
- What risks were identified?
- What prevented testing?
- What remains unclear?
- What should happen next?

The debrief converts individual exploration into shared team knowledge.

---

## Follow-Up Session

A session frequently creates new questions.

These questions may justify additional charters.

For example:

    Session 1:
    Explore checkout under network interruption.

            ↓

    Observation:
    Duplicate payment requests may occur.

            ↓

    Session 2:
    Explore duplicate-submission protection
    during payment retries.

Session-Based Testing therefore supports iterative investigation.

---

# Relationship with Exploratory Testing

Session-Based Testing and Exploratory Testing are closely related but are not identical concepts.

| Aspect | Exploratory Testing | Session-Based Testing |
|---|---|---|
| Primary focus | Adaptive learning and investigation | Structured management of exploration |
| Test design | During execution | During execution |
| Predefined detailed steps | No | No |
| Charter | Optional | Core element |
| Timebox | Optional | Core element |
| Notes | Recommended | Expected |
| Debrief | Optional | Important |
| Management visibility | Variable | Higher |
| Tester autonomy | High | High |

Exploratory Testing defines the adaptive testing approach.

Session-Based Testing provides a structured way to organize that approach.

---

# Relationship with Scripted Testing

Session-Based Testing should not be confused with scripted testing.

A scripted test may define:

    Step 1 — Open Login page
    Step 2 — Enter valid username
    Step 3 — Enter valid password
    Step 4 — Click Login
    Step 5 — Verify Dashboard

A session charter may instead define:

    Explore authentication behavior with a focus on
    session handling and interrupted login attempts.

The scripted test defines actions in advance.

The charter defines a mission while allowing the tester to determine actions during execution.

---

# Testing Philosophy

Session-Based Testing is based on one central principle:

> **Exploration can remain adaptive without becoming invisible or unmanaged.**

Structure should support exploration rather than restrict it.

The objective is not to convert exploratory testing into predefined test cases.

The objective is to make exploratory work:

- Focused.
- Observable.
- Reviewable.
- Reusable.

---

# How It Works

A typical Session-Based Testing cycle follows:

    Identify Testing Mission
            │
            ▼
    Define Charter
            │
            ▼
    Prepare Session
            │
            ▼
    Start Timebox
            │
            ▼
    Explore and Learn
            │
            ▼
    Record Notes and Findings
            │
            ▼
    End Session
            │
            ▼
    Debrief
            │
            ▼
    Define Follow-Up Actions

---

## Step 1 — Identify the Testing Mission

Determine the broader objective.

Questions may include:

- What feature needs investigation?
- What risk is important?
- Why is exploration needed?
- What information is currently missing?
- What level of confidence is required?

Example:

    Mission:
    Investigate reliability risks in the file upload workflow.

---

## Step 2 — Define the Charter

Translate the mission into a focused exploratory objective.

Example:

    Explore Excel file upload with a focus on
    interrupted uploads, repeated submission,
    and recovery after failure.

A useful charter should be:

- Focused.
- Understandable.
- Risk-oriented where appropriate.
- Broad enough to allow investigation.
- Narrow enough to prevent random exploration.

---

## Step 3 — Prepare the Session

Before starting, prepare what is necessary to make exploration productive.

This may include:

- Test environment.
- Test account.
- Test data.
- Logs.
- API tools.
- Database access.
- Requirement references.
- Existing defect information.

Preparation should support the session without turning the charter into a scripted test case.

---

## Step 4 — Start the Timebox

Begin the defined session period.

During this period, the tester should primarily focus on the charter.

Unrelated findings may be recorded for later investigation rather than causing uncontrolled scope expansion.

---

## Step 5 — Explore and Learn

Interact with the system and continuously adapt testing.

Example:

    Upload starts
        ↓
    Progress becomes slow
        ↓
    Tester refreshes page
        ↓
    Upload request is repeated
        ↓
    Duplicate processing suspected
        ↓
    Tester investigates request and data state

The direction of testing changes because new information is discovered.

---

## Step 6 — Record Notes and Findings

Capture meaningful information throughout the session.

Example session notes:

    Charter:
    Explore file upload recovery behavior.

    Areas explored:
    - Browser refresh during upload
    - Network interruption
    - Repeated upload
    - Retry after timeout

    Observations:
    - Progress indicator does not recover after reconnect.
    - Refresh may resend the upload request.

    Issues:
    - Possible duplicate processing after refresh.

    Questions:
    - Is upload request expected to be idempotent?

    Follow-up:
    - Verify database state after repeated request.

Notes should support later review without unnecessarily documenting every minor interaction.

---

## Step 7 — End the Session

At the end of the timebox:

- Stop the current exploration at a reasonable point.
- Preserve notes.
- Record unresolved questions.
- Ensure defects have sufficient evidence.
- Identify unfinished investigations.

A critical active investigation may require immediate continuation, but that continuation should remain visible rather than silently extending the session indefinitely.

---

## Step 8 — Conduct the Debrief

Review the session.

A debrief may cover:

### Mission

Was the charter addressed?

### Coverage

Which areas were explored?

### Findings

What defects, risks, and questions were identified?

### Obstacles

What prevented effective testing?

### Learning

What new understanding was gained?

### Follow-Up

What should be investigated next?

---

## Step 9 — Define Follow-Up Actions

Session results may lead to:

- New exploratory sessions.
- New scripted regression tests.
- Requirement clarification.
- Defect investigation.
- Checklist updates.
- Test-data preparation.
- Environment fixes.
- Risk reassessment.

This prevents session learning from being lost after execution.

---

# Session Structure

A practical session record may contain:

| Field | Purpose |
|---|---|
| Session ID | Identifies the session |
| Tester | Identifies who performed the session |
| Date | Records when testing occurred |
| Mission | Defines the broader testing objective |
| Charter | Defines the focus of the session |
| Timebox | Defines the planned session boundary |
| Environment | Records relevant execution context |
| Areas Explored | Summarizes coverage |
| Notes | Records meaningful observations |
| Defects | References confirmed defects |
| Issues | Records other concerns or blockers |
| Questions | Captures unresolved information |
| Follow-Up | Defines next actions |

The exact template may vary by organization.

The important principle is that the record preserves the purpose and learning of the session.

---

# Session Metrics

Session-Based Testing may use lightweight metrics to improve visibility.

Possible measures include:

- Number of completed sessions.
- Number of charters covered.
- Time spent testing.
- Time spent investigating defects.
- Time lost to setup or environment problems.
- Number of issues discovered.
- Number of follow-up charters created.

Metrics should support decision-making.

They should not be used mechanically to judge tester productivity.

For example:

    More defects found ≠ Better tester

and:

    More sessions completed ≠ Better coverage

The value of a session depends on risk, learning, investigation quality, and useful outcomes.

---

# Coverage Interpretation

Session-Based Testing does not provide structural coverage metrics such as statement or branch coverage.

Coverage is usually interpreted through the charters and areas explored.

For example:

    Authentication

    Session 1 → Session expiration
    Session 2 → Concurrent login
    Session 3 → Network interruption
    Session 4 → Account lock behavior

Together, these sessions provide visibility into which risk areas have been explored.

Session coverage should not be interpreted as proof that every possible behavior has been tested.

---

# When to Use

Session-Based Testing is particularly useful when:

- Exploratory testing needs more structure.
- Requirements are incomplete or evolving.
- A feature contains uncertain risks.
- A new feature requires rapid learning.
- Scripted tests provide insufficient confidence.
- Complex workflows require investigation.
- Production issues need reproduction.
- Regression testing reveals unexpected behavior.
- Multiple testers perform exploratory testing.
- Testing activity needs better visibility.
- Teams need documented exploratory findings.

It is especially valuable when the tester needs freedom to investigate but the team also needs traceability and reviewability.

---

# When Not to Use

Session-Based Testing should not be the only testing approach when:

- Exact regulatory evidence requires predefined execution steps.
- A deterministic regression suite must be repeatedly executed.
- Automated verification is more appropriate.
- Formal acceptance procedures require scripted test evidence.
- A simple requirement can be verified efficiently with a small number of deterministic tests.

It should also not be used merely to make random testing appear structured.

A charter without purposeful investigation does not create meaningful Session-Based Testing.

---

# Advantages

## Preserves Exploratory Flexibility

Testers can continuously adapt their investigation based on new information.

---

## Improves Focus

Charters prevent exploration from becoming unnecessarily broad or random.

---

## Improves Visibility

Session records help teams understand:

- What was explored.
- Why it was explored.
- What was discovered.
- What remains.

---

## Supports Accountability

Testing activity becomes reviewable without requiring detailed scripted test cases.

---

## Captures Learning

Notes preserve information that may otherwise remain only in the tester's memory.

---

## Supports Team Collaboration

Debriefs allow individual observations to become shared knowledge.

---

## Supports Follow-Up Testing

New risks and questions can become future charters, regression tests, or clarification items.

---

## Complements Scripted Testing

Session-Based Testing can investigate risks that predefined test cases may not anticipate.

---

# Limitations

## Depends on Tester Skill

Effective sessions require:

- Observation.
- Critical thinking.
- Product knowledge.
- Risk awareness.
- Investigation ability.
- Note-taking discipline.

A charter alone does not guarantee effective exploration.

---

## Documentation Quality Can Vary

Poor notes may make a session difficult to review or reproduce.

---

## Repeatability Is Limited

Different testers may follow different investigation paths even when using the same charter.

This is expected because the approach remains exploratory.

---

## Coverage Is Not Exhaustive

Completing a charter does not prove that every behavior within the area has been tested.

---

## Timeboxes Can Be Misused

Rigid enforcement may interrupt valuable investigations.

Timeboxes should support focus and planning, not discourage appropriate investigation.

---

## Metrics Can Be Misinterpreted

Session counts, defect counts, or testing time can create misleading conclusions when used as productivity measures.

---

# Examples

## Example 1 — Authentication

### Mission

Investigate authentication reliability.

### Charter

    Explore login behavior with a focus on
    session expiration and concurrent login.

### Exploration

The tester:

- Logs in from multiple browsers.
- Waits for session expiration.
- Refreshes expired sessions.
- Reuses old browser tabs.
- Changes credentials during an active session.

### Findings

- One browser remains authenticated after password change.
- Expired session message is inconsistent.
- Concurrent session behavior requires clarification.

### Follow-Up

Create another session focused on token invalidation.

---

## Example 2 — File Upload

### Mission

Investigate upload reliability.

### Charter

    Explore Excel upload behavior under
    interruption and repeated submission.

### Exploration

The tester:

- Interrupts the network.
- Refreshes during upload.
- Retries after timeout.
- Uploads the same file again.
- Opens another browser tab.

### Findings

- Progress state becomes inconsistent.
- Duplicate request may be processed.
- Retry behavior is unclear.

### Follow-Up

Investigate duplicate processing and database consistency.

---

## Example 3 — REST API

### Mission

Investigate transaction reliability.

### Charter

    Explore transaction creation with a focus on
    timeout, retry, and duplicate requests.

### Exploration

The tester:

- Sends a valid request.
- Simulates timeout.
- Retries the request.
- Reuses the same request data.
- Sends requests concurrently.

### Findings

- Duplicate transaction may be created after retry.
- Error response does not indicate whether the original request succeeded.

### Follow-Up

Investigate idempotency behavior and database records.

---

## Example 4 — Mobile Application

### Mission

Investigate state recovery.

### Charter

    Explore an in-progress transaction with a focus on
    app backgrounding, termination, and network changes.

### Exploration

The tester:

- Moves the app to background.
- Terminates the app.
- Changes Wi-Fi to mobile data.
- Reopens the app.
- Repeats the action.

### Findings

- Loading state is not restored consistently.
- Repeated submission may occur after recovery.

### Follow-Up

Create a focused session for transaction-state synchronization.

---

# Best Practices

## Write Focused Charters

Avoid:

    Explore the entire application.

Prefer:

    Explore checkout with a focus on
    duplicate submission and recovery after payment timeout.

---

## Focus on Risks

Use known risks to guide charters when appropriate.

Examples:

- Data loss.
- Duplicate processing.
- Authorization.
- State inconsistency.
- Integration failure.
- Recovery behavior.

---

## Keep Notes Useful

Record information that supports:

- Understanding.
- Reproduction.
- Follow-up.
- Decision-making.

Do not turn session notes into unnecessary click-by-click transcripts.

---

## Separate Findings by Type

Distinguish:

- Confirmed defects.
- Risks.
- Questions.
- Environment issues.
- Test-data issues.
- Future ideas.

This improves follow-up handling.

---

## Debrief Consistently

Do not treat the debrief as optional when session results affect team decisions.

The debrief is where exploratory learning becomes shared knowledge.

---

## Convert Stable Findings into Reusable Assets

A session may reveal scenarios that should later become:

- Regression tests.
- Checklists.
- Test data.
- Risk items.
- Knowledge articles.

Exploration should contribute to future testing maturity.

---

## Avoid Over-Scripting the Charter

A charter should guide exploration.

If it contains detailed predefined actions and expected results for every step, it is becoming a scripted test case.

---

## Preserve Tester Autonomy

Structure should not prevent testers from following meaningful observations.

Unexpected behavior is often the most valuable direction for further investigation.

---

# Common Mistakes

## Treating Sessions as Random Testing

A session must have a meaningful mission and charter.

---

## Writing Charters That Are Too Broad

Example:

    Test the payment module.

This provides insufficient focus.

---

## Writing Charters That Are Too Detailed

A charter should not prescribe every step.

Overly detailed charters remove the adaptive nature of exploratory testing.

---

## Ignoring Session Notes

Without useful notes, learning and coverage visibility may be lost.

---

## Skipping Debrief

Important findings may remain isolated with the individual tester.

---

## Measuring Productivity by Defect Count

A session that finds no defect may still provide valuable confidence or knowledge.

---

## Extending Sessions Indefinitely

If a new investigation becomes substantial, create a follow-up charter rather than silently expanding the original scope.

---

# Decision Guide

Use the following guide when deciding whether Session-Based Testing is appropriate.

    Is exploratory investigation needed?
            │
            ├── No
            │    │
            │    ▼
            │  Use another suitable technique
            │
            └── Yes
                 │
                 ▼
    Does the exploration need focus,
    visibility, or reviewability?
                 │
                 ├── No
                 │    │
                 │    ▼
                 │  Exploratory Testing may be sufficient
                 │
                 └── Yes
                      │
                      ▼
              Use Session-Based Testing

---

# QA Review Checklist

Before considering a session complete, review the following.

## Session Definition

- □ Is the mission clear?
- □ Is the charter focused?
- □ Is the scope understandable?
- □ Is the timebox defined?

## Preparation

- □ Is the environment ready?
- □ Is required test data available?
- □ Are relevant references accessible?

## Execution

- □ Did testing remain primarily aligned with the charter?
- □ Were meaningful observations investigated?
- □ Were important notes captured?
- □ Were defects supported by sufficient evidence?
- □ Were blockers and environment issues recorded?

## Debrief

- □ Was the session outcome reviewed?
- □ Were important findings discussed?
- □ Were unresolved questions identified?
- □ Were follow-up actions defined?

## Knowledge Reuse

- □ Should any finding become a regression test?
- □ Should any finding update a checklist?
- □ Should another exploratory charter be created?
- □ Should any risk or lesson be preserved for future testing?

---

# Related Knowledge

Session-Based Testing is closely related to:

- Exploratory Testing
- Checklist-Based Testing
- Error Guessing
- Risk-Based Testing
- Regression Testing
- Test Planning
- Defect Analysis

The most important prerequisite is Exploratory Testing.

Session-Based Testing should be understood as a structured approach for organizing exploratory work rather than a replacement for exploratory thinking.

---

# References

Recommended reference areas include:

- Exploratory Testing literature.
- Session-Based Test Management literature.
- Experience-Based Testing guidance.
- Software testing body-of-knowledge materials.
- Organizational exploratory testing practices.

When external references are added to the repository, they should follow the repository documentation and citation standards.

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | YYYY-MM-DD | Initial version |