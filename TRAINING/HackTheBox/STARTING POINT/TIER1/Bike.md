
Bike
---
## Getting Started
---
Use command to set Target IP
```bash
IP='10.129.97.64' ; echo $IP
```

Use command to set Target IP
```bash
HIP="$(ifconfig tun0  | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')" ; echo $HIP

```
---
## Enumeration
---
### NMAP
---
Nmap Command Ran
```bash
nmap -sV -sC $IP -v
```

Results
```bash
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-12 18:41 EDT
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 18:41
Completed NSE at 18:41, 0.00s elapsed
Initiating NSE at 18:41
Completed NSE at 18:41, 0.00s elapsed
Initiating NSE at 18:41
Completed NSE at 18:41, 0.00s elapsed
Initiating Ping Scan at 18:41
Scanning 10.129.97.64 [2 ports]
Completed Ping Scan at 18:41, 0.03s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 18:41
Completed Parallel DNS resolution of 1 host. at 18:41, 0.00s elapsed
Initiating Connect Scan at 18:41
Scanning 10.129.97.64 [1000 ports]
Discovered open port 80/tcp on 10.129.97.64
Discovered open port 22/tcp on 10.129.97.64
Completed Connect Scan at 18:41, 0.44s elapsed (1000 total ports)
Initiating Service scan at 18:41
Scanning 2 services on 10.129.97.64
Completed Service scan at 18:41, 6.10s elapsed (2 services on 1 host)
NSE: Script scanning 10.129.97.64.
Initiating NSE at 18:41
Completed NSE at 18:41, 1.15s elapsed
Initiating NSE at 18:41
Completed NSE at 18:41, 0.13s elapsed
Initiating NSE at 18:41
Completed NSE at 18:41, 0.00s elapsed
Nmap scan report for 10.129.97.64
Host is up (0.028s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
80/tcp open  http    Node.js (Express middleware)
|_http-title:  Bike 
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 18:41
Completed NSE at 18:41, 0.00s elapsed
Initiating NSE at 18:41
Completed NSE at 18:41, 0.00s elapsed
Initiating NSE at 18:41
Completed NSE at 18:41, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.29 seconds
zsh: segmentation fault  nmap -sV -sC $IP -v

```

---
## Foothold

---
## Lateral Movement

---
## Privilege Escalation

---
## Flags
---

root.txt
```bash
6b258d726d287462d60c103d0142a81c
```

---
## Tags
---