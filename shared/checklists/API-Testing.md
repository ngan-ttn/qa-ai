# API Testing Checklist

## Purpose

The `API-Testing` checklist defines the validation criteria for assessing the quality and completeness of API testing artifacts.

Its purpose is to ensure that API testing adequately verifies functional behavior, data integrity, security, error handling, and integration before release.

This checklist defines **what should be validated**. It does not define **how API testing is performed**.

---

## Scope

This checklist applies to API testing artifacts produced by QA engineers or AI capabilities.

Artifacts reviewed by this checklist include:

- API requests
- API responses
- Request parameters
- Response payloads
- Status codes
- Authentication and authorization
- Error handling
- Data validation
- Integration verification

---

## How To Use

Apply this checklist after the API testing artifacts have been completed.

Review each validation category independently before determining the final review result.

- Verify all **MUST** criteria.
- Evaluate **SHOULD** criteria where applicable.
- Record review findings.
- Determine the final review result.

This checklist evaluates artifact quality only. It should not be used as an API testing guide or template.

---

## Validation Categories

### 1. Request Validation

Review whether API requests are correctly defined.

| Validation Criteria | Level |
|---------------------|:-----:|
| HTTP method is validated. | MUST |
| Endpoint is validated. | MUST |
| Required headers are validated. | MUST |
| Request parameters are validated where applicable. | MUST |
| Request body is validated where applicable. | MUST |

---

### 2. Response Validation

Review whether API responses match the expected behavior.

| Validation Criteria | Level |
|---------------------|:-----:|
| Status code is validated. | MUST |
| Response body matches the expected schema. | MUST |
| Response data is validated. | MUST |
| Response headers are validated where applicable. | SHOULD |
| Response time is evaluated where applicable. | SHOULD |

---

### 3. Data Validation

Review whether API operations correctly manipulate data.

| Validation Criteria | Level |
|---------------------|:-----:|
| Data is created, updated, or deleted correctly. | MUST |
| Database state is validated where applicable. | SHOULD |
| Data consistency is maintained across related operations. | MUST |
| Returned data matches persisted data where applicable. | SHOULD |

---

### 4. Error Handling

Review whether the API handles invalid or unexpected requests correctly.

| Validation Criteria | Level |
|---------------------|:-----:|
| Invalid requests return appropriate status codes. | MUST |
| Error responses contain meaningful information where applicable. | SHOULD |
| Boundary conditions are validated where applicable. | SHOULD |
| Invalid input scenarios are tested where applicable. | SHOULD |

---

### 5. Security

Review whether API security mechanisms are validated.

| Validation Criteria | Level |
|---------------------|:-----:|
| Authentication is validated where applicable. | MUST |
| Authorization is validated where applicable. | MUST |
| Unauthorized access is rejected. | MUST |
| Sensitive information is not exposed. | MUST |
| Input validation helps prevent common attacks where applicable. | SHOULD |

---

### 6. Integration

Review whether API interactions with dependent systems are validated.

| Validation Criteria | Level |
|---------------------|:-----:|
| Integration with dependent services is validated where applicable. | SHOULD |
| Upstream and downstream interactions are verified where applicable. | SHOULD |
| API contracts are validated where applicable. | SHOULD |
| External dependency behavior is considered where applicable. | SHOULD |

---

### 7. Maintainability

Review whether the API testing artifacts remain reusable and maintainable.

| Validation Criteria | Level |
|---------------------|:-----:|
| Test data is reusable where applicable. | SHOULD |
| Duplicate validations are avoided. | SHOULD |
| Test artifacts are clearly organized. | SHOULD |
| Naming and terminology are used consistently. | MUST |

---

### 8. Testability

Review whether the API testing artifacts support reliable execution and verification.

| Validation Criteria | Level |
|---------------------|:-----:|
| Expected outcomes are objectively verifiable. | MUST |
| Pass or fail can be determined objectively. | MUST |
| Required environments or dependencies are identified where applicable. | SHOULD |
| Required mock services or test doubles are documented where applicable. | SHOULD |

---

## Acceptance Criteria

| Review Result | Criteria |
|---------------|----------|
| **PASS** | All **MUST** criteria are satisfied. No critical review findings remain unresolved. The API testing artifacts are suitable for execution and verification. |
| **FAIL** | One or more **MUST** criteria are not satisfied, or critical review findings prevent reliable API testing. |

---

## Common Review Findings

| Category | Typical Findings |
|----------|------------------|
| Request Validation | Missing validation for parameters, headers, or request body |
| Response Validation | Incorrect status codes or incomplete response verification |
| Data Validation | Missing database verification or inconsistent data validation |
| Error Handling | Missing negative or boundary test coverage |
| Security | Authentication or authorization not verified |
| Integration | Missing validation for dependent services or API contracts |
| Maintainability | Duplicate validations or inconsistent terminology |
| Testability | Expected outcomes are not objectively verifiable |

---

## Input Artifacts

- API specifications
- Requirement analysis
- Business rules
- API test scenarios
- API test cases

---

## Output Artifacts

- Reviewed API testing artifacts
- API execution results
- API defect reports
- API regression testing

---

## References

- `shared/standards/`
- `shared/templates/API-Testing.md`
- `shared/glossary/`