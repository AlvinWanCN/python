#!/usr/bin/python
#coding:utf-8
'''
import time
import hashlib
print(time.strftime('%Y %m-%d %H:%M:%S'))
password='wankaihao'
#print(hashlib.md5(password).hexdigest())

def md5(alpha):
    return hashlib.md5(alpha.encode('utf-8')).hexdigest()

print(md5('sophiroth'))
'''
import re
a='inet 192.168.127.78/24 brd 192.168.127.255 scope global dynamic ens32'
print(re.findall(r'\s(.*)\/',a))


