#!/usr/bin/python
#coding:utf-8
import urllib.request

#response = urllib2.urlopen("http://www.baidu.com")
response = urllib.request.urlopen("http://localhost:8000")
print (response.read())