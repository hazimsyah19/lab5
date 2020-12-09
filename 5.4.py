import socket
import sys
import os


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('[+]:Socket created')

port = 8888
s.bind(('',port))
print("[+]:Socket bind at port : " + str(port))
s.listen(5)
print("[+]:Waiting for client connection...")

while True:
    c,addr = s.accept()
    print("[+]:Got connetion from : " + str(addr))
    #c.send(b'Thank you')
    buffer = c.recv(1024)
    print(buffer)

c.close()

if __name__ == '__main__':
    print("Waiting for instruction")
    data = 
