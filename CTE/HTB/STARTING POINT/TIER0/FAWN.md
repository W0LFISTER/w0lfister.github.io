---
  ``
---

FAWN
---
## Getting Started
---
Use command to set Target IP
```bash
IP=10.129.195.205 ; echo $IP
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
nmap -sC -sV $IP -F | copy 
```

Results
```bash
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-29 17:44 EDT
Nmap scan report for 10.129.195.205
Host is up (0.028s latency).
Not shown: 99 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.80
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 0.99 seconds

```

**Finding**
```bash
ftp-anon: Anonymous FTP login allowed (FTP code 230)
```

>A typical misconfiguration for running FTP services allows an anonymous account to access the service like any other authenticated user. The anonymous username can be input when the prompt appears, followed by any password whatsoever since the service will disregard the password for this specific account.


---
### FTP ENUM
---

>The File Transfer Protocol (FTP) is a standard communication protocol used to transfer  computer files from a server to a client on a computer network. FTP is built on a client–server model architecture using separate control and data connections between  the client and the server. FTP users may authenticate themselves with a clear-text  sign-in protocol, generally in the form of a username and password. However, they can  connect anonymously if the server is configured to allow it. For secure transmission  that protects the username and password and encrypts the content, FTP is often secured  with SSL/TLS (FTPS) or replaced with SSH File Transfer Protocol (SFTP).

**FTP Commands**

| CMD | DETAILS                                                                                                                                                          |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|!| **This command toggles back and forth between the operating system and ftp.** Once back in the operating system, typing exit takes you back to the FTP command line. |
|_?_|Accesses the Help screen.|
| _append_ |Append text to a local file.||_ascii_Switch to ASCII transfer mode.
|_bell_|Turns bell mode on or off.
|_binary_|Switches to binary transfer mode.
|_bye_|Exits from FTP.
|_cd_|Changes directory.
|_close_|Exits from FTP.
|_delete_|Deletes a file.
|_debug_|Sets debugging on or off.
|_dir_|Lists files, if connected.  
|dir -C | lists the files in wide format.  
|dir -1 | Lists the files in bare format in alphabetic order.  
|dir -r | Lists directory in reverse alphabetic order.  
|dir -R | Lists all files in current directory and sub directories.  
|dir -S | Lists files in bare format in alphabetic order.|
|_disconnect_|Exits from FTP.
|_get_|Get file from the remote computer.
|_glob_|Sets globbing on or off. When turned off, the file name in the **put** and **get** commands is taken literally, and wildcards will not be looked at.
|_hash_|Sets hash mark printing on or off. When turned on, for each 1024 bytes of data received, a hash-mark (#) is displayed.|Accesses the Help screen and displays information about the command if the command is typed after help.
|_lcd_|Displays local directory if typed alone or if path typed after lcd will change the local directory.
|_literal_|Sends a literal command to the connected computer with an expected one-line response.
|_ls_|Lists files of the remotely connected computer.
|_mdelete_|Multiple delete.
|_mdir_|Lists contents of multiple remote directories.
|_mget_|Get multiple files.
|_mkdir_|Make directory.
|_mls_|Lists contents of multiple remote directories.
|_mput_|Send multiple files.
|_open_|Opens address.
|_prompt_|Enables or disables the prompt.
|_put_|Send one file.
|pwd|Print working directory.
|quit|Exits from FTP.
|_quote_|Same as the literal command.
|_recv_|Receive file.
|_remotehelp_|Get help from remote server.
|_rename_|Renames a file.
|_rmdir_|Removes a directory on the remote computer.
|_send_|Send single file.
|_status_|Shows status of currently enabled and disabled options.
|_trace_|Toggles packet tracing.
|type|Set file transfer type.
|_[user](https://www.serv-u.com/resource/tutorial/quit-user-abor-acct-syst-xdel-ftp-command)_|Send new user information.
|_verbose_|Sets verbose on or off.
#ftpcommands

Command
```bash
ftp $IP   
```

Result
```
Connected to 10.129.195.205.
220 (vsFTPd 3.0.3)
Name (10.129.195.205:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.

```

Notes
>Used the username anonymous. No password needed.


Command
```bash
ls
```

Result
```bash
229 Entering Extended Passive Mode (|||42337|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
226 Directory send OK.

```

Command
```bash
get flag.txt
```

Result
```bash
local: flag.txt remote: flag.txt
229 Entering Extended Passive Mode (|||61275|)
150 Opening BINARY mode data connection for flag.txt (32 bytes).
100% |******************************************************************************************************************************************************************|    32      801.28 KiB/s    00:00 ETA
226 Transfer complete.
32 bytes received in 00:00 (1.18 KiB/s)
```

Exit ftp

Command
```bash
cat flag.txt    
```

Result
```bash
035db21c881520061c53e0536e44f815
```
---
## Keys
---
user.text
```bash
035db21c881520061c53e0536e44f815
```
---
## Tags
---
#ftp #ftpnotes