#!/usr/bin/python
#coding:utf8


'''
def ap(i,e):
    print ("first is {i},last is  {nnn}".format(i=i,nnn=e))

bb = 'facebook'
##ap(1)
ap('alvin',bb)


def aa(a,b):
    if a <= 0:
        return 1
    else:
        print ("hello{b},thi is {a}".format(b=b,a=a))

aa(21,'alvin')
'''


"""
#*args代表任意个参数，**kwargs代表字典
def test(*args,**kwargs):
    print args,type(args)
    print kwargs,type(kwargs)
    return args,kwargs

print(test('hello','yes'))
print()
print(test(1,2,3,4,5,name = 'alvin',age = 22))
"""

#return 是返回值，a=re() 等于将re()的执行返回值赋值给a
def re():
    print('hello')
    return 'no'
a=re()
print
print(a)

