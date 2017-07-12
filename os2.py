#!/usr/bin/python
import os

var = 'ok'

os.environ['yes']=str(var)
os.system('echo $yes')
