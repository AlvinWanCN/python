#!/usr/bin/python
#coding:utf-8
from get_access_ip import getip
import urllib.request,re
#gip=getip()
#print (gip.ipinfo())
content=urllib.request.urlopen("http://www.howbuy.com/fund/ajax/gmfund/valuation/valuationnav.htm?jjdm=000961").read().decode('utf-8')


#print(content)
#print(re.findall(r'con.*\">(.*)<',content)[1])
A=22.33333
print(float('%.2f' % (A)))