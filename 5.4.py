import socket
import sys
import struct

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '10.0.2.18'
port = 8888
BUFFER_SIZE = 1024

def conn():
    print("[+]:Send request...")
    try:
        s.connect((host,port))
        print("[+]:Connection successful...")
    except:
        print("[+]:Connection not successful")

def upload(x):
    try:
        content = open(x,"rb")
    except:
        print("Can not read the file")
        return
    #try:
        #s.send("UPLD")
    #except:
        #print("Cannot make server request")
        #return
    try:
        s.recv(BUFFER_SIZE)
        s.send(struct.pack("h",sys.getsizeof(file_name)))
        s.send(x)
        s.recv(BUFFER_SIZE)
        s.send(struct.pack("i",os.path.getsize(file_name)))
    except:
        print("Error sending files...")
        return
    try:
        l = content.read(BUFFER_SIZE)
        print("Sending...")
        while l:
            s.send(l)
            l = content.read(BUFFER_SIZE)
        content.close()
        upload_time = struct.unpack("f",s.recv(4))[0]
        upload_size = struct.unpack("i",s.recv(4))[0]
        print("\nSent file: {}\nTime elapsed: {}s\nFile size: {}b".format(file_name,upload_time,upload_size))
    except:
        print("error sending file")
        return
    return


if __name__ == "__main__":
    print("File : ",sys.argv[1])
    file_name = sys.argv[1]
    conn()
    upload(file_name)
    #print(sys.argv[1])
