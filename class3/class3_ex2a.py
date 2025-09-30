import yaml
from pprint import pprint

arista1 = {"device_name": "arista1", "host": "arista1.lasthop.io"}

arista2 = {"device_name": "arista2", "host": "arista2.lasthop.io"}

arista3 = {"device_name": "arista3", "host": "arista3.lasthop.io"}

arista4 = {"device_name": "arista4", "host": "arista4.lasthop.io"}

my_devices = [arista1, arista2, arista3, arista4]
for device in my_devices:
    device["username"] = "pyclass"
    device["password"] = "88newclass"

print()
pprint(my_devices)
print()

with open("my_devices.yml", "w") as f:
    yaml.dump(my_devices, f, default_flow_style=False)
