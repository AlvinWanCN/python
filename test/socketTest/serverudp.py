#!/usr/bin/python
#coding:utf-8
import socket,time

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#绑定ip
sock.bind(("",8000))

#接受与发送。

data,address = sock.recvfrom(512)
print("%s:%s is connect"%address)
print(data)
sock.sendto("hello world",address)

#关闭

sock.close()
#