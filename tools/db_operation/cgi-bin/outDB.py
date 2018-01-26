#!/usr/bin/python
#coding:utf-8
from fundDB import useDB
import cgi,json

udb=useDB()
#state = {"success":"True","code":0}
#respense = json.dumps(state)
lastdata=udb.queryDB()
last_value=lastdata[0]
lastPercent=lastdata[1]
last_date=lastdata[2].strftime('%Y-%m-%d %H:%M:%S')
state={"last_value":last_value,"lastPercent":lastPercent,"last_date":last_date}
respense = json.dumps(state)
#print (state)
#print("Content-type:text/html")
print("Content-Type: application/json")
print('')
print(respense)