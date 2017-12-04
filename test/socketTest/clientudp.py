#!/usr/bin/python
#coding:utf-8


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("",8001))

#接受和发送

sock.sendto("hello world Iam 8001",("1"))