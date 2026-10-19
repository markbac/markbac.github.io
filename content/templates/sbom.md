---
title: Software bill of materials
---

# Software bill of materials

Use this template to describe the components a product is built from, with their versions, licences and known vulnerabilities. For anything you ship, generate the bill of materials in a standard format such as CycloneDX or SPDX as part of the build, and keep this page as the summary.

## Template

```markdown
---
title: Software Bill of Materials (SBOM) - [Product/System Name] v[Version Number]
status: Draft / Generated / Verified / Baselined
date: YYYY-MM-DD (Date of Generation)
author: [Name or Role of SBOM Generator/Owner]
version: 1.0
related_documents:
  - Release Plan - [Product Name] v[Version Number]
  - Risk Register - [Product Name]
---

# Software Bill of Materials (SBOM): [Product/System Name] v[Version Number]

This document lists all software components, including open-source and commercial, that are incorporated into [Product/System Name] version [Version Number]. It provides transparency into our software supply chain, enabling proactive vulnerability management, license compliance, and risk assessment.

---

## 1. Introduction

### 1.1 Purpose

The purpose of this Software Bill of Materials (SBOM) is to:
* Provide a comprehensive inventory of all software components within the product.
* Facilitate vulnerability management by identifying affected components when new vulnerabilities are disclosed.
* Ensure compliance with open-source and third-party software licenses.
* Support security auditing and risk assessment activities.
* Enhance transparency and trust in our software supply chain.

### 1.2 Scope

This SBOM covers all software components (libraries, frameworks, operating systems, firmware, etc.) that are part of, or linked into, the [Product/System Name] version [Version Number]. It includes both direct dependencies and transitive dependencies (dependencies of dependencies).

### 1.3 Definitions and Acronyms

* **Component:** A distinct software package, library, or module.
* **Direct Dependency:** A component explicitly listed in the product's build or manifest file.
* **Transitive Dependency:** A component that is a dependency of a direct dependency (or further down the chain).
* **CPE (Common Platform Enumeration):** A standardized naming scheme for software applications, operating systems, and hardware devices.
* **PURL (Package URL):** A URL string that identifies and locates a software package.
* **SPDX (Software Package Data Exchange):** An open standard for communicating SBOM information.
* **CycloneDX:** A lightweight SBOM standard designed for use in application security contexts and supply chain component analysis.

## 2. SBOM Generation Details

### 2.1 Generation Tool(s)

[Specify the tool(s) used to generate this SBOM (e.g., Syft, Dependency-Track, Black Duck, custom scripts).]

* **Tool Name:** [e.g., Syft]
* **Version:** [e.g., 0.80.0]
* **Configuration/Command:** [e.g., `syft dir:./ --output spdx-json=sbom.json`]

### 2.2 Source of Analysis

[Describe where the SBOM was generated from (e.g., source code repository, built artifact, container image).]

* **Location:** [e.g., `git@github.com:your-org/your-repo.git#v1.0.0`]
* **Artifact Hash (if applicable):** [e.g., SHA256 hash of the final build artifact]

### 2.3 SBOM Format

[Specify the format of the generated SBOM (e.g., SPDX JSON, CycloneDX JSON, SPDX Tag-Value).]

* **Format:** [e.g., SPDX JSON]

## 3. Software Component Inventory

This section provides a summary of the identified components. For a detailed, machine-readable list, refer to the attached/linked SBOM file.

| Component Name | Version | Supplier/Author | License(s) | CPE / PURL (if available) | Hashes (SHA256) | Direct/Transitive | Vulnerabilities (Known) | Notes |
|----------------|---------|-----------------|------------|---------------------------|-----------------|-------------------|-------------------------|-------|
| `openssl`      | `1.1.1u`| OpenSSL Project | OpenSSL    | `pkg:deb/debian/openssl@1.1.1u` | `abcdef123...`  | Direct            | CVE-2023-XXXX           |       |
| `libjpeg-turbo`| `2.1.0` | libjpeg-turbo   | BSD-3-Clause | `pkg:npm/libjpeg-turbo@2.1.0` | `1234567...`    | Transitive        |                         |       |
| `react`        | `18.2.0`| Meta            | MIT        | `pkg:npm/react@18.2.0`    | `fedcba9...`    | Direct            |                         |       |
| `sqlite`       | `3.39.0`| SQLite          | Public Domain | `pkg:generic/sqlite@3.39.0` | `9876543...`    | Direct            |                         | Used for local caching |
| `firmware-sdk` | `2.5.1` | Internal        | Proprietary |                           | `zyxwvu...`     | Direct            |                         |       |

## 4. License Compliance Summary

[Summarize the licensing posture of the components. Highlight any licenses requiring specific actions (e.g., copyleft licenses).]

* **Total Unique Licenses:** [Number]
* **Common Licenses:** [e.g., MIT, Apache 2.0, BSD-3-Clause]
* **Licenses Requiring Attention:** [e.g., GPLv3 (if applicable), LGPLv2.1]
    * **[License Type]:** [Action Required, e.g., "Ensure source code distribution compliance."]

## 5. Vulnerability Management

### 5.1 Known Vulnerabilities

[Summarize any known vulnerabilities identified in the components listed in this SBOM. Refer to a separate vulnerability report if detailed.]

* **Total Critical Vulnerabilities:** [Number]
* **Total High Vulnerabilities:** [Number]
* **Top 3 Vulnerabilities (CVE ID & Component):**
    1.  [CVE-YYYY-XXXX - Component A vX.Y.Z]
    2.  [CVE-YYYY-YYYY - Component B vA.B.C]
    3.  [CVE-YYYY-ZZZZ - Component C vP.Q.R]

### 5.2 Remediation Strategy (High-Level)

[Describe the general approach to addressing identified vulnerabilities.]

* [e.g., "Prioritize critical and high vulnerabilities for immediate patching/upgrading."]
* [e.g., "Monitor vulnerability databases (e.g., NVD, OSV) for new disclosures."]
* [e.g., "Regularly regenerate SBOMs to detect new components or changes."]

## 6. SBOM Usage and Maintenance

### 6.1 How to Use This SBOM

* **Security Teams:** For vulnerability assessment and supply chain risk management.
* **Legal/Compliance Teams:** For open-source license compliance.
* **Development Teams:** For understanding dependencies and making informed decisions about new component adoption.
* **Operations Teams:** For understanding deployed software components.

### 6.2 Maintenance

This SBOM is a living artifact and should be regenerated and reviewed:
* [e.g., "Upon every major release."]
* [e.g., "After significant dependency changes."]
* [e.g., "Periodically (e.g., monthly/quarterly) for continuous monitoring."]
* [e.g., "When a new critical vulnerability is disclosed in a commonly used component."]

## 7. References

* [Link to the raw SBOM file (e.g., `sbom.json`)]
* [Link to Vulnerability Report (if separate)]
* [Link to Licensing Compliance Report (if separate)]
* [Official SPDX Specification]
* [Official CycloneDX Specification]
```
