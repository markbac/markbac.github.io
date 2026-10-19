---
title: Fleet-scale OTA update campaigns
---

# Fleet-scale OTA update campaigns

Firmware Over-The-Air (FOTA) updates represent both the most critical operational capability and the single highest-risk procedure in connected device engineering. A bug in cloud software can be rolled back within seconds by an SRE squad. A flawed firmware update dispatched globally can simultaneously brick an entire fleet of field-deployed hardware, requiring catastrophic physical recalls.

This chapter defines the engineering requirements for managing fleet-scale OTA campaigns, executing phased canary rollouts, minimizing cellular bandwidth via delta compression, and enforcing autonomous bootloader rollbacks.

## 1. Phased Staged Rollouts & Canary Deployments

Dispatched updates must never be released to a production fleet simultaneously. Campaigns must progress through five gated phases:

```mermaid
flowchart LR
    P0["Phase 0: Lab HIL Racks<br/>(10 Units, 24 Hours)"] --> P1["Phase 1: Canary Dogfood<br/>(0.1% Fleet, 48 Hours)"]
    P1 --> P2["Phase 2: Pilot Fleet<br/>(1% Fleet, 5 Days)"]
    P2 --> P3["Phase 3: Broad Staged<br/>(10% Fleet, 7 Days)"]
    P3 --> P4["Phase 4: Full Deployment<br/>(100% Fleet)"]
```

[[CAPTION:Figure]] Five-phase staged rollout sequence for risk-managed OTA deployments.

### 1.1 Automated Campaign Circuit Breakers

Every active campaign must be monitored by automated health supervisors in the cloud:

> [!CAUTION]
> If the cumulative failure rate (devices reporting download failures, bootloader CRC errors, or watchdog crash loops) exceeds **0.5% of targeted nodes**, the campaign engine must immediately trip an automated circuit breaker, halting further firmware distributions and alerting engineering on-call personnel.

## 2. Bandwidth Optimisation: Delta Updates (BSDiff / Courgette)

Sending a full 1 MB or 2 MB firmware image over cellular LPWAN (NB-IoT) to one million devices would use terabytes of data. It would take weeks and drain the batteries.

The enterprise OTA platform must support **Binary Delta Compression**:

```mermaid
flowchart TD
    Old["Base Firmware (v2.1.0)"] --> Diff{"Binary Diff Engine<br/>(BSDiff / Courgette)"}
    New["Target Firmware (v2.2.0)"] --> Diff
    Diff --> Delta["Signed Delta Patch (v2.1 -> v2.2)<br/>(Typical Size: 35 KB - 80 KB)"]
    Delta --> Device["Edge Device (Runs v2.1.0)"]
    Device --> Reconstruct["On-Device Patch Reconstructor"]
    Reconstruct --> ActiveBank["Writes Assembled v2.2.0 to Bank B"]
```

[[CAPTION:Figure]] Delta compression generating compact patches from existing base images.

1. **85% to 95% Bandwidth Reduction**: By transmitting only the changed binary symbols and instruction relocations, the payload size drops from ~1 MB down to 40 KB.
1. **Deterministic Verification**: Before applying a delta patch, the edge device validates the SHA-256 hash of its currently executing flash image (Bank A) to ensure the base matches the delta expectations exactly. Once reconstructed in Bank B, the full binary hash is verified against the signed release manifest.

## 3. Dual-Bank A/B Bootloader Architecture & Automatic Rollback

Hardware must implement dual-bank flash partitioning (Bank A and Bank B) coordinated by a cryptographically secure bootloader (such as MCUboot or TF-M):

```mermaid
sequenceDiagram
    participant Cloud as OTA Cloud Service
    participant App as Active Firmware (Bank A)
    participant BL as Secure Bootloader
    participant NewBank as Candidate (Bank B)
    participant WDT as Hardware Watchdog

    Cloud->>App: Deliver Signed Firmware Binary / Delta
    App->>NewBank: Stream chunks into Bank B, then Verify ECDSA P-256 Signature
    App->>App: Mark Bank B as "Candidate / Test Run" in NVS
    App->>BL: Issue System Reboot
    
    BL->>BL: Detect "Test Run" flag, then Boot execution from Bank B
    BL->>NewBank: Jump to Application Entry Point (Bank B)
    
    alt Firmware Boots Successfully
        NewBank->>WDT: Initialize Watchdog
        NewBank->>Cloud: Connect to MQTT Broker & Perform Handshake
        NewBank->>NewBank: Mark Bank B as "Permanently Active / Confirmed"
        Note over NewBank,BL: Update Permanent! Bank A now available as scratch.
    else Firmware Crashes / HardFaults
        Note over NewBank: System hangs in infinite loop or HardFault
        WDT-->>BL: Watchdog times out (8 seconds), then Triggers Hardware Reset!
        BL->>BL: Detect failed trial boot! Clear "Test Run" flag.
        BL->>App: Roll back and boot proven image in Bank A!
        App->>Cloud: Report FOTA Failure (REASON: CRASH_LOOP_WATCHDOG)
    end
```

[[CAPTION:Figure]] Dual-bank trial boot sequence ensuring automated self-healing rollback.

### 3.1 Rules for Trial Boot Confirmation

1. **Autonomous Rollback**: The new firmware image must be booted in a provisional "trial" state. If the device reboots before confirming stability, the bootloader automatically reverts to the previous known-good bank.
1. **Mandatory Handshake Before Confirmation**: Firmware must never mark itself as permanently confirmed simply because it reached `main()`. Confirmation requires successfully passing three criteria:
   - Initializing all sensor buses and peripherals without errors.
   - Establishing an encrypted connection with the cloud MQTT broker.
   - Successfully receiving an acknowledgment packet from the cloud twin service.

## 4. Fleet Campaign Lifecycle Metrics

The fleet operations dashboard must track the real-time state machine of every device targeted by the campaign:

| Campaign State | Description | Next Permitted State |
| :--- | :--- | :--- |
| **Pending** | Device targeted; waiting for next communication window | Downloading |
| **Downloading** | Chunks currently streaming to Bank B over radio | Validating, Failed |
| **Validating** | Binary received; checking ECDSA signature and SHA-256 | Rebooting, Failed |
| **Rebooting** | Device has scheduled reset into candidate bank | Confirming, Rolled Back |
| **Confirming** | Candidate bank running in trial mode; testing cloud link | Succeeded, Rolled Back |
| **Succeeded** | Candidate permanently confirmed; twin updated | Complete |
| **Rolled Back** | Watchdog reset during trial boot; reverted to prior bank | Failed |

[[CAPTION:Table]] Finite state machine states during fleet OTA campaigns.
