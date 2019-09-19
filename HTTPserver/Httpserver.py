#!/usr/bin/env python3

'''
httpserver
获取HTTP请求
解析HTTP请求
将请求发送给webFrame
从webFrame接收反馈数据
将数据组织为Response格式发送给客户端
'''


import sys
from threading import Thread
from config import *
from socket import *
import re
import json

def connect_frame(env):
    """
    与webfream交互
    :param env:
    :return:
    """
    s= socket()
    try:
        s.connect((frame_ip,frame_port))
    except:
        return

    data = json.dumps(env)
    s.send(data.encode())
    data = s.recv(1024*1024*10).decode()
    print(data)
    return json.loads(data)

class HTTPServer:
    def __init__(self):
        self.host = HOST_http
        self.port = PORT_http
        self.addr = (HOST_http,PORT_http)
    def creat_socket(self):
        """
        创建并绑定套接字
        :return:
        """
        self.socketfd=socket(AF_INET,SOCK_STREAM)
        self.socketfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.socketfd.bind(self.addr)

    def server_forever(self):
        self.creat_socket()
        self.socketfd.listen(5)
        print("Listen...")
        while True:
            connfd,addr = self.socketfd.accept()
            print("conect from " ,addr)
            client = Thread(target=self.handle,args=(connfd,))
            client.setDaemon(Thread)
            client.start()

    def handle(self,connfd):
        '''
        子进程,处理HTTP请求
        :param connfd:
        :return:
        '''


        request = connfd.recv(4096).decode()
        print(request)
        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"

        try:
            env = re.match(pattern,request).groupdict()
            print(env)
        except:
            connfd.close()
            print("close")
        else:
            #和fream 交互
            respond = connect_frame(env)
            if respond:
                self.send_response(connfd,respond)




        # 组织http响应，发送给浏览器
    def send_response(self, connfd, response):
        # response->{'status':'200','data':'ccc'}
        if response['status'] == '200':
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type:text/html\r\n"
            data += '\r\n'
            data += response['data']
        elif response['status'] == '404':
            data = "HTTP/1.1 404 Not Found\r\n"
            data += "Content-Type:text/html\r\n"
            data += '\r\n'
            data += response['data']
        elif response['status'] == '500':
            pass
        connfd.send(data.encode())

if __name__ =="__main__":
    http = HTTPServer()
    http.server_forever()# 启动文件
