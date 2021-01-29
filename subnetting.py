import re


def get_octets(address: str):
    pattern = re.compile(r'\b(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})')
    result = pattern.fullmatch(address)
    try:
        if int(max(result.groups(), key=lambda i: int(i))) > 255:
            raise ValueError('Not a Valid Ip address')
        octets = ['{:08b}'.format(int(i)) for i in result.groups()]
        print(octets)
        return octets
    except AttributeError as ae:
        print(ae)
    except ValueError as ve:
        print(ve)


def un_mask(host: str, mask: str):
    host, mask = get_octets(host), get_octets(mask)
    net = []
    for i, j in zip(host, mask):
        b = ''
        for x, y in zip(i, j):
            z = int(x) & int(y)
            b += str(z)
        net.append(int(b, 2))
    network_id = '.'.join(str(i) for i in net)
    print(network_id)


ip = '8780.36.78.0'
ips = '255.255.255.0'

get_octets(ip)
