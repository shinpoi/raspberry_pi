# -*- encode: utf-8 -*-
# python3

from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.bind(('', 8000))

print('wating...')
msg = s.recv(4096)
print(msg.decode('utf-8'))
