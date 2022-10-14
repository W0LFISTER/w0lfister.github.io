

Explosion
---
## Getting Started
---
Use command to set Target IP
```bash
IP='10.129.16.233' ; echo $IP
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
nmap -sV -sC $IP | copy
```

Results
```bash
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-10 18:48 EDT
Nmap scan report for 10.129.16.233
Host is up (0.030s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: EXPLOSION
|   NetBIOS_Domain_Name: EXPLOSION
|   NetBIOS_Computer_Name: EXPLOSION
|   DNS_Domain_Name: Explosion
|   DNS_Computer_Name: Explosion
|   Product_Version: 10.0.17763
|_  System_Time: 2022-10-10T22:49:07+00:00
|_ssl-date: 2022-10-10T22:49:16+00:00; +2s from scanner time.
| ssl-cert: Subject: commonName=Explosion
| Not valid before: 2022-10-09T22:38:40
|_Not valid after:  2023-04-10T22:38:40
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-10-10T22:49:12
|_  start_date: N/A
|_clock-skew: mean: 1s, deviation: 0s, median: 1s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.75 seconds
```

**FIndings**
```bash
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
```

Seems to have RDP on it.


---
## Foothold
 Use xfreerdp to gain a foothold

Command
```bash
xfreerdp /v:$IP         
```


Result
>![[Pasted image 20221010193313.png]]

try to bypass cert and us Administrator 

try with no password

```bash
xfreerdp /v:$IP /cert:ignore /u:Administrator
```

>![[Pasted image 20221010191212.png]]

**Findings**
flag.txt on the desktop


---
## Flags

flag.txt
```bash
951fa96d7830c451b536be5a6be008a0
```

---
## Tags
---
