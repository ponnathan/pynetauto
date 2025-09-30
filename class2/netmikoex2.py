import os
from netmiko import ConnectHandler
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "global_delay_factor": 2,
    "fast_cli": False,
}

net_connect = ConnectHandler(**nxos2)

cmd = "show lldp neighbors detail"
output = net_connect.send_command(cmd)
print(output)

output1 = net_connect.send_command("show lldp neighbors", delay_factor=8)
print(output1)

net_connect.disconnect()
