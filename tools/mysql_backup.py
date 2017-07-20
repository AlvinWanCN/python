#!/usr/bin/python
#coding:UTF-8
import os,sys
dbName = 'blood_suger_v26'
dbAddress = '192.168.1.214'
dbPort = 3306
dbPassword = sys.argv[1]
dbUser= 'root'
os.system('mysqldump -u{u} -p{pw} -P{po} -h{a} {n} > {n}.sql'.format(u=dbUser,po=dbPort,pw=dbPassword,a=dbAddress,n=dbName))
