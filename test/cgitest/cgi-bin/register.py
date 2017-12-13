#!/usr/bin/python
#coding:utf-8
import cgi,time
from models import User

html_user="""
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
html_blank="""
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

        </body>

    </head>
</html>
"""

data = cgi.FieldStorage()
name = data.getvalue("user")
password = data.getvalue("pawd")

if name and password:
    user = User()
    user.username = name
    user.password = password
    user.save()
print("Content-type:text/html")
print()
if name and password:
    print(html_user%(data,name,password))
else:
    print(html_blank)
