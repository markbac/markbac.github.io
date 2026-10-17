---
title: IoT and embedded primers
---

# IoT and embedded primers

An embedded system is a computer built into a product to do one job: a microcontroller in a sensor, a thermostat, a motor drive. The Internet of Things (IoT) connects such devices to networks and to services in the cloud. Building them means working with small memories, limited power, unreliable links and hardware that is hard to reach once it is installed, and the devices must stay secure for years.

```mermaid
flowchart LR
    S[Sensors and actuators] --> M[Microcontroller and firmware]
    M -- radio or wired link --> G[Gateway or edge]
    G -- internet --> C[Cloud platform]
    C --> A[Applications and users]
```

[[CAPTION:Figure]] The layers of a typical IoT system.

## On the device

- [Embedded systems design](embedded-systems-design.md): constraints, layering and power.
- [Real-time operating systems and FreeRTOS](rtos-and-freertos.md): tasks, scheduling and when you need an RTOS.
- [Finite state machines](finite-state-machines.md): the most useful pattern in firmware.
- [Interrupts and DMA](interrupts-and-dma.md): reacting to hardware without wasting the CPU.
- [Watchdog timers](watchdog-timers.md): recovering when software hangs.
- [Bootloaders](bootloaders.md): starting safely and accepting new firmware.

## Connecting devices

- [MQTT](mqtt.md): publish and subscribe over TCP.
- [CoAP](coap.md): REST for constrained devices over UDP.
- [LwM2M](lwm2m.md): device management built on CoAP.
- [Cellular LPWAN](cellular-lpwan.md): NB-IoT and LTE-M.
- [Firmware over the air](firmware-over-the-air.md): updating devices in the field.
- [Edge computing for IoT](edge-computing-for-iot.md): processing data close to the devices.

## Testing

- [Hardware-in-the-loop testing](hardware-in-the-loop-testing.md): automated tests on real boards.

Security standards for devices are in [Security primers](security.md), including [ETSI EN 303 645](etsi-en-303-645.md). The [Handbook](../handbook/index.md) covers device and platform architecture, and the [Guides](../guides/index.md) give practical how-tos.
