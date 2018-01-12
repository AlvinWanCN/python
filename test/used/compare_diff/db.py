#!/usr/bin/python
#coding:utf-8

#导入模块
import peewee,sys

#建立连接

connect  = peewee.MySQLDatabase(
    database = sys.argv[2],#设置数据库名
    host = sys.argv[1],#设置服务器的域名或ip
    user = sys.argv[3],#用户名
    passwd = sys.argv[4] #密码
    )

connect2  = peewee.MySQLDatabase(
    database = 'sophiroth', #数据库名
    host = 'c7u4.alv.pub', #域名或ip
    user = 'alvin', #数据库用户名
    passwd = 'sophiroth' #数据库用户密码
    )

'''
class user(peewee.Model):
    id = peewee.IntegerField() #定义数据类型为int
    name = peewee.CharField(max_length=32) #定义name的数据类型为char (32)

    class Meta:
        database = connect2
 '''
#定义表
class hospital(peewee.Model): #表名
    id = peewee.IntegerField() #int   #指定我们需要用到的字段和数据类型
    name = peewee.CharField() #只需要这两个字段，我们就只定义这两个字段。
    class Meta:
        database = connect


#定义表
class user(peewee.Model): #表名
    id = peewee.CharField()
    mobile = peewee.CharField() #int   #指定我们需要用到的字段和数据类型
    hospitalId = peewee.CharField() #只需要这两个字段，我们就只定义这两个字段。

    class Meta:
        database = connect


