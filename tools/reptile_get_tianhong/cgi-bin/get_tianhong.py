#!/usr/bin/python
# _*_ coding:utf-8 _*_
import urllib.request,re,time,json,os
from  bs4 import BeautifulSoup as BS
dirname=os.getcwd()
try:
    from module.get_access_ip import getip
    gip = getip()
    access_ip = gip.ipinfo()
except:
    pass
thdict={}
totalFund=75941.89
totalMoney=96000
content = urllib.request.urlopen("http://www.howbuy.com/fund/ajax/gmfund/valuation/valuationnav.htm?jjdm=000961").read().decode('utf-8')
#thdict['latestValue'] = re.findall(r'con.*\">(.*)<',content)[0]
#thdict['latestBenefit']= re.findall(r'con.*\">(.*)<',content)[1]
#thdict['latestPercent']=re.findall(r'con.*\">(.*)<',content)[2]
content_list=BS(content,'lxml').find_all('span')
thdict['latestValue'] =re.findall(r'>(.*)<',str(content_list[0]))[0]
thdict['latestBenefit']= re.findall(r'>(.*)<',str(content_list[1]))[0]
thdict['latestPercent']=re.findall(r'>(.*)<',str(content_list[2]))[0]
thdict['Nowtime']=time.strftime('%Y-%m-%d %H:%M:%S')
thdict['date']=re.sub(r'\s','%20',time.strftime('%Y-%m-%d %H:%M:%S'))
thdict['earnings'] = '%.2f' % float(float(thdict['latestValue'])*totalFund-totalMoney)
thdict['todayEarnings']='%.2f' % float(totalFund*float(thdict['latestBenefit']))
thdict['insertUrl']='http://t.alv.pub/insert'
thdict['queryUrl']='http://t.alv.pub/query'
thdict.update(json.loads(urllib.request.urlopen('{queryUrl}'.format_map(thdict)).read().decode('utf-8')))
#print (thdict)
urllib.request.urlopen('{insertUrl}?value={latestValue}&percent={latestPercent}&date={date}'.format_map(thdict)).read().decode('utf-8')
try:
    thdict['access_ip']=access_ip
    thdict['ipinfo']='上次访问IP地址：{access_ip} </br>'.format_map(thdict)
except:
    thdict['ipinfo']='Welcome </br>'
filename=os.getcwd()+'/tianhong.html'
if os.path.exists(filename):
    pass
else:
    filename=os.getcwd()+'/cgi-bin/tianhong.html'
htmlfile=open(filename,'r',encoding='UTF-8')
htmlcontent=htmlfile.read()
#print (htmlcontent)
htmlfile.close()
print("Content-type:text/html")
print()
print(htmlcontent.format_map(thdict))
