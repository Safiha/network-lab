# network-lab
import socket 
UDP_IP_ADDRESS = "10.1.24.122"

UDP_PORT_NO = 6789
Message = "Hello, Server"
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print("server is waiting")
while True:

    data,addr = serverSock.recvfrom(1024)
    print ("Message: ", data)
