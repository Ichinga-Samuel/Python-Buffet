import socket
import os


ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ms.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
ms.send(cmd)

data = ms.recv(16)
with open('romeo.txt', 'wt') as rm:
    while len(data) > 1:
        data = ms.recv(16)
        print(data.decode(), end='', file=rm)

os.startfile('romeo.txt')
ms.close()

ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ns.connect(('data.pr4e.org', 80))
ns.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
pic = b''
count = 0
data = ns.recv(512)
while len(data) > 1:
    data = ns.recv(512)
    pic += data

pos = pic.find(b'\r\n\r\n')
picture = pic[pos+4:]
with open('cover.jpg', 'wb') as p:
    p.write(picture)

os.startfile('cover.jpg')

