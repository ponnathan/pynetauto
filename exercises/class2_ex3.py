from netmiko import ConnectHandler
import yaml
from pprint import pprint

with open("/home/ponnathan/.netmiko.yml") as yaml_file:
    devices = yaml.safe_load(yaml_file)

device = devices["cisco4"]

dev_con = ConnectHandler(**device)

ver = dev_con.send_command("show version", use_textfsm=True)
print("\n=== SHOW VERSION ===")
pprint(ver)

lldp = dev_con.send_command("show lldp neighbors", use_textfsm=True)
print("\n=== SHOW LLDP NEIGHBORS ===")
pprint(lldp)

print()
print("#" * 30)
print("\nData type for 'lldp neighbors':", type(lldp))
print(f"\nHPE switch port :", lldp[0].get("neighbor_interface"))
print()
dev_con.disconnect()
