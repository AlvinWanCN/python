#!/usr/bin/python
#coding:utf-8


import peewee #导入模块

# 建立连接
connect  = peewee.MySQLDatabase(
    database = 'sophiroth', #数据库名
    host = 'c7u4.alv.pub', #域名或ip
    user = 'alvin', #数据库用户名
    passwd = 'sophiroth' #数据库用户密码
    )

class user(peewee.Model):
    id = peewee.IntegerField() #定义数据类型为int
    name = peewee.CharField(max_length=32) #定义name的数据类型为char (32)
    age = peewee.IntegerField() #定义age的数据类型为int
   # birthday = peewee.DateTimeField()  #日期定义birthday的数据类型为日期类型
    class Meta:
        database = connect
if __name__ == '__main__': #设置若是直接执行该脚本，则执行下面的内容。若是被其他脚本调用，则不执行。
    user.create_table() #使用user这个类创建表，如果该表不存在则创建，若已存在则会报错。
