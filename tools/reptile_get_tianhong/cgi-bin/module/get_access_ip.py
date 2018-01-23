#!/usr/bin/python
#coding:utf-8
import re
logfile='/var/log/nginx/access.log' #设置日志文件路径
f1=open(logfile,'r')
all_content=f1.read()
class getip():
    def ipinfo(self):
        return re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',all_content)[-1] #返回日志文件里最后一个IP