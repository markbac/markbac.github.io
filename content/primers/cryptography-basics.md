---
title: Cryptography basics
---

# Cryptography basics

Cryptography provides a small set of building blocks: keeping data secret (confidentiality), detecting changes (integrity), and proving who sent it (authenticity). Almost every security protocol is a combination of the primitives below. The first rule is never to invent your own: use well-reviewed algorithms through a well-maintained library.

## Hash functions

A cryptographic hash turns any input into a fixed-size digest. It is one-way (you cannot recover the input), and it is infeasible to find two inputs with the same digest.

- **Use**: SHA-256 and SHA-384 (the SHA-2 family), SHA-3, BLAKE2 or BLAKE3.
- **Avoid**: MD5 and SHA-1, both broken for collision resistance.
- **Uses**: file and firmware integrity checks, digital signatures (which sign a hash), content addressing as in Git.
- **Not for passwords on their own**: a plain hash is far too fast to resist guessing. See key derivation below.

## Symmetric encryption

One shared key both encrypts and decrypts. It is fast and suits bulk data.

- **AES** (Advanced Encryption Standard) with 128- or 256-bit keys is the standard, and most microcontrollers and processors have hardware acceleration for it. **ChaCha20** is a fast alternative in software.
- Always use an authenticated mode, which encrypts and protects integrity together: **AES-GCM**, **AES-CCM** (common in constrained devices) or **ChaCha20-Poly1305**. Never use ECB mode, and never reuse a nonce with the same key in GCM: doing so breaks both secrecy and integrity.
- The hard part is sharing and protecting the key.

## Message authentication codes

A MAC (message authentication code) is a short tag computed from a message and a secret key. Anyone with the key can check that the message has not changed and came from another key holder. **HMAC-SHA256** is the common choice; authenticated encryption modes include a MAC already. Compare tags in constant time to avoid leaking information through timing.

## Public-key cryptography

Each party has a key pair: a private key kept secret and a public key shared freely.

- **Digital signatures**: sign with the private key; anyone can verify with the public key. Used for firmware signing, certificates and software packages. Algorithms: **ECDSA** with P-256, **Ed25519**, and **RSA** (3072 bits or more for new keys).
- **Key exchange**: two parties agree a shared secret over an open channel. **ECDH**, especially **X25519**, is the modern choice. The shared secret then keys a symmetric cipher.
- Public-key operations are much slower than symmetric ones, so protocols such as [TLS](tls-and-dtls.md) use them only to authenticate and agree keys.
- The hard part is trusting that a public key really belongs to who it claims; that is the job of [PKI](pki-and-certificates.md).

## Key derivation

A key derivation function (KDF) turns one secret into the keys a protocol needs.

- **HKDF** derives several keys from a shared secret, as in TLS 1.3.
- **Password hashing** needs a deliberately slow, memory-hard function: **Argon2id** first, otherwise **scrypt**, **bcrypt** or **PBKDF2** with a high iteration count. Always use a unique salt per password.

## Random numbers

Keys, nonces and salts must come from a cryptographically secure random number generator. On a computer, use the operating system's (`/dev/urandom`, `getrandom()`, Python's `secrets`). On a microcontroller, use the hardware true random number generator (TRNG) feeding a DRBG (deterministic random bit generator). `rand()` is never acceptable. Weak randomness at first boot, before enough entropy has been gathered, is a known source of duplicate keys in device fleets.

## Choosing for constrained devices

Small devices often use AES-CCM, ECDSA or Ed25519, X25519 and SHA-256. Hardware accelerators support them, as do libraries such as Mbed TLS, wolfSSL and the PSA Crypto API. NIST's Ascon (lightweight cryptography standard, 2025) targets the smallest devices.

## Where next

- [PKI and certificates](pki-and-certificates.md) and [TLS and DTLS](tls-and-dtls.md) show the primitives in use.
- [Post-quantum cryptography](post-quantum-cryptography.md) covers what will replace today's public-key algorithms.
- The [Standards](../standards/index.md) section lists the algorithms approved here.
