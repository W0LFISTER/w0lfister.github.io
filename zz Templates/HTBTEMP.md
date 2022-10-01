---

---

# {{title}}
---
## Getting Started
---
Use command to set Target IP
```bash
IP='TARGETIP' ; echo $IP
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


```

---
## Foothold

---
## Lateral Movement

---
## Privilege Escalation

---
## Flags
user.text
```bash

```

root.txt
```bash

```

---
## Tags
---