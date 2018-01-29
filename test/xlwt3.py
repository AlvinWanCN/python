#!/usr/bin/python
#coding:utf-8
import xlwt
from fundDB import useDB
workbook = xlwt.Workbook()  #创建工作薄
sheet = workbook.add_sheet("Sophiroth")  #创建工作表

#写单元格（cell)
sheet.write(0,2,'This is Sophiroth') #row,clume,value


workbook.save('D:\sophiroth.xls')

udb=useDB()
#state = {"success":"True","code":0}
#respense = json.dumps(state)
lastdata=udb.queryDB('select value,percent,date from fund_tab ORDER by id desc limit 3')
print (lastdata[0][0])