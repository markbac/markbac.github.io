---
date: 2025-03-11T11:00:00
authors:
  - markbac
categories:
  - Home lab
slug: setting-up-an-nginx-reverse-proxy-with-ssl-and-local-dns-for
---

# Setting Up an Nginx Reverse Proxy with SSL and Local DNS for a Synology NAS and Other Services (home.example)

> **For a private home network using a Synology NAS, Synology Router, and Raspberry Pis**

## **What This Guide Covers**

* ✅ **Use a local domain (`*.home.example`)** to access internal services.
* ✅ **Secure access with a wildcard SSL certificate (Let's Encrypt).**
* ✅ **Run Nginx Proxy Manager on Synology NAS without port conflicts.**
* ✅ **Pi-hole for local DNS resolution (without Unbound).**
* ✅ **Use Cloudflare API for automatic SSL certificate renewal.**
* ✅ **Works for all devices on the network (PC, Mac, iOS, Android, Smart TVs).**
* ❌ **No external access required.**

***

## **1⃣ Devices & Network Setup**

For this setup, we assume the following hardware:

<!-- more -->

| Device                     | IP Address         | Role                                |
| -------------------------- | ------------------ | ----------------------------------- |
| **Synology NAS**           | `192.0.2.203`      | Nginx Proxy Manager (Reverse Proxy) |
| **Home Assistant**         | `192.0.2.101`      | Home automation                     |
| **Heimdall Dashboard**     | `192.0.2.203:5050` | Service launcher                    |
| **Pi-hole (Raspberry Pi)** | `192.0.2.10`       | Local DNS                           |

***

## **2⃣ Configure Local DNS with Pi-hole (No Unbound)**

Pi-hole ensures `*.home.example` resolves correctly inside your network.

### **2.1 Install Pi-hole on a Raspberry Pi**

1. **Run the installer:**
   ```sh
   curl -sSL https://install.pi-hole.net | bash
   ```

2. **Follow the setup:**

   * Choose the Raspberry Pi’s **network interface**.
   * **Set a static IP** (`192.0.2.10` recommended).
   * **Upstream DNS Provider:** Choose **"Custom"** (we’ll configure NextDNS later).
   * Enable the **web interface** for easy management.

### **2.2 Set Up Local DNS Records in Pi-hole**

1. Open the **Pi-hole Admin Panel**:\
   `http://pi.hole/admin`
2. Go to **Settings → Local DNS → DNS Records**.
3. **Add your internal services:**
   ```
   nas.home.example → 192.0.2.203
   ha.home.example → 192.0.2.101
   heim.home.example → 192.0.2.203
   ```
4. **Save changes**.

Now, any device using Pi-hole will resolve `*.home.example` to the correct local IP.

***

## **3⃣ Set Pi-hole as the Network’s Primary DNS**

### **On Synology Router (Best Option)**

1. **Log into your Synology Router** (`http://router.synology.com`).
2. **Go to Network Centre → Internet → DHCP Server**.
3. **Set Primary DNS to:** `192.0.2.10` (Pi-hole).
4. **Remove any Secondary DNS** (to prevent bypassing Pi-hole).
5. **Apply changes**.

***

## **4⃣ Configure NextDNS as Pi-hole’s Upstream**

Since we’re not using Unbound, **Pi-hole needs an external resolver for non-local queries**.

1. Open **Pi-hole Admin Panel**.

2. **Go to Settings → DNS**.

3. **Disable all default upstream DNS providers**.

4. **Set NextDNS as the upstream DNS**:

   ```
   45.90.28.0
   45.90.30.0
   ```

   * If using **DNS-over-HTTPS (DoH)**:

     ```sh
     sudo apt install cloudflared -y
     ```

     * Add this config to `/etc/dnsmasq.d/02-cloudflared.conf`:
       ```ini
       server=https://dns.nextdns.io/YOUR_NEXTDNS_ID
       ```
     * Restart Pi-hole:
       ```sh
       sudo systemctl restart pihole-FTL
       ```

Now, **Pi-hole resolves local domains (`*.home.example`) and forwards external lookups to NextDNS.**

***

## **5⃣ Install Nginx Proxy Manager on Synology NAS**

### **5.1 Install Docker on Synology NAS**

1. **Go to Synology Package Centre**.
2. **Install Docker**.

### **5.2 Deploy Nginx Proxy Manager**

1. **SSH into your NAS** and create an NPM folder:
   ```sh
   mkdir -p /volume1/docker/npm && cd /volume1/docker/npm
   ```
2. **Create a `docker-compose.yml` file:**
   ```sh
   nano docker-compose.yml
   ```
3. **Modify the port mappings to avoid conflicts with Synology DSM:**
   ```yaml
   version: "3"
   services:
     npm:
       image: 'jc21/nginx-proxy-manager:latest'
       restart: always
       ports:
         - "8080:80"   # HTTP → Change to 8080
         - "8443:443"  # HTTPS → Change to 8443
         - "81:81"     # NPM Web UI (unchanged)
       volumes:
         - ./data:/data
         - ./letsencrypt:/etc/letsencrypt
   ```
4. **Start NPM:**
   ```sh
   docker-compose up -d
   ```

Now, NPM will listen on:

* **`http://NAS_IP:8080`** instead of `80`.
* **`https://NAS_IP:8443`** instead of `443`.

***

## **6⃣ Configure Let’s Encrypt SSL with Cloudflare API**

### **6.1 Get a Cloudflare API Token**

1. **Go to** [Cloudflare Dashboard]().
2. **Select your domain (`home.example`)**.
3. **Go to "API Tokens" → "Create Token".**
4. **Select "Edit Zone DNS"** as the permission scope.
5. **Restrict it to `home.example`**.
6. **Generate and copy the token**.

### **6.2 Add SSL Certificate in NPM**

1. **Log into Nginx Proxy Manager (`http://NAS_IP:81`)**.
2. **Go to "SSL Certificates" → "Add SSL Certificate".**
3. **Choose "Let’s Encrypt".**
4. **Enter `*.home.example` as the domain.**
5. **Use DNS Challenge → Cloudflare.**
6. **Paste your Cloudflare API Token**.
7. **Click "Save" and issue the certificate.**

✅ **Now, Let’s Encrypt will automatically renew your wildcard SSL every 90 days.**

***

## **7⃣ Configure Proxy Hosts in Nginx Proxy Manager**

1. **Go to "Hosts" → "Proxy Hosts"**.

2. **Add services (e.g., `nas.home.example`, `ha.home.example`)**:

   * **Domain**: `nas.home.example`
   * **Forward IP**: `192.0.2.203`
   * **Forward Port**: `5000`
   * **Force SSL**

3. **Repeat for other services**.

***

## **Final Setup Summary**

| Component                        | Port                                     |
| -------------------------------- | ---------------------------------------- |
| **Synology DSM**                 | Uses ports **80 & 443**                  |
| **Nginx Proxy Manager (Docker)** | Now runs on **8080 & 8443**              |
| **Synology Reverse Proxy**       | Routes **80 → 8080 & 443 → 8443**        |
| **Pi-hole (Raspberry Pi)**       | Runs on **192.0.2.10 (port 53 for DNS)** |

✅ **No port conflicts with Synology NAS.**\
✅ **Wildcard SSL auto-renewal via Cloudflare API.**\
✅ **All services accessible with `*.home.example` and HTTPS.**
