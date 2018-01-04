#!/usr/bin/python
#coding:utf-8
import urllib2

#response = urllib2.urlopen("http://www.baidu.com")
response = urllib2.urlopen("http://localhost:8000")
print response.read()