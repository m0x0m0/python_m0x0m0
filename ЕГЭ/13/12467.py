from ipaddress import *

k = 0
for a in range(256):
    net = ip_network(f'246.81.65.{a}/255.255.255.224', 0)
    if all(f'{ip:b}'[16:24].count('0') > f'{ip:b}'[24:].count('0') for ip in net.hosts()):
        k += 1

print(k)