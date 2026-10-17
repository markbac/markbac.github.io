---
title: Post-quantum cryptography
---

# Post-quantum cryptography

A large enough quantum computer could break the public-key algorithms used today. RSA, elliptic-curve Diffie-Hellman and ECDSA all rest on problems (factoring and discrete logarithms) that Shor's algorithm solves efficiently on such a machine. No quantum computer that can do this exists yet, but data and devices last a long time, so the change to new algorithms has already started. Post-quantum cryptography (PQC) means algorithms that run on ordinary computers and are believed to resist quantum attacks.

## What is affected

| Primitive | Quantum impact | Action |
| --- | --- | --- |
| RSA, ECDH, ECDSA, Ed25519 | Broken | Replace with post-quantum algorithms |
| AES | Weakened (Grover's algorithm roughly halves the effective key length) | Use 256-bit keys for long-term protection |
| SHA-2, SHA-3 | Slightly weakened | Existing output sizes (256 bits or more) remain fine |

[[CAPTION:Table]] How quantum computing affects common primitives.

## The new standards

NIST published the first post-quantum standards in August 2024:

- **ML-KEM** (FIPS 203, based on CRYSTALS-Kyber): key encapsulation, which replaces ECDH-style key exchange.
- **ML-DSA** (FIPS 204, based on CRYSTALS-Dilithium): the general-purpose signature scheme.
- **SLH-DSA** (FIPS 205, based on SPHINCS+): a hash-based signature scheme with conservative security assumptions, but large signatures.

A further signature scheme based on FALCON (FN-DSA) and a backup key encapsulation scheme (HQC) are on the way. For firmware signing, the stateful hash-based schemes **LMS** and **XMSS** (NIST SP 800-208) are already approved, and suit [bootloaders](bootloaders.md) well because verification is simple. The signer must never reuse a state, which needs careful key management.

The new algorithms have much larger keys and signatures than elliptic curves: an ML-DSA signature is a few kilobytes against 64 bytes for Ed25519. That matters for certificates, constrained devices and [narrow radio links](cellular-lpwan.md).

## Harvest now, decrypt later

An attacker can record encrypted traffic today and decrypt it once a quantum computer exists. Any data that must stay secret for ten years or more is already at risk. That is why key exchange is moving first. Hybrid key exchange combines X25519 with ML-KEM, so the connection is safe if either holds. It is already the default in major browsers and in recent OpenSSH and TLS libraries.

## Preparing

- **Inventory**: find where public-key cryptography is used: TLS, VPNs, code signing, device identity, stored data.
- **Crypto agility**: make algorithms configurable and updatable rather than fixed in code or hardware. A device that cannot change its signature algorithm through an update may have to be replaced.
- **Prioritise**: long-lived secrets and long-lived devices first. A product designed today may still be in service when quantum attacks become practical.
- **Follow guidance**: the UK National Cyber Security Centre has set out a timeline with migration complete by 2035, and similar plans exist in the US and EU.

## Where next

- [Cryptography basics](cryptography-basics.md) explains the primitives being replaced.
- The [Standards](../standards/index.md) section will record the algorithms approved here.
- NIST's [post-quantum cryptography project](https://csrc.nist.gov/projects/post-quantum-cryptography) has the standards and the status of the remaining candidates.
