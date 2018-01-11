#!/usr/bin/python
#coding:utf-8

#导入模块
import peewee

#建立连接
connect  = peewee.MySQLDatabase(
    database = 'xxx',#设置数据库名
    host = 'xxxxx',#设置服务器的域名或ip
    user = 'xxxx',#用户名
    passwd = 'xxxxxxxx' #密码
    )

#定义表
class t_nuoh_patient_normal_user(peewee.Model): #表名
    id = peewee.IntegerField() #int   #指定我们需要用到的字段和数据类型
    projectLevel = peewee.IntegerField() #只需要这两个字段，我们就只定义这两个字段。
    class Meta:
        database = connect
