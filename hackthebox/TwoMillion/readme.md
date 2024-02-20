# TwoMillion

10.129.35.170

## nmap

22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 3e:ea:45:4b:c5:d1:6d:6f:e2:d4:d1:3b:0a:3d:a9:4f (ECDSA)
|_  256 64:cc:75:de:4a:e6:a5:b4:73:eb:3f:1b:cf:b4:e3:94 (ED25519)
80/tcp open  http    nginx
|_http-title: Did not follow redirect to http://2million.htb/

## http 80

gobuster dir -e -u http://2million.htb/api/v1/invite -w /usr/share/seclists/Discovery/Web-Content/api/actions.txt -b 301


curl -X POST http://2million.htb/api/v1/invite/generate                                                            1 ⨯
{"0":200,"success":1,"data":{"code":"M0JGM00tMVFYRkgtUTZFU0ktVkVBT0k=","format":"encoded"}}                                              

## foothold

Enumerate /api/v1
Set admin with /api/v1/admin/settings/update
Command injection with /api/v1/admin/vpn/generate

## user

(remote) www-data@2million:/var/www/html$ cat .env
DB_HOST=127.0.0.1
DB_DATABASE=htb_prod
DB_USERNAME=admin
DB_PASSWORD=SuperDuperPass123

## root

/var/mail/admin
-> OverlayFS

https://github.com/xkaneiki/CVE-2023-0386/tree/main