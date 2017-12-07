#!/usr/bin/python
#coding:utf-8
import commands,cgi,time

output = commands.getoutput('ps -eo rss,pmem,pcpu,args | sort -k 1 -r -n |head -20|cat -n|sed "s/$/<\/br>"/')

html = """

<html>
    <head>
        <meta charset="UTF-8">
        <title>
        Sophiroth System Memory Usage Status
        </title>
    </head>
    <body>
        <p>
            %s
        </p>
        <p>
            Alvin</br>Wan
        </p>
    </body>
</html>

"""
print("Content-type:text/html")
print()
print(html%output)

