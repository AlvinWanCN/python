#!/usr/bin/python
#coding:utf-8

Name='E:\\alvin.txt'
file_object = open(Name,'a+')
'''
try:
     all_the_text = file_object.read( )
finally:
     file_object.close( )
'''


#print(file_object.name)
#print(file_object.read())
file_object.write('natasha\n')
#file_object.write('diana\n')
#file_object.write('sophia')
file_object.close