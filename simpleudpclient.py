import socket
UDP_IP = "10.1.24.122"
UDP_PORT = 6789
message = ("Hello, Server")
bytesTosend = str.encode(message)
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto(bytesTosend,(UDP_IP,UDP_PORT))
