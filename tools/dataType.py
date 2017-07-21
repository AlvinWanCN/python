#!/usr/bin/python
#-*-coding:utf-8-*-
a = ('alvin', 'tomath')  #这种数据是tuple类型,要使用括号
print(a)
print(type(a))

a = 'alvin' #(这种数据是字符串类型，不用使用括号，要用引号)
print(a)
print(type(a))

a = 666 #整数类型数据
print(a)
print(type(a))

a = 3.14159
print(a)
print(type(a))

a = zip((1,2,3),['a','b','c'],'defg')
print(a)
print(type(a))

a = dict([1,2],('a',1),('b',3))
print a