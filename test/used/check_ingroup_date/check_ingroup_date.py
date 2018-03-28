#!/usr/bin/python
#coding:utf-8

#!/usr/bin/python
#coding:utf-8
import pymysql,time
db = pymysql.connect(
    host='hostname',
    password='password',
    user='alvin',
    db='dbname',
    port=3306,
    charset='utf8'
)
cursor=db.cursor()
class useDB():
    def queryDB(self,mobile):
        querySql = 'select t2.createdate from user t1, userservicecode t2 where t1.mobile = "%s" and t1.id = t2.userId  and serviceCodeId = 1611010600068947'%mobile
        cursor.execute(querySql)
        data=cursor.fetchall()
        return (data)


udb=useDB()
numbers="""
13939266508
15839200299
15939261650
13849212790
13839232558
18839272317
13849216286
18892115544
13783015039
18903920013
13939228465
13663925021

"""
numbers_list=numbers.split('\n')




for i in numbers_list:
    if i == '':
        continue
    print(i+' 的胰友同伴项目入组时间是: '+ str(udb.queryDB(i)[0][0]))
