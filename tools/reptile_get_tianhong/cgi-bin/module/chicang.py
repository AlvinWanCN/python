#!/usr/bin/python3
#coding:utf-8
import urllib.request,re
from  bs4 import BeautifulSoup as BS
from lxml import etree
baseurl="http://finance.sina.com.cn/fund/quotesold/000961/bc.shtml"
#baseurl='http://www.howbuy.com/fund/ajax/gmfund/valuation/valuationnav.htm?jjdm=000961'
content = urllib.request.urlopen(baseurl).read().decode('gb2312')
#print(content)
#content_list=BS(content,'lxml').find_all('td')
#print(len(content_list))
#print(content_list)

html=etree.HTML(content)
content_list=html.xpath('//*[@id="blue-chips-sh601318"]/td[1]/a')
content_list=html.xpath('//*[@id="blue-chips-sh601318"]/td[3]/span')
#for i in content_list:
print(len(content_list))
print(float(content_list[0].text))
print(content_list[0].tag)
print(content_list[0].attrib)
