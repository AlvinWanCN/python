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
import os
import logging
import urllib2,time
from lxml import etree
import re,os,subprocess
host = 'http://tianqi.2345.com'
path = '/today-58362.htm'
url = host + path
content = urllib2.urlopen(url).read()
html = etree.HTML(content)
#本脚本兼容linux下python2

import sys

reload(sys)
sys.setdefaultencoding('utf8')

from selenium import webdriver

if 0 == 1 or 99 == 99:
    print 99