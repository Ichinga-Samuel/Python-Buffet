from socket import *


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


server_port = 1200


def server():
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(('', server_port))
    while True:
        request, client_address = server_socket.recvfrom(2048)
        request = int.from_bytes(request, 'little')
        result = fib(request)
        server_socket.sendto(result.to_bytes(8, 'little'), client_address)


server()
