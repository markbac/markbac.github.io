---
title: Platforms and Operations
---

# Platforms and Operations

This quadrant covers real-time operating systems, embedded build distributions, container runtimes, cloud infrastructure platforms, and messaging protocols.

## Ring: Adopt

### FreeRTOS
- **Status**: **Adopt**
- **Tags**: `rtos`, `embedded`, `real-time`, `microcontroller`
- **Rationale**: The core real-time operating system kernel powering our microcontroller firmware. FreeRTOS provides deterministic preemptive task scheduling, minimal RAM overhead ($< 10\,\mathrm{KB}$), and extensive hardware support across ARM Cortex-M and RISC-V architectures.

### Yocto Project
- **Status**: **Adopt**
- **Tags**: `linux`, `embedded`, `build-system`, `gateways`
- **Rationale**: Standard build automation framework for producing customized, minimal, and fully reproducible embedded Linux board support packages (BSPs) for edge compute gateways.

### Docker
- **Status**: **Adopt**
- **Tags**: `containers`, `devops`, `cloud`, `ci`
- **Rationale**: Standard containerization runtime for cloud microservices, local developer environments, and automated CI build runners. Guarantees environment parity between development and production.

### Google Cloud Platform (GCP)
- **Status**: **Adopt**
- **Tags**: `cloud`, `infrastructure`, `analytics`, `bigquery`
- **Rationale**: Primary cloud platform provider hosting our IoT telemetry ingestion pipelines, BigQuery data analytics warehouse, and Google Kubernetes Engine (GKE) clusters.

### MQTT
- **Status**: **Adopt**
- **Tags**: `iot`, `protocol`, `pubsub`, `messaging`
- **Rationale**: Standard lightweight publish/subscribe protocol for low-bandwidth, high-latency edge-to-cloud device communications. Provides QoS delivery guarantees and keep-alive heartbeats over TLS.

### Serverless (Cloud Functions / Cloud Run)
- **Status**: **Adopt**
- **Tags**: `cloud`, `serverless`, `faas`, `event-driven`
- **Rationale**: Adopted for asynchronous event processing, third-party webhook receivers, and sporadic background tasks that scale instantly from zero to thousands of instances without dedicated server costs.

## Ring: Assess

### CloudEvents
- **Status**: **Assess**
- **Tags**: `standards`, `event-driven`, `cloud`, `cncf`
- **Rationale**: Assessing the CNCF CloudEvents 1.0 specification for standardising event envelopes and metadata across heterogeneous cloud and edge message buses.
