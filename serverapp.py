import socket
import sys
import os


s = socket.socket()
host = ''
port = 8888
s.bind((host,port))

print("SERVER")
filename = str(input("Please enter the file name :"))
recv_file = open(filename,'wb')
s.listen(5)
#while True:
c, addr = s.accept()
print("[+]:File recv from : ", addr)
print("[+]:Start receive...")
l = c.recv(1024)
while (l):
    print("[+]:Receiving...")
    recv_file.write(l)
    l = c.recv(1024)
recv_file.close()
print("[+]:File receive successfully")
c.send(b'Message from client: File received successfully')
c.close()
sys.exit('[+]:Closed by system')

