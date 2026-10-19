---
title: "Deployment, Tips & Tricks, and Anti-Patterns"
---

# Deployment, Tips & Tricks, and Anti-Patterns

## 1. Physical Deployment and Hardware Topology

In standard enterprise and web applications, software containers run inside virtual machines, cloud instances, or Kubernetes pods. In **connected IoT and embedded systems**, software containers run on specific silicon packages, connected by printed circuit board (`PCB`) traces. They are powered by batteries or energy-harvesting circuits, and subject to real-world electrical constraints.

A **C4 Deployment Diagram** bridges software containers to their physical hardware execution environment.

### A. Physical Architecture Overview

The Smart Environmental Sensor runs its firmware container on an **STM32U575** microcontroller and reads the **BME688** sensor over an I2C bus. It logs offline data to an external **SPI NOR Flash**, and transmits over an integrated 2.4 GHz radio:

```mermaid
flowchart TB
    subgraph Power Supply and Energy Domain
        Battery["Lithium Polymer (LiPo) Battery<br/><i>[3.7V Nominal / 1200 mAh]</i>"]
        LDO["Low-Dropout Regulator (LDO)<br/><i>[Constant 3.3V Always-On Domain]</i>"]
        LoadSwitch["Switched Power Rail<br/><i>[TPS22918 Load Switch - Controlled by MCU]</i>"]
    end

    subgraph SensorBoard["Smart Sensor Hardware Board (4-Layer PCB)"]
        MCU["STM32U575 Microcontroller<br/><i>[QFN-48 Package / ARM Cortex-M33 @ 160 MHz]</i><br/>Runs FreeRTOS Sensor Application"]
        Sensor["Bosch BME688 Sensor<br/><i>[3.0 x 3.0 mm LGA Package]</i><br/>Digital Gas, Temperature, Humidity & Pressure"]
        Flash["Macronix MX25R 8MB NOR Flash<br/><i>[USON-8 Package]</i><br/>NVS Configuration, Certificates & Staged Firmware"]
        Antenna["2.4 GHz Ceramic Chip Antenna<br/><i>[Matched 50-Ohm RF Network]</i><br/>802.11 b/g/n Wi-Fi & BLE 5.2 Transmission"]
    end

    Battery --> LDO
    Battery --> LoadSwitch
    LDO -- "Powers MCU core & RTC (Always-On)" --> MCU
    LDO -- "Powers secure NVS storage" --> Flash
    LoadSwitch -- "Powers sensor during measurement" --> Sensor
    MCU -- "GPIO Rail Enable Pin" --> LoadSwitch

    MCU <== "I2C Bus (SDA, SCL) @ 400 kHz with 4.7k Pull-ups" ==> Sensor
    MCU <== "Quad-SPI Bus (4 Data, CLK, CS) @ 32 MHz" ==> Flash
    MCU <== "50-Ohm Microstrip RF Trace" ==> Antenna
```
[[CAPTION:Figure]] Physical Deployment and Electrical Topology diagram mapping software containers to hardware silicon, power rails, and peripheral buses.

### B. PlantUML C4 Deployment Diagram

The PlantUML deployment model below formalises the physical hardware topology of the device and the cloud infrastructure:

```plantuml
@startuml
!include <C4/C4_Deployment>

Deployment_Node(home, "Residential Smart Home", "Physical Customer Site") {
    Deployment_Node(wall, "Living Room Sensor Enclosure", "Polycarbonate Wall Mount") {
        Deployment_Node(pcb, "Sensor Mainboard PCB", "4-Layer FR-4 Board") {
            Deployment_Node(mcu, "STM32U575 MCU", "ARM Cortex-M33, 786KB SRAM, 2MB Flash") {
                Container(fw, "Sensor Application Firmware", "C / FreeRTOS", "Runs measurement tasks, network stack, and state machines")
            }
            Deployment_Node(sensor_ic, "Bosch BME688", "Integrated MEMS Gas & Climate Sensor") {
                Container(sensor_chip, "Sensor Subsystem", "Silicon IC", "Measures temperature, humidity, pressure, and VOC gases")
            }
            Deployment_Node(flash_ic, "Macronix MX25R 8MB", "External SPI NOR Flash") {
                ContainerDb(flash_db, "Non-Volatile Storage (NVS)", "LittleFS Partition", "Stores credentials, certificates, and staged FOTA binaries")
            }
        }
    }
}

Deployment_Node(aws, "Amazon Web Services (AWS)", "Public Cloud Infrastructure") {
    Deployment_Node(iot_core, "AWS IoT Core", "Managed Cloud Service") {
        Container(broker, "Cloud MQTT Broker", "MQTT over TLS 1.3", "Terminates device sessions and validates client certificates")
    }
    Deployment_Node(eks, "EKS Cluster", "Managed Kubernetes") {
        Container(ingest, "Telemetry Ingestion Worker", "Go Service", "Validates payloads and batch-writes to database")
        Container(api, "GraphQL Gateway", "Node.js / Apollo", "Serves authenticated queries and real-time streams")
    }
    Deployment_Node(db_tier, "Managed Databases", "RDS / Timestream") {
        ContainerDb(tsdb, "Telemetry Database", "TimescaleDB", "Time-series storage for environmental metrics")
    }
}

Rel(fw, sensor_chip, "Reads measurement data", "I2C Bus @ 400 kHz")
Rel(fw, flash_db, "Reads credentials / writes staged FOTA", "Quad-SPI @ 32 MHz")
Rel(fw, broker, "Publishes telemetry / receives delta state", "MQTT over TLS 1.3 / Port 8883")
Rel(broker, ingest, "Routes device messages", "Internal Message Queue")
Rel(ingest, tsdb, "Inserts batch metrics", "SQL / Native TCP")
Rel(api, tsdb, "Queries historical trends", "SQL")
@enduml
```
[[CAPTION:Figure]] PlantUML C4 Deployment diagram showing edge hardware packaging and cloud infrastructure hosting.

## 2. Dynamic Sequences: Modelling Time and Lifecycles

While standard C4 diagrams capture static relationships, connected IoT systems are inherently dynamic. Microcontrollers sleep for 99% of their lifespan to conserve energy, waking periodically to measure sensors, negotiate Wi-Fi associations, publish MQTT telemetry, and immediately return to low-power sleep.

A **C4 Dynamic Diagram** or UML sequence diagram illustrates this runtime sequence:

```mermaid
sequenceDiagram
    autonumber
    participant Timer as Hardware RTC Timer
    participant Core as MCU Application Core
    participant Rail as Sensor Power Switch
    participant Sensor as BME688 Sensor IC
    participant WiFi as Wi-Fi & Network Subsystem
    participant Cloud as Cloud MQTT Broker

    Note over Core: Ultra-Low-Power Deep Sleep (2.1 uA)
    Timer->>Core: RTC Wakeup Alarm Interrupt
    Core->>Rail: Assert GPIO (Enable Sensor Power Rail)
    Core->>Core: Initialize System Clocks & FreeRTOS Scheduler
    Core->>Sensor: Initialize Sensor & Trigger Forced Measurement Mode
    Sensor-->>Core: Data Ready Interrupt (Temperature, Humidity, VOC)
    Core->>Rail: Deassert GPIO (Disable Sensor Power Rail)
    
    Core->>Core: Compensate Readings & Construct JSON Telemetry Payload
    Core->>WiFi: Wake Wi-Fi Subsystem & Connect to AP
    WiFi-->>Core: Association & DHCP Lease Acquired
    Core->>Cloud: Establish mTLS Handshake & Publish MQTT Payload
    Cloud-->>Core: MQTT PUBACK Received
    
    Core->>WiFi: Graceful Disconnect & Power Down Radio
    Core->>Timer: Program Next RTC Wakeup Alarm (+300 Seconds)
    Core->>Core: Enter Deep Sleep Mode
```
[[CAPTION:Figure]] Sequence diagram illustrating the sensor acquisition, network transmission, and power-gating lifecycle.

## 3. Practical Architecture Tips & Tricks for IoT Teams

### A. Establish Clear Layer Boundaries

Avoid mixing physical electronics schematics with logical firmware components:

- **Level 2 (Containers)**: Treat the running firmware binary as a software execution unit. Do not draw GPIO pins or pull-up resistors here.
- **Level 3 (Components)**: Focus on software modules, RTOS tasks, message queues, and HAL drivers.
- **Physical Deployment**: Place the PCB, connectors, bus routing, and power supplies strictly in the Deployment view.

### B. Make Communication Protocols Explicit

An unlabelled arrow in an IoT architecture diagram is a major risk. Every relationship arrow must explicitly state:

1. **The application protocol** (for example, MQTT, CoAP, HTTPS, Matter, Modbus).
1. **The security transport layer** (for example, TLS 1.3, DTLS 1.2, AES-128-CCM, plaintext).
1. **The physical or network carrier** (for example, Wi-Fi 802.11 b/g/n, BLE 5.2, Thread, Ethernet, I2C, SPI, UART).

### C. Automate Diagram Validation in CI/CD

Prevent architecture diagrams from becoming obsolete by integrating validation into your development pipeline:

```yaml
# Example GitHub Actions step
- name: Validate C4 Structurizr Model
  run: |
    docker run --rm -v $(pwd):/workspace structurizr/cli \
      validate -w /workspace/docs/guides/c4-model-guide/workspace.dsl
```

Using tools like `tools/docs-check/check_docs.py` and pre-commit hooks ensures that all referenced diagram files, links, and versions are automatically verified whenever code changes are committed.

## 4. Architectural Anti-Patterns to Avoid

When architecting connected systems, watch for these common pitfalls:

| Anti-Pattern | Description | Impact | Recommended Solution |
| :--- | :--- | :--- | :--- |
| **The "Everything is a Container" Trap** | Modelling every C source file, module, or struct as a container at Level 2. | Diagrams become unreadable and lose architectural abstraction. | Restrict containers strictly to separate binaries, isolated cores, auxiliary chips, or storage media. Source modules belong at Level 3. |
| **The "Passive Wire" Trap** | Drawing connecting arrows without labelling the protocol, baud rate, or security transport. | Leaves firmware and cloud teams guessing at message formats and authentication requirements. | Always label relations with protocol and payload (for example, `[MQTT over mTLS 1.3 / Port 8883]`, `[I2C @ 400 kHz]`). |
| **The "Black Box Cloud" Fallacy** | Drawing the entire cloud platform as a single monolithic circle labelled "Cloud". | Hides critical latency, scaling bottlenecks, ingestion brokers, and database boundaries. | Decompose the cloud into distinct containers: Ingestion Broker, Processing Services, Time-Series Storage, and User APIs. |
| **Conflating Physical and Logical** | Showing PCB copper traces and power supplies on a Level 2 software container diagram. | Confuses software developers who need to understand data flow and execution logic. | Keep Level 2 focused on software execution and storage units. Move electrical and PCB wiring to a dedicated Physical Deployment diagram. |
| **Hardware Omission** | Pretending embedded software executes in an environment with infinite RAM, persistent power, and zero latency. | Leads to designs that fail under low-battery, brownout, or intermittent connectivity conditions. | Explicitly model hardware watchdogs, battery constraints, flash write cycles, and offline storage queues. |
| **Abandonware Diagrams** | Treating diagrams as static slide images drawn once during proposal phases and never updated. | Diagrams become obsolete within weeks, leading to architectural debt and confusion. | Keep diagram source text in version control (using Structurizr DSL or PlantUML). Integrate checks into Git pre-commit hooks. |
[[CAPTION:Table]] Anti-patterns and pitfalls in embedded and connected systems architecture modelling.
