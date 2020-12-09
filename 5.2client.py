import socket

ClientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '10.0.2.18'
port = 8889

print('Waiting for connection...')

try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)


while True:
    Input = str(input("Say something : "))
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))


ClientSocket.close()
