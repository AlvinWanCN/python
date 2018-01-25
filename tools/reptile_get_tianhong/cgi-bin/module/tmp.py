#!/usr/bin/python
#coding:utf-8
import urllib.request,re
from get_access_ip import getip

gip=getip()
print (gip.ipinfo())
#thdict={}
#content = urllib.request.urlopen("http://www.howbuy.com/fund/ajax/gmfund/valuation/valuationnav.htm?jjdm=000961").read().decode('utf-8')

#thdict['latestValue'] = re.findall(r'con.*\">(.*)<',content)[0]
#print(type(re.findall(r'con.*\">(.*)<',content)))