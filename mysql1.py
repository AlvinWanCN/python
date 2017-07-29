#!/usr/bin/python
#coding:utf8
import MySQLdb as sql,sys

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

sqls = 'select name from t1' #查询t1表里的所有name列。 alvin 07-07-29
#sqls = "insert into t1 set name = 'diana', math='69' "

print(cursor.execute(sqls)) #他有返回值，但是返回内容，是执行条数。

#查询结果
#查询结果的方法是有指针的
print(cursor.fetchall()) #查询所有条
#print(cursor.fetchone()) #查询一条。
#print(cursor.fetchmany()) #查询指定条。



#关闭游标
cursor.close()
#提交修改
connect.commit()
#关闭连接
connect.close()
