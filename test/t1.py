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


def makeAlvHost(hostname,ip):
    return\
        {'ip': ip, 'hostname': hostname+'.alv.pub'}
hostDict={}
hostDict['zabbix']=makeAlvHost('zabbix','51')
hostDict['db1']=makeAlvHost('db1','52')
hostDict['db2']=makeAlvHost('db2','53')
lastIPNumber='51'

'''
for i in hostDict:
    if lastIPNumber == i['ip']:
        os.system('hostname %s'%i['hostname'])
        os.system('echo %s > /etc/hostname'%i['hostname'])
        break

print(hostDict)
'''
for hostname in hostDict:
    if hostDict[hostname]['ip'] == lastIPNumber:
        print(hostDict[hostname]['hostname'])
        break