---
title: P
---

# P

## PaaS
**Platform as a Service.** Cloud computing that provides a managed platform for building and running applications, so the customer does not manage servers or operating systems.

See also: [IaaS](i.md#iaas), [SaaS](s.md#saas).

## Packet sniffing
Capturing and decoding the packets crossing a network, usually with a packet analyser such as Wireshark, to troubleshoot problems or, in an attack, to steal data.

See also: [Wireshark](w.md#wireshark), [DPI](d.md#dpi).

## Packet Switched
A network that splits data into packets, each with a header that routers use to forward it independently, sharing links with other traffic. The internet works this way.

See also: [Circuit Switched](c.md#circuit-switched).

## PAF
**Postcode Address File.** Royal Mail's database of every UK delivery address and its postcode.

## Pair Programming
Two developers working together at one computer: one writes the code while the other reviews it and thinks ahead, and they swap often.

See also: [Mob Programming](m.md#mob-programming), [XP](x.md#xp).

## PAP
**Password Authentication Protocol.** A simple PPP authentication method that sends the username and password in clear text. It should be used only when nothing stronger, such as CHAP or EAP, is available.

See also: [CHAP](c.md#chap), [PPP](#ppp).

## Parametric Estimation
Estimating with a model that calculates effort, cost or schedule from input factors, using formulas based on historical data. COCOMO is an example.

See also: [Estimation](e.md#estimation), [Statistical Estimation](s.md#statistical-estimation).

## Pascal
A procedural language designed by Niklaus Wirth around 1970 to teach structured programming. Object Pascal and Delphi descend from it.

See also: [Delphi](d.md#delphi), [Ada](a.md#ada).

## Pattern
A reusable template or model for creating an artefact or solving a recurring problem.

See also: [Design Pattern](d.md#design-pattern), [Antipattern](a.md#antipattern).

## PCM
**Pulse-Code Modulation.** The standard way of representing an analogue signal digitally: sample it at regular intervals and quantise each sample to a binary value. Telephone speech uses 8,000 samples a second at 8 bits (G.711), and CDs use 44,100 at 16 bits.

See also: [G.711](g.md#g711), [A-law](a.md#a-law), [Mu-law](m.md#mu-law).

## PCP
**Primary Connection Point.** The green roadside cabinet in the UK access network where the main cables from the exchange connect to the cables to local distribution points. Fibre-to-the-cabinet equipment sits next to it.

In Ethernet, PCP also means the **Priority Code Point**: the 3-bit priority field in an 802.1Q tag.

See also: [DP](d.md#dp), [VDSL](v.md#vdsl), [Dot1Q](d.md#dot1q).

## PCRF
**Policy and Charging Rules Function.** The node in a mobile core that decides, in real time, the policy and charging rules for each subscriber's data sessions, such as quality of service and usage limits. The gateways then enforce them.

See also: [PGW](#pgw), [QoS](q.md#qos).

## PCS
**Physical Coding Sublayer.** The top sublayer of the Ethernet physical layer, which encodes and decodes data, for example with 8b/10b or 64b/66b coding, and scrambles it.

See also: [L1](l.md#l1).

## PDCP
**Packet Data Convergence Protocol.** A 3GPP radio protocol layer, in UMTS, LTE and 5G, that compresses headers, ciphers data and delivers packets in order between the device and the base station.

See also: [RRC](r.md#rrc), [E-UTRAN](e.md#e-utran).

## PDH
**Plesiochronous Digital Hierarchy.** The older digital transmission hierarchy. Links such as E1 (2 Mbit/s) and E3 run at nearly, but not exactly, the same rates and are multiplexed by bit stuffing. SDH replaced it in backbones.

See also: [SDH](s.md#sdh), [TDM](t.md#tdm).

## PDU
**Protocol Data Unit.** The unit of data a protocol layer exchanges with its peer. It is a frame at layer 2, a packet at layer 3, and a segment (TCP) or datagram (UDP) at layer 4.

See also: [MTU](m.md#mtu).

## PEAP
**Protected EAP.** An EAP method that sets up a TLS tunnel first and then runs a simpler authentication, often a password, inside it. It is common for Wi-Fi in organisations.

See also: [EAP](e.md#eap), [TLS](t.md#tls).

## Peer review
Checking work by people with similar skills and roles, to see that it meets its criteria.

See also: [Review](r.md#review).

## Pen testing
**Penetration testing.** An authorised simulated attack on a system to find vulnerabilities that a real attacker could exploit. Testers may get full information about the system (white box) or none (black box).

See also: [Ethical Hacking](e.md#ethical-hacking).

## PER
**Packed Encoding Rules.** Compact ASN.1 encoding rules that use the limits in the schema to encode values in as few bits as possible. The decoder needs the schema. Mobile radio protocols such as RRC use PER.

See also: [ASN.1](a.md#asn1), [BER](b.md#ber).

## Performance
How well a system does what it does, such as speed, resource use, reliability and availability. The term is sometimes also used for the mix of features and quality a project delivers.

See also: [Non-functional Requirement](n.md#non-functional-requirement).

## Perl
A general-purpose scripting language created by Larry Wall in 1987, strong at text processing. Raku began as Perl 6 and became a separate language.

See also: [Awk](a.md#awk), [Sed](s.md#sed).

## Personas
Short, fictional profiles of typical users, used to keep their goals and needs in mind during design.

See also: [User Experience](u.md#user-experience).

## Perspective
In an inspection, a point of view given to an inspector, such as the tester's or the maintainer's, so that different inspectors find different issues.

See also: [Inspection](i.md#inspection).

## PERT chart
<!-- vale PyDoc.Spelling = NO -->
**Program Evaluation and Review Technique.**
<!-- vale PyDoc.Spelling = YES -->
A project planning technique, developed by the US Navy in the 1950s, that shows tasks as a network of dependencies. It estimates each task's duration from optimistic, likely and pessimistic values.

See also: [CPM](c.md#cpm), [Gantt chart](g.md#gantt-chart).

## PGP
**Pretty Good Privacy.** Encryption software, created by Phil Zimmermann in 1991, for signing and encrypting email and files. The OpenPGP standard (RFC 4880) describes its format.

## PGW
**Packet Data Network Gateway.** The LTE core gateway that connects devices to external packet networks, such as the internet. It allocates IP addresses, enforces policy and charging, and anchors mobility.

See also: [S-GW](s.md#s-gw), [PCRF](#pcrf), [GGSN](g.md#ggsn), [APN](a.md#apn).

## Phase
A group of activities in a lifecycle, or a period in a schedule, often marking a major transition in a project. Sometimes used to mean a stage.

See also: [Stage](s.md#stage), [Lifecycle](l.md#lifecycle).

## Phased Estimation
Re-estimating throughout a project's lifecycle, using the techniques that best suit each phase.

See also: [Estimation](e.md#estimation).

## PHP
A server-side scripting language for the web, created by Rasmus Lerdorf in 1994. Its code can be embedded in HTML pages, and it powers many content management systems.

## Planning and Tracking Lead
**PTL.** The person responsible for planning a project's technical work and tracking it: work breakdown, estimation, scheduling and progress.

## Planning Poker
An agile estimation technique in which each team member chooses a card for their estimate and all reveal at once. Differences are then discussed and the round repeated until the estimates converge.

See also: [Points](#points), [Relative Estimation](r.md#relative-estimation).

## PLL
**Phase-Locked Loop.** A control circuit that adjusts an oscillator so that its output stays in phase with a reference signal. PLLs are used for clock recovery, frequency synthesis and synchronisation.

See also: [Jitter](j.md#jitter).

## PNT
**Pointer.** Ordnance Survey of Northern Ireland's address database for Northern Ireland.

See also: [PAF](#paf).

## Points
**Story points.** Units for estimating the relative size or effort of user stories, rather than hours.

See also: [Planning Poker](#planning-poker), [Velocity](v.md#velocity).

## Polymorphism
The ability of one interface to work with different types, so that the same call does different things depending on the object it is made on.

See also: [OO](o.md#oo).

## POP
**Point of Presence.** A location, such as a building or data centre, where a network provider has equipment and where others can connect to its network.

See also: [ISP](i.md#isp).

## Portability
How easily software can be moved to a different platform or operating system without major rework.

See also: [POSIX](#posix).

## POSIX
**Portable Operating System Interface.** IEEE standards that define the API, shell and utilities of Unix-like operating systems, so software can move between them.

See also: [Unix](u.md#unix), [Sh](s.md#sh).

## Postmortem
A review at the end of a project, and its report, in which the team looks at what went well and badly and draws lessons for next time.

See also: [Milestone Retrospective](m.md#milestone-retrospective).

## POTS
**Plain Old Telephone Service.** Basic analogue voice telephony over a copper line.

See also: [PSTN](#pstn), [FXS](f.md#fxs).

## PPP
**Point-to-Point Protocol.** A data link protocol for a direct link between two nodes, with authentication, link negotiation and network-layer configuration. Its variants, PPPoE and PPPoA, carry broadband sessions.

See also: [PPPoE](#pppoe), [CHAP](c.md#chap), [PAP](#pap), [L2TP](l.md#l2tp).

## PPPoE
**PPP over Ethernet.** PPP frames carried inside Ethernet frames, so broadband providers can authenticate users and manage sessions over Ethernet-based access networks.

See also: [PPP](#ppp), [BNG](b.md#bng).

## PPTP
**Point-to-Point Tunnelling Protocol.** An old VPN protocol that tunnels PPP over GRE with a TCP control channel. Its security is broken, so it should not be used.

See also: [L2TP](l.md#l2tp), [IPSec](i.md#ipsec).

## Preemption
Interrupting a running task, without its cooperation, to run another, intending to resume it later. A preemptive scheduler does this, typically to run a higher-priority task.

See also: [Scheduler](s.md#scheduler), [RTOS](r.md#rtos).

## Preview
A meeting, with material sent out beforehand, to probe a proposed solution and suggest alternatives. Unlike a review, it looks for solutions rather than defects.

See also: [Engineering Discussion](e.md#engineering-discussion), [Review](r.md#review).

## PRI
**Primary Rate Interface.** ISDN access for larger sites. On an E1 (2.048 Mbit/s) it has 30 bearer channels and one signalling channel; on a T1 (1.544 Mbit/s), 23 bearers and one signalling channel. BT sold it as ISDN30.

See also: [ISDN](i.md#isdn), [BRI](b.md#bri), [ISDN30](i.md#isdn30), [Q.931](q.md#q931).

## PRINCE2
**Projects in Controlled Environments.** A process-based project management method that originated in UK government and is widely used in the UK and Europe.

See also: [CCTA](c.md#ccta).

## Process
A standard way of doing an activity or task, whether written down or not. A defined process is documented. The word also refers to running the process, as in "the build process".

See also: [Process Flow](#process-flow), [Engineering Process](e.md#engineering-process).

## Process Flow
A model of a process that defines its steps, events, inputs and outputs.

See also: [Process](#process).

## Product Owner
The Scrum role responsible for maximising the value of the product: managing the product backlog and deciding what the team works on next.

See also: [Scrum](s.md#scrum), [Backlog](b.md#backlog).

## Product Release
A release made for distribution or deployment to end users.

See also: [Release](r.md#release).

## Programming language
A formal language for writing instructions that a computer can carry out, after compilation or interpretation.

See also: [Programming paradigm](#programming-paradigm), [Compiled Language](c.md#compiled-language), [Interpreted Language](i.md#interpreted-language).

## Programming paradigm
A style of programming, and a way of classifying languages by the features that support it. Examples are imperative, procedural, object-oriented, functional, declarative and logic programming. Most modern languages support several.

See also: [OO](o.md#oo), [AOP](a.md#aop).

## Progressive Elaboration
Defining a project's requirements and plans in more detail as the project goes on and more becomes known. The term comes from the PMBOK.

See also: [Rolling Wave Planning](r.md#rolling-wave-planning), [Project Headlights](#project-headlights).

## Project
A temporary piece of work to create a unique product, service or result.

See also: [Project Charter](#project-charter), [Project Plan](#project-plan).

## Project Build
A build made through the project's shared build process, usually in a dedicated build environment.

See also: [Local Build](l.md#local-build), [Build Environment](b.md#build-environment).

## Project Business Manager
**PBM.** The person responsible for a project's business outcome: staffing, resources, people issues and dealing with the client. They make the top-level decisions and usually defer technical ones to the technical leads.

See also: [Project Manager](#project-manager).

## Project Charter
The document that starts a project, setting out its objectives, business case, risks, resources and constraints.

See also: [Project Sponsor](#project-sponsor), [Fuzzy Front End](f.md#fuzzy-front-end).

## Project Chartering
Summarising a project's key success factors on one sheet, often a flip chart on the team room wall.

See also: [Project Charter](#project-charter).

## Project Estimate
An estimate for a whole project, or a large part of one, usually using several techniques.

See also: [Task Estimate](t.md#task-estimate), [Estimate](e.md#estimate).

## Project Headlights
The idea that a project can only plan with confidence a limited distance ahead, like driving within the range of a car's headlights. Beyond that, plans are rougher.

See also: [Rolling Wave Planning](r.md#rolling-wave-planning), [Progressive Elaboration](#progressive-elaboration).

## Project History
A summary of the significant information and statistics about a whole project.

See also: [Project Log](#project-log), [Postmortem](#postmortem).

## Project Log
A record of the significant information and statistics about each phase of a project.

See also: [Project History](#project-history).

## Project Management
**PM.** Planning, tracking, controlling and reporting on a project.

See also: [PRINCE2](#prince2), [Project Management Body of Knowledge](#project-management-body-of-knowledge).

## Project Management Body of Knowledge
**PMBOK.** The Project Management Institute's guide to the generally recognised knowledge and practices of project management.

See also: [Project Management Institute](#project-management-institute).

## Project Management Institute
**PMI.** A professional association for project managers, which publishes the PMBOK and runs certifications.

See also: [Project Management Body of Knowledge](#project-management-body-of-knowledge).

## Project Manager
**PM.** The person who manages a project. The role often combines those of the project business manager and the planning and tracking lead.

See also: [Project Business Manager](#project-business-manager), [Planning and Tracking Lead](#planning-and-tracking-lead).

## Project Plan
**PP.** The controlling document that defines how a project will be carried out.

See also: [Project Charter](#project-charter), [Work Plan](w.md#work-plan).

## Project Reviewer
Someone outside a project who reviews or audits it, to check that processes are being followed and risks managed.

See also: [Audit](a.md#audit).

## Project Sponsor
The person or organisation that sponsors a project: starts it, provides its resources, oversees its manager and makes sure it meets stakeholders' needs.

See also: [Authority](a.md#authority), [Project Charter](#project-charter).

## Pseudocode
An informal, readable description of an algorithm, written in structured natural language rather than a real programming language.

## PSTN
**Public Switched Telephone Network.** The world's interconnected circuit-switched telephone networks, fixed and mobile. Its core is now digital, and many countries are moving its services to IP.

See also: [POTS](#pots), [Circuit Switched](c.md#circuit-switched), [SS7](s.md#ss7).

## PTP
**Precision Time Protocol.** The IEEE 1588 protocol for synchronising clocks across a network to sub-microsecond accuracy, with hardware timestamping. Mobile networks, finance and industrial control use it.

See also: [NTP](n.md#ntp), [MRTIE](m.md#mrtie).

## PTT
**Push-to-Talk.** Talking over a half-duplex channel by holding a button to transmit and releasing it to listen, as on a two-way radio.

See also: [Half Duplex](h.md#half-duplex).

## PVC
**Permanent Virtual Circuit.** A virtual circuit set up permanently between two endpoints, so no call set-up is needed. Frame Relay and ATM services were usually built from PVCs.

See also: [SVC](s.md#svc), [Frame Relay](f.md#frame-relay), [ATM](a.md#atm).

## PW
**Pseudowire.** The emulation of a point-to-point circuit, such as Ethernet, TDM or ATM, over a packet network, typically MPLS.

See also: [VPWS](v.md#vpws), [L2VPN](l.md#l2vpn).

## PWFQ
**Priority Weighted Fair Queuing.** A queuing scheme that serves strict-priority queues first and shares the remaining capacity between the other queues by weight.

See also: [NGWFQ](n.md#ngwfq), [QoS](q.md#qos).

## Python
A high-level, general-purpose language created by Guido van Rossum and first released in 1991. It is known for readable code with significant indentation and a large standard library. Python 2 reached end of life in 2020, and Python 3 is the current version.

See also: [Interpreted Language](i.md#interpreted-language).
