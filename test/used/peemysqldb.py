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
class t_nuoh_patient_normal_user(peewee.Model):
    id = peewee.IntegerField() #int
    projectLevel = peewee.IntegerField()
    class Meta:
        database = connect
