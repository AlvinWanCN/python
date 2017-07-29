#!/usr/bin/python
#coding:utf8
import MySQLdb as sql
import sys
import xlwt,time

'''
connect = sql.connect(
    host = sys.argv[1],
    user = sys.argv[2],
    passwd = sys.argv[3],
    db = 'alv',
    port = 1006
    )

#实例化游标

cursor = connect.cursor()
    #他是一个内存，里面可以存放python给mysql的命令和mysql返回的结果

#知识sql语句
    #sql 语句不用加分号
        #方便修改
        #方便调用
        #结构清晰
        #方便注释

sqls = 'select * from t1' #查询t1表里的所有name列。 alvin 07-07-29
#sqls = "insert into t1 set name = 'diana', math='69' "

print(cursor.execute(sqls)) #他有返回值，但是返回内容，是执行条数。

#查询结果
#查询结果的方法是有指针的
print(cursor.fetchall()) #查询所有条
#print(cursor.fetchone()) #查询一条。
#print(cursor.fetchmany()) #查询指定条。

print(cursor.description)

#关闭游标
cursor.close()
#提交修改
connect.commit()
#关闭连接
connect.close()
'''

filename = 'D:\sophiroth{Now}.xls'.format(Now=time.strftime('%y-%m-%d-%H-%M-%S'))

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
    SQL = 'select id,name,math from t1'

    sqls = OurSql()
    num, result,desc = sqls.execute(SQL)
   # print(num)
    print(len(result))
    print(len(desc))
    workbook = xlwt.Workbook()  #创建工作薄
    sheet = workbook.add_sheet("Sophiroth")  #创建工作表

    #将标题写入到第一行到单元格
    for col in range(len(desc)):
        sheet.write(0,col,desc[col][0])
    #将查询到的内容写入到后面的单元格（cell)
    for row in range(len(result)):
        for col in range(len(result[row])):
            sheet.write(row+1,col,(result[row])[col])
    #sheet.write(0,2,'This is Sophiroth') #row,clume,value


    workbook.save(filename)
    del sqls
if __name__ == "__main__":
    main(1)