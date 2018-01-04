#!/usr/bin/python
#coding:utf-8
import commands,cgi,time,os

#output = commands.getoutput('ps -eo rss,pmem,pcpu,args | sort -k 1 -r -n |head -20|cat -n|sed "s/$/<\/br>"/').replace('sort: Broken pipe','')
output = os.popen('df -h').read().replace('\n','</br>')
html = """

<html>
    <head>
        <meta charset="UTF-8">
        <title>
        Sophiroth System Disk Usage Status
        </title>
    </head>
    <body>
        <font size=3>
        <p>
            %s
        </p>
        <p>
        Yes
        </p>
            Alvin</br>Wan
        </p>
        </font>
    </body>
</html>

"""
print("Content-type:text/html")
print()
print(html%output)

