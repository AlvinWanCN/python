#!/usr/bin/python
#coding:utf-8

d='face'
class sophia():
    alvin='Alvin Wan'
    def tomath(self):
        print('hahaha')

class ok():
    def tomath(self):
        print('hahaha')

if __name__ =='__main__':
    print("hello")

a=u'你好啊'
import os
print(os.getcwd())
dir=os.path.dirname(__file__)
name='t1.py'

if os.path.exists(os.path.join(dir,name)):
    print('hello')
    print(os.path.join(dir,name))