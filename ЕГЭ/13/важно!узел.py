from ipaddress import *

ip = ip_address('238.237.149.255')
for m in range(33):
    net = ip_network(f'{ip}/{m}', 0)
    if str(net.network_address) == '238.237.148.0' and net[0] < ip < net[-1]:
        print(m)