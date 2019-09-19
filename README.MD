# 多任务编程练习项目
## 项目简介
该项目模拟了webserver处理过程

浏览器发送请求->httpserver接收并解析HTTP请求->根据请求内容将任务交付给webframe处理处理完成后以一定格式交个httpserver,再有httpserver组织成HTTP响应返回给浏览器



### 功能 

>httpserver部分
>
>> 获取http请求
>> 解析http请求
>> 将请求发送给WebFrame
>> 从WebFrame接收反馈数据
>> 将数据组织为Response格式发

> 给客户端
>> WebFrame部分
>> 从httpserver接收具体请求
>> 根据请求进行逻辑处理和数据处理
>> 将需要的数据反馈给httpserver

> 特点
>> 采用httpserver和应用处理分离的模式,降低了耦合度
>> 采用了用户配置文件的思路
>> webframe部分采用了模拟后端框架的处理方法

> 技术点
>> httpserver部分需要与两端建立通信
>> webFrame部分采用多路复用接收并发请求
>> 数据传递使用json格式

项目结构:
目结构:
				  |--httpserver--| --HttpServer.py (主程序)
                  |							|--config (httpserver配置)
project--|
                  |
				  |--WebFrame-- |
                 								|  --WebFrame.py (主程序代码)
			     							    |--static (存放静态网页)
				   							  |--views.py ( 应用处理程序)
												 |--urls.py (存放路由)
												 |--settings (框架配置)

![HTTP](/home/tarena/桌面/笔记/IO网络编程/http.png)

### 交互数据格式协议

httpserver-->webframe {'method':'GET',info:'/'}

键 info 对应值 为请求内容

webframe-->httpserver {'status':'200','data':'ccccc'}

data为处理后结果



## 代码分析

### httpserver 部分

congfig.py中包含相关的配置信息

> ```Python
> # [HTTP 服务器地址]
> HOST_http = "127.0.0.1"
> PORT_http = 8808
> #[调试模式]
> DEBUG = True
> # webframe.py 地址f
> rame_ip = '127.0.0.1'
> frame_port = 8806
> ```

封装:

httpserver.py

* 创建 HTTPServer类

  1.实例变量:

  >  self.host #服务器IP地址
  >
  > self.port # 端口号
  >
  > self.addr # 套接字
  >
  > self.socketfd # 套接字对像

  2.实例方法

  > __ init__() #
  >
  > create_socket()#创建套接字对象并绑定
  >
  > server_forever() # 服务器入口启动函数
  >
  > handle(self,connfd) #子进程
  >
  > send_response(self.connfd,response) # 组织HTTP相应

  > connfd_frame(env)#与webframe
  >
  > 参数:{'method':'GET',info:'/'}s

###  webframe部分

* setting.py部分

  ​	功能:配置文件

* webframe.py

  设计思路:

  ​	服务端每次接受一个请求建立一个进程处理,处理完后退出进程

  封装:

  1. 实例变量

     >  self.host #服务器IP地址
     >
     > self.port # 端口号
     >
     > self.addr # 套接字
     >
     > self.socketfd # 套接字对像

     2. 示例方法

        > handle()
        >
        > get_html()# 处理网页请求
        >
        > get_data()#数据处理

* views.py

  封装数据处理的方法

* urls.py

  请求与函数或URL的映射

  根据查表可找到找到请求对应的函数或ＵＲＬ

  ```python
  from views import *
  
  urls =[("/datetime",datetime),
         ("hi",hi)]
  ```

  