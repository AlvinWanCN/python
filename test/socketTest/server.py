#!/usr/bin/python

import socket
#TCP协议socket server
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #socket type
        #socket.AF_INET     ipv4协议的socket套接字
        #socket.AF_INET6    ipv6协议的socket套接字
        #socket.AF_UNIX     Unix系统间数据进行传输的套接字
    #socket family
        #socket.SOCK_STREAM tcp协议的socket
        #socket.SOCK_DGRAM  udp协议的socket
