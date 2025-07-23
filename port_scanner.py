#ping sweeper
#send ICMP ping requests through subprocess, expects response from active hosts in subnet

#script header
print("-"*50)
print("Ping Sweep - by Jonathan Lin")
print("-"*50)


import subprocess
import ipaddress
import platform
#get range of ip address to ping
#start with /24 mask networks
print("Input network/mask")
net_in=input()
#covert string into IPv4 object
net = ipaddress.IPv4Network(net_in)
#check for windows or linux
os=platform.system().lower()
if os=="windows":
    #windows
    flag="-n"
else:
    #macOS or Linux
    flag="-c"


for addr in net.hosts():
    try: 
        str_addr=str(addr)
        #1 ping, -W 1000 milliseconds
        cmd= ["ping", flag, str_addr]
        #pings each ip addr in subnet
        #shell= true otherwise tries to find program literally named the passed string'
        #stdout and stderrsaved into result 
        result= subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output= result.stdout
        error= result.stderr
        #result.return code seems to always return 0 with ping on my version of windows
        if "unreachable" in output or "timed out" in output:
            print(f"Ping failed, {str_addr} is unreachable")
        else:
            #stderror empty when successful
            print(f"Ping successful, {str_addr} is reachable")

    except Exception as e:
        print(f"Error pinging {str_addr}: {e}")
