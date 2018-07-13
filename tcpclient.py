import socket
server_ip = '10.1.24.122'
server_port = 6789
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((server_ip,server_port))

while True:
  sentence = input(">> ")
  client_socket.send(sentence.encode())
  message = client_socket.recv(1024)
  print (">> ", message.decode())
  if(sentence == 'stop'):
    client_socket.close()
