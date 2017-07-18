#!/usr/bin/python
#coding:UTF-8
import os,sys
dbName = 'alvinlife'
dbAddress = 'localhost'
dbPort = 3306
dbPassword = sys.argv[1]
dbUser= 'alvin'
os.system('mysqldump -u{u} -p{pw} -P{po} -h{a} {n} > {n}.sql'.format(u=dbUser,po=dbPort,pw=dbPassword,a=dbAddress,n=dbName))
