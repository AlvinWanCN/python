#!/usr/bin/python
#coding:utf8

#用户切分目录与文件名，获取到我们的文件名。
a='/home/alvin/app/nginx/www/index.html'
print a.rsplit('/',1)[-1]
