#!/usr/bin/python
#-*-coding:utf-8-*-
def i(v):
    print('values {v}'.format(v=v))
    print(type(v))
    print('')

a = ('alvin', 'tomath')  #这种数据是tuple类型,要使用括号
i(a)
a = 'alvin' #(这种数据是字符串类型，不用使用括号，要用引号)
i(a)

a = 666 #整数类型数据
i(a)

a = 3.14159  #小数
i(a)

a = zip((1,2,3),['a','b','c'],'defg')
i(a)

#print type(dict(zip('abc',range(1,3))))
#a = dict([1,2],('a',1),('b',3))
#print a
a={'a':'alvin','b':'natasah'}
i(a)