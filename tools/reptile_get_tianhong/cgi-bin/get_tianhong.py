#!/usr/bin/python
#coding:utf-8

import urllib.request,re,time
from module.fundDB import fund_tab
try:
    from module.get_access_ip import getip
    gip = getip()
    access_ip = gip.ipinfo()
except:
    pass
thdict={}
content = urllib.request.urlopen("http://www.howbuy.com/fund/ajax/gmfund/valuation/valuationnav.htm?jjdm=000961").read().decode('utf-8')
thdict['latestValue'] = re.findall(r'con.*\">(.*)<',content)[0]
thdict['latestBenefit']= re.findall(r'con.*\">(.*)<',content)[1]
thdict['latestPercent']=re.findall(r'con.*\">(.*)<',content)[2]
thdict['Nowtime']=time.strftime('%Y-%m-%d %H:%M:%S')
thdict['earnings'] = '%.2f' % float(float(thdict['latestValue'])*63351.09-80000)
thdict['todayEarnings']='%.2f' % float(63351.09*float(thdict['latestBenefit']))

class usedb():
    f = fund_tab()
    def insert_db(self):
        self.f.value=thdict['latestValue']
        self.f.percent=thdict['latestPercent']
        self.f.date=time.strftime('%Y-%m-%d %H:%M:%S')
        self.f.save()
    def query_db(self):
        t_list=self.f.select().order_by(fund_tab.date.desc()).limit(1)
        for T in t_list:
            global last_value,last_date,latestPercent
            thdict['last_value']=T.value
            thdict['last_date'] =T.date
            thdict['lastPercent'] =T.percent
db=usedb()
db.query_db()
db.insert_db()
try:
    thdict['access_ip']=access_ip
    thdict['ipinfo']='上次访问IP地址：{access_ip} </br>'.format_map(thdict)
except:
    thdict['ipinfo']='Welcome'

html = """
<html>
    <head>
        <meta charset="UTF-8">
        <title>
        Alvin 天弘基金收益
        </title>
    </head>
    <body>
        <p>
        {ipinfo}
        上次天弘沪深300指数估值：{last_value} ， 涨幅是{lastPercent} 查询时间是 {last_date} </br>
        最新天弘沪深300指数估值：{latestValue} ， 涨幅是 {latestPercent} 当前时间是 {Nowtime}
        </p>
        <p>
            我的累计天弘基金收益：￥ {earnings} </br>
            我的今日天弘基金收益：￥ {todayEarnings}
        </p>
        <p>
            Alvin Wan  
        </p>
    </body>
</html>
"""
###
print("Content-type:text/html")
print()
print(html.format_map(thdict))
