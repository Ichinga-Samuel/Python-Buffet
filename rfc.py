import urllib.request
from urllib.request import Request
import socket


def get_rfc(rfc, display=False):

    url = f'http://www.ietf.org/rfc/rfc{rfc}.txt'
    headers = {'Accept-Language': 'en', 'Connection': 'close', 'Accept-Encoding': 'identity'}
    req = Request(url, headers=headers, method='HEAD')
    resp = urllib.request.urlopen(req)
    if resp.status == 200:
        result = resp.read().decode()
        if display:
            print(resp.headers)
        else:
            with open(f'rfc {rfc}.txt', 'w') as rh:
                rh.write(result)


def sock_rfc(rfc, display=False):
    host = 'www.ietf.org'
    port = 80
    sock = socket.create_connection((host, port))

    # the http request message
    """req = (f'GET /rfc/rfc{rfc}.txt HTTP/1.1\r\n'
           f'Host: {host}:{port}\r\n'
           'User-Agent: Python\r\n'
           'Connection: close\r\n'
           '\r\n').encode('ascii')"""
    req = 'GET http://www.ietf.org/rfc/rfc2616.txt HTTP/1.1 \r\n\r\n'
    req = req.encode()
    sock.sendall(req)
    rfc_raw = bytearray()
    while True:
        buf = sock.recv(4096)
        if not len(buf):
            break
        rfc_raw += buf
    result = rfc_raw.decode()
    with open(f'rfc {rfc}.txt', 'w') as rh:
        rh.write(result)
    if display:
        print(result)

