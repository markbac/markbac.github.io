---
title: I
---

# I

## IA
**Information Assurance.** Managing the risks to information and the systems that handle it, so that it keeps its confidentiality, integrity, availability, authenticity and non-repudiation.

See also: [CESG](c.md#cesg), [NCSC](n.md#ncsc).

## IaaS
**Infrastructure as a Service.** Cloud computing that rents virtual machines, storage and networks, which the customer manages from the operating system up.

See also: [PaaS](p.md#paas), [SaaS](s.md#saas), [NaaS](n.md#naas).

## ICE
**Interactive Connectivity Establishment.** A technique, defined in RFC 8445, for finding the most direct working path between two peers behind NATs and firewalls. It tries candidate addresses gathered with STUN and TURN. SIP and WebRTC media use it.

See also: [STUN](s.md#stun), [NAT](n.md#nat).

## ICMP
**Internet Control Message Protocol.** The IP protocol that carries error and diagnostic messages, such as "destination unreachable" and the echo request and reply used by `ping`.

See also: [ICMPv6](#icmpv6), [Internet Protocol Suite](#internet-protocol-suite).

## ICMPv6
ICMP for IPv6, defined in RFC 4443. As well as errors and `ping`, it carries Neighbour Discovery, which replaces ARP, and Multicast Listener Discovery, which replaces IGMP.

See also: [ICMP](#icmp), [IPv6](#ipv6).

## IDE
**Integrated Development Environment.** An application that combines a code editor, build tools and a debugger, and often much more, for writing software.

See also: [Integrated Development Environment](#integrated-development-environment).

## IDQ
**Informatica Data Quality.** Informatica's tool for profiling, cleansing and standardising enterprise data.

See also: [DQ](d.md#dq).

## IEC
**International Electrotechnical Commission.** The international body that publishes standards for electrical and electronic technologies. It works with ISO on information technology standards, such as the ISO/IEC series.

See also: [ISO](#iso).

## IEEE
**Institute of Electrical and Electronics Engineers.** The world's largest professional association of engineers. It publishes many standards, including the 802 family for LANs: Ethernet (802.3) and Wi-Fi (802.11).

See also: [802.11](numbers.md#80211), [802.3 Physical Layer](numbers.md#8023-physical-layer).

## IEEE 802.1ah {#ieee-8021ah}
**Provider Backbone Bridges (PBB), or MAC-in-MAC.** An IEEE standard that wraps customer Ethernet frames in a provider's own Ethernet header. Providers can then scale carrier Ethernet without learning customer MAC addresses or running out of VLAN IDs.

See also: [IEEE 802.1Qay](#ieee-8021qay), [VLAN](v.md#vlan).

## IEEE 802.1Qay {#ieee-8021qay}
**Provider Backbone Bridge Traffic Engineering (PBB-TE).** A carrier Ethernet standard that builds on 802.1ah MAC-in-MAC. It removes flooding and spanning tree and has the operator set up paths explicitly, giving predictable, SDH-like behaviour.

See also: [IEEE 802.1ah](#ieee-8021ah), [SDH](s.md#sdh).

## IETF
**Internet Engineering Task Force.** The open standards body that develops internet protocols, such as TCP/IP, HTTP and TLS, and publishes them as RFCs.

See also: [RFC](r.md#rfc).

## IGMP
**Internet Group Management Protocol.** The IPv4 protocol with which hosts tell their local routers which multicast groups they want to receive. IPTV uses it to join channels.

See also: [Multicast](m.md#multicast), [IPTV](#iptv).

## IGP
**Interior Gateway Protocol.** A routing protocol used within one autonomous system, such as OSPF, IS-IS, RIP or EIGRP.

See also: [BGP](b.md#bgp), [OSPF](o.md#ospf), [RIP](r.md#rip).

## IGRP
**Interior Gateway Routing Protocol.** Cisco's original distance-vector routing protocol, which used a composite metric of bandwidth and delay. EIGRP replaced it.

See also: [EIGRP](e.md#eigrp), [RIP](r.md#rip).

## IIS
**Internet Information Services.** Microsoft's web server for Windows Server.

## IKE
**Internet Key Exchange.** The protocol that sets up security associations for IPsec. The peers authenticate each other and agree keys using Diffie-Hellman. IKEv2 is the current version.

See also: [IPSec](#ipsec), [VPN](v.md#vpn).

## iLBC
**Internet Low Bitrate Codec.** A royalty-free narrowband speech codec at about 13 to 15 kbit/s, designed to cope well with packet loss. It was part of WebRTC.

See also: [OPUS](o.md#opus), [Audio Codecs](a.md#audio-codecs).

## iManager
Huawei's network management software for its access equipment, such as MSANs and DSLAMs.

## IMAP
**Internet Message Access Protocol.** The protocol email clients use to read and manage mail held on a server, so that several devices see the same mailbox. It uses port 143, or 993 over TLS.

See also: [POP](p.md#pop).

## Implementation
A synonym for construction, deployment or both, depending on context.

See also: [Construction](c.md#construction), [Deployment](d.md#deployment).

## Implementation Lead
A synonym for the construction lead, the deployment lead or both.

## Implicit Change Control
Control of artefacts, such as source code, that the change control board does not manage directly, but which change only when the controlled artefacts they derive from change.

See also: [Explicit Change Control](e.md#explicit-change-control).

## Implicit Risk Management
See [Intrinsic Risk Management](#intrinsic-risk-management).

## IMS
**IP Multimedia Subsystem.** The 3GPP architecture for delivering voice, video and messaging over IP using SIP. It is the core behind VoLTE, Wi-Fi calling and many fixed-line VoIP networks.

See also: [CSCF](c.md#cscf), [HSS](h.md#hss), [SIP](s.md#sip), [VoLTE](v.md#volte).

## IMSI
**International Mobile Subscriber Identity.** The unique number, of up to 15 digits, that identifies a mobile subscriber, stored on the SIM. It is made up of the mobile country code, the network code and the subscriber number. Networks send it as rarely as possible, using temporary identities instead, to stop tracking.

See also: [SIM](s.md#sim), [HLR](h.md#hlr), [MNC](m.md#mnc).

## IN
**Intelligent Network.** The ITU-T architecture (Q.1200 series) that moves service logic out of telephone switches into separate service control points. Freephone, number translation and prepaid services were built on it.

See also: [INAP](#inap), [CAMEL](c.md#camel), [SS7](s.md#ss7).

## INAP
**Intelligent Network Application Part.** The SS7 protocol, over TCAP, between switches and service control points in an Intelligent Network.

See also: [IN](#in), [TCAP](t.md#tcap), [CAP](c.md#cap).

## Inch-Pebble
See [Miniature Milestone](m.md#miniature-milestone).

## Incremental Development
Building a product in increments, where each version is usable and adds user-visible functionality to the one before.

See also: [Iterative Development](#iterative-development).

## Informal Review
Any review other than an inspection, such as a walkthrough or desk check.

See also: [Inspection](#inspection), [Walkthrough](w.md#walkthrough), [Desk Check](d.md#desk-check).

## Informal Testing
Testing based on the tester's judgement, without documented test cases.

See also: [Formal Testing](f.md#formal-testing), [Exploratory Testing](e.md#exploratory-testing).

## Information architecture
How information in a system or site is organised, structured and labelled so that people can find and understand it.

See also: [Information design](#information-design).

## Information design
Planning the specific information to give a particular audience, and how to present it, to meet given goals.

See also: [Information architecture](#information-architecture).

## Information Radiators
Large, visible displays, such as task boards or burndown charts, placed where the whole team can see the current state of work at a glance.

See also: [Task Board](t.md#task-board), [Kanban Board](k.md#kanban-board), [Burndown Chart](b.md#burndown-chart).

## Ingress
Traffic entering a network or a device, as opposed to egress traffic leaving it.

See also: [Egress](e.md#egress).

## Inspection
A formal review with defined roles (moderator, author, reader, inspectors and scribe), preparation, a logging meeting, rework and follow-up.

See also: [Moderator](m.md#moderator), [Inspector](#inspector), [Reading Inspection](r.md#reading-inspection).

## Inspector
A reviewer in an inspection.

See also: [Inspection](#inspection).

## Institute of Electrical and Electronics Engineers
See [IEEE](#ieee).

## Integrated Development Environment
See [IDE](#ide).

## Integration
Combining software components and making them work together.

See also: [Integration Test](#integration-test), [Continuous Integration](c.md#continuous-integration).

## Integration Test
A test that checks that components work together correctly after they are combined or changed.

See also: [Unit Testing](u.md#unit-testing), [System Test](s.md#system-test).

## Internet Protocol Suite
The protocols of the internet, often called TCP/IP after its two main protocols. It has four layers: link, internet (IP), transport (TCP, UDP) and application (such as HTTP or DNS).

See also: [TCP](t.md#tcp), [UDP](u.md#udp), [IPv4](#ipv4), [IPv6](#ipv6).

## Interpreted Language
A language whose usual implementations run the source, or bytecode compiled from it, through an interpreter rather than compiling it ahead of time to machine code. Python and JavaScript are examples. The distinction is about implementations rather than languages.

See also: [Compiled Language](c.md#compiled-language).

## Intrinsic Risk Management
Managing risk through how a project is run, for example by choosing a lifecycle and practices that expose and reduce risks as a matter of course.

See also: [Extrinsic Risk Management](e.md#extrinsic-risk-management).

## INVEST
A checklist for good user stories: Independent, Negotiable, Valuable, Estimable, Small and Testable.

See also: [User Stories](u.md#user-stories), [Definition of Ready](d.md#definition-of-ready).

## IOS
**Internetwork Operating System.** The operating system on most Cisco routers and switches, known for its command-line interface.

## IPS
**Intrusion Prevention System.** A device or software that watches network or host activity for attacks and policy breaches and blocks them. An intrusion detection system (IDS) only reports them.

See also: [Firewall](f.md#firewall), [DPI](d.md#dpi).

## IPSC
**IP Stream Connect.** A BT Wholesale product that handed over broadband customers' traffic to an internet service provider at a central point.

See also: [ISP](#isp), [L2TP](l.md#l2tp).

## IPSec
**Internet Protocol Security.** A suite of protocols that authenticate and encrypt IP packets, between hosts, between gateways or between a host and a gateway. It is widely used for VPNs; IKE sets up its keys.

See also: [IKE](#ike), [VPN](v.md#vpn), [ePDG](e.md#epdg).

## IPTV
**Internet Protocol Television.** Television delivered over a managed IP network, usually by multicast to a set-top box, rather than by broadcast or the open internet.

See also: [IGMP](#igmp), [STB](s.md#stb), [VOD](v.md#vod).

## IPv4
**Internet Protocol version 4.** The original version of IP, from 1981 (RFC 791), with 32-bit addresses. It still carries much of the internet's traffic, stretched by NAT because its address space is too small.

See also: [IPv6](#ipv6), [NAT](n.md#nat).

## IPv6
**Internet Protocol version 6.** The successor to IPv4, with 128-bit addresses, a simpler header and built-in autoconfiguration. It became an internet standard in 2017 (RFC 8200).

See also: [IPv4](#ipv4), [ICMPv6](#icmpv6), [DNS - AAAA](d.md#dns-aaaa).

## ISDN
**Integrated Services Digital Network.** A set of standards for digital voice and data over the telephone network, using 64 kbit/s channels with separate signalling. It was sold as basic rate (BRI) and primary rate (PRI) access.

See also: [BRI](b.md#bri), [PRI](p.md#pri), [Q.931](q.md#q931), [ISDN2](#isdn2), [ISDN30](#isdn30).

## ISDN2
BT's name for ISDN basic rate access: two 64 kbit/s channels. See [BRI](b.md#bri).

## ISDN30
BT's name for ISDN primary rate access: up to 30 channels on a 2 Mbit/s line. See [PRI](p.md#pri).

## ISO
<!-- vale PyDoc.Spelling = NO -->
**International Organization for Standardization.**
<!-- vale PyDoc.Spelling = YES -->
The international body made up of national standards bodies, such as BSI and ANSI, that publishes standards in almost every field.

See also: [IEC](#iec), [ANSI](a.md#ansi).

## ISP
**Internet Service Provider.** A company that provides internet access, and often related services such as email, hosting and domain registration.

## Issue
Something that needs resolving and could affect the project if left. In this sense it is not already covered by the plan, a change request, a defect or a risk.

See also: [Issue Management](#issue-management), [Issue tracker](#issue-tracker).

## Issue Management
Recording, tracking and resolving a project's issues.

See also: [Issue](#issue).

## Issue tracker
Software that records issues, such as bugs, tasks or support requests, and tracks them from report to resolution.

See also: [Defect Management](d.md#defect-management).

## ISUP
**ISDN User Part.** The SS7 protocol that sets up and clears telephone calls between exchanges, carrying details such as the called number. It is defined in the ITU-T Q.76x series.

See also: [SS7](s.md#ss7), [IUP](#iup), [TUP](t.md#tup).

## ITIL
A widely used framework of good practice for IT service management, covering how services are designed, delivered, run and improved. The name came from the Information Technology Infrastructure Library.

See also: [CMDB](c.md#cmdb), [CCTA](c.md#ccta).

## ITU
**International Telecommunication Union.** The United Nations agency for information and communication technologies. It coordinates the radio spectrum and satellite orbits, and sets telecoms standards through ITU-T.

See also: [ITU-T](#itu-t), [ETSI](e.md#etsi).

## ITU-T
The ITU's standardisation sector, which publishes telecoms standards as Recommendations, such as G.711 and H.323. It was called the CCITT until 1993.

See also: [ITU](#itu), [CCITT](c.md#ccitt).

## IUP
**Interconnect User Part.** The UK national version of SS7 call signalling between operators' networks, formerly called BTNUP.

See also: [ISUP](#isup), [BTNUP](b.md#btnup).

## IVR
**Interactive Voice Response.** A telephone system that talks to callers with recorded or generated speech and responds to their key presses or spoken answers, typically to route calls or serve simple requests.

See also: [DTMF](d.md#dtmf).

## Item
In a backlog or tracker, one unit of work being managed, such as a change request, defect, risk or issue.

See also: [Work Item](w.md#work-item).

## Iteration
A fixed period, or timebox, in which a team develops and delivers a working increment.

See also: [Sprints](s.md#sprints), [Timebox](t.md#timebox).

## Iterative Development
Developing by repeating cycles of work and deliberately revisiting earlier work in the light of feedback, rather than doing each step once.

See also: [Incremental Development](#incremental-development), [Refactoring](r.md#refactoring).
