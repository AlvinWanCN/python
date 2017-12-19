#!/usr/bin/python
#coding:utf-8
import os
import peewee
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#这个路径可以保证我们web服务器调用数据库的路径和我们脚本执行的时候创建数据库的路径一致。
db = peewee.SqliteDatabase(os.path.join(BASE_DIR,"register.db"))
#db = peewee.SqliteDatabase("register.db")
'''
db = peewee.MySQLDatabase(
    database= "register",
    host = "u1",
    user = "root",
    passwd = "root"

)
'''
class User(peewee.Model):
    username = peewee.CharField(max_length = 32)
    password = peewee.CharField(max_length = 32)
    class Meta:
        database = db

if __name__ == "__main__":
    try:
        User.create_table()
    except:
            pass
