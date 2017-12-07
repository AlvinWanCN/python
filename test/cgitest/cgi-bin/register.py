#!/usr/bin/python
#coding:utf-8
import cgi,time

html="""
<html>
    <head>
        <mata charset="UTF-8">
        <title>
            News
        </title>
        <body>
            <p>
                this is new
            </p>
            <form action="" mothod="">
                <input type="text" name="user">
                <input type="password" name="pawd">
                <input type="submit" value="click me">
            </form>
            <p>
                %s
            </p>
            <p>
                name:%s
            </p>
            <p>
                password:%s
            </p>

        </body>

    </head>
</html>
"""

data = cgi.FieldStorage()
name = data.getvalue("user")
password = data.getvalue("pawd")
print("Content-type:text/html")
print()
print(html%(data,name,password))