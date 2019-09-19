from socket import *
import json,os
from settings import *
from multiprocessing import Process

# s = socket(AF_INET,SOCK_STREAM)
# s.connect((Host_Webfream,Port_Webfream))
# env = json.dump()
# data = json.dumps(env)
# s.send(data.encode())
# data = s.recv(1024*1024*10).decode()
# print(data)

print(os.path.exists(File_path+"/index.html"))