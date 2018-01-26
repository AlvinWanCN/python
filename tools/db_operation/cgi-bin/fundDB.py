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
    def queryDB(self):
        querySql = 'select value,percent,date from fund_tab ORDER by id desc limit 1'
        cursor.execute(querySql)
        data=cursor.fetchall()[0]
        return (data)
        #print('Value is %s, percent is %s, date is %s '%(data[0],data[1],data[2]))
        #print (cursor.fetchall()[0][0])
        db.close()


#udb=useDB()
#udb.insertDB('insert into fund_tab set value = "1.2751",percent = "1.06%",date = "2018-01-23 15:24:20" ')