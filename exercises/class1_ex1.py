from netmiko import ConnectHandler
import yaml

with open("/home/ponnathan/.netmiko.yml") as yaml_file:
    devices = yaml.safe_load(yaml_file)

dev_name = "nxos1"
nxos_device = devices[dev_name]
dev_conn = ConnectHandler(**nxos_device)


print(dev_conn.find_prompt())

print("device prompt verified")

dev_conn.disconnect()

print("Connection closed")

