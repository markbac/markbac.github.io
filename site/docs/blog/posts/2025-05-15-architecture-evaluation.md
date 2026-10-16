---
date: 2025-05-15T09:07:00
authors:
  - markbac
categories:
  - Docs as Code
slug: architecture-evaluation
---

# Architecture Evaluation and Trade-Off Analysis

Architectural decisions aren't just about picking the best-looking diagram. They're about **trade-offs**. Every technical choice — from a protocol to a cloud provider, from memory layout to messaging patterns — carries consequences.

<!-- more -->

As a system architect or lead engineer, your job isn't to get it perfect. It's to understand what you're trading off, why, and what risks you're taking on. And to make sure everyone else understands too.

In this post, I’ll walk through practical ways to evaluate architectural options — from formal methods like ATAM to lightweight, docs-as-code-friendly approaches. You’ll see how to document trade-offs, link them to decisions, and embed evaluations into your existing artefacts like ADRs and risk logs.

---

## Why Architecture Evaluation Matters

I’ve lost count of the times I’ve seen architecture presented as fait accompli — a glorious Visio diagram on slide 12 of a 30-slide deck. No risks. No constraints. No alternatives considered.

That’s not architecture. That’s fiction.

Real architecture is:

- Incomplete by design
- Full of tension between qualities (speed vs safety, flexibility vs cost)
- Sensitive to context (teams, skills, existing tech)

Evaluation gives you the language and structure to **explain** and **defend** those tensions.

---

## 1. ATAM: The Structured Classic

The **Architecture Trade-off Analysis Method (ATAM)** was developed at the SEI and is still the most comprehensive evaluation framework around.

### Core Concepts

- Identify **business drivers**
- Elicit **quality attributes** (e.g. performance, modifiability, reliability)
- Describe the architecture
- Identify **scenarios** that stress the design
- Analyse trade-offs, risks, and sensitivity points

### Quality Attribute Scenarios

Each one has:

- Stimulus (e.g. hardware failure, new config)
- Source (user, device, admin)
- Environment (runtime, update)
- Response (what happens)
- Response measure (e.g. time to failover)

### Why it’s good

- Structured, repeatable
- Supports auditing and regulation
- Forces the team to state assumptions

### Why it’s heavy

- Requires facilitation and time
- May feel too formal in lean or agile teams

---

## 2. Lightweight Alternatives

I’ve had great success with simplified evaluations. You don't need a workshop to assess trade-offs — you just need clarity.

### Trade-Off Table

| Option | Benefits | Drawbacks | Risks | Notes |
|--------|----------|-----------|-------|-------|
| JSON over REST | Simple, debuggable, supported | Verbose, no binary support | High bandwidth use | Matches existing stack |
| Protobuf over gRPC | Efficient, typed | Harder to debug, learning curve | Schema evolution risk | Used by cloud partner |
| FlatBuffers | Zero-copy, low memory | Complex toolchain | Poor IDE support | Best for constrained devices |

📌 **Tip**: Keep this table in your RFCs or inline in ADRs.

---

## 3. Connecting Quality Attributes to Choices

Before you can evaluate trade-offs, you need to understand your quality goals.

| Quality Attribute | Evaluation Metric | Example Constraint |
|-------------------|-------------------|---------------------|
| Performance       | Latency, throughput | Must process message <200ms |
| Reliability       | MTBF, failover time | Must recover <5s |
| Modifiability     | LOC changed for feature | No more than 10% module churn |
| Scalability       | Load vs cost curve | Must support 10x users in 1yr |

Include these metrics in your Solution Vision or test strategy. Then evaluate your architecture **against** them.

---

## 4. Structuring Evaluation Outputs

### In ADRs

```markdown
## Alternatives Considered

| Option | Pros | Cons |
|--------|------|------|
| JSON | Easy, readable | Bulky, inefficient |
| Protobuf | Compact | Hard to debug |

## Risks
- Message bloat (JSON)
- Migration complexity (Protobuf)

## Justification
We prioritise readability over compactness for Phase 1 MVP. Revisit before scale-up.
```

### In Risk Logs

| ID | Risk | Impact | Mitigation | Linked Decision |
|----|------|--------|------------|------------------|
| R-21 | Slow cold-start of container | High | Warm pool | ADR-019 |

### In RFCs

Include:

- Summary of options
- Evaluation matrix
- Stakeholder input
- Preferred choice + rationale

---

## 5. Real-World Scenario Example

Say you’re designing a telemetry ingestion path from a device to cloud.

- Option A: HTTP push from device
- Option B: MQTT over TLS
- Option C: Custom UDP binary format

Now layer on quality attributes:

- Reliability: MQTT wins
- Simplicity: HTTP wins
- Efficiency: UDP wins

What’s the trade-off?

You might choose MQTT, accept the slight complexity, and mitigate with test tooling and retries.

📌 Embed this reasoning in the decision artefact. Don’t just say “we chose MQTT” — explain why.

---

## 6. Embedding in Docs-as-Code

### Folder layout

```plaintext
docs/
├── adr/
│   ├── adr-003-mqtt-choice.md
│   └── adr-004-tls-handshake-design.md
├── rfc/
│   ├── rfc-001-device-ingestion-protocol.md
├── risks/
│   └── risk-log.md
├── vision/
│   └── quality-attributes.md
```

### Metadata example

```yaml
title: "Protocol Evaluation for Telemetry Ingest"
type: "evaluation"
linked_adr: "adr-003"
quality_focus: ["performance", "modifiability"]
review_date: 2025-05-01
```

This makes evaluations searchable, taggable, and traceable across the project.

---

## Final Thoughts

Architecture isn’t about “picking the right tech”. It’s about evaluating options **in context**, and explaining what you’re trading off.

You don’t need heavyweight processes. But you do need structure:

- Capture quality goals
- Compare options with context
- Document risks and rationale
- Revisit when constraints change

Whether you use ATAM or a one-table summary, embedding evaluation into Docs-as-Code makes it part of your delivery pipeline — not a forgotten slide.

---

📘 Next in the series: [Tools of the Trade: Building a Docs-as-Code Stack That Works](2025-05-15-docs-as-code-tools.md)
