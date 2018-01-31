#!/usr/bin/python3
#coding:utf-8
import urllib.request, sys
import ssl


host = 'https://fesms.market.alicloudapi.com'
path = '/sms/'
method = 'GET'
appcode = '4ca26b23675f4b7f81b365d115184cdf'
querys = 'code=895642&phone=13554856120&skin=12'
bodys = {}
url = host + path + '?' + querys

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)