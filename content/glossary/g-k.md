---
title: Glossary, G to K
---

# G to K

## G

### G.711 {#g711}
The ITU-T standard, from 1972, for coding telephone speech as 64 kbit/s PCM: 8,000 samples a second, each companded to 8 bits. It has two variants, A-law and µ-law. It is the baseline codec that every VoIP system supports.

See also: [A-law](a-c.md#a-law), [Mu-law](l-n.md#mu-law), [PCM](o-r.md#pcm), [G.711.1](#g7111).

### G.711.1 {#g7111}
A wideband extension of G.711, from 2008, that adds layers on top of a G.711 core. It runs at 64, 80 or 96 kbit/s, and a G.711-only receiver can still decode the core.

See also: [G.711](#g711), [G.722](#g722).

### G.719 {#g719}
An ITU-T codec for full-band audio (20 Hz to 20 kHz) at 32 to 128 kbit/s, developed by Polycom and Ericsson for high-quality conferencing. It handles music as well as speech.

See also: [G.722](#g722), [Audio Codecs](a-c.md#audio-codecs).

### G.722 {#g722}
An ITU-T wideband speech codec from 1988, covering 50 to 7,000 Hz at 48 to 64 kbit/s using sub-band ADPCM. It is widely used for HD voice on desk phones. G.722.1 and G.722.2 (AMR-WB) are different codecs despite the names.

See also: [G.711](#g711), [AMR-WB](a-c.md#amr-wb).

### G.723.1 {#g7231}
An ITU-T low-rate speech codec, at 5.3 or 6.3 kbit/s, with 30 ms frames. It was common in early VoIP and H.323 systems. It is unrelated to the older G.723.

See also: [G.726](#g726), [H.323](#h323).

### G.726 {#g726}
An ITU-T ADPCM speech codec at 16, 24, 32 or 40 kbit/s, which replaced G.721 and G.723. The 32 kbit/s rate, half that of G.711, is the most used, for example in DECT cordless phones.

See also: [G.711](#g711), [PCM](o-r.md#pcm).

### G.Fast {#gfast}
An ITU-T DSL standard (G.9700 and G.9701) for very short copper lines, up to a few hundred metres, giving several hundred megabits per second. It is used from a distribution point or cabinet fed by fibre.

See also: [VDSL](s-z.md#vdsl), [DSL](d-f.md#dsl), [DP](d-f.md#dp).

### Gantt chart
A bar chart of a project schedule, with tasks down the side and time along the top. It shows when each task starts and ends, and how the tasks depend on each other.

See also: [PERT chart](o-r.md#pert-chart), [CPM](a-c.md#cpm).

### Gap analysis
Comparing where things are now with where they need to be, to find what must change to get there.

### Gate
A set of criteria that must be met before work can pass from one phase or stage to the next.

See also: [Gate Checklist](#gate-checklist), [Phase](o-r.md#phase).

### Gate Checklist
A checklist used to check that the criteria for a gate have been met.

See also: [Gate](#gate).

### GBE / GE {#gbe-ge}
Abbreviations for [Gigabit Ethernet](#gigabit-ethernet).

### GCHQ
**Government Communications Headquarters.** The UK's signals intelligence and security agency, based in Cheltenham. It grew out of the Government Code and Cypher School of Bletchley Park, and runs the National Cyber Security Centre.

See also: [NCSC](l-n.md#ncsc), [CESG](a-c.md#cesg).

### Geocast
Delivering a message to all the nodes in a geographical area, rather than to a list of addresses. It is a form of multicast used in some mobile ad hoc and vehicle networks.

See also: [Multicast](l-n.md#multicast), [MANET](l-n.md#manet).

### GERAN
**GSM EDGE Radio Access Network.** The radio access network of GSM and EDGE: the base stations, their controllers and the interfaces between them. 3GPP maintains its standards.

See also: [BTS](a-c.md#bts), [BSC](a-c.md#bsc), [EDGE](d-f.md#edge), [UTRAN](s-z.md#utran).

### GGSN
**Gateway GPRS Support Node.** The GPRS and UMTS core node that connects the mobile packet network to external networks such as the internet. It allocates the device's IP address and anchors the session as the user moves. In LTE the PGW does this job.

See also: [SGSN](s-z.md#sgsn), [GPRS](#gprs), [APN](a-c.md#apn), [PGW](o-r.md#pgw).

### Gherkin
The plain-language format used by Cucumber and similar tools to write behaviour-driven tests. Scenarios are written as `Given`, `When` and `Then` steps under a `Feature`, so that business people and developers can read the same tests.

See also: [BDD](a-c.md#bdd), [Given When Then](#given-when-then).

### Gigabit Ethernet
Ethernet at 1 Gbit/s, defined in IEEE 802.3. It replaced Fast Ethernet as the usual speed for wired networks from the early 2000s.

See also: [GBE / GE](#gbe-ge), [100 Mbps (Fast Ethernet)](s-z.md#100-mbps-fast-ethernet), [Ethernet over twisted pair](d-f.md#ethernet-over-twisted-pair).

### Git
A distributed version control system, created by Linus Torvalds in 2005 for the Linux kernel. Every clone holds the full history, so most work is local and fast, and branching and merging are cheap.

See also: [Version Control](s-z.md#version-control), [Subversion](s-z.md#subversion).

### Given When Then
A template for writing acceptance criteria and tests: given some context, when an action happens, then expect these results.

See also: [Gherkin](#gherkin), [BDD](a-c.md#bdd).

### GMSC
**Gateway Mobile Switching Centre.** An MSC function that routes calls between the mobile network and other networks. For an incoming call it asks the HLR where the subscriber is.

See also: [MSC](l-n.md#msc), [HLR](#hlr).

### GNU
**GNU's Not Unix.** The free software operating system started by Richard Stallman in 1983, made up of tools, libraries and compilers. Combined with the Linux kernel, it forms most Linux distributions.

See also: [GPL](#gpl), [Linux](l-n.md#linux), [Copyleft](a-c.md#copyleft).

### Go
A statically typed, compiled language created at Google in 2009 by Robert Griesemer, Rob Pike and Ken Thompson. It has garbage collection, built-in concurrency with goroutines and channels, and fast builds. It is also called Golang.

### Goals
The results a project, process or activity is meant to achieve. Also called objectives.

See also: [Objectives](o-r.md#objectives).

### GoF
**Gang of Four.** The four authors (Gamma, Helm, Johnson and Vlissides) of *Design Patterns: Elements of Reusable Object-Oriented Software* (1994). The book catalogues 23 object-oriented design patterns.

See also: [Design Pattern](d-f.md#design-pattern).

### Google Cloud Platform
Google's cloud computing services, offering infrastructure, platform and serverless computing, data analytics and machine learning on the infrastructure Google uses itself.

See also: [AWS](a-c.md#aws), [Azure](a-c.md#azure).

### GPL
<!-- vale PyDoc.Spelling = NO -->
**GNU General Public License.**
<!-- vale PyDoc.Spelling = YES -->
The most widely used copyleft free software licence, written by Richard Stallman. It lets anyone run, study, share and change the software, as long as they share copies and derived works under the same licence.

See also: [Copyleft](a-c.md#copyleft), [GNU](#gnu).

### GPRS
**General Packet Radio Service.** The packet data service added to GSM, giving always-on connections charged by data volume rather than by time. It is best-effort, with speeds of tens of kilobits per second.

See also: [GSM](#gsm), [EDGE](d-f.md#edge), [SGSN](s-z.md#sgsn), [GGSN](#ggsn).

### GSM
**Global System for Mobile communications.** The second-generation (2G) digital mobile standard, developed by ETSI and first launched in 1991. It was designed for circuit-switched voice and SMS, and GPRS and EDGE later added data.

See also: [GPRS](#gprs), [EDGE](d-f.md#edge), [UMTS](s-z.md#umts), [SIM](s-z.md#sim).

### GSM AMR
The AMR speech codec as used in GSM. See [AMR-NB](a-c.md#amr-nb).

### GSM-FR
**GSM Full Rate.** The first GSM speech codec (GSM 06.10), at 13 kbit/s. Its quality is poor by modern standards; Enhanced Full Rate and AMR replaced it.

See also: [GSM AMR](#gsm-amr), [AMR-NB](a-c.md#amr-nb).

### GSM-R
**GSM for Railways.** A version of GSM for railway voice and data, including the signalling of the European Rail Traffic Management System. It is designed to work at train speeds up to 500 km/h.

See also: [GSM](#gsm).

### GSN
**GPRS Support Node.** A node in the GPRS core network: either a serving node (SGSN) or a gateway node (GGSN).

See also: [SGSN](s-z.md#sgsn), [GGSN](#ggsn).

## H

### H.248 {#h248}
**Gateway Control Protocol (Megaco).** The ITU-T and IETF protocol with which a media gateway controller or softswitch controls media gateways, which convert between telephone circuits and IP media streams. It does the same job as MGCP.

See also: [MGCP](l-n.md#mgcp), [MGW](l-n.md#mgw), [Softswitch](s-z.md#softswitch).

### H.323 {#h323}
An ITU-T family of protocols for voice and video calls over packet networks, covering signalling, media and bandwidth control. It was the main VoIP standard before SIP replaced it.

See also: [SIP](s-z.md#sip), [Q.931](o-r.md#q931), [RAS](o-r.md#ras).

### Half Duplex
Communication in which both ends can send, but only one at a time, like a push-to-talk radio.

See also: [Duplex](d-f.md#duplex), [Full duplex](d-f.md#full-duplex), [Simplex](s-z.md#simplex).

### Happy Path
See [Nominal Path](l-n.md#nominal-path).

### Hash Function
A function that maps data of any size to a fixed-size value. A cryptographic hash, such as SHA-256, is also one-way and collision-resistant. That makes it useful for integrity checks, digital signatures and storing passwords.

See also: [SHA](s-z.md#sha), [MD5](l-n.md#md5), [CRC](a-c.md#crc).

### HDF
**Handover Distribution Frame.** In UK local loop unbundling, the frame in the exchange where the copper pairs are handed over from the main distribution frame to another operator's equipment.

See also: [MDF](l-n.md#mdf), [Local Loop](l-n.md#local-loop).

### HDLC
**High-Level Data Link Control.** An ISO bit-oriented, synchronous data link protocol. Many other link protocols, including PPP framing, LAPB in X.25 and LAPD in ISDN, are based on it.

See also: [PPP](o-r.md#ppp), [X.25](s-z.md#x25), [Frame Relay](d-f.md#frame-relay).

### HDSL
**High-bit-rate Digital Subscriber Line.** A symmetrical DSL that carries a 2 Mbit/s (E1) or 1.5 Mbit/s (T1) circuit over two or three copper pairs. It was used to deliver leased lines without new cable.

See also: [SDSL](s-z.md#sdsl), [DSL](d-f.md#dsl).

### Heartbeat Retrospective
A retrospective held at a regular interval, such as the end of each iteration, in which the team reflects on recent events and agrees improvements.

See also: [Sprint retrospective](s-z.md#sprint-retrospective).

### HiFi Prototype
See [High Fidelity Prototype](#high-fidelity-prototype).

### High Fidelity Prototype
A prototype that looks and behaves much like the finished system, usually built with real development tools.

See also: [Low Fidelity Prototype](l-n.md#low-fidelity-prototype), [User Interface Prototype](s-z.md#user-interface-prototype).

### High Level Design
**HLD.** The design level between the architecture and the low-level design. It defines the components of the solution, their interfaces and how they interact, without going into how each is built.

See also: [Low Level Design](l-n.md#low-level-design), [Architecture](a-c.md#architecture).

### HLD
See [High Level Design](#high-level-design).

### HLR
**Home Location Register.** The central database of a GSM or UMTS network, holding each subscriber's details: their IMSI, phone numbers, services and current location. In LTE and IMS, the HSS replaced it.

See also: [VLR](s-z.md#vlr), [HSS](#hss), [IMSI](#imsi), [MSC](l-n.md#msc).

### Hotfix
A small, urgent change, sometimes called a patch, that fixes a bug in released software outside the normal release cycle.

See also: [Release](o-r.md#release).

### How Requirement
Usually a synonym for [Non-functional Requirement](l-n.md#non-functional-requirement); sometimes used for design constraints.

### How Well Requirement
See [Non-functional Requirement](l-n.md#non-functional-requirement).

### HSRP
**Hot Standby Router Protocol.** Cisco's protocol for a fault-tolerant default gateway. Two or more routers share a virtual IP address; one is active and the others take over if it fails. VRRP is the open-standard equivalent.

See also: [Router](o-r.md#router).

### HSS
**Home Subscriber Server.** The master subscriber database for IMS and LTE, holding user profiles and authentication data and tracking where users are registered. It takes over the jobs of the HLR and the authentication centre.

See also: [HLR](#hlr), [IMS](#ims), [CSCF](a-c.md#cscf), [MME](l-n.md#mme).

### HTTP
**Hypertext Transfer Protocol.** The request-response protocol of the web. A client asks for a resource by URL with a method such as `GET` or `POST`, and the server returns a status and content. HTTP/2 and HTTP/3 keep the same model with more efficient transports.

See also: [HTTPS](#https), [REST](o-r.md#rest), [URL](s-z.md#url).

### HTTPS
HTTP over TLS. It encrypts the traffic and lets the client check the server's identity through its certificate, protecting against eavesdropping and tampering.

See also: [HTTP](#http), [TLS](s-z.md#tls), [CA](a-c.md#ca).

### Hub
A network device that repeats every frame it receives to all its other ports, so all connected devices share one collision domain. It works at layer 1, and switches have replaced it.

See also: [Switch](s-z.md#switch), [L1](l-n.md#l1).

### Human factors
The study of how people behave, physically and mentally, with products, systems and environments, and how to design for them.

See also: [User Experience](s-z.md#user-experience).

### Hungarian notation
A naming convention in which a prefix on an identifier shows its kind or type, such as `cApples` for a count or `szName` for a zero-terminated string. Most modern style guides advise against encoding the type in this way.

See also: [Camel Case](a-c.md#camel-case), [Snake Case](s-z.md#snake-case).

## I

### IA
**Information Assurance.** Managing the risks to information and the systems that handle it, so that it keeps its confidentiality, integrity, availability, authenticity and non-repudiation.

See also: [CESG](a-c.md#cesg), [NCSC](l-n.md#ncsc).

### IaaS
**Infrastructure as a Service.** Cloud computing that rents virtual machines, storage and networks, which the customer manages from the operating system up.

See also: [PaaS](o-r.md#paas), [SaaS](s-z.md#saas), [NaaS](l-n.md#naas).

### ICE
**Interactive Connectivity Establishment.** A technique, defined in RFC 8445, for finding the most direct working path between two peers behind NATs and firewalls. It tries candidate addresses gathered with STUN and TURN. SIP and WebRTC media use it.

See also: [STUN](s-z.md#stun), [NAT](l-n.md#nat).

### ICMP
**Internet Control Message Protocol.** The IP protocol that carries error and diagnostic messages, such as "destination unreachable" and the echo request and reply used by `ping`.

See also: [ICMPv6](#icmpv6), [Internet Protocol Suite](#internet-protocol-suite).

### ICMPv6
ICMP for IPv6, defined in RFC 4443. As well as errors and `ping`, it carries Neighbour Discovery, which replaces ARP, and Multicast Listener Discovery, which replaces IGMP.

See also: [ICMP](#icmp), [IPv6](#ipv6).

### IDE
**Integrated Development Environment.** An application that combines a code editor, build tools and a debugger, and often much more, for writing software.

See also: [Integrated Development Environment](#integrated-development-environment).

### IDQ
**Informatica Data Quality.** Informatica's tool for profiling, cleansing and standardising enterprise data.

See also: [DQ](d-f.md#dq).

### IEC
**International Electrotechnical Commission.** The international body that publishes standards for electrical and electronic technologies. It works with ISO on information technology standards, such as the ISO/IEC series.

See also: [ISO](#iso).

### IEEE
**Institute of Electrical and Electronics Engineers.** The world's largest professional association of engineers. It publishes many standards, including the 802 family for LANs: Ethernet (802.3) and Wi-Fi (802.11).

See also: [802.11](s-z.md#80211), [802.3 Physical Layer](s-z.md#8023-physical-layer).

### IEEE 802.1ah {#ieee-8021ah}
**Provider Backbone Bridges (PBB), or MAC-in-MAC.** An IEEE standard that wraps customer Ethernet frames in a provider's own Ethernet header. Providers can then scale carrier Ethernet without learning customer MAC addresses or running out of VLAN IDs.

See also: [IEEE 802.1Qay](#ieee-8021qay), [VLAN](s-z.md#vlan).

### IEEE 802.1Qay {#ieee-8021qay}
**Provider Backbone Bridge Traffic Engineering (PBB-TE).** A carrier Ethernet standard that builds on 802.1ah MAC-in-MAC. It removes flooding and spanning tree and has the operator set up paths explicitly, giving predictable, SDH-like behaviour.

See also: [IEEE 802.1ah](#ieee-8021ah), [SDH](s-z.md#sdh).

### IETF
**Internet Engineering Task Force.** The open standards body that develops internet protocols, such as TCP/IP, HTTP and TLS, and publishes them as RFCs.

See also: [RFC](o-r.md#rfc).

### IGMP
**Internet Group Management Protocol.** The IPv4 protocol with which hosts tell their local routers which multicast groups they want to receive. IPTV uses it to join channels.

See also: [Multicast](l-n.md#multicast), [IPTV](#iptv).

### IGP
**Interior Gateway Protocol.** A routing protocol used within one autonomous system, such as OSPF, IS-IS, RIP or EIGRP.

See also: [BGP](a-c.md#bgp), [OSPF](o-r.md#ospf), [RIP](o-r.md#rip).

### IGRP
**Interior Gateway Routing Protocol.** Cisco's original distance-vector routing protocol, which used a composite metric of bandwidth and delay. EIGRP replaced it.

See also: [EIGRP](d-f.md#eigrp), [RIP](o-r.md#rip).

### IIS
**Internet Information Services.** Microsoft's web server for Windows Server.

### IKE
**Internet Key Exchange.** The protocol that sets up security associations for IPsec. The peers authenticate each other and agree keys using Diffie-Hellman. IKEv2 is the current version.

See also: [IPSec](#ipsec), [VPN](s-z.md#vpn).

### iLBC
**Internet Low Bitrate Codec.** A royalty-free narrowband speech codec at about 13 to 15 kbit/s, designed to cope well with packet loss. It was part of WebRTC.

See also: [OPUS](o-r.md#opus), [Audio Codecs](a-c.md#audio-codecs).

### iManager
Huawei's network management software for its access equipment, such as MSANs and DSLAMs.

### IMAP
**Internet Message Access Protocol.** The protocol email clients use to read and manage mail held on a server, so that several devices see the same mailbox. It uses port 143, or 993 over TLS.

See also: [POP](o-r.md#pop).

### Implementation
A synonym for construction, deployment or both, depending on context.

See also: [Construction](a-c.md#construction), [Deployment](d-f.md#deployment).

### Implementation Lead
A synonym for the construction lead, the deployment lead or both.

### Implicit Change Control
Control of artefacts, such as source code, that the change control board does not manage directly, but which change only when the controlled artefacts they derive from change.

See also: [Explicit Change Control](d-f.md#explicit-change-control).

### Implicit Risk Management
See [Intrinsic Risk Management](#intrinsic-risk-management).

### IMS
**IP Multimedia Subsystem.** The 3GPP architecture for delivering voice, video and messaging over IP using SIP. It is the core behind VoLTE, Wi-Fi calling and many fixed-line VoIP networks.

See also: [CSCF](a-c.md#cscf), [HSS](#hss), [SIP](s-z.md#sip), [VoLTE](s-z.md#volte).

### IMSI
**International Mobile Subscriber Identity.** The unique number, of up to 15 digits, that identifies a mobile subscriber, stored on the SIM. It is made up of the mobile country code, the network code and the subscriber number. Networks send it as rarely as possible, using temporary identities instead, to stop tracking.

See also: [SIM](s-z.md#sim), [HLR](#hlr), [MNC](l-n.md#mnc).

### IN
**Intelligent Network.** The ITU-T architecture (Q.1200 series) that moves service logic out of telephone switches into separate service control points. Freephone, number translation and prepaid services were built on it.

See also: [INAP](#inap), [CAMEL](a-c.md#camel), [SS7](s-z.md#ss7).

### INAP
**Intelligent Network Application Part.** The SS7 protocol, over TCAP, between switches and service control points in an Intelligent Network.

See also: [IN](#in), [TCAP](s-z.md#tcap), [CAP](a-c.md#cap).

### Inch-Pebble
See [Miniature Milestone](l-n.md#miniature-milestone).

### Incremental Development
Building a product in increments, where each version is usable and adds user-visible functionality to the one before.

See also: [Iterative Development](#iterative-development).

### Informal Review
Any review other than an inspection, such as a walkthrough or desk check.

See also: [Inspection](#inspection), [Walkthrough](s-z.md#walkthrough), [Desk Check](d-f.md#desk-check).

### Informal Testing
Testing based on the tester's judgement, without documented test cases.

See also: [Formal Testing](d-f.md#formal-testing), [Exploratory Testing](d-f.md#exploratory-testing).

### Information architecture
How information in a system or site is organised, structured and labelled so that people can find and understand it.

See also: [Information design](#information-design).

### Information design
Planning the specific information to give a particular audience, and how to present it, to meet given goals.

See also: [Information architecture](#information-architecture).

### Information Radiators
Large, visible displays, such as task boards or burndown charts, placed where the whole team can see the current state of work at a glance.

See also: [Task Board](s-z.md#task-board), [Kanban Board](#kanban-board), [Burndown Chart](a-c.md#burndown-chart).

### Ingress
Traffic entering a network or a device, as opposed to egress traffic leaving it.

See also: [Egress](d-f.md#egress).

### Inspection
A formal review with defined roles (moderator, author, reader, inspectors and scribe), preparation, a logging meeting, rework and follow-up.

See also: [Moderator](l-n.md#moderator), [Inspector](#inspector), [Reading Inspection](o-r.md#reading-inspection).

### Inspector
A reviewer in an inspection.

See also: [Inspection](#inspection).

### Institute of Electrical and Electronics Engineers
See [IEEE](#ieee).

### Integrated Development Environment
See [IDE](#ide).

### Integration
Combining software components and making them work together.

See also: [Integration Test](#integration-test), [Continuous Integration](a-c.md#continuous-integration).

### Integration Test
A test that checks that components work together correctly after they are combined or changed.

See also: [Unit Testing](s-z.md#unit-testing), [System Test](s-z.md#system-test).

### Internet Protocol Suite
The protocols of the internet, often called TCP/IP after its two main protocols. It has four layers: link, internet (IP), transport (TCP, UDP) and application (such as HTTP or DNS).

See also: [TCP](s-z.md#tcp), [UDP](s-z.md#udp), [IPv4](#ipv4), [IPv6](#ipv6).

### Interpreted Language
A language whose usual implementations run the source, or bytecode compiled from it, through an interpreter rather than compiling it ahead of time to machine code. Python and JavaScript are examples. The distinction is about implementations rather than languages.

See also: [Compiled Language](a-c.md#compiled-language).

### Intrinsic Risk Management
Managing risk through how a project is run, for example by choosing a lifecycle and practices that expose and reduce risks as a matter of course.

See also: [Extrinsic Risk Management](d-f.md#extrinsic-risk-management).

### INVEST
A checklist for good user stories: Independent, Negotiable, Valuable, Estimable, Small and Testable.

See also: [User Stories](s-z.md#user-stories), [Definition of Ready](d-f.md#definition-of-ready).

### IOS
**Internetwork Operating System.** The operating system on most Cisco routers and switches, known for its command-line interface.

### IPS
**Intrusion Prevention System.** A device or software that watches network or host activity for attacks and policy breaches and blocks them. An intrusion detection system (IDS) only reports them.

See also: [Firewall](d-f.md#firewall), [DPI](d-f.md#dpi).

### IPSC
**IP Stream Connect.** A BT Wholesale product that handed over broadband customers' traffic to an internet service provider at a central point.

See also: [ISP](#isp), [L2TP](l-n.md#l2tp).

### IPSec
**Internet Protocol Security.** A suite of protocols that authenticate and encrypt IP packets, between hosts, between gateways or between a host and a gateway. It is widely used for VPNs; IKE sets up its keys.

See also: [IKE](#ike), [VPN](s-z.md#vpn), [ePDG](d-f.md#epdg).

### IPTV
**Internet Protocol Television.** Television delivered over a managed IP network, usually by multicast to a set-top box, rather than by broadcast or the open internet.

See also: [IGMP](#igmp), [STB](s-z.md#stb), [VOD](s-z.md#vod).

### IPv4
**Internet Protocol version 4.** The original version of IP, from 1981 (RFC 791), with 32-bit addresses. It still carries much of the internet's traffic, stretched by NAT because its address space is too small.

See also: [IPv6](#ipv6), [NAT](l-n.md#nat).

### IPv6
**Internet Protocol version 6.** The successor to IPv4, with 128-bit addresses, a simpler header and built-in autoconfiguration. It became an internet standard in 2017 (RFC 8200).

See also: [IPv4](#ipv4), [ICMPv6](#icmpv6), [DNS - AAAA](d-f.md#dns-aaaa).

### ISDN
**Integrated Services Digital Network.** A set of standards for digital voice and data over the telephone network, using 64 kbit/s channels with separate signalling. It was sold as basic rate (BRI) and primary rate (PRI) access.

See also: [BRI](a-c.md#bri), [PRI](o-r.md#pri), [Q.931](o-r.md#q931), [ISDN2](#isdn2), [ISDN30](#isdn30).

### ISDN2
BT's name for ISDN basic rate access: two 64 kbit/s channels. See [BRI](a-c.md#bri).

### ISDN30
BT's name for ISDN primary rate access: up to 30 channels on a 2 Mbit/s line. See [PRI](o-r.md#pri).

### ISO
<!-- vale PyDoc.Spelling = NO -->
**International Organization for Standardization.**
<!-- vale PyDoc.Spelling = YES -->
The international body made up of national standards bodies, such as BSI and ANSI, that publishes standards in almost every field.

See also: [IEC](#iec), [ANSI](a-c.md#ansi).

### ISP
**Internet Service Provider.** A company that provides internet access, and often related services such as email, hosting and domain registration.

### Issue
Something that needs resolving and could affect the project if left. In this sense it is not already covered by the plan, a change request, a defect or a risk.

See also: [Issue Management](#issue-management), [Issue tracker](#issue-tracker).

### Issue Management
Recording, tracking and resolving a project's issues.

See also: [Issue](#issue).

### Issue tracker
Software that records issues, such as bugs, tasks or support requests, and tracks them from report to resolution.

See also: [Defect Management](d-f.md#defect-management).

### ISUP
**ISDN User Part.** The SS7 protocol that sets up and clears telephone calls between exchanges, carrying details such as the called number. It is defined in the ITU-T Q.76x series.

See also: [SS7](s-z.md#ss7), [IUP](#iup), [TUP](s-z.md#tup).

### ITIL
A widely used framework of good practice for IT service management, covering how services are designed, delivered, run and improved. The name came from the Information Technology Infrastructure Library.

See also: [CMDB](a-c.md#cmdb), [CCTA](a-c.md#ccta).

### ITU
**International Telecommunication Union.** The United Nations agency for information and communication technologies. It coordinates the radio spectrum and satellite orbits, and sets telecoms standards through ITU-T.

See also: [ITU-T](#itu-t), [ETSI](d-f.md#etsi).

### ITU-T
The ITU's standardisation sector, which publishes telecoms standards as Recommendations, such as G.711 and H.323. It was called the CCITT until 1993.

See also: [ITU](#itu), [CCITT](a-c.md#ccitt).

### IUP
**Interconnect User Part.** The UK national version of SS7 call signalling between operators' networks, formerly called BTNUP.

See also: [ISUP](#isup), [BTNUP](a-c.md#btnup).

### IVR
**Interactive Voice Response.** A telephone system that talks to callers with recorded or generated speech and responds to their key presses or spoken answers, typically to route calls or serve simple requests.

See also: [DTMF](d-f.md#dtmf).

### Item
In a backlog or tracker, one unit of work being managed, such as a change request, defect, risk or issue.

See also: [Work Item](s-z.md#work-item).

### Iteration
A fixed period, or timebox, in which a team develops and delivers a working increment.

See also: [Sprints](s-z.md#sprints), [Timebox](s-z.md#timebox).

### Iterative Development
Developing by repeating cycles of work and deliberately revisiting earlier work in the light of feedback, rather than doing each step once.

See also: [Incremental Development](#incremental-development), [Refactoring](o-r.md#refactoring).

## J

### Java
A class-based, object-oriented language released by Sun Microsystems in 1995. It compiles to bytecode that runs on the Java virtual machine, so the same code runs on any platform that has one.

See also: [JavaScript](#javascript), [C#](a-c.md#c_2).

### JavaScript
The scripting language of the web, run by every browser and, through Node.js, on servers. It is dynamic and supports object-oriented, functional and event-driven styles. It is standardised as ECMAScript.

See also: [JSON](#json), [Java](#java).

### Jitter
Variation in the timing of a signal or in the delay of packets. In packet networks it is also called packet delay variation, and it affects real-time traffic such as voice and video.

See also: [Jitter buffer](#jitter-buffer), [Latency](l-n.md#latency).

### Jitter buffer
A buffer at a receiver that holds arriving voice or video packets for a short time, so they can be played out at an even rate despite jitter. Adaptive buffers change their size to match conditions, trading delay against loss.

See also: [Jitter](#jitter), [RTP](o-r.md#rtp).

### Joint Application Development
**JAD.** A facilitated workshop in which customer representatives and developers draft requirements together.

See also: [RAD](o-r.md#rad).

### JSON
**JavaScript Object Notation.** A lightweight text format for data made of objects (name and value pairs) and arrays, defined in RFC 8259. It is the usual format for web APIs.

See also: [JSON-RPC](#json-rpc), [YAML](s-z.md#yaml), [XML](s-z.md#xml), [CBOR](a-c.md#cbor).

### JSON-RPC
A simple remote procedure call protocol that encodes calls and results in JSON.

See also: [XML-RPC](s-z.md#xml-rpc), [RPC](o-r.md#rpc).

## K

### K & R {#k-r}
**Kernighan and Ritchie.** Brian Kernighan and Dennis Ritchie of Bell Labs, authors of *The C Programming Language* (1978). Ritchie created C and, with Ken Thompson, Unix.

See also: [K & R C](#k-r-c), [C Language](a-c.md#c-language).

### K & R C {#k-r-c}
The version of C described in the first edition of Kernighan and Ritchie's book, which served as its informal specification before the ANSI standard of 1989.

See also: [K & R](#k-r), [C Language](a-c.md#c-language).

### K & R indent style {#k-r-indent-style}
The brace style used in Kernighan and Ritchie's book. A function's opening brace goes on its own line, while blocks inside the function open on the same line as their control statement.

See also: [Construction Standard](a-c.md#construction-standard).

### Kanban
A method for managing knowledge work by making the workflow visible, limiting work in progress and improving the flow step by step.

See also: [Kanban Board](#kanban-board), [Lean](l-n.md#lean).

### Kanban Board
A board with a column for each stage of a workflow, on which cards representing work items move from left to right.

See also: [Kanban](#kanban), [Task Board](s-z.md#task-board).

### KDL
A document language with XML-like semantics and a syntax that looks like a series of commands. It is used for configuration and data, like JSON, YAML or XML.

See also: [YAML](s-z.md#yaml), [TOML](s-z.md#toml).

### Kerberos
A network authentication protocol, developed at MIT, in which a trusted key distribution centre issues time-limited tickets. Clients and services then prove their identities to each other without sending passwords. Windows Active Directory uses it.

See also: [AD](a-c.md#ad), [LDAP](l-n.md#ldap).

### Kernel
The core of an operating system, which runs with full control of the hardware. It manages processes, memory, devices and system calls, and keeps applications apart from each other.

See also: [Linux](l-n.md#linux), [Driver](d-f.md#driver).

### KISS Principle
**Keep it simple, stupid.** The principle that most systems work best when kept simple, and that unnecessary complexity should be avoided.

See also: [Rule of Simplicity](o-r.md#rule-of-simplicity), [Simple Design](s-z.md#simple-design).

### Knowledge Management
**KM.** Capturing, sharing and reusing an organisation's knowledge so that people can find what they need.

See also: [Wiki](s-z.md#wiki).

### KPI
**Key Performance Indicator.** A measure of how well an organisation or activity is meeting an important goal.

See also: [Metric](l-n.md#metric), [SLA](s-z.md#sla).

### Ksh
The KornShell, a Unix shell written by David Korn at Bell Labs in the early 1980s. It is compatible with the Bourne shell and adds features from the C shell.

See also: [Sh](s-z.md#sh), [Bash](a-c.md#bash), [Csh](a-c.md#csh).
