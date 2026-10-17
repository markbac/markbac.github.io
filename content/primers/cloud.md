---
title: Cloud primers
---

# Cloud primers

Cloud computing means renting computing, storage and managed services from a provider, paying for what you use, and creating or removing resources through an API rather than buying hardware. The trade is less control and some lock-in in exchange for speed and not having to run the infrastructure yourself.

## Service models

| Model | You manage | The provider manages | Examples |
| --- | --- | --- | --- |
| IaaS (Infrastructure as a Service) | Operating system, runtime, application, data | Hardware, network, virtualisation | Virtual machines, block storage |
| PaaS (Platform as a Service) | Application and data | Everything underneath | Managed databases, app platforms, Kubernetes services |
| FaaS (Functions as a Service) | Functions and data | Everything else, including scaling | AWS Lambda, Cloud Run functions, Azure Functions |
| SaaS (Software as a Service) | Configuration and your data | The whole application | Email, CRM, source hosting |

[[CAPTION:Table]] Cloud service models, from most to least control.

The further down the table, the less you run yourself and the less you can change. Most systems mix several models.

## The primers

- [CI/CD pipelines](cicd-pipelines.md): building, testing and deploying automatically.
- [Infrastructure as code](infrastructure-as-code.md): describing infrastructure in version-controlled files.
- [Serverless computing](serverless-computing.md): functions and managed services that scale to zero.
- [Event streaming with Kafka](kafka-event-streaming.md): durable, replayable event logs.
- [IoT on Google Cloud](iot-on-google-cloud.md): building a device platform from general cloud services.

The [Handbook](../handbook/index.md) covers cloud architecture decisions, and the [Tech Radar](../radar/index.md) shows which cloud tools are recommended.
