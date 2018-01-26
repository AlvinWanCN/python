#!/usr/bin/python
#coding:utf-8
from fundDB import useDB
import cgi,json

udb=useDB()
data = cgi.FieldStorage()
tvalue = data.getvalue("tvalue")
tpercent = data.getvalue("tpercent")
tdate=data.getvalue("tdate")
state = {"success":"True","code":0}

respense = json.dumps(state)
udb.insertDB(tvalue,tpercent,tdate)
#lastdata=udb.queryDB()
#print("Content-type:text/html")
print("Content-Type: application/json")
print()
print(respense)