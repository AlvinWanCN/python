#!/usr/bin/python
#coding:utf-8
import xlwt

workbook = xlwt.Workbook()  #创建工作薄
sheet = workbook.add_sheet("Sophiroth")  #创建工作表

#写单元格（cell)
sheet.write(0,2,'This is Sophiroth') #row,clume,value


workbook.save('D:\sophiroth.xls')