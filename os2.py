#!/usr/bin/python
#coding:utf8

import os

#var = 'ok'
#
#os.environ['yes']=str(var)
#os.system('echo $yes')

#a=os.system('ps aux|grep asda|grep ada|grep -v grep')
#print a
a = os.system('ls  &>/dev/null')
print a
