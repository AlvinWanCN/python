#!/usr/bin/python3
#coding:utf-8
import urllib.request
import time,re,json

t={}
t['tvalue']=1.64423
t['tpercent']='0.33%'
t['tdate']=re.sub(r'\s','%20',time.strftime('%Y-%m-%d %H:%M:%S'))
#print (t['tdate'])
url='http://localhost/cgi-bin/inDB.py'

#content=json.loads(urllib.request.urlopen('http://localhost/cgi-bin/inDB.py?tvalue={tvalue}&tpercent={tpercent}&tdate={tdate}'.format_map(t)).read().decode('utf-8'))
#print (content)
#content=urllib.request.urlopen('http://localhost/cgi-bin/inDB.py?tvalue=1.276&tpercent=0.66%&tdate=2018-01-26 11:48:10').read().decode('utf-8')
#print (content['code'])
