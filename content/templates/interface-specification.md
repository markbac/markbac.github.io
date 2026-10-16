---
title: Interface specification
---

# Interface specification

Use this template to describe an interface between components, products or external systems: a web API, a message stream, a remote procedure call, inter-process communication or a hardware bus. The machine-readable specification, such as an OpenAPI or AsyncAPI file, is the contract. This page wraps it with what the specification file cannot say: who owns it, the quality of service, errors, versioning and security.

## Choose the specification format

[[CAPTION:Table]] Specification formats by interface style.

| Style | Specification | Where it usually lives |
|-------|---------------|------------------------|
| HTTP web API | OpenAPI 3.1 | `api/openapi.yaml` |
| Events and messaging (MQTT, Kafka, AMQP, WebSocket) | AsyncAPI 3 | `api/asyncapi.yaml` |
| Remote procedure call and streaming | gRPC with Protocol Buffers | `api/proto/*.proto` |
| Client-driven queries | GraphQL schema | `api/schema.graphql` |
| Inter-process communication, operating system or embedded | D-Bus XML, C headers, register maps | `api/idl/`, `include/` |
| Constrained device management | LwM2M object definitions | `api/lwm2m/*.xml` |

Generate code, mocks and contract tests from the specification file where you can, so it cannot drift from the implementation.

## Template

```markdown
---
id: IF-0000
name: Interface name
owner: Team or role
version: 1.0.0
status: proposed        # proposed | active | deprecated | retired
style: openapi          # openapi | asyncapi | grpc | graphql | ipc | hardware | custom
providers: [component]
consumers: [component, product]
last-reviewed: YYYY-MM-DD
---

# IF-0000: Interface name

## 1. Purpose and scope

What the interface does, what it deliberately does not do, who
provides it and who uses it.

## 2. Specification

Link to the specification file, for example `api/openapi.yaml`, and
summarise the main operations, topics or messages. For a hardware or
binary interface, give the transport, the message layout, packing,
byte order and alignment.

## 3. Data and encoding

Serialisation (JSON, CBOR, Protocol Buffers, raw binary), character
set (UTF-8), byte order, units and time format (UTC, ISO 8601).

## 4. Timing and quality of service

- Latency: for example 99th percentile under 50 ms.
- Throughput and rate limits: for example 100 requests per second per client.
- Delivery guarantee for messages: at most once, at least once or exactly once.
- Ordering and duplicate handling.

## 5. Errors and recovery

- Error codes and the error format (for HTTP, RFC 9457 problem details).
- Retry policy: which errors to retry, back-off and jitter.
- What consumers do when the provider is unreachable.

## 6. Versioning and compatibility

- Semantic versioning: a field removed or retyped is a major change.
- How the version is carried: path, header, topic or field.
- Deprecation notice period, for example six months.

## 7. Security

- Authentication: how callers prove who they are (mTLS, tokens, keys).
- Authorisation: roles or scopes per operation.
- Encryption in transit and, for sensitive data, at rest.
- Personal data carried, and why.

## 8. Verification

- Contract tests and where they run.
- Mock servers or simulators generated from the specification.
- The CI check that blocks incompatible changes.

## 9. Change history

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | YYYY-MM-DD | First version |
```
