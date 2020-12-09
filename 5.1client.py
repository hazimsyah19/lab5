import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 8888
s.connect(('10.0.2.18',port))
data = s.recv(1024)
s.send(b'Hi,sayas client.Terima kasih')
print(data)
s.close()

