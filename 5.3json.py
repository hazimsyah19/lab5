import socket
import sys
import json


mydata = {"id":2020974265,"name":"Hazim","age":"29"}
sendData = json.dumps(mydata)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket successfully created")
port = 8080

s.bind(('',port))
print("Socket is listening")

s.listen(5)
print("socket is listening")

while True:
    c,addr = s.accept()
    print("Got connection from"+ str(addr))
    

    c.sendall(bytes(sendData,encoding="utf-8"))
    buffer = c.recv(1024)
    print(buffer)

c.close()
