# Domain Fixtures

## Fixture Metadata

- Fixture Model ID: `FIXTURE-MODEL-DOMAIN-001`
- Fixture Type: `Domain`
- Scope: `QA-AI Controlled Business-Domain Context`
- Status: `Approved`
- Purpose: Define reusable and deterministic domain fixtures for QA-AI testing, evaluation, examples, and benchmark execution.

---

## Purpose

This document defines the canonical domain fixture model for QA-AI.

Domain fixtures provide controlled business-domain context that helps QA-AI understand terminology, entity meaning, classifications, status values, role concepts, and other stable domain information relevant to a QA task.

They may support activities such as:

- Requirement analysis
- Business-rule extraction
- Risk analysis
- Scenario generation
- Test-case generation
- Regression analysis
- Test-data generation
- Evaluation
- Benchmark execution
- Cross-platform comparison
- Framework regression testing

A domain fixture represents controlled contextual knowledge.

It is not:

- A requirement
- A source of feature-specific behavior
- A business-rule artifact
- A complete enterprise domain model
- A production data dictionary
- A generated QA artifact
- A benchmark result

---

## Fixture Role in QA-AI

The canonical relationship is:

`Requirement Dataset + Domain Fixture → QA-AI Execution → Generated Artifact`

For evaluation:

`Requirement + Domain Fixture → QA-AI Execution → Artifact → Evaluation`

For benchmarking:

`Same Dataset + Same Domain Fixture Version + Compatible Evaluation Configuration → Comparable Execution`

Domain fixtures help QA-AI interpret source information consistently without requiring each requirement to redefine stable domain concepts.

---

## Domain Fixture Objective

A domain fixture should provide enough controlled domain context to prevent ambiguity while avoiding feature-specific behavior that belongs in the requirement.

A fixture may define:

- Domain terminology
- Entity definitions
- Role definitions
- Stable classifications
- Status vocabulary
- Identifier concepts
- Entity relationships
- Value sets
- Domain-level constraints
- Semantic distinctions
- Common domain assumptions explicitly approved for the evaluation context

Only context required for the intended QA task should be included.

---

## Fixture Design Principles

Canonical domain fixtures should be:

### Source-Supported

Every domain definition must come from an authoritative or explicitly approved source.

### Stable

Fixtures should contain concepts expected to remain stable across multiple feature requirements.

### Minimal

Only relevant contextual information should be included.

### Explicit

Important semantic distinctions should be written directly.

### Reusable

Domain context should be reusable across datasets that operate within the same business domain.

### Traceable

Each fixture should have a stable identifier, version, and source reference.

### Non-Behavioral by Default

A domain fixture should not silently define feature-specific workflows or acceptance behavior.

### Platform-Neutral

Domain semantics must remain independent of the AI execution platform.

---

## Fixture Scope

Domain fixtures may represent:

- One domain concept
- A related domain concept group
- Entity vocabulary
- Role vocabulary
- Status vocabulary
- Business classification
- Identifier semantics
- Stable relationship definitions

Examples include:

- Authentication
- Product
- Order
- Inventory
- Import Permit
- Product Request
- Loyalty
- Booking

The fixture should not attempt to model the entire business unless explicitly required.

---

## Canonical Fixture Structure

A reusable domain fixture should contain enough information to identify:

1. Fixture metadata
2. Domain scope
3. Terms
4. Entities
5. Roles
6. Classifications
7. Status values
8. Relationships
9. Known stable constraints
10. Related fixtures
11. Source references
12. Fixture boundaries

Sections that do not apply may be omitted.

Unknown domain behavior must not be filled with assumptions.

---

## Fixture Identification

Each domain fixture should have a stable identifier.
### Fixture Model ID vs Fixture ID

The fixture model and fixture instances use separate identifier namespaces.

- `Fixture Model ID` identifies this canonical fixture specification.
- `Fixture ID` identifies a concrete domain fixture instance created from the model.

The canonical domain fixture model uses:

`FIXTURE-MODEL-DOMAIN-001`

Concrete domain fixture instances use the pattern defined below.

These identifiers must not be treated as interchangeable.
Recommended pattern:

`DOMAIN-FIX-<DOMAIN>-<NUMBER>`

Examples:

- `DOMAIN-FIX-AUTH-001`
- `DOMAIN-FIX-ORDER-001`
- `DOMAIN-FIX-INVENTORY-001`
- `DOMAIN-FIX-PERMIT-001`

The identifier should remain stable while the semantic domain context remains unchanged.

---

## Fixture Versioning

A domain fixture should be versioned when domain meaning changes materially.

Examples include:

- Term definition changes
- Entity meaning changes
- Role responsibility changes
- Status vocabulary changes
- Classification changes
- Entity relationship changes
- Stable domain constraint changes

Formatting-only documentation changes do not necessarily require a semantic fixture version change.

Any material fixture change requires benchmark compatibility review.

---

## Domain Scope

A fixture should clearly identify the domain it describes.

Example:

    domain:
      id: import-permit
      name: Import Permit Management
      purpose: Manage import-permit coverage and approval information.

The scope should be narrow enough that readers understand what context is authoritative.

---

## Term Definition

Domain fixtures may define important terms.

Example:

    terms:
      UPN:
        definition: Unique Product Number used to identify a product.

      Device Family:
        definition: A grouping of related medical devices managed under a family-level permit.

Definitions should preserve authoritative terminology.

Do not replace domain terms with generalized synonyms when the distinction matters.

---

## Acronyms

Acronyms may be expanded when their meanings are explicitly known.

Example:

    acronyms:
      UPN: Unique Product Number
      RA: Regulatory Affairs

An acronym must not be expanded based only on guesswork.

If the meaning is unknown, leave it unresolved.

---

## Entity Definition

A domain fixture may define stable business entities.

Example:

    entities:
      ImportPermit:
        description: Approval record that permits defined products or product families to be imported.

      ProductRequest:
        description: Business request representing products that require processing or allocation.

Entity definitions describe what a concept represents.

They should not automatically define implementation models or database tables.

---

## Entity Attributes

Stable conceptual attributes may be included when authoritative.

Example:

    entity:
      Product:
        attributes:
          - UPN
          - Product Name
          - Division

These are domain concepts.

They do not automatically imply:

- UI fields
- API fields
- Database columns

Those mappings belong to the applicable technical fixture when known.

---

## Entity Relationships

Stable domain relationships may be represented.

Example:

    relationships:
      - from: ProductRequest
        to: Product
        relation: references

      - from: ImportPermit
        to: Product
        relation: covers

Relationships should describe domain semantics without inventing implementation cardinality unless authoritative.

---

## Role Definition

Domain fixtures may define stable user or business roles.

Example:

    roles:
      RA:
        name: Regulatory Affairs
        description: Role responsible for regulatory permit-related activities.

      IAS:
        name: Inventory Administration Staff
        description: Role involved in inventory and product-request processing.

A role definition does not automatically define every permission available to that role.

Feature-specific authorization belongs in the requirement or a dedicated fixture when explicitly defined.

---

## Role Versus Permission

Role meaning and permission behavior must remain separate.

Example:

    role:
      RA:
        description: Regulatory Affairs user.

does not automatically imply:

    permissions:
      - create
      - edit
      - delete

Permissions should only be included when supported by authoritative domain or feature information.

---

## Classification Fixtures

Stable business classifications may be represented.

Example:

    classifications:
      request_type:
        values:
          - Training
          - Others
          - Rent Out

Classifications should not be extended with additional values merely because they seem plausible.

---

## Status Vocabulary

Domain fixtures may define known status values.

Example:

    statuses:
      product_request:
        - Unallocated
        - Allocated
        - Permit Required
        - Permit in Progress
        - Ready for Import
        - Received
        - Canceled

A status list defines vocabulary.

It does not automatically define:

- Transition rules
- Role permissions
- UI actions
- API behavior

unless those are separately authoritative.

---

## Status Meaning

Known status meanings may be represented.

Example:

    status_definitions:
      Allocated:
        meaning: Product quantity has been allocated to the request.

      Canceled:
        meaning: Request is no longer active for processing.

Status definitions should remain semantic rather than implementation-specific.

---

## State Transition Context

A domain fixture may define stable transition relationships only when explicitly established at the domain level.

Example:

    transitions:
      - from: Draft
        to: Submitted

      - from: Submitted
        to: Approved

Do not infer transition paths from the status list alone.

If transitions are feature-specific, keep them in the requirement.

---

## Identifier Concepts

Domain fixtures may define identifier semantics.

Example:

    identifiers:
      UPN:
        entity: Product
        uniqueness: domain-defined identifier

      Request ID:
        entity: ProductRequest

Do not infer technical format, length, or database uniqueness constraints unless authoritative.

---

## Business Value Sets

Stable controlled value sets may be represented.

Example:

    value_sets:
      division:
        values:
          - CRM
          - NMD

Only authoritative values should be included.

If the list is partial, mark it as partial rather than implying completeness.

---

## Partial Value Sets

When a fixture intentionally contains only selected values:

    value_set:
      name: division
      completeness: partial
      values:
        - CRM
        - NMD

This prevents QA-AI from assuming no other values exist.

---

## Domain Constraints

Stable domain constraints may be recorded when they apply across features.

Example:

    constraints:
      - id: DOMAIN-C-001
        statement: A UPN represents one product identity within the defined product catalog.

A domain constraint must be genuinely domain-level.

Feature-specific conditions such as:

`Edit button remains visible when Remaining Qty < Approval Qty`

belong in the feature requirement, not the domain fixture.

---

## Feature-Specific Rule Boundary

A domain fixture must not contain feature acceptance criteria merely because they reference domain entities.

Examples that normally do not belong in a general domain fixture:

- Fifth failed login locks the account.
- Submit button is disabled until all mandatory fields are populated.
- A permit can add UPN after allocation.
- A request becomes Ready for Import after a specific workflow action.

These behaviors belong in their feature requirements unless explicitly standardized as domain-wide rules.

---

## Domain Assumptions

Approved domain assumptions may be included only when they are intentionally part of the evaluation context.

Example:

    assumptions:
      - statement: Test datasets use synthetic customer identities.
        source: evaluation-policy

An assumption must be explicitly labeled.

It must not be presented as a confirmed domain rule.

---

## Terminology Consistency

Domain fixtures help normalize terminology across datasets.

If the domain uses:

`Product Request`

QA-AI should not silently rename it to:

`Purchase Request`

unless the source identifies them as equivalent.

Terminology consistency improves:

- Requirement fidelity
- Traceability
- Scenario quality
- Test-case clarity
- Cross-artifact consistency

---

## Synonyms and Aliases

Known aliases may be represented.

Example:

    aliases:
      Product Request:
        - PR

Aliases should only be included when their equivalence is authoritative.

Avoid inventing abbreviations.

---

## Ambiguous Terms

If a term has multiple possible meanings, the fixture should make the intended domain meaning explicit.

Example:

    term:
      Owner:
        domain_meaning: Business owner responsible for the product record.

This prevents QA-AI from interpreting `Owner` as:

- Record creator
- Account owner
- Device owner

when the domain defines a narrower meaning.

---

## Role-Aware Domain Context

Some domain concepts are interpreted differently depending on user role.

Example:

    role_context:
      RA:
        domain_focus:
          - Import Permit

      IAS:
        domain_focus:
          - Product Request
          - Inventory

This describes contextual focus.

It does not automatically create authorization rules.

---

## Domain Scenario Context

Fixtures may provide stable domain context useful for scenario generation.

Example:

    scenario_context:
      entities:
        - Product
        - ImportPermit
        - ProductRequest

      key_relationship:
        ImportPermit: covers Product
        ProductRequest: references Product

This helps QA-AI understand the business landscape without prescribing exact test scenarios.

---

## Synthetic Domain Data

Domain fixtures may contain stable synthetic examples.

Example:

    examples:
      product:
        upn: TEST-UPN-001
        name: Test Product
        division: NMD

Synthetic values should not reproduce real customer or confidential production data.

---

## Domain Fixture Relationships

A domain fixture may be referenced by:

`API Fixture → Domain Fixture`

`Database Fixture → Domain Fixture`

`UI Fixture → Domain Fixture`

The domain fixture should own semantic definitions that are shared across those technical contexts.

Example:

    related_fixtures:
      - API-FIX-PERMIT-001
      - DB-FIX-PERMIT-001
      - UI-FIX-PERMIT-001

Technical fixtures should reference domain concepts rather than redefine them inconsistently.

---

## Domain and API Relationship

A domain concept may appear in an API contract.

Example:

`Product Status`

The API fixture may define:

- Field name
- Request format
- Response representation

while the domain fixture defines:

- Meaning
- Allowed business vocabulary

Do not assume the API representation is the canonical domain representation.

---

## Domain and Database Relationship

A domain entity may map to one or more database structures.

The domain fixture should not assume:

`1 domain entity = 1 database table`

unless authoritative.

The database fixture owns known physical or logical persistence context.

---

## Domain and UI Relationship

The UI may display domain concepts using:

- Labels
- Localized text
- Formatted values
- Simplified names

The domain fixture owns the underlying semantic concept.

The UI fixture owns observable presentation behavior.

---

## Domain Fixture and Requirement Relationship

The requirement remains the primary source for feature-specific behavior.

The domain fixture provides supporting context.

If a requirement intentionally introduces a new domain concept or changes domain meaning:

1. Review whether the domain fixture should be updated.
2. Version the fixture when the change is material.
3. Review related datasets and benchmark compatibility.

The fixture must not override newer authoritative requirement behavior silently.

---

## Domain Fixture and Golden Output Relationship

Domain fixtures provide controlled context for generation.

Golden outputs remain reviewed QA reference interpretations.

A domain fixture must not encode:

- Expected scenario lists
- Expected test-case lists
- Risk ratings
- Evaluation scores
- Rubric levels
- Exact generated wording

---

## Domain Fixture and Benchmark Relationship

Domain fixtures improve benchmark consistency by ensuring all executions receive the same business terminology and stable domain context.

Example:

`Dataset v1 + Domain Fixture v1 + Evaluation Configuration v1`

may be reused for:

- Baseline benchmark
- Cross-platform benchmark
- Regression benchmark

Material fixture changes require comparison compatibility review.

---

## Fixture Immutability During Benchmark Execution

Once a benchmark run selects a domain fixture version, its semantic definitions should remain unchanged for that run.

If a fixture error is discovered:

1. Identify affected benchmark results.
2. Invalidate results when the error affects interpretation.
3. Correct and version the fixture.
4. Re-run affected evaluations.

This prevents benchmark results from being based on changing domain truth.

---

## Fixture Storage

Domain fixtures belong under:

`datasets/fixtures/domain/`

The canonical fixture model may be documented in Markdown.

Machine-readable fixture instances may later use:

- JSON
- YAML

when an actual automated consumer requires them.

Domain fixture structure should not be optimized prematurely for a hypothetical runtime consumer.

---

## Recommended Fixture Record

A canonical domain fixture record may contain:

| Field | Description |
|---|---|
| Fixture ID | Stable fixture identifier |
| Version | Fixture version |
| Domain | Domain identifier and name |
| Purpose | Fixture purpose |
| Terms | Domain terminology |
| Acronyms | Known acronym expansions |
| Entities | Stable business entities |
| Relationships | Stable domain relationships |
| Roles | Role meanings |
| Classifications | Business classifications |
| Status Values | Known status vocabulary |
| Value Sets | Controlled domain values |
| Constraints | Stable domain-level constraints |
| Assumptions | Explicitly approved contextual assumptions |
| Aliases | Authoritative synonyms or abbreviations |
| Related Fixtures | Referenced technical fixtures |
| Source References | Authoritative sources |
| Status | Fixture lifecycle state |

Unused fields should not be populated with invented information.

---

## Example Canonical Fixture

The following serialized representation is illustrative only.

Its terminology, entities, relationships, roles, and values demonstrate the fixture structure and are not derived from any QA-AI requirement dataset.

    fixture_id: DOMAIN-FIX-EXAMPLE-001
    version: 1.0.0
    status: Example

    domain:
      id: example-domain
      name: Example Domain

    terms:
      Resource:
        definition: Synthetic domain concept used only to demonstrate the fixture structure.

      Resource Group:
        definition: Synthetic grouping concept used only to demonstrate a domain relationship.

    entities:
      Resource:
        identifiers:
          - Resource ID

      ResourceGroup:
        relationships:
          contains:
            target: Resource

    roles:
      ExampleRole:
        name: Example Role
        description: Synthetic role used only to demonstrate role representation.

    classifications:
      resource_type:
        completeness: example-only
        values:
          - Type A
          - Type B

    related_fixtures:
      - UI-FIX-EXAMPLE-001

    source_reference:
      type: illustrative-example
      authoritative: false

The example demonstrates the canonical domain fixture structure only.

Its terminology, entities, relationships, roles, classifications, and values are synthetic and must not be treated as authoritative domain knowledge.

A real domain fixture instance must replace illustrative values with information supported by authoritative or explicitly approved domain sources.

An illustrative example must not reference a requirement dataset or domain source as authoritative unless the represented domain information is actually defined by that source.

---

## Fixture Lifecycle

The recommended domain fixture lifecycle is:

`Draft → Review → Validate → Approve → Use → Maintain`

### Draft

Create the fixture from authoritative business-domain information.

### Review

Verify:

- Terminology
- Definitions
- Scope
- Relationships
- Role meaning
- Source traceability

### Validate

Confirm that domain information is sufficient and unambiguous for the intended QA task.

### Approve

Accept the fixture as controlled reusable domain context.

### Use

Reference the approved fixture from datasets, technical fixtures, QA-AI execution, or benchmarks.

### Maintain

Version the fixture when semantic domain meaning changes materially.

---

## Fixture Validation

Before approval, verify:

- Fixture ID is unique.
- Version is defined.
- Domain scope is clear.
- Terms are authoritative.
- Acronym definitions are confirmed.
- Entity definitions are correct.
- Relationships are source-supported.
- Role meanings are correct.
- Permissions are not invented.
- Status values are source-supported.
- Status transitions are not inferred from vocabulary alone.
- Value sets are complete or explicitly marked partial.
- Constraints are genuinely domain-level.
- Feature-specific behavior has not leaked into the fixture.
- Synthetic examples are safe.
- Related fixture references are valid.
- Source references are available.
- Fixture semantics are deterministic enough for the intended evaluation.

---

## Security and Privacy

Domain fixtures must not contain:

- Customer PII
- Confidential customer data
- Real account identifiers
- Production credentials
- Trade secrets not approved for repository use
- Sensitive contract data
- Production-only business records

Use sanitized or synthetic examples where examples are required.

Domain definitions themselves should also be reviewed for repository confidentiality.

---

## Determinism Requirements

Domain fixtures should avoid contextual meaning that depends on uncontrolled runtime state.

Stable definitions are preferred.

For example:

    status:
      name: Allocated
      meaning: Quantity has been allocated.

is preferable to a definition that depends on a temporary production configuration.

When domain meaning is environment-dependent, the fixture should explicitly identify the applicable environment or context.

---

## Fixture Quality Controls

A domain fixture should be:

### Correct

Its terminology and semantics reflect authoritative domain knowledge.

### Stable

It captures reusable concepts rather than temporary feature behavior.

### Scoped

It does not model unrelated domain areas.

### Explicit

Semantic distinctions are clear.

### Traceable

Definitions can be traced to approved sources.

### Non-Behavioral by Default

Feature-specific acceptance behavior remains outside the fixture.

### Safe

No sensitive or production data is exposed.

### Maintainable

Material semantic changes can be versioned.

---

## Fixture Boundaries

Domain fixtures must not:

- Replace source requirements.
- Define feature-specific acceptance criteria by default.
- Invent business rules.
- Invent role permissions.
- Infer state transitions from status lists.
- Infer technical implementation.
- Define API fields.
- Define database schema.
- Define UI layout.
- Encode generated QA artifacts.
- Encode benchmark scores.
- Encode evaluation ratings.
- Force exact AI-generated output.
- Hide domain uncertainty with invented definitions.

---

## Validation Checklist

Before using a domain fixture, verify:

- Fixture ID exists.
- Version exists.
- Status is appropriate.
- Domain scope is clear.
- Terms are authoritative.
- Acronyms are confirmed.
- Entity definitions are valid.
- Relationships are supported.
- Role meanings are correct.
- Permissions are not inferred.
- Classifications are correct.
- Status vocabulary is supported.
- Value-set completeness is understood.
- Domain constraints are genuinely reusable.
- Feature-specific rules have not leaked into the fixture.
- Assumptions are explicitly labeled.
- Synthetic examples are safe.
- Related fixtures are valid.
- Fixture version is compatible with the dataset.
- Benchmark comparability remains valid.

---

## Final Domain Fixture Definition

A QA-AI domain fixture is:

> A controlled, versioned, source-supported representation of stable business-domain terminology, entities, relationships, roles, classifications, and semantic context used to make QA-AI generation, evaluation, and benchmark execution consistent without turning supporting context into feature-specific requirements.

The canonical domain fixture model provides:

- Stable domain terminology
- Entity definitions
- Role definitions
- Classification and status vocabulary
- Identifier semantics
- Domain relationships
- Controlled value sets
- Explicit contextual assumptions
- Cross-fixture semantic consistency
- Safe synthetic examples
- Requirement traceability
- Fixture versioning
- Benchmark reproducibility
- Cross-platform consistency
- Regression compatibility
- Protection against feature-rule leakage

It enables QA-AI to interpret domain concepts consistently while preserving the boundary between stable business context, feature requirements, and technical implementation details.
