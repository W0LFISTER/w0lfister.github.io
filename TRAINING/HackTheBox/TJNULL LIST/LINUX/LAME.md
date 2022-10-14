
# LAME
---
## Getting Started
---
Use command to set Target IP
```bash
IP='10.10.10.3' ; echo $IP
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
nmap -p- $IP -Pn
```

Results
```bash
Not shown: 65530 filtered tcp ports (no-response)
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3632/tcp open  distccd


```

Nmap Command Ran
```bash
nmap -sV -v -sC $IP  -Pn -p 21,22,139,445,3632
```

Results
```bash
ORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.10.14.19
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      vsFTPd 2.3.4 - secure, fast, stable
|_End of status
22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
| ssh-hostkey: 
|   1024 60:0f:cf:e1:c0:5f:6a:74:d6:90:24:fa:c4:d5:6c:cd (DSA)
|_  2048 56:56:24:0f:21:1d:de:a7:2b:ae:61:b1:24:3d:e8:f3 (RSA)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba -Debian (workgroup: WORKGROUP)
3632/tcp open  distccd     distccd v1 ((GNU) 4.2.4 (Ubuntu 4.2.4-1ubuntu4))
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_smb2-time: Protocol negotiation failed (SMB2)
| smb-os-discovery: 
|   OS: Unix (Samba 3.0.20-Debian)
|   Computer name: lame
|   NetBIOS computer name: 
|   Domain name: hackthebox.gr
|   FQDN: lame.hackthebox.gr
|_  System time: 2022-10-13T19:26:53-04:00
|_clock-skew: mean: 1h59m40s, deviation: 2h49m43s, median: -20s
```

**Findings**

FTP can be logged into anonymously. 

### FTP enumeration
```
Connected to 10.10.10.3.
220 (vsFTPd 2.3.4)
Name (10.10.10.3:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||14211|).
150 Here comes the directory listing.
226 Directory send OK.

```

Send the information to a a listening port 

>The server received the EPSV command. The server successfully opened a data socket, and is listening on the socket. The IP address associated with the listening socket is the same as the IP address used for the control connection.
>port_number is the port number associated with the listening data socket.
>**System action**
>The FTP server continues processing commands on the control connection. The server expects the client to create a data socket and connect it to the IP address of the control connection and port number indicated in the EPSV reply.

Used `ls -al` and now files shown.

```bash
ftp> pwd
Remote directory: /

```

### SMB enumeration

Command
```bash
smbmap -H $IP 
```

Result
```bash
[+] IP: 10.10.10.3:445  Name: 10.10.10.3                                        
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        print$                                                  NO ACCESS       Printer Drivers
        tmp                                                     READ, WRITE     oh noes!
        opt                                                     NO ACCESS
        IPC$                                                    NO ACCESS       IPC Service (lame server (Samba 3.0.20-Debian))
        ADMIN$                                                  NO ACCESS       IPC Service (lame server (Samba 3.0.20-Debian))

```

**Findings**
I may have read/write access to tmp 
couldnt do anything with is

---
## Foothold
---
Research the version of samba. Find a CVE on search 

![[Pasted image 20221013202916.png]]

Use metasploit 

>![[Pasted image 20221013203110.png]]

Set RHOST and LHOST and EXPLOIT

>![[Pasted image 20221013203403.png]]

get shell

```bash
ls
bin
boot
cdrom
dev
etc
home
initrd
initrd.img
initrd.img.old
lib
lost+found
media
mnt
nohup.out
opt
proc
root
sbin
srv
sys
tmp
usr
var
vmlinuz
vmlinuz.old
```

cd to root. see root.txt. cat it. found flag
```bash
cd /root
ls
Desktop
reset_logs.sh
root.txt
vnc.log
cat root.txt
809abbfb56b34b3816a22a1d58e07a59
```


---
## Flags
root.txt
```bash
809abbfb56b34b3816a22a1d58e07a59
```

---
## Tags
---
#metasploit #samba