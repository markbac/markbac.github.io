---
title: Glossary, O to R
---

# O to R

## O

### Objective C
An object-oriented language that adds Smalltalk-style messaging to C. It was Apple's main language for macOS and iOS apps until Swift arrived.

See also: [Swift](s-z.md#swift), [C Language](a-c.md#c-language).

### Objectives
See [Goals](g-k.md#goals).

### ODF
**Optical Distribution Frame.** A frame that terminates fibre cables and lets connections between them be made and changed with patch leads.

See also: [MDF](l-n.md#mdf), [OFC](#ofc).

### OFC
**Optical Fibre Connector.** A connector that joins optical fibres, aligning their cores so light passes with little loss. It is quicker to connect and disconnect than a splice. Common types include LC, SC and ST.

See also: [ODF](#odf).

### Ofcom
**Office of Communications.** The UK regulator for broadcasting, telecoms, post and the radio spectrum, set up under the Communications Act 2003.

### OFDMA
**Orthogonal Frequency-Division Multiple Access.** The multi-user form of OFDM, in which different users get different sets of closely spaced subcarriers at the same time. LTE downlinks, 5G and Wi-Fi 6 use it.

See also: [SC-FDMA](s-z.md#sc-fdma), [COFDM](a-c.md#cofdm), [LTE (4G)](l-n.md#lte-4g).

### OO
**Object-Oriented.** A paradigm that organises software around objects, which bundle data with the code that acts on it. Most OO languages are class-based, with inheritance and polymorphism.

See also: [Programming paradigm](#programming-paradigm), [Polymorphism](#polymorphism), [UML](s-z.md#uml).

### Operations Plan
A plan for running a system after deployment: roles, responsibilities, procedures and maintenance schedules.

See also: [Deployment Plan](d-f.md#deployment-plan), [Maintenance Plan](l-n.md#maintenance-plan).

### OPUS
**Opus.** An open, royalty-free audio codec, standardised by the IETF in RFC 6716. It combines the SILK speech coder with the CELT low-delay coder and adapts from narrowband speech to full-band music. It is the standard codec for WebRTC.

See also: [SPEEX](s-z.md#speex), [Vorbis](s-z.md#vorbis), [Audio Codecs](a-c.md#audio-codecs).

### OS X
**macOS.** Apple's operating system for Mac computers, released in 2001 as Mac OS X and renamed OS X and then macOS. It is a Unix system built on the Darwin kernel.

See also: [Unix](s-z.md#unix).

### OSA-FC
**Optical Spectrum Access Filter Connect.** An Openreach service that gives a provider a managed fibre connection on which it runs its own optical equipment. It works like dark fibre, but Openreach monitors and repairs the link.

See also: [Dark Fibre](d-f.md#dark-fibre), [EAD](d-f.md#ead).

### OSPF
**Open Shortest Path First.** A link-state interior gateway protocol: each router learns the whole topology of its area and calculates the shortest paths. Version 2 (RFC 2328) is for IPv4 and version 3 for IPv6.

See also: [IGP](g-k.md#igp), [RIP](#rip), [BGP](a-c.md#bgp).

### OSS
**Operations Support Systems.** The systems a telecoms operator uses to run its network, such as inventory, provisioning, configuration, fault and performance management. They work with the business support systems (BSS).

See also: [BSS](a-c.md#bss), [Mediation](l-n.md#mediation).

### OTN
**Optical Transport Network.** The ITU-T G.709 standard for carrying client signals, such as Ethernet or SDH, over wavelengths. It adds framing, forward error correction and management to optical networks.

See also: [SDH](s-z.md#sdh).

### Out-of-order delivery
Packets arriving in a different order from the one in which they were sent, for example because they took different paths. TCP puts the data back in order; real-time protocols must cope with it.

See also: [TCP](s-z.md#tcp), [Jitter buffer](g-k.md#jitter-buffer).

### Overlap Dialling
Sending a dialled number in pieces as the caller enters it, rather than all at once, so that routing can begin before the number is complete. The far end waits for more digits until a timer runs out.

See also: [ISUP](g-k.md#isup), [Q.931](#q931).

## P

### PaaS
**Platform as a Service.** Cloud computing that provides a managed platform for building and running applications, so the customer does not manage servers or operating systems.

See also: [IaaS](g-k.md#iaas), [SaaS](s-z.md#saas).

### Packet sniffing
Capturing and decoding the packets crossing a network, usually with a packet analyser such as Wireshark, to troubleshoot problems or, in an attack, to steal data.

See also: [Wireshark](s-z.md#wireshark), [DPI](d-f.md#dpi).

### Packet Switched
A network that splits data into packets, each with a header that routers use to forward it independently, sharing links with other traffic. The internet works this way.

See also: [Circuit Switched](a-c.md#circuit-switched).

### PAF
**Postcode Address File.** Royal Mail's database of every UK delivery address and its postcode.

### Pair Programming
Two developers working together at one computer: one writes the code while the other reviews it and thinks ahead, and they swap often.

See also: [Mob Programming](l-n.md#mob-programming), [XP](s-z.md#xp).

### PAP
**Password Authentication Protocol.** A simple PPP authentication method that sends the username and password in clear text. It should be used only when nothing stronger, such as CHAP or EAP, is available.

See also: [CHAP](a-c.md#chap), [PPP](#ppp).

### Parametric Estimation
Estimating with a model that calculates effort, cost or schedule from input factors, using formulas based on historical data. COCOMO is an example.

See also: [Estimation](d-f.md#estimation), [Statistical Estimation](s-z.md#statistical-estimation).

### Pascal
A procedural language designed by Niklaus Wirth around 1970 to teach structured programming. Object Pascal and Delphi descend from it.

See also: [Delphi](d-f.md#delphi), [Ada](a-c.md#ada).

### Pattern
A reusable template or model for creating an artefact or solving a recurring problem.

See also: [Design Pattern](d-f.md#design-pattern), [Antipattern](a-c.md#antipattern).

### PCM
**Pulse-Code Modulation.** The standard way of representing an analogue signal digitally: sample it at regular intervals and quantise each sample to a binary value. Telephone speech uses 8,000 samples a second at 8 bits (G.711), and CDs use 44,100 at 16 bits.

See also: [G.711](g-k.md#g711), [A-law](a-c.md#a-law), [Mu-law](l-n.md#mu-law).

### PCP
**Primary Connection Point.** The green roadside cabinet in the UK access network where the main cables from the exchange connect to the cables to local distribution points. Fibre-to-the-cabinet equipment sits next to it.

In Ethernet, PCP also means the **Priority Code Point**: the 3-bit priority field in an 802.1Q tag.

See also: [DP](d-f.md#dp), [VDSL](s-z.md#vdsl), [Dot1Q](d-f.md#dot1q).

### PCRF
**Policy and Charging Rules Function.** The node in a mobile core that decides, in real time, the policy and charging rules for each subscriber's data sessions, such as quality of service and usage limits. The gateways then enforce them.

See also: [PGW](#pgw), [QoS](#qos).

### PCS
**Physical Coding Sublayer.** The top sublayer of the Ethernet physical layer, which encodes and decodes data, for example with 8b/10b or 64b/66b coding, and scrambles it.

See also: [L1](l-n.md#l1).

### PDCP
**Packet Data Convergence Protocol.** A 3GPP radio protocol layer, in UMTS, LTE and 5G, that compresses headers, ciphers data and delivers packets in order between the device and the base station.

See also: [RRC](#rrc), [E-UTRAN](d-f.md#e-utran).

### PDH
**Plesiochronous Digital Hierarchy.** The older digital transmission hierarchy. Links such as E1 (2 Mbit/s) and E3 run at nearly, but not exactly, the same rates and are multiplexed by bit stuffing. SDH replaced it in backbones.

See also: [SDH](s-z.md#sdh), [TDM](s-z.md#tdm).

### PDU
**Protocol Data Unit.** The unit of data a protocol layer exchanges with its peer. It is a frame at layer 2, a packet at layer 3, and a segment (TCP) or datagram (UDP) at layer 4.

See also: [MTU](l-n.md#mtu).

### PEAP
**Protected EAP.** An EAP method that sets up a TLS tunnel first and then runs a simpler authentication, often a password, inside it. It is common for Wi-Fi in organisations.

See also: [EAP](d-f.md#eap), [TLS](s-z.md#tls).

### Peer review
Checking work by people with similar skills and roles, to see that it meets its criteria.

See also: [Review](#review).

### Pen testing
**Penetration testing.** An authorised simulated attack on a system to find vulnerabilities that a real attacker could exploit. Testers may get full information about the system (white box) or none (black box).

See also: [Ethical Hacking](d-f.md#ethical-hacking).

### PER
**Packed Encoding Rules.** Compact ASN.1 encoding rules that use the limits in the schema to encode values in as few bits as possible. The decoder needs the schema. Mobile radio protocols such as RRC use PER.

See also: [ASN.1](a-c.md#asn1), [BER](a-c.md#ber).

### Performance
How well a system does what it does, such as speed, resource use, reliability and availability. The term is sometimes also used for the mix of features and quality a project delivers.

See also: [Non-functional Requirement](l-n.md#non-functional-requirement).

### Perl
A general-purpose scripting language created by Larry Wall in 1987, strong at text processing. Raku began as Perl 6 and became a separate language.

See also: [Awk](a-c.md#awk), [Sed](s-z.md#sed).

### Personas
Short, fictional profiles of typical users, used to keep their goals and needs in mind during design.

See also: [User Experience](s-z.md#user-experience).

### Perspective
In an inspection, a point of view given to an inspector, such as the tester's or the maintainer's, so that different inspectors find different issues.

See also: [Inspection](g-k.md#inspection).

### PERT chart
<!-- vale PyDoc.Spelling = NO -->
**Program Evaluation and Review Technique.**
<!-- vale PyDoc.Spelling = YES -->
A project planning technique, developed by the US Navy in the 1950s, that shows tasks as a network of dependencies. It estimates each task's duration from optimistic, likely and pessimistic values.

See also: [CPM](a-c.md#cpm), [Gantt chart](g-k.md#gantt-chart).

### PGP
**Pretty Good Privacy.** Encryption software, created by Phil Zimmermann in 1991, for signing and encrypting email and files. The OpenPGP standard (RFC 4880) describes its format.

### PGW
**Packet Data Network Gateway.** The LTE core gateway that connects devices to external packet networks, such as the internet. It allocates IP addresses, enforces policy and charging, and anchors mobility.

See also: [S-GW](s-z.md#s-gw), [PCRF](#pcrf), [GGSN](g-k.md#ggsn), [APN](a-c.md#apn).

### Phase
A group of activities in a lifecycle, or a period in a schedule, often marking a major transition in a project. Sometimes used to mean a stage.

See also: [Stage](s-z.md#stage), [Lifecycle](l-n.md#lifecycle).

### Phased Estimation
Re-estimating throughout a project's lifecycle, using the techniques that best suit each phase.

See also: [Estimation](d-f.md#estimation).

### PHP
A server-side scripting language for the web, created by Rasmus Lerdorf in 1994. Its code can be embedded in HTML pages, and it powers many content management systems.

### Planning and Tracking Lead
**PTL.** The person responsible for planning a project's technical work and tracking it: work breakdown, estimation, scheduling and progress.

### Planning Poker
An agile estimation technique in which each team member chooses a card for their estimate and all reveal at once. Differences are then discussed and the round repeated until the estimates converge.

See also: [Points](#points), [Relative Estimation](#relative-estimation).

### PLL
**Phase-Locked Loop.** A control circuit that adjusts an oscillator so that its output stays in phase with a reference signal. PLLs are used for clock recovery, frequency synthesis and synchronisation.

See also: [Jitter](g-k.md#jitter).

### PNT
**Pointer.** Ordnance Survey of Northern Ireland's address database for Northern Ireland.

See also: [PAF](#paf).

### Points
**Story points.** Units for estimating the relative size or effort of user stories, rather than hours.

See also: [Planning Poker](#planning-poker), [Velocity](s-z.md#velocity).

### Polymorphism
The ability of one interface to work with different types, so that the same call does different things depending on the object it is made on.

See also: [OO](#oo).

### POP
**Point of Presence.** A location, such as a building or data centre, where a network provider has equipment and where others can connect to its network.

See also: [ISP](g-k.md#isp).

### Portability
How easily software can be moved to a different platform or operating system without major rework.

See also: [POSIX](#posix).

### POSIX
**Portable Operating System Interface.** IEEE standards that define the API, shell and utilities of Unix-like operating systems, so software can move between them.

See also: [Unix](s-z.md#unix), [Sh](s-z.md#sh).

### Postmortem
A review at the end of a project, and its report, in which the team looks at what went well and badly and draws lessons for next time.

See also: [Milestone Retrospective](l-n.md#milestone-retrospective).

### POTS
**Plain Old Telephone Service.** Basic analogue voice telephony over a copper line.

See also: [PSTN](#pstn), [FXS](d-f.md#fxs).

### PPP
**Point-to-Point Protocol.** A data link protocol for a direct link between two nodes, with authentication, link negotiation and network-layer configuration. Its variants, PPPoE and PPPoA, carry broadband sessions.

See also: [PPPoE](#pppoe), [CHAP](a-c.md#chap), [PAP](#pap), [L2TP](l-n.md#l2tp).

### PPPoE
**PPP over Ethernet.** PPP frames carried inside Ethernet frames, so broadband providers can authenticate users and manage sessions over Ethernet-based access networks.

See also: [PPP](#ppp), [BNG](a-c.md#bng).

### PPTP
**Point-to-Point Tunnelling Protocol.** An old VPN protocol that tunnels PPP over GRE with a TCP control channel. Its security is broken, so it should not be used.

See also: [L2TP](l-n.md#l2tp), [IPSec](g-k.md#ipsec).

### Preemption
Interrupting a running task, without its cooperation, to run another, intending to resume it later. A preemptive scheduler does this, typically to run a higher-priority task.

See also: [Scheduler](s-z.md#scheduler), [RTOS](#rtos).

### Preview
A meeting, with material sent out beforehand, to probe a proposed solution and suggest alternatives. Unlike a review, it looks for solutions rather than defects.

See also: [Engineering Discussion](d-f.md#engineering-discussion), [Review](#review).

### PRI
**Primary Rate Interface.** ISDN access for larger sites. On an E1 (2.048 Mbit/s) it has 30 bearer channels and one signalling channel; on a T1 (1.544 Mbit/s), 23 bearers and one signalling channel. BT sold it as ISDN30.

See also: [ISDN](g-k.md#isdn), [BRI](a-c.md#bri), [ISDN30](g-k.md#isdn30), [Q.931](#q931).

### PRINCE2
**Projects in Controlled Environments.** A process-based project management method that originated in UK government and is widely used in the UK and Europe.

See also: [CCTA](a-c.md#ccta).

### Process
A standard way of doing an activity or task, whether written down or not. A defined process is documented. The word also refers to running the process, as in "the build process".

See also: [Process Flow](#process-flow), [Engineering Process](d-f.md#engineering-process).

### Process Flow
A model of a process that defines its steps, events, inputs and outputs.

See also: [Process](#process).

### Product Owner
The Scrum role responsible for maximising the value of the product: managing the product backlog and deciding what the team works on next.

See also: [Scrum](s-z.md#scrum), [Backlog](a-c.md#backlog).

### Product Release
A release made for distribution or deployment to end users.

See also: [Release](#release).

### Programming language
A formal language for writing instructions that a computer can carry out, after compilation or interpretation.

See also: [Programming paradigm](#programming-paradigm), [Compiled Language](a-c.md#compiled-language), [Interpreted Language](g-k.md#interpreted-language).

### Programming paradigm
A style of programming, and a way of classifying languages by the features that support it. Examples are imperative, procedural, object-oriented, functional, declarative and logic programming. Most modern languages support several.

See also: [OO](#oo), [AOP](a-c.md#aop).

### Progressive Elaboration
Defining a project's requirements and plans in more detail as the project goes on and more becomes known. The term comes from the PMBOK.

See also: [Rolling Wave Planning](#rolling-wave-planning), [Project Headlights](#project-headlights).

### Project
A temporary piece of work to create a unique product, service or result.

See also: [Project Charter](#project-charter), [Project Plan](#project-plan).

### Project Build
A build made through the project's shared build process, usually in a dedicated build environment.

See also: [Local Build](l-n.md#local-build), [Build Environment](a-c.md#build-environment).

### Project Business Manager
**PBM.** The person responsible for a project's business outcome: staffing, resources, people issues and dealing with the client. They make the top-level decisions and usually defer technical ones to the technical leads.

See also: [Project Manager](#project-manager).

### Project Charter
The document that starts a project, setting out its objectives, business case, risks, resources and constraints.

See also: [Project Sponsor](#project-sponsor), [Fuzzy Front End](d-f.md#fuzzy-front-end).

### Project Chartering
Summarising a project's key success factors on one sheet, often a flip chart on the team room wall.

See also: [Project Charter](#project-charter).

### Project Estimate
An estimate for a whole project, or a large part of one, usually using several techniques.

See also: [Task Estimate](s-z.md#task-estimate), [Estimate](d-f.md#estimate).

### Project Headlights
The idea that a project can only plan with confidence a limited distance ahead, like driving within the range of a car's headlights. Beyond that, plans are rougher.

See also: [Rolling Wave Planning](#rolling-wave-planning), [Progressive Elaboration](#progressive-elaboration).

### Project History
A summary of the significant information and statistics about a whole project.

See also: [Project Log](#project-log), [Postmortem](#postmortem).

### Project Log
A record of the significant information and statistics about each phase of a project.

See also: [Project History](#project-history).

### Project Management
**PM.** Planning, tracking, controlling and reporting on a project.

See also: [PRINCE2](#prince2), [Project Management Body of Knowledge](#project-management-body-of-knowledge).

### Project Management Body of Knowledge
**PMBOK.** The Project Management Institute's guide to the generally recognised knowledge and practices of project management.

See also: [Project Management Institute](#project-management-institute).

### Project Management Institute
**PMI.** A professional association for project managers, which publishes the PMBOK and runs certifications.

See also: [Project Management Body of Knowledge](#project-management-body-of-knowledge).

### Project Manager
**PM.** The person who manages a project. The role often combines those of the project business manager and the planning and tracking lead.

See also: [Project Business Manager](#project-business-manager), [Planning and Tracking Lead](#planning-and-tracking-lead).

### Project Plan
**PP.** The controlling document that defines how a project will be carried out.

See also: [Project Charter](#project-charter), [Work Plan](s-z.md#work-plan).

### Project Reviewer
Someone outside a project who reviews or audits it, to check that processes are being followed and risks managed.

See also: [Audit](a-c.md#audit).

### Project Sponsor
The person or organisation that sponsors a project: starts it, provides its resources, oversees its manager and makes sure it meets stakeholders' needs.

See also: [Authority](a-c.md#authority), [Project Charter](#project-charter).

### Pseudocode
An informal, readable description of an algorithm, written in structured natural language rather than a real programming language.

### PSTN
**Public Switched Telephone Network.** The world's interconnected circuit-switched telephone networks, fixed and mobile. Its core is now digital, and many countries are moving its services to IP.

See also: [POTS](#pots), [Circuit Switched](a-c.md#circuit-switched), [SS7](s-z.md#ss7).

### PTP
**Precision Time Protocol.** The IEEE 1588 protocol for synchronising clocks across a network to sub-microsecond accuracy, with hardware timestamping. Mobile networks, finance and industrial control use it.

See also: [NTP](l-n.md#ntp), [MRTIE](l-n.md#mrtie).

### PTT
**Push-to-Talk.** Talking over a half-duplex channel by holding a button to transmit and releasing it to listen, as on a two-way radio.

See also: [Half Duplex](g-k.md#half-duplex).

### PVC
**Permanent Virtual Circuit.** A virtual circuit set up permanently between two endpoints, so no call set-up is needed. Frame Relay and ATM services were usually built from PVCs.

See also: [SVC](s-z.md#svc), [Frame Relay](d-f.md#frame-relay), [ATM](a-c.md#atm).

### PW
**Pseudowire.** The emulation of a point-to-point circuit, such as Ethernet, TDM or ATM, over a packet network, typically MPLS.

See also: [VPWS](s-z.md#vpws), [L2VPN](l-n.md#l2vpn).

### PWFQ
**Priority Weighted Fair Queuing.** A queuing scheme that serves strict-priority queues first and shares the remaining capacity between the other queues by weight.

See also: [NGWFQ](l-n.md#ngwfq), [QoS](#qos).

### Python
A high-level, general-purpose language created by Guido van Rossum and first released in 1991. It is known for readable code with significant indentation and a large standard library. Python 2 reached end of life in 2020, and Python 3 is the current version.

See also: [Interpreted Language](g-k.md#interpreted-language).

## Q

### Q.931 {#q931}
The ITU-T ISDN signalling protocol on the D channel, which sets up, maintains and clears calls between the user and the network. H.323 and QSIG reuse its messages.

See also: [ISDN](g-k.md#isdn), [PRI](#pri), [QSIG](#qsig).

### QA Lead
**QAL.** The person responsible for the quality of a project's process and product.

See also: [Quality Assurance](#quality-assurance).

### QAM
**Quadrature Amplitude Modulation.** Modulation that sends data by varying the amplitude of two carriers 90° apart, so that each symbol carries several bits. Higher orders, such as 256-QAM, carry more bits but need a cleaner signal. DSL, cable, Wi-Fi and mobile networks use it.

See also: [FSK](d-f.md#fsk), [OFDMA](#ofdma).

### QoS
**Quality of Service.** The mechanisms that give different traffic different treatment in a network, through classification, marking, queuing and policing. They protect delay-sensitive traffic, such as voice, from loss, delay and jitter. The term also means the measured performance of a service.

See also: [DSCP](d-f.md#dscp), [CoS](a-c.md#cos), [RSVP](#rsvp), [PWFQ](#pwfq).

### QSIG
An ISDN-based signalling protocol between PBXs in a private network, standardised by Ecma and ISO. It supports basic calls and supplementary services across different vendors' equipment.

See also: [DPNSS](d-f.md#dpnss), [Q.931](#q931).

### Quality
How well a system and its artefacts meet their requirements and standards, and the activities that make sure they do.

See also: [Quality Assurance](#quality-assurance), [Quality Control](#quality-control).

### Quality Assurance
**QA.** Activities that prevent defects, by making sure the right processes are in place and followed.

See also: [Quality Control](#quality-control), [Quality Plan](#quality-plan).

### Quality Assurance Plan
See [Quality Plan](#quality-plan).

### Quality Control
**QC.** Activities that find defects, mainly reviews and testing.

See also: [Quality Assurance](#quality-assurance), [Testing](s-z.md#testing).

### Quality Plan
**QP.** A plan for the quality methods and practices a project will use, and which artefacts they cover. It often leaves the testing details to the test plan.

See also: [Test Plan](s-z.md#test-plan).

### Quick Design Session
A short meeting, often at a whiteboard, where two or more developers settle a design choice that has wide consequences.

See also: [Simple Design](s-z.md#simple-design).

## R

### R Language
A language and free environment for statistical computing and graphics, widely used by statisticians and data scientists.

See also: [Python](#python).

### RACI
**Responsible, Accountable, Consulted, Informed.** A responsibility matrix that sets out, for each task or deliverable, who does the work, who is accountable for it, who is consulted and who is kept informed.

### RAD
**Rapid Application Development.** An approach that develops software quickly through prototypes, workshops, early user testing and component reuse, with less formal documentation.

See also: [Rapid Application Development](#rapid-application-development), [DSDM](d-f.md#dsdm), [Joint Application Development](g-k.md#joint-application-development).

### RAD Environment
A development tool that combines a language and an IDE with a toolbox of ready-made user interface components, for building applications quickly.

See also: [IDE](g-k.md#ide), [RAD](#rad).

### Radius
**RADIUS: Remote Authentication Dial-In User Service.** The protocol (RFC 2865) that network access servers use to authenticate users, authorise their access and record their usage against a central server. It is widely used for broadband, Wi-Fi and VPN access.

See also: [NAS](l-n.md#nas), [EAP](d-f.md#eap), [FNA](d-f.md#fna).

### RAN
**Radio Access Network.** The part of a mobile network between devices and the core: the base stations and their controllers. GERAN, UTRAN and E-UTRAN are the 2G, 3G and 4G versions.

See also: [GERAN](g-k.md#geran), [UTRAN](s-z.md#utran), [E-UTRAN](d-f.md#e-utran), [Backhaul](a-c.md#backhaul).

### RANAP
**Radio Access Network Application Part.** The UMTS signalling protocol on the Iu interface between the radio access network (the RNC) and the core (MSC or SGSN).

See also: [RNC](#rnc), [UTRAN](s-z.md#utran).

### RANCID
**Really Awesome New Cisco confIg Differ.** An open-source tool that logs in to network devices, collects their configurations, stores them in version control and reports changes.

### Rapid Application Development
See [RAD](#rad).

### RARP
**Reverse Address Resolution Protocol.** An obsolete protocol (RFC 903) with which a device that knows only its MAC address asks a server for its IP address. BOOTP and DHCP replaced it.

See also: [BOOTP](a-c.md#bootp), [DHCP](d-f.md#dhcp).

### RAS
**Registration, Admission and Status.** The part of H.323 (in H.225) with which endpoints register with a gatekeeper and ask permission to make calls. RAS also stands for remote access server.

See also: [H.323](g-k.md#h323).

### RDBMS
**Relational Database Management System.** A database system based on Edgar Codd's relational model, which stores data in tables with rows and columns and is queried with SQL.

See also: [SQL](s-z.md#sql), [NoSQL](l-n.md#nosql).

### RDP
**Remote Desktop Protocol.** Microsoft's protocol for using another computer's desktop over a network, on TCP and UDP port 3389.

### Reading Inspection
An inspection that follows every step of the full process except the inspection meeting.

See also: [Inspection](g-k.md#inspection).

### Refactoring
Improving the internal structure of code without changing what it does, in small steps backed by tests.

See also: [Technical Debt](s-z.md#technical-debt), [TDD](s-z.md#tdd).

### Regression testing
Re-running tests after a change to check that what worked before still works.

See also: [Automated Testing](a-c.md#automated-testing).

### Regular expression
A pattern that describes a set of strings, used to search, match, validate and replace text. It is also called a regex.

See also: [Sed](s-z.md#sed), [Awk](a-c.md#awk).

### Relative Estimation
Estimating work by comparing items with each other, or grouping items of similar difficulty, rather than estimating each in absolute units.

See also: [Points](#points), [T-Shirt Sizing](s-z.md#t-shirt-sizing).

### Release
Delivering a deployable version of a system to a customer, such as a test group or end users. The word also means the version delivered.

See also: [Release Management](#release-management), [Product Release](#product-release).

### Release Management
Identifying, packaging and delivering the parts of a product to its customers, internal or external.

See also: [Release](#release), [Semantic Versioning](s-z.md#semantic-versioning).

### Release Test
A test that checks software is ready for release.

### Requirement
A statement of something a system must do, or a quality it must have.

See also: [Functional Requirement](d-f.md#functional-requirement), [Non-functional Requirement](l-n.md#non-functional-requirement).

### Requirements
The work of finding out, recording and managing what a software system should do.

See also: [Requirement](#requirement), [Software Requirements Specification](s-z.md#software-requirements-specification).

### Requirements Lead
The person responsible for defining, maintaining and tracing a product's requirements, and for the user documentation that follows from them.

### REST
**Representational State Transfer.** An architecture style for web services in which resources are identified by URLs and handled through a uniform set of stateless operations, usually the HTTP methods. `GET` reads, `POST` creates, `PUT` replaces and `DELETE` removes.

See also: [HTTP](g-k.md#http), [SOAP](s-z.md#soap), [API](a-c.md#api).

### Review
A defined process in which people other than an artefact's author examine it to find issues. Reviews range from informal desk checks to formal inspections.

See also: [Inspection](g-k.md#inspection), [Desk Check](d-f.md#desk-check), [Walkthrough](s-z.md#walkthrough).

### Reviewer
A person who takes part in a review.

See also: [Review](#review).

### Revision
One recorded version of an artefact, usually as numbered by a version control system.

See also: [Version Control](s-z.md#version-control).

### Revision Control
See [Version Control](s-z.md#version-control).

### Rework
Unplanned work needed to bring an artefact into line with the project's needs, such as fixing defects.

See also: [Update](s-z.md#update).

### RFC
**Request for Comments.** The IETF's numbered document series, which includes the internet's standards and many informational and experimental documents.

See also: [IETF](g-k.md#ietf).

### RIP
**Routing Information Protocol.** One of the oldest distance-vector routing protocols. It uses hop count as its metric, with a limit of 15 hops, so it suits only small networks.

See also: [OSPF](#ospf), [IGRP](g-k.md#igrp), [IGP](g-k.md#igp).

### Risk
A possible future event that would harm a project's features, budget, schedule or quality if it happened.

See also: [Risk Management](#risk-management), [Risk List](#risk-list).

### Risk Analysis
Assessing each risk for its likelihood and impact.

See also: [Risk Management](#risk-management).

### Risk Identification
Finding and recording a project's current risks.

See also: [Risk Management](#risk-management).

### Risk List
A list of a project's current and past risks, with their analysis and mitigation plans.

See also: [Risk Management](#risk-management), [Extrinsic Risk Management](d-f.md#extrinsic-risk-management).

### Risk Management
Identifying, analysing and controlling a project's risks, either explicitly or as part of how the project is run.

See also: [Risk](#risk), [Extrinsic Risk Management](d-f.md#extrinsic-risk-management), [Intrinsic Risk Management](g-k.md#intrinsic-risk-management), [Risk Mitigation](#risk-mitigation).

### Risk Mitigation
Planning and taking action to reduce a risk's likelihood or impact.

See also: [Risk Management](#risk-management).

### Risk Reward Matrix
A two-by-two grid for comparing options, with risk on one axis and reward on the other. High-reward, low-risk options are the best candidates; high-risk, low-reward ones are to be avoided. The size of each marker can show the resources each option needs.

### RNC
**Radio Network Controller.** The UMTS node that controls a group of Node Bs. It manages radio resources and handovers, and ciphers user data. It connects to the circuit-switched core through the Iu-CS interface and to the packet core through Iu-PS.

See also: [Node B](l-n.md#node-b), [UTRAN](s-z.md#utran), [RANAP](#ranap), [BSC](a-c.md#bsc).

### RNSAP
**Radio Network Subsystem Application Part.** The UMTS signalling protocol between RNCs, on the Iur interface, used for soft handover and moving a connection from one RNC to another.

See also: [RNC](#rnc), [UTRAN](s-z.md#utran).

### Role-feature-reason
The usual template for writing user stories: "As a *role*, I want *feature*, so that *reason*."

See also: [User Stories](s-z.md#user-stories).

### Rolling Wave Planning
Planning the near future in detail and later work only roughly, then adding detail as each period comes closer.

See also: [Project Headlights](#project-headlights), [Progressive Elaboration](#progressive-elaboration).

### Root of Trust
**RoT.** The hardware, firmware and keys that a device trusts without checking, because everything else is checked against them. It anchors secure boot, device identity and key storage, and is usually built into the chip or a secure element.

See also: [RoT](#rot), [Secure Element](s-z.md#secure-element), [TrustZone](s-z.md#trustzone).

### RoT
See [Root of Trust](#root-of-trust).

### Round Robin
A scheduling method that gives each task or queue a turn in a fixed circular order, with equal time slices and no priorities. It is simple and no task is starved.

See also: [Scheduler](s-z.md#scheduler), [Preemption](#preemption).

### Router
A device that forwards packets between networks, choosing the next hop for each from its routing table, which it builds from configuration and routing protocols.

See also: [Switch](s-z.md#switch), [Control Plane](a-c.md#control-plane), [BGP](a-c.md#bgp), [OSPF](#ospf).

### RPC
**Remote Procedure Call.** Calling a procedure that runs in another process or on another machine as if it were a local call, with the messaging hidden by the framework.

See also: [JSON-RPC](g-k.md#json-rpc), [XML-RPC](s-z.md#xml-rpc), [SOAP](s-z.md#soap).

### RRC
**Radio Resource Control.** The 3GPP control protocol between a device and the radio network in UMTS, LTE and 5G. It sets up and releases connections and radio bearers, broadcasts system information and manages mobility. A state machine, with idle and connected states, governs the device.

See also: [PDCP](#pdcp), [E-UTRAN](d-f.md#e-utran).

### RSTP
**Rapid Spanning Tree Protocol.** IEEE 802.1w, a faster version of the spanning tree protocol that recovers from a topology change in seconds rather than tens of seconds. It is now part of 802.1D.

See also: [STP](s-z.md#stp).

### RSVP
**Resource Reservation Protocol.** A protocol (RFC 2205) with which receivers reserve network resources for a flow along its path. Its extension, RSVP-TE, sets up traffic-engineered MPLS paths.

See also: [QoS](#qos), [LSP](l-n.md#lsp).

### RTCP
**RTP Control Protocol.** The companion to RTP, defined in RFC 3550. It reports statistics on an RTP session, such as packet loss, jitter and round-trip time, and helps synchronise streams.

See also: [RTP](#rtp).

### RTOS
**Real-Time Operating System.** An operating system that guarantees tasks respond within defined time limits, usually by priority-based preemptive scheduling. FreeRTOS, Zephyr and VxWorks are examples.

See also: [Scheduler](s-z.md#scheduler), [Preemption](#preemption), [MCU](l-n.md#mcu).

### RTP
**Real-time Transport Protocol.** The protocol (RFC 3550) that carries audio and video over IP, usually on UDP, with sequence numbers and timestamps so receivers can play media out smoothly. SIP or another protocol sets up the session.

See also: [RTCP](#rtcp), [SIP](s-z.md#sip), [VoIP](s-z.md#voip).

### RTSP
**Real Time Streaming Protocol.** A protocol for controlling streaming media servers with commands such as play, pause and record. The media itself usually travels over RTP.

See also: [RTP](#rtp).

### Ruby
A dynamic, object-oriented scripting language created by Yukihiro Matsumoto in the mid-1990s, designed to make programmers productive and happy.

See also: [Ruby on Rails](#ruby-on-rails).

### Ruby on Rails
A web application framework written in Ruby, built on the model-view-controller pattern and known for "convention over configuration".

See also: [Ruby](#ruby).

### Rule of Simplicity
Kent Beck's rules, in priority order, for judging whether code is simple enough: it passes the tests, reveals its intent, has no duplication and has the fewest elements.

See also: [Simple Design](s-z.md#simple-design), [KISS Principle](g-k.md#kiss-principle).

### RUP
**Rational Unified Process.** An iterative software development process framework from Rational Software (later IBM), with four phases: inception, elaboration, construction and transition.

See also: [UML](s-z.md#uml), [Iterative Development](g-k.md#iterative-development).
