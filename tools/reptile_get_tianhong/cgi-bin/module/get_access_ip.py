#!/usr/bin/python
#coding:utf-8
import re,time
import os
log1='/var/log/nginx/access.log'
log2='E:\\log.txt'
if os.path.exists(log1):
    logfile = log1
elif os.path.exists(log2):
    logfile = log2



class getip():
        def ipinfo(self):
            try:
                f1 = open(logfile, 'r')
                all_content = f1.read()
                #print all_content
                return re.findall(r'\n(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s',all_content)[-1] #返回日志文件里最后一个IP
            except:
                return False