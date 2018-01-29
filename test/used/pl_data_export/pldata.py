#!/usr/bin/python
#coding:utf-8
import pymysql,time
#db = pymysql.connect('hostname','user','password','databaseName')
db = pymysql.connect(
    host='t.alv.pub',
    password='fund',
    user='fund',
    db='fund',
    port=3306,
    charset='utf8'
)
cursor=db.cursor()
class useDB():
    def insertDB(self,value,percent,date):
        inserSql="insert into fund_tab set value = %s ,percent = '%s',date = '%s'" %(value,percent,date)
        try:
            cursor.execute(inserSql)
            db.commit()
            print('commit success')
        except Exception as e:
            db.rollback()
            print('commit failed')
            print (e)
        finally:
            db.close()
    def queryDB(self,sql):
        querySql = sql
        cursor.execute(querySql)
        data=cursor.fetchall()
        return (data)

udb=useDB() #实例化类
sql='select value,percent,date from fund_tab ORDER by id desc limit 10' #定义查询语句
result=udb.queryDB(sql) #执行查询，并返回查询结果
print(result)