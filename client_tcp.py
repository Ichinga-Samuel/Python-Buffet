from socket import *


server_name = 'fib_server'
server_port = 1200

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
n = int(input('Enter Number')).to_bytes(8, 'little')
client_socket.send(n)
resp = b''
while True:
    buf = client_socket.recv(1024)
    if not buf:
        break
    resp += buf
client_socket.close()
