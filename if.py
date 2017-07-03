#!/usr/bin/python
#encoding: utf8


_username = 'alvin'
_password = 'alvinpassword'
username = str(raw_input("username:"))
password = str(raw_input("password:"))


if _username == username and _password == password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("Ivalid username or password,无效的密码")
