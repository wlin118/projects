#import modules
import sys;
import socket;
from datetime import datetime;

#script header
print("-"*50)
print("Port Scanner - by Jonathan Lin")
print("-"*50)

#target
if len(sys.argv) !=2:
    print("No Target IP")
    sys.exit()
target = socket.gethostbyname(sys.argv[1])
now = datetime.now();

print(f"starting scan on IP {target} at {now} for ports 1-10000")
try:
    #port ranges
    for port in range(1,10000):
        #AF_INET is address family for IPv4
        #SOCK_STREAM is socket type for TCP
        soc= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #timeout for when port is closed or filtered, otherwise it will hang
        soc.settimeout(2)
        #result returns 0 if port is open, integer if closed
        result = soc.connect_ex((target, port))
        if result ==0: 
            print(f"Port {port} is open")
        soc.close()
    print("Scan Complete")
except socket.gaierror:
    #hostname invalid
    print("Hostname could not be resolved")
    sys.exit()
except socket.error:
    #server not reached
    print("Could not connect to server")
    sys.exit()
