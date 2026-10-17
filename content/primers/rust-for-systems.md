---
title: Rust for systems programming
---

# Rust for systems programming

Rust is a systems programming language that gives the performance and low-level control of C and C++ while preventing most memory safety bugs at compile time. It has no garbage collector, so it suits operating systems, embedded firmware, network services and anything where predictable performance matters. Microsoft and Google have both reported that around 70 % of their serious security bugs are memory safety issues. That is why governments and large companies now encourage memory-safe languages for new code.

## How it achieves safety

- **Ownership**: every value has exactly one owner, and the value is freed when its owner goes out of scope. No manual `free`, no double free, no leaks from forgetting.
- **Borrowing**: code can borrow a value either as any number of shared, read-only references or as one mutable reference, never both at once. The compiler's borrow checker enforces this, which rules out use-after-free, dangling pointers and data races.
- **No null**: a value that might be missing is an `Option<T>`, which the compiler forces you to handle.
- **Errors as values**: functions that can fail return `Result<T, E>`, and the `?` operator passes errors up neatly. Errors cannot be ignored by accident.
- **`unsafe`**: low-level operations the compiler cannot check (raw pointers, hardware registers, calling C) are allowed inside `unsafe` blocks. This keeps the risky code small, visible and reviewable.

```rust
fn parse_reading(frame: &[u8]) -> Result<u16, &'static str> {
    let bytes = frame.get(2..4).ok_or("frame too short")?;
    Ok(u16::from_be_bytes([bytes[0], bytes[1]]))
}
```

[[CAPTION:Figure]] Bounds-checked parsing: a short frame is an error, not a buffer overrun.

## The ecosystem

- **Cargo** builds, tests, documents and manages dependencies (crates) out of the box.
- **Clippy** (linter) and **rustfmt** (formatter) are standard.
- **Async** networking with Tokio; web services with Axum.
- **Interoperability**: Rust can call C and be called from C, so it can be introduced one module at a time into an existing codebase.

## On microcontrollers

Embedded Rust is mature on Arm Cortex-M, RISC-V and the ESP32 family:

- `no_std` code runs without an operating system or heap.
- **Peripheral access crates** are generated from vendor register descriptions, and **HAL crates** implement the shared `embedded-hal` traits, so drivers work across chips.
- **Embassy** provides async tasks on bare metal; **RTIC** provides interrupt-driven concurrency checked at compile time.
- **probe-rs** handles flashing and debugging.
- **Ferrocene** is a Rust toolchain qualified for safety standards such as ISO 26262 and IEC 61508.

## Trade-offs

- The learning curve is real, especially the borrow checker; expect weeks before a C programmer feels productive.
- Compile times are longer than C.
- Vendor support (SDKs, examples, certified stacks) is still mostly C. Check that the chips and protocol stacks you need are covered.
- Hiring and team experience may be limited.

A sensible way to start is a new, self-contained component (a parser, a protocol handler, a command-line tool) rather than rewriting working C.

## Where next

- [Secure coding practices](secure-coding-practices.md) explains the bugs Rust prevents.
- The [Tech Radar](../radar/index.md) records where Rust is recommended.
- *The Rust Programming Language* ([doc.rust-lang.org/book](https://doc.rust-lang.org/book/)) and *The Embedded Rust Book* ([docs.rust-embedded.org/book](https://docs.rust-embedded.org/book/)) are free.
