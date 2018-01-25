#!/usr/bin/python
#coding:utf8
import os

web_url='u2:30080'

def Curl(wb):
  for i in range(1,10000):
    os.system('curl {wu}'.format(wu=wb))
    os.system('sleep 1')



Curl(web_url)
