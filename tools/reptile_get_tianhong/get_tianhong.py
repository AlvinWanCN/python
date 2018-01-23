#!/usr/bin/python
#coding:utf-8

import urllib2,re

response = urllib2.urlopen("http://www.howbuy.com/fund/ajax/gmfund/valuation/valuationnav.htm?jjdm=000961")
content= response.read()
#print content
latestValue = re.findall(r'con_value con_value_up\">(.*)</',content)
latestPercent= re.findall(r'con_ratio_red\">(.*)</',content)

print(latestValue)
print(latestPercent)