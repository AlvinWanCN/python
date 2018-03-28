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
f1=open('F:/alvin.txt','r')
f1Content=f1.read()
print(f1Content)
print(re.sub(r'.*192.168.38.4.*','',f1Content))