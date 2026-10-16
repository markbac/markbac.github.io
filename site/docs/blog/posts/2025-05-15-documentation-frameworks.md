---
date: 2025-05-15T09:05:00
authors:
  - markbac
categories:
  - Docs as Code
slug: documentation-frameworks
---

# Frameworks That Bring Order to Documentation

Most of us have been burned by unstructured documentation.

<!-- more -->

You know the drill: dozens of Markdown files scattered across folders, architecture notes buried in a README, overlapping diagrams with no explanation. Or worse — all of it duplicated in a slide deck last updated six months ago.

What most teams lack isn’t effort. It’s **structure**.

This post explores the frameworks that provide just that — repeatable, usable, durable structure. The kind that survives through features, refactors, and team turnover. And I’ll walk through how to apply these frameworks within a Docs-as-Code setup.

---

## Why Use a Documentation Framework?

Documentation frameworks offer:

- **Clarity** – you know what to write and what to omit
- **Consistency** – everyone uses the same format and language
- **Traceability** – you can follow decisions and structure across views
- **Reusability** – you can lift and reuse the model in other projects or products

When you embed frameworks into your Docs-as-Code practice, they become sustainable — and automated.

---

## 1. arc42: The Modular Powerhouse

Originally designed for German engineering and systems architecture, **arc42** is modular, pragmatic, and works across embedded, system, and software architecture.

### Highlights

- 12 sections covering everything from goals to runtime and quality
- Works at different levels (system, product, deployment)
- Easily mapped to Markdown

### Typical sections

- Introduction and goals
- Constraints
- Context and scope
- Building blocks
- Runtime behaviour
- Quality scenarios
- Risks and technical decisions

📌 **Why I like it**: You can use just the bits you need. It’s not all-or-nothing.

---

## 2. ISO/IEC 42010: Views and Viewpoints

This one’s more formal, but it’s the standard that underpins a lot of other frameworks.

### Core idea

- Architecture = system of **views**
- Each view answers a stakeholder concern
- Viewpoints define how to construct those views

### Example

| View         | Viewpoint        | Stakeholder     | Concern                        |
|--------------|------------------|------------------|--------------------------------|
| Deployment   | Tech Infrastructure | Ops / SRE      | Where does it run?            |
| Functional   | Behavioural Model | Developer       | What does it do and when?     |
| Development  | Code & Structure | Engineer         | What’s the component boundary?|

📌 **Why I like it**: It forces you to think about who you're writing for — not just what you're writing.

---

## 3. Rozanski & Woods: Practical Perspectives

This is my go-to recommendation for engineers who want **depth without drowning**.

The authors identify **7 architectural views**, each with practical focus:

- **Logical**: functional breakdown
- **Development**: modules, dependencies, repos
- **Process**: runtime execution flows
- **Physical**: deployment on infrastructure
- **Scenarios**: use cases and event flows
- **Security**: threats, mitigations, trust boundaries
- **Data**: storage, movement, consistency

Each view supports specific stakeholder needs, and you can adapt them per team or product type.

📌 **Why I like it**: It bridges system and software architecture without going full enterprise.

---

## 4. The C4 Model: Simple, Scalable, Visual

Popularised by Simon Brown, C4 stands for:

- **Context** – what’s in/out of scope
- **Container** – major deployable units (e.g., services, apps, firmware blocks)
- **Component** – inner structure of each container
- **Code** – optional level for classes/functions

### Example hierarchy

```plaintext
System: IoT Device Platform
├── Context: Device ↔ Cloud ↔ User
├── Container: Embedded App, API Gateway, UI
├── Component: State Manager, Sensor Poller, Auth Handler
```

C4 diagrams work beautifully with **Structurizr DSL** or **Mermaid** in a Docs-as-Code setup.

📌 **Why I like it**: It gives just enough structure for diagrams to make sense without needing UML.

---

## Comparison Table

| Framework         | Best For                             | Formality | Flexibility | Tooling Support | Docs-as-Code Fit |
|------------------|---------------------------------------|-----------|-------------|------------------|------------------|
| arc42            | Modular system or product docs        | Medium    | High        | High (Markdown)  | Excellent        |
| ISO/IEC 42010    | Enterprise or regulated environments  | High      | Medium      | Medium           | Good             |
| Rozanski & Woods | Full-stack system + software views    | Medium    | High        | Medium           | Good             |
| C4 Model         | Visualising software architecture     | Low       | High        | High (Mermaid, Structurizr) | Excellent |

---

## Using Frameworks in Docs-as-Code

Here’s how I embed these frameworks in practice:

### 1. Folder structure

```plaintext
docs/
├── context/
├── containers/
├── components/
├── views/
│   ├── logical/
│   ├── physical/
│   └── development/
├── arc42/
│   ├── constraints.md
│   ├── quality-scenarios.md
```

### 2. Metadata and navigation

Use frontmatter like:

```yaml
title: "Firmware State Manager Design"
view: "Logical"
framework: "Rozanski-Woods"
component: "Device Platform"
```

Static site generators like **MkDocs** or **Docusaurus** can use this to create filtered navigation or tag-based indexes.

### 3. Reuse and references

- Link ADRs to views (`See: development/logging-structure.md`)
- Include diagrams inline with explanations
- Annotate diagrams by stakeholder concern (security, data, performance)

---

## Cheat Sheet Summary

| Use Case                          | Framework           | View/Section to Start With      |
|----------------------------------|---------------------|----------------------------------|
| API Gateway Integration          | C4 + Rozanski-Woods | Container + Data + Security     |
| Embedded platform documentation  | arc42 + C4          | Context + Building Blocks       |
| Cloud Infrastructure Deployment  | ISO + Rozanski      | Physical + Deployment Views     |
| Secure Messaging Design          | Rozanski + C4       | Scenario + Component + Security |
| Regulated system traceability    | ISO 42010 + arc42   | Viewpoints + Constraints        |

---

## Final Thoughts

The point of a framework isn’t to write more — it’s to write **the right things**, for the right people, at the right time.

I use arc42 when I need structure across multiple teams.  
I use C4 when I want clean diagrams.  
I use Rozanski & Woods when I want to explain behaviour, security, or runtime.  
I use ISO when auditors get involved.

Pick what fits. Adapt what works. And make your Docs-as-Code setup not just automated — but structured, explainable, and useful.

---

📘 Next in the series: [Canvas Tools for Strategy, Communication, and Clarity](2025-05-15-canvas-tools.md)
