#!/usr/bin/python
import urllib, urllib2, sys


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
    print(content)