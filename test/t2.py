#!/usr/bin/python
#coding:utf-8
import os,re
logdir='E:\\'
newlogfile=logdir+'latest.log'
newlog=open(newlogfile,'r')

#send_mail(['alvin.wan@shenmintech.com'],'subject',newlog.read())

newlog.close()




#print (old_database)
#cc='\n'.join(os.listdir(logdir))
#print cc
#print (re.findall(r'late.*',('\n'.join(os.listdir(logdir)))))

#print str(back)
#if os.path.exists(newlogfile):  print 'haha'

#!/usr/bin/python
#coding:utf-8
import os
alvin='tomath'
d={'alvin':'sophia','wan':'diana'}
#print d
html="""
yes
{alvin}
"""
#print html
print (html.format(alvin='natasha'))

#print (html.format(vars()))
People = {'name':'john', 'age':56}

print ('My name is {name},i am {age} old'.format_map(People))