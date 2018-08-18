#!/usr/bin/python

import requests

username="xxxxx"
password="yyyyy"
dominio="zzzz.no-ip.info"
log="/no-ip-updater/ips.txt"

url ="http://"+username+":"+password+"@dynupdate.no-ip.com/nic/update?hostname="+dominio

r = requests.get(url)
print(r.content)

with open(log, "a") as myfile:
    myfile.write(r.content)
