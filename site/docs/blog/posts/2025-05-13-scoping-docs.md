---
date: 2025-05-13T09:02:00
authors:
  - markbac
categories:
  - Docs as Code
slug: scoping-docs
---

# Writing for Systems, Products, and Projects – Scoping Documentation the Right Way

One of the biggest documentation problems I’ve seen in engineering organisations — whether we’re talking about embedded firmware, cloud services, or head-end systems — is this. There’s a lack of clarity on **who writes what, where it lives, and who owns it**. We end up with duplicated interface specs, system diagrams out of sync with platform documentation, and project teams guessing what applies to them.

<!-- more -->

This post is about fixing that.

It's about scoping documentation correctly across three levels:

- **Systems** — end-to-end integrations
- **Products** — long-lived reusable platforms
- **Projects** — bespoke deployments and customer overlays

It’s aimed at engineers, tech leads, and architects working across teams, stacks, or release lines. And it’s particularly useful when you’re trying to avoid documentation rot, drift, and repetition.

---

## Start with Separation of Concerns

The most powerful idea in software applies equally to documentation: **separation of concerns**.

| Concern         | Typical Focus                                  | Typical Artefacts                                 |
|-----------------|-------------------------------------------------|--------------------------------------------------|
| **System**       | Integration of products in a delivery context   | System context diagrams, integration specs, solution vision, deployment views |
| **Product**      | Reusable platforms, firmware, services          | API docs, state machines, internal component diagrams, SDKs, test coverage strategy |
| **Project**      | Customer-specific configs, overlays             | Install guides, customer integration notes, regional deployment adjustments, regulatory packs |

Trying to document all of this in one structure or format will lead to chaos. These scopes need **separate ownership**, **different lifecycles**, and **tailored documentation approaches**.

---

## 1. System-Level Documentation

System documentation captures how various products come together to form a solution. It’s often **project-scoped**, meaning the integration and delivery context will differ between customers or use cases.

### Common artefacts

- System context diagrams (C4 Level 1)
- End-to-end data flow diagrams
- Integration point definitions
- Risk registers and trade-off discussions (e.g. comms protocol selection)
- Solution vision documents
- Quality attribute mapping and compliance traceability

📌 **Tip**: These docs are often temporary in scope (for the duration of a delivery project) but critical for integration and testing phases.

### Example

<!-- vale PyDoc.Spelling = NO -->

In a smart metering rollout, the system doc would describe how the meter firmware integrates with the head-end system, billing engine, and third-party data collector. It would include the assumptions and custom mappings required.

<!-- vale PyDoc.Spelling = YES -->

---

## 2. Product-Level Documentation

Product documentation should describe **what the product is** — not how it's used in a particular system.

This includes firmware platforms, application services, APIs, and shared libraries.

### Common artefacts

- Firmware module overviews
- State machine diagrams
- RTOS scheduling strategy
- REST/gRPC/serial API definitions
- C4 container and component views
- Test strategy and verification matrices

These docs are long-lived and should be versioned alongside the product. They support both **product development** and **reuse** across multiple system-level deployments.

📌 **Tip**: Store product docs close to the product repo or in a dedicated product documentation repo with tagged versions.

### Example

<!-- vale PyDoc.Spelling = NO -->

Take the comms stack used by multiple embedded devices, whether in a gas meter, heat pump, or controller. It has a single set of API docs, test strategies, and diagrams describing its internal design. Projects then document how that stack is configured or extended.

<!-- vale PyDoc.Spelling = YES -->

---

## 3. Project-Level Documentation

Project-level docs are **where the reality happens** — configs, tweaks, client-specific integration points. These are often the most volatile docs and should be lightweight, accurate, and maintained alongside deployment or infra code.

### Common artefacts

- Regional deployment diagrams
- Customer-specific config
- Onboarding/install guides
- Project-specific risk mitigations
- Firmware parameter overlays
- Delivery checklists and handover notes

📌 **Tip**: Keep these docs in the same repo as your infrastructure or config-as-code, not in your product SDK repo.

---

## Avoiding Duplication

Duplication happens when teams:

- Copy product docs into project folders (then forget to update them)
- Document system-level integration logic in firmware-level design docs
- Use shared diagrams without clear ownership

To avoid this, I recommend using **inheritance and overlay patterns**:

- Product doc contains “how the system works”
- Project doc contains “how it’s configured for this customer”
- System doc contains “how all parts integrate for this delivery”

📌 Diagrams can be reused if they are versioned and included by reference (e.g. embedded Mermaid from a central folder, or Structurizr workspace components).

---

## Who Owns What?

Here’s a practical ownership matrix that’s worked for me:

| Artefact Type                       | Scope     | Owned By              | Maintained Where                          |
|------------------------------------|-----------|------------------------|--------------------------------------------|
| Firmware state diagram             | Product   | Firmware engineer      | Firmware repo docs/ directory              |
| API definition (serial/MQTT/etc)   | Product   | Platform team          | Shared protocol spec repo                  |
| Customer install guide             | Project   | Integration engineer   | Infra/deployment repo                      |
| System context diagram             | System    | Solution architect     | Project documentation repo                 |
| Runbook or support flow            | System    | Ops/DevOps             | Shared runbook repo / project overlay      |
| RFC for new feature                | Product   | Feature owner          | Product doc or RFC repo                    |

---

## Using Docs-as-Code to Enforce Scope

When using Docs-as-Code, this separation becomes **enforceable**:

- Folder structures define scope: `/product/`, `/system/`, `/project/`
- Frontmatter tags can include: `scope: product`, `owner: firmware`
- CI rules can ensure that only certain teams approve certain folders
- Static sites can render these docs under different sections with different audiences

---

## Common Pitfalls

1. **Dumping all docs in a shared repo with no structure**  
   This leads to navigation hell and version mismatches.

2. **Copy-pasting diagrams or specs between system and product docs**  
   Now you’ve got two truths — and neither is reliable.

3. **Over-centralising ownership**  
   If the architecture team owns every doc, nothing gets updated. Push ownership to where the knowledge is.

4. **No overlays**  
   Every project rewrites the same “how to integrate” notes because product docs are too generic. Use overlays.

---

## Summary

Documentation only adds value if it’s scoped right. In modern systems, that means clearly separating:

- System docs (for integration and delivery)
- Product docs (for design, architecture, reuse)
- Project docs (for configuration, deployment, support)

Docs-as-Code gives us the tools to enforce this: folder structure, tagging, version control, and review.

But it’s the discipline that matters more.

As an architect or engineering lead, it’s your job to make documentation **fit the system**, **fit the delivery**, and **fit the team**. Get the scope wrong, and you’ll bury your knowledge in chaos. Get it right, and your documentation becomes a strategic asset — one that survives teams, timelines, and tooling fads.

---

📘 Next in the series: [Structuring Docs for Complex Systems: Layered, Flexible, and Discoverable](2025-05-13-structuring-docs.md)
