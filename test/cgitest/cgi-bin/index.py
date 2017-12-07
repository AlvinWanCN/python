#coding:utf-8
import cgi
import time

html = """
<!DOCTYPE html>
<html lang="en">
    <head>
    <meta charset="UTF-8">
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
