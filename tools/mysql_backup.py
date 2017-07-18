#!/usr/bin/python
#coding:UTF-8
import os
dbName = 'alvinlife'
dbAddress = 'localhost'
dbPort = 3306
dbPassword = 'password'
dbUser= 'alvin'
os.system('mysqldump -u{u} -p{pw} -P{po} -h{a} {n} > alvinlife.sql'.format(u=dbUser,po=dbPort,pw=dbPassword,a=dbAddress,n=dbName))