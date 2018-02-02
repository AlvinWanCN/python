#!/usr/bin/python3
#coding:utf-8
import cgi

data=cgi.FieldStorage()
new_account={}
new_account['app']=data.getvalue('app')
new_account['username']=data.getvalue('username')
new_account['password']=data.getvalue('password')
new_account['comment']=data.getvalue('comment')
#print(new_account)
html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>添加新账号结果</title>
</head>
<body>
    您已成功添加新账号
</body>
</html>
"""
#print("Content-Type: application/json")
print("Content-type:text/html")
print()
print(html)