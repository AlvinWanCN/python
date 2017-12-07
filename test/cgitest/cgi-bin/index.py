#coding:utf-8

import time,cgi

html = """
<html>
     <head>
        <title>new page</title>
    </head>
    <body>
        <p>
            This is our python index
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
print('aaa')