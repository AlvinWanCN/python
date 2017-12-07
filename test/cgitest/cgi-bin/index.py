#!/usr/bin/python
#coding:utf-8

import cgi,time

html = """
<html>
    <head>
        <title>
            news
        </title>
    </head>
    <body>
        <p>
            this is our python index
        </p>
        <p>
            %s
        </p>
    </body>
</html>

"""
now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print("Content-type:text/html")
print()
print(html%now)