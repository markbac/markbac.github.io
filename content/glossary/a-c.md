---
title: Glossary, A to C
---

# A to C

## A

### A-law
A companding algorithm that squeezes the dynamic range of speech before it is coded as 8-bit PCM. It is one of the two variants of ITU-T G.711, used in Europe and most of the world outside North America and Japan.

See also: [Mu-law](l-n.md#mu-law), [G.711](g-k.md#g711), [PCM](o-r.md#pcm).

### AA
**Authoritative Answer.** A flag in a DNS response that says the server answering owns the zone for the name asked about, rather than passing on a cached answer.

See also: [DNS](d-f.md#dns), [Authoritative Answer](#authoritative-answer).

### AAC
**Advanced Audio Coding.** A lossy audio coding format, standardised in MPEG-2 and MPEG-4 as the successor to MP3. At the same bit rate it usually sounds better than MP3. HE-AAC (AAC+) is a variant tuned for low bit rates, used in digital radio such as DAB+.

See also: [MP3](l-n.md#mp3), [MPEG](l-n.md#mpeg), [Audio Codecs](#audio-codecs).

### AAL1
**ATM Adaptation Layer 1.** The ATM adaptation layer for constant bit rate, connection-oriented traffic with tight timing, such as uncompressed voice and circuit emulation. It does not retransmit lost cells; it reports them and leaves recovery to the application.

See also: [ATM](#atm), [AAL2](#aal2), [AAL5](#aal5).

### AAL2
**ATM Adaptation Layer 2.** The ATM adaptation layer for low-delay, variable bit rate traffic, mainly compressed voice. It packs short packets from several users into one ATM connection, and was used on the Iu interfaces of UMTS. It is defined in ITU-T I.363.2.

See also: [ATM](#atm), [ALCAP](#alcap), [UMTS](s-z.md#umts).

### AAL5
**ATM Adaptation Layer 5.** The ATM adaptation layer for variable-length data packets of up to 65,535 octets, and the one most used for carrying IP over ATM. It puts its control information in an 8-octet trailer, including a 32-bit CRC, rather than a header.

See also: [ATM](#atm), [CRC](#crc).

### Acceptance Test
A formal test, agreed with the customer, whose result decides whether a release is accepted.

See also: [Acceptance Testing](#acceptance-testing), [ATDD](#atdd).

### Acceptance Testing
Testing that checks a system against the behaviour its customer or users expect, usually written as concrete examples or scenarios. The aim is often to automate those examples so they run with every build.

See also: [Acceptance Test](#acceptance-test), [ATDD](#atdd), [BDD](#bdd).

### Activity
A piece of work in a project that uses time and resources. Activities and tasks are near synonyms. PMBOK treats tasks as what an activity breaks down into.

See also: [Task](s-z.md#task), [Work Breakdown Structure](s-z.md#work-breakdown-structure).

### Activity Model
A model, such as a UML activity diagram, that shows the steps of a process or workflow and the flow of control between them.

See also: [UML](s-z.md#uml), [Model](l-n.md#model).

### AD
**Active Directory.** Microsoft's directory service for Windows domain networks. Domain controllers running Active Directory Domain Services authenticate users and computers, and apply security policy across the domain.

See also: [LDAP](l-n.md#ldap), [Kerberos](g-k.md#kerberos).

### Ad Hoc Testing
See [Informal Testing](g-k.md#informal-testing).

### Ada
A strongly and statically typed programming language, descended from Pascal, with built-in support for concurrency, contracts and protected objects. It is used where safety matters, such as avionics and rail. The language is standardised as ISO/IEC 8652.

See also: [Pascal](o-r.md#pascal).

### ADR
**Architecture Decision Record.** A short document that records one significant architecture decision: its context, the options considered, the choice made and its consequences. ADRs are kept with the code and are not edited once accepted; a later ADR supersedes an earlier one.

### ADSL
**Asymmetric Digital Subscriber Line.** A form of DSL that carries broadband over an ordinary copper telephone line, with more bandwidth downstream to the customer than upstream.

See also: [DSL](d-f.md#dsl), [SDSL](s-z.md#sdsl), [VDSL](s-z.md#vdsl), [DSLAM](d-f.md#dslam).

### AES
**Advanced Encryption Standard.** A symmetric block cipher, chosen by NIST in 2001 from the Rijndael family. It has a 128-bit block and keys of 128, 192 or 256 bits, and replaced DES as the default cipher for bulk encryption.

See also: [DES](d-f.md#des), [Triple DES](s-z.md#triple-des), [NIST](l-n.md#nist).

### Agent
In a project charter, another name for the [Project Sponsor](o-r.md#project-sponsor).

### Agile
An approach to projects that delivers requirements in small increments, with frequent feedback, rather than in one pass at the end.

See also: [Agile development](#agile-development), [Agile Manifesto](#agile-manifesto), [Scrum](s-z.md#scrum).

### Agile development
An umbrella term for iterative, incremental ways of developing software, such as Scrum, XP, Lean and DSDM.

See also: [Agile](#agile), [Scrum](s-z.md#scrum), [XP](s-z.md#xp), [DSDM](d-f.md#dsdm).

### Agile Manifesto
The 2001 statement of the values behind agile development. It prefers individuals and interactions to processes and tools, and working software to comprehensive documentation. It also prefers customer collaboration to contract negotiation, and responding to change to following a plan.

See also: [Agile](#agile).

### AIS
**Alarm Indication Signal.** A signal, all ones, that a transmission element sends downstream in place of traffic when the link feeding it has failed. It keeps the framing intact and tells equipment further along that the fault is upstream.

See also: [SDH](s-z.md#sdh), [PDH](o-r.md#pdh).

### ALCAP
**Access Link Control Application Part.** The UMTS control protocol that sets up and releases AAL2 connections in the radio access network, multiplexing many users onto one AAL2 path. It is the 3GPP version of ITU-T Q.2630.2.

See also: [AAL2](#aal2), [UTRAN](s-z.md#utran).

### Amazon EC2
**Amazon Elastic Compute Cloud.** The AWS service that rents virtual machines, called instances, started from machine images and paid for by the second while they run.

See also: [AWS](#aws), [IaaS](g-k.md#iaas).

### AMP
**Asymmetric Multiprocessing.** A multiprocessor design in which the processors have different roles, for example one running the operating system and the others running dedicated tasks. It is common in embedded systems that pair a general-purpose core with a real-time one.

See also: [SMP](s-z.md#smp), [RTOS](o-r.md#rtos).

### AMR-NB
**Adaptive Multi-Rate Narrowband.** The 3GPP speech codec for narrowband (300 to 3,400 Hz) speech, at eight bit rates from 4.75 to 12.2 kbit/s. The network picks the rate to suit the radio conditions. It is the standard codec for GSM and UMTS voice.

See also: [AMR-WB](#amr-wb), [GSM AMR](g-k.md#gsm-amr), [Audio Codecs](#audio-codecs).

### AMR-WB
**Adaptive Multi-Rate Wideband.** The wideband (50 to 7,000 Hz) version of AMR, also standardised as ITU-T G.722.2. It gives the "HD voice" quality used in VoLTE.

See also: [AMR-NB](#amr-nb), [VoLTE](s-z.md#volte), [G.722](g-k.md#g722).

### Analogy Estimation
Estimating new work by comparing it with similar work done before, and adjusting for the differences.

See also: [Estimation](d-f.md#estimation), [Expert Judgement](d-f.md#expert-judgement).

### Android
Google's mobile operating system, built on the Linux kernel and used on most smartphones and tablets, as well as TVs, cars and watches.

See also: [Linux](l-n.md#linux).

### ANDSF
**Access Network Discovery and Selection Function.** A 3GPP function that tells a mobile device which non-3GPP access networks, such as Wi-Fi, are nearby. It also gives the device policies for choosing between them and the mobile network.

See also: [E-UTRAN](d-f.md#e-utran), [Wi-Fi](s-z.md#wi-fi).

### ANSI
**American National Standards Institute.** The private, non-profit body that coordinates voluntary standards in the United States and represents the country at ISO.

See also: [ISO](g-k.md#iso).

### Antipattern
A common response to a recurring problem that looks reasonable but usually makes things worse.

See also: [Pattern](o-r.md#pattern), [Design Pattern](d-f.md#design-pattern).

### Anycast
An addressing and routing method in which one address is announced from several places, and the network delivers each packet to the nearest one by its routing metrics. DNS root servers and content delivery networks use it.

See also: [Unicast](s-z.md#unicast), [Multicast](l-n.md#multicast), [Broadcast](#broadcast), [Geocast](g-k.md#geocast).

### AOP
**Aspect-Oriented Programming.** A programming paradigm that separates cross-cutting concerns, such as logging or security checks, from the main logic. Code called advice is added at points chosen by a pattern called a pointcut, without editing the code it applies to.

See also: [Programming paradigm](o-r.md#programming-paradigm), [OO](o-r.md#oo).

### API
**Application Programming Interface.** A defined set of calls, messages or endpoints through which one piece of software uses another.

See also: [REST](o-r.md#rest), [SDK](s-z.md#sdk).

### APN
**Access Point Name.** The name a mobile device gives when it opens a data connection. It tells the operator which packet data network to connect it to, such as the public internet or a private company network, and so which addresses and policies apply.

See also: [GGSN](g-k.md#ggsn), [PGW](o-r.md#pgw), [GPRS](g-k.md#gprs).

### Architecture
The top-level structure of a system: its main parts, how they relate, and the principles behind its design.

See also: [ADR](#adr), [High Level Design](g-k.md#high-level-design), [TOGAF](s-z.md#togaf).

### ARP spoofing
An attack on a local network in which the attacker sends forged ARP replies. Other hosts then link the attacker's MAC address to someone else's IP address, often the default gateway's. Traffic then flows through the attacker, who can read, change or drop it. It is also called ARP cache poisoning.

See also: [RARP](o-r.md#rarp), [MAC Spoofing](l-n.md#mac-spoofing), [DNS Spoofing](d-f.md#dns-spoofing).

### Artefact
A tangible product of work, such as a document, a model, source code or a built system.

See also: [Deliverable](d-f.md#deliverable), [Work Product](s-z.md#work-product).

### ASCII
**American Standard Code for Information Interchange.** A 7-bit character encoding for English text, control codes and common symbols. UTF-8 and most other modern encodings keep ASCII as their first 128 characters.

See also: [Unicode](s-z.md#unicode), [UTF-8](s-z.md#utf-8).

### ASN.1 {#asn1}
**Abstract Syntax Notation One.** A language for describing data structures independently of how they are encoded, together with standard encoding rules such as BER, DER and PER. It is widely used in telecoms protocols and in cryptography, for example in X.509 certificates.

See also: [BER](#ber), [DER](d-f.md#der), [PER](o-r.md#per), [CER](#cer), [X.509](s-z.md#x509).

### Assessment
A review of a project's or an organisation's state or practices, often by someone independent.

See also: [Audit](#audit), [Review](o-r.md#review).

### ATDD
**Acceptance Test-Driven Development.** A practice in which customer, developer and tester agree acceptance tests before the feature is built, and the tests then drive the work.

See also: [TDD](s-z.md#tdd), [BDD](#bdd), [Three Amigos](s-z.md#three-amigos).

### ATM
**Asynchronous Transfer Mode.** A connection-oriented switching technology that carries voice, video and data in fixed 53-byte cells. It was the basis of broadband ISDN and was widely used in carrier backbones and DSL access networks before IP and Ethernet replaced it.

See also: [AAL1](#aal1), [AAL2](#aal2), [AAL5](#aal5), [VPI](s-z.md#vpi), [VCI](s-z.md#vci).

### Audio Codecs
Software or hardware that encodes and decodes digital audio in a given coding format, usually compressing it. Speech codecs such as G.711, AMR and Opus are tuned for voice calls; music codecs such as MP3, AAC and Vorbis for general audio.

See also: [Codecs](#codecs), [G.711](g-k.md#g711), [OPUS](o-r.md#opus), [AAC](#aac).

### Audit
A formal, independent assessment, usually against a standard or a contract.

See also: [Assessment](#assessment).

### Author
In a review, the person who wrote the artefact under review and who represents its viewpoint.

See also: [Review](o-r.md#review), [Inspection](g-k.md#inspection).

### Authoritative Answer
A DNS response from a server that is an authority for the zone holding the name asked about. The AA flag in the response header marks it.

See also: [AA](#aa), [DNS](d-f.md#dns).

### Authority
In a project charter, the person who funds and champions the project: the [Project Sponsor](o-r.md#project-sponsor).

### Automated Build
A build that runs from start to finish without anyone stepping in, using only what is in version control, so that anyone can repeat it at any time.

See also: [Build](#build), [Continuous Integration](#continuous-integration).

### Automated Testing
Running tests and checking their results with tools rather than by hand.

See also: [Manual Testing](l-n.md#manual-testing), [Regression testing](o-r.md#regression-testing).

### Awk
A small language for processing text line by line, found on every Unix-like system. An Awk script is a list of patterns and actions, and it is often used for one-line reports and data extraction in pipelines.

See also: [Sed](s-z.md#sed), [Shell Scripting](s-z.md#shell-scripting).

### AWS
**Amazon Web Services.** Amazon's cloud computing platform: virtual machines, storage, databases, networking and many managed services, rented on demand.

See also: [Amazon EC2](#amazon-ec2), [Azure](#azure), [Google Cloud Platform](g-k.md#google-cloud-platform).

### Azure
Microsoft's cloud computing platform, offering infrastructure, platform and software as a service.

See also: [AWS](#aws), [Google Cloud Platform](g-k.md#google-cloud-platform), [IaaS](g-k.md#iaas), [PaaS](o-r.md#paas).

## B

### B2B
**Business-to-business.** Trade between businesses, such as a manufacturer buying parts or a retailer buying stock, as opposed to selling to consumers.

See also: [B2C](#b2c).

### B2C
**Business-to-consumer.** Selling goods or services directly to the people who use them.

See also: [B2B](#b2b).

### Backhaul
The links that connect the edge of a network, such as mobile cell sites or exchange equipment, back to the core. Commercially, it also means wholesale capacity bought from another operator for that purpose.

See also: [RAN](o-r.md#ran), [Leased Line](l-n.md#leased-line).

### Backlog
An ordered list of everything that might be needed to deliver an outcome, such as a product. The items at the top are the most valuable and the best understood.

See also: [Backlog Grooming](#backlog-grooming), [Product Owner](o-r.md#product-owner), [User Stories](s-z.md#user-stories).

### Backlog Grooming
Regular work by the product owner and the team to keep the backlog in order. They add and remove items, prioritise them, and break down the items at the top so they are ready to start. It is also called backlog refinement.

See also: [Backlog](#backlog), [Definition of Ready](d-f.md#definition-of-ready).

### Bandwidth
In networking, the maximum rate at which data can cross a path, in bits per second. In signal processing and radio, it means the range of frequencies a signal occupies, in hertz.

See also: [Latency](l-n.md#latency), [Jitter](g-k.md#jitter).

### Baseline
An agreed version of an artefact that later work builds on. Changes to a baselined artefact go through change control.

See also: [Change Control](#change-control), [Configuration Management](#configuration-management).

### Bash
The GNU Project's Unix shell, a free replacement for the Bourne shell first released in 1989. It is the default shell on most Linux distributions.

See also: [Sh](s-z.md#sh), [Ksh](g-k.md#ksh), [Csh](#csh), [Shell Scripting](s-z.md#shell-scripting).

### BASIC
**Beginner's All-purpose Symbolic Instruction Code.** A family of high-level languages designed in 1964 at Dartmouth College to be easy to learn. It was the language most home computers of the 1980s started with.

See also: [VB](s-z.md#vb).

### BAU
**Business as usual.** The normal day-to-day running of an organisation, as opposed to projects that bring change.

### BDD
**Behaviour-Driven Development.** A practice in which the team describes how a system should behave through concrete examples, often in the Given, When, Then form, and uses them as automated tests.

See also: [Gherkin](g-k.md#gherkin), [Given When Then](g-k.md#given-when-then), [TDD](s-z.md#tdd), [ATDD](#atdd).

### Bench Test
A test run in the development environment on the part of the system being worked on.

See also: [Unit Testing](s-z.md#unit-testing), [Developer Integration Test](d-f.md#developer-integration-test).

### BER
**Basic Encoding Rules.** The original encoding rules for ASN.1, in which each value is written as a type, a length and the value itself. BER allows several encodings of the same value.

See also: [ASN.1](#asn1), [CER](#cer), [DER](d-f.md#der), [TLV](s-z.md#tlv).

### Best Practice
A practice or technique that experience shows to work well for a given goal or risk.

### BFF
**Backend for Frontend.** An architecture pattern in which each kind of client, such as a mobile app or a web app, has its own server-side gateway. The gateway shapes the data and calls that client needs from the services behind it.

See also: [Microservice](l-n.md#microservice), [API](#api).

### BGCF
**Breakout Gateway Control Function.** In IMS, the SIP server that decides where a call leaves the IMS network for the circuit-switched telephone network, based on the dialled number.

See also: [IMS](g-k.md#ims), [MGCF](l-n.md#mgcf), [CSCF](#cscf).

### BGP
**Border Gateway Protocol.** The routing protocol that exchanges reachability information between autonomous systems on the internet. It is a path vector protocol, and routes are chosen by policy as well as by path.

See also: [IGP](g-k.md#igp), [OSPF](o-r.md#ospf), [Router](o-r.md#router).

### Bjarne Stroustrup
The Danish computer scientist who created C++.

See also: [C++](#c_1).

### Black-Box Testing
Testing a system through its interfaces, without looking at how it is built. Also called [Functional Testing](d-f.md#functional-testing).

### Bluetooth
A short-range radio standard in the 2.4 GHz band for connecting devices such as headsets, keyboards and phones into personal area networks. The Bluetooth Special Interest Group manages it.

See also: [ZigBee](s-z.md#zigbee), [Wi-Fi](s-z.md#wi-fi).

### BNF
**Backus-Naur Form.** A notation for writing the grammar of a language as a set of production rules. Extended BNF (EBNF) and augmented BNF (ABNF), the variant used in RFCs, add shorthand for repetition and options.

### BNG
**Broadband Network Gateway.** The router at the edge of a broadband provider's network that terminates subscriber sessions, applies policy and passes their traffic on to the provider's IP network. It is the successor to the BRAS.

See also: [BRAS](#bras), [PPPoE](o-r.md#pppoe), [DSLAM](d-f.md#dslam).

### BOOTP
**Bootstrap Protocol.** An early protocol, defined in RFC 951, with which a device gets an IP address and boot information from a server when it starts. DHCP grew out of it and uses the same UDP ports, 67 and 68.

See also: [DHCP](d-f.md#dhcp), [RARP](o-r.md#rarp).

### Boston Matrix
A two-by-two chart that sorts a company's products by market share and market growth into stars, cash cows, question marks and dogs. It helps decide where to invest. It is also called the growth-share matrix.

### Bottom-Up Estimation
Estimating a system by breaking it into small pieces, estimating each one, and adding up the results.

See also: [Top-Down Estimation](s-z.md#top-down-estimation), [Decomposition Estimation](d-f.md#decomposition-estimation), [Work Breakdown Structure](s-z.md#work-breakdown-structure).

### BPEL
**Business Process Execution Language.** An OASIS XML language for describing business processes as orchestrations of web service calls. It is also written WS-BPEL.

See also: [BPMN](#bpmn), [SOA](s-z.md#soa), [WS-BPEL](s-z.md#ws-bpel).

### BPMN
**Business Process Model and Notation.** A graphical notation, maintained by the Object Management Group, for drawing business processes. Version 2.0 also defines how the diagrams execute.

See also: [BPEL](#bpel), [UML](s-z.md#uml).

### BRAS
**Broadband Remote Access Server.** The router that aggregates broadband sessions from DSLAMs and routes them on to the internet service provider's network. Newer designs call it a BNG.

See also: [BNG](#bng), [DSLAM](d-f.md#dslam), [PPPoE](o-r.md#pppoe).

### BRI
**Basic Rate Interface.** The ISDN access for homes and small businesses. It has two 64 kbit/s bearer (B) channels for voice or data and one 16 kbit/s D channel for signalling, often written 2B+D. In the UK, BT sold it as ISDN2.

See also: [ISDN](g-k.md#isdn), [PRI](o-r.md#pri).

### Broadcast
Sending a message to every receiver on a network segment at once, such as an Ethernet broadcast to all hosts on a LAN.

See also: [Unicast](s-z.md#unicast), [Multicast](l-n.md#multicast), [Anycast](#anycast).

### BSC
**Base Station Controller.** In GSM, the node that controls a group of base transceiver stations: it allocates radio channels, manages handovers between them, and concentrates their traffic towards the MSC.

See also: [BTS](#bts), [MSC](l-n.md#msc), [GSM](g-k.md#gsm), [RNC](o-r.md#rnc).

### BSS
**Business Support Systems.** The systems a telecoms operator uses to run its business with customers, such as ordering, billing and customer management. They sit beside the operations support systems (OSS). In mobile networks, BSS also stands for base station subsystem: the BTSs and BSCs.

See also: [OSS](o-r.md#oss).

### BT 21CN
**BT 21st Century Network.** BT's programme, from the mid-2000s, to replace its separate legacy networks with one IP and MPLS network, using multi-service access nodes (MSANs) in exchanges. The plan to move voice onto it was shelved at the time; the later switch-off of the PSTN finishes that job.

See also: [MSAN](l-n.md#msan), [NGN](l-n.md#ngn), [PSTN](o-r.md#pstn).

### BTNUP
**BT National User Part.** BT's variant of ISDN user part signalling. See [IUP](g-k.md#iup).

### BTS
**Base Transceiver Station.** The radio equipment at a GSM cell site that talks to mobile phones. In UMTS the equivalent is the Node B, and in LTE the eNodeB.

See also: [BSC](#bsc), [Node B](l-n.md#node-b), [E NodeB](d-f.md#e-nodeb).

### Bug
A fault in software that makes it behave other than intended.

See also: [Defect](d-f.md#defect).

### Build
The process that turns source code and other assets into a runnable system. The word also means the result: a version of the system ready to test.

See also: [Automated Build](#automated-build), [Build Environment](#build-environment).

### Build Environment
A separate environment kept for making builds, usually on one or more dedicated build machines.

See also: [Build Machine](#build-machine), [Development Environment](d-f.md#development-environment).

### Build Machine
A computer used only to make software builds.

See also: [Build Environment](#build-environment).

### Build tool
A tool that automates building software, such as Make, Maven or Gradle.

See also: [Build](#build).

### Burndown Chart
A chart that shows the work remaining in an iteration or project against time. A burnup chart shows the work completed instead.

See also: [Velocity](s-z.md#velocity), [Sprints](s-z.md#sprints).

### Burst
A short transmission at a high rate, or a group of errors that arrive close together.

### Business Agility Ownership
Business agility is an organisation's ability to notice change, inside or outside it, and respond quickly enough to keep delivering value to its customers.

See also: [Agile](#agile).

### Business Requirement
A high-level goal of the organisation or customer asking for a system: why it is wanted. Also called a [Why Requirement](s-z.md#why-requirement).

See also: [Requirement](o-r.md#requirement), [Functional Requirement](d-f.md#functional-requirement).

### Business Schedule
A high-level schedule of a project's main milestones and the business goals tied to them. It sets the top-down limits that the detailed schedule must fit.

See also: [Detailed Schedule](d-f.md#detailed-schedule), [Milestone](l-n.md#milestone).

### BYOD
**Bring Your Own Device.** A policy that lets staff use their own laptops, tablets and phones for work, including access to company systems and data. It brings security and support questions that the policy needs to answer.

## C

### C Language
A general-purpose, imperative programming language created by Dennis Ritchie at Bell Labs in the early 1970s to write Unix. Its constructs map closely to machine instructions, so it is still the main language for operating systems and embedded software. It is standardised by ISO as ISO/IEC 9899.

See also: [C++](#c_1), [K & R C](g-k.md#k-r-c), [Embedded systems programming](d-f.md#embedded-systems-programming).

### C++ {#c_1}
A general-purpose language, created by Bjarne Stroustrup as an extension of C, that adds classes, templates and other abstractions while keeping low-level control of memory. It is standardised by ISO, with new versions every three years.

See also: [C Language](#c-language), [Bjarne Stroustrup](#bjarne-stroustrup).

### C-Tag
**Customer VLAN tag.** In IEEE 802.1ad double tagging (Q-in-Q), the inner VLAN tag, set by the customer. The service provider adds an outer S-Tag.

See also: [S-Tag](s-z.md#s-tag), [VLAN](s-z.md#vlan), [Dot1Q](d-f.md#dot1q).

### C# {#c_2}
A general-purpose, object-oriented language from Microsoft, created around 2000 for the .NET platform. It also supports functional and generic programming, and is standardised as ECMA-334 and ISO/IEC 23270.

See also: [.NET](s-z.md#net), [Java](g-k.md#java).

### CA
**Certificate Authority.** A trusted organisation that issues digital certificates, signing each to bind a public key to the named subject. Browsers trust HTTPS sites because a CA they trust signed the site's certificate.

See also: [X.509](s-z.md#x509), [TLS](s-z.md#tls), [HTTPS](g-k.md#https).

### Cacti
An open-source web tool that polls devices, usually over SNMP, and graphs the results with RRDtool, typically to show network traffic and CPU load over time.

See also: [SNMP](s-z.md#snmp).

### Cadence
The regular rhythm of a team's work, such as the length of its sprints or its release cycle.

See also: [Sprints](s-z.md#sprints), [Iteration](g-k.md#iteration), [Timebox](s-z.md#timebox).

### Calendar Days
The elapsed time an activity takes on the calendar. How staff days turn into calendar days depends on how many people work on it, and when.

See also: [Staff Days](s-z.md#staff-days).

### CAMEL
**Customised Applications for Mobile networks Enhanced Logic.** A set of 3GPP standards, based on Intelligent Network ideas, that lets operators add services such as prepaid calling to GSM and UMTS, including while the subscriber is roaming. It uses the CAP protocol.

See also: [CAP](#cap), [IN](g-k.md#in), [INAP](g-k.md#inap).

### Camel Case
Writing compound words with no spaces and a capital letter at the start of each word after the first, as in `camelCase`. Pascal case (`PascalCase`) capitalises the first word too. Many coding standards use one or both for identifiers.

See also: [Snake Case](s-z.md#snake-case), [Hungarian notation](g-k.md#hungarian-notation).

### CAP
**CAMEL Application Part.** The signalling protocol that CAMEL uses between the switch and the service control point. It runs over TCAP in SS7.

See also: [CAMEL](#camel), [TCAP](s-z.md#tcap), [SS7](s-z.md#ss7).

### Capability Maturity Model
**CMM.** A model of software process maturity, developed by the Software Engineering Institute for the US military. It defines five levels: initial, repeatable, defined, managed and optimising. Each level names the key process areas an organisation must have in place. Capability Maturity Model Integration (CMMI) replaced it.

### Cat 5
**Category 5 cable.** Twisted-pair cable rated to 100 MHz, used for 100 Mbit/s Ethernet and telephony. Category 5e superseded it in 2001.

See also: [Cat 5e](#cat-5e), [Cat 6](#cat-6), [Twisted pair](s-z.md#twisted-pair).

### Cat 5e
**Category 5e cable.** An enhanced Category 5 cable with tighter limits on crosstalk, rated to 100 MHz and good for Gigabit Ethernet up to 100 m.

See also: [Cat 5](#cat-5), [Cat 6](#cat-6).

### Cat 6
**Category 6 cable.** Twisted-pair cable rated to 250 MHz, with stricter crosstalk limits than Cat 5e. It carries 10 Gigabit Ethernet up to about 55 m; Category 6A, rated to 500 MHz, does so up to 100 m.

See also: [Cat 5](#cat-5), [Cat 5e](#cat-5e), [Ethernet over twisted pair](d-f.md#ethernet-over-twisted-pair).

### CBOR
**Concise Binary Object Representation.** A binary data format, defined in RFC 8949, based on the JSON data model but designed for small messages and small decoders. It is widely used in constrained IoT devices, with CoAP, and in security tokens.

See also: [JSON](g-k.md#json), [LwM2M](l-n.md#lwm2m).

### CCITT
**Comité Consultatif International Téléphonique et Télégraphique.** The former name, until 1993, of the [ITU-T](g-k.md#itu-t).

### CCS
**Common Channel Signalling.** Telephone signalling carried on a separate channel shared by many voice circuits, rather than in or alongside each circuit. SS7 is the main example. The alternative is channel-associated signalling (CAS).

See also: [SS7](s-z.md#ss7), [ISUP](g-k.md#isup).

### CCTA
**Central Computer and Telecommunications Agency.** A former UK government agency that supported departments' computing and telecoms. It created ITIL and PRINCE.

See also: [ITIL](g-k.md#itil), [PRINCE2](o-r.md#prince2).

### CDMA
**Code-Division Multiple Access.** A channel access method in which many transmitters share the same frequency band at the same time, each spread with its own code. It is the basis of cdmaOne, CDMA2000 and, as wideband CDMA, UMTS.

See also: [CDMA2000](#cdma2000), [W-CDMA](s-z.md#w-cdma), [OFDMA](o-r.md#ofdma).

### CDMA2000
The 3G family of mobile standards developed by 3GPP2 as the successor to cdmaOne (IS-95), used mainly in North America and South Korea. It competed with UMTS.

See also: [CDMA](#cdma), [UMTS](s-z.md#umts).

### CDR
**Call Detail Record.** A record made by a switch or other network element for each call or session, with details such as the numbers, start time, duration and outcome. CDRs feed billing, fraud detection and reporting.

See also: [Mediation](l-n.md#mediation).

### CE
**Customer Edge.** The customer's router that connects to the service provider's provider edge (PE) router in an MPLS VPN. It exchanges routes with the PE, statically or with a routing protocol.

See also: [VRF](s-z.md#vrf), [L3VPN](l-n.md#l3vpn), [NPE](l-n.md#npe).

### CER
**Canonical Encoding Rules.** A restricted form of BER for ASN.1 that allows only one encoding for each value, so that encoded data can be compared or signed.

See also: [BER](#ber), [DER](d-f.md#der), [ASN.1](#asn1).

### Ceremonies
The regular meetings of an agile process, such as sprint planning, the daily stand-up, the review and the retrospective.

See also: [Daily Scrum](d-f.md#daily-scrum), [Sprint Planning](s-z.md#sprint-planning), [Sprint retrospective](s-z.md#sprint-retrospective).

### CESG
**Communications-Electronics Security Group.** The part of GCHQ that was the UK government's technical authority for information assurance. Its role passed to the National Cyber Security Centre in 2016.

See also: [GCHQ](g-k.md#gchq), [NCSC](l-n.md#ncsc), [IA](g-k.md#ia).

### CFi
**Canonical Format Indicator.** A one-bit field in the IEEE 802.1Q VLAN tag that showed whether MAC addresses were in canonical form. It is always 0 on Ethernet, and later revisions renamed it the drop eligible indicator.

See also: [Dot1Q](d-f.md#dot1q), [VLAN](s-z.md#vlan).

### CGI
**Common Gateway Interface.** A standard way for a web server to run an external command to answer a request, passing it the request details and returning its output as the page.

See also: [HTTP](g-k.md#http).

### Change Control
The part of change management that decides which artefacts are controlled and makes sure changes to them are proposed, assessed and approved before they are made. The term is also used for change management as a whole.

See also: [Change Control Board](#change-control-board), [Change Request](#change-request), [Explicit Change Control](d-f.md#explicit-change-control), [Implicit Change Control](g-k.md#implicit-change-control).

### Change Control Board
**CCB.** The group that decides on change requests to artefacts under change control.

See also: [Change Control](#change-control), [Change Request](#change-request).

### Change Control Plan
A plan that sets out what change control applies to which project artefacts.

See also: [Change Control](#change-control).

### Change Management
Managing requested changes to a project's scope, features or artefacts in a controlled way.

See also: [Change Control](#change-control), [Configuration Management](#configuration-management).

### Change Request
**CR.** A request to change something under change control, usually to add, change or remove a requirement, or to change the project plan.

See also: [Change Control Board](#change-control-board), [Software Change Request](s-z.md#software-change-request).

### CHAP
**Challenge-Handshake Authentication Protocol.** A PPP authentication protocol, defined in RFC 1994. The server sends a challenge and the client answers with a hash of the challenge and a shared secret, so the secret never crosses the link. It is safer than PAP.

See also: [PAP](o-r.md#pap), [PPP](o-r.md#ppp), [EAP](d-f.md#eap).

### Chrome OS
Google's operating system, based on the Linux kernel, that uses the Chrome browser as its main interface and runs mostly web applications.

See also: [Linux](l-n.md#linux), [Android](#android).

### Circuit Switched
A network in which a dedicated path is set up between the two ends before they communicate, and held for the whole call, as in the traditional telephone network.

See also: [Packet Switched](o-r.md#packet-switched), [PSTN](o-r.md#pstn), [TDM](s-z.md#tdm).

### Class 4 Softswitch
A softswitch that routes large volumes of voice calls between carriers, the VoIP equivalent of a class 4 (trunk) exchange. What matters most is protocol support and conversion, transcoding and call capacity.

See also: [Softswitch](s-z.md#softswitch), [Class 5 Softswitch](#class-5-softswitch).

### Class 5 Softswitch
A softswitch that serves end users, the VoIP equivalent of a class 5 (local) exchange. It provides subscriber features such as IP PBX functions, call centres and voicemail.

See also: [Softswitch](s-z.md#softswitch), [Class 4 Softswitch](#class-4-softswitch).

### Class Model
A model of the static structure of an object-oriented system: its classes and how they relate.

See also: [UML](s-z.md#uml), [OO](o-r.md#oo).

### CLF
**Connectivity Session Location and Repository Function.** In the ETSI TISPAN next-generation network, the function that records each subscriber's access session, linking their IP address to their line and location. It is not to be confused with the IMS subscriber location function (SLF), which finds the right HSS for a user when there are several.

See also: [NGN](l-n.md#ngn), [HSS](g-k.md#hss), [IMS](g-k.md#ims).

### CMDB
**Configuration Management Database.** A store of the configuration items in an IT estate and the relationships between them, used in ITIL to understand the effect of changes and incidents.

See also: [Configuration Item](#configuration-item), [ITIL](g-k.md#itil).

### CNG
**Comfort Noise Generation.** Adding artificial background noise at the receiving end of a call during silences, when voice activity detection has stopped the sender transmitting. Without it, the line goes dead quiet and callers think the call has dropped.

See also: [VAD](s-z.md#vad), [VoIP](s-z.md#voip).

### COBOL
**Common Business-Oriented Language.** An English-like, compiled language designed in 1959 for business data processing. A great deal of banking and government software on mainframes is still written in it.

See also: [Fortran](d-f.md#fortran).

### Code and Fix Lifecycle
Developing a system from a rough idea through repeated rounds of coding and fixing, with little planning or design, until it seems ready to release.

See also: [Lifecycle](l-n.md#lifecycle), [Waterfall](s-z.md#waterfall).

### Codecs
A codec (coder-decoder) is a device or piece of software that encodes a signal or data stream for transmission or storage, usually compressing it. It also decodes it again for use.

See also: [Audio Codecs](#audio-codecs), [MPEG](l-n.md#mpeg).

### Coding
Writing the source code that defines how software behaves; the core activity of construction.

See also: [Construction](#construction), [Source Code](s-z.md#source-code).

### Coding Standard
See [Construction Standard](#construction-standard).

### CoE
**Centre of Excellence.** A team or group that provides leadership, good practice, support and training in one area, such as a technology or a skill, across an organisation.

### COFDM
**Coded Orthogonal Frequency-Division Multiplexing.** OFDM with forward error correction and interleaving added, so the signal survives multipath fading. Digital terrestrial TV (DVB-T) and DAB use it.

See also: [OFDMA](o-r.md#ofdma), [DTT](d-f.md#dtt).

### Collaboration Model
A model, such as a UML communication diagram, that shows a set of objects or roles and the messages they exchange.

See also: [Sequence Model](s-z.md#sequence-model), [UML](s-z.md#uml).

### Collaborative Construction
A way of building software in which a small group of developers work closely together on the same functionality. They talk often and informally, and share ownership of the code and its tests.

See also: [Pair Programming](o-r.md#pair-programming), [Mob Programming](l-n.md#mob-programming), [Collective code ownership](#collective-code-ownership).

### Collective code ownership
The convention that anyone on the team may change any part of the code, to finish a task, fix a defect or improve its structure.

See also: [XP](s-z.md#xp), [Pair Programming](o-r.md#pair-programming).

### COLO
**Colocation.** Housing equipment in another party's building, typically placing a provider's equipment in a carrier's exchange or a data centre.

### Compatibility Test
See [Configuration Test](#configuration-test).

### Compiled Language
A programming language whose usual implementations translate source code ahead of time into machine code, rather than interpret it. The line is blurred: many languages compile to bytecode that a virtual machine then interprets or compiles just in time.

See also: [Compiler](#compiler), [Interpreted Language](g-k.md#interpreted-language).

### Compiler
Software that translates code from one language, usually a high-level language, into another, usually machine code or bytecode. A typical compiler has a front end, a middle end and a back end. A cross-compiler produces code for a different machine from the one it runs on.

See also: [Compiler Front end](#compiler-front-end), [Compiler Middle end](#compiler-middle-end), [Compiler Back end](#compiler-back-end), [Compiler preprocessor](#compiler-preprocessor), [Machine code](l-n.md#machine-code).

### Compiler Back end
The stage of a compiler that turns the optimised intermediate representation into code for one target processor: choosing instructions, allocating registers and scheduling.

See also: [Compiler](#compiler), [Compiler Middle end](#compiler-middle-end).

### Compiler Front end
The stage of a compiler that reads the source language: it checks syntax and semantics, reports errors, and produces an intermediate representation for the later stages.

See also: [Compiler](#compiler), [Compiler Middle end](#compiler-middle-end).

### Compiler Middle end
The stage of a compiler that optimises the intermediate representation in ways that do not depend on the target processor, such as removing dead code and propagating constants.

See also: [Compiler](#compiler), [Compiler Front end](#compiler-front-end), [Compiler Back end](#compiler-back-end).

### Compiler preprocessor
A tool that transforms source code before compilation, for example the C preprocessor, which expands macros, includes files and handles conditional compilation.

See also: [Compiler](#compiler), [C Language](#c-language).

### Component
A part of a software system with a defined interface and responsibility.

See also: [Component Test](#component-test).

### Component Test
A test of one software component on its own, apart from the rest of the system.

See also: [Unit Testing](s-z.md#unit-testing), [Integration Test](g-k.md#integration-test).

### Cone of Uncertainty
The observation that estimates made early in a project can be wrong by a large factor either way. The range narrows as the project goes on and decisions are made.

See also: [Estimation](d-f.md#estimation), [Progressive Elaboration](o-r.md#progressive-elaboration).

### Configuration Item
**CI.** An artefact, or a group of them, that is placed under configuration management and tracked as a unit.

See also: [Configuration Management](#configuration-management), [CMDB](#cmdb).

### Configuration Management
**CM.** Identifying, recording, releasing and controlling the versions of a system's artefacts so that its state is known at every point.

See also: [Configuration Item](#configuration-item), [Version Control](s-z.md#version-control), [Software Configuration Management](s-z.md#software-configuration-management).

### Configuration Test
A test of how a system behaves on different platforms, settings and environments.

### Construction
Turning a design into working software: detailed design, coding, unit testing, integration and debugging.

See also: [Coding](#coding), [Construction Standard](#construction-standard).

### Construction Environment
See [Development Environment](d-f.md#development-environment).

### Construction Lead
The person responsible for construction on a project: integration, builds, the development environment, technology problems and deployment.

### Construction Standard
The conventions and style developers follow when writing a system's source code. Also called a coding standard.

See also: [Coding Standard](#coding-standard).

### Construction Test Environment
See [Local Test Environment](l-n.md#local-test-environment).

### Construction Testing
The tests a developer runs while building a component, to check changes both in the component and in the system around it.

See also: [Unit Testing](s-z.md#unit-testing), [Developer Integration Test](d-f.md#developer-integration-test).

### Continuous Deployment
Releasing every change that passes the automated pipeline straight to production, so that code reaches users soon after it is written.

See also: [Continuous Integration](#continuous-integration), [DevOps](d-f.md#devops).

### Continuous Integration
**CI.** Merging every developer's changes into a shared mainline several times a day, with an automated build and tests on each merge. The product is then always in a releasable state.

See also: [Automated Build](#automated-build), [Continuous Deployment](#continuous-deployment).

### Control Plane
The part of a network device or network that decides where traffic goes: running routing protocols and building the tables that the data plane uses to forward packets.

See also: [Data Plane](d-f.md#data-plane), [Management Plane](l-n.md#management-plane), [User Plane](s-z.md#user-plane), [SDN](s-z.md#sdn).

### Copyleft
Licensing that lets anyone copy, change and share a work on condition that copies and derived works are shared under the same terms. The GPL is the best-known copyleft licence.

See also: [GPL](g-k.md#gpl), [GNU](g-k.md#gnu).

### CoS
**Class of Service.** A marking in a frame or packet that puts it into a traffic class, so the network can give some classes priority over others.

See also: [QoS](o-r.md#qos), [PCP](o-r.md#pcp), [DSCP](d-f.md#dscp).

### COTS
**Commercial off-the-shelf.** Products bought ready-made, and configured or adapted, rather than built to order.

See also: [Mil-COTS](l-n.md#mil-cots).

### CPE
**Customer Premises Equipment.** Equipment at the customer's site that connects to the operator's network at the demarcation point, such as a router, modem or phone.

See also: [NTU](l-n.md#ntu).

### CPM
**Critical Path Method.** A scheduling technique that finds the longest chain of dependent activities in a project. That chain sets the shortest possible duration, and any delay on it delays the end date.

See also: [PERT chart](o-r.md#pert-chart), [Gantt chart](g-k.md#gantt-chart).

### CPS
**Carrier Pre-Selection.** A UK telephone service that sent a customer's calls through another carrier's network automatically, without dialling a prefix, while the line stayed with the incumbent.

See also: [WLR](s-z.md#wlr), [LCR](l-n.md#lcr).

### CRC
**Cyclic Redundancy Check.** An error-detecting code calculated as the remainder of a polynomial division of the data. The sender appends it; the receiver recalculates it and treats any mismatch as corruption. Ethernet's frame check sequence is a CRC-32.

See also: [FCS](d-f.md#fcs), [Hash Function](g-k.md#hash-function).

### CRC Cards
**Class-Responsibility-Collaborator cards.** Index cards used in object-oriented design sessions, one for each class, listing what the class is responsible for and which classes it works with.

See also: [OO](o-r.md#oo), [Class Model](#class-model).

### CSCF
**Call Session Control Function.** The SIP servers at the heart of IMS. The proxy CSCF (P-CSCF) is the device's first contact with the network. The interrogating CSCF (I-CSCF) finds the right serving CSCF for a user. The serving CSCF (S-CSCF) registers users and controls their sessions.

See also: [IMS](g-k.md#ims), [SIP](s-z.md#sip), [HSS](g-k.md#hss).

### Csh
The C shell, a Unix shell written by Bill Joy at Berkeley in the late 1970s, with a syntax modelled on C. Tcsh is its improved successor.

See also: [Tcsh](s-z.md#tcsh), [Bash](#bash), [Sh](s-z.md#sh).

### CSI
**Customer Site Interconnect.** A physical link between an operator's network and a customer's site or another operator's equipment.

See also: [Leased Line](l-n.md#leased-line).

### CSMA
**Carrier-Sense Multiple Access.** A media access method in which a device listens for traffic on a shared medium and transmits only when it is idle. Classic Ethernet added collision detection (CSMA/CD); Wi-Fi uses collision avoidance (CSMA/CA).

See also: [MAC](l-n.md#mac), [Wi-Fi](s-z.md#wi-fi).

### CSS
**Cascading Style Sheets.** The language that describes how HTML documents are presented, such as layout, colours and fonts, keeping presentation apart from content.

See also: [XML](s-z.md#xml), [W3C](s-z.md#w3c).

### CUE
**Configure Unify Execute.** An open-source language for validating, templating and generating configuration and data. It treats types and values as one thing, so a schema, a constraint and concrete data can be combined and checked in the same way.

See also: [JSON](g-k.md#json), [YAML](s-z.md#yaml).

### Customer Development
A four-step framework from Steve Blank (discovery, validation, creation and building the company) for testing assumptions about a product and its market by experiment.

See also: [MVP](l-n.md#mvp).

### CVSD
**Continuously Variable Slope Delta modulation.** A speech coding method that sends one bit per sample, saying whether the signal went up or down, with a step size that adapts to the signal. It is robust against bit errors and is used in military radio and Bluetooth voice.

See also: [PCM](o-r.md#pcm), [Audio Codecs](#audio-codecs).
