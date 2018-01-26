#!/usr/bin/python
#coding:utf-8
import os,re,time
logdir='E:\\'
newlogfile=logdir+'latest.log'
newlog=open(newlogfile,'r')

#send_mail(['alvin.wan@shenmintech.com'],'subject',newlog.read())

newlog.close()

import time,json


#print (old_database)
#cc='\n'.join(os.listdir(logdir))
#print cc
#print (re.findall(r'late.*',('\n'.join(os.listdir(logdir)))))

#print str(back)
#if os.path.exists(newlogfile):  print 'haha'

#!/usr/bin/python
#coding:utf-8
a={1:'alvin',2:'data'}
print (a)
print (json.dumps(a))