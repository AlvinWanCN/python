#!/usr/bin/python
#coding:utf8
import commands,os

v_sorcDir='/home/alvin'
v_destDir='/tmp/alvin'


v_fileName='{s}/dir1,{s}/dir2,{s}/dir3'.format(s=v_sorcDir)
a =  v_fileName.split(',')

for i in a:
    os.chdir(v_sorcDir)
    sortName=i.split('/home/alvin/')[1]
    os.system('tar cf {d}/{s}.tar.gz {s}'.format(d=v_destDir,s=sortName))
