from ipaddress import *
for m in range(33):
    net = ip_network(f'142.198.113.106/{m}', 0)
    if str(net.network_address) == '142.198.112.0':
        print(m)