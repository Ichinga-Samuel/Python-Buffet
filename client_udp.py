from socket import *


server_name = 'fib_server'
server_port = 1200

client_socket = socket(AF_INET, SOCK_DGRAM)
n = int(input('Enter A Number'))
client_socket.sendto(n.to_bytes(8, 'little'), (server_name, server_port))
resp, server_address = client_socket.recvfrom(2048)
print(int.from_bytes(resp, 'little'))
client_socket.close()

