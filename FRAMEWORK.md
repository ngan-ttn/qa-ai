# QA-AI Framework

> Version: 1.0.0  
> Status: Approved  
> Last Updated: 2026-08-20

## 1. Framework Identity

QA-AI is a vendor-neutral, modular QA skill framework designed to transform software requirements and related project context into structured QA deliverables.

The framework provides reusable QA knowledge, standards, templates, skills, and workflows that can be consumed by compatible AI runtimes without coupling the core framework to a specific AI provider, model, or product.

QA-AI is designed around a simple principle:

```text
Requirement
    +
QA-AI Framework
    +
AI Runtime
    │
    ▼
Structured QA Execution
    │
    ▼
QA Deliverables
```

The AI runtime provides the reasoning and generation capability.

QA-AI provides the QA operating model that guides how that capability is used.

### 1.1 Framework Goals

QA-AI aims to:

- Transform requirements into structured QA artifacts.
- Provide reusable QA capabilities through independently defined skills.
- Coordinate multiple QA capabilities through workflows.
- Apply consistent QA knowledge, standards, templates, and review practices.
- Reduce dependency on platform-specific prompts or configurations.
- Support both standalone QA tasks and multi-stage QA workflows.
- Improve consistency, traceability, coverage, and maintainability of AI-assisted QA work.
- Enable the same QA framework to be evaluated across different AI runtimes.

### 1.2 Vendor-Neutral Principle

QA-AI does not define its behavior according to a specific AI platform.

Core framework behavior must remain independent of:

- AI provider.
- AI model.
- Chat interface.
- Project or workspace feature.
- Platform-specific memory mechanism.
- Platform-specific tool or plugin system.

Platform capabilities may affect how the framework is loaded or executed, but they must not redefine QA-AI skills, workflows, standards, or expected deliverables.

The expected relationship is:

```text
                    QA-AI
                       │
              Vendor-Neutral Core
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   AI Runtime A   AI Runtime B   AI Runtime N
```

### 1.3 Modular Principle

QA-AI separates responsibilities across framework components.

Each component owns a specific concern and should not duplicate responsibilities owned by another component.

This enables individual knowledge resources, skills, workflows, and supporting assets to evolve independently while preserving the overall framework contract.

### 1.4 Deliverable-Oriented Principle

QA-AI is designed to produce QA artifacts rather than merely conversational responses.

Depending on the selected capability or workflow, deliverables may include:

- Requirement analysis.
- Business rules.
- Risk analysis.
- Test scenarios.
- Coverage review.
- Test cases.
- Regression analysis.
- Test data.
- Bug reports or bug report reviews.

A conversational response may be used to communicate with the user, but the QA artifact remains the primary product of framework execution.

### 1.5 Framework Bootstrap

When QA-AI is provided to an AI runtime, `FRAMEWORK.md` must be treated as the primary framework entry point.

Before executing a QA request, the runtime should:

1. Read the framework operating rules.
2. Identify the user's QA objective.
3. Resolve the applicable workflow or skill.
4. Load only the dependencies required for that execution.

The runtime should not attempt to infer the complete QA-AI operating model from individual skill, workflow, or shared-resource files in isolation.
## 2. Framework Architecture

QA-AI separates framework definition, reusable QA intelligence, execution capabilities, orchestration, development utilities, and generated artifacts.

At runtime, the primary framework relationship is:

```text
FRAMEWORK.md
      │
      ▼
workflows/
      │
      ▼
skills/
      │
      ▼
shared/
      │
      ▼
QA Deliverables
```

The complete repository may contain additional assets for documentation, examples, evaluation, execution utilities, and generated output.

### 2.1 Core Runtime Components

The portable QA-AI Skill Pack consists of the following core components:

```text
qa-ai-skill-pack/
├── FRAMEWORK.md
├── manifest.json
├── shared/
├── skills/
└── workflows/
```

#### `FRAMEWORK.md`

Defines how an AI runtime should consume and operate the QA-AI framework.

It owns:

- Framework operating principles.
- Request resolution.
- Workflow and skill resolution rules.
- Context assembly rules.
- Execution lifecycle.
- Quality validation.
- Output behavior.
- Failure and missing-information handling.
- Portability requirements.

It does not redefine the detailed behavior of individual skills or workflows.

#### `manifest.json`

Provides machine-readable metadata describing the QA-AI Skill Pack and its primary framework locations.

The manifest supports packaging, validation, discovery, and future automation without requiring tooling to infer package structure from Markdown content.

#### `shared/`

Provides reusable QA intelligence and supporting assets.

This may include:

- Standards.
- Templates.
- Checklists.
- Prompt patterns.
- Knowledge.
- Glossary.

Shared resources support skills and workflows but do not independently orchestrate execution.

#### `skills/`

Defines atomic QA capabilities.

Each skill owns the behavior required to perform one clearly scoped QA capability, including its inputs, outputs, constraints, dependencies, and execution guidance.

Skills must remain reusable across workflows and AI runtimes.

#### `workflows/`

Defines orchestration across one or more QA skills.

A workflow determines:

- Which skills are required.
- Their execution order.
- Artifact dependencies.
- Review points.
- Final workflow outputs.

Workflow definitions must not duplicate the internal capability logic owned by individual skills.

### 2.2 Repository Components Outside the Runtime Pack

The complete QA-AI repository may additionally contain:

```text
docs/
examples/
datasets/
scripts/
output/
```

These components support framework development and usage but are not mandatory runtime dependencies of the default Skill Pack.

Their responsibilities are:

| Component | Responsibility |
|---|---|
| `docs/` | Framework architecture and project documentation |
| `examples/` | Curated examples demonstrating expected framework usage |
| `datasets/` | Evaluation, benchmark, and regression datasets |
| `scripts/` | Validation, packaging, evaluation, export, and execution utilities |
| `output/` | QA artifacts generated during actual framework usage |

### 2.3 Dependency Direction

Dependencies should flow toward reusable framework resources rather than toward AI platforms.

```text
User Request
     │
     ▼
Framework
     │
     ▼
Workflow
     │
     ▼
Skills
     │
     ▼
Shared Resources
```

The following dependency patterns should be avoided:

```text
shared/    ──X──► specific AI platform

skills/    ──X──► specific AI platform

workflows/ ──X──► specific AI platform
```

This dependency direction protects framework portability.

### 2.4 Responsibility Boundaries

Framework components must preserve the following ownership boundaries:

```text
FRAMEWORK.md
    → How QA-AI operates

workflows/
    → Which capabilities execute and in what sequence

skills/
    → How an individual QA capability is performed

shared/
    → Which reusable QA knowledge and supporting assets are applied

output/
    → Which generated QA artifacts are retained
```

When information already has a clear owner, another component should reference that owner instead of duplicating the content.

---

## 3. Operating Principles

All QA-AI execution should follow the principles defined in this section.

### 3.1 Knowledge First

QA-AI should use the framework's established knowledge, standards, templates, checklists, and terminology before relying on unsupported assumptions.

Relevant shared resources should be resolved according to the selected task, skill, and workflow.

### 3.2 Skill-Based Execution

QA activities should be executed through the appropriate defined skill whenever one exists.

The runtime should not replace a defined skill with an improvised capability simply because it can generate a plausible response.

### 3.3 Workflow-Driven Orchestration

When a request requires multiple QA capabilities, execution should follow the applicable defined workflow.

The runtime must preserve:

- Skill sequence.
- Artifact dependencies.
- Required review stages.
- Workflow output expectations.

### 3.4 Minimum Sufficient Context

The runtime should load the minimum context sufficient to execute the selected task correctly.

```text
Task
  ↓
Workflow
  ↓
Required Skills
  ↓
Required Dependencies
  ↓
Relevant Shared Resources
```

Loading unrelated knowledge should be avoided when it does not contribute to the current QA objective.

This reduces:

- Context noise.
- Conflicting instructions.
- Unnecessary token consumption.
- Irrelevant knowledge influence.

### 3.5 Evidence Over Assumption

Confirmed requirement information takes precedence over inference.

The runtime must distinguish among:

- Confirmed information.
- Derived information.
- Assumptions.
- Missing information.
- Clarification questions.

Information must not be silently invented to make an artifact appear complete.

### 3.6 Human Validation

QA-AI supports QA analysis and artifact generation but does not remove human accountability.

Human review is particularly important when execution involves:

- Ambiguous business intent.
- High-impact assumptions.
- Risk prioritization.
- Release decisions.
- Conflicting requirements.
- Incomplete business context.

### 3.7 Platform Independence

The framework defines QA behavior.

The AI runtime provides execution capability.

Platform-specific behavior must not silently modify:

- Skill responsibilities.
- Workflow sequencing.
- QA standards.
- Artifact contracts.
- Quality gates.

---

## 4. Input Contract

QA-AI supports both minimal and enriched input.

### 4.1 Required Input

The minimum input for requirement-driven execution is:

```text
Requirement
```

A requirement may be provided as:

- User story.
- Business requirement.
- Functional requirement.
- Acceptance criteria.
- Feature specification.
- Requirement document.
- Equivalent structured or unstructured requirement information.

The framework should not require the user to know internal skill or workflow names.

### 4.2 Optional Input

Execution quality may be improved when additional context is available.

Optional input may include:

- Project context.
- Business context.
- Domain information.
- Existing QA artifacts.
- Existing system behavior.
- UI designs.
- API specifications.
- Database information.
- Business constraints.
- User roles and permissions.
- Integration information.
- Known defects or historical risks.
- Requested QA artifact.
- Explicit execution scope.

Optional context should only influence execution when relevant to the selected QA objective.

### 4.3 User Objective

A user may explicitly request a QA objective.

For example:

```text
Requirement
+
"Analyze this requirement."
```

or:

```text
Requirement
+
"Generate detailed test cases."
```

The runtime should resolve the appropriate skill or workflow without requiring commands such as:

```text
Run requirement-analyzer.
```

or:

```text
Execute testcase-generation workflow.
```

Internal framework terminology should not become a mandatory user interface.

### 4.4 Standalone Execution

When the user requests a single QA capability, QA-AI may execute the corresponding standalone skill or applicable standalone workflow.

Example:

```text
Requirement
    +
"Analyze risks."
        │
        ▼
Applicable Risk Analysis Capability
        │
        ▼
Risk-Analysis.md
```

Only the dependencies required for that execution should be loaded.

### 4.5 Multi-Stage Execution

When the requested objective requires multiple dependent capabilities, QA-AI should resolve and execute the applicable workflow.

A multi-stage execution progressively transforms requirement information into structured QA artifacts.

Example:

```text
Requirement
      │
      ▼
Requirement Analysis
      │
      ▼
Business Rules
      │
      ▼
Risk Analysis
      │
      ▼
Test Scenarios
      │
      ▼
Test Cases
      │
      ▼
Coverage Review
```

Intermediate artifacts should be reused by downstream skills instead of repeatedly deriving the same information from the original requirement.

The execution order must follow the applicable workflow and the input/output contracts of the participating skills.

For example:

```text
Test Scenarios
      │
      ▼
Testcase Generator
      │
      ▼
Structured Test Case Model
      │
      ▼
Coverage Reviewer
      │
      ▼
Structured Coverage Assessment
```

A downstream capability must not be executed before its required upstream artifact is available.

The runtime may perform prerequisite analysis internally when required, but it should only present artifacts that are requested by the user or defined as deliverables by the selected workflow.

---

## 5. Request Resolution

Before generating QA content, the runtime must determine what the user is asking QA-AI to accomplish.

Request resolution follows:

```text
User Request
     │
     ▼
Identify QA Objective
     │
     ▼
Determine Execution Mode
     │
     ├── Standalone Capability
     │
     └── Multi-Stage Workflow
     │
     ▼
Resolve Framework Component
```

For canonical testcase generation, the dependency chain is:

`Requirement ? Requirement Analysis ? Business Rules ? Test Scenarios ? Test Cases`.

Risk Analysis and Coverage Review remain valid QA-AI capabilities and may
participate when required by the selected workflow or QA objective, but they
must not be interpreted as mandatory stages of the canonical testcase-generation
dependency chain.

### 5.1 Identify the QA Objective

The runtime should identify:

- Requested artifact.
- Requested QA activity.
- Available requirement/context.
- Explicit scope.
- Relevant constraints.

If the user does not explicitly name an artifact, the objective should be derived from the user's requested outcome rather than from arbitrary assumptions.

### 5.2 Determine Execution Mode

QA-AI supports two primary execution modes.

#### Standalone Mode

Use when the objective can be fulfilled by one independently executable QA capability.

```text
Request
   ↓
Skill / Standalone Workflow
   ↓
Artifact
```

#### Workflow Mode

Use when the requested outcome depends on multiple capabilities or intermediate artifacts.

```text
Request
   ↓
Workflow
   ↓
Skill A
   ↓
Artifact A
   ↓
Skill B
   ↓
Artifact B
   ↓
Final Deliverable
```

### 5.3 Prefer Defined Framework Behavior

When QA-AI already defines a suitable skill or workflow, the runtime should use it.

Execution priority is:

```text
Defined Workflow
      ↓
Defined Skill
      ↓
Supported Framework Composition
      ↓
Unsupported Request Handling
```

The runtime should not create a new implicit workflow when an existing workflow already covers the objective.

### 5.4 Request Scope

The runtime must respect explicit user scope.

For example, if the user requests only test scenarios:

```text
Requirement
      ↓
Required upstream analysis
      ↓
Test Scenarios
```

User scope controls the deliverables that are presented, but it does not automatically remove internal prerequisite analysis required by the selected skill or workflow.

Required internal analysis may be performed without exposing additional artifacts unless the user requests them or the workflow defines them as deliverables.

### 5.5 Unsupported Requests

If the requested QA activity is not supported by an existing skill or workflow, the runtime should:

1. Identify that no defined capability fully covers the request.
2. Avoid pretending that an existing skill provides unsupported behavior.
3. Explain the unsupported or partially supported scope.
4. Use supported capabilities only where applicable.
5. Preserve the framework's standards and no-fabrication principles.

Unsupported requests should not cause the runtime to silently redefine the QA-AI framework.
## 6. Workflow Resolution

Workflow resolution determines whether an existing QA-AI workflow should be used to satisfy the requested objective.

A workflow should be selected when the requested outcome requires multiple coordinated QA capabilities or when QA-AI already defines a standardized execution path for that objective.

The general resolution process is:

```text
QA Objective
     │
     ▼
Discover Applicable Workflows
     │
     ▼
Evaluate Workflow Scope
     │
     ▼
Select Best Matching Workflow
     │
     ▼
Resolve Required Skills
     │
     ▼
Execute Workflow
```

### 6.1 Workflow Discovery

The runtime should inspect the available definitions under:

```text
workflows/
```

Workflow discovery should consider:

- Workflow purpose.
- Supported inputs.
- Expected outputs.
- Required skills.
- Preconditions.
- Execution scope.
- Artifact dependencies.

Workflow selection must be based on declared capability rather than workflow name alone.

### 6.2 Workflow Selection

When multiple workflows could apply, the runtime should prefer the workflow that most directly satisfies the user's requested outcome with the least unnecessary execution.

Selection should consider:

1. User objective.
2. Requested deliverables.
3. Available inputs.
4. Workflow scope.
5. Required intermediate artifacts.
6. Explicit user constraints.

A broader workflow should not be selected when a narrower defined workflow fully satisfies the request.

### 6.3 Workflow Precedence

When a defined workflow covers the requested objective, the workflow definition takes precedence over an improvised sequence of skills.

```text
Defined Workflow
       │
       ▼
Declared Skill Sequence
       │
       ▼
Execution
```

The runtime must not silently:

- Reorder mandatory skills.
- Remove required review stages.
- Replace required skills with improvised reasoning.
- Introduce unrelated skills.
- Change declared workflow outputs.

Any optional behavior defined by the workflow should remain optional according to that workflow's rules.

### 6.4 Workflow Inputs

Before execution, the runtime should verify that required workflow inputs are available.

Inputs may originate from:

- The user's requirement.
- User-provided supporting context.
- Existing QA artifacts.
- Upstream workflow artifacts.
- Previously completed framework execution.

If a required input is missing, the runtime should follow the missing-information rules defined by this framework and the selected workflow.

### 6.5 Workflow Outputs

Workflow outputs are determined by the workflow definition.

Outputs may include:

- Intermediate artifacts used by downstream skills.
- Review artifacts.
- Final user-facing deliverables.

Intermediate artifacts should not automatically be presented as final deliverables unless requested or defined as workflow outputs.

---

## 7. Skill Resolution

Skill resolution identifies the atomic QA capabilities required to perform the selected task or workflow.

Skills are resolved from:

```text
skills/
```

The runtime should treat skill definitions as authoritative capability contracts.

### 7.1 Skill Discovery

Skill discovery should consider:

- Skill purpose.
- Supported QA capability.
- Required inputs.
- Optional inputs.
- Expected outputs.
- Dependencies.
- Constraints.

The runtime should select skills according to capability match rather than keyword similarity alone.

### 7.2 Standalone Skill Resolution

For a standalone QA request:

```text
User Objective
      │
      ▼
Capability Match
      │
      ▼
Applicable Skill
      │
      ▼
Skill Execution
```

The runtime should load only the dependencies necessary for that skill.

### 7.3 Workflow Skill Resolution

When executing a workflow, the workflow determines the required skills.

```text
Workflow
   │
   ├── Skill A
   ├── Skill B
   └── Skill C
```

The runtime should not independently replace a declared workflow skill simply because another skill appears related.

### 7.4 Skill Input Validation

Before executing a skill, verify:

- Required inputs exist.
- Input artifacts are valid for the skill.
- Required upstream artifacts are available.
- Relevant dependencies can be resolved.

If required information is unavailable, execution should follow the applicable clarification or assumption rules.

### 7.5 Skill Dependencies

A skill may depend on reusable framework assets such as:

```text
Skill
 │
 ├── Knowledge
 ├── Standards
 ├── Templates
 ├── Checklists
 ├── Prompt Patterns
 └── Glossary
```

Dependencies should be resolved from their authoritative locations under `shared/`.

The skill should reference these resources rather than duplicate their contents.

### 7.6 Skill Output Contract

Every skill execution must satisfy the output contract defined by that skill.

The runtime should verify:

- Required sections are present.
- Required information is represented.
- Output structure is correct.
- Applicable standards are followed.
- Required template is respected.

A plausible response that violates the skill's output contract is not considered successful skill execution.

---

## 8. Context Assembly

Context assembly prepares the minimum set of framework information required to execute the resolved skill or workflow correctly.

Context assembly occurs after resolution and before execution.

```text
Resolved Task
      │
      ▼
Workflow Definition
      │
      ▼
Skill Definitions
      │
      ▼
Declared Dependencies
      │
      ▼
Relevant Shared Resources
      │
      ▼
Execution Context
```

### 8.1 Context Sources

Execution context may include:

#### User Context

- Requirement.
- Requested objective.
- Business context.
- Project constraints.
- Supporting specifications.
- Existing QA artifacts.

#### Framework Context

- Selected workflow.
- Required skills.
- Relevant knowledge.
- Applicable standards.
- Templates.
- Checklists.
- Prompt patterns.
- Glossary terms.

### 8.2 Dependency-Driven Loading

Framework context should primarily be resolved through declared dependencies.

For example:

```text
Selected Workflow
       │
       ▼
Required Skills
       │
       ▼
Skill Dependencies
       │
       ├── Standard
       ├── Template
       ├── Checklist
       └── Knowledge
```

This is preferred over indiscriminately loading the complete QA-AI repository.

### 8.3 Context Relevance

A resource should be loaded when it contributes directly to:

- Understanding the task.
- Executing a required capability.
- Applying an applicable QA rule.
- Producing the required artifact.
- Validating output quality.

Unrelated resources should remain outside the active execution context.

### 8.4 Context Precedence

When context sources conflict, use the following general precedence:

```text
Explicit User Requirement / Confirmed Project Information
                        │
                        ▼
Defined Workflow and Skill Contracts
                        │
                        ▼
Applicable QA-AI Standards
                        │
                        ▼
Relevant Project / Domain Knowledge
                        │
                        ▼
General QA-AI Knowledge
                        │
                        ▼
Assumption
```

This precedence does not authorize the runtime to override explicit framework constraints.

Conflicts that materially affect correctness should be surfaced rather than silently resolved.

### 8.5 Context Reuse

Artifacts generated earlier in the execution lifecycle should be reused when they provide validated inputs for downstream skills.

Example:

```text
Requirement
     │
     ▼
Requirement Analysis
     │
     ▼
Business Rules
     │
     ▼
Test Scenarios
```

The scenario-generation stage should consume validated upstream artifacts rather than independently reinterpret the requirement from the beginning.

### 8.6 Context Minimization

The runtime should avoid loading unnecessary framework resources.

Context minimization helps:

- Reduce irrelevant influence.
- Reduce instruction conflicts.
- Preserve execution focus.
- Improve portability across runtimes with different context capabilities.
- Reduce unnecessary processing.

Context minimization must not remove dependencies required for correct execution.

---

## 9. Execution Lifecycle

All QA-AI executions follow a common lifecycle:

```text
Understand
    │
    ▼
Resolve
    │
    ▼
Load
    │
    ▼
Execute
    │
    ▼
Review
    │
    ▼
Deliver
```

### 9.1 Understand

Determine:

- User objective.
- Requirement scope.
- Available context.
- Requested deliverables.
- Explicit constraints.
- Potential information gaps.

No QA artifact should be generated before the execution objective is sufficiently understood.

### 9.2 Resolve

Resolve the appropriate:

- Workflow.
- Skills.
- Dependencies.
- Expected outputs.

Resolution establishes the execution plan.

### 9.3 Load

Assemble:

- User context.
- Workflow definition.
- Skill definitions.
- Relevant shared resources.
- Existing upstream artifacts.

Only context necessary for correct execution should be loaded.

### 9.4 Execute

Execute the selected skills according to:

- Skill contracts.
- Workflow sequence.
- Declared dependencies.
- Applicable standards.
- Relevant QA knowledge.

Intermediate artifacts should be preserved when required by downstream stages.

### 9.5 Review

Before delivery, generated artifacts must pass the applicable quality validation.

Review may include:

- Output contract validation.
- Coverage review.
- Standards compliance.
- Template compliance.
- Internal consistency.
- Traceability.
- Assumption review.

Review is part of framework execution, not an optional cosmetic step.

### 9.6 Deliver

Only artifacts that satisfy applicable execution and quality requirements should be treated as final QA-AI deliverables.

Delivery should:

- Respect requested scope.
- Follow output standards.
- Preserve traceability where required.
- Identify unresolved assumptions or clarification items.
- Avoid presenting incomplete artifacts as fully validated outputs.

---

## 10. Artifact Dependency Management

QA-AI workflows may generate multiple artifacts that depend on one another.

The framework should preserve these relationships throughout execution.

### 10.1 Artifact Dependency Chain

A typical dependency chain may look like:

```text
Requirement
     │
     ▼
Requirement Analysis
     │
     ▼
Business Rules
     │
     ▼
Risk Analysis
     │
     ▼
Test Scenarios
     │
     ▼
Test Cases
     │
     ▼
Coverage Review
```

The exact chain is determined by the selected workflow.

This example must not be interpreted as a mandatory sequence for every QA-AI execution.

### 10.2 Upstream Artifacts

An upstream artifact provides validated information required by a downstream capability.

Examples may include:

```text
Requirement Analysis
        ↓
Scenario Generation
```

or:

```text
Test Scenarios
        ↓
Test Case Generation
```

When an upstream artifact exists and remains valid, downstream skills should consume it rather than recreate equivalent analysis.

### 10.3 Artifact Reuse

Artifact reuse improves:

- Consistency.
- Traceability.
- Execution efficiency.
- Cross-skill alignment.

The runtime should preserve established information unless new evidence requires it to be reconsidered.

### 10.4 Artifact Validation Before Reuse

Generated artifacts should not automatically become trusted dependencies merely because they were produced earlier.

Before reuse, the runtime should verify that the artifact:

- Completed its required execution stage.
- Meets its output contract.
- Does not contain unresolved blocking issues.
- Is still applicable to the current scope.

An invalid upstream artifact should not silently propagate into downstream deliverables.

### 10.5 Intermediate and Final Artifacts

QA-AI distinguishes between:

**Intermediate artifacts**

Used primarily to support downstream execution.

**Final artifacts**

Defined as user-facing deliverables by the selected workflow or requested scope.

An artifact may serve both roles.

For example:

```text
Test Scenarios
     │
     ├── Final deliverable
     │
     └── Input to Test Case Generation
```

### 10.6 Traceability

Where supported by the applicable skill, workflow, standard, or template, QA-AI should preserve traceability among:

```text
Requirement
    ↕
Business Rule
    ↕
Risk
    ↕
Scenario
    ↕
Test Case
```

Traceability should use stable identifiers when defined by the relevant artifact contracts.

The framework must not invent arbitrary identifier schemes when an authoritative naming or output standard already exists.

### 10.7 Artifact Change Propagation

If an upstream artifact changes materially during the same execution lifecycle, affected downstream artifacts should be reconsidered.

```text
Upstream Change
      │
      ▼
Identify Dependent Artifacts
      │
      ▼
Determine Impact
      │
      ▼
Re-execute Affected Stages
      │
      ▼
Revalidate Outputs
```

Unaffected stages do not need to be regenerated solely because another artifact changed.

### 10.8 Artifact Integrity

The framework should prevent contradictions across generated artifacts.

For example, a confirmed business rule should not be represented differently in:

- Risk analysis.
- Test scenarios.
- Test cases.

When contradictions are detected, the runtime should resolve them against the authoritative upstream source or surface the conflict when resolution requires human input.
## 11. Quality Validation

Quality validation is a mandatory stage of QA-AI execution.

Generated content must not be considered a final QA deliverable solely because a skill or workflow has completed generation.

The general validation process is:

```text
Generated Artifact
       │
       ▼
Output Contract Validation
       │
       ▼
Standards & Template Validation
       │
       ▼
Content Quality Validation
       │
       ▼
Cross-Artifact Consistency
       │
       ▼
Final Deliverable
```

The exact validation activities depend on the selected skill, workflow, artifact type, and applicable framework resources.

### 11.1 Output Contract Validation

Every generated artifact must satisfy the output contract defined by its owning skill or workflow.

Validation should confirm:

- Required sections are present.
- Required fields are represented.
- Expected artifact structure is followed.
- Required information has not been omitted.
- Unsupported information has not been introduced.
- The artifact satisfies the requested scope.

Failure to satisfy a required output contract means the artifact is not complete.

### 11.2 Standards Compliance

Applicable standards under:

```text
shared/standards/
```

must be respected.

Depending on the artifact, validation may include:

- Naming.
- Documentation structure.
- Metadata.
- Output conventions.
- Prompt-related conventions where applicable.

Standards should be referenced from their authoritative definitions rather than reproduced in the framework.

### 11.3 Template Compliance

When an applicable template exists under:

```text
shared/templates/
```

the generated artifact should follow that template.

Templates define artifact structure.

Skills define capability behavior.

The framework coordinates their use.

```text
Skill
   +
Template
   +
Input
   │
   ▼
Structured Artifact
```

A runtime should not substitute its preferred formatting when an authoritative QA-AI template applies.

### 11.4 Checklist Validation

Applicable checklists under:

```text
shared/checklists/
```

should be used as quality gates when required by the selected skill or workflow.

Checklist validation may identify:

- Missing coverage.
- Missing information.
- Structural problems.
- Inconsistent terminology.
- Incomplete expected results.
- Missing traceability.
- Other artifact-specific quality gaps.

### 11.5 Coverage Validation

When coverage validation is applicable, QA-AI should evaluate whether the generated artifact sufficiently represents the confirmed requirement and relevant QA scope.

Coverage validation should use the appropriate framework capability when one exists rather than relying only on an informal completeness judgment.

### 11.6 Internal Consistency

Generated content should remain internally consistent.

Examples include:

- The same business rule should not have conflicting interpretations.
- Risk analysis should remain aligned with confirmed requirement behavior.
- Test scenarios should not contradict upstream business rules.
- Test cases should remain aligned with approved scenarios.
- Terminology should remain consistent across related artifacts.

### 11.7 Cross-Artifact Consistency

For multi-artifact execution, validation should consider the artifact set as a whole.

```text
Requirement Analysis
        │
        ▼
Business Rules
        │
        ▼
Risk Analysis
        │
        ▼
Test Scenarios
        │
        ▼
Test Cases
```

A downstream artifact that conflicts with a validated upstream artifact should be corrected or flagged before delivery.

### 11.8 Validation Result

An artifact may reach one of the following logical outcomes:

```text
PASS
    → Ready for delivery

PASS WITH OPEN ITEMS
    → Deliverable with clearly identified non-blocking
      assumptions or clarification items

FAIL
    → Not ready for final delivery
```

These outcomes describe framework validation behavior and do not replace any artifact status convention defined elsewhere in QA-AI standards or templates.

---

## 12. Missing Information and Assumptions

QA-AI must explicitly manage missing, ambiguous, and inferred information.

The framework must not silently fabricate information to complete an artifact.

### 12.1 Information Classification

Relevant information should be distinguishable as:

- Confirmed information.
- Derived information.
- Assumption.
- Missing information.
- Ambiguous information.
- Conflicting information.

This distinction should be preserved when it materially affects QA analysis or downstream artifacts.

### 12.2 Missing Information Detection

Missing information should be identified when required inputs cannot be determined from:

- User-provided requirements.
- Supporting project context.
- Valid upstream artifacts.
- Applicable framework knowledge.

General QA knowledge must not be treated as confirmed project-specific behavior.

### 12.3 Blocking Information Gaps

An information gap is blocking when proceeding would require inventing behavior that materially affects the correctness of the requested artifact.

In this case:

```text
Missing Required Information
           │
           ▼
Cannot Proceed Reliably
           │
           ▼
Request Clarification
```

The runtime should ask for the minimum clarification necessary to continue.

### 12.4 Non-Blocking Information Gaps

Execution may continue when the missing information does not prevent a useful and reliable artifact from being produced.

In that case:

```text
Missing Information
        │
        ▼
Proceed Safely
        │
        ▼
Record Gap / Assumption
        │
        ▼
Generate Artifact
```

The unresolved item should remain visible when relevant to interpretation or execution.

### 12.5 Assumption Rules

An assumption may be used only when:

- It is necessary to proceed.
- It does not contradict confirmed information.
- It is clearly identified as an assumption.
- Its impact can be understood by the reviewer.
- The applicable skill or workflow permits execution with assumptions.

Assumptions must not be presented as confirmed business rules.

### 12.6 Clarification Questions

Clarification questions should be:

- Specific.
- Relevant to the current QA objective.
- Actionable.
- Non-duplicative.
- Prioritized when multiple questions exist.

The runtime should avoid blocking execution with questions that do not materially affect the requested artifact.

### 12.7 Conflicting Information

When confirmed sources conflict:

```text
Conflict Detected
      │
      ▼
Can Authoritative Source Be Determined?
      │
   ┌──┴──┐
  Yes    No
   │      │
   ▼      ▼
Use      Surface Conflict
Source   for Clarification
```

The runtime must not silently choose the interpretation that is easiest to test.

### 12.8 No-Fabrication Principle

QA-AI must not invent:

- Business rules.
- Acceptance criteria.
- System behavior.
- User permissions.
- Validation rules.
- API behavior.
- Database behavior.
- Integration behavior.

when such information is required to be project-specific and is not supported by available context.

---

## 13. Output Contract

QA-AI outputs are structured QA deliverables produced according to the selected skill or workflow.

### 13.1 Artifact Selection

The requested QA objective determines which artifacts should be delivered.

Examples include:

```text
Requirement Analysis Request
        ↓
Requirement-Analysis.md
```

or:

```text
Test Case Generation Request
        ↓
Required Internal/Upstream Analysis
        ↓
Test-Cases.md
```

or:

```text
Full QA Workflow
        ↓
Feature Artifact Package
```

The runtime should not expose every intermediate artifact unless required by the workflow or requested by the user.

### 13.2 Standalone Output

Standalone execution should produce the artifact defined by the selected capability.

Examples may include:

```text
Requirement-Analysis.md
Risk-Analysis.md
Test-Scenarios.md
Test-Cases.md
Regression-Analysis.md
Test-Data.md
```

The authoritative artifact names and formats are governed by applicable QA-AI standards and templates.

### 13.3 Feature Package Output

A multi-stage workflow may produce a feature package such as:

```text
<project-name>/
└── <feature-id>/
    ├── input/
    │   └── Requirement.md
    │
    ├── Requirement-Analysis.md
    ├── Business-Rules.md
    ├── Risk-Analysis.md
    ├── Test-Scenarios.md
    ├── Test-Cases.md
    ├── Coverage-Review.md
    ├── Regression-Analysis.md
    ├── Test-Data.md
    └── metadata.json
```

The exact package contents depend on the selected workflow.

Artifacts that are not part of the workflow should not be created merely to fill the package structure.

### 13.4 Output Location

When QA-AI is executed in a repository environment that supports artifact persistence, generated deliverables should follow the applicable structure under:

```text
output/
```

Standalone artifacts and project-level packages should follow the output architecture defined by the repository.

When the AI runtime cannot directly write to the repository, it should still generate content that conforms to the same artifact contract so that it can be saved or exported without structural reinterpretation.

### 13.5 Output Format

Output format must follow:

```text
Skill Output Contract
        +
Applicable Template
        +
Output Standard
```

Platform-specific presentation preferences must not override authoritative QA-AI artifact requirements.

### 13.6 Final Deliverable Rules

A final deliverable should:

- Satisfy the requested scope.
- Meet its skill or workflow output contract.
- Follow applicable standards.
- Follow applicable templates.
- Pass required quality validation.
- Preserve relevant traceability.
- Clearly identify unresolved assumptions or open clarification items.
- Avoid unsupported project-specific claims.

---

## 14. Failure Handling

QA-AI should fail predictably and transparently when framework execution cannot be completed correctly.

Failure handling should preserve useful completed work whenever possible without representing incomplete execution as successful.

### 14.1 Missing Skill

If no defined skill supports a required capability:

1. Identify the unsupported capability.
2. Do not pretend an unrelated skill supports it.
3. Continue supported portions only when they remain useful independently.
4. Report the limitation.

### 14.2 Missing Workflow

If no workflow directly supports the requested multi-stage objective:

- Use an explicitly supported framework composition only when permitted by existing skill contracts.
- Do not silently create a permanent new workflow definition.
- Identify that execution is using a temporary supported composition rather than a defined workflow.

If reliable composition cannot be determined, surface the unsupported scope.

### 14.3 Missing Dependency

If a required dependency cannot be resolved:

```text
Missing Dependency
       │
       ▼
Is Dependency Required?
     ┌────┴────┐
    Yes        No
     │          │
     ▼          ▼
Block or      Continue
Degrade       Safely
Execution
```

The runtime should identify the missing dependency and its effect on output quality.

### 14.4 Invalid Input

If required input is invalid, unreadable, unsupported, or insufficient:

- Identify the affected input.
- Explain why it cannot be used.
- Request corrected input when necessary.
- Preserve unaffected valid inputs.

### 14.5 Conflicting Instructions

When instructions conflict, the runtime should preserve framework ownership boundaries and applicable instruction precedence.

A platform-specific preference must not override a core QA-AI requirement.

Conflicts that cannot be safely resolved should be surfaced.
When framework instructions conflict, ownership should be resolved according to responsibility:

1. Framework operating rules — `FRAMEWORK.md`
2. Selected workflow contract — `workflows/`
3. Selected skill contract — `skills/`
4. Applicable standards — `shared/standards/`
5. Applicable templates and checklists — `shared/`
6. Supporting knowledge — `shared/knowledge/`

A higher-level component governs orchestration and boundaries, while a lower-level authoritative component remains responsible for its specialized content.

Instruction precedence must not be used to overwrite confirmed project requirements or user-provided business facts.

### 14.6 Partial Execution

If execution fails after some stages have completed:

```text
Completed Artifacts
       │
       ├── Valid
       │     ↓
       │   Preserve
       │
       └── Invalid / Dependent on Failure
             ↓
           Mark Incomplete
```

Valid completed artifacts may be retained.

Artifacts affected by the failure must not be presented as fully validated deliverables.

### 14.7 Failure Reporting

Failure reporting should identify:

- Failed stage.
- Cause.
- Affected artifacts.
- Preserved artifacts.
- Required user action, if any.
- Whether execution can safely continue.

---

## 15. Portability Rules

QA-AI is designed to preserve comparable QA behavior across compatible AI runtimes.

### 15.1 Core Behavior Ownership

QA-AI behavior is defined by:

```text
FRAMEWORK.md
+
workflows/
+
skills/
+
shared/
```

It is not defined by the AI platform.

### 15.2 Runtime Responsibilities

A compatible AI runtime should be able to:

- Read the framework entry point.
- Access required skill and workflow definitions.
- Access relevant shared resources.
- Preserve sufficient execution context.
- Follow framework instructions.
- Generate structured outputs.

Different runtimes may implement these capabilities differently.

### 15.3 Platform-Specific Logic

Core QA-AI runtime assets must not contain logic such as:

```text
If ChatGPT → execute differently

If Claude → change workflow

If Platform X → use different QA standard
```

Platform-specific mechanisms may be used to load or expose the same framework, but they must not redefine QA behavior.

### 15.4 Cross-Platform Consistency

Given:

```text
Same Requirement
        +
Same QA-AI Skill Pack
        +
Equivalent User Objective
```

compatible runtimes should produce **comparable QA behavior**.

Comparable behavior means consistency in:

- Selected QA capability.
- Workflow intent.
- Application of business rules.
- QA coverage principles.
- Artifact structure.
- Quality gates.
- Treatment of assumptions.
- Treatment of missing information.

It does not require identical wording.

### 15.5 Runtime Limitations

AI runtimes may differ in:

- Context capacity.
- File access.
- Persistent memory.
- Tool availability.
- Artifact creation.
- Instruction handling.

Such limitations should affect the **execution mechanism**, not the QA-AI capability definition.

If a runtime cannot satisfy a required framework behavior, the limitation should be surfaced rather than silently changing the framework contract.

### 15.6 Portability Validation

Cross-platform portability should be evaluated using:

```text
Common Requirement
       │
       ▼
Same Skill Pack
       │
       ├── Runtime A
       └── Runtime B
             │
             ▼
Compare
   ├── Coverage
   ├── Structure
   ├── Consistency
   ├── Assumption Handling
   └── Quality Compliance
```

Portability validation belongs to framework evaluation and does not require platform-specific QA logic in the Skill Pack.

---

## 16. Framework Completion Criteria

An execution is complete only when the selected task or workflow has satisfied its required completion conditions.

### 16.1 Execution Completion

Execution should confirm that:

- The requested QA objective was resolved.
- Required workflow or skill execution completed.
- Required dependencies were available or appropriately handled.
- Required artifacts were generated.
- Required quality validation completed.
- Blocking failures were resolved or clearly reported.

### 16.2 Artifact Completion

A final artifact should satisfy:

```text
Output Contract
      +
Applicable Standards
      +
Applicable Template
      +
Required Validation
      =
Complete Artifact
```

Generation alone does not establish completion.

### 16.3 Open Items

Non-blocking items may remain when clearly identified.

Examples include:

- Assumptions requiring later confirmation.
- Non-blocking clarification questions.
- Known scope exclusions.
- External dependencies unavailable during execution.

Open items must not be hidden merely to produce a clean-looking artifact.

### 16.4 Workflow Completion

A workflow is complete when:

- Required stages completed.
- Required artifact dependencies were satisfied.
- Required review stages completed.
- Final outputs passed applicable quality gates.
- Blocking issues were resolved or execution was explicitly reported as incomplete.

### 16.5 Completion Status

At framework level, execution may be considered:

```text
COMPLETE

COMPLETE WITH OPEN ITEMS

INCOMPLETE
```

These framework-level outcomes describe execution completeness and must not replace artifact-specific statuses defined by templates or standards.

---

## 17. Repository References

`FRAMEWORK.md` defines how QA-AI operates but does not duplicate the detailed contracts maintained by other framework components.

The following locations are authoritative for their respective responsibilities.

### 17.1 Shared Resources

```text
shared/
```

Provides reusable QA intelligence and supporting resources.

Primary areas include:

```text
shared/
├── standards/
├── templates/
├── checklists/
├── prompt-patterns/
├── knowledge/
└── glossary/
```

### 17.2 Skills

```text
skills/
```

Provides atomic QA capability definitions.

Skill definitions are authoritative for:

- Capability scope.
- Required inputs.
- Expected outputs.
- Skill-specific dependencies.
- Skill constraints.
- Skill execution behavior.

### 17.3 Workflows

```text
workflows/
```

Provides multi-skill orchestration definitions.

Workflow definitions are authoritative for:

- Workflow scope.
- Required skills.
- Skill sequence.
- Artifact dependencies.
- Review stages.
- Workflow outputs.

### 17.4 Output

```text
output/
```

Provides the repository location for generated QA deliverables when artifact persistence is available.

Output structure is governed by applicable repository standards and output conventions.

### 17.5 Manifest

```text
manifest.json
```

Provides machine-readable metadata for the portable QA-AI Skill Pack.

The manifest supports framework discovery, packaging, validation, and automation.

### 17.6 Framework Entry Point

```text
FRAMEWORK.md
```

is the authoritative entry point for operating the QA-AI Skill Pack.

A compatible runtime should begin framework discovery here and resolve detailed behavior through the referenced workflows, skills, and shared resources rather than attempting to infer QA-AI behavior from repository structure alone.