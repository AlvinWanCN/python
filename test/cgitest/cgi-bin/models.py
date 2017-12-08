#!/usr/bin/python
#cocding:utf-8

import peewee

db = peewee.SqliteDatabase("register.db")

class User(peewee.Model):
    username = peewee.CharField(Max_length = 32)
    password = peewee.CharField(max_length = 32)
    class Meta:
        database = db

if __name__ == "__main__":
    try:
        User.create_table()
        except:
            pass
