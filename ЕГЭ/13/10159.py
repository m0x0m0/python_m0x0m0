from ipaddress import *

k = 0
for m in range(33):
    net = ip_network(f'76.155.48.2/{m}', 0)
    if str(net.network_address) == '76.155.48.0':
        k += 1
print(k)