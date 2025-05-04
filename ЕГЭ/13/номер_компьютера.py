from ipaddress import *

net = ip_network('192.168.156.235/255.255.255.240', 0)
print(net) #192.168.156.224/28

ip1 = ip_address('192.168.156.235') #айпи адрес
ip2 = ip_address('192.168.156.224') #адрес сети
print(int(ip1) - int(ip2))