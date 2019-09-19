from socket import *
import json

s = socket()
s.bind(("0.0.0.0",8000))
s.listen(3)

c,addr = s.accept()
data = c.recv(1024).decode()
print(json.loads(data))
c.send("OK".encode())
