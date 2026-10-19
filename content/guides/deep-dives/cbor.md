---
title: CBOR
---

# CBOR

## Purpose and scope

This document explains the Concise Binary Object Representation (CBOR) at a byte level: the type system, the encoding rules, and the worked examples needed to read or write a CBOR payload by hand. It is a companion document to *LwM2M: A Deep Explainer*, which uses CBOR (via SenML CBOR) as one of its payload formats, and to *CoAP: A Deep Explainer*, which carries CBOR as an opaque payload without caring about its structure. It assumes familiarity with binary/hex representations but no prior exposure to CBOR or similar formats.

## 1. Why a binary format at all

JSON is a text format: every byte of a JSON document is human-readable ASCII, which is exactly why it is inefficient on a constrained device. The number `1000000` encoded as JSON text is 7 bytes; encoded as CBOR it is 5 bytes, and a boolean `true` that costs 4 ASCII bytes in JSON costs a single byte in CBOR. On an NB-IoT link where every byte transmitted costs airtime and battery (see the repetition mechanism in the NB-IoT explainer), and where parsing has to happen on a microcontroller with a few tens of kilobytes of RAM, both the wire size and the parsing cost matter.

CBOR (RFC 8949) is designed to solve this without inventing a new data model: it encodes exactly the same tree of maps, arrays, numbers, strings, and booleans that JSON does, just as compact binary rather than text. A CBOR decoder does not need a schema to parse a payload -- the type and length of every item is self-describing from its first byte, which is what makes generic CBOR libraries possible.

## 2. The major type system

Every CBOR data item begins with a single **initial byte**, split into two fields:

```wavedrom
{reg: [
  {bits: 5, name: 'Additional info'},
  {bits: 3, name: 'Major type'}
], config: {bits: 8, lanes: 1}}
```

The major type says what kind of item this is; the additional info either encodes a small value directly or says how many following bytes encode a larger value/length.

| Major type | Value | Meaning |
|---|---|---|
| 0 | Unsigned integer | 0 to 2^64-1 |
| 1 | Negative integer | -1 down to -2^64 |
| 2 | Byte string | Raw bytes |
| 3 | Text string | UTF-8 text |
| 4 | Array | Ordered sequence of items |
| 5 | Map | Key/value pairs |
| 6 | Tag | Semantic tag wrapping the following item |
| 7 | Simple/float | Booleans, null, floating point, "break" |

### Additional info encoding

The bottom 5 bits of the initial byte follow one rule, used identically across every major type:

| Additional info value | Meaning |
|---|---|
| 0-23 | The value itself, encoded directly in these bits |
| 24 | Value follows as 1 more byte |
| 25 | Value follows as 2 more bytes |
| 26 | Value follows as 4 more bytes |
| 27 | Value follows as 8 more bytes |
| 31 | Indefinite length (see section 5) |

This single rule is why CBOR needs no separate "length-prefix" mechanism per type -- the same 5-bit scheme sizes an integer's value, a string's length, an array's item count, or a map's pair count.

## 3. Worked examples

### Small unsigned integer: `10`

```
0x0A
```

Major type 0 (unsigned int, top 3 bits `000`), additional info 10 (bottom 5 bits `01010`) -- the value is encoded entirely in the initial byte. One byte, done.

### Larger unsigned integer: `1000000`

```
0x1A 000F4240
```

`0x1A` = major type 0, additional info 26 ("value follows as 4 more bytes"). The following 4 bytes, `00 0F 42 40`, are 1,000,000 in big-endian. Five bytes total, versus 7 ASCII bytes for the JSON text `1000000`.

```wavedrom
{reg: [
  {bits: 8, name: '0x40'},
  {bits: 8, name: '0x42'},
  {bits: 8, name: '0x0F'},
  {bits: 8, name: '0x00'},
  {bits: 5, name: '26'},
  {bits: 3, name: '0'}
], config: {bits: 40, lanes: 1}}
```

### Negative integer: `-500`

```
0x39 01F3
```

Major type 1 (negative integer, `001`), additional info 25 ("2 more bytes follow"). CBOR encodes negative integers as `-(n+1)`, so to encode -500 it stores `n = 499 = 0x01F3`. This offset-by-one trick means major type 1 can represent -2^64 with the same bit width that major type 0 uses for 2^64-1, rather than wasting a sign bit.

### Text string: `"gas"`

```
0x63 676173
```

`0x63` = major type 3 (text string, `011`), additional info 3 (length 3 bytes). The following bytes `67 61 73` are the UTF-8 encoding of "g", "a", "s".

### Array: `[1, 2, 3]`

```
0x83 01 02 03
```

`0x83` = major type 4 (array, `100`), additional info 3 (3 items follow). Then three individual data items, each self-encoded: `01`, `02`, `03`.

### Map: `{"id": 1}`

```
0xA1 6269 64 01
```

`0xA1` = major type 5 (map, `101`), additional info 1 (1 key/value pair follows). Then the key as a text string -- `62` (text string, length 2), `69 64` ("i", "d") -- followed by the value `01` (unsigned int 1). A map is encoded as a flat sequence of alternating key, value, key, value items; nothing marks where one pair ends and the next begins except walking the items in order.

### Putting it together: `{"id": 1, "name": "meter"}`

```
0xA2                      # map, 2 pairs
  62 6964                 # key: "id"
  01                       # value: 1
  64 6E616D65              # key: "name"
  65 6D65746572             # value: "meter"
```

Reading this byte-by-byte: `A2` (map, 2 pairs); `62 69 64` (text string length 2 = "id"); `01` (unsigned int 1); `64 6E 61 6D 65` (text string length 4 = "name"); `65 6D 65 74 65 72` (text string length 5 = "metre"). A generic CBOR decoder walks this without ever being told in advance that a map, then a string, then an int is coming -- every item announces its own type and length.

## 4. Simple values, booleans, and floats (major type 7)

Major type 7 is a catch-all for values that are not numbers, strings, arrays, or maps:

| Encoding | Meaning |
|---|---|
| `0xF4` | `false` |
| `0xF5` | `true` |
| `0xF6` | `null` |
| `0xF7` | `undefined` |
| `0xF9` xxxx | half-precision (16-bit) float |
| `0xFA` xxxxxxxx | single-precision (32-bit) float |
| `0xFB` xxxxxxxxxxxxxxxx | double-precision (64-bit) float |
| `0xFF` | "break" -- closes an indefinite-length item (see section 5) |

A sensor reading such as `21.4` would typically be encoded as a 32-bit float (`0xFA` + 4 bytes) unless the application has already agreed on a fixed-point integer representation to save the extra bytes.

## 5. Indefinite-length items

Sometimes the encoder does not know an item's final length in advance -- streaming a byte string as it arrives, for instance. Additional info value 31 marks an item as indefinite-length: instead of a length, the item is terminated by a `0xFF` "break" byte once all its chunks (for strings) or elements (for arrays/maps) have been written.

```
0x9F 01 02 03 FF
```

`0x9F` = array, additional info 31 (indefinite length) -- items follow until `FF` (break) is seen. This is functionally equivalent to `0x83 01 02 03` but useful when the encoder is generating items faster than it can count them, which matters less for small fixed-schema payloads (most LwM2M resources) than for genuinely streamed data.

> **Warning:** Indefinite-length encoding is explicitly disallowed under **Canonical CBOR** (deterministic encoding, RFC 8949 §4.2), which many constrained-device implementations require so that two encoders always produce byte-identical output for the same logical data -- useful for signing or hashing a payload. If a payload needs to be signed or compared by hash, confirm the encoder is using definite lengths and the canonical map-key ordering below.

## 6. Canonical CBOR and map key ordering

Because a map is just a flat sequence of key/value pairs with no inherent ordering requirement, two encoders can produce different (but semantically identical) byte sequences for the same map depending on key order. Canonical CBOR fixes this by requiring map keys to be sorted (by the bytewise encoding of the key, not by application-level meaning) and by requiring the shortest possible encoding of every length and integer (never using the 2-byte form where the 1-byte form would do).

This matters wherever a payload's exact bytes need to be reproducible -- signature verification being the obvious case -- and is easy to get wrong when hand-rolling an encoder rather than using a conformant library.

## 7. Tags (major type 6)

A tag wraps the following data item with extra semantic meaning that a generic decoder can choose to interpret or ignore. For example, tag 1 (`0xC1`) means "the following integer or float is a Unix timestamp":

```
0xC1 1A 653C 8A00
```

`0xC1` = tag 1, followed by `1A 653C8A00` -- an unsigned integer (major type 0, 4-byte form) representing seconds since the epoch. A decoder that understands tag 1 renders this as a date; one that does not can still safely read the underlying integer.

## 8. CBOR compared to alternatives

| | CBOR | JSON | Protocol Buffers | MessagePack |
|---|---|---|---|---|
| Format | Binary | Text | Binary | Binary |
| Schema required to decode | No | No | Yes (.proto file) | No |
| Self-describing | Yes | Yes | No | Yes |
| Typical size vs JSON | Smaller | Baseline | Smallest (with schema) | Similar to CBOR |
| Extensibility | Tags | N/A | Field numbers + versioning | Limited |
| IETF standard | Yes (RFC 8949) | Yes (RFC 8259) | No (Google-defined) | No (community spec) |

CBOR's advantage over Protocol Buffers for a device-management protocol is that no schema needs to be distributed, compiled, or kept in version-lockstep between client and server -- a genuine benefit when a server may need to talk to devices running several different firmware versions with slightly different object definitions. The cost is that CBOR payloads carry more self-description overhead than a schema-compiled Protobuf message would for the same data.

## 9. Why this matters for LwM2M

LwM2M does not use raw CBOR directly; it uses **SenML CBOR**, which is CBOR encoding a specific SenML (Sensor Measurement Lists, RFC 8428) record structure -- an array of maps, each map using short integer keys (rather than the human-readable string keys shown in the examples above) to represent a resource path, a value, and a timestamp, all wrapped in the byte-level rules described in this document. Everything above still applies unchanged: SenML CBOR is CBOR, just with an agreed application-level schema for what the maps contain. The LwM2M deep dive covers that schema; this document covers the byte-level mechanics underneath it.
