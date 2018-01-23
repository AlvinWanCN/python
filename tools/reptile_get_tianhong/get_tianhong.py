#!/usr/bin/python
#coding:utf-8

import urllib2,re

response = urllib2.urlopen("http://www.howbuy.com/fund/ajax/gmfund/valuation/valuationnav.htm?jjdm=000961")
content= response.read()
#print content
latestValue = re.findall(r'con_value con_value_up\">(.*)</',content)
latestPercent= re.findall(r'con_ratio_red\">(.*)</',content)

#print(latestValue)
#print(latestPercent)
earnings = float(latestValue[0])*63351.09-79930.07


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
        最新天弘天弘沪深300指数估值：%s
        </p>
        <p>
        今日天弘天弘沪深300指数涨幅：%s
        </p>
        <p>
           我的天弘基金收益： %s
        </p>
        <p>
            Alvin Wan
        </p>
        <p>
            雷利亭你看啥看
        </p>
    </body>
</html>

"""
print("Content-type:text/html")
print()
print(html%(latestValue,latestPercent,earnings))