#!/usr/bin/python
#coding:utf-8

import peewee #导入模块

# 建立连接
connect  = peewee.MySQLDatabase(
    database = 'fund', #数据库名
    host = 't.alv.pub', #域名或ip
    user = 'fund', #数据库用户名
    passwd = 'fund' #数据库用户密码
    )

class fund_tab(peewee.Model):
    id = peewee.IntegerField() #定义数据类型为int
    value = peewee.FloatField() #Float
    percent = peewee.CharField()
    date = peewee.DateTimeField()  #日期
    class Meta:
        database = connect
if __name__ == '__main__': #设置若是直接执行该脚本，则执行下面的内容。若是被其他脚本调用，则不执行。
    fund_tab.create_table() #使用user这个类创建表，如果该表不存在则创建，若已存在则会报错。
