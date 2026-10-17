---
title: Cellular LPWAN
---

# Cellular LPWAN: NB-IoT and LTE-M

A low-power wide-area network (LPWAN) carries small amounts of data over long distances from devices that must run for years on a battery. NB-IoT and LTE-M are the two LPWAN technologies built into the mobile network standards by 3GPP (the body behind 4G and 5G). Because they run on operators' licensed spectrum and existing masts, they need no private network infrastructure, and both are part of 5G's support for massive numbers of devices.

The unlicensed alternatives, LoRaWAN and Sigfox, need their own gateways or a provider that runs them, and offer lower data rates.

## NB-IoT and LTE-M compared

| | NB-IoT (Cat-NB1, Cat-NB2) | LTE-M (Cat-M1, Cat-M2) |
| --- | --- | --- |
| 3GPP release | 13 (NB1), 14 (NB2) | 13 (M1), 14 (M2) |
| Bandwidth | 180 kHz | 1.4 MHz (M1), 5 MHz (M2) |
| Peak data rate | Tens of kbit/s (NB1) to about 130 kbit/s (NB2) | About 300 kbit/s to 1 Mbit/s (M1), up to about 4 Mbit/s (M2) |
| Latency | Seconds | 10 to 15 ms in good conditions |
| Mobility | Cell reselection when idle; no handover | Full handover while connected |
| Voice | No | VoLTE possible |
| Coverage | Best: designed for basements and cellars | Good, slightly less than NB-IoT |
| Roaming | Patchy, depends on operator agreements | Widely available |
| Good for | Static devices sending small, infrequent messages | Moving devices, larger downloads such as firmware, anything that needs a quick reply |

[[CAPTION:Table]] The two cellular LPWAN technologies. Real-world rates are well below the peaks.

Many modules support both, and choose according to what the network offers. Where an operator supports both, LTE-M is usually the safer choice unless deep indoor coverage is critical.

## Saving power

Two features let a device stay registered on the network while its radio is almost entirely off.

- **PSM (Power Saving Mode)**: after sending, the device stays reachable for a short active time (timer T3324), then goes into a deep sleep in which it cannot be reached at all. It wakes when it has something to send, or when the periodic update timer (T3412) expires. Sleep current can be a few microamps. Best for devices that only send.
- **eDRX (extended Discontinuous Reception)**: the device sleeps and wakes briefly at a fixed interval (from seconds up to hours) to check for incoming data. It can receive downlink messages with a known delay. Best for devices that must sometimes be commanded.

Devices request these timers with standard AT commands (`AT+CPSMS`, `AT+CEDRXS`), but the network decides what it actually grants. Always read back the values the network accepted.

## Coverage and signal

- **RSRP** (Reference Signal Received Power): signal strength. Around −100 dBm is good; below −120 dBm is weak.
- **RSRQ** and **SINR**: signal quality and interference.
- **Coverage enhancement (CE) levels**: in poor coverage, the network repeats transmissions many times so they still get through. Data still arrives, but each message takes far longer and uses far more energy. A device that is always at the deepest CE level will have a much shorter battery life than the datasheet suggests.

## SIMs

- **Plastic and MFF2 SIMs**: a removable card or a SIM chip soldered to the board.
- **eSIM (eUICC)**: the SIM holds several operator profiles that can be changed remotely, so devices can switch operator without a site visit. GSMA's SGP.32 specification defines remote provisioning designed for IoT devices.
- **iSIM**: the SIM function built into the modem chip itself, saving space and cost.

## Designing for cellular LPWAN

- Send as few and as small messages as possible. Use compact payloads ([CBOR](cbor.md)) and UDP-based protocols ([CoAP](coap.md), [LwM2M](lwm2m.md)) where you can; a TLS-over-TCP handshake on NB-IoT can cost more energy than the data itself.
- Use DTLS Connection ID or session resumption so a wake-up does not need a full handshake.
- Measure current with a real SIM on a real network, in the worst coverage you expect.
- Plan for network changes: 2G and 3G are being switched off in many countries, including the UK, so LTE-M and NB-IoT are the long-term options for new designs.

## Where next

- [Firmware over the air](firmware-over-the-air.md) covers updates over slow links.
- The [Guides](../guides/index.md) section covers modem integration in practice.
