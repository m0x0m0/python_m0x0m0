from ipaddress import *

k=0
net = ip_network('192.168.32.160/255.255.255.240', 0)
for ip in net:
    if f'{ip:b}'.count('1') % 2 == 0: k += 1
print(k)
