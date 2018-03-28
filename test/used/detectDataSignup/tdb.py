#!/usr/bin/python3
#coding:utf-8
import pymysql,time
#db = pymysql.connect('hostname','user','password','databaseName')
db = pymysql.connect(
    host='pdb',
    password='alpha',
    user='alpha',
    db='alvinlife',
    port=3306,
    charset='utf8'
)
cursor=db.cursor()

class useDB():
    def insertDB(self,a,b,c,d,e,f):
        inserSql="insert into signup VALUES (%s,%s,%s,%s,%s,%s)"%(a,b,c,d,e,f)
        try:
            cursor.execute(inserSql)
            db.commit()
            return ('commit success')
            #return (inserSql)
        except Exception as e:
            db.rollback()
            print('commit failed')
            return (str(inserSql+e))
        finally:
            db.close()
    def queryDB(self,sql):
        querySql = sql
        cursor.execute(querySql)
        data=cursor.fetchall()
        return (data)
