from netmiko import ConnectHandler
from my_devices import rtr3, rtr4, API_KEY

net_connect = ConnectHandler(**rtr3)

print(net_connect.find_prompt())

print(API_KEY)
