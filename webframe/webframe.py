#!/usr/bin/env python3
"""
webframe.py
模拟网站的后端应用行为

从httpserver接收具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver
"""

from socket import *
import json,os
from settings import *
from multiprocessing import Process
import signal
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

class Application:
    def __init__(self):
        self.host = Host_Webfream
        self.port = Port_Webfream
        self.addr = (Host_Webfream,Port_Webfream)
        self.creat_socket()

    def creat_socket(self):
        '''
        创建套接字
        :return:
        '''
        self.socketfd = socket(AF_INET,SOCK_STREAM)
        self.socketfd.bind(self.addr)
        self.socketfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.socketfd.listen()
        print("listen....")

    def handle(self,connfd):
        import re
        data=connfd.recv(1024)
        if not data:
            connfd.close()
            return
        data = json.loads(data)
        info = data['info']

        if re.findall(r'\w+.html',info) or info =='/':
            response = self.get_html(info)
        else:
            response = self.get_data(info)
        response=json.dumps(response)
        connfd.send(response.encode())

    def get_html(self,file):
        """
        HTML请求操作
        :param file:
        :return:
        """
        response = {}
        if file =='/':
            file = "/index.html"
        if os.path.exists(File_path+file):
            print(File_path+file)
            with open(File_path+file,'r') as fd:
                response["status"] = '200'
                response['data'] = fd.read()
        else:
            with open(File_path+'/404.html') as fd:
                response['status'] = "404"
                response['data'] = fd.read()
        return response

    def get_data(self,info):
        """
        数据请求操作
        :return:
        """
        from urls import urls
        response = {}
        for url,func in urls:
            if url == info:
                response["status"] = '200'
                response['data'] = func()
                return response
        response["status"] = '404'
        response['data'] = func()
        return response




    # def get_data(self):
    def start(self):
        while True:
            connfd,addr = self.socketfd.accept()
            p = Process(target=self.handle,args=[connfd,])
            p.start()






if __name__ == '__main__':
    app = Application()
    app.start()
