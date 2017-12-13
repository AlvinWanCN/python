#!/usr/bin/python
#_*_coding:utf-8_*_

import os

print(os.popen('df -h').read())

'''
for i in os.popen('df -h').readlines():
    print(i)
'''