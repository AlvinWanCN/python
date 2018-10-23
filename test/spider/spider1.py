#!/usr/bin/python
#coding:utf-8
import json
import urllib2,re
import time
from lxml import etree
#response = urllib2.urlopen("http://www.baidu.com")
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#print sys.getdefaultencoding()
#定义ip地址
#ip='47.75.70.80'
ip='112.13.74.69'
#get response
#response = urllib2.urlopen("http://www.114best.com/ip/114.aspx?w=%s"%ip)
response = urllib2.urlopen("http://ip.taobao.com/service/getIpInfo.php?ip=%s"%ip)

#read response and decode
content = response.read().decode('utf-8')

html=etree.HTML(content)
#用xpath去找指定内容，xpath地址可以用谷歌浏览器按f12后找到。
# content_list=html.xpath('//*[@id="json"]/ul/li[2]/div/ul/li[5]/div/span[1]')
# print(content)
citydict=json.loads(content)

#获取最终城市地址
city=str(citydict['data']['city'])
#打印城市地址
if re.search('省', city):
    city = (re.findall(r'省(.*)', city)[0])
if city == 'XX':
    city = str(citydict['data']['region'])
weather_url='https://www.sojson.com/open/api/weather/json.shtml?city=%s'%city

weather_response=urllib2.urlopen(weather_url)
weather_content=weather_response.read().decode('utf-8')

dicinfo=json.loads(weather_content)
try:
    city=dicinfo['city']
except Exception as e :
    print('对不起，获取不到您当前地区的天气。')
    exit(1)
shidu=dicinfo['data']['shidu']
forecast=dicinfo['data']['forecast']
date=forecast[0]['date']
high=forecast[0]['high']
low=forecast[0]['low']
fx=forecast[0]['fx']
fl=forecast[0]['fl']
type=forecast[0]['type']
notice=forecast[0]['notice']
aqi=str(forecast[0]['aqi'])

month=re.findall(r'0*(.*)',time.strftime('%m'))[0]
forecast=dicinfo['data']['forecast']
weather_dict0={}

weather_dict0['shidu']=dicinfo['data']['shidu']
weather_dict0['date']=forecast[0]['date']
weather_dict0['high']=forecast[0]['high']
weather_dict0['low']=forecast[0]['low']
weather_dict0['fx']=forecast[0]['fx']
weather_dict0['fl']=forecast[0]['fl']
weather_dict0['type']=forecast[0]['type']
weather_dict0['notice']=forecast[0]['notice']
weather_dict0['aqi']=forecast[0]['aqi']
weather_dict0['month']=month
weather_dict0['city']=city
weather_dict0['ganmao']=dicinfo['data']['ganmao']


weather_dict1={}
weather_dict1['high']=forecast[1]['high']
weather_dict1['low']=forecast[1]['low']
weather_dict1['fx']=forecast[1]['fx']
weather_dict1['fl']=forecast[1]['fl']
weather_dict1['type']=forecast[1]['type']
weather_dict1['notice']=forecast[1]['notice']
weather_dict1['aqi']=forecast[1]['aqi']
weather_dict1['date']=forecast[1]['date']
weather_dict1['city']=city


weather_dict2={}
weather_dict2['high']=forecast[2]['high']
weather_dict2['low']=forecast[2]['low']
weather_dict2['fx']=forecast[2]['fx']
weather_dict2['fl']=forecast[2]['fl']
weather_dict2['type']=forecast[2]['type']
weather_dict2['notice']=forecast[2]['notice']
weather_dict2['aqi']=forecast[2]['aqi']
weather_dict2['date']=forecast[2]['date']
weather_dict2['city']=city


weather_dict3={}
weather_dict3['high']=forecast[3]['high']
weather_dict3['low']=forecast[3]['low']
weather_dict3['fx']=forecast[3]['fx']
weather_dict3['fl']=forecast[3]['fl']
weather_dict3['type']=forecast[3]['type']
weather_dict3['notice']=forecast[3]['notice']
weather_dict3['aqi']=forecast[3]['aqi']
weather_dict3['date']=forecast[3]['date']
weather_dict3['city']=city



weather_dict4={}
weather_dict4['high']=forecast[4]['high']
weather_dict4['low']=forecast[4]['low']
weather_dict4['fx']=forecast[4]['fx']
weather_dict4['fl']=forecast[4]['fl']
weather_dict4['type']=forecast[4]['type']
weather_dict4['notice']=forecast[4]['notice']
weather_dict4['aqi']=forecast[4]['aqi']
weather_dict4['date']=forecast[4]['date']
weather_dict4['city']=city



#print(forecast)

print('今天是{month}月{date}, {city}的天气是{type}, 空气质量指数(AQI)是{aqi}, 湿度:{shidu}, {high}, {low}, {fx}{fl}, {ganmao},{notice}。</br></br>\n\n').format(**weather_dict0)  \
    +  ('{date}, 天气是{type}, 空气质量指数(AQI)是{aqi}, {high}, {low}, {fx}{fl}, {notice}。</br>\n').format(**weather_dict1)  \
    +  ('{date}, 天气是{type}, 空气质量指数(AQI)是{aqi}, {high}, {low}, {fx}{fl}, {notice}。</br>\n').format(**weather_dict2)  \
    + ('{date}, 天气是{type}, 空气质量指数(AQI)是{aqi}, {high}, {low}, {fx}{fl}, {notice}。</br>\n').format(**weather_dict3) \
    + ('{date}, 天气是{type}, 空气质量指数(AQI)是{aqi}, {high}, {low}, {fx}{fl}, {notice}。</br>\n').format(**weather_dict4)


#print('{high},{low})'.format(**weather_dict4))