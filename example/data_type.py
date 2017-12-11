#!/usr/bin/python
#coding:utf-8


#整数
print(type(4396))

#小数
print(type(43.96))

#字符串
print(type('Alvin'))

#列表（列表可以修改）
print(type(['Alvin','Wan']))

#元组（元组不可以修改）
print(type(('Alvin','Wan')))

#字典
print(type({'a':'alvin','b':'wan','c':'cn'}))
a={'a':'alvin','b':'wan','c':'cn'}
print(a['b'])
print(dict(zip('abcde',range(1,6))))
print(zip('abcde',range(1,6)))
print(range(1,6))
print(a.get('a'))