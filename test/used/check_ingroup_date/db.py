#!/usr/bin/python
#coding:utf-8
import pymysql,time
#db = pymysql.connect('hostname','user','password','databaseName')
db = pymysql.connect(
    host='localhost',
    password='fund',
    user='fund',
    db='fund',
    port=3306,
    charset='utf8'
)
cursor=db.cursor()
class useDB():
    def queryDB(self,sql):
        querySql = sql
        cursor.execute(querySql)
        data=cursor.fetchall()
        return (data)