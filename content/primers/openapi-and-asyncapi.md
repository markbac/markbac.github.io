---
title: OpenAPI and AsyncAPI
---

# OpenAPI and AsyncAPI

An interface description is a machine-readable file that says exactly what an API offers: its operations or channels, the messages and their schemas, and how to authenticate. Writing it down as a file makes the API a reviewable contract and lets tools generate documentation, client code, mock servers and tests from one source.

- **OpenAPI** describes request-response HTTP APIs. It started as Swagger and is now run by the OpenAPI Initiative under the Linux Foundation. Version 3.1 aligned its schemas with JSON Schema.
- **AsyncAPI** describes event-driven and message-based interfaces: MQTT, Kafka, AMQP, WebSockets. It deliberately looks like OpenAPI, so the skills transfer.

## OpenAPI in brief

```yaml
openapi: 3.1.0
info:
  title: Device API
  version: 1.2.0
paths:
  /devices/{id}:
    get:
      summary: Read one device
      parameters:
        - name: id
          in: path
          required: true
          schema: {type: string}
      responses:
        "200":
          description: The device
          content:
            application/json:
              schema: {$ref: "#/components/schemas/Device"}
        "404":
          description: No such device
components:
  schemas:
    Device:
      type: object
      required: [id, status]
      properties:
        id: {type: string}
        status: {type: string, enum: [online, offline]}
```

[[CAPTION:Figure]] A minimal OpenAPI 3.1 description.

## AsyncAPI in brief

AsyncAPI 3.0 separates channels (where messages go), operations (whether this application sends or receives) and messages (what is sent):

```yaml
asyncapi: 3.0.0
info:
  title: Device telemetry
  version: 1.0.0
channels:
  telemetry:
    address: devices/{deviceId}/telemetry
    parameters:
      deviceId: {}
    messages:
      reading:
        payload:
          type: object
          properties:
            temperature: {type: number}
            timestamp: {type: string, format: date-time}
operations:
  receiveTelemetry:
    action: receive
    channel: {$ref: "#/channels/telemetry"}
```

[[CAPTION:Figure]] A minimal AsyncAPI 3.0 description of an MQTT topic.

## Design first or code first

- **Design first**: write the description, review it with the consumers, then build. Better APIs, because the contract gets attention before anything depends on it.
- **Code first**: annotate the code and generate the description. Quicker to start, but the API tends to reflect the implementation.

For any API used outside the team, design first is worth the effort. Either way, keep the file in version control and check it in CI.

## Tooling

- Linters such as Spectral check descriptions against style rules.
- Breaking-change detectors (`oasdiff` for OpenAPI) compare versions in a pull request.
- Generators produce client libraries and server stubs; Redocly, Swagger UI and the AsyncAPI generator produce documentation.
- Mock servers (Prism, Microcks) let consumers start before the API exists.

## Where next

- [REST APIs](rest-apis.md) and [event-driven architecture](event-driven-architecture.md) give the background.
- The [Guidelines](../guidelines/index.md) section sets the API conventions used here.
- The specifications are at [spec.openapis.org](https://spec.openapis.org/) and [asyncapi.com](https://www.asyncapi.com/docs/reference/specification/latest).
