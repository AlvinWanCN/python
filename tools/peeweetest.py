#!/usr/bin/python
#coding:utf-8
import time
from gold_db import sophia

#T=sophia.get()
#print(T.value)

T_list=sophia.select().where(sophia.value > 100).order_by(sophia.value.desc()).limit(5)
for T in T_list:
    print(T.name,T.value,T.date.strftime('%Y-%m-%d %H:%M:%S'))
 #  print(str(end))