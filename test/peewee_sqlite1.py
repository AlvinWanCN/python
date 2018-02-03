#!/usr/bin/python
#coding:utf-8

#导入模块
import peewee

#建立连接
connect = peewee.SqliteDatabase("gold.db")
#创建表
    #类名必须大写
    #peewee 创建数据库模型的时候，默认会添加主键id
    #peewee 创建数据库字段默认不可为空
class sophia(peewee.Model):
    name = peewee.CharField(max_length=32) #name char (32)
    value = peewee.FloatField() #Float
    date = peewee.DateTimeField()  #日期

    class Meta:
        database = connect
if __name__ == '__main__':
    sophia.create_table()