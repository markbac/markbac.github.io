---
title: Data formats
---

# Data formats

Every interface and configuration file needs a format. The three you meet most are JSON, YAML and Protocol Buffers. They solve different problems, and choosing the wrong one makes life harder for years.

## JSON

JSON (JavaScript Object Notation, RFC 8259) is the default format for web APIs. It has objects, arrays, strings, numbers, booleans and `null`, and nothing else.

```json
{"id": "dev-042", "online": true, "battery": 71, "tags": ["roof", "north"]}
```

[[CAPTION:Figure]] A JSON object.

- Readable, supported everywhere, easy to debug.
- No comments, no date type, no binary data (use base64) and only one number type. Large integers can lose precision in JavaScript.
- JSON Schema describes and validates JSON documents, and OpenAPI uses it.
- Verbose on the wire for small devices; see [CBOR](cbor.md) for a binary equivalent.

## YAML

YAML is a superset of JSON aimed at people writing configuration by hand: indentation instead of braces, comments, multi-line strings and anchors for reuse.

```yaml
device:
  id: dev-042
  online: true
  tags: [roof, north]   # comments are allowed
```

[[CAPTION:Figure]] The same data in YAML.

- Good for configuration files: CI pipelines, Kubernetes, Docker Compose, this site's own `py-doc.yml`.
- Indentation errors change the meaning silently. Unquoted values can surprise: in YAML 1.1 parsers `no` and `on` become booleans and `1.10` becomes a number. Quote strings when in doubt.
- Do not use it for data exchanged between programs; JSON is simpler and safer.

## Protocol Buffers

Protocol Buffers (protobuf), from Google, is a binary format defined by a schema file. A compiler generates code for each language.

```protobuf
syntax = "proto3";
message Device {
  string id = 1;
  bool online = 2;
  uint32 battery = 3;
  repeated string tags = 4;
}
```

[[CAPTION:Figure]] A protobuf schema. The numbers are field tags, which go on the wire instead of names.

- Small and fast; typically a fraction of the size of the same JSON.
- Not self-describing: you need the schema to read a message.
- Schema evolution is built in: add fields with new numbers, never reuse or renumber old ones, and old and new code keep working together.
- The basis of gRPC. `nanopb` brings it to microcontrollers.

## Choosing

| Need | Good choice |
| --- | --- |
| Public web API, easy debugging | JSON |
| Hand-written configuration | YAML (or TOML for simpler files) |
| Fast internal RPC with a fixed schema | Protocol Buffers |
| Constrained devices, no schema compiler | CBOR |
| Large analytical data sets | Columnar formats such as Parquet |

[[CAPTION:Table]] Matching the format to the job.

## Where next

- [CBOR and compact binary formats](cbor.md) covers the device side.
- [OpenAPI and AsyncAPI](openapi-and-asyncapi.md) shows how schemas become contracts.
