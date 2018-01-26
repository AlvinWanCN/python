#!/usr/bin/python
#coding:utf-8
from fundDB import useDB
import cgi,json

udb=useDB()
data = cgi.FieldStorage()
tvalue = data.getvalue("tvalue")
tpercent = data.getvalue("tpercent")
tdate=data.getvalue("tdate")
success = {"success":"True","code":0}
fail = {"success":"False","code":1}

#success['dateType']=type(tdate)
print (success)
if tvalue and tpercent and tdate:
    udb.insertDB(tvalue,tpercent,tdate)
    respense = json.dumps(success)
else:
    respense = json.dumps(fail)
#lastdata=udb.queryDB()
#print("Content-type:text/html")
print("Content-Type: application/json")
print()
print(respense)