#/usr/bin/python
#coding:utf-8

import pymysql
db = pymysql.connect('t.alv.pub','fund','fund','fund')

file1=open('E:\\mysql.txt','w+')
cursor=db.cursor()
cursor.execute('select * from fund_tab')
#date=cursor.fetchall()
#date=cursor.fetchone()
data=cursor.fetchone()
print (data[-1])
file1.write(str(data[-1]))
file1.close()
