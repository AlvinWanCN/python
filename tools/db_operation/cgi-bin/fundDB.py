#!/usr/bin/python
#coding:utf-8
import pymysql,time
#db = pymysql.connect('hostname','user','password','databaseName')
db = pymysql.connect('t.alv.pub','fund','fund','fund')
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
