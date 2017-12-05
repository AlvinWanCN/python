#!/usr/bin/python
#coding:utf-8


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("",8001))

#接受和发送

sock.sendto("hello world Iam 8001",("127.0.0.1",8000))
data,address = sock.recvfrom(512)
#udp 服务器接受recvfrom

print("%s:%s is content"%address)