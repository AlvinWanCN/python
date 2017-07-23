#!/usr/bin/python
#coding:utf-8
import socket,time
#TCP协议socket server
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #socket type
        #socket.AF_INET     ipv4协议的socket套接字
        #socket.AF_INET6    ipv6协议的socket套接字
        #socket.AF_UNIX     Unix系统间数据进行传输的套接字
    #socket family
        #socket.SOCK_STREAM tcp协议的socket
        #socket.SOCK_DGRAM  udp协议的socket
#绑定套接字
sock.bind(("",8000))
    #参数为双元素元组
        #第一个元素是ip地址，如果写空字符串代表代表本机所有的ip
        #第一个元素是端口，0-66535，前一千个是我们系统预留的
            #Apache 80
            #mysql 3306
#监听
sock.listen(5)

content,address = sock.accept()
    #content 用来接收请求用户的消息和发送对该请求用户的消息的功能
    #address 请求用户的身份，ip port （ip，port)
print("%s:%s is connect"%address)
content.send("吃了吗？")
print(content.recv(512))
#recv 接收用户发来的信息，512 指每次最多接收512字节，多余部分下次接收
#618
    #content.recv(512)
    #content.recv(512)
#关闭连接
sock.close()