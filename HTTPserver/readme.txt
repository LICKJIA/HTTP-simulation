import json

json.dumps(data)
将字典或列表转换成Json格式

json.loads(data)
将Json 格式转换为字典或列表


让程序后台运行
1.程序开头添加
#!/usr/bin/env python3
2.添加可执行权限
 chmod u+x file.py
3.执行文件后加 &
 ./file.py &

添加软连接
ln -s [路径]目标文件 [路径/]链接名