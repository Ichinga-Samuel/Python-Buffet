from socket import *
from serverudp import fib


server_name = 'fib_server'
server_port = 1200

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(5)

while True:
    connection_sock, address = server_socket.accept()
    req = connection_sock.recv(1024)
    n = int.from_bytes(req, 'little')
    resp = fib(n)
    connection_sock.send(resp.to_bytes(8, 'little'))
