from netmiko import ConnectHandler

device1 = {
    "device_type": 'cisco_ios',
    "host": 'cisco1.lasthop.io',
    "username": 'student5',
    "use_keys": True,
    "key_file": "/home/ponnathan/.ssh/test_rsa",
}
net_connect =  ConnectHandler(**device1)
print(net_connect.find_prompt())
net_connect.disconnect()
