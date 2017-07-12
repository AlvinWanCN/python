#!/usr/bin/python
#coding:utf8
import commands,os

v_sorcDir='/home/alvin'
v_destDir='/tmp/alvin'


v_fileName='{s}/dir1,{s}/dir2,,{s}/dir3'.format(s=v_sorcDir)
print v_fileName.split(',')
