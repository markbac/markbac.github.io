---
title: Component diagrams (level 3)
---

# Component diagrams (level 3)

## 1. Decomposing Containers into Components

A **Component diagram** zooms into an individual container (from Level 2) to reveal its internal modular software architecture. 

In connected systems, components exist both at the physical edge and in the cloud. In this chapter, we explore two complementary Level 3 Component views:
1. **The High-Level Firmware Component Architecture** inside the physical Sensor Microcontroller container.
2. **The Cloud Telemetry Ingestion Worker** inside the cloud microservices layer.

## 2. High-Level Firmware Component Architecture

Within the microcontroller firmware (executing on an RTOS like FreeRTOS or Zephyr), components represent **cohesive functional modules, subsystems, or background tasks** connected by message queues and function interfaces:

```mermaid
flowchart TB
    subgraph Firmware [Container: Sensor Microcontroller High-Level Firmware]
        subgraph Sensing & Application Layer
            SensorMgr["Sensor Acquisition Manager<br/><i>[Component: Periodic RTOS Task]</i><br/>Samples the environmental sensor, averages readings, and compensates for thermal drift."]
            PowerOrch["Power & Sleep Orchestrator<br/><i>[Component: State Controller Task]</i><br/>Coordinates sensor heater duty-cycles, radio sleep states, and battery preservation."]
        end

        subgraph Communications & Cloud Integration Layer
            NetMgr["Wi-Fi & Network Manager<br/><i>[Component: Event-Driven Task]</i><br/>Maintains WPA2/WPA3 associations, performs exponential backoff, and hosts BLE onboarding."]
            MQTTClient["MQTT Telemetry Client<br/><i>[Component: Client Subsystem]</i><br/>Formats JSON/CBOR telemetry frames, handles QoS 1 deliveries, and manages subscriptions."]
            FotaAgent["FOTA Update Agent<br/><i>[Component: Background Task]</i><br/>Streams firmware blocks over HTTPS/MQTT, writes to flash staging slot, and verifies image hashes."]
        end

        subgraph System Services & Hardware Abstraction
            ConfigStore["Local Configuration Store<br/><i>[Component: LittleFS Storage Subsystem]</i><br/>Thread-safe access to Wi-Fi credentials, alert thresholds, and calibration offsets."]
            SensorDriver["BME688 Sensor Driver & HAL<br/><i>[Component: I2C Driver Layer]</i><br/>Configures gas sensor heating profiles and reads raw ADC sample registers."]
        end
    end

    %% External interfaces
    SensorIC[("Environmental Sensor IC")]
    NORFlash[("SPI NOR Flash")]
    CloudBroker[("Cloud MQTT Broker")]

    SensorDriver -- "I2C register transfers" --> SensorIC
    ConfigStore -- "Block read/write" --> NORFlash
    FotaAgent -- "Write downloaded image" --> NORFlash
    MQTTClient -- "TLS Socket Send/Receive" --> CloudBroker

    %% Internal interactions
    SensorMgr -- "Read temperature, humidity, VOCs" --> SensorDriver
    SensorMgr -- "Dispatch metric bundle<br/>[RTOS Message Queue]" --> MQTTClient
    SensorMgr -- "Read calibration data" --> ConfigStore

    PowerOrch -- "Schedule measurement ticks" --> SensorMgr
    PowerOrch -- "Trigger radio sleep mode" --> NetMgr

    NetMgr -- "Network available notification" --> MQTTClient
    MQTTClient -- "Forward FOTA payload notification" --> FotaAgent
    MQTTClient -- "Update remote threshold settings" --> ConfigStore
```
[[CAPTION:Figure]] High-level firmware Component diagram (Level 3) for the Smart Home Sensor microcontroller.

## 3. Matching PlantUML C4 Firmware Component Diagram

Below is the matching **PlantUML C4 Component diagram** detailing the firmware subsystems using `C4_Component.puml`:

```plantuml
@startuml
!include <C4/C4_Component>

LAYOUT_WITH_LEGEND()

title Component Diagram: Sensor Microcontroller Firmware

Container_Boundary(fw, "Sensor Microcontroller Firmware (FreeRTOS)") {
    Component(sens_mgr, "Sensor Acquisition Manager", "C Task", "Coordinates sensor sampling schedule, averages data, and calculates air comfort scores.")
    Component(power, "Power & Sleep Orchestrator", "C State Machine", "Manages ultra-low-power sleep states, timer wakeups, and peripheral power rails.")
    Component(net, "Wi-Fi & Network Manager", "C Task", "Maintains Wi-Fi association, manages backoff reconnects, and handles BLE provisioning.")
    Component(mqtt, "MQTT Telemetry Client", "C Subsystem", "Serialises telemetry to JSON/CBOR, publishes metrics, and processes inbound cloud commands.")
    Component(fota, "FOTA Update Agent", "C Task", "Streams firmware update blocks from cloud, validates cryptographic hashes, and marks boots.")
    Component(cfg, "Local Configuration Store", "LittleFS Manager", "Provides persistent key-value storage for Wi-Fi credentials and threshold configs.")
    Component(drv, "BME688 Driver & I2C HAL", "Driver Layer", "Drives I2C peripheral hardware and controls sensor heating plates.")
}

ContainerDb_Ext(flash, "SPI NOR Flash", "External Memory", "Stores LittleFS partition and staging FOTA slot.")
Container_Ext(sensor_ic, "BME688 Sensor", "Hardware IC", "Physical ambient sensor hardware.")
Container_Ext(broker, "Cloud MQTT Broker", "Cloud Gateway", "Ingests telemetry and issues commands.")

Rel(sens_mgr, drv, "Triggers measurement & reads registers", "C Function API")
Rel(drv, sensor_ic, "Reads gas & climate registers", "I2C Bus @ 400 kHz")
Rel(sens_mgr, mqtt, "Queues telemetry packet", "RTOS Message Queue")
Rel(sens_mgr, cfg, "Fetches calibration curve", "C API")

Rel(power, sens_mgr, "Signals sample intervals", "RTOS Event Flag")
Rel(power, net, "Signals sleep/wake windows", "RTOS Event Flag")

Rel(net, mqtt, "Notifies network connectivity status", "Event Callback")
Rel(mqtt, broker, "Publishes telemetry & receives topics", "TLS Socket")
Rel(mqtt, fota, "Signals new firmware available", "RTOS Queue")
Rel(mqtt, cfg, "Persists updated setpoints", "C API")

Rel(fota, flash, "Writes downloaded image blocks", "SPI Block Driver")
Rel(cfg, flash, "Reads/writes configuration records", "LittleFS API")

@enduml
```
[[CAPTION:Figure]] PlantUML C4 Component diagram for the sensor firmware.

## 4. Cloud Telemetry Ingestion Worker Component Architecture

Zooming into the cloud tier, the **Telemetry Ingestion Worker** container consumes raw MQTT streams, validates payload signatures, applies calibration curves, and batches samples into the time-series store:

```mermaid
flowchart TB
    subgraph WorkerContainer["Container: Telemetry Ingestion Worker (Go Service)"]
        Consumer["MQTT Stream Consumer<br/><i>[Component: Worker Goroutine]</i><br/>Subscribes to broker queue and deserialises protobuf/JSON frames."]
        Validator["Schema & Signature Validator<br/><i>[Component: Go Package]</i><br/>Verifies HMAC-SHA256 device signatures and schema compatibility."]
        Calibrator["Metric Normaliser & Calibrator<br/><i>[Component: Pipeline Stage]</i><br/>Applies sensor altitude offsets and converts raw VOC resistance to IAQ index."]
        BatchWriter["Time-Series Batch Buffer<br/><i>[Component: Ring Buffer]</i><br/>Aggregates measurements and executes bulk COPY inserts into database."]
        ShadowSyncer["Device Shadow Syncer<br/><i>[Component: gRPC Client]</i><br/>Updates device connectivity status, last-seen timestamps, and battery levels."]
    end

    BrokerQueue[("Cloud MQTT Broker / Message Queue")]
    TimescaleDB[("TimescaleDB Telemetry Store")]
    RegistrySvc[("Device Registry Service")]

    BrokerQueue -->|"Delivers raw telemetry stream<br/><b>[Kafka / AMQP Protocol]</b>"| Consumer
    Consumer -->|"Passes unvalidated frame<br/><b>[Go Channel]</b>"| Validator
    Validator -->|"Passes verified payload<br/><b>[Go Channel]</b>"| Calibrator
    Calibrator -->|"Appends calibrated record<br/><b>[In-Memory Buffer]</b>"| BatchWriter
    Calibrator -->|"Dispatches device heartbeat<br/><b>[Asynchronous Channel]</b>"| ShadowSyncer

    BatchWriter -->|"Executes batch SQL insert<br/><b>[SQL / pgxpool Native TCP]</b>"| TimescaleDB
    ShadowSyncer -->|"Updates reported shadow state<br/><b>[gRPC over HTTP/2]</b>"| RegistrySvc
```
[[CAPTION:Figure]] High-level cloud component diagram (Level 3) for the Telemetry Ingestion Worker microservice.

## 5. Matching PlantUML C4 Cloud Component Diagram

Below is the matching **PlantUML C4 Component diagram** for the cloud Telemetry Ingestion Worker service using `C4_Component.puml`:

```plantuml
@startuml
!include <C4/C4_Component>

LAYOUT_WITH_LEGEND()

title Component Diagram: Cloud Telemetry Ingestion Worker

Container_Boundary(worker, "Telemetry Ingestion Worker (Go Microservice)") {
    Component(consumer, "MQTT Stream Consumer", "Go Goroutine Pool", "Subscribes to internal broker queues and unmarshals telemetry payloads.")
    Component(validator, "Schema & Security Validator", "Go Package", "Validates payload structure and authenticates cryptographic device tokens.")
    Component(calibrator, "Metric Normaliser & Calibrator", "Pipeline Module", "Applies altitude corrections and converts raw VOC gas sensor readings.")
    Component(batcher, "Time-Series Batch Writer", "Buffer Pool", "Buffers samples in memory and executes bulk SQL copy operations.")
    Component(syncer, "Device Shadow Syncer", "gRPC Client", "Synchronises device battery, firmware version, and last-seen state.")
}

Container_Ext(broker, "Cloud Ingestion Broker", "EMQX / AWS IoT", "Dispatches device messages to worker queue.")
ContainerDb_Ext(tsdb, "Telemetry Time-Series Store", "TimescaleDB", "Stores time-series metrics.")
Container_Ext(registry, "Device Registry Service", "Node.js Microservice", "Maintains device shadow digital twins.")

Rel(broker, consumer, "Streams incoming telemetry", "AMQP / Kafka Queue")
Rel(consumer, validator, "Passes raw payload", "Go Channel")
Rel(validator, calibrator, "Passes validated data", "Go Channel")
Rel(calibrator, batcher, "Appends processed sample", "In-Memory Ring Buffer")
Rel(calibrator, syncer, "Signals device heartbeat", "Go Channel")

Rel(batcher, tsdb, "Executes multi-row batch insert", "SQL / Native TCP")
Rel(syncer, registry, "Updates reported shadow state", "gRPC over HTTP/2")

@enduml
```
[[CAPTION:Figure]] PlantUML C4 Component diagram for the cloud Telemetry Ingestion Worker microservice.

## 6. Component Concurrency & Execution Mapping

In connected architectures, defining how components map to execution units prevents concurrency bottlenecks and race conditions:

| Component | Execution Context | Priority / Scaling | Concurrency Mechanism |
| :--- | :--- | :--- | :--- |
| **Sensor Acquisition Manager** (Firmware) | Periodic RTOS Task | High | Wakes on timer tick; blocks while awaiting I2C completion. |
| **Power & Sleep Orchestrator** (Firmware) | Event-Driven Task | Highest | Coordinates sleep entry when all task queues are empty. |
| **Wi-Fi & Network Manager** (Firmware) | System Event Task | Normal | Handles network state transitions and IP DHCP renewal. |
| **MQTT Telemetry Client** (Firmware) | Networking Task | Normal | Consumes from telemetry queue; blocks on network sockets. |
| **FOTA Update Agent** (Firmware) | Background Task | Lowest | Executes cooperatively; throttled to avoid starving sensing. |
| **BME688 Driver & HAL** (Firmware) | Synchronous Library | Caller Context | Mutex-protected to prevent concurrent I2C bus collisions. |
| **MQTT Stream Consumer** (Cloud) | Goroutine Pool (50 workers) | Autoscaling Pod | Worker pool reading concurrently from partitioned queue. |
| **Time-Series Batch Writer** (Cloud) | Scheduled Flush Goroutine | High Throughput | Flushes ring buffer on 1-second interval or 500-sample limit. |
| **Device Shadow Syncer** (Cloud) | Non-Blocking Goroutine | Normal | Asynchronous gRPC dispatch to prevent blocking ingestion pipeline. |
[[CAPTION:Table]] Concurrency mapping for firmware tasks and cloud ingestion components.

## 7. Tips & Tricks for Level 3 Diagrams

1. **Avoid Over-Diagramming Procedural Utilities**: Do not create components for generic helper utilities like `crc32.c`, `string_utils.c`, or standard math libraries. Focus on cohesive subsystems that own state, background tasks, or worker pools.
1. **Show Concurrency Interactions**: Always specify whether communication occurs via function calls, RTOS message queues, event flags, Go channels, or gRPC streams.
1. **Model Both Edge and Cloud Separately**: Maintain dedicated Level 3 Component diagrams for each major container. Do not merge firmware task diagrams and cloud microservice component diagrams into a single confusing drawing.
