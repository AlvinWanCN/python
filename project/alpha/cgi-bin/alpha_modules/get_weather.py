# _*_ coding:utf-8 _*_
import urllib.request
from lxml import etree
import re
host='http://tianqi.2345.com'
path='/today-58362.htm'
url=host + path
content=urllib.request.urlopen(url).read()
html=etree.HTML(content)
def get_status(): ##获取天气状况
    weather_status=html.xpath('//*[@id="wrap"]/div[4]/div[1]/div[3]/dl[1]/dd/ul/li[1]/span[2]')[0].text
    return weather_status

def get_max_temperature(): #获取最高气温
    weather_max_temperature=re.findall(r'</b>(-?\d)<i>',str(content))[0]
    return weather_max_temperature
def get_min_temperature():#获取最低气温
    weather_min__temperature=re.findall(r'</b>(-?\d)<i>',str(content))[1]
    return weather_min__temperature