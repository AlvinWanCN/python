#!/usr/bin/python
#coding:utf-8
import os,re,time

import time,json


#print (old_database)
#cc='\n'.join(os.listdir(logdir))
#print cc
#print (re.findall(r'late.*',('\n'.join(os.listdir(logdir)))))

#print str(back)
#if os.path.exists(newlogfile):  print 'haha'

#!/usr/bin/python
#coding:utf-8

#print (content)
#html=etree.HTML(content)
#html = BS(content,'lxml')
#print (content_list[0])
#print(re.findall(r'>(.*)<',str(content_list[0]))[0])

#print ( re.findall(r'con.*\">(.*)<',content)[0])
import xlwt
import time

time.clock()
f = xlwt.Workbook()
sheet1 = f.add_sheet('A Demo')
for i in range(0,10000):
    for g in range(0,10):
        sheet1.write(i,g,'Alvin Wan')
f.save('D:\\xlwt.xls')
t = time.clock()
print(t)