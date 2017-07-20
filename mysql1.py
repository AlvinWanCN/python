#!/usr/bin/python
#coding:utf8
import MySQLdb as sql,sys

connect = sql.connect(
    host = '192.168.1.214',
    user = 'root',
    passwd = sys.argv[1],
    db = 'blood_suger_v26'
    )


cursor = connect.cursor()


sqls = 'select username from user'

b = cursor.execute(sqls)
a = cursor.fetchone()
c = cursor.fetchall()
print c
#print "Database version : %s " %c

connect.close()
