---
title: G
---

# G

## G.711 {#g711}
The ITU-T standard, from 1972, for coding telephone speech as 64 kbit/s PCM: 8,000 samples a second, each companded to 8 bits. It has two variants, A-law and µ-law. It is the baseline codec that every VoIP system supports.

See also: [A-law](a.md#a-law), [Mu-law](m.md#mu-law), [PCM](p.md#pcm), [G.711.1](#g7111).

## G.711.1 {#g7111}
A wideband extension of G.711, from 2008, that adds layers on top of a G.711 core. It runs at 64, 80 or 96 kbit/s, and a G.711-only receiver can still decode the core.

See also: [G.711](#g711), [G.722](#g722).

## G.719 {#g719}
An ITU-T codec for full-band audio (20 Hz to 20 kHz) at 32 to 128 kbit/s, developed by Polycom and Ericsson for high-quality conferencing. It handles music as well as speech.

See also: [G.722](#g722), [Audio Codecs](a.md#audio-codecs).

## G.722 {#g722}
An ITU-T wideband speech codec from 1988, covering 50 to 7,000 Hz at 48 to 64 kbit/s using sub-band ADPCM. It is widely used for HD voice on desk phones. G.722.1 and G.722.2 (AMR-WB) are different codecs despite the names.

See also: [G.711](#g711), [AMR-WB](a.md#amr-wb).

## G.723.1 {#g7231}
An ITU-T low-rate speech codec, at 5.3 or 6.3 kbit/s, with 30 ms frames. It was common in early VoIP and H.323 systems. It is unrelated to the older G.723.

See also: [G.726](#g726), [H.323](h.md#h323).

## G.726 {#g726}
An ITU-T ADPCM speech codec at 16, 24, 32 or 40 kbit/s, which replaced G.721 and G.723. The 32 kbit/s rate, half that of G.711, is the most used, for example in DECT cordless phones.

See also: [G.711](#g711), [PCM](p.md#pcm).

## G.Fast {#gfast}
An ITU-T DSL standard (G.9700 and G.9701) for very short copper lines, up to a few hundred metres, giving several hundred megabits per second. It is used from a distribution point or cabinet fed by fibre.

See also: [VDSL](v.md#vdsl), [DSL](d.md#dsl), [DP](d.md#dp).

## Gantt chart
A bar chart of a project schedule, with tasks down the side and time along the top. It shows when each task starts and ends, and how the tasks depend on each other.

See also: [PERT chart](p.md#pert-chart), [CPM](c.md#cpm).

## Gap analysis
Comparing where things are now with where they need to be, to find what must change to get there.

## Gate
A set of criteria that must be met before work can pass from one phase or stage to the next.

See also: [Gate Checklist](#gate-checklist), [Phase](p.md#phase).

## Gate Checklist
A checklist used to check that the criteria for a gate have been met.

See also: [Gate](#gate).

## GBE / GE {#gbe-ge}
Abbreviations for [Gigabit Ethernet](#gigabit-ethernet).

## GCHQ
**Government Communications Headquarters.** The UK's signals intelligence and security agency, based in Cheltenham. It grew out of the Government Code and Cypher School of Bletchley Park, and runs the National Cyber Security Centre.

See also: [NCSC](n.md#ncsc), [CESG](c.md#cesg).

## Geocast
Delivering a message to all the nodes in a geographical area, rather than to a list of addresses. It is a form of multicast used in some mobile ad hoc and vehicle networks.

See also: [Multicast](m.md#multicast), [MANET](m.md#manet).

## GERAN
**GSM EDGE Radio Access Network.** The radio access network of GSM and EDGE: the base stations, their controllers and the interfaces between them. 3GPP maintains its standards.

See also: [BTS](b.md#bts), [BSC](b.md#bsc), [EDGE](e.md#edge), [UTRAN](u.md#utran).

## GGSN
**Gateway GPRS Support Node.** The GPRS and UMTS core node that connects the mobile packet network to external networks such as the internet. It allocates the device's IP address and anchors the session as the user moves. In LTE the PGW does this job.

See also: [SGSN](s.md#sgsn), [GPRS](#gprs), [APN](a.md#apn), [PGW](p.md#pgw).

## Gherkin
The plain-language format used by Cucumber and similar tools to write behaviour-driven tests. Scenarios are written as `Given`, `When` and `Then` steps under a `Feature`, so that business people and developers can read the same tests.

See also: [BDD](b.md#bdd), [Given When Then](#given-when-then).

## Gigabit Ethernet
Ethernet at 1 Gbit/s, defined in IEEE 802.3. It replaced Fast Ethernet as the usual speed for wired networks from the early 2000s.

See also: [GBE / GE](#gbe-ge), [100 Mbps (Fast Ethernet)](numbers.md#100-mbps-fast-ethernet), [Ethernet over twisted pair](e.md#ethernet-over-twisted-pair).

## Git
A distributed version control system, created by Linus Torvalds in 2005 for the Linux kernel. Every clone holds the full history, so most work is local and fast, and branching and merging are cheap.

See also: [Version Control](v.md#version-control), [Subversion](s.md#subversion).

## Given When Then
A template for writing acceptance criteria and tests: given some context, when an action happens, then expect these results.

See also: [Gherkin](#gherkin), [BDD](b.md#bdd).

## GMSC
**Gateway Mobile Switching Centre.** An MSC function that routes calls between the mobile network and other networks. For an incoming call it asks the HLR where the subscriber is.

See also: [MSC](m.md#msc), [HLR](h.md#hlr).

## GNU
**GNU's Not Unix.** The free software operating system started by Richard Stallman in 1983, made up of tools, libraries and compilers. Combined with the Linux kernel, it forms most Linux distributions.

See also: [GPL](#gpl), [Linux](l.md#linux), [Copyleft](c.md#copyleft).

## Go
A statically typed, compiled language created at Google in 2009 by Robert Griesemer, Rob Pike and Ken Thompson. It has garbage collection, built-in concurrency with goroutines and channels, and fast builds. It is also called Golang.

## Goals
The results a project, process or activity is meant to achieve. Also called objectives.

See also: [Objectives](o.md#objectives).

## GoF
**Gang of Four.** The four authors (Gamma, Helm, Johnson and Vlissides) of *Design Patterns: Elements of Reusable Object-Oriented Software* (1994). The book catalogues 23 object-oriented design patterns.

See also: [Design Pattern](d.md#design-pattern).

## Google Cloud Platform
Google's cloud computing services, offering infrastructure, platform and serverless computing, data analytics and machine learning on the infrastructure Google uses itself.

See also: [AWS](a.md#aws), [Azure](a.md#azure).

## GPL
<!-- vale PyDoc.Spelling = NO -->
**GNU General Public License.**
<!-- vale PyDoc.Spelling = YES -->
The most widely used copyleft free software licence, written by Richard Stallman. It lets anyone run, study, share and change the software, as long as they share copies and derived works under the same licence.

See also: [Copyleft](c.md#copyleft), [GNU](#gnu).

## GPRS
**General Packet Radio Service.** The packet data service added to GSM, giving always-on connections charged by data volume rather than by time. It is best-effort, with speeds of tens of kilobits per second.

See also: [GSM](#gsm), [EDGE](e.md#edge), [SGSN](s.md#sgsn), [GGSN](#ggsn).

## GSM
**Global System for Mobile communications.** The second-generation (2G) digital mobile standard, developed by ETSI and first launched in 1991. It was designed for circuit-switched voice and SMS, and GPRS and EDGE later added data.

See also: [GPRS](#gprs), [EDGE](e.md#edge), [UMTS](u.md#umts), [SIM](s.md#sim).

## GSM AMR
The AMR speech codec as used in GSM. See [AMR-NB](a.md#amr-nb).

## GSM-FR
**GSM Full Rate.** The first GSM speech codec (GSM 06.10), at 13 kbit/s. Its quality is poor by modern standards; Enhanced Full Rate and AMR replaced it.

See also: [GSM AMR](#gsm-amr), [AMR-NB](a.md#amr-nb).

## GSM-R
**GSM for Railways.** A version of GSM for railway voice and data, including the signalling of the European Rail Traffic Management System. It is designed to work at train speeds up to 500 km/h.

See also: [GSM](#gsm).

## GSN
**GPRS Support Node.** A node in the GPRS core network: either a serving node (SGSN) or a gateway node (GGSN).

See also: [SGSN](s.md#sgsn), [GGSN](#ggsn).
