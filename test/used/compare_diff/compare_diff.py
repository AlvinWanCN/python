#!/usr/bin/python
#coding:utf-8
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from db import hospital
from db import user
baseDir='E:\\'
file1=baseDir+'1.txt'
file2=baseDir+'2.txt'
file3=baseDir+'3.txt'
file4=baseDir+'4.txt'
f1=open(file1,'r')
f2=open(file2,'r')
f3=open(file3,'w')
f4=open(file4,'w')


#ff1=open(file1,'r')

#print (ff1.readline())
#print re.sub(r'\s+',ff1.read())
aa='hellword'
all_file1=f1.read().strip().split('\n')
all_file2=f2.read().strip().split('\n')

merge_file=all_file1+all_file2

print (f1.readline())


def run_compare():
    unique_word = []
    for i in merge_file:

        if merge_file.count(i) == 1:
            unique_word.append(i)

    u_list = user.select().where(user.mobile << unique_word) #query user table
    #Get hospitalID
    hospitalId=[]
    for T in u_list:
        hospitalId.append(T.hospitalId)
    h_list = hospital.select().where(hospital.id << hospitalId)
    #Get hospitalName
    hospitalName=[]
    for T in h_list:
        hospitalName.append(T.name)
        print T.name
    #print(hospitalName)
    #print(unique_word)
    #print ('\n'.join(unique_word))
    print (hospitalName)

    f3.write('\n'.join(unique_word))
    f4.write('\n'.join(hospitalName))




run_compare()
