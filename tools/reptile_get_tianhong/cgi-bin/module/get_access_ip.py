#!/usr/bin/python
#coding:utf-8
import re,time
time.sleep(2)
logfile='/var/log/nginx/access.log' #设置日志文件路径
#logfile='E:\\log.txt'
f1=open(logfile,'r')
all_content=f1.read()
class getip():
    def ipinfo(self):
        #print all_content
        return re.findall(r'\n(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s',all_content)[-1] #返回日志文件里最后一个IP