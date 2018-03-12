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
    if weather_status:
        return weather_status
    else:
        return "unknow"

def get_max_temperature(): #获取最高气温
    #weather_max_temperature=re.findall(r'</b>(-?\d)<i>',str(content))[0]
    weather_max_temperature=html.xpath('//*[@id="wrap"]/div[4]/div[1]/div[3]/dl[1]/dd/ul/li[2]/span/text()')[0]
    if weather_max_temperature:
        return weather_max_temperature
    else:
        return "unknow"
def get_min_temperature():#获取最低气温
    weather_min__temperature=re.findall(r'</b>(-?\d+)<i>',str(content))[-1]
    if weather_min__temperature:
        return weather_min__temperature
    else:
        return "unknow"

#print (html.xpath('//*[@id="wrap"]/div[4]/div[1]/div[3]/dl[1]/dd/ul/li[2]/span/text()')[0])

print(get_status())
print(get_max_temperature())
print(get_min_temperature())
#print(content)