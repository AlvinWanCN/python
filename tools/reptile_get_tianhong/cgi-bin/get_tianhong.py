#!/usr/bin/python
#coding:utf-8

import urllib.request,re,time,json
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
thdict['latestValue'] = re.findall(r'con.*\">(.*)<',content)[0]
thdict['latestBenefit']= re.findall(r'con.*\">(.*)<',content)[1]
thdict['latestPercent']=re.findall(r'con.*\">(.*)<',content)[2]
thdict['Nowtime']=time.strftime('%Y-%m-%d %H:%M:%S')
thdict['date']=re.sub(r'\s','%20',time.strftime('%Y-%m-%d %H:%M:%S'))
thdict['earnings'] = '%.2f' % float(float(thdict['latestValue'])*totalFund-totalMoney)
thdict['todayEarnings']='%.2f' % float(totalFund*float(thdict['latestBenefit']))
thdict['insertUrl']='http://t.alv.pub/insert'
thdict['queryUrl']='http://t.alv.pub/query'
queryResult=json.loads(urllib.request.urlopen('{queryUrl}'.format_map(thdict)).read().decode('utf-8'))
thdict.update(queryResult)
#print (thdict)
json.loads(urllib.request.urlopen('{insertUrl}?value={latestValue}&percent={latestPercent}&date={date}'.format_map(thdict)).read().decode('utf-8'))

try:
    thdict['access_ip']=access_ip
    thdict['ipinfo']='上次访问IP地址：{access_ip} </br>'.format_map(thdict)
except:
    thdict['ipinfo']='Welcome'

html = """
<!DOCTYPE html>
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
        上次天弘沪深300指数估值：{lastValue} ， 涨幅是{lastPercent} 查询时间是 {lastDate} </br>
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
print("Content-type:text/html")
print()
print(html.format_map(thdict))
