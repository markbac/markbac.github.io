---
title: Requirements and quality scenarios
---

# Requirements and quality scenarios

These two templates help you write requirements that can be traced and tested. The first is for a single requirement, kept as data. The second is for a quality attribute (non-functional) requirement, written as a scenario.

## Requirement

Keep each requirement as a small YAML record in the repository, one file per requirement or one list per component. Tools can then check the IDs, build the traceability matrix, and fail the build when a requirement has no test.

[[CAPTION:Figure]] Requirement record (download [`requirement.yaml`](https://github.com/markbac/markbac.github.io/raw/main/content/templates/files/requirement.yaml)).

```yaml
id: REQ-XX-0000          # stable, never reused
title: Short title
statement: The system shall ...
type: functional         # functional | performance | security | safety | interface | constraint
level: firmware          # system | subsystem | software | firmware | hardware
parent: REQ-SYS-0000     # the requirement this one refines
verification: test       # test | analysis | inspection | demonstration
status: draft            # draft | approved | implemented | verified | retired
owner:
rationale: Why this requirement exists.
```

Good requirement statements:

- Use "shall" for a requirement and nothing else, one requirement per statement.
- Can be verified. "Fast" cannot be tested and "within 200 ms" can.
- Say what is needed, not how to build it.
- Trace up to a parent and down to the design and the tests. Name tests after the requirement IDs they verify.

## Quality scenario

A quality attribute such as performance, availability or security means little until it is measurable. A scenario states what triggers the behaviour, under which conditions, what the system does and how the response is measured.

[[CAPTION:Figure]] Quality attribute scenario.

```text
ID:           NFR-XXXX-000
Attribute:    Performance and timing
Source:       Who or what causes the stimulus
Stimulus:     The event that triggers the behaviour
Environment:  The conditions under which the requirement applies
Response:     What the system does
Measure:      How the response is measured, with a threshold
Verification: Test | Analysis | Inspection | Demonstration
```

For example:

```text
ID:           NFR-GW-012
Attribute:    Availability
Source:       Mobile network
Stimulus:     The cellular connection drops
Environment:  Normal operation, signal of -110 dBm or better
Response:     The gateway buffers readings and reconnects
Measure:      Reconnects within 60 s in 99 % of drops, with no lost readings
Verification: Test (hardware-in-the-loop network drop test)
```
