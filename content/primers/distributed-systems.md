---
title: Distributed systems primers
---

# Distributed systems primers

A distributed system is one where the parts run on different machines and talk over a network. Almost every modern system is one, including any IoT platform. The network can be slow, lose messages, deliver them twice or split in two, and clocks on different machines disagree. These primers cover the ideas that follow from that.

- [CAP and PACELC](cap-and-pacelc.md): what you give up when the network fails, and when it does not.
- [Consistency models](consistency-models.md): strong, eventual and causal consistency, and CRDTs.
- [Idempotency](idempotency.md): making it safe to do the same thing twice.
- [The saga pattern](saga-pattern.md): transactions that span several services.

The [Handbook](../handbook/index.md) covers how to apply these in a design, and [event-driven architecture](event-driven-architecture.md) is where they matter most.
