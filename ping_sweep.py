#ping sweeper
#send ICMP ping requests through subprocess, expects response from active hosts in subnet

#script header
print("-"*50)
print("Ping Sweep - by Jonathan Lin")
print("-"*50)


import subprocess
import ipaddress
#get range of ip address to ping
#start with /24 mask networks
net_in=input("Input network/mask")
#covert string into IPv4 object
net = ipaddress.IPv4Network(net_in)
for addr in net.hosts():
    print(addr)
