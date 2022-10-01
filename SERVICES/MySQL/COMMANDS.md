
# mysql Commands
---
## MySQL command-line client Commands
---


Connect to MySQL server using mysql  command-line client with a username and password (MySQL will prompt for a password):

```bash
mysql -u [username] -p;
```

Code language: SQL (Structured Query Language) (sql)

Connect to MySQL Server with a specified database using a username and password:

`mysql -u [username] -p [database];`

Code language: SQL (Structured Query Language) (sql)

Exit mysql command-line client:

`exit;`

Code language: SQL (Structured Query Language) (sql)

[Export data using mysqldump tool](https://www.mysqltutorial.org/how-to-backup-database-using-mysqldump.aspx)

`mysqldump -u [username] -p [database] > data_backup.sql;`

Code language: SQL (Structured Query Language) (sql)

To clear MySQL screen console window on Linux, you use the following command:

`mysql> system clear;`

Code language: SQL (Structured Query Language) (sql)

Currently, there is no command available on Windows OS for clearing MySQL screen console window.

## Working with databases

[Create a database](https://www.mysqltutorial.org/mysql-create-drop-database.aspx) with a specified name if it does not exist in the database server

`CREATE DATABASE [IF NOT EXISTS] database_name;`

Code language: SQL (Structured Query Language) (sql)

Use a database or change the current database to another database that you are working with:

`USE database_name;`

Code language: SQL (Structured Query Language) (sql)

Drop a database with a specified name permanently. All physical files associated with the database will be deleted.

`DROP DATABASE [IF EXISTS] database_name;`

Code language: SQL (Structured Query Language) (sql)

Show all available databases in the current MySQL database server

`SHOW DATABASE;`

Code language: SQL (Structured Query Language) (sql)

## Working with tables

Show all tables in a current database.

`SHOW TABLES;`

Code language: SQL (Structured Query Language) (sql)

[Create a new table](https://www.mysqltutorial.org/mysql-create-table/)

`CREATE TABLE [IF NOT EXISTS] table_name(   column_list );`

Code language: SQL (Structured Query Language) (sql)

[Add a new column](https://www.mysqltutorial.org/mysql-add-column/) into a table:

`ALTER TABLE table  ADD [COLUMN] column_name;`

Code language: SQL (Structured Query Language) (sql)

[Drop a column](https://www.mysqltutorial.org/mysql-drop-column/) from a table:

`ALTER TABLE table_name DROP [COLUMN] column_name;`

Code language: SQL (Structured Query Language) (sql)

Add index with a specific name to a table on a column:

`ALTER TABLE table  ADD INDEX [name](column, ...);`

Code language: SQL (Structured Query Language) (sql)

Add [primary key](https://www.mysqltutorial.org/mysql-primary-key/) into a table:

`ALTER TABLE table_name  ADD PRIMARY KEY (column_name,...);`

Remove the primary key of a table:

`ALTER TABLE table_name DROP PRIMARY KEY;`

[Drop a table](https://www.mysqltutorial.org/mysql-drop-table):

`DROP TABLE [IF EXISTS] table_name;`

Code language: SQL (Structured Query Language) (sql)

[Show the columns](https://www.mysqltutorial.org/mysql-show-columns/) of a table:

`DESCRIBE table_name;`

Code language: SQL (Structured Query Language) (sql)

Show the information of a column in a table:

`DESCRIBE table_name column_name;`

Code language: SQL (Structured Query Language) (sql)

## Working with indexes

[Creating an index](https://www.mysqltutorial.org/mysql-index/mysql-create-index/) with the specified name on a table:

`CREATE INDEX index_name ON table_name (column,...);`

Code language: SQL (Structured Query Language) (sql)

[Drop an index](https://www.mysqltutorial.org/mysql-index/mysql-drop-index/):

`DROP INDEX index_name;`

Code language: SQL (Structured Query Language) (sql)

[Create a unique index](https://www.mysqltutorial.org/mysql-unique/):

`CREATE UNIQUE INDEX index_name  ON table_name (column,...);`

Code language: SQL (Structured Query Language) (sql)

## Working with views

Create a new view:

`CREATE VIEW [IF NOT EXISTS] view_name  AS    select_statement;`

Code language: SQL (Structured Query Language) (sql)

Create a new view with the `WITH CHECK OPTION`:

`CREATE VIEW [IF NOT EXISTS] view_name  AS select_statement WITH CHECK OPTION;`

Code language: SQL (Structured Query Language) (sql)

Create or replace a view:

`CREATE OR REPLACE view_name  AS  select_statement;`

Code language: SQL (Structured Query Language) (sql)

Drop a view:

`DROP VIEW [IF EXISTS] view_name;`

Code language: SQL (Structured Query Language) (sql)

Drop multiple views:

`DROP VIEW [IF EXISTS] view1, view2, ...;`

Code language: SQL (Structured Query Language) (sql)

Rename a view:

`RENAME TABLE view_name TO new_view_name;`

Code language: SQL (Structured Query Language) (sql)

Show views from a database:

`SHOW FULL TABLES [{FROM | IN } database_name] WHERE table_type = 'VIEW';`

Code language: SQL (Structured Query Language) (sql)

## Working with triggers

Create a new trigger:

`CREATE TRIGGER trigger_name {BEFORE | AFTER} {INSERT | UPDATE| DELETE } ON table_name FOR EACH ROW trigger_body;`

Code language: SQL (Structured Query Language) (sql)

Drop a trigger:

`DROP TRIGGER [IF EXISTS] trigger_name;`

Code language: SQL (Structured Query Language) (sql)

Show triggers in a database:

`SHOW TRIGGERS [{FROM | IN} database_name] [LIKE 'pattern' | WHERE search_condition];`

Code language: SQL (Structured Query Language) (sql)

## Working with stored procedures

Create a stored procedure:

`DELIMITER $$  CREATE PROCEDURE procedure_name(parameter_list) BEGIN    body; END $$  DELIMITER ;`

Code language: SQL (Structured Query Language) (sql)

Drop a stored procedure:

`DROP PROCEDURE [IF EXISTS] procedure_name;`

Code language: SQL (Structured Query Language) (sql)

Show stored procedures:

`SHOW PROCEDURE STATUS  [LIKE 'pattern' | WHERE search_condition];`

Code language: SQL (Structured Query Language) (sql)

## Working with stored functions

Create a new stored function:

`DELIMITER $$   CREATE FUNCTION function_name(parameter_list) RETURNS datatype [NOT] DETERMINISTIC BEGIN  -- statements END $$   DELIMITER ;`

Code language: SQL (Structured Query Language) (sql)

Drop a stored function:

`DROP FUNCTION [IF EXISTS] function_name;`

Code language: SQL (Structured Query Language) (sql)

Show stored functions:

`SHOW FUNCTION STATUS  [LIKE 'pattern' | WHERE search_condition];`

Code language: SQL (Structured Query Language) (sql)

## Querying data from tables

[Query all data](https://www.mysqltutorial.org/mysql-select-statement-query-data.aspx) from a table:

`SELECT * FROM table_name;`

Code language: SQL (Structured Query Language) (sql)

Query data from one or more column of a table:

`SELECT      column1, column2, ... FROM      table_name;`

Code language: SQL (Structured Query Language) (sql)

Remove duplicate rows from the result of a query:

`SELECT      DISTINCT (column) FROM     table_name;`

Code language: SQL (Structured Query Language) (sql)

Query data with a filter using a `[WHERE](https://www.mysqltutorial.org/mysql-where/)` clause:

`SELECT select_list FROM table_name WHERE condition;`

Code language: SQL (Structured Query Language) (sql)

Change the output of the column name using [column alias](https://www.mysqltutorial.org/mysql-alias/):

`SELECT      column1 AS alias_name,     expression AS alias,     ... FROM      table_name;`

Code language: SQL (Structured Query Language) (sql)

Query data from multiple tables using [inner join](https://www.mysqltutorial.org/mysql-inner-join.aspx):

`SELECT select_list FROM table1 INNER JOIN table2 ON condition;`

Code language: SQL (Structured Query Language) (sql)

Query data from multiple tables using [left join](https://www.mysqltutorial.org/mysql-left-join.aspx):

`SELECT select_list FROM table1  LEFT JOIN table2 ON condition;`

Code language: SQL (Structured Query Language) (sql)

Query data from multiple tables using [right join](https://www.mysqltutorial.org/mysql-right-join/):

`SELECT select_list  FROM table1  RIGHT JOIN table2 ON condition;`

Code language: SQL (Structured Query Language) (sql)

Make a Cartesian product of rows:

`SELECT select_list FROM table1 CROSS JOIN table2;`

Code language: SQL (Structured Query Language) (sql)

[Counting rows](https://www.mysqltutorial.org/mysql-count/) in a table.

`SELECT COUNT(*) FROM table_name;`

Code language: SQL (Structured Query Language) (sql)

Sorting a result set:

`SELECT      select_list FROM      table_name ORDER BY      column1 ASC [DESC],      column2 ASC [DESC];`

Code language: SQL (Structured Query Language) (sql)

Group rows using the [`GROUP BY`](https://www.mysqltutorial.org/mysql-group-by.aspx) clause.

`SELECT select_list FROM table_name GROUP BY column_1, column_2, ...;`

Code language: SQL (Structured Query Language) (sql)

Filter group using the `[HAVING](https://www.mysqltutorial.org/mysql-having.aspx)` clause:

`SELECT select_list FROM table_name GROUP BY column1 HAVING condition;`

Code language: SQL (Structured Query Language) (sql)

## Modifying data in tables

[Insert a new row](https://www.mysqltutorial.org/mysql-insert-statement.aspx) into a table:

`INSERT INTO table_name(column_list) VALUES(value_list);`

Code language: SQL (Structured Query Language) (sql)

[Insert multiple rows](https://www.mysqltutorial.org/mysql-insert-multiple-rows/) into a table:

`INSERT INTO table_name(column_list) VALUES(value_list1),       (value_list2),       (value_list3),       ...;`

Code language: SQL (Structured Query Language) (sql)

[Update](https://www.mysqltutorial.org/mysql-update-data.aspx) all rows in a table:

`UPDATE table_name SET column1 = value1,     ...;`

Code language: SQL (Structured Query Language) (sql)

Update data for a set of rows specified by a condition in `WHERE` clause.

`UPDATE table_name SET column_1 = value_1,     ... WHERE condition`

Code language: SQL (Structured Query Language) (sql)

[Update with join](https://www.mysqltutorial.org/mysql-update-join/)

`UPDATE      table1,      table2 INNER JOIN table1 ON table1.column1 = table2.column2 SET column1 = value1, WHERE condition;`

Code language: SQL (Structured Query Language) (sql)

[Delete all rows in a table](https://www.mysqltutorial.org/mysql-delete-statement.aspx)

`DELETE FROM table_name;`

Code language: SQL (Structured Query Language) (sql)

Delete rows specified by a condition:

`DELETE FROM table_name WHERE condition;`

Code language: SQL (Structured Query Language) (sql)

[Delete with join](https://www.mysqltutorial.org/mysql-delete-join/)

`DELETE table1, table2 FROM table1 INNER JOIN table2     ON table1.column1 = table2.column2 WHERE condition;`

Code language: SQL (Structured Query Language) (sql)

## Searching

Search for data using the `[LIKE](https://www.mysqltutorial.org/mysql-like/)` operator:

`SELECT select_list FROM table_name WHERE column LIKE '%pattern%';`

Code language: SQL (Structured Query Language) (sql)

Text search using a [regular expression](https://www.mysqltutorial.org/mysql-regular-expression-regexp.aspx) with `RLIKE` operator.

`SELECT select_list FROM table_name WHERE column RLIKE 'regular_expression';`

Code language: SQL (Structured Query Language) (sql)


---
## MAN
---
```bash
mysql  Ver 15.1 Distrib 10.6.8-MariaDB, for debian-linux-gnu (x86_64) using  EditLine wrapper
Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Usage: mysql [OPTIONS] [database]

Default options are read from the following files in the given order:
/etc/my.cnf /etc/mysql/my.cnf ~/.my.cnf 
The following groups are read: mysql mariadb-client client client-server client-mariadb
The following options may be given as the first argument:
--print-defaults          Print the program argument list and exit.
--no-defaults             Don't read default options from any option file.
The following specify which files/extra groups are read (specified before remaining options):
--defaults-file=#         Only read default options from the given file #.
--defaults-extra-file=#   Read this file after the global files are read.
--defaults-group-suffix=# Additionally read default groups with # appended as a suffix.

  -?, --help          Display this help and exit.
  -I, --help          Synonym for -?
  --abort-source-on-error 
                      Abort 'source filename' operations in case of errors
  --auto-rehash       Enable automatic rehashing. One doesn't need to use
                      'rehash' to get table and field completion, but startup
                      and reconnecting may take a longer time. Disable with
                      --disable-auto-rehash.
                      (Defaults to on; use --skip-auto-rehash to disable.)
  -A, --no-auto-rehash 
                      No automatic rehashing. One has to use 'rehash' to get
                      table and field completion. This gives a quicker start of
                      mysql and disables rehashing on reconnect.
  --auto-vertical-output 
                      Automatically switch to vertical output mode if the
                      result is wider than the terminal width.
  -B, --batch         Don't use history file. Disable interactive behavior.
                      (Enables --silent.)
  --binary-as-hex     Print binary data as hex
  --character-sets-dir=name 
                      Directory for character set files.
  --column-type-info  Display column type information.
  -c, --comments      Preserve comments. Send comments to the server. The
                      default is --skip-comments (discard comments), enable
                      with --comments.
  -C, --compress      Use compression in server/client protocol.
  -#, --debug[=#]     This is a non-debug version. Catch this and exit.
  --debug-check       Check memory and open file usage at exit.
  -T, --debug-info    Print some debug info at exit.
  -D, --database=name Database to use.
  --default-character-set=name 
                      Set the default character set.
  --delimiter=name    Delimiter to be used.
  -e, --execute=name  Execute command and quit. (Disables --force and history
                      file.)
  -E, --vertical      Print the output of a query (rows) vertically.
  -f, --force         Continue even if we get an SQL error. Sets
                      abort-source-on-error to 0
  -G, --named-commands 
                      Enable named commands. Named commands mean this program's
                      internal commands; see mysql> help . When enabled, the
                      named commands can be used from any line of the query,
                      otherwise only from the first line, before an enter.
                      Disable with --disable-named-commands. This option is
                      disabled by default.
  -i, --ignore-spaces Ignore space after function names.
  --init-command=name SQL Command to execute when connecting to MariaDB server.
                      Will automatically be re-executed when reconnecting.
  --local-infile      Enable/disable LOAD DATA LOCAL INFILE.
  -b, --no-beep       Turn off beep on error.
  -h, --host=name     Connect to host.
  -H, --html          Produce HTML output.
  -X, --xml           Produce XML output.
  --line-numbers      Write line numbers for errors.
                      (Defaults to on; use --skip-line-numbers to disable.)
  -L, --skip-line-numbers 
                      Don't write line number for errors.
  -n, --unbuffered    Flush buffer after each query.
  --column-names      Write column names in results.
                      (Defaults to on; use --skip-column-names to disable.)
  -N, --skip-column-names 
                      Don't write column names in results.
  --sigint-ignore     Ignore SIGINT (CTRL-C).
  -o, --one-database  Ignore statements except those that occur while the
                      default database is the one named at the command line.
  --pager[=name]      Pager to use to display results. If you don't supply an
                      option, the default pager is taken from your ENV variable
                      PAGER. Valid pagers are less, more, cat [> filename],
                      etc. See interactive help (\h) also. This option does not
                      work in batch mode. Disable with --disable-pager. This
                      option is disabled by default.
  -p, --password[=name] 
                      Password to use when connecting to server. If password is
                      not given it's asked from the tty.
  -P, --port=#        Port number to use for connection or 0 for default to, in
                      order of preference, my.cnf, $MYSQL_TCP_PORT,
                      /etc/services, built-in default (3306).
  --progress-reports  Get progress reports for long running commands (like
                      ALTER TABLE)
                      (Defaults to on; use --skip-progress-reports to disable.)
  --prompt=name       Set the command line prompt to this value.
  --protocol=name     The protocol to use for connection (tcp, socket, pipe).
  -q, --quick         Don't cache result, print it row by row. This may slow
                      down the server if the output is suspended. Doesn't use
                      history file.
  -r, --raw           Write fields without conversion. Used with --batch.
  --reconnect         Reconnect if the connection is lost. Disable with
                      --disable-reconnect. This option is enabled by default.
                      (Defaults to on; use --skip-reconnect to disable.)
  -s, --silent        Be more silent. Print results with a tab as separator,
                      each row on new line.
  -S, --socket=name   The socket file to use for connection.
  --ssl               Enable SSL for connection (automatically enabled with
                      other flags).
  --ssl-ca=name       CA file in PEM format (check OpenSSL docs, implies
                      --ssl).
  --ssl-capath=name   CA directory (check OpenSSL docs, implies --ssl).
  --ssl-cert=name     X509 cert in PEM format (implies --ssl).
  --ssl-cipher=name   SSL cipher to use (implies --ssl).
  --ssl-key=name      X509 key in PEM format (implies --ssl).
  --ssl-crl=name      Certificate revocation list (implies --ssl).
  --ssl-crlpath=name  Certificate revocation list path (implies --ssl).
  --tls-version=name  TLS protocol version for secure connection.
  --ssl-verify-server-cert 
                      Verify server's "Common Name" in its cert against
                      hostname used when connecting. This option is disabled by
                      default.
  -t, --table         Output in table format.
  --tee=name          Append everything into outfile. See interactive help (\h)
                      also. Does not work in batch mode. Disable with
                      --disable-tee. This option is disabled by default.
  -u, --user=name     User for login if not current user.
  -U, --safe-updates  Only allow UPDATE and DELETE that uses keys.
  -U, --i-am-a-dummy  Synonym for option --safe-updates, -U.
  -v, --verbose       Write more. (-v -v -v gives the table output format).
  -V, --version       Output version information and exit.
  -w, --wait          Wait and retry if connection is down.
  --connect-timeout=# Number of seconds before connection timeout.
  --max-allowed-packet=# 
                      The maximum packet length to send to or receive from
                      server.
  --net-buffer-length=# 
                      The buffer size for TCP/IP and socket communication.
  --select-limit=#    Automatic limit for SELECT when using --safe-updates.
  --max-join-size=#   Automatic limit for rows in a join when using
                      --safe-updates.
  --secure-auth       Refuse client connecting to server if it uses old
                      (pre-4.1.1) protocol.
  --server-arg=name   Send embedded server this as a parameter.
  --show-warnings     Show warnings after every statement.
  --plugin-dir=name   Directory for client-side plugins.
  --default-auth=name Default authentication client-side plugin to use.
  --binary-mode       Binary mode allows certain character sequences to be
                      processed as data that would otherwise be treated with a
                      special meaning by the parser. Specifically, this switch
                      turns off parsing of all client commands except \C and
                      DELIMITER in non-interactive mode (i.e., when binary mode
                      is combined with either 1) piped input, 2) the --batch
                      mysql option, or 3) the 'source' command). Also, in
                      binary mode, occurrences of '\r\n' and ASCII '\0' are
                      preserved within strings, whereas by default, '\r\n' is
                      translated to '\n' and '\0' is disallowed in user input.
  --connect-expired-password 
                      Notify the server that this client is prepared to handle
                      expired password sandbox mode even if --batch was
                      specified.

Variables (--variable-name=value)
and boolean options {FALSE|TRUE}  Value (after reading options)
--------------------------------- ----------------------------------------
abort-source-on-error             FALSE
auto-rehash                       TRUE
auto-vertical-output              FALSE
binary-as-hex                     FALSE
character-sets-dir                (No default value)
column-type-info                  FALSE
comments                          FALSE
compress                          FALSE
debug-check                       FALSE
debug-info                        FALSE
database                          (No default value)
default-character-set             auto
delimiter                         ;
vertical                          FALSE
force                             FALSE
named-commands                    FALSE
ignore-spaces                     FALSE
init-command                      (No default value)
local-infile                      FALSE
no-beep                           FALSE
host                              (No default value)
html                              FALSE
xml                               FALSE
line-numbers                      TRUE
unbuffered                        FALSE
column-names                      TRUE
sigint-ignore                     FALSE
port                              0
progress-reports                  TRUE
prompt                            \N [\d]> 
protocol                          
quick                             FALSE
raw                               FALSE
reconnect                         TRUE
socket                            /run/mysqld/mysqld.sock
ssl                               FALSE
ssl-ca                            (No default value)
ssl-capath                        (No default value)
ssl-cert                          (No default value)
ssl-cipher                        (No default value)
ssl-key                           (No default value)
ssl-crl                           (No default value)
ssl-crlpath                       (No default value)
tls-version                       (No default value)
ssl-verify-server-cert            FALSE
table                             FALSE
user                              (No default value)
safe-updates                      FALSE
i-am-a-dummy                      FALSE
connect-timeout                   0
max-allowed-packet                16777216
net-buffer-length                 16384
select-limit                      1000
max-join-size                     1000000
secure-auth                       FALSE
show-warnings                     FALSE
plugin-dir                        (No default value)
default-auth                      (No default value)
binary-mode                       FALSE
connect-expired-password          FALSE
```

---
