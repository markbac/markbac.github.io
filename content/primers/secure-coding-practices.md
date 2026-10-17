---
title: Secure coding practices
---

# Secure coding practices

Most security vulnerabilities are ordinary bugs in places where an attacker can reach them. Secure coding is a set of habits that prevent whole classes of those bugs, plus the discipline to treat every input from outside as potentially hostile. It applies equally to a web service and to device firmware.

## Principles

- **Validate all input** at the boundary: check type, length, range and format against what is allowed (an allow-list), and reject everything else. This includes data from devices, files, environment variables and other internal services, not just users.
- **Encode output for its context**: HTML-escape for web pages, use parameterised queries for SQL, pass argument lists rather than shell strings to processes. Most injection bugs come from mixing data and code in one string.
- **Least privilege**: every process, service account, token and device credential gets only the access it needs.
- **Defence in depth**: assume any one control can fail, and layer them.
- **Fail securely**: when something goes wrong, deny access and keep the system in a safe state. Error messages to users should not reveal internals; logs should have the detail.
- **Secure defaults**: the product must be secure as shipped, without relying on the user to change settings.
- **Keep it simple**: complex code hides bugs. The less code that handles untrusted data, the better.

## Common weaknesses and their fixes

| Weakness | Prevention |
| --- | --- |
| Injection (SQL, command, LDAP) | Parameterised queries, safe APIs, no string concatenation of inputs into commands |
| Cross-site scripting | Templating that escapes by default, Content Security Policy |
| Buffer overflow (C and C++) | Bounds-checked functions, length checks before every copy, compiler hardening, or a memory-safe language such as [Rust](rust-for-systems.md) |
| Integer overflow | Check arithmetic on sizes and lengths before using the result |
| Hard-coded secrets | A secrets manager or secure element; secret scanning in CI |
| Insecure deserialisation | Never deserialise untrusted data into arbitrary objects; use simple formats and validate them |
| Path traversal | Normalise paths and check they stay inside the allowed directory |
| Race conditions | Atomic operations, proper locking, check-and-use in one step |
| Weak cryptography | Standard libraries and algorithms only; see [cryptography basics](cryptography-basics.md) |

[[CAPTION:Table]] Common weaknesses, as catalogued in the CWE list, and how to prevent them.

## For embedded C

- Follow a coding standard: MISRA C or the SEI CERT C standard.
- Enable compiler warnings and treat them as errors; enable stack protection and, where the hardware supports it, the memory protection unit.
- Never trust lengths in received packets. Check them against both the buffer size and the bytes actually received.
- Clear keys and secrets from memory after use, in a way the compiler cannot optimise away.
- Lock debug ports (JTAG, SWD) on production devices.

## In the development process

- **Threat model** new features: what are the assets, who might attack them, and how? STRIDE is a simple checklist.
- **Review** code with security in mind; see [code review](code-review.md).
- **Automate**: [static analysis](static-code-analysis.md), dependency scanning, secret scanning and fuzzing in the [CI/CD pipeline](cicd-pipelines.md).
- **Manage dependencies**: keep a software bill of materials, update regularly, and remove what you do not use.
- **Learn from incidents**: every vulnerability found is a chance to remove a whole class, not just one instance.

## Where next

- [OWASP Top 10](owasp-top-10.md) lists the most common web risks.
- The [Guidelines](../guidelines/index.md) section sets the secure coding rules used here.
- The [OWASP Secure Coding Practices quick reference](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) and the [CWE Top 25](https://cwe.mitre.org/top25/) are good checklists.
