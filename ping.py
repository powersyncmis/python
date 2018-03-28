# Import modules
import subprocess
import os
import ipaddress

# Prompt the user to input a network address
#net_addr = input("Enter a network address in CIDR format(ex.192.168.1.0/24): ")
net_addr = "192.168.2.0/24"
# Create the network
ip_net = ipaddress.ip_network(net_addr)

# Get all hosts on that network
all_hosts = list(ip_net.hosts())

# Configure subprocess to hide the console window
info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE

# For each IP address in the subnet, 
# run the ping command with subprocess.popen interface

a=[]
for i in range(len(all_hosts)):
    output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_hosts[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
    if "Destination host unreachable" in output.decode('cp950'):
        #print(str(all_hosts[i]), "is Offline")
        continue
    elif "要求等候逾時。" in output.decode('cp950'):
        #print(str(all_hosts[i]), "is Offline")
        continue
    else:
        
        #cc=input(str(all_hosts[i])+" Yes(1) or No(0)")
        #if cc == '1':
        #    a.append(str(all_hosts[i]))
        #    bb=subprocess.Popen(['shutdown', '/s', '/m', str(all_hosts[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
        #    print(bb.decode('cp950'))
        #elif cc == '0':
        #    continue
        #else:
        #    continue
        
        print(str(all_hosts[i]), "is Online")
