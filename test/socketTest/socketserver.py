#!/usr/bin/python
#coding:utf-8

import SocketServer
import threading
class MyHandle(SocketServer.BaseRequestHandler):
    """
    当前类是要重新定义的一个句柄
    """
    def setup(self):
        print("this is our server")
    def handle(self):
        """
        这个方法就是用来处理socket请求的
        self.request 请求
        self.client_address 请求用户ip和端口
        slef.server 当前服务
        :return:
        """

        print("%s:%s is content"%self.client_address)
        content = self.request
        recvData = content.recv(512)
        print(recvData)
        content.send(recvData.upper())

    def finish(self):
        print("server is done")


if __name__ == "__main":
    server = SocketServer.ThreadingTCPServer(("",8000),MyHandle)
    #开启服务的函数server.server_forever
    server_thread = threading.Thread(target = server.serve_forever())
    server_thread.start()
    print("%s is start "%server_thread.name)
