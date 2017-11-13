# -*- encode: utf-8 -*-
# python3

from socket import *
import re
import subprocess

p = re.compile('inet .+?[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
ip_msg = p.findall(subprocess.check_output('/sbin/ifconfig').decode('utf-8'))
msg = ''
for i in ip_msg:
    msg += (i + '  ')

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.sendto(msg.encode('utf-8'), ('<broadcast>', 8000))
