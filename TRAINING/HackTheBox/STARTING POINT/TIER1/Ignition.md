
# Ignition
---
## Getting Started
---
Use command to set Target IP
```bash
IP='10.129.1.27' ; echo $IP
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
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-12 17:47 EDT
Stats: 0:00:12 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 0.00% done
Nmap scan report for ignition.htb (10.129.1.27)
Host is up (0.027s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.14.2
|_http-title: Home page
|_http-server-header: nginx/1.14.2

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.48 seconds


```

**Findings**

Port 80 seems to hosting website.

### Website enumeration
### Website Enumeration
Got to the IP on Firefox.
Fails to got to it. 

Use curl to gather further information
Command
```bash
curl -v http://10.129.1.27
```

Result
```bash
*   Trying 10.129.1.27:80...
* Connected to 10.129.1.27 (10.129.1.27) port 80 (#0)
> GET / HTTP/1.1
> Host: 10.129.1.27
> User-Agent: curl/7.85.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 302 Found
< Server: nginx/1.14.2
< Date: Wed, 12 Oct 2022 22:20:10 GMT
< Content-Type: text/html; charset=UTF-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< Set-Cookie: PHPSESSID=ukeh9qs184nqt6um4g2udpu9gh; expires=Wed, 12-Oct-2022 23:20:10 GMT; Max-Age=3600; path=/; domain=10.129.1.27; HttpOnly; SameSite=Lax
< Location: http://ignition.htb/

```

**Findings**
Possible domain ignition.htb


add ignition.htb/ to /etc/hosts

Use GoBuster to enumerate further

Command
```bash
gobuster dir --url http://ignition.htb/ --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt 
```

Result
```bash
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://ignition.htb/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/10/12 17:50:31 Starting gobuster in directory enumeration mode
===============================================================
/contact              (Status: 200) [Size: 28673]
/home                 (Status: 200) [Size: 25802]
/media                (Status: 301) [Size: 185] [--> http://ignition.htb/media/]
/0                    (Status: 200) [Size: 25803]                               
/catalog              (Status: 302) [Size: 0] [--> http://ignition.htb/]        
/static               (Status: 301) [Size: 185] [--> http://ignition.htb/static/]
/admin                (Status: 200) [Size: 7095]                                 
/Home                 (Status: 301) [Size: 0] [--> http://ignition.htb/home]     
/cms                  (Status: 200) [Size: 25817]                                
/checkout             (Status: 302) [Size: 0] [--> http://ignition.htb/checkout/cart/]
/robots               (Status: 200) [Size: 1]                                         
/setup                (Status: 301) [Size: 185] [--> http://ignition.htb/setup/]      
/wishlist             (Status: 302) [Size: 0] [--> 
===============================================================
2022/10/12 17:57:52 Finished
==============================================================================================================================
```


**Findings**
There seems to be an admin page.


---
## Foothold

Navigate to admin page.
Try default creds `admin:123123`
Did not work
Try admin username with other passwords
successful with `admin:qwerty12`

Access admin dashboard

**Findings**
>![[Pasted image 20221012180350.png]]

Only one user
>![[Pasted image 20221012180501.png]]

Flag was on Dashboard

>![[Pasted image 20221012180750.png]]


---
## Flags
Dashboard
```bash
797d6c988d9dc5865e010b9410f247e0
```


---
## Tags
---
#magento 