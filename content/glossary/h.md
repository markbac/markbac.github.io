---
title: Glossary, H
---

# H

## H.248 {#h248}
**Gateway Control Protocol (Megaco).** The ITU-T and IETF protocol with which a media gateway controller or softswitch controls media gateways, which convert between telephone circuits and IP media streams. It does the same job as MGCP.

See also: [MGCP](m.md#mgcp), [MGW](m.md#mgw), [Softswitch](s.md#softswitch).

## H.323 {#h323}
An ITU-T family of protocols for voice and video calls over packet networks, covering signalling, media and bandwidth control. It was the main VoIP standard before SIP replaced it.

See also: [SIP](s.md#sip), [Q.931](q.md#q931), [RAS](r.md#ras).

## Half Duplex
Communication in which both ends can send, but only one at a time, like a push-to-talk radio.

See also: [Duplex](d.md#duplex), [Full duplex](f.md#full-duplex), [Simplex](s.md#simplex).

## Happy Path
See [Nominal Path](n.md#nominal-path).

## Hash Function
A function that maps data of any size to a fixed-size value. A cryptographic hash, such as SHA-256, is also one-way and collision-resistant. That makes it useful for integrity checks, digital signatures and storing passwords.

See also: [SHA](s.md#sha), [MD5](m.md#md5), [CRC](c.md#crc).

## HDF
**Handover Distribution Frame.** In UK local loop unbundling, the frame in the exchange where the copper pairs are handed over from the main distribution frame to another operator's equipment.

See also: [MDF](m.md#mdf), [Local Loop](l.md#local-loop).

## HDLC
**High-Level Data Link Control.** An ISO bit-oriented, synchronous data link protocol. Many other link protocols, including PPP framing, LAPB in X.25 and LAPD in ISDN, are based on it.

See also: [PPP](p.md#ppp), [X.25](x.md#x25), [Frame Relay](f.md#frame-relay).

## HDSL
**High-bit-rate Digital Subscriber Line.** A symmetrical DSL that carries a 2 Mbit/s (E1) or 1.5 Mbit/s (T1) circuit over two or three copper pairs. It was used to deliver leased lines without new cable.

See also: [SDSL](s.md#sdsl), [DSL](d.md#dsl).

## Heartbeat Retrospective
A retrospective held at a regular interval, such as the end of each iteration, in which the team reflects on recent events and agrees improvements.

See also: [Sprint retrospective](s.md#sprint-retrospective).

## HiFi Prototype
See [High Fidelity Prototype](#high-fidelity-prototype).

## High Fidelity Prototype
A prototype that looks and behaves much like the finished system, usually built with real development tools.

See also: [Low Fidelity Prototype](l.md#low-fidelity-prototype), [User Interface Prototype](u.md#user-interface-prototype).

## High Level Design
**HLD.** The design level between the architecture and the low-level design. It defines the components of the solution, their interfaces and how they interact, without going into how each is built.

See also: [Low Level Design](l.md#low-level-design), [Architecture](a.md#architecture).

## HLD
See [High Level Design](#high-level-design).

## HLR
**Home Location Register.** The central database of a GSM or UMTS network, holding each subscriber's details: their IMSI, phone numbers, services and current location. In LTE and IMS, the HSS replaced it.

See also: [VLR](v.md#vlr), [HSS](#hss), [IMSI](i.md#imsi), [MSC](m.md#msc).

## Hotfix
A small, urgent change, sometimes called a patch, that fixes a bug in released software outside the normal release cycle.

See also: [Release](r.md#release).

## How Requirement
Usually a synonym for [Non-functional Requirement](n.md#non-functional-requirement); sometimes used for design constraints.

## How Well Requirement
See [Non-functional Requirement](n.md#non-functional-requirement).

## HSRP
**Hot Standby Router Protocol.** Cisco's protocol for a fault-tolerant default gateway. Two or more routers share a virtual IP address; one is active and the others take over if it fails. VRRP is the open-standard equivalent.

See also: [Router](r.md#router).

## HSS
**Home Subscriber Server.** The master subscriber database for IMS and LTE, holding user profiles and authentication data and tracking where users are registered. It takes over the jobs of the HLR and the authentication centre.

See also: [HLR](#hlr), [IMS](i.md#ims), [CSCF](c.md#cscf), [MME](m.md#mme).

## HTTP
**Hypertext Transfer Protocol.** The request-response protocol of the web. A client asks for a resource by URL with a method such as `GET` or `POST`, and the server returns a status and content. HTTP/2 and HTTP/3 keep the same model with more efficient transports.

See also: [HTTPS](#https), [REST](r.md#rest), [URL](u.md#url).

## HTTPS
HTTP over TLS. It encrypts the traffic and lets the client check the server's identity through its certificate, protecting against eavesdropping and tampering.

See also: [HTTP](#http), [TLS](t.md#tls), [CA](c.md#ca).

## Hub
A network device that repeats every frame it receives to all its other ports, so all connected devices share one collision domain. It works at layer 1, and switches have replaced it.

See also: [Switch](s.md#switch), [L1](l.md#l1).

## Human factors
The study of how people behave, physically and mentally, with products, systems and environments, and how to design for them.

See also: [User Experience](u.md#user-experience).

## Hungarian notation
A naming convention in which a prefix on an identifier shows its kind or type, such as `cApples` for a count or `szName` for a zero-terminated string. Most modern style guides advise against encoding the type in this way.

See also: [Camel Case](c.md#camel-case), [Snake Case](s.md#snake-case).
