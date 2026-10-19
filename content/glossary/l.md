---
title: L
---

# L

## L1
**Layer 1, the physical layer.** The lowest layer of the OSI model, which sends raw bits over a medium such as copper, fibre or radio. It defines the connectors, signals, timing and encoding.

See also: [L2](#l2), [Hub](h.md#hub).

## L2
**Layer 2, the data link layer.** The OSI layer that moves frames between devices on the same link or LAN segment, with local (MAC) addressing and error detection. Ethernet and Wi-Fi work here; switches forward traffic at this layer.

See also: [L1](#l1), [MAC](m.md#mac), [Switch](s.md#switch), [DLP](d.md#dlp).

## L2F
**Layer 2 Forwarding.** A Cisco tunnelling protocol for carrying PPP sessions across an IP network. It has no encryption of its own, and L2TP replaced it.

See also: [L2TP](#l2tp), [PPTP](p.md#pptp).

## L2TP
**Layer 2 Tunnelling Protocol.** A protocol that tunnels PPP sessions over an IP network, used by ISPs to hand broadband sessions between networks and to build VPNs. It does not encrypt, so it is often run inside IPsec.

See also: [LAC](#lac), [LNS](#lns), [LTS](#lts), [IPSec](i.md#ipsec).

## L2VPN
**Layer 2 VPN.** A provider service that carries a customer's Ethernet or other layer-2 traffic between sites over the provider's MPLS network. The sites then appear to share one LAN or wire. Point-to-point and multipoint (VPLS) forms exist.

See also: [VPLS](v.md#vpls), [VPWS](v.md#vpws), [L3VPN](#l3vpn), [PW](p.md#pw).

## L3VPN
**Layer 3 VPN.** A provider service, usually MPLS-based as in RFC 4364, that routes a customer's IP traffic between sites. The provider edge routers keep each customer's routes in a separate VRF; customer edge routers connect to them, and provider core routers just switch labels.

See also: [VRF](v.md#vrf), [CE](c.md#ce), [L2VPN](#l2vpn), [LSP](#lsp).

## LAC
**L2TP Access Concentrator.** The device at one end of an L2TP tunnel that receives a user's PPP session and forwards it through the tunnel to the LNS.

See also: [L2TP](#l2tp), [LNS](#lns).

## LACP
**Link Aggregation Control Protocol.** The IEEE 802.1AX (formerly 802.3ad) protocol with which two devices agree to bundle several physical links into one logical link and check that each member is working.

See also: [LAG](#lag).

## LAG
**Link Aggregation Group.** Several physical links bundled into one logical link, to add capacity and survive the failure of a member. LACP usually manages it.

See also: [LACP](#lacp).

## LAN
**Local Area Network.** A network that connects devices within a limited area, such as a home, office or campus, usually with Ethernet and Wi-Fi.

See also: [WAN](w.md#wan), [MAN](m.md#man).

## LANE
**LAN Emulation.** An ATM Forum standard that made an ATM network look like an Ethernet or Token Ring LAN to the devices attached to it.

See also: [ATM](a.md#atm).

## Latency
The delay between something being sent and it arriving. For telephone calls it is the mouth-to-ear delay, made up of codec, network and playout delays. ITU-T G.114 advises keeping one-way delay under about 150 ms for good conversation.

See also: [Jitter](j.md#jitter), [Jitter buffer](j.md#jitter-buffer), [Bandwidth](b.md#bandwidth).

## Lawful intercept
**LI.** Facilities in telecoms networks that let authorised agencies, with a warrant, intercept a named target's communications. Operators must provide them, through standardised interfaces. It differs from bulk surveillance in being targeted at individuals.

## LCR
**Least Cost Routing.** Choosing the route for each outgoing call by cost, across several carriers. Carriers revise their tables often, and PBXs can do the same for a business.

See also: [CPS](c.md#cps).

## LDAP
**Lightweight Directory Access Protocol.** An open protocol, defined in RFC 4511, for reading and updating directory services, such as a company's directory of users and groups. Active Directory supports it.

See also: [AD](a.md#ad), [Kerberos](k.md#kerberos).

## Lead Time
The time from a customer's request to its delivery. In software, often the time from a requirement being raised to it being met in production.

See also: [Kanban](k.md#kanban).

## Lean
A way of working, from Toyota's production system, that aims to deliver value to the customer by removing waste: anything that does not add value.

See also: [Lean programming](#lean-programming), [Kanban](k.md#kanban).

## Lean programming
Lean ideas applied to software development: removing waste, delivering fast, deciding as late as possible and building quality in.

See also: [Lean](#lean).

## Leased Line
A dedicated, symmetrical circuit between two points, rented for a fixed fee and always on. In the UK it is also called a private circuit. Businesses use leased lines to link sites and for internet access.

See also: [EAD](e.md#ead), [Dark Fibre](d.md#dark-fibre), [CSI](c.md#csi).

## LeSS
**Large-Scale Scrum.** A framework for scaling Scrum to many teams working on one product, with one product owner and one product backlog.

See also: [Scrum](s.md#scrum), [SAFe](s.md#safe), [DAD](d.md#dad).

## Lifecycle
A model of the activities from the first idea for a system to its retirement, usually divided into phases. Projects choose and tailor a lifecycle to suit their risks.

See also: [Waterfall](w.md#waterfall), [Spiral Lifecycle](s.md#spiral-lifecycle), [SDLC](s.md#sdlc), [Phase](p.md#phase).

## Lines of Code
**LOC.** A measure of software size as the number of source lines, usually counting neither comments nor blank lines. KLOC means thousands of lines.

See also: [Function Point](f.md#function-point).

## Linux
A family of free, open-source operating systems built on the Linux kernel, first released by Linus Torvalds in 1991. It is packaged in distributions, such as Debian, Ubuntu, Fedora and Red Hat Enterprise Linux. It runs most servers and embedded devices, and underlies Android.

See also: [GNU](g.md#gnu), [Unix](u.md#unix), [Kernel](k.md#kernel), [Android](a.md#android).

## Lisp
A family of languages, first specified in 1958, with a fully bracketed prefix syntax in which code and data share the same form. Common Lisp, Scheme and Clojure are its main dialects. Lisp introduced many ideas now common, such as garbage collection and the read-eval-print loop.

## LL
See [Local Loop](#local-loop).

## LNS
**L2TP Network Server.** The device at the far end of an L2TP tunnel from the LAC, which terminates the users' PPP sessions, typically at the ISP.

See also: [L2TP](#l2tp), [LAC](#lac), [LTS](#lts).

## Local Build
A build done in a developer's local development environment.

See also: [Project Build](p.md#project-build), [Build](b.md#build).

## Local Development Environment
**LDE.** A developer's own development environment, usually on their own machine.

See also: [Development Environment](d.md#development-environment), [Build Environment](b.md#build-environment).

## Local Loop
The line that connects a customer's premises to the operator's network, traditionally a copper pair to the local exchange. Also called the last mile or subscriber line.

See also: [MPF](m.md#mpf), [MDF](m.md#mdf), [DP](d.md#dp).

## Local Test Environment
The part of the local development environment used for construction testing.

See also: [Local Development Environment](#local-development-environment).

## LoFi Prototype
See [Low Fidelity Prototype](#low-fidelity-prototype).

## Low Fidelity Prototype
A rough mock-up of a system made with paper, sticky notes or simple drawings, used to explore ideas cheaply before building anything.

See also: [High Fidelity Prototype](h.md#high-fidelity-prototype), [Storyboard](s.md#storyboard).

## Low Level Design
**LLD.** The design level between high-level design and construction, detailed enough to build from directly.

See also: [High Level Design](h.md#high-level-design), [Detailed Design](d.md#detailed-design).

## LSP
**Label Switched Path.** A path through an MPLS network, set up by a protocol such as LDP or RSVP-TE. The first router adds a label, each router along the way swaps it, and the last removes it.

See also: [LSR](#lsr), [RSVP](r.md#rsvp), [L3VPN](#l3vpn).

## LSR
**Label Switch Router.** A router in the middle of an MPLS network that forwards packets by their labels alone.

See also: [LSP](#lsp).

## LTE (4G)
**Long-Term Evolution.** The 3GPP mobile standard (Release 8 onwards) that followed UMTS, with an OFDMA radio interface and an all-IP core, the Evolved Packet Core. LTE-Advanced meets the ITU's 4G requirements. Voice runs over IP as VoLTE.

See also: [E-UTRAN](e.md#e-utran), [E NodeB](e.md#e-nodeb), [MME](m.md#mme), [S-GW](s.md#s-gw), [PGW](p.md#pgw), [VoLTE](v.md#volte).

## LTS
**L2TP Tunnel Switch.** A router between a LAC and an LNS that acts as both. It ends incoming L2TP tunnels and forwards the sessions through new tunnels to other LNSs, for example to different ISPs.

See also: [L2TP](#l2tp), [LAC](#lac), [LNS](#lns).

## Lua
A small, fast scripting language from Brazil, designed in 1993 to be embedded in applications through a simple C API. It is used widely in games and network equipment.

## LwM2M
**Lightweight Machine to Machine.** The OMA SpecWorks protocol for managing IoT devices and their data over CoAP, usually secured with DTLS. Devices expose standard objects, such as device information, connectivity and firmware update, so servers can manage different makers' devices in the same way.

See also: [M2M](m.md#m2m), [DTLS](d.md#dtls), [CBOR](c.md#cbor), [FOTA](f.md#fota).
