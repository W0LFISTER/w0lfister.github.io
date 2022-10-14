# Preignition
---
## Getting Started
---
Use command to set Target IP
```bash
IP='10.129.65.136' ; echo $IP
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
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-11 16:36 EDT
Nmap scan report for 10.129.65.136
Host is up (0.029s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.14.2
|_http-title: Welcome to nginx!
|_http-server-header: nginx/1.14.2

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.51 seconds


```

**Findings**
Port 80 is running nginx. 

### Website Enumeration
Command
```bash
gobuster dir --url http://$IP/ --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php
```

Result
```bash
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.129.65.136/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php
[+] Timeout:                 10s
===============================================================
2022/10/11 16:41:05 Starting gobuster in directory enumeration mode
===============================================================
/admin.php            (Status: 200) [Size: 999]
Progress: 73978 / 175330 (42.19%)             ^C
[!] Keyboard interrupt detected, terminating.
                                               
===============================================================
2022/10/11 16:45:57 Finished
===============================================================
```

---
## Foothold
---
Navigate to `http://10.129.65.136/admin.php` and find login page.
>![[Pasted image 20221011165102.png]]

Google to find that admin/ admin are default creds.
log in with the creds and find flag on webpage.

>![[Pasted image 20221011165031.png]]
---
## Flags


website
```bash
6483bee07c1c1d57f14e5b0717503c73
```

---
## Tags
---