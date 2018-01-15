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
    if re.findall(r'late*.txt',i):
        old_database=i

#print (old_database)
#cc='\n'.join(os.listdir(logdir))
#print cc
#print (re.findall(r'late.*',('\n'.join(os.listdir(logdir)))))
back= (re.findall(r'late.*','\n'.join(os.listdir(logdir))))
print str(back)
#if os.path.exists(newlogfile):  print 'haha'

