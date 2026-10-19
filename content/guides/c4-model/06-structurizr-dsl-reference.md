---
title: Structurizr DSL Reference for Connected Systems
---

# Structurizr DSL Reference for Connected Systems

## 1. Why Structurizr DSL for IoT Architectures?

When designing connected systems that span physical edge devices, microcontrollers, radio gateways, and cloud microservices, authoring standalone visual diagrams quickly becomes unmaintainable. An update to an MQTT topic format, an ingestion endpoint, or a device hardware component often requires manually redrawing half a dozen diagrams across multiple levels.

The **Structurizr DSL** (Domain Specific Language) solves this problem by enforcing a **single source of truth**:

1. **Model Once, View Anywhere**: You define people, software systems, containers, components, deployment nodes, and their relationships once in an architectural model.
1. **Multiple Perspectives**: You declare views (Context, Container, Component, Deployment, Dynamic) that automatically project subsets of that same unified model.
1. **Format Agnostic**: From one `workspace.dsl` file, you can render interactive web views via **Structurizr Lite**, generate **PlantUML C4 diagrams**, or export **Mermaid** graphics for documentation.

```mermaid
graph LR
    DSL["workspace.dsl<br/><b>Single Architectural Model</b><br/>(Sensors, MCU, Cloud, DBs)"]
    Lite["Structurizr Lite<br/><b>Interactive Web UI</b>"]
    Puml["PlantUML Export<br/><b>C4 Container & Component Diagrams</b>"]
    Merm["Mermaid Export<br/><b>Git Markdown Rendering</b>"]
    PDF["DOCX & PDF Guides<br/><b>Createdocs Automation</b>"]

    DSL --> Lite
    DSL --> Puml
    DSL --> Merm
    Puml --> PDF
```
[[CAPTION:Figure]] The Structurizr DSL architecture-as-code workflow for connected IoT systems.

## 2. Complete Smart Home IoT `workspace.dsl`

Below is a complete `workspace.dsl` file that models the whole Smart Home Environmental Monitoring system. It runs from the physical sensor and MCU firmware components to the cloud microservices and the mobile app.

```structurizr
workspace "Smart Home Environmental Monitoring System" "End-to-end architecture model from edge sensor firmware to cloud microservices and mobile user experience." {

    model {
        # =====================================================================
        # People / User Personas
        # =====================================================================
        homeowner = person "Homeowner" "Monitors home air quality and receives comfort alerts." "Person"
        installer = person "Field Technician" "Commissions, provisions, and diagnostics sensors during installation." "Person"

        # =====================================================================
        # External Systems
        # =====================================================================
        localHub = softwareSystem "Local Smart Hub" "Local home automation gateway (for example, Home Assistant, Apple Home, Matter hub)." "External"
        weatherService = softwareSystem "National Weather API" "Provides external outdoor baseline temperature and pollen data." "External"
        pushService = softwareSystem "Push Notification Service" "Apple APNs and Google FCM delivery network." "External"

        # =====================================================================
        # Connected Edge Product: Smart Environmental Sensor
        # =====================================================================
        sensorDevice = softwareSystem "Smart Environmental Sensor" "Battery-powered physical IoT edge device measuring ambient environment." "Device" {
            
            sensorHardware = container "BME688 Sensor Subsystem" "Digital MEMS sensor measuring temperature, humidity, barometric pressure, and VOC gas." "Silicon / MEMS" "Sensor"
            
            configStorage = container "Non-Volatile Storage (NVS)" "Encrypted SPI NOR flash memory storing Wi-Fi credentials, certificates, and offline logs." "Macronix SPI Flash" "Database"
            
            sensorFirmware = container "Sensor Application Firmware" "FreeRTOS-based embedded firmware managing data acquisition, power cycling, and networking." "C / FreeRTOS on STM32U575" "Firmware" {
                
                sensorAcq = component "Sensor Acquisition Manager" "Schedules periodic sensor readings, applies calibration offsets, and filters noise." "C Module / RTOS Task" "FirmwareComponent"
                powerOrch = component "Power & Sleep Orchestrator" "Coordinates transitions between active measurement, network transmission, and deep sleep." "C Module / State Machine" "FirmwareComponent"
                wifiMgr = component "Wi-Fi & Network Manager" "Manages 802.11 b/g/n association, station state, and network recovery." "C Module / Network Task" "FirmwareComponent"
                mqttClient = component "MQTT Ingestion Client" "Manages secure mTLS connections and serialises JSON telemetry payloads." "C Module / coreMQTT" "FirmwareComponent"
                fotaAgent = component "FOTA Update Agent" "Downloads signed firmware chunks, validates SHA-256 signatures, and writes to staging flash." "C Module / Bootloader Interface" "FirmwareComponent"
                configStore = component "Configuration Store" "Provides thread-safe access to provisioned settings and network credentials." "C Module / LittleFS HAL" "FirmwareComponent"
                sensorHal = component "Sensor HAL & Driver" "I2C peripheral driver communicating directly with the BME688 hardware registers." "C Module / I2C Bus Driver" "FirmwareComponent"
            }
        }

        # =====================================================================
        # Cloud Platform
        # =====================================================================
        cloudPlatform = softwareSystem "Environmental Cloud Platform" "Scalable cloud platform for device ingestion, shadow management, and telemetry analytics." "Cloud" {
            
            mqttBroker = container "Cloud Ingestion Broker" "High-throughput MQTT broker terminating device TLS connections and routing messages." "EMQX / AWS IoT Core" "CloudService"
            
            ingestionWorker = container "Telemetry Ingestion Worker" "Consumes raw telemetry messages, validates schema, applies calibrations, and writes time-series records." "Go Microservice" "CloudService" {
                streamConsumer = component "MQTT Stream Consumer" "Consumes raw telemetry events from message broker queue." "Go Goroutine Pool" "CloudComponent"
                payloadValidator = component "Schema & Security Validator" "Validates payload format and authenticates device HMAC signatures." "Go Package" "CloudComponent"
                metricCalibrator = component "Metric Normaliser & Calibrator" "Applies sensor altitude offsets and converts VOC resistance to IAQ index." "Pipeline Module" "CloudComponent"
                batchWriter = component "Time-Series Batch Writer" "Buffers samples and executes bulk SQL copy operations into database." "Buffer Pool" "CloudComponent"
                shadowSyncer = component "Device Shadow Syncer" "Synchronises reported battery, firmware version, and last-seen state." "gRPC Client" "CloudComponent"
            }
            
            deviceRegistry = container "Device Shadow & Registry Service" "Maintains device digital twins, provisioning credentials, desired state, and FOTA campaigns." "Node.js / TypeScript" "CloudService"
            
            telemetryDb = container "Telemetry Time-Series Store" "Optimised time-series database storing sensor metrics and historical aggregates." "TimescaleDB / Timeseries" "Database"
            
            metadataDb = container "Relational Metadata Database" "Stores user accounts, home floor plans, device ownership, and alerting rules." "PostgreSQL 16" "Database"
            
            graphqlApi = container "GraphQL Application Gateway" "Serves unified queries and real-time WebSockets subscriptions to clients." "Node.js / Apollo Server" "CloudService"
        }

        # =====================================================================
        # User Client Applications
        # =====================================================================
        mobileApp = softwareSystem "Smart Life Mobile App" "Cross-platform mobile application providing real-time telemetry, historical charts, and push alerts." "MobileApp"

        # =====================================================================
        # System-Level Relationships (Level 1)
        # =====================================================================
        homeowner -> mobileApp "Views live metrics, trends, and alerts" "HTTPS"
        homeowner -> sensorDevice "Views RGB status LED and presses commissioning button" "Physical / Visual"
        installer -> sensorDevice "Provisions Wi-Fi credentials and inspects diagnostics" "BLE 5.2"
        
        sensorDevice -> cloudPlatform "Publishes periodic telemetry and checks for updates" "MQTT over TLS 1.3 / Port 8883"
        sensorDevice -> localHub "Broadcasts local metrics and status" "Matter over Wi-Fi / CoAP"
        cloudPlatform -> pushService "Dispatches push alert payloads" "HTTPS / REST"
        pushService -> mobileApp "Delivers push notifications" "Apple APNs / Google FCM"
        cloudPlatform -> weatherService "Fetches outdoor baseline temperature and air quality" "HTTPS / JSON"
        mobileApp -> cloudPlatform "Queries device data, historical metrics, and updates configuration" "GraphQL / HTTPS / WSS"

        # =====================================================================
        # Container-Level Relationships (Level 2)
        # =====================================================================
        sensorFirmware -> sensorHardware "Triggers measurement cycles and reads raw register values" "I2C Bus @ 400 kHz"
        sensorFirmware -> configStorage "Reads/writes credentials, crash dumps, and staged firmware" "SPI Bus @ 32 MHz"
        sensorFirmware -> mqttBroker "Publishes telemetry and subscribes to delta updates" "MQTT over TLS 1.3 (mTLS)"
        sensorFirmware -> localHub "Emits local telemetry" "Matter / UDP"

        mqttBroker -> ingestionWorker "Routes incoming telemetry messages" "Internal Queue / Kafka"
        ingestionWorker -> telemetryDb "Writes batch time-series sensor samples" "SQL / Native TCP"
        ingestionWorker -> deviceRegistry "Updates last-seen timestamp and battery state" "gRPC"

        deviceRegistry -> metadataDb "Reads and writes device profiles and ownership records" "SQL"
        graphqlApi -> telemetryDb "Queries metric history and rollups" "SQL"
        graphqlApi -> deviceRegistry "Reads device shadow and dispatches desired state updates" "gRPC"
        graphqlApi -> metadataDb "Authenticates users and reads home layouts" "SQL"

        mobileApp -> graphqlApi "Fetches dashboard metrics and sends remote commands" "HTTPS / WSS"

        # =====================================================================
        # Component-Level Relationships inside Firmware (Level 3)
        # =====================================================================
        powerOrch -> sensorAcq "Wakes and triggers scheduled reading" "Direct Call / Event Signal"
        sensorAcq -> sensorHal "Reads compensated sensor values" "C API Call"
        sensorHal -> sensorHardware "Reads data registers" "I2C HAL Driver"
        
        sensorAcq -> mqttClient "Enqueues telemetry payload" "FreeRTOS Queue"
        powerOrch -> wifiMgr "Commands network connect/disconnect for power conservation" "RTOS Event Group"
        wifiMgr -> mqttClient "Notifies IP address acquisition and link state" "Event Notification"
        
        mqttClient -> configStore "Retrieves client TLS certificates and broker endpoint" "C API Call"
        configStore -> configStorage "Reads stored keys and nonces" "LittleFS File IO"

        fotaAgent -> mqttClient "Subscribes to update jobs and downloads signed chunks" "MQTT Callback"
        fotaAgent -> configStorage "Writes firmware image to staging partition" "Flash Driver Call"
        fotaAgent -> powerOrch "Requests system reboot into bootloader" "System Reset"

        # =====================================================================
        # Component-Level Relationships inside Cloud Ingestion Worker (Level 3)
        # =====================================================================
        mqttBroker -> streamConsumer "Routes raw messages" "AMQP / Kafka Queue"
        streamConsumer -> payloadValidator "Passes raw payload" "Go Channel"
        payloadValidator -> metricCalibrator "Passes validated data" "Go Channel"
        metricCalibrator -> batchWriter "Appends processed sample" "In-Memory Ring Buffer"
        metricCalibrator -> shadowSyncer "Signals device heartbeat" "Go Channel"
        batchWriter -> telemetryDb "Executes batch insert" "SQL / Native TCP"
        shadowSyncer -> deviceRegistry "Updates reported shadow state" "gRPC over HTTP/2"

        # =====================================================================
        # Deployment Environment: Physical Smart Home Deployment
        # =====================================================================
        deploymentEnvironment "Production" {
            deploymentNode "Residential Smart Home" "Physical residence of the homeowner." "Physical Boundary" {
                
                deploymentNode "Living Room Wall Mount" "Physical wall installation point." "Hardware Enclosure" {
                    deploymentNode "PCB Assembly" "Custom 4-layer printed circuit board." "Hardware" {
                        deploymentNode "STM32U575 MCU" "ARM Cortex-M33 running at 160MHz with TrustZone." "Microcontroller" {
                            containerInstance sensorFirmware
                        }
                        deploymentNode "Bosch BME688" "Integrated environmental sensor in 3.0 x 3.0 mm package." "Hardware IC" {
                            containerInstance sensorHardware
                        }
                        deploymentNode "Macronix MX25R 8MB" "External NOR flash memory chip." "Hardware IC" {
                            containerInstance configStorage
                        }
                    }
                }

                deploymentNode "Home Wi-Fi Router" "Standard dual-band residential wireless gateway." "Network Device" {
                    deploymentNode "Local Home Server" "Raspberry Pi 5 home server." "Hardware" {
                        softwareSystemInstance localHub
                    }
                }

                deploymentNode "User Smartphone" "Apple iPhone 15 running iOS 18." "Mobile Device" {
                    softwareSystemInstance mobileApp
                }
            }

            deploymentNode "AWS Cloud Region (eu-west-1)" "Amazon Web Services Ireland data centre." "Cloud Infrastructure" {
                deploymentNode "AWS IoT Core" "Managed cloud MQTT message broker and TLS gateway." "AWS Service" {
                    containerInstance mqttBroker
                }
                deploymentNode "Amazon Elastic Kubernetes Service (EKS)" "Managed container orchestration cluster." "Kubernetes" {
                    deploymentNode "Telemetry Ingestion Pods" "Auto-scaling worker pods." "Container Runtime" {
                        containerInstance ingestionWorker
                    }
                    deploymentNode "Device Registry Pods" "Stateful management pods." "Container Runtime" {
                        containerInstance deviceRegistry
                    }
                    deploymentNode "GraphQL API Pods" "Public gateway service pods." "Container Runtime" {
                        containerInstance graphqlApi
                    }
                }
                deploymentNode "Managed Database Tier" "High-availability managed data tier." "Cloud Database" {
                    deploymentNode "Amazon RDS PostgreSQL" "Multi-AZ relational database." "Database Server" {
                        containerInstance metadataDb
                    }
                    deploymentNode "Amazon Timestream / TimescaleDB" "Scalable time-series storage engine." "Database Server" {
                        containerInstance telemetryDb
                    }
                }
            }
        }
    }

    # =========================================================================
    # Views Definition
    # =========================================================================
    views {
        systemContext sensorDevice "SystemContext_Overview" "Overall system context showing device, users, cloud platform, and third-party integrations." {
            include *
            autoLayout lr
        }

        container sensorDevice "Container_EdgeDevice" "Internal containers of the Smart Environmental Sensor edge device." {
            include *
            autoLayout tb
        }

        container cloudPlatform "Container_CloudPlatform" "Internal microservices and database containers of the Cloud Platform." {
            include *
            autoLayout tb
        }

        component sensorFirmware "Component_FirmwareArchitecture" "Component-level architecture of the FreeRTOS embedded application firmware." {
            include *
            autoLayout tb
        }

        component ingestionWorker "Component_CloudIngestionWorker" "Component-level architecture of the Go Telemetry Ingestion Worker." {
            include *
            autoLayout tb
        }

        deployment sensorDevice "Production" "Deployment_ProductionTopology" "Physical hardware and cloud infrastructure deployment mapping." {
            include *
            autoLayout tb
        }

        # =====================================================================
        # Visual Styling and Tag Configurations
        # =====================================================================
        styles {
            element "Person" {
                shape Person
                background #08427b
                color #ffffff
            }
            element "Software System" {
                background #1168bd
                color #ffffff
            }
            element "Device" {
                shape RoundedBox
                background #2A6F97
                color #ffffff
            }
            element "Cloud" {
                shape RoundedBox
                background #014F86
                color #ffffff
            }
            element "External" {
                background #999999
                color #ffffff
            }
            element "MobileApp" {
                shape MobileDevicePortrait
                background #0077B6
                color #ffffff
            }
            element "Container" {
                background #438dd5
                color #ffffff
            }
            element "Firmware" {
                shape RoundedBox
                background #1E88E5
                color #ffffff
            }
            element "Sensor" {
                shape Hexagon
                background #00897B
                color #ffffff
            }
            element "Database" {
                shape Cylinder
                background #2E7D32
                color #ffffff
            }
            element "CloudService" {
                shape RoundedBox
                background #1565C0
                color #ffffff
            }
            element "FirmwareComponent" {
                shape Component
                background #5C6BC0
                color #ffffff
            }
            element "CloudComponent" {
                shape Component
                background #0288D1
                color #ffffff
            }
            relationship "Relationship" {
                thickness 2
                dashed false
                color #707070
                fontSize 24
            }
        }
    }
}
```
[[CAPTION:Figure]] Complete Structurizr DSL specification (`workspace.dsl`) for the Smart Home Environmental Monitoring system.

## 3. Matching PlantUML C4 Diagrams for DSL Views

When exporting or pairing the Structurizr model with standard PlantUML, each view declared in `workspace.dsl` generates a corresponding PlantUML C4 diagram. Below are the complete matching PlantUML scripts for all six declared views:

### A. View 1: System Context Overview (`SystemContext_Overview.puml`)

```plantuml
@startuml
!include <C4/C4_Context>

LAYOUT_WITH_LEGEND()

title System Context Overview - Smart Environmental Sensor System

Person(homeowner, "Homeowner", "Monitors home air quality and receives comfort alerts.")
Person(installer, "Field Technician", "Commissions, provisions, and diagnostics sensors during installation.")

System(sensorDevice, "Smart Environmental Sensor", "Battery-powered physical IoT edge device measuring ambient environment.")
System(cloudPlatform, "Environmental Cloud Platform", "Scalable cloud platform for device ingestion, shadow management, and telemetry analytics.")
System(mobileApp, "Smart Life Mobile App", "Cross-platform mobile application providing real-time telemetry, historical charts, and push alerts.")

System_Ext(localHub, "Local Smart Hub", "Local home automation gateway (for example, Home Assistant, Matter hub).")
System_Ext(weatherService, "National Weather API", "Provides external outdoor baseline temperature and pollen data.")
System_Ext(pushService, "Push Notification Service", "Apple APNs and Google FCM delivery network.")

Rel(homeowner, mobileApp, "Views live metrics, trends, and alerts", "HTTPS")
Rel(homeowner, sensorDevice, "Views RGB status LED and presses button", "Physical / Visual")
Rel(installer, sensorDevice, "Provisions Wi-Fi credentials and inspects diagnostics", "BLE 5.2")

Rel(sensorDevice, cloudPlatform, "Publishes periodic telemetry and checks for updates", "MQTT over TLS 1.3 / Port 8883")
Rel(sensorDevice, localHub, "Broadcasts local metrics and status", "Matter over Wi-Fi / CoAP")
Rel(cloudPlatform, pushService, "Dispatches push alert payloads", "HTTPS / REST")
Rel(pushService, mobileApp, "Delivers push notifications", "Apple APNs / Google FCM")
Rel(cloudPlatform, weatherService, "Fetches outdoor baseline temperature and air quality", "HTTPS / JSON")
Rel(mobileApp, cloudPlatform, "Queries device data, historical metrics, and updates configuration", "GraphQL / HTTPS / WSS")

@enduml
```
[[CAPTION:Figure]] Matching PlantUML C4 script for View 1: System Context Overview.

### B. View 2: Edge Device Container Diagram (`Container_EdgeDevice.puml`)

```plantuml
@startuml
!include <C4/C4_Container>

LAYOUT_WITH_LEGEND()

title Container Diagram - Smart Environmental Sensor (Edge Device)

System_Boundary(sensorDevice, "Smart Environmental Sensor") {
    Container(sensorFirmware, "Sensor Application Firmware", "C / FreeRTOS on STM32U575", "FreeRTOS-based embedded firmware managing data acquisition, power cycling, and networking.")
    Container(sensorHardware, "BME688 Sensor Subsystem", "Silicon / MEMS", "Digital MEMS sensor measuring temperature, humidity, barometric pressure, and VOC gas.")
    ContainerDb(configStorage, "Non-Volatile Storage (NVS)", "Macronix SPI Flash", "Encrypted SPI NOR flash memory storing Wi-Fi credentials, certificates, and offline logs.")
}

Container_Ext(mqttBroker, "Cloud Ingestion Broker", "EMQX / AWS IoT Core", "High-throughput MQTT broker terminating device TLS connections.")
System_Ext(localHub, "Local Smart Hub", "Matter over Wi-Fi", "Local home automation gateway.")

Rel(sensorFirmware, sensorHardware, "Triggers measurement cycles and reads raw register values", "I2C Bus @ 400 kHz")
Rel(sensorFirmware, configStorage, "Reads/writes credentials, crash dumps, and staged firmware", "SPI Bus @ 32 MHz")
Rel(sensorFirmware, mqttBroker, "Publishes telemetry and subscribes to delta updates", "MQTT over TLS 1.3 (mTLS)")
Rel(sensorFirmware, localHub, "Emits local telemetry", "Matter / UDP")

@enduml
```
[[CAPTION:Figure]] Matching PlantUML C4 script for View 2: Edge Device Containers.

### C. View 3: Cloud Platform Container Diagram (`Container_CloudPlatform.puml`)

```plantuml
@startuml
!include <C4/C4_Container>

LAYOUT_WITH_LEGEND()

title Container Diagram - Environmental Cloud Platform

System_Boundary(cloudPlatform, "Environmental Cloud Platform") {
    Container(mqttBroker, "Cloud Ingestion Broker", "EMQX / AWS IoT Core", "High-throughput MQTT broker terminating device TLS connections and routing messages.")
    Container(ingestionWorker, "Telemetry Ingestion Worker", "Go Microservice", "Consumes raw telemetry messages, validates schema, applies calibrations, and writes time-series records.")
    Container(deviceRegistry, "Device Shadow & Registry Service", "Node.js / TypeScript", "Maintains device digital twins, provisioning credentials, desired state, and FOTA campaigns.")
    ContainerDb(telemetryDb, "Telemetry Time-Series Store", "TimescaleDB / Timeseries", "Optimised time-series database storing sensor metrics and historical aggregates.")
    ContainerDb(metadataDb, "Relational Metadata Database", "PostgreSQL 16", "Stores user accounts, home floor plans, device ownership, and alerting rules.")
    Container(graphqlApi, "GraphQL Application Gateway", "Node.js / Apollo Server", "Serves unified queries and real-time WebSockets subscriptions to clients.")
}

Container_Ext(sensorFirmware, "Sensor Firmware", "C / FreeRTOS", "Embedded sensor fleet.")
System_Ext(mobileApp, "Smart Life Mobile App", "Flutter Client", "Homeowner user interface.")

Rel(sensorFirmware, mqttBroker, "Publishes telemetry and subscribes to delta updates", "MQTT over TLS 1.3 (mTLS)")
Rel(mqttBroker, ingestionWorker, "Routes incoming telemetry messages", "Internal Queue / Kafka")
Rel(ingestionWorker, telemetryDb, "Writes batch time-series sensor samples", "SQL / Native TCP")
Rel(ingestionWorker, deviceRegistry, "Updates last-seen timestamp and battery state", "gRPC")

Rel(deviceRegistry, metadataDb, "Reads and writes device profiles and ownership records", "SQL")
Rel(graphqlApi, telemetryDb, "Queries metric history and rollups", "SQL")
Rel(graphqlApi, deviceRegistry, "Reads device shadow and dispatches desired state updates", "gRPC")
Rel(graphqlApi, metadataDb, "Authenticates users and reads home layouts", "SQL")

Rel(mobileApp, graphqlApi, "Fetches dashboard metrics and sends remote commands", "HTTPS / WSS")

@enduml
```
[[CAPTION:Figure]] Matching PlantUML C4 script for View 3: Cloud Platform Containers.

### D. View 4: Firmware Component Architecture (`Component_FirmwareArchitecture.puml`)

```plantuml
@startuml
!include <C4/C4_Component>

LAYOUT_WITH_LEGEND()

title Component Diagram - Sensor Application Firmware

Container_Boundary(sensorFirmware, "Sensor Application Firmware") {
    Component(sensorAcq, "Sensor Acquisition Manager", "C Module / RTOS Task", "Schedules periodic sensor readings, applies calibration offsets, and filters noise.")
    Component(powerOrch, "Power & Sleep Orchestrator", "C Module / State Machine", "Coordinates transitions between active measurement, network transmission, and deep sleep.")
    Component(wifiMgr, "Wi-Fi & Network Manager", "C Module / Network Task", "Manages 802.11 b/g/n association, station state, and network recovery.")
    Component(mqttClient, "MQTT Ingestion Client", "C Module / coreMQTT", "Manages secure mTLS connections and serialises JSON telemetry payloads.")
    Component(fotaAgent, "FOTA Update Agent", "C Module / Bootloader Interface", "Downloads signed firmware chunks, validates SHA-256 signatures, and writes to staging flash.")
    Component(configStore, "Configuration Store", "C Module / LittleFS HAL", "Provides thread-safe access to provisioned settings and network credentials.")
    Component(sensorHal, "Sensor HAL & Driver", "C Module / I2C Bus Driver", "I2C peripheral driver communicating directly with the BME688 hardware registers.")
}

Container_Ext(sensorHardware, "BME688 Sensor Subsystem", "Silicon IC", "Digital MEMS sensor measuring environmental climate.")
ContainerDb_Ext(configStorage, "Non-Volatile Storage (NVS)", "Macronix Flash", "SPI NOR flash memory.")
Container_Ext(mqttBroker, "Cloud Ingestion Broker", "Cloud MQTT", "Ingests telemetry frames.")

Rel(powerOrch, sensorAcq, "Wakes and triggers scheduled reading", "Direct Call / Event Signal")
Rel(sensorAcq, sensorHal, "Reads compensated sensor values", "C API Call")
Rel(sensorHal, sensorHardware, "Reads data registers", "I2C HAL Driver")

Rel(sensorAcq, mqttClient, "Enqueues telemetry payload", "FreeRTOS Queue")
Rel(powerOrch, wifiMgr, "Commands network connect/disconnect for power conservation", "RTOS Event Group")
Rel(wifiMgr, mqttClient, "Notifies IP address acquisition and link state", "Event Notification")

Rel(mqttClient, configStore, "Retrieves client TLS certificates and broker endpoint", "C API Call")
Rel(configStore, configStorage, "Reads stored keys and nonces", "LittleFS File IO")

Rel(fotaAgent, mqttClient, "Subscribes to update jobs and downloads signed chunks", "MQTT Callback")
Rel(fotaAgent, configStorage, "Writes firmware image to staging partition", "Flash Driver Call")
Rel(fotaAgent, powerOrch, "Requests system reboot into bootloader", "System Reset")

Rel(mqttClient, mqttBroker, "Publishes telemetry payload", "mTLS Socket")

@enduml
```
[[CAPTION:Figure]] Matching PlantUML C4 script for View 4: Firmware Components.

### E. View 5: Cloud Ingestion Worker Component Architecture (`Component_CloudIngestionWorker.puml`)

```plantuml
@startuml
!include <C4/C4_Component>

LAYOUT_WITH_LEGEND()

title Component Diagram - Telemetry Ingestion Worker

Container_Boundary(ingestionWorker, "Telemetry Ingestion Worker (Go Service)") {
    Component(streamConsumer, "MQTT Stream Consumer", "Go Goroutine Pool", "Consumes raw telemetry events from message broker queue.")
    Component(payloadValidator, "Schema & Security Validator", "Go Package", "Validates payload format and authenticates device HMAC signatures.")
    Component(metricCalibrator, "Metric Normaliser & Calibrator", "Pipeline Module", "Applies sensor altitude offsets and converts VOC resistance to IAQ index.")
    Component(batchWriter, "Time-Series Batch Writer", "Buffer Pool", "Buffers samples and executes bulk SQL copy operations into database.")
    Component(shadowSyncer, "Device Shadow Syncer", "gRPC Client", "Synchronises reported battery, firmware version, and last-seen state.")
}

Container_Ext(mqttBroker, "Cloud Ingestion Broker", "EMQX / AWS IoT", "Dispatches device messages to worker queue.")
ContainerDb_Ext(telemetryDb, "Telemetry Time-Series Store", "TimescaleDB", "Time-series database storing sensor metrics.")
Container_Ext(deviceRegistry, "Device Registry Service", "Node.js Service", "Maintains device digital twins and shadows.")

Rel(mqttBroker, streamConsumer, "Routes raw messages", "AMQP / Kafka Queue")
Rel(streamConsumer, payloadValidator, "Passes raw payload", "Go Channel")
Rel(payloadValidator, metricCalibrator, "Passes validated data", "Go Channel")
Rel(metricCalibrator, batchWriter, "Appends processed sample", "In-Memory Ring Buffer")
Rel(metricCalibrator, shadowSyncer, "Signals device heartbeat", "Go Channel")

Rel(batchWriter, telemetryDb, "Executes batch insert", "SQL / Native TCP")
Rel(shadowSyncer, deviceRegistry, "Updates reported shadow state", "gRPC over HTTP/2")

@enduml
```
[[CAPTION:Figure]] Matching PlantUML C4 script for View 5: Cloud Ingestion Worker Components.

### F. View 6: Physical and Cloud Deployment Topology (`Deployment_ProductionTopology.puml`)

```plantuml
@startuml
!include <C4/C4_Deployment>

LAYOUT_WITH_LEGEND()

title Deployment Diagram - Production Hardware & Cloud Topology

Deployment_Node(home, "Residential Smart Home", "Customer Site") {
    Deployment_Node(wall, "Living Room Wall Mount", "Polycarbonate Enclosure") {
        Deployment_Node(pcb, "PCB Assembly", "4-Layer FR-4 Board") {
            Deployment_Node(mcu, "STM32U575 MCU", "ARM Cortex-M33 @ 160MHz") {
                Container(sensorFirmware, "Sensor Firmware", "C / FreeRTOS", "Application image")
            }
            Deployment_Node(sensor_ic, "Bosch BME688", "3.0 x 3.0 mm LGA Package") {
                Container(sensorHardware, "BME688 Sensor", "MEMS Silicon", "Digital environmental sensor")
            }
            Deployment_Node(flash_ic, "Macronix MX25R 8MB", "USON-8 Package") {
                ContainerDb(configStorage, "NVS Storage", "SPI NOR Flash", "LittleFS filesystem")
            }
        }
    }

    Deployment_Node(router, "Home Wi-Fi Router", "Residential Gateway") {
        Deployment_Node(server, "Local Home Server", "Raspberry Pi 5") {
            System_Ext(localHub, "Local Smart Hub", "Home Assistant / Matter")
        }
    }

    Deployment_Node(phone, "User Smartphone", "Apple iPhone 15") {
        System_Ext(mobileApp, "Smart Life App", "Flutter Mobile Client")
    }
}

Deployment_Node(aws, "AWS Cloud Region (eu-west-1)", "Amazon Web Services") {
    Deployment_Node(iot_core, "AWS IoT Core", "Managed Gateway") {
        Container(mqttBroker, "Ingestion Broker", "EMQX / AWS IoT", "MQTT TLS endpoint")
    }
    Deployment_Node(eks, "EKS Kubernetes Cluster", "Managed Containers") {
        Deployment_Node(worker_pod, "Ingestion Pods", "Go Runtime") {
            Container(ingestionWorker, "Ingestion Worker", "Go Microservice", "Stream processing")
        }
        Deployment_Node(registry_pod, "Registry Pods", "Node.js Runtime") {
            Container(deviceRegistry, "Registry Service", "Node.js", "Device shadows")
        }
        Deployment_Node(api_pod, "Gateway Pods", "Node.js Runtime") {
            Container(graphqlApi, "GraphQL Gateway", "Apollo Server", "Client API")
        }
    }
    Deployment_Node(db_tier, "Managed Database Tier", "AWS Cloud DBs") {
        ContainerDb(telemetryDb, "Telemetry Store", "TimescaleDB", "Time-series data")
        ContainerDb(metadataDb, "Metadata Store", "RDS PostgreSQL", "User & device metadata")
    }
}

Rel(sensorFirmware, sensorHardware, "Reads raw data", "I2C Bus @ 400 kHz")
Rel(sensorFirmware, configStorage, "Reads credentials & logs", "SPI Bus @ 32 MHz")
Rel(sensorFirmware, mqttBroker, "Publishes telemetry", "MQTT over TLS 1.3")
Rel(sensorFirmware, localHub, "Broadcasts events", "Matter over Wi-Fi")

Rel(mqttBroker, ingestionWorker, "Routes stream", "Internal Queue")
Rel(ingestionWorker, telemetryDb, "Batch inserts", "SQL / TCP")
Rel(ingestionWorker, deviceRegistry, "Syncs shadow", "gRPC")

Rel(deviceRegistry, metadataDb, "Reads/writes metadata", "SQL")
Rel(graphqlApi, telemetryDb, "Queries history", "SQL")
Rel(graphqlApi, deviceRegistry, "Queries shadow", "gRPC")
Rel(graphqlApi, metadataDb, "Queries user records", "SQL")

Rel(mobileApp, graphqlApi, "Fetches dashboard data", "HTTPS / WSS")

@enduml
```
[[CAPTION:Figure]] Matching PlantUML C4 script for View 6: Physical and Cloud Deployment Topology.

## 4. Running Structurizr Lite Locally

This repository provides built-in tools to launch and export Structurizr DSL models directly without manual Docker configurations:

### A. Launching the Interactive Web Viewer

Run the local helper script from the root of the repository:

```bash
python tools/structurizr/structurizr-local.py docs/guides/c4-model-guide/workspace.dsl
```

This launches Structurizr Lite in a containerised instance. Open your browser to `http://localhost:8080` to interactively pan, zoom, inspect component dependencies, and switch between System Context, Container, Component, and Deployment views.

### B. Exporting Diagrams to PlantUML and Mermaid

To export the views defined in `workspace.dsl` into standard PlantUML C4 files or Mermaid markdown snippets:

```bash
# Using Structurizr CLI export
structurizr-cli export -w docs/guides/c4-model-guide/workspace.dsl -f plantuml/c4plantuml -o docs/guides/c4-model-guide/gen/

# Using the repository automated exporter
python tools/structurizr/structurizr-export.py docs/guides/c4-model-guide/workspace.dsl
```

The exporter generates `.puml` files corresponding to each declared view (for example, `SystemContext_Overview.puml`, `Container_EdgeDevice.puml`, `Component_FirmwareArchitecture.puml`, `Component_CloudIngestionWorker.puml`, `Deployment_ProductionTopology.puml`).

## 5. Best Practices for Structurizr DSL in Embedded Projects

| Practice | Recommendation | Why It Matters |
| :--- | :--- | :--- |
| **Separate Firmware from Hardware** | Model physical sensors as `#Sensor` hardware containers and the application code as `#Firmware` containers. | Clarifies the boundary between physical silicon and executable machine code. |
| **Label Hardware Interfaces** | Specify baud rates, bus standards, and voltages on relations (for example, `"I2C Bus @ 400 kHz"`, `"SPI @ 32 MHz"`). | Eliminates ambiguity for electrical and firmware engineers reviewing pinouts and timing. |
| **Model Power Modes with Tags** | Use custom tags such as `#AlwaysOn` and `#SwitchedPowerRail` on hardware deployment nodes. | Highlights high-current radio peripherals that must be dynamically power-gated to preserve battery life. |
| **Keep Components Architectural** | Model RTOS tasks, worker pools, event queues, and state machines as components. Do not model single helper functions or static utility files. | Prevents diagram bloat and keeps the view focused on system concurrency and data flow. |
[[CAPTION:Table]] Structurizr DSL best practices for embedded and connected systems.
