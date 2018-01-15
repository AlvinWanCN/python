#!/usr/bin/python
#coding:utf-8
from used.pro_useful.sophiroth_email import send_mail
import os,re
logdir='E:\\'
newlogfile=logdir+'latest.log'
newlog=open(newlogfile,'r')

#send_mail(['alvin.wan@shenmintech.com'],'subject',newlog.read())

newlog.close()


for i in os.listdir(logdir) :
    if re.findall(r'late.*',i):
        old_database=i

print (old_database)