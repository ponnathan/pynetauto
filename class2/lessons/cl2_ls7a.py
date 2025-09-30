from getpass import getpass
from netmiko import ConnectHandler

device1 = {
    "host": 'cisco1.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios_telnet',
}
net_connect =  ConnectHandler(**device1)
print(net_connect.find_prompt()) 

#output = net_connect.send_command("show ip arp", use_textfsm=True)

#print(output)

#net_connect.disconnect()
