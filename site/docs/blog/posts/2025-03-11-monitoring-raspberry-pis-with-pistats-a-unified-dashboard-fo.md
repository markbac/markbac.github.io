---
date: 2025-03-11T13:00:00
authors:
  - markbac
categories:
  - Home lab
slug: monitoring-raspberry-pis-with-pistats-a-unified-dashboard-fo
---

# Monitoring Raspberry Pis with PiStats & A Unified Dashboard for All Devices

As my self-hosted network grows, keeping an eye on my **Raspberry Pis** is becoming more important. With multiple **Pi-hole, Home Assistant, and testing boards**, I need a way to track their **CPU usage, temperature, storage, and overall health**—ideally from a **single dashboard** that also monitors other key devices.

<!-- more -->

In this post, I’ll cover:

* **PiStats** – A simple way to monitor Raspberry Pi devices.
* **Unified Dashboards** – How to centralise monitoring for all devices, including Synology NAS and other hardware.

***

## **PiStats: A Simple Raspberry Pi Monitoring Tool**

### **What is PiStats?**

PiStats is a **lightweight monitoring tool** designed for Raspberry Pi devices. It provides real-time stats on:\
✅ CPU usage\
✅ Temperature\
✅ Memory & storage usage\
✅ Uptime

It’s a great alternative to setting up **Grafana & Prometheus**, which, while powerful, can be overkill for basic monitoring needs.

### **How to Install PiStats on a Raspberry Pi**

Since PiStats is a simple Python script, setup is quick.

1️⃣ **Install dependencies**

```bash
sudo apt update && sudo apt install python3-pip -y
pip3 install flask
```

2️⃣ **Download PiStats**

```bash
git clone https://github.com/Spirotot/PiStats.git
cd PiStats
```

3️⃣ **Run PiStats**

```bash
python3 app.py
```

4️⃣ **Access the Web UI**

* Open a browser and go to `http://<your-pi-ip>:5000`
* You’ll see a basic dashboard with CPU, temperature, and memory stats.

### **Should You Use PiStats?**

✅ **Pros:**

* Super lightweight (just a small Python script).
* Simple web-based UI with key metrics.
* No need for a database or complex setup.

❌ **Cons:**

* No long-term data storage (only real-time stats).
* No multi-device monitoring—only shows one Raspberry Pi at a time.

PiStats is great for quick, **per-device** monitoring, but if you want a **single dashboard for all Raspberry Pis and other devices**, you’ll need something more **scalable**.

***

## **Building a Unified Dashboard for Raspberry Pis & Other Devices**

Since I want **one dashboard** to monitor **all Raspberry Pis, my Synology NAS, and other devices**, PiStats alone won’t cut it. Here are **two solid options**:

***

### **Option 1: Glances + Web UI (Quick & Simple)**

Glances is a lightweight system monitoring tool that can show CPU, RAM, disk, and network usage across **multiple devices**.

#### **How to Install & Set Up Glances**

1️⃣ **Install Glances on all Raspberry Pis**

```bash
sudo apt update && sudo apt install glances -y
```

2️⃣ **Run Glances in Web Mode**

```bash
glances -w
```

* Access it via `http://<your-pi-ip>:61208`

3️⃣ **Centralised Dashboard:**

* Install Glances on **one device** (e.g., NAS or a Raspberry Pi).
* Add all other Pis as remote agents:

```bash
glances --browser
```

* Now, you can monitor all devices in a **single web interface**.

✅ **Pros:**

* Quick to set up, no database required.
* Works on **Raspberry Pi, Synology NAS, and other Linux devices**.
* Lightweight compared to Prometheus/Grafana.

❌ **Cons:**

* No historical data storage—only real-time monitoring.

***

### **Option 2: Grafana + Prometheus (Powerful & Scalable)**

If you want **long-term monitoring, alerts, and detailed analytics**, Grafana + Prometheus is a **more advanced solution**.

#### **How to Set Up a Centralised Grafana Dashboard**

1️⃣ **Install Prometheus on a central device (NAS or Pi)**

```bash
docker run -d --name=prometheus -p 9090:9090 prom/prometheus
```

2️⃣ **Install Node Exporter on Raspberry Pis**

```bash
wget https://github.com/prometheus/node_exporter/releases/latest/download/node_exporter-armv7
chmod +x node_exporter-armv7
./node_exporter-armv7 &
```

* This sends Pi metrics to Prometheus.

3️⃣ **Install Grafana** (on NAS or another Pi)

```bash
docker run -d -p 3000:3000 grafana/grafana
```

* Access Grafana at `http://<your-ip>:3000`
* Add Prometheus as a **data source**.
* Create dashboards to track **CPU, temperature, RAM, uptime**, and more.

✅ **Pros:**

* Scales to **multiple Raspberry Pis, NAS, and other devices**.
* Stores historical data for analysis.
* Custom dashboards with alerts.

❌ **Cons:**

* More complex to set up.
* Uses more resources than Glances.

***

## **What’s Best for My Setup?**

Since I want a **single dashboard** that covers all my Raspberry Pis **and** my NAS, my approach will likely be:

* **For quick monitoring:** **Glances Web UI**
* **For long-term data & alerts:** **Grafana + Prometheus**

PiStats is great as a **basic, per-device tool**, but if you want true **multi-device monitoring**, Glances or Grafana are the way to go.
