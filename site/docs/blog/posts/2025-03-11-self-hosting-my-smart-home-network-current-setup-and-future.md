---
date: 2025-03-11T12:00:00
authors:
  - markbac
categories:
  - Home lab
slug: self-hosting-my-smart-home-network-current-setup-and-future
---

# Self-Hosting My Smart Home & Network: Current Setup and Future Plans

Living in rural Lancashire with no close neighbours has its perks—peace, privacy, and the freedom to build a powerful self-hosted home network without worrying about ISP restrictions or poor infrastructure. My setup is built around **Synology, Raspberry Pi, and Docker-powered services**, giving me complete control over my network, automation, and devices. Here’s what I have running today and what I’m planning next.

<!-- more -->

***

## **My Current Home Network Setup**

### **Core Infrastructure**

* **Synology RT6600ax Router** – Handles routing and VLANs like a champ.
* **Synology DS723+ NAS (32GB RAM, NVMe cache)** – The backbone of my network, running Docker containers and hosting services.
* **Portainer** – Makes managing Docker containers much easier.
* **Heimdall** – A clean homepage for quick access to my self-hosted services.
* **Fing** – A dedicated network monitoring device to track all connected devices and detect new ones.

### **Raspberry Pi Fleet**

* **Raspberry Pi 4 (Pi-hole)** – Blocks ads and trackers at the network level.
* **Raspberry Pi 5 & Pi 400** – Used for testing, tinkering, and lightweight workloads.
* **Raspberry Pi (Home Assistant)** – The core of my smart home automation.

***

## **What Works Well?**

✅ **Reliable Infrastructure** – The NAS and Raspberry Pis each handle their own dedicated tasks.\
✅ **Network Visibility** – **Fing** helps track connected devices and alerts me to any new ones.\
✅ **Ad-Free Browsing** – Pi-hole ensures the internet is cleaner.\
✅ **Containerisation** – Running most services in Docker keeps everything modular and easy to manage.\
✅ **Smart Home Control** – Home Assistant integrates my devices seamlessly.

***

## **What’s Next? Future Plans & Additions**

### **Monitoring & Dashboards**

🔹 **Flame Dashboard** – A sleek, modern alternative to Heimdall with search functionality.\
🔹 **Uptime Kuma** – A self-hosted service to monitor uptime and network status.\
🔹 **Glances** – A real-time monitoring tool to track CPU, RAM, and system stats across devices.

### **Raspberry Pi Monitoring**

I want better visibility into the **health and performance** of my Raspberry Pis. Some potential solutions:

* **Grafana + Prometheus** – Powerful but requires some setup.
* **Glances with Agent Mode** – Simple and lightweight.
* **PiStats** – A dashboard-style web tool specifically for monitoring Pi devices.
* **Raspberry Pi Monitoring Script** – A simple cron job that logs CPU temp, RAM, and storage usage.

### **Automation & Updates**

🔹 **Watchtower** – Automates Docker container updates (used with caution).\
🔹 **Dozzle** – A lightweight web-based log viewer for Docker.

***

## **Why Self-Host?**

For me, self-hosting is about **control, reliability, and performance**. I don’t rely on external cloud services, I avoid monthly subscription costs, and I can fine-tune everything to my specific needs.

With **better monitoring, dashboards, and automation**, my setup will become even more streamlined and resilient. Now, the only question is: **What should I add first?** 🤔
