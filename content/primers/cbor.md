---
title: CBOR and compact binary formats
---

# CBOR and compact binary formats

On a battery-powered device sending data over a narrow radio link, every byte costs energy and airtime. JSON spends many of those bytes on field names, quotes and digits written as text. Compact binary formats carry the same data in far fewer bytes, and are cheaper to parse on a small microcontroller.

## CBOR

CBOR (Concise Binary Object Representation, RFC 8949) is the IETF's binary format for constrained environments. It has the same data model as JSON (maps, arrays, strings, numbers, booleans, null). It adds byte strings, tags for extra types such as dates, and separate integer and floating-point numbers. It is self-describing: a reader needs no schema to decode a message.

Each item starts with one byte holding a 3-bit major type and a 5-bit value or length. Small integers fit in that byte.

| Major type | Meaning |
| --- | --- |
| 0 | Unsigned integer |
| 1 | Negative integer |
| 2 | Byte string |
| 3 | Text string (UTF-8) |
| 4 | Array |
| 5 | Map |
| 6 | Tag (adds meaning, such as a timestamp) |
| 7 | Floats and simple values (`true`, `false`, `null`) |

[[CAPTION:Table]] The eight CBOR major types.

A worked example: `{"t": 21, "b": 71}` is 15 bytes as compact JSON and 8 bytes as CBOR: `A2` (a map of two pairs), `61 74` ("t"), `15` (21), `61 62` ("b"), `18 47` (71). Using integer keys instead of text keys shrinks it further, which is what most constrained protocols do.

CBOR is used by CoAP, [LwM2M](lwm2m.md) (as the SenML CBOR format), COSE (CBOR Object Signing and Encryption), WebAuthn and the FIDO standards.

## CDDL

CBOR does not need a schema, but a protocol still needs a specification. CDDL (Concise Data Definition Language, RFC 8610) describes the expected structure in a compact grammar, and tools can validate messages against it:

```cddl
reading = {
  1 => uint,        ; device-local timestamp
  2 => float,       ; temperature in °C
  ? 3 => uint,      ; battery percentage, optional
}
```

[[CAPTION:Figure]] A CDDL definition with integer keys.

## Other compact formats

| Format | Schema | Self-describing | Notes |
| --- | --- | --- | --- |
| CBOR | Optional (CDDL) | Yes | IETF standard; small decoders such as TinyCBOR, QCBOR, zcbor |
| Protocol Buffers | Required | No | Smallest messages; needs generated code (`nanopb` on microcontrollers) |
| MessagePack | No | Yes | Very similar to CBOR; popular in scripting languages, not an IETF standard |
| ASN.1 (PER, UPER) | Required | No | Very compact; used in telecoms and some security standards; heavy tooling |

[[CAPTION:Table]] Compact binary formats compared.

## Choosing

- If you control both ends and can generate code, Protocol Buffers gives the smallest messages and the best schema evolution.
- If you need an open standard, interoperability with CoAP or LwM2M, or messages a gateway can decode without a schema, choose CBOR.
- Whatever the format, version your payloads and keep the schema or CDDL in version control.
- Use the same data on both sides of a gateway: decoding CBOR into JSON for the cloud is straightforward because the data models match.

## Where next

- [Data formats](data-formats.md) covers JSON, YAML and Protocol Buffers.
- [CoAP](coap.md) and [cellular LPWAN](cellular-lpwan.md) explain why size matters so much.
- [cbor.io](https://cbor.io/) lists implementations for most languages.
