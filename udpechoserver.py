import socket 
UDP_IP = "10.1.24.122"
UDP_PORT = 6789
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP, UDP_PORT))
print("server is waiting")
while True:
 data,addr = serverSock.recvfrom(1024)
 print ("Message: ", data)
 print  ( addr )
 serverSock.sendto( data,addr )
