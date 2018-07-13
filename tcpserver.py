import socket
server_ip = '10.1.24.122'
server_port = 6789
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((server_ip,server_port))
server_socket.listen(1)
print ("Welcome: The server is now ready to receive")
connection_socket, address = server_socket.accept()
while True:
  sentence = connection_socket.recv(1024).decode()
  print('>> ',sentence)
  message = input(">> ")
  connection_socket.send(message.encode())
  if(message == 'stop'):
    connectionSocket.close()
