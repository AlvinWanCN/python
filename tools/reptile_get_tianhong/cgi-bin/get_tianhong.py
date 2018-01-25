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

response = urllib.request.urlopen("http://www.howbuy.com/fund/ajax/gmfund/valuation/valuationnav.htm?jjdm=000961")
content=response.read()
#print content
latestValue = re.findall(r'con_value con_value_\w+\">(.*)</',content.decode('utf-8'))[0]
latestPercent= re.findall(r'con_ratio_\w+\">(.*)</',content.decode('utf-8'))[0]

Nowtime=time.strftime('%Y-%m-%d %H:%M:%S')
#print(latestValue)
#print(latestPercent)
earnings = float(latestValue)*63351.09-80000


class usedb():
    f = fund_tab()
    def insert_db(self):
        self.f.value=latestValue
        self.f.percent=latestPercent
        self.f.date=time.strftime('%Y-%m-%d %H:%M:%S')
        self.f.save()
    def query_db(self):
        t_list=self.f.select().order_by(fund_tab.date.desc()).limit(1)
        for T in t_list:
            global last_value,last_date,last_percent
            last_value=T.value
            last_date=T.date
            last_percent=T.percent

db=usedb()
db.query_db()
db.insert_db()
#print(last_value)
try:
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
            上次访问IP地址：%s </br>
            上次天弘天弘沪深300指数估值：%s ， 涨幅是 %s 查询时间是 %s </br>
            最新天弘天弘沪深300指数估值：%s ， 涨幅是 %s 当前时间是 %s
            </p>
            <p>
                我的累计天弘基金收益：￥ %s </br>
                我的今日天弘基金收益：￥ %s
            </p>
            <p>
                Alvin Wan  
            </p>
        </body>
    </html>
    """
    finallyHtml=html%(access_ip,last_value,last_percent,last_date,latestValue,latestPercent,Nowtime,earnings,63351.09*float(latestPercent))
except Exception as e:
    print (e)
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
            上次天弘天弘沪深300指数估值：%s ， 涨幅是 %s 查询时间是 %s </br>
            最新天弘天弘沪深300指数估值：%s ， 涨幅是 %s 当前时间是 %s
            </p>
            <p>
                我的累计天弘基金收益：￥ %s </br>
                我的今日天弘基金收益：￥ %s
            </p>
            <p>
                Alvin Wan  
            </p>
        </body>
    </html>
    """
    finallyHtml=html%(last_value,last_percent,last_date,latestValue,latestPercent,Nowtime,earnings,63351.09*float(latestPercent))
finally:
    print("Content-type:text/html")
    print()
    print(finallyHtml)