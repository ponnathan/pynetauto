import os
import pyeapi
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

connection = pyeapi.client.connect(
    transport="https",
    host="arista8.lasthop.io",
    username="pyclass",
    password=password,
    port="443",
)

enable = (
    os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass("Enable: ")
)
device = pyeapi.client.Node(connection, enablepwd=enable)

vlan_cfg = device.api("vlans")
print(vlan_cfg)
