---
title: Product conformance profile and component register
---

# Product conformance profile and component register

Engineering guidelines are written for every product, but no two products need exactly the same rules. A small sensor and a safety controller should not carry the same paperwork. The conformance profile records, for one product, which guidelines apply, which values it changes, and which exceptions it holds. The component register lists what the product is built from and who owns each part.

Keep both in the product's repository and review them at each release.

## Conformance profile

Core rules apply to every product and cannot be tailored, so they never appear in the tailoring table. Every other change to a default needs a reason and an approver. Every exception needs an expiry date.

```markdown
---
product: Product name
technical-lead:
version: 0.1.0
last-reviewed: YYYY-MM-DD
review-by: YYYY-MM-DD
---

# Conformance profile: product name

## Scope

What the product is, its target hardware, and its main risks: safety,
security and regulatory.

## Guideline applicability

| Guideline | Applies | Notes |
|-----------|---------|-------|
| EG-001 | Yes | |
| EG-023 | No | No certification needed. Revisit if the market changes |

## Tailored rules and values

| Rule | Default | This product | Reason | Approved by |
|------|---------|--------------|--------|-------------|
| PRR-09 | One working day | | | |

## Exceptions

| Rule | Scope | Reason | Approved by | Expires |
|------|-------|--------|-------------|---------|

## Toolchain

- Compiler and version:
- Build system:
- Static analysis:
- Test frameworks and rigs:

## Components

Link to the component register (`docs/components.yaml`), and list the
components this product provides to others.

## Quality attribute profile

The top three quality attributes, and any change to their order of
precedence, with the ADR that records it.
```

## Component register

A list of the product's components, kept as YAML so tools can check it. Each entry names an owner and a deputy, preferably at another site, and lists the interfaces it provides and the products that use it. Download [`component-register.yaml`](https://github.com/markbac/markbac.github.io/raw/main/content/templates/files/component-register.yaml).

[[CAPTION:Figure]] Component register.

```yaml
components:
  - name: component-name
    owner: "Name or role"
    deputy: "Name or role"          # ideally at another site
    repository: "git@example.com:group/component.git"
    version: 0.0.0
    status: active                  # active | maintenance | deprecated | retired
    consumers: [product-a]          # products that use it
    interfaces: [IF-0000]           # interface specifications it provides
    variation-points: []            # where products may configure or extend it
    third-party: false              # true for bought-in or open-source components
    licence:                        # SPDX identifier, for third-party components
```

The register is also the starting point for the software bill of materials: every component marked `third-party` needs its licence and version recorded.
