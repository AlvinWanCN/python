#!/usr/bin/python
#coding:utf-8
import time
import hashlib
print(time.strftime('%Y %m-%d %H:%M:%S'))
password='wankaihao'
#print(hashlib.md5(password).hexdigest())

def md5(alpha):
    return hashlib.md5(alpha.encode('utf-8')).hexdigest()

print(md5('sophiroth'))