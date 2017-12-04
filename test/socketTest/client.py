#!/usr/bin/python
#coding:utf-8
import socket,time

#TCP协议socket client

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#连接服务器
sock.connect(('127.0.0.1',8000))
    #双元素元组
    #第一个元素 服务器的ip
    #第二个元素 服务端端口
#接受和发送消息。
print(time.ctime())
time.sleep(2)
print(sock.recv(512))
sock.send('没呢。')
print(time.ctime())
time.sleep(2)
sock.close()