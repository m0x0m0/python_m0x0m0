from ipaddress import *

for m in range(33):
    net = ip_network(f'145.192.94.230/{m}', 0)
    if str(net)[:-3] == '145.192.80.0':
        print(net)

mask = '11111111.11111111.11110000.00000000'
print(int("11110000", 2))


for m in range(33):
    net = ip_network(f'145.192.94.230/{m}', 0)
    if str(net.network_address) == '145.192.80.0':
        print(net.netmask)
