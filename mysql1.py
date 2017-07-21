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
cursor = connect.cursor()

sqls = 'select name from t1'
#sqls = "insert into t1 set name = 'diana', math='69' "

a = cursor.execute(sqls)
c = cursor.fetchall()
b = cursor.fetchone()
bb = cursor.fetchone()




print a
print b
print b
#print b+b+b
if c[0] == ('alvin',):
    print 'The first name is alvin'

else:
    print("That's not alvin")
    print c[0]

#print "Database version : %s " %c
cursor.close()
#cursor.commit()
connect.close()
