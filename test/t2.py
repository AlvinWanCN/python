#!/usr/bin/python
#coding:utf-8
import os,re,time
logdir='E:\\'
newlogfile=logdir+'latest.log'
newlog=open(newlogfile,'r')

#send_mail(['alvin.wan@shenmintech.com'],'subject',newlog.read())

newlog.close()

import time,json


#print (old_database)
#cc='\n'.join(os.listdir(logdir))
#print cc
#print (re.findall(r'late.*',('\n'.join(os.listdir(logdir)))))

#print str(back)
#if os.path.exists(newlogfile):  print 'haha'

#!/usr/bin/python
#coding:utf-8
from lxml import etree
from  bs4 import BeautifulSoup as BS
import urllib.request
content = urllib.request.urlopen("http://www.howbuy.com/fund/ajax/gmfund/valuation/valuationnav.htm?jjdm=000961").read().decode('utf-8')
#print (content)
#html=etree.HTML(content)
#html = BS(content,'lxml')
content_list=BS(content,'lxml').find_all('span')
#print (content_list[0])
#print(re.findall(r'>(.*)<',str(content_list[0]))[0])

#print ( re.findall(r'con.*\">(.*)<',content)[0])

a=['a','b',3,4,'5']

for i in range(1,len(a)+1):
    print(i)