#!/usr/bin/python
#coding:utf8
import MySQLdb as sql

connect = sql.connect(
    host = 'localhost',
    user = 'alvin',
    passwd = 'wankaihao',
    db = 'alvinlife'
    )


cursor = connect.cursor()


sqls = 'select username from account'

b = cursor.execute(sqls)
a = cursor.fetchone()
c = cursor.fetchall()
print c
#print "Database version : %s " %c

connect.close()
