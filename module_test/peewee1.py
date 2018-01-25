#!/usr/bin/python
#coding:utf-8

#导入模块
import peewee

#建立连接
connect  = peewee.MySQLDatabase(
    database = 'sophiroth',
    host = 'c7u4.alv.pub',
    user = 'alvin',
    passwd = 'sophiroth'
    )
#创建表
    #类名必须大写
    #peewee 创建数据库模型的时候，默认会添加主键id
    #peewee 创建数据库字段默认不可为空
class natasha2(peewee.Model):
    name = peewee.CharField(max_length=32) #name char (32)
    age = peewee.IntegerField() #int
    birthday = peewee.DateTimeField()  #日期

    class Meta:
        database = connect
if __name__ == '__main__':
    natasha2.create_table()