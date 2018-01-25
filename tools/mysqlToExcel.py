#!/usr/bin/python
#coding:utf8
import MySQLdb as sql
import sys
import xlwt,time

filename = 'D:\sophiroth{Now}.xls'.format(Now=time.strftime('%y-%m-%d-%H-%M-%S'))  #excel的文件名

class OurSql:
    def __init__(self,host = sys.argv[1],user = sys.argv[2],passwd = sys.argv[3],db = 'alv',port = 1006):
        self.connect = sql.connect(
            host = sys.argv[1],
            user=sys.argv[2],
            passwd=sys.argv[3],
            db='alv',
            port=1006
        )
        self.cursor = self.connect.cursor()
    def execute(self,sql):
        num = self.cursor.execute(sql)
        result = self.cursor.fetchall()
        desc = self.cursor.description
        return num,result,desc

    def __del__(self):
        self.cursor.close()
        self.connect.commit()
        self.connect.close()

def main(self):
    SQL = '''
select id,name,math from t1
'''  #要执行的sql语句

    sqls = OurSql()
    num, result,desc = sqls.execute(SQL)
   # print(num)
    print(len(result))
    print(len(desc))
    workbook = xlwt.Workbook()  #创建工作薄
    sheet = workbook.add_sheet("Sophiroth")  #创建工作表
    sheet2 = workbook.add_sheet("natasha")

    #将标题写入到第一行到单元格
    for col in range(len(desc)):
        sheet.write(0,col,desc[col][0])
    #将查询到的内容写入到后面的单元格（cell)
    for row in range(len(result)):
        for col in range(len(result[row])):
            sheet.write(row+1,col,(result[row])[col])
    #sheet.write(0,2,'This is Sophiroth') #row,clume,value

    #下面重写了一份到第二个工作表里，用于测试多个工作表。
    for col in range(len(desc)):
        sheet2.write(0,col,desc[col][0])
    #将查询到的内容写入到后面的单元格（cell)
    for row in range(len(result)):
        for col in range(len(result[row])):
            sheet2.write(row+1,col,(result[row])[col])
    #sheet.write(0,2,'This is Sophiroth') #row,clume,value

    workbook.save(filename)
    del sqls
if __name__ == "__main__":
    main(1)