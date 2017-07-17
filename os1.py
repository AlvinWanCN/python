#!/usr/bin/python
#-*-coding:utf8-*-
import os,datetime
#os.getcwd()
#os.system('ls')
#a = os.path.isfile('yes')
#print a
os.system('name="alvin"')
#name = 'alvin'
#name = datetime.datetime.now.strftime('%Y-%m-%d %H:%M:%S')
#os.system('echo yes" "`date +%Y%m%d`" "Nameis${name}')
#os.system('echo {na}'.format(na=name))
#os.system('ls')
#os.mkdir('face')
'''

#var = 'ok'
#
#os.environ['yes']=str(var)
#os.system('echo $yes')

#a=os.system('ps aux|grep asda|grep ada|grep -v grep')
#print a
a = os.system('ls  &>/dev/null')
print a
'''
'''
import sys,os
oldSterr = None
logfile = None

try:
        logfile = open('/tmp/1.txt','w+')
        oldStderr = sys.stderr
        sys.stderr = logfile
        os.system('dialog --inputbox "Please input something text:" 10 40')
finally:
        if logfile:
           logfile.close()
'''
now = datetime.datetime.now()
a=now.strftime('%Y-%m-%d %H:%M:%S')  
print a
os.system('sleep 3')
b=now.strftime('%Y-%m-%d %H:%M:%S')  
print b
