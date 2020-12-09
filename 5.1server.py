import socket


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Berjaya buat socket")
port = 8888
s.bind(('',port))
print("Berjaya bind socket di port : "+ str(port))
s.listen(5)
print("socket tengah menunggu client!")


while True:
    c,addr = s.accept()
    print("Dapat capaian dari :" + str(addr))

    c.send(b'Terima kasih')
    buffer = c.recv(1024)
    print(buffer)

c.close()
