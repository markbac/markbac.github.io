---
title: OWASP Top 10
---

# OWASP Top 10

The OWASP Top 10 is a list of the most critical security risks to web applications, published by the Open Worldwide Application Security Project (OWASP), a non-profit community. It is based on data from real application testing plus a survey of practitioners, and it is updated every few years. It is an awareness document, not a complete standard: an application that avoids all ten can still be insecure. For a fuller checklist, use the OWASP Application Security Verification Standard (ASVS).

## The 2021 list

| Rank | Risk | In short | Main defences |
| --- | --- | --- | --- |
| A01 | Broken access control | Users can act outside their permissions, such as reading another user's data by changing an ID | Deny by default; check authorisation on the server for every request; test it |
| A02 | Cryptographic failures | Sensitive data exposed through missing or weak encryption | TLS everywhere; strong algorithms; encrypt sensitive data at rest; proper key management |
| A03 | Injection | Untrusted data interpreted as code: SQL, command, cross-site scripting | Parameterised queries; output encoding; input validation |
| A04 | Insecure design | Flaws in the design itself, which perfect code cannot fix | Threat modelling; secure design patterns; abuse cases |
| A05 | Security misconfiguration | Default accounts, verbose errors, open cloud storage, unnecessary features | Hardened, automated configuration; minimal installs; regular review |
| A06 | Vulnerable and outdated components | Libraries and frameworks with known vulnerabilities | Inventory (SBOM); dependency scanning; prompt patching |
| A07 | Identification and authentication failures | Weak passwords, credential stuffing, poor session handling | Multi-factor authentication; rate limiting; secure session management |
| A08 | Software and data integrity failures | Unsigned updates, compromised build pipelines, unsafe deserialisation | Signed artefacts; protected CI/CD; verified dependencies |
| A09 | Security logging and monitoring failures | Attacks go unnoticed | Log security events; alert on them; practise incident response |
| A10 | Server-side request forgery (SSRF) | The server is tricked into fetching a URL chosen by the attacker, often reaching internal systems | Allow-list destinations; block internal addresses; separate networks |

[[CAPTION:Table]] The OWASP Top 10, 2021 edition.

## The 2025 edition

OWASP released a new edition in late 2025. Broken access control stays first. Misconfiguration rises to second, reflecting how much behaviour now lives in configuration. Vulnerable components broaden into software supply chain failures, covering build systems and distribution as well as dependencies. SSRF is folded into access control, and a new category covers the mishandling of exceptional conditions: errors that fail open or leak information. The ideas above still apply; check [owasp.org/Top10](https://owasp.org/Top10/) for the current text.

## Other OWASP lists

- **API Security Top 10**: risks specific to APIs, led by broken object-level authorisation, the API form of A01.
- **Mobile Top 10** and **IoT Top 10**: the same idea for mobile apps and connected devices. The IoT list (2018) opens with weak or hard-coded passwords, which [ETSI EN 303 645](etsi-en-303-645.md) also tackles first.
- **Top 10 for LLM Applications**: risks such as prompt injection in systems built on large language models.

## Using it

- Use it to train developers and to structure security reviews and tests.
- Map each category to concrete controls in your own standards and to automated checks in the [CI/CD pipeline](cicd-pipelines.md).
- Do not treat it as the whole job. Threat modelling, [secure coding practices](secure-coding-practices.md) and testing are still needed.

## Where next

- [Secure coding practices](secure-coding-practices.md) covers the habits that prevent most of these risks.
- [OAuth 2.0 and OpenID Connect](oauth-and-oidc.md) addresses much of A07.
- The [Guidelines](../guidelines/index.md) section sets the security rules used here.
