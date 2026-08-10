# API Terms

## Purpose

This document defines standardized terminology related to Application Programming Interfaces (APIs) and API testing.

Its purpose is to establish a shared vocabulary across the QA-AI framework, ensuring that API-related documentation, skills, workflows, templates, and testing artifacts use consistent terminology.

---

## A

### API (Application Programming Interface)

**Definition**

A set of rules and contracts that enables software systems to communicate and exchange data.

**Related Terms**

- Endpoint
- Request
- Response

---

### API Contract

**Definition**

A formal specification that defines how an API should behave, including requests, responses, data structures, and expected behaviors.

**Related Terms**

- OpenAPI Specification
- Request
- Response

---

### Authentication

**Definition**

The process of verifying the identity of a user, application, or system before access is granted.

**Related Terms**

- Authorization
- Access Token
- OAuth

---

### Authorization

**Definition**

The process of determining what actions an authenticated user or system is permitted to perform.

**Related Terms**

- Authentication
- Role
- Permission

---

## B

### Bearer Token

**Definition**

An access token transmitted in the HTTP Authorization header to authenticate API requests.

**Related Terms**

- Access Token
- Authentication
- OAuth

---

## E

### Endpoint

**Definition**

A specific URL that provides access to an API resource or operation.

**Related Terms**

- API
- Request
- Response

---

## H

### HTTP Method

**Definition**

The operation type used to interact with an API resource, such as GET, POST, PUT, PATCH, or DELETE.

**Related Terms**

- Endpoint
- Request

---

### HTTP Status Code

**Definition**

A standardized numeric code indicating the result of an HTTP request.

**Related Terms**

- Response
- Error Response

---

## O

### OAuth

**Definition**

An authorization framework that enables secure delegated access to protected resources.

**Related Terms**

- Authentication
- Authorization
- Access Token

---

## P

### Path Parameter

**Definition**

A variable included within the API endpoint path that identifies a specific resource.

**Related Terms**

- Endpoint
- Query Parameter

---

### Payload

**Definition**

The data transmitted within an API request or response body.

**Related Terms**

- Request Body
- Response Body

---

## Q

### Query Parameter

**Definition**

A key-value pair appended to a URL to filter, sort, or modify the behavior of an API request.

**Related Terms**

- Path Parameter
- Request

---

## R

### Request

**Definition**

A message sent by a client to invoke an API operation.

**Related Terms**

- Response
- Endpoint

---

### Request Body

**Definition**

The payload transmitted within an API request.

**Related Terms**

- Payload
- Request

---

### Response

**Definition**

A message returned by an API after processing a request.

**Related Terms**

- Request
- Status Code

---

### Response Body

**Definition**

The payload returned within an API response.

**Related Terms**

- Payload
- Response

---

### REST (Representational State Transfer)

**Definition**

An architectural style for designing networked APIs using standard HTTP methods and stateless communication.

**Related Terms**

- API
- HTTP Method
- Endpoint

---

## S

### Schema

**Definition**

A structured definition describing the expected format and data types of an API request or response.

**Related Terms**

- Payload
- API Contract

---

### Stateless

**Definition**

A communication model in which each request contains all information required for processing, without relying on previous requests.

**Related Terms**

- REST
- Session

---

## T

### Timeout

**Definition**

The maximum duration allowed for an API request before it is terminated.

**Related Terms**

- Request
- Response Time

---

## V

### Versioning

**Definition**

The practice of managing changes to an API while maintaining compatibility between different API versions.

**Related Terms**

- API Contract
- Endpoint