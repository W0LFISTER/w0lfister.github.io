### SMB Commands
  

**List shares on a machine using NULL Session**

```bash

smbclient -L <$IP>

```

**List shares on a machine using a valid username + password**

```bash

smbclient -L \<$IP\> -U username%password

```

**Connect to a valid share with username + password**

```bash

smbclient //\$IP/\<share$\> -U username%password

```

**List files on a specific share**

```bash

smbclient //\$IP/\<share$\> -c 'ls' password -U username

```

**List files on a specific share folder inside the share**

```bash

smbclient //\$IP/\<share$\> -c 'cd folder; ls' password -U username

```

**Download a file from a specific share folder**

```bash

smbclient //\$IP/\<share$\> -c 'cd folder;get desired_file_name' password -U username

```

**Copy a file to a specific share folder**

```bash

smbclient //\$IP/\<share$\> -c 'put /var/www/my_local_file.txt .\target_folder\target_file.txt' password -U username

```

**Create a folder in a specific share folder**

```bash

smbclient //\$IP/\<share$\> -c 'mkdir .\target_folder\new_folder' password -U username

```

**Rename a file in a specific share folder**

```bash

smbclient //\$IP/\<share$\> -c 'rename current_file.txt new_file.txt' password -U username

```

**enum4linux - General enumeration - anonymous session**

```bash

enum4linux -a \$IP

```

**enum4linux - General enumeration - authenticated session**

```bash

enum4linux -a \$IP -u \<user\> -p \<pass\>

```

**enum4linux - Users enumeration**

```bash

enum4linux -u \<user\> -p \<pass\> -U \$IP

```

**enum4linux - Group and members enumeration**

```bash

enum4linux -u \<user\> -p \<pass\> -G \$IP

```

**enum4linux - Password policy**

```bash

enum4linux -u \<user\> -p \<pass\> -P \$IP

```

**nmap - Enum Users**

```bash

nmap -p 445 --script smb-enum-users \$IP --script-args smbuser=username,smbpass=password,smbdomain=domain

nmap -p 445 --script smb-enum-users \$IP --script-args smbuser=username,smbhash=LM:NTLM,smbdomain=domain

nmap --script smb-enum-users.nse --script-args smbusername=User1,smbpass=Pass@1234,smbdomain=workstation -p445 192.168.1.10

nmap --script smb-enum-users.nse --script-args smbusername=User1,smbhash=aad3b435b51404eeaad3b435b51404ee:C318D62C8B3CA508DD753DDA8CC74028,smbdomain=mydomain -p445 192.168.1.10<br>

```

**nmap - Enum Groups**

```bash

nmap -p 445 --script smb-enum-groups \$IP --script-args smbuser=username,smbpass=password,smbdomain=domain

nmap -p 445 --script smb-enum-groups \$IP --script-args smbuser=username,smbhash=LM:NTLM,smbdomain=domain

```

**nmap - Enum Shares**

```bash

nmap -p 445 --script smb-enum-shares \$IP --script-args smbuser=username,smbpass=password,smbdomain=domain

nmap -p 445 --script smb-enum-shares \$IP --script-args smbuser=username,smbpass=LM:NTLM,smbdomain=domain

```

**nmap - OS Discovery**

```bash

nmap -p 445 --script smb-os-discovery \$IP

```

**nmap - SMB Vulnerabilities on Windows**

```bash

nmap -p 445 --script smb-vuln-ms06-025 $IP <br>

nmap -p 445 --script smb-vuln-ms07-029 $IP <br>

nmap -p 445 --script smb-vuln-ms08-067 $IP <br>

nmap -p 445 --script smb-vuln-ms10-054 $IP <br>

nmap -p 445 --script smb-vuln-ms10-061 $IP <br>

nmap -p 445 --script smb-vuln-ms17-010 $IP <br>

nmap -p 445 --script smb-vuln-cve-2017-7494 $IP <br>

```

map - Brute Force Accounts (be aware of account lockout!)

```bash

nmap –p 445 --script smb-brute –script-args userdb=user-list.txt,passdb=pass-list.txt $IP

```

#smbclient  #enum4linux #nmap4smb