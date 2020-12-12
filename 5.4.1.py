import socket
import sys

s = socket.socket()
host = '10.0.2.18'
port = 8888
s.connect((host,port))

print("File : ",sys.argv[1])
filename = sys.argv[1]

try:
    send_file = open(filename,'rb')
    print("File opened")
except Exception as fileerror:
    print("Cannot open this file chech this error: %s " % str(fileerror))
filesend = send_file.read(1024)
while(filesend):
    print("[+]:Sending file")
    s.send(filesend)
    filesend = send_file.read(1024)
send_file.close()
print("[+]:File send successful")
s.close()
sys.exit("[+]:Close by system")

    



