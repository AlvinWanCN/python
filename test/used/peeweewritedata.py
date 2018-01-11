#!/usr/bin/python
#coding:utf-8
from peemysqldb import t_nuoh_patient_normal_user as t
import os,time

bashDir="E:\\" #定义基本目录
f0=bashDir+'tongban0.txt'#定义存储用户id的文件名
f1=bashDir+'tongban1.txt'
f2=bashDir+'tongban2.txt'
tb0 = open(f0,'w')#打开文件
tb1 = open(f1,'w')
tb2 = open(f2,'w')

def msg_(recordfile):#定义消息输出格式
    print('start write data to %s at %s'%(recordfile,time.strftime('%Y-%m-%d %H:%M:%S'))) #打印包含时间的消息，变量为文件名
def tongban(period,recordfile,tbf):#定义导出数据的执行函数
    tdata=[]#定义一个tdata默认值
    if period in (1,2):#判断期数，根据期数定义查询条件
        t_list = t.select().where(t.projectLevel == period )#查询数据，使用指定削减，匹配期数
    elif period == 0:
        t_list = t.select().where(t.projectLevel >> None ) #查询期数为空的数据
    for T in t_list:#将数据写入到文件
        tdata.append(str(T.id)) #将数据放如一个list
    msg_(recordfile)    #打印保护当前时间的消息
    finalData=('\n'.join(tdata)) #将数据合并
    tbf.write(finalData)    #将数据些到制定文件里
    tbf.close() #关闭文件
def _main():#定义主函数
    print('start time is %s'%time.strftime('%Y-%m-%d %H:%M:%S'))
    tongban(0,f0,tb0)
    tongban(1,f1,tb1)
    tongban(2,f2,tb2)
    print('end time is %s'%time.strftime('%Y-%m-%d %H:%M:%S'))
if __name__ == "__main__":#直接执行该脚本则执行main
    _main()
