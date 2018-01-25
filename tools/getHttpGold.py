#!/usr/bin/python
#coding:utf-8
import os

httpGoldPrice = os.popen("curl http://gold.hexun.com/hjxh/ 2>/dev/null|grep -A1 '>Au99.99'|tail -1").read().split('<td>')[1].split('<')[0]

print(type(float(httpGoldPrice)))

