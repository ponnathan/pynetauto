"""This is doc string"""
from getpass import getpass
from ncclient import manager
from ncclient.xml_ import new_ele
import ipdb

conn = manager.connect(
    host="srx2.lasthop.io",
    username="pyclass",
    password=getpass(),
    device_params={"name": "junos"},
    hostkey_verify=False,
    allow_agent=False,
    look_for_keys=False,
    port=830,
    timeout=60,
)

ipdb.set_trace()
rpc = new_ele("get-software-information")
nc_out = conn.rpc(rpc)

DEVICE = """
<device type="subtree">
  <configuration>
    <interfaces>
    </interfaces>
  </configuration>
</device>
"""

# It is an XML like thing
print(nc_out.tostring.decode())
print(nc_out.find(".//product-name"))
print(nc_out.find(".//product-name").text)
print(nc_out.find(".//product-model").text)

config = conn.get_config(source="running")
config_xml = config.data_xml
