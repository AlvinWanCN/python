#!/usr/bin/python
#coding:utf-8
import urllib, urllib2, sys

class GetGoldPrice():
    host = 'http://jisugold.market.alicloudapi.com'
    path = '/gold/shgold'
    method = 'GET'
    appcode = '5ca26b23675f4b7f81b365d115184cdf'
    querys = ''
    bodys = {}
    url = host + path

    request = urllib2.Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    response = urllib2.urlopen(request)
    content = response.read()
    if (content):
    #print(content)
        gold_price = content.split('"price":"')[1].split('"')[0]
        price = "最新黄金价格是："+gold_price




if __name__ == "__main__":
    print(GetGoldPrice().price)