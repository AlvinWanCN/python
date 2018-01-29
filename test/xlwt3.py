#!/usr/bin/python
#coding:utf-8
import xlwt,time
from fundDB import useDB
workbook = xlwt.Workbook()  #创建工作薄
sheet = workbook.add_sheet("Sophiroth")  #创建工作表
date=time.strftime('%Y-%m-%d')
#写单元格（cell)
excelFile='D:\%s_sophiroth.xls'%(date) #定义文件名和路径
udb=useDB() #实例化类
sql='select value,percent,date from fund_tab ORDER by id desc limit 10' #定义查询语句
result=udb.queryDB(sql) #执行查询，并返回查询结果
columnName=('净值','百分比','日期'),#column name. 这里我们手动填写好列名，加入到查询结果里面去，后面那个逗号，很重要。表示前面空号里的是一条数据。
result=columnName+result #将列名与查询到的数据合并

for row in range(0,len(result)): #以查询到的数据的条数为循环次数，也就是说多少条数，row
    for col in range(0,len(result[0])):   #以每一条数据的列的数量为循环次数，也就是有多少列数据。columu
        try:
            sheet.write(row, col, result[row][col].strftime('%Y-%m-%d %H:%M:%S')) #将日期类型的数据格式化输出为指定日期类型
        except:
            sheet.write(row, col, result[row][col]) #格式化为日期如果类型报错，就输出这样的类型
        finally:
            workbook.save(excelFile) #报错excel到指定的地方。