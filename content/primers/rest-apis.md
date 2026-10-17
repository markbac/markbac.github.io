---
title: REST APIs
---

# REST APIs

REST (Representational State Transfer) is the architectural style Roy Fielding described in his 2000 doctoral thesis, based on how the web itself works. In everyday use, a "REST API" means an HTTP API organised around resources, using the HTTP methods and status codes for what they mean. Few APIs follow every one of Fielding's constraints, and that is fine; the conventions are what make an API predictable.

## Resources and URLs

A resource is a thing the API exposes: a device, a reading, a user. Each has a URL. Use nouns and plural collections:

```text
GET    /devices                  list devices
POST   /devices                  create a device
GET    /devices/{id}             read one device
PATCH  /devices/{id}             change some fields
DELETE /devices/{id}             remove it
GET    /devices/{id}/readings    a sub-collection
```

[[CAPTION:Figure]] Resource-oriented URLs.

Actions that do not fit create, read, update and delete can be modelled as a resource of their own (`POST /devices/{id}/reboots`) rather than a verb in the URL.

## Methods

| Method | Meaning | Safe | [Idempotent](idempotency.md) |
| --- | --- | --- | --- |
| GET | Read | Yes | Yes |
| POST | Create, or start a process | No | No |
| PUT | Replace entirely | No | Yes |
| PATCH | Change part of it | No | Not necessarily |
| DELETE | Remove | No | Yes |

[[CAPTION:Table]] HTTP methods as REST uses them.

## Status codes

Use the right class so that clients and proxies behave correctly:

- **2xx success**: 200 OK, 201 Created (with a `Location` header), 202 Accepted (work will happen later), 204 No Content.
- **4xx client error**: 400 Bad Request, 401 Unauthorized (not authenticated), 403 Forbidden (authenticated but not allowed), 404 Not Found, 409 Conflict, 422 Unprocessable Content, 429 Too Many Requests.
- **5xx server error**: 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout.

Return errors in one consistent body format. RFC 9457 (Problem Details for HTTP APIs) defines a standard one.

## Design habits that pay off

- **Statelessness**: each request carries everything needed to process it, including authentication. This makes servers easy to scale.
- **Pagination** on every collection that can grow, preferably with cursors rather than page numbers.
- **Filtering and sorting** through query parameters: `/devices?status=offline&sort=-lastSeen`.
- **Versioning** from day one, in the path (`/v1/`) or a header, and a policy for how long old versions live.
- **Caching** with `ETag` and `Cache-Control`; conditional requests (`If-Match`) also prevent lost updates.
- **Security**: HTTPS only, tokens such as [OAuth 2.0](oauth-and-oidc.md) access tokens, rate limits, and input validation. See [OWASP Top 10](owasp-top-10.md).

## REST and the alternatives

REST suits public and resource-shaped APIs. gRPC (Protocol Buffers over HTTP/2) suits fast internal service-to-service calls. GraphQL suits clients that need flexible queries across many resources. Event-driven interfaces suit notifications and streams. For constrained devices, CoAP brings the REST model to UDP; see [CoAP](coap.md).

## Where next

- [OpenAPI and AsyncAPI](openapi-and-asyncapi.md) shows how to describe an API as a contract.
- The [Guidelines](../guidelines/index.md) section has the API design rules for this site.
