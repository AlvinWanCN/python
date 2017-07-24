#!/usr/bin/python

import socket

#TCP协议socket client

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#连接服务器
sock.connect('127.0.0.1',8000)
    #双元素元组
    #第一个元素 服务器的ip
    #第二个元素 服务端端口
