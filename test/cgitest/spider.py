#!/usr/bin/python
#coding:utf-8
import urllib
import urllib2

url = "http://localhost:8000/cgi-bin/register.py"

data = {
    "user":"sophia",
    "pawd":"natasha"
}
header = {
    ""
}
sendData =urllib.urlencode(data)

request = urllib2.Request(url,data = sendData,headers = header)
opener = url
#https://ke.qq.com/webcourse/index.html#course_id=199684&term_id=100236635&taid=1310961457892356&vid=k1419fu5o27